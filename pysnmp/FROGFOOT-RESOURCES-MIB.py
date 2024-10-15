# SNMP MIB module (FROGFOOT-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FROGFOOT-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:26 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

resources = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TableIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Frogfoot_ObjectIdentity = ObjectIdentity
frogfoot = _Frogfoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002)
)
_Servers_ObjectIdentity = ObjectIdentity
servers = _Servers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1)
)
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 1)
)
_MemTotal_Type = Gauge32
_MemTotal_Object = MibScalar
memTotal = _MemTotal_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 1, 1),
    _MemTotal_Type()
)
memTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotal.setStatus("current")
_MemFree_Type = Gauge32
_MemFree_Object = MibScalar
memFree = _MemFree_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 1, 2),
    _MemFree_Type()
)
memFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFree.setStatus("current")
_MemBuffer_Type = Gauge32
_MemBuffer_Object = MibScalar
memBuffer = _MemBuffer_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 1, 3),
    _MemBuffer_Type()
)
memBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBuffer.setStatus("current")
_MemCache_Type = Gauge32
_MemCache_Object = MibScalar
memCache = _MemCache_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 1, 4),
    _MemCache_Type()
)
memCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCache.setStatus("current")
_Swap_ObjectIdentity = ObjectIdentity
swap = _Swap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 2)
)
_SwapTotal_Type = Gauge32
_SwapTotal_Object = MibScalar
swapTotal = _SwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 2, 1),
    _SwapTotal_Type()
)
swapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapTotal.setStatus("current")
_SwapFree_Type = Gauge32
_SwapFree_Object = MibScalar
swapFree = _SwapFree_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 2, 2),
    _SwapFree_Type()
)
swapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapFree.setStatus("current")
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3)
)
_DiskNumber_Type = Integer32
_DiskNumber_Object = MibScalar
diskNumber = _DiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 1),
    _DiskNumber_Type()
)
diskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNumber.setStatus("current")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1)
)
diskEntry.setIndexNames(
    (0, "FROGFOOT-RESOURCES-MIB", "diskIndex"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")
_DiskIndex_Type = TableIndex
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 1),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskIndex.setStatus("current")
_DiskDev_Type = DisplayString
_DiskDev_Object = MibTableColumn
diskDev = _DiskDev_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 2),
    _DiskDev_Type()
)
diskDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDev.setStatus("current")
_DiskDir_Type = DisplayString
_DiskDir_Object = MibTableColumn
diskDir = _DiskDir_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 3),
    _DiskDir_Type()
)
diskDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDir.setStatus("current")


