# Deleting specific files in Ubuntu

- Source: https://claude.ai/share/1545d277-b20e-47fd-9f46-0476f790ee83
- Author: Johannes
- Created: 2025-03-03
- Messages: 6

---

## Human

In an Ubuntu console, how can I delete all files in the current folder which have the shape
stratum_euler*_[2,3,4,5,6,7,8,9].pkl.bz2
where the brackets means: one of these digits?

---

## Assistant

Here's the command you can use:

```bash
rm stratum_euler*_[2-9].pkl.bz2
```

This command will match and delete any file that:
- Starts with "stratum_euler"
- Has any characters in between (represented by *)
- Has an underscore followed by a single digit from 2 to 9
- Ends with ".pkl.bz2"

If you want to be cautious, you can first preview which files will be deleted by using `ls` with the same pattern:

```bash
ls stratum_euler*_[2-9].pkl.bz2
```

---

## Human

jo314@JoSAsus:~/.sage$ ls stratum_euler*_[2-9].pkl.bz2
ls: cannot access 'stratum_euler*_[2-9].pkl.bz2': No such file or directory

---

## Assistant

The error suggests the files might not match the pattern exactly as written. Let's check what files actually exist in the directory:

```bash
ls stratum_euler*
```

This will show us all files that start with "stratum_euler" so we can see the exact pattern. Could you run this and share what you see? There might be additional characters or a different format in the actual filenames that we need to account for in our pattern.

---

## Human

don't you have to specify that you look in the current folder . ?

---

## Assistant

No, you don't have to specify the current folder with a dot (.) - when you run commands like `ls` or `rm` without specifying a path, they automatically operate on the current directory.

However, if you want to be explicit, you can certainly write:

```bash
ls ./stratum_euler*
```

Both commands will give you the same result. The `.` is implicit when no path is specified.
