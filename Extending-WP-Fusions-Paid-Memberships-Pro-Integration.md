# Extending WP Fusion's Paid Memberships Pro Integration

- Source: https://claude.ai/share/92837c16-1db2-4358-9fb4-0ccafc9397dc
- Author: Jack
- Created: 2025-02-27
- Messages: 4

---

## Human

Our WP Fusion integration with Paid Memberships Pro (https://wpfusion.com/documentation/membership/paid-memberships-pro/ ) currently allows syncing fields like Membership Status and Expiration Date with the customer's CRM. This is currently configured sitewide, which means it's not compatible with Paid Memberships Pro's new feature that allows members to have multiple concurrent memberships. We'd like to extend the integration to support adding a new settings panel to the PMPro membership configuration page where users can map fields with their CRM specific to that membership level. When a member signs up at that level, the fields should be synced to their contact record in your CRM. You can find the Paid Memberships Pro plugin here: https://github.com/strangerstudios/paid-memberships-pro . I have uploaded WP Fusion's existing PMPro integration class. Can you please propose a solution, or let me know if you require more information or code examples before proceeding?

---

## Assistant

I'll help you extend your WP Fusion integration with Paid Memberships Pro to support per-membership level field mapping for CRMs. Let me analyze what we need to accomplish based on the information you've provided.

First, I'll outline what I understand about the current situation and desired outcome:

1. Currently, your WP Fusion integration syncs membership data (status, expiration date) to CRMs, but this is configured sitewide
2. PMPro now supports multiple concurrent memberships for users
3. You need to extend the integration to allow per-membership level field mapping
4. This requires adding a settings panel to the PMPro membership configuration page

To implement this effectively, we'll need to:

1. Create a new settings panel on the membership level admin page
2. Store per-membership level field mappings
3. Update the syncing logic to use level-specific mappings when available

Let me review the uploaded file to understand the current implementation better. Then I'll provide a solution that maintains backward compatibility while adding the new functionality.

Could you please confirm what file you've uploaded? I don't see it in our current conversation. If you could share your existing PMPro integration class, I can provide a more specific implementation plan. 

Specifically, these details would help:
- How the current field mapping is structured
- The hooks you're using for sync events
- How you're currently storing the global settings

---

## Human

I wasn't able to upload the whole file due to the length. We currently hook into the `pmpro_membership_level_before_content_settings` action to add our settings to the membership level. Here's an example from our WooCommerce subscriptions integration showing how we render the CRM field select dropdown:


```
		echo '<p class="form-field"><label><strong>' . esc_html__( 'Subscription Fields', 'wp-fusion' ) . '</strong></label></p>';

		$crm_fields = $this->get_product_subscription_crm_fields();

		$fields = wp_fusion()->settings->get( 'contact_fields' );

		foreach ( $crm_fields as $key => $value ) {

			$id = $key . '_' . $post_id;

			echo '<p class="form-field"><label for="' . esc_attr( $id ) . '">' . esc_html( $value['name'] ) . '</label>';

			wpf_render_crm_field_select(
				isset( $fields[ $id ] ) ? $fields[ $id ]['crm_field'] : false,
				'wpf_settings_woo_crm_fields',
				$id
			);
			echo '</p>';
		}
```


We already have a function `sync_membership_level_fields()` which runs whenever the fields need to be synced for a membership. Here is that function:


```
	public function sync_membership_level_fields( $user_id, $membership_level ) {

		if ( ! empty( $membership_level ) ) {

			if ( ! isset( $membership_level->startdate ) ) {
				$membership_level->startdate = time(); // sometimes this isn't set yet during signup.
			} elseif ( ! is_numeric( $membership_level->startdate ) ) {
				$membership_level->startdate = strtotime( $membership_level->startdate );
			}

			$nextdate = strtotime( '+' . $membership_level->cycle_number . ' ' . $membership_level->cycle_period, intval( $membership_level->startdate ) );

			$update_data = array(
				'pmpro_status'             => $this->get_membership_level_status( $user_id, $membership_level->id ),
				'pmpro_start_date'         => gmdate( get_option( 'date_format' ), intval( $membership_level->startdate ) ),
				'pmpro_next_payment_date'  => gmdate( get_option( 'date_format' ), intval( $nextdate ) ),
				'pmpro_membership_level'   => $membership_level->name,
				'pmpro_subscription_price' => $membership_level->billing_amount,
			);

			if ( ! empty( $membership_level->enddate ) ) {

				if ( ! is_numeric( $membership_level->enddate ) ) {
					$membership_level->enddate = strtotime( $membership_level->enddate );
				}

				// Take it out of UNIX time.
				$update_data['pmpro_expiration_date'] = gmdate( get_option( 'date_format' ), intval( $membership_level->enddate ) );

			} else {

				// Never expires.
				$update_data['pmpro_expiration_date'] = null;

			}

			// Approvals

			$approval_status = get_user_meta( $user_id, 'pmpro_approval_' . $membership_level->id, true );

			if ( ! empty( $approval_status ) ) {
				$update_data['pmpro_approval'] = $approval_status['status'];
			}
		} else {

			// No level.

			$update_data = array(
				'pmpro_membership_level'   => null,
				'pmpro_expiration_date'    => null,
				'pmpro_subscription_price' => null,
				'pmpro_next_payment_date'  => null,
				'pmpro_status'             => $this->get_membership_level_status( $user_id ),
			);

		}

		// Send the updated data
		wp_fusion()->user->push_user_meta( $user_id, $update_data );
	}
```

Does that give you enough to go on to complete the feature request?

---

## Assistant

Thanks for providing those code snippets! Now I understand how your current integration works. With these details, I can propose a solution for supporting per-membership level field mapping in WP Fusion for Paid Memberships Pro.

Here's my implementation plan:

<antArtifact identifier="pmpro-per-level-integration" type="application/vnd.ant.code" language="php" title="WP Fusion PMPro Per-Level Field Mapping">
/**
 * Add per-level CRM field mappings to the membership level settings
 *
 * @since 3.40.0 (or your next version number)
 *
 * @param int $level_id The membership level ID
 */
public function add_level_settings( $level_id ) {

	// Continue showing existing settings and global message
	echo '<tr class="wpf-settings-row">
		<th scope="row" valign="top"><label>' . __( 'WP Fusion Settings', 'wp-fusion' ) . '</label></th>
		<td><p class="description">' . sprintf( __( 'For more information on these settings, %1$ssee our documentation%2$s.', 'wp-fusion' ), '<a href="https://wpfusion.com/documentation/membership/paid-memberships-pro/" target="_blank">', '</a>' ) . '</p></td>
	</tr>';

	// Add new section for per-level CRM field mappings
	echo '<tr class="wpf-settings-row">
		<th scope="row" valign="top"><label>' . __( 'Field Mapping', 'wp-fusion' ) . '</label></th>
		<td><p class="description">' . __( 'These fields will be synced to the CRM when a member registers for this specific level.', 'wp-fusion' ) . '</p>';
	
	$level_fields = $this->get_membership_level_fields();
	$saved_mappings = get_option( 'wpf_pmpro_level_' . $level_id . '_fields', array() );
	
	echo '<table class="form-table wpf-level-fields-table">';
	
	foreach ( $level_fields as $key => $field ) {
		$field_id = $key . '_level_' . $level_id;
		$saved_value = isset( $saved_mappings[$key] ) ? $saved_mappings[$key] : false;
		
		echo '<tr>
			<th scope="row"><label for="' . esc_attr( $field_id ) . '">' . esc_html( $field['name'] ) . '</label></th>
			<td>';
		
		wpf_render_crm_field_select(
			$saved_value,
			'wpf_pmpro_level_fields',
			$field_id
		);
		
		echo '</td>
		</tr>';
	}
	
	echo '</table></td>
	</tr>';
}

/**
 * Get available membership level fields for mapping
 *
 * @since 3.40.0
 *
 * @return array The available fields
 */
public function get_membership_level_fields() {
	return array(
		'pmpro_status' => array(
			'name' => __( 'Membership Status', 'wp-fusion' ),
		),
		'pmpro_start_date' => array(
			'name' => __( 'Start Date', 'wp-fusion' ),
		),
		'pmpro_expiration_date' => array(
			'name' => __( 'Expiration Date', 'wp-fusion' ),
		),
		'pmpro_next_payment_date' => array(
			'name' => __( 'Next Payment Date', 'wp-fusion' ),
		),
		'pmpro_membership_level' => array(
			'name' => __( 'Membership Level Name', 'wp-fusion' ),
		),
		'pmpro_subscription_price' => array(
			'name' => __( 'Subscription Price', 'wp-fusion' ),
		),
		'pmpro_approval' => array(
			'name' => __( 'Approval Status', 'wp-fusion' ),
		),
	);
}

/**
 * Save the membership level field mappings
 *
 * @since 3.40.0
 *
 * @param int $level_id The membership level ID
 */
public function save_level_settings( $level_id ) {
	
	// Save the field mappings
	if ( isset( $_POST['wpf_pmpro_level_fields'] ) ) {
		$field_mappings = array();
		
		foreach ( $_POST['wpf_pmpro_level_fields'] as $field_key => $crm_field ) {
			// Extract the field name from the combined key (field_level_id)
			$parts = explode('_level_', $field_key);
			if ( count($parts) == 2 && $parts[1] == $level_id ) {
				if ( ! empty( $crm_field ) ) {
					$field_mappings[$parts[0]] = $crm_field;
				}
			}
		}
		
		update_option( 'wpf_pmpro_level_' . $level_id . '_fields', $field_mappings );
	}
}

/**
 * Modify the membership level sync function to support per-level field mappings
 *
 * @since 3.40.0
 *
 * @param int   $user_id         The user ID
 * @param object $membership_level The membership level object
 */
public function sync_membership_level_fields( $user_id, $membership_level ) {

	if ( ! empty( $membership_level ) ) {

		if ( ! isset( $membership_level->startdate ) ) {
			$membership_level->startdate = time(); // sometimes this isn't set yet during signup.
		} elseif ( ! is_numeric( $membership_level->startdate ) ) {
			$membership_level->startdate = strtotime( $membership_level->startdate );
		}

		$nextdate = strtotime( '+' . $membership_level->cycle_number . ' ' . $membership_level->cycle_period, intval( $membership_level->startdate ) );

		// Prepare all the available data
		$all_data = array(
			'pmpro_status'             => $this->get_membership_level_status( $user_id, $membership_level->id ),
			'pmpro_start_date'         => gmdate( get_option( 'date_format' ), intval( $membership_level->startdate ) ),
			'pmpro_next_payment_date'  => gmdate( get_option( 'date_format' ), intval( $nextdate ) ),
			'pmpro_membership_level'   => $membership_level->name,
			'pmpro_subscription_price' => $membership_level->billing_amount,
		);

		if ( ! empty( $membership_level->enddate ) ) {
			if ( ! is_numeric( $membership_level->enddate ) ) {
				$membership_level->enddate = strtotime( $membership_level->enddate );
			}
			$all_data['pmpro_expiration_date'] = gmdate( get_option( 'date_format' ), intval( $membership_level->enddate ) );
		} else {
			// Never expires.
			$all_data['pmpro_expiration_date'] = null;
		}

		// Approvals
		$approval_status = get_user_meta( $user_id, 'pmpro_approval_' . $membership_level->id, true );
		if ( ! empty( $approval_status ) ) {
			$all_data['pmpro_approval'] = $approval_status['status'];
		}
		
		// Get per-level field mappings
		$level_mappings = get_option( 'wpf_pmpro_level_' . $membership_level->id . '_fields', array() );
		
		// Get global field mappings
		$fields = wp_fusion()->settings->get( 'contact_fields' );
		
		$update_data = array();
		
		// First check level-specific mappings
		if ( ! empty( $level_mappings ) ) {
			foreach ( $level_mappings as $field_key => $crm_field ) {
				if ( isset( $all_data[$field_key] ) && ! empty( $crm_field ) ) {
					$update_data[$field_key] = $all_data[$field_key];
				}
			}
		}
		
		// Then check global mappings for any fields not already set
		foreach ( $all_data as $field_key => $value ) {
			// If we already have a level-specific mapping, skip
			if ( isset( $update_data[$field_key] ) ) {
				continue;
			}
			
			// Check if there's a global mapping
			if ( isset( $fields[$field_key] ) && ! empty( $fields[$field_key]['crm_field'] ) ) {
				$update_data[$field_key] = $value;
			}
		}
		
	} else {
		// No level, use global settings
		$update_data = array(
			'pmpro_membership_level'   => null,
			'pmpro_expiration_date'    => null,
			'pmpro_subscription_price' => null,
			'pmpro_next_payment_date'  => null,
			'pmpro_status'             => $this->get_membership_level_status( $user_id ),
		);
	}

	// Send the updated data
	wp_fusion()->user->push_user_meta( $user_id, $update_data );
}

/**
 * Set up hooks to add and save settings
 *
 * @since 3.40.0
 */
public function init() {
    // Add existing hooks
    
    // Add new hooks for per-level settings
    add_action( 'pmpro_membership_level_before_content_settings', array( $this, 'add_level_settings' ) );
    add_action( 'pmpro_save_membership_level', array( $this, 'save_level_settings' ) );
}
</antArtifact>

## Implementation Details

Based on the code samples you provided, I've developed a solution that allows for per-membership level field mapping. Here's how it works:

1. **New Settings Panel**: Added a field mapping table to the membership level settings page that shows all available PMPro fields.

2. **Storage**: The mappings are stored in a unique option for each level: `wpf_pmpro_level_{level_id}_fields`.

3. **Sync Logic**: Modified the `sync_membership_level_fields()` function to:
   - First prepare all available data
   - Check for level-specific field mappings
   - Fall back to global mappings for any fields not mapped at the level
   - Only push fields that have valid mappings

4. **Backward Compatibility**: The solution maintains compatibility with the existing global field mappings while adding the per-level functionality.

## Integration Steps

To implement this solution:

1. Add the provided code to your PMPro integration class
2. Update your class constructor or init method to include the new action hooks
3. Test the interface on a membership level edit page
4. Verify that field mappings are saved correctly and synced for member signups

## Additional Considerations

1. **Data Format**: The level-specific mappings are stored as an array with field keys as the keys and CRM field IDs as the values.

2. **UI Integration**: The field mapping UI is integrated with your existing settings panel for PMPro.

3. **Multiple Memberships**: When a user has multiple memberships, each membership's fields will be synced according to its specific mappings.

Would you like me to explain any part of the implementation in more detail or make any adjustments to the approach?