class _DiskFSType_Type(Integer32):
    """Custom type diskFSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("adfs", 1),
          ("affs", 2),
          ("coda", 3),
          ("cramfs", 4),
          ("ext2", 5),
          ("hpfs", 6),
          ("iso9660", 7),
          ("jffs2", 8),
          ("jfs", 9),
          ("minix", 10),
          ("msdos", 11),
          ("ncpfs", 12),
          ("nfs", 13),
          ("ntfs", 14),
          ("qnx4", 15),
          ("reiserfs", 16),
          ("romfs", 17),
          ("smbfs", 18),
          ("sysv", 19),
          ("tmpfs", 20),
          ("udf", 21),
          ("ufs", 22),
          ("unknown", 0),
          ("vxfs", 23),
          ("xfs", 24))
    )


_DiskFSType_Type.__name__ = "Integer32"
_DiskFSType_Object = MibTableColumn
diskFSType = _DiskFSType_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 4),
    _DiskFSType_Type()
)
diskFSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFSType.setStatus("current")
_DiskTotal_Type = Gauge32
_DiskTotal_Object = MibTableColumn
diskTotal = _DiskTotal_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 5),
    _DiskTotal_Type()
)
diskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotal.setStatus("current")
_DiskFree_Type = Gauge32
_DiskFree_Object = MibTableColumn
diskFree = _DiskFree_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 6),
    _DiskFree_Type()
)
diskFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFree.setStatus("current")
_Load_ObjectIdentity = ObjectIdentity
load = _Load_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4)
)
_LoadNumber_Type = Integer32
_LoadNumber_Object = MibScalar
loadNumber = _LoadNumber_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 1),
    _LoadNumber_Type()
)
loadNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadNumber.setStatus("current")
_LoadTable_Object = MibTable
loadTable = _LoadTable_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    loadTable.setStatus("current")
_LoadEntry_Object = MibTableRow
loadEntry = _LoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 2, 1)
)
loadEntry.setIndexNames(
    (0, "FROGFOOT-RESOURCES-MIB", "loadIndex"),
)
if mibBuilder.loadTexts:
    loadEntry.setStatus("current")
_LoadIndex_Type = TableIndex
_LoadIndex_Object = MibTableColumn
loadIndex = _LoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 2, 1, 1),
    _LoadIndex_Type()
)
loadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadIndex.setStatus("current")
_LoadDescr_Type = DisplayString
_LoadDescr_Object = MibTableColumn
loadDescr = _LoadDescr_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 2, 1, 2),
    _LoadDescr_Type()
)
loadDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadDescr.setStatus("current")
_LoadValue_Type = Gauge32
_LoadValue_Object = MibTableColumn
loadValue = _LoadValue_Object(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 2, 1, 3),
    _LoadValue_Type()
)
loadValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadValue.setStatus("current")
_ResMIB_ObjectIdentity = ObjectIdentity
resMIB = _ResMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31)
)
_ResMIBObjects_ObjectIdentity = ObjectIdentity
resMIBObjects = _ResMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 1)
)
_ResConformance_ObjectIdentity = ObjectIdentity
resConformance = _ResConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2)
)
_ResGroups_ObjectIdentity = ObjectIdentity
resGroups = _ResGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 1)
)
_ResCompliances_ObjectIdentity = ObjectIdentity
resCompliances = _ResCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 2)
)

# Managed Objects groups

resMemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 1, 1)
)
resMemGroup.setObjects(
      *(("FROGFOOT-RESOURCES-MIB", "memTotal"),
        ("FROGFOOT-RESOURCES-MIB", "memFree"),
        ("FROGFOOT-RESOURCES-MIB", "memBuffer"),
        ("FROGFOOT-RESOURCES-MIB", "memCache"))
)
if mibBuilder.loadTexts:
    resMemGroup.setStatus("current")

resSwapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 1, 2)
)
resSwapGroup.setObjects(
      *(("FROGFOOT-RESOURCES-MIB", "swapTotal"),
        ("FROGFOOT-RESOURCES-MIB", "swapFree"))
)
if mibBuilder.loadTexts:
    resSwapGroup.setStatus("current")

resDiskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 1, 3)
)
resDiskGroup.setObjects(
      *(("FROGFOOT-RESOURCES-MIB", "diskNumber"),
        ("FROGFOOT-RESOURCES-MIB", "diskDev"),
        ("FROGFOOT-RESOURCES-MIB", "diskDir"),
        ("FROGFOOT-RESOURCES-MIB", "diskFSType"),
        ("FROGFOOT-RESOURCES-MIB", "diskTotal"),
        ("FROGFOOT-RESOURCES-MIB", "diskFree"))
)
if mibBuilder.loadTexts:
    resDiskGroup.setStatus("current")

resLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 1, 4)
)
resLoadGroup.setObjects(
      *(("FROGFOOT-RESOURCES-MIB", "loadNumber"),
        ("FROGFOOT-RESOURCES-MIB", "loadDescr"),
        ("FROGFOOT-RESOURCES-MIB", "loadValue"))
)
if mibBuilder.loadTexts:
    resLoadGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

resCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 2, 1)
)
if mibBuilder.loadTexts:
    resCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FROGFOOT-RESOURCES-MIB",
    **{"TableIndex": TableIndex,
       "frogfoot": frogfoot,
       "servers": servers,
       "system": system,
       "resources": resources,
       "memory": memory,
       "memTotal": memTotal,
       "memFree": memFree,
       "memBuffer": memBuffer,
       "memCache": memCache,
       "swap": swap,
       "swapTotal": swapTotal,
       "swapFree": swapFree,
       "storage": storage,
       "diskNumber": diskNumber,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskIndex": diskIndex,
       "diskDev": diskDev,
       "diskDir": diskDir,
       "diskFSType": diskFSType,
       "diskTotal": diskTotal,
       "diskFree": diskFree,
       "load": load,
       "loadNumber": loadNumber,
       "loadTable": loadTable,
       "loadEntry": loadEntry,
       "loadIndex": loadIndex,
       "loadDescr": loadDescr,
       "loadValue": loadValue,
       "resMIB": resMIB,
       "resMIBObjects": resMIBObjects,
       "resConformance": resConformance,
       "resGroups": resGroups,
       "resMemGroup": resMemGroup,
       "resSwapGroup": resSwapGroup,
       "resDiskGroup": resDiskGroup,
       "resLoadGroup": resLoadGroup,
       "resCompliances": resCompliances,
       "resCompliance": resCompliance}
)
