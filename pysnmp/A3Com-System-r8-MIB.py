# SNMP MIB module (A3Com-System-r8-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3Com-System-r8-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:26 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "RFC1286-MIB",
    "MacAddress")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComSys_ObjectIdentity = ObjectIdentity
a3ComSys = _A3ComSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13)
)
_A3ComSysID_ObjectIdentity = ObjectIdentity
a3ComSysID = _A3ComSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 1)
)
_A3sysVersion_Type = DisplayString
_A3sysVersion_Object = MibScalar
a3sysVersion = _A3sysVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 1, 1),
    _A3sysVersion_Type()
)
a3sysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysVersion.setStatus("mandatory")
_A3sysPlatformDescr_Type = DisplayString
_A3sysPlatformDescr_Object = MibScalar
a3sysPlatformDescr = _A3sysPlatformDescr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 1, 2),
    _A3sysPlatformDescr_Type()
)
a3sysPlatformDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysPlatformDescr.setStatus("mandatory")
_A3sysPlatformID_Type = ObjectIdentifier
_A3sysPlatformID_Object = MibScalar
a3sysPlatformID = _A3sysPlatformID_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 1, 3),
    _A3sysPlatformID_Type()
)
a3sysPlatformID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysPlatformID.setStatus("mandatory")


class _A3sysCallerID_Type(DisplayString):
    """Custom type a3sysCallerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3sysCallerID_Type.__name__ = "DisplayString"
_A3sysCallerID_Object = MibScalar
a3sysCallerID = _A3sysCallerID_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 1, 4),
    _A3sysCallerID_Type()
)
a3sysCallerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysCallerID.setStatus("mandatory")
_A3ComChip_ObjectIdentity = ObjectIdentity
a3ComChip = _A3ComChip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 2)
)
_A3sysChipTable_Object = MibTable
a3sysChipTable = _A3sysChipTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 2, 1)
)
if mibBuilder.loadTexts:
    a3sysChipTable.setStatus("mandatory")
_A3sysChipEntry_Object = MibTableRow
a3sysChipEntry = _A3sysChipEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 2, 1, 1)
)
a3sysChipEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysChipSlotIndex"),
    (0, "A3Com-System-r8-MIB", "a3sysChipIndex"),
)
if mibBuilder.loadTexts:
    a3sysChipEntry.setStatus("mandatory")
_A3sysChipSlotIndex_Type = Integer32
_A3sysChipSlotIndex_Object = MibTableColumn
a3sysChipSlotIndex = _A3sysChipSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 2, 1, 1, 1),
    _A3sysChipSlotIndex_Type()
)
a3sysChipSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysChipSlotIndex.setStatus("mandatory")
_A3sysChipIndex_Type = Integer32
_A3sysChipIndex_Object = MibTableColumn
a3sysChipIndex = _A3sysChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 2, 1, 1, 2),
    _A3sysChipIndex_Type()
)
a3sysChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysChipIndex.setStatus("mandatory")
_A3sysChipName_Type = DisplayString
_A3sysChipName_Object = MibTableColumn
a3sysChipName = _A3sysChipName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 2, 1, 1, 3),
    _A3sysChipName_Type()
)
a3sysChipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysChipName.setStatus("mandatory")
_A3sysChipDescr_Type = DisplayString
_A3sysChipDescr_Object = MibTableColumn
a3sysChipDescr = _A3sysChipDescr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 2, 1, 1, 4),
    _A3sysChipDescr_Type()
)
a3sysChipDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysChipDescr.setStatus("mandatory")
_A3ComMem_ObjectIdentity = ObjectIdentity
a3ComMem = _A3ComMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 3)
)
_A3sysMemTable_Object = MibTable
a3sysMemTable = _A3sysMemTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 3, 1)
)
if mibBuilder.loadTexts:
    a3sysMemTable.setStatus("mandatory")
_A3sysMemEntry_Object = MibTableRow
a3sysMemEntry = _A3sysMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 3, 1, 1)
)
a3sysMemEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysMemSlotIndex"),
    (0, "A3Com-System-r8-MIB", "a3sysMemIndex"),
)
if mibBuilder.loadTexts:
    a3sysMemEntry.setStatus("mandatory")
_A3sysMemSlotIndex_Type = Integer32
_A3sysMemSlotIndex_Object = MibTableColumn
a3sysMemSlotIndex = _A3sysMemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 3, 1, 1, 1),
    _A3sysMemSlotIndex_Type()
)
a3sysMemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysMemSlotIndex.setStatus("mandatory")
_A3sysMemIndex_Type = Integer32
_A3sysMemIndex_Object = MibTableColumn
a3sysMemIndex = _A3sysMemIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 3, 1, 1, 2),
    _A3sysMemIndex_Type()
)
a3sysMemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysMemIndex.setStatus("mandatory")


class _A3sysMemType_Type(Integer32):
    """Custom type a3sysMemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ram-data", 3),
          ("ram-instruction", 2),
          ("ram-shared", 4),
          ("ram-total", 7),
          ("rom-eeprom", 6),
          ("rom-fprom", 5))
    )


_A3sysMemType_Type.__name__ = "Integer32"
_A3sysMemType_Object = MibTableColumn
a3sysMemType = _A3sysMemType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 3, 1, 1, 3),
    _A3sysMemType_Type()
)
a3sysMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysMemType.setStatus("mandatory")
_A3sysMemStartAdd_Type = Integer32
_A3sysMemStartAdd_Object = MibTableColumn
a3sysMemStartAdd = _A3sysMemStartAdd_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 3, 1, 1, 4),
    _A3sysMemStartAdd_Type()
)
a3sysMemStartAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysMemStartAdd.setStatus("mandatory")
_A3sysMemSize_Type = Integer32
_A3sysMemSize_Object = MibTableColumn
a3sysMemSize = _A3sysMemSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 3, 1, 1, 5),
    _A3sysMemSize_Type()
)
a3sysMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysMemSize.setStatus("mandatory")
_A3ComBrd_ObjectIdentity = ObjectIdentity
a3ComBrd = _A3ComBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 4)
)
_A3sysSlotNumber_Type = Integer32
_A3sysSlotNumber_Object = MibScalar
a3sysSlotNumber = _A3sysSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 4, 1),
    _A3sysSlotNumber_Type()
)
a3sysSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysSlotNumber.setStatus("mandatory")
_A3sysBrdTable_Object = MibTable
a3sysBrdTable = _A3sysBrdTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 4, 2)
)
if mibBuilder.loadTexts:
    a3sysBrdTable.setStatus("mandatory")
_A3sysBrdEntry_Object = MibTableRow
a3sysBrdEntry = _A3sysBrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 4, 2, 1)
)
a3sysBrdEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysSlotIndex"),
)
if mibBuilder.loadTexts:
    a3sysBrdEntry.setStatus("mandatory")
_A3sysSlotIndex_Type = Integer32
_A3sysSlotIndex_Object = MibTableColumn
a3sysSlotIndex = _A3sysSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 4, 2, 1, 1),
    _A3sysSlotIndex_Type()
)
a3sysSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysSlotIndex.setStatus("mandatory")
_A3sysBrdDescr_Type = DisplayString
_A3sysBrdDescr_Object = MibTableColumn
a3sysBrdDescr = _A3sysBrdDescr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 4, 2, 1, 2),
    _A3sysBrdDescr_Type()
)
a3sysBrdDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysBrdDescr.setStatus("mandatory")
_A3sysBrdPathCapacity_Type = Integer32
_A3sysBrdPathCapacity_Object = MibTableColumn
a3sysBrdPathCapacity = _A3sysBrdPathCapacity_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 4, 2, 1, 3),
    _A3sysBrdPathCapacity_Type()
)
a3sysBrdPathCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysBrdPathCapacity.setStatus("mandatory")
_A3sysBrdOID_Type = ObjectIdentifier
_A3sysBrdOID_Object = MibTableColumn
a3sysBrdOID = _A3sysBrdOID_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 4, 2, 1, 4),
    _A3sysBrdOID_Type()
)
a3sysBrdOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysBrdOID.setStatus("mandatory")


class _A3sysBrdReset_Type(Integer32):
    """Custom type a3sysBrdReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_A3sysBrdReset_Type.__name__ = "Integer32"
_A3sysBrdReset_Object = MibTableColumn
a3sysBrdReset = _A3sysBrdReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 4, 2, 1, 5),
    _A3sysBrdReset_Type()
)
a3sysBrdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysBrdReset.setStatus("mandatory")
_A3sysBrdFwVers_Type = ObjectIdentifier
_A3sysBrdFwVers_Object = MibTableColumn
a3sysBrdFwVers = _A3sysBrdFwVers_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 4, 2, 1, 6),
    _A3sysBrdFwVers_Type()
)
a3sysBrdFwVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysBrdFwVers.setStatus("mandatory")
_A3ComAudit_ObjectIdentity = ObjectIdentity
a3ComAudit = _A3ComAudit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 5)
)


class _A3sysAuditTrailType_Type(Integer32):
    """Custom type a3sysAuditTrailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("universal", 2))
    )


_A3sysAuditTrailType_Type.__name__ = "Integer32"
_A3sysAuditTrailType_Object = MibScalar
a3sysAuditTrailType = _A3sysAuditTrailType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 5, 1),
    _A3sysAuditTrailType_Type()
)
a3sysAuditTrailType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysAuditTrailType.setStatus("mandatory")
_A3sysLogServerAddress_Type = IpAddress
_A3sysLogServerAddress_Object = MibScalar
a3sysLogServerAddress = _A3sysLogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 5, 2),
    _A3sysLogServerAddress_Type()
)
a3sysLogServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysLogServerAddress.setStatus("deprecated")
_A3ComTime_ObjectIdentity = ObjectIdentity
a3ComTime = _A3ComTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 6)
)
_A3sysDate_Type = DisplayString
_A3sysDate_Object = MibScalar
a3sysDate = _A3sysDate_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 6, 1),
    _A3sysDate_Type()
)
a3sysDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysDate.setStatus("mandatory")


class _A3sysDSTime_Type(Integer32):
    """Custom type a3sysDSTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 120),
    )


_A3sysDSTime_Type.__name__ = "Integer32"
_A3sysDSTime_Object = MibScalar
a3sysDSTime = _A3sysDSTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 6, 2),
    _A3sysDSTime_Type()
)
a3sysDSTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysDSTime.setStatus("mandatory")


class _A3sysTimeZone_Type(Integer32):
    """Custom type a3sysTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 720),
    )


_A3sysTimeZone_Type.__name__ = "Integer32"
_A3sysTimeZone_Object = MibScalar
a3sysTimeZone = _A3sysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 6, 3),
    _A3sysTimeZone_Type()
)
a3sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysTimeZone.setStatus("mandatory")
_A3ComAccCtl_ObjectIdentity = ObjectIdentity
a3ComAccCtl = _A3ComAccCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7)
)


class _A3sysRemoteAccess_Type(Integer32):
    """Custom type a3sysRemoteAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3sysRemoteAccess_Type.__name__ = "Integer32"
_A3sysRemoteAccess_Object = MibScalar
a3sysRemoteAccess = _A3sysRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 1),
    _A3sysRemoteAccess_Type()
)
a3sysRemoteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysRemoteAccess.setStatus("mandatory")


class _A3sysTelnetAccess_Type(Integer32):
    """Custom type a3sysTelnetAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3sysTelnetAccess_Type.__name__ = "Integer32"
_A3sysTelnetAccess_Object = MibScalar
a3sysTelnetAccess = _A3sysTelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 2),
    _A3sysTelnetAccess_Type()
)
a3sysTelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysTelnetAccess.setStatus("mandatory")


class _A3sysConsoleAccess_Type(Integer32):
    """Custom type a3sysConsoleAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3sysConsoleAccess_Type.__name__ = "Integer32"
_A3sysConsoleAccess_Object = MibScalar
a3sysConsoleAccess = _A3sysConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 3),
    _A3sysConsoleAccess_Type()
)
a3sysConsoleAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysConsoleAccess.setStatus("mandatory")


class _A3sysSNMPAccess_Type(Integer32):
    """Custom type a3sysSNMPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabledNoTraps", 4),
          ("disabledTraps", 3),
          ("enabledNoTraps", 2),
          ("enabledTraps", 1))
    )


_A3sysSNMPAccess_Type.__name__ = "Integer32"
_A3sysSNMPAccess_Object = MibScalar
a3sysSNMPAccess = _A3sysSNMPAccess_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 4),
    _A3sysSNMPAccess_Type()
)
a3sysSNMPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysSNMPAccess.setStatus("mandatory")
_A3sysSNMPCommTable_Object = MibTable
a3sysSNMPCommTable = _A3sysSNMPCommTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 5)
)
if mibBuilder.loadTexts:
    a3sysSNMPCommTable.setStatus("mandatory")
_A3sysSNMPCommEntry_Object = MibTableRow
a3sysSNMPCommEntry = _A3sysSNMPCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 5, 1)
)
a3sysSNMPCommEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysSNMPCommString"),
)
if mibBuilder.loadTexts:
    a3sysSNMPCommEntry.setStatus("mandatory")


class _A3sysSNMPCommString_Type(DisplayString):
    """Custom type a3sysSNMPCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_A3sysSNMPCommString_Type.__name__ = "DisplayString"
_A3sysSNMPCommString_Object = MibTableColumn
a3sysSNMPCommString = _A3sysSNMPCommString_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 5, 1, 1),
    _A3sysSNMPCommString_Type()
)
a3sysSNMPCommString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysSNMPCommString.setStatus("mandatory")


class _A3sysSNMPCommAccess_Type(Integer32):
    """Custom type a3sysSNMPCommAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_A3sysSNMPCommAccess_Type.__name__ = "Integer32"
_A3sysSNMPCommAccess_Object = MibTableColumn
a3sysSNMPCommAccess = _A3sysSNMPCommAccess_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 5, 1, 2),
    _A3sysSNMPCommAccess_Type()
)
a3sysSNMPCommAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysSNMPCommAccess.setStatus("mandatory")


class _A3sysSNMPCommTrap_Type(Integer32):
    """Custom type a3sysSNMPCommTrap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allTraps", 3),
          ("authenOnly", 2),
          ("genericOnly", 1),
          ("noTraps", 4))
    )


_A3sysSNMPCommTrap_Type.__name__ = "Integer32"
_A3sysSNMPCommTrap_Object = MibTableColumn
a3sysSNMPCommTrap = _A3sysSNMPCommTrap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 5, 1, 3),
    _A3sysSNMPCommTrap_Type()
)
a3sysSNMPCommTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysSNMPCommTrap.setStatus("mandatory")
_A3sysSNMPCommStatus_Type = RowStatus
_A3sysSNMPCommStatus_Object = MibTableColumn
a3sysSNMPCommStatus = _A3sysSNMPCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 5, 1, 4),
    _A3sysSNMPCommStatus_Type()
)
a3sysSNMPCommStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysSNMPCommStatus.setStatus("mandatory")
_A3sysSNMPMgrTable_Object = MibTable
a3sysSNMPMgrTable = _A3sysSNMPMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 6)
)
if mibBuilder.loadTexts:
    a3sysSNMPMgrTable.setStatus("mandatory")
_A3sysSNMPMgrEntry_Object = MibTableRow
a3sysSNMPMgrEntry = _A3sysSNMPMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 6, 1)
)
a3sysSNMPMgrEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysSNMPMgrCommString"),
    (0, "A3Com-System-r8-MIB", "a3sysSNMPMgrAddress"),
)
if mibBuilder.loadTexts:
    a3sysSNMPMgrEntry.setStatus("mandatory")


class _A3sysSNMPMgrCommString_Type(DisplayString):
    """Custom type a3sysSNMPMgrCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_A3sysSNMPMgrCommString_Type.__name__ = "DisplayString"
_A3sysSNMPMgrCommString_Object = MibTableColumn
a3sysSNMPMgrCommString = _A3sysSNMPMgrCommString_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 6, 1, 1),
    _A3sysSNMPMgrCommString_Type()
)
a3sysSNMPMgrCommString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysSNMPMgrCommString.setStatus("mandatory")
_A3sysSNMPMgrAddress_Type = IpAddress
_A3sysSNMPMgrAddress_Object = MibTableColumn
a3sysSNMPMgrAddress = _A3sysSNMPMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 6, 1, 2),
    _A3sysSNMPMgrAddress_Type()
)
a3sysSNMPMgrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysSNMPMgrAddress.setStatus("mandatory")
_A3sysSNMPMgrMask_Type = IpAddress
_A3sysSNMPMgrMask_Object = MibTableColumn
a3sysSNMPMgrMask = _A3sysSNMPMgrMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 6, 1, 3),
    _A3sysSNMPMgrMask_Type()
)
a3sysSNMPMgrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysSNMPMgrMask.setStatus("mandatory")
_A3sysSNMPMgrStatus_Type = RowStatus
_A3sysSNMPMgrStatus_Object = MibTableColumn
a3sysSNMPMgrStatus = _A3sysSNMPMgrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 6, 1, 4),
    _A3sysSNMPMgrStatus_Type()
)
a3sysSNMPMgrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysSNMPMgrStatus.setStatus("mandatory")
_A3sysTelnetMgrTable_Object = MibTable
a3sysTelnetMgrTable = _A3sysTelnetMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 7)
)
if mibBuilder.loadTexts:
    a3sysTelnetMgrTable.setStatus("mandatory")
_A3sysTelnetMgrEntry_Object = MibTableRow
a3sysTelnetMgrEntry = _A3sysTelnetMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 7, 1)
)
a3sysTelnetMgrEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysTelnetMgrAddress"),
)
if mibBuilder.loadTexts:
    a3sysTelnetMgrEntry.setStatus("mandatory")
_A3sysTelnetMgrAddress_Type = IpAddress
_A3sysTelnetMgrAddress_Object = MibTableColumn
a3sysTelnetMgrAddress = _A3sysTelnetMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 7, 1, 1),
    _A3sysTelnetMgrAddress_Type()
)
a3sysTelnetMgrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysTelnetMgrAddress.setStatus("mandatory")
_A3sysTelnetMgrStatus_Type = RowStatus
_A3sysTelnetMgrStatus_Object = MibTableColumn
a3sysTelnetMgrStatus = _A3sysTelnetMgrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 7, 1, 2),
    _A3sysTelnetMgrStatus_Type()
)
a3sysTelnetMgrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysTelnetMgrStatus.setStatus("mandatory")
_A3sysPasswordTable_Object = MibTable
a3sysPasswordTable = _A3sysPasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 8)
)
if mibBuilder.loadTexts:
    a3sysPasswordTable.setStatus("mandatory")
_A3sysPasswordEntry_Object = MibTableRow
a3sysPasswordEntry = _A3sysPasswordEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 8, 1)
)
a3sysPasswordEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysUserName"),
    (0, "A3Com-System-r8-MIB", "a3sysOldPassword"),
)
if mibBuilder.loadTexts:
    a3sysPasswordEntry.setStatus("mandatory")


class _A3sysPwStatus_Type(Integer32):
    """Custom type a3sysPwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_A3sysPwStatus_Type.__name__ = "Integer32"
_A3sysPwStatus_Object = MibTableColumn
a3sysPwStatus = _A3sysPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 8, 1, 1),
    _A3sysPwStatus_Type()
)
a3sysPwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysPwStatus.setStatus("mandatory")


class _A3sysUserName_Type(DisplayString):
    """Custom type a3sysUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_A3sysUserName_Type.__name__ = "DisplayString"
_A3sysUserName_Object = MibTableColumn
a3sysUserName = _A3sysUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 8, 1, 2),
    _A3sysUserName_Type()
)
a3sysUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysUserName.setStatus("mandatory")


class _A3sysUserLevel_Type(Integer32):
    """Custom type a3sysUserLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("manager", 3),
          ("monitor", 1),
          ("secureMonitor", 2),
          ("security", 5),
          ("specialist", 4))
    )


_A3sysUserLevel_Type.__name__ = "Integer32"
_A3sysUserLevel_Object = MibTableColumn
a3sysUserLevel = _A3sysUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 8, 1, 3),
    _A3sysUserLevel_Type()
)
a3sysUserLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUserLevel.setStatus("mandatory")
_A3sysOldPassword_Type = DisplayString
_A3sysOldPassword_Object = MibTableColumn
a3sysOldPassword = _A3sysOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 8, 1, 4),
    _A3sysOldPassword_Type()
)
a3sysOldPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysOldPassword.setStatus("mandatory")
_A3sysNewPassword_Type = DisplayString
_A3sysNewPassword_Object = MibTableColumn
a3sysNewPassword = _A3sysNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 8, 1, 5),
    _A3sysNewPassword_Type()
)
a3sysNewPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysNewPassword.setStatus("mandatory")


class _A3sysSnmpPasswordCtl_Type(Integer32):
    """Custom type a3sysSnmpPasswordCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3sysSnmpPasswordCtl_Type.__name__ = "Integer32"
_A3sysSnmpPasswordCtl_Object = MibScalar
a3sysSnmpPasswordCtl = _A3sysSnmpPasswordCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 7, 9),
    _A3sysSnmpPasswordCtl_Type()
)
a3sysSnmpPasswordCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysSnmpPasswordCtl.setStatus("mandatory")
_A3ComSysMisc_ObjectIdentity = ObjectIdentity
a3ComSysMisc = _A3ComSysMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8)
)


class _A3sysNetMapTime_Type(Integer32):
    """Custom type a3sysNetMapTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_A3sysNetMapTime_Type.__name__ = "Integer32"
_A3sysNetMapTime_Object = MibScalar
a3sysNetMapTime = _A3sysNetMapTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 1),
    _A3sysNetMapTime_Type()
)
a3sysNetMapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysNetMapTime.setStatus("mandatory")


class _A3sysUIBinary_Type(Integer32):
    """Custom type a3sysUIBinary based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_A3sysUIBinary_Type.__name__ = "Integer32"
_A3sysUIBinary_Object = MibScalar
a3sysUIBinary = _A3sysUIBinary_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 2),
    _A3sysUIBinary_Type()
)
a3sysUIBinary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUIBinary.setStatus("mandatory")
_A3sysChangeTimestamp_Type = TimeTicks
_A3sysChangeTimestamp_Object = MibScalar
a3sysChangeTimestamp = _A3sysChangeTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 3),
    _A3sysChangeTimestamp_Type()
)
a3sysChangeTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysChangeTimestamp.setStatus("mandatory")


class _A3sysCpuUtil_Type(Integer32):
    """Custom type a3sysCpuUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_A3sysCpuUtil_Type.__name__ = "Integer32"
_A3sysCpuUtil_Object = MibScalar
a3sysCpuUtil = _A3sysCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 4),
    _A3sysCpuUtil_Type()
)
a3sysCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysCpuUtil.setStatus("mandatory")
_A3sysCpuBrdMacAddr_Type = MacAddress
_A3sysCpuBrdMacAddr_Object = MibScalar
a3sysCpuBrdMacAddr = _A3sysCpuBrdMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 5),
    _A3sysCpuBrdMacAddr_Type()
)
a3sysCpuBrdMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysCpuBrdMacAddr.setStatus("mandatory")
_A3sysExpMacAddr_Type = MacAddress
_A3sysExpMacAddr_Object = MibScalar
a3sysExpMacAddr = _A3sysExpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 6),
    _A3sysExpMacAddr_Type()
)
a3sysExpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysExpMacAddr.setStatus("mandatory")
_A3sysVportTimestamp_Type = TimeTicks
_A3sysVportTimestamp_Object = MibScalar
a3sysVportTimestamp = _A3sysVportTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 7),
    _A3sysVportTimestamp_Type()
)
a3sysVportTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysVportTimestamp.setStatus("mandatory")


class _A3sysDefDrive_Type(Integer32):
    """Custom type a3sysDefDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("driveA", 1),
          ("driveB", 2))
    )


_A3sysDefDrive_Type.__name__ = "Integer32"
_A3sysDefDrive_Object = MibScalar
a3sysDefDrive = _A3sysDefDrive_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 8),
    _A3sysDefDrive_Type()
)
a3sysDefDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysDefDrive.setStatus("mandatory")


class _A3sysDefDriveType_Type(Integer32):
    """Custom type a3sysDefDriveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("flash", 2),
          ("floppy", 1),
          ("noDrive", 4),
          ("unknown", 3))
    )


_A3sysDefDriveType_Type.__name__ = "Integer32"
_A3sysDefDriveType_Object = MibScalar
a3sysDefDriveType = _A3sysDefDriveType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 9),
    _A3sysDefDriveType_Type()
)
a3sysDefDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysDefDriveType.setStatus("mandatory")


class _A3sysDriveStatus_Type(Integer32):
    """Custom type a3sysDriveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("driveA", 2),
          ("driveAB", 4),
          ("driveB", 3),
          ("noDrives", 1))
    )


_A3sysDriveStatus_Type.__name__ = "Integer32"
_A3sysDriveStatus_Object = MibScalar
a3sysDriveStatus = _A3sysDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 10),
    _A3sysDriveStatus_Type()
)
a3sysDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysDriveStatus.setStatus("mandatory")
_A3sysBogusDhcpSvr_Type = IpAddress
_A3sysBogusDhcpSvr_Object = MibScalar
a3sysBogusDhcpSvr = _A3sysBogusDhcpSvr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 11),
    _A3sysBogusDhcpSvr_Type()
)
a3sysBogusDhcpSvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysBogusDhcpSvr.setStatus("mandatory")
_A3sysNb2EepromVers_Type = Integer32
_A3sysNb2EepromVers_Object = MibScalar
a3sysNb2EepromVers = _A3sysNb2EepromVers_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 12),
    _A3sysNb2EepromVers_Type()
)
a3sysNb2EepromVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysNb2EepromVers.setStatus("mandatory")
_A3sysX25Conns_Type = Integer32
_A3sysX25Conns_Object = MibScalar
a3sysX25Conns = _A3sysX25Conns_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 8, 13),
    _A3sysX25Conns_Type()
)
a3sysX25Conns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysX25Conns.setStatus("mandatory")
_A3ComFW_ObjectIdentity = ObjectIdentity
a3ComFW = _A3ComFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 9)
)


class _A3sysFwSerBaudCons_Type(Integer32):
    """Custom type a3sysFwSerBaudCons based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 2),
          ("bps1200", 5),
          ("bps19200", 9),
          ("bps2400", 6),
          ("bps300", 3),
          ("bps38400", 10),
          ("bps4800", 7),
          ("bps57600", 11),
          ("bps600", 4),
          ("bps9600", 8),
          ("unknown", 1))
    )


_A3sysFwSerBaudCons_Type.__name__ = "Integer32"
_A3sysFwSerBaudCons_Object = MibScalar
a3sysFwSerBaudCons = _A3sysFwSerBaudCons_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 9, 1),
    _A3sysFwSerBaudCons_Type()
)
a3sysFwSerBaudCons.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysFwSerBaudCons.setStatus("mandatory")


class _A3sysFwSerBaudAux_Type(Integer32):
    """Custom type a3sysFwSerBaudAux based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 2),
          ("bps1200", 5),
          ("bps19200", 9),
          ("bps2400", 6),
          ("bps300", 3),
          ("bps4800", 7),
          ("bps600", 4),
          ("bps9600", 8),
          ("unknown", 1))
    )


_A3sysFwSerBaudAux_Type.__name__ = "Integer32"
_A3sysFwSerBaudAux_Object = MibScalar
a3sysFwSerBaudAux = _A3sysFwSerBaudAux_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 9, 2),
    _A3sysFwSerBaudAux_Type()
)
a3sysFwSerBaudAux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysFwSerBaudAux.setStatus("mandatory")


class _A3sysFwSelfTest_Type(Integer32):
    """Custom type a3sysFwSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("loop", 4),
          ("other", 3),
          ("skip", 1),
          ("testOnce", 2))
    )


_A3sysFwSelfTest_Type.__name__ = "Integer32"
_A3sysFwSelfTest_Object = MibScalar
a3sysFwSelfTest = _A3sysFwSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 9, 3),
    _A3sysFwSelfTest_Type()
)
a3sysFwSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysFwSelfTest.setStatus("mandatory")
_A3ComBoot_ObjectIdentity = ObjectIdentity
a3ComBoot = _A3ComBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10)
)


class _A3sysReBoot_Type(Integer32):
    """Custom type a3sysReBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("stdReboot", 2))
    )


_A3sysReBoot_Type.__name__ = "Integer32"
_A3sysReBoot_Object = MibScalar
a3sysReBoot = _A3sysReBoot_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 1),
    _A3sysReBoot_Type()
)
a3sysReBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysReBoot.setStatus("mandatory")
_A3sysTestBootTime_Type = Integer32
_A3sysTestBootTime_Object = MibScalar
a3sysTestBootTime = _A3sysTestBootTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 2),
    _A3sysTestBootTime_Type()
)
a3sysTestBootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysTestBootTime.setStatus("mandatory")


class _A3sysStartUpAction_Type(Integer32):
    """Custom type a3sysStartUpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 4),
          ("monitor", 1),
          ("userListForever", 3),
          ("userListOnce", 2))
    )


_A3sysStartUpAction_Type.__name__ = "Integer32"
_A3sysStartUpAction_Object = MibScalar
a3sysStartUpAction = _A3sysStartUpAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 3),
    _A3sysStartUpAction_Type()
)
a3sysStartUpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysStartUpAction.setStatus("mandatory")
_A3sysTestRecoveryTimer_Type = Integer32
_A3sysTestRecoveryTimer_Object = MibScalar
a3sysTestRecoveryTimer = _A3sysTestRecoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 4),
    _A3sysTestRecoveryTimer_Type()
)
a3sysTestRecoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysTestRecoveryTimer.setStatus("mandatory")
_A3sysDirectedReBoots_Type = Counter32
_A3sysDirectedReBoots_Object = MibScalar
a3sysDirectedReBoots = _A3sysDirectedReBoots_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 5),
    _A3sysDirectedReBoots_Type()
)
a3sysDirectedReBoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysDirectedReBoots.setStatus("mandatory")
_A3sysExceptionReBoots_Type = Counter32
_A3sysExceptionReBoots_Object = MibScalar
a3sysExceptionReBoots = _A3sysExceptionReBoots_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 6),
    _A3sysExceptionReBoots_Type()
)
a3sysExceptionReBoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysExceptionReBoots.setStatus("mandatory")


class _A3sysBootDump_Type(Integer32):
    """Custom type a3sysBootDump based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("localDevice", 3),
          ("monitor", 2),
          ("network", 5),
          ("noDump", 1),
          ("userList", 4))
    )


_A3sysBootDump_Type.__name__ = "Integer32"
_A3sysBootDump_Object = MibScalar
a3sysBootDump = _A3sysBootDump_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 7),
    _A3sysBootDump_Type()
)
a3sysBootDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysBootDump.setStatus("mandatory")


class _A3sysBootSources_Type(Integer32):
    """Custom type a3sysBootSources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("primaryAndSecondary", 2),
          ("secondary", 4),
          ("testWithPrimaryBackup", 3))
    )


_A3sysBootSources_Type.__name__ = "Integer32"
_A3sysBootSources_Object = MibScalar
a3sysBootSources = _A3sysBootSources_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 8),
    _A3sysBootSources_Type()
)
a3sysBootSources.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysBootSources.setStatus("mandatory")
_A3sysUserBootListTable_Object = MibTable
a3sysUserBootListTable = _A3sysUserBootListTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9)
)
if mibBuilder.loadTexts:
    a3sysUserBootListTable.setStatus("mandatory")
_A3sysUserBootListEntry_Object = MibTableRow
a3sysUserBootListEntry = _A3sysUserBootListEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1)
)
a3sysUserBootListEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysUblSource"),
)
if mibBuilder.loadTexts:
    a3sysUserBootListEntry.setStatus("mandatory")


class _A3sysUblSource_Type(Integer32):
    """Custom type a3sysUblSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dump", 4),
          ("primary", 1),
          ("secondary", 2),
          ("test", 3))
    )


_A3sysUblSource_Type.__name__ = "Integer32"
_A3sysUblSource_Object = MibTableColumn
a3sysUblSource = _A3sysUblSource_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 1),
    _A3sysUblSource_Type()
)
a3sysUblSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysUblSource.setStatus("mandatory")


class _A3sysUblDevice_Type(Integer32):
    """Custom type a3sysUblDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 6),
          ("localMediaA", 1),
          ("localMediaB", 2),
          ("monitor", 4),
          ("network", 3),
          ("other", 5))
    )


_A3sysUblDevice_Type.__name__ = "Integer32"
_A3sysUblDevice_Object = MibTableColumn
a3sysUblDevice = _A3sysUblDevice_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 2),
    _A3sysUblDevice_Type()
)
a3sysUblDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblDevice.setStatus("mandatory")
_A3sysUblFileName_Type = DisplayString
_A3sysUblFileName_Object = MibTableColumn
a3sysUblFileName = _A3sysUblFileName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 3),
    _A3sysUblFileName_Type()
)
a3sysUblFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblFileName.setStatus("mandatory")
_A3sysUblNetFile_Type = DisplayString
_A3sysUblNetFile_Object = MibTableColumn
a3sysUblNetFile = _A3sysUblNetFile_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 4),
    _A3sysUblNetFile_Type()
)
a3sysUblNetFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblNetFile.setStatus("deprecated")
_A3sysUblSlot_Type = Integer32
_A3sysUblSlot_Object = MibTableColumn
a3sysUblSlot = _A3sysUblSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 5),
    _A3sysUblSlot_Type()
)
a3sysUblSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblSlot.setStatus("mandatory")


class _A3sysUblInterface_Type(Integer32):
    """Custom type a3sysUblInterface based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interfaceA", 2),
          ("interfaceB", 3),
          ("unknown", 1))
    )


_A3sysUblInterface_Type.__name__ = "Integer32"
_A3sysUblInterface_Object = MibTableColumn
a3sysUblInterface = _A3sysUblInterface_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 6),
    _A3sysUblInterface_Type()
)
a3sysUblInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblInterface.setStatus("mandatory")


class _A3sysUblMaxRetries_Type(Integer32):
    """Custom type a3sysUblMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A3sysUblMaxRetries_Type.__name__ = "Integer32"
_A3sysUblMaxRetries_Object = MibTableColumn
a3sysUblMaxRetries = _A3sysUblMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 7),
    _A3sysUblMaxRetries_Type()
)
a3sysUblMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblMaxRetries.setStatus("mandatory")


class _A3sysUblConfigFileDevice_Type(Integer32):
    """Custom type a3sysUblConfigFileDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bootDevice", 1),
          ("local", 2),
          ("network", 3),
          ("other", 4))
    )


_A3sysUblConfigFileDevice_Type.__name__ = "Integer32"
_A3sysUblConfigFileDevice_Object = MibTableColumn
a3sysUblConfigFileDevice = _A3sysUblConfigFileDevice_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 8),
    _A3sysUblConfigFileDevice_Type()
)
a3sysUblConfigFileDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblConfigFileDevice.setStatus("mandatory")
_A3sysUblConfigFilePath_Type = DisplayString
_A3sysUblConfigFilePath_Object = MibTableColumn
a3sysUblConfigFilePath = _A3sysUblConfigFilePath_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 9),
    _A3sysUblConfigFilePath_Type()
)
a3sysUblConfigFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblConfigFilePath.setStatus("mandatory")


class _A3sysUblConfigProt_Type(Integer32):
    """Custom type a3sysUblConfigProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fap", 1),
          ("ftp", 2),
          ("other", 3))
    )


_A3sysUblConfigProt_Type.__name__ = "Integer32"
_A3sysUblConfigProt_Object = MibTableColumn
a3sysUblConfigProt = _A3sysUblConfigProt_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 10),
    _A3sysUblConfigProt_Type()
)
a3sysUblConfigProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysUblConfigProt.setStatus("mandatory")


class _A3sysUblConfigUserName_Type(DisplayString):
    """Custom type a3sysUblConfigUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_A3sysUblConfigUserName_Type.__name__ = "DisplayString"
_A3sysUblConfigUserName_Object = MibTableColumn
a3sysUblConfigUserName = _A3sysUblConfigUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 11),
    _A3sysUblConfigUserName_Type()
)
a3sysUblConfigUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblConfigUserName.setStatus("mandatory")


class _A3sysUblConfigPassword_Type(DisplayString):
    """Custom type a3sysUblConfigPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_A3sysUblConfigPassword_Type.__name__ = "DisplayString"
_A3sysUblConfigPassword_Object = MibTableColumn
a3sysUblConfigPassword = _A3sysUblConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 12),
    _A3sysUblConfigPassword_Type()
)
a3sysUblConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblConfigPassword.setStatus("mandatory")


class _A3sysUblConfigAcct_Type(DisplayString):
    """Custom type a3sysUblConfigAcct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_A3sysUblConfigAcct_Type.__name__ = "DisplayString"
_A3sysUblConfigAcct_Object = MibTableColumn
a3sysUblConfigAcct = _A3sysUblConfigAcct_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 13),
    _A3sysUblConfigAcct_Type()
)
a3sysUblConfigAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblConfigAcct.setStatus("mandatory")


class _A3sysUblMacAddress_Type(Integer32):
    """Custom type a3sysUblMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpu-module", 1),
          ("io-module", 2),
          ("other", 3))
    )


_A3sysUblMacAddress_Type.__name__ = "Integer32"
_A3sysUblMacAddress_Object = MibTableColumn
a3sysUblMacAddress = _A3sysUblMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 14),
    _A3sysUblMacAddress_Type()
)
a3sysUblMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblMacAddress.setStatus("mandatory")


class _A3sysUblCanonicalFlag_Type(Integer32):
    """Custom type a3sysUblCanonicalFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 2),
          ("nonCanonical", 3),
          ("other", 1))
    )


_A3sysUblCanonicalFlag_Type.__name__ = "Integer32"
_A3sysUblCanonicalFlag_Object = MibTableColumn
a3sysUblCanonicalFlag = _A3sysUblCanonicalFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 15),
    _A3sysUblCanonicalFlag_Type()
)
a3sysUblCanonicalFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblCanonicalFlag.setStatus("mandatory")


class _A3sysUblRemoteProt_Type(Integer32):
    """Custom type a3sysUblRemoteProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("frameRelay", 3),
          ("notApplicable", 1),
          ("ppp", 2))
    )


_A3sysUblRemoteProt_Type.__name__ = "Integer32"
_A3sysUblRemoteProt_Object = MibTableColumn
a3sysUblRemoteProt = _A3sysUblRemoteProt_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 16),
    _A3sysUblRemoteProt_Type()
)
a3sysUblRemoteProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblRemoteProt.setStatus("mandatory")


class _A3sysUblBaudRate_Type(Integer32):
    """Custom type a3sysUblBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("bps9600", 2),
          ("kbps128", 7),
          ("kbps1536", 10),
          ("kbps19", 3),
          ("kbps2048", 11),
          ("kbps256", 8),
          ("kbps38", 4),
          ("kbps448", 9),
          ("kbps56", 5),
          ("kbps64", 6),
          ("mbps16", 13),
          ("mbps4", 12),
          ("unknown", 1))
    )


_A3sysUblBaudRate_Type.__name__ = "Integer32"
_A3sysUblBaudRate_Object = MibTableColumn
a3sysUblBaudRate = _A3sysUblBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 17),
    _A3sysUblBaudRate_Type()
)
a3sysUblBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblBaudRate.setStatus("mandatory")


class _A3sysUblClockSource_Type(Integer32):
    """Custom type a3sysUblClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("unknown", 3))
    )


_A3sysUblClockSource_Type.__name__ = "Integer32"
_A3sysUblClockSource_Object = MibTableColumn
a3sysUblClockSource = _A3sysUblClockSource_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 18),
    _A3sysUblClockSource_Type()
)
a3sysUblClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblClockSource.setStatus("mandatory")


class _A3sysUblConnectorType_Type(Integer32):
    """Custom type a3sysUblConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 2),
          ("unknown", 1),
          ("v35", 3))
    )


_A3sysUblConnectorType_Type.__name__ = "Integer32"
_A3sysUblConnectorType_Object = MibTableColumn
a3sysUblConnectorType = _A3sysUblConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 19),
    _A3sysUblConnectorType_Type()
)
a3sysUblConnectorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblConnectorType.setStatus("mandatory")


class _A3sysUblWanAddress_Type(DisplayString):
    """Custom type a3sysUblWanAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_A3sysUblWanAddress_Type.__name__ = "DisplayString"
_A3sysUblWanAddress_Object = MibTableColumn
a3sysUblWanAddress = _A3sysUblWanAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 20),
    _A3sysUblWanAddress_Type()
)
a3sysUblWanAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblWanAddress.setStatus("mandatory")
_A3sysUblClientIpAddr_Type = IpAddress
_A3sysUblClientIpAddr_Object = MibTableColumn
a3sysUblClientIpAddr = _A3sysUblClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 21),
    _A3sysUblClientIpAddr_Type()
)
a3sysUblClientIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblClientIpAddr.setStatus("mandatory")
_A3sysUblServerIpAddr_Type = IpAddress
_A3sysUblServerIpAddr_Object = MibTableColumn
a3sysUblServerIpAddr = _A3sysUblServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 22),
    _A3sysUblServerIpAddr_Type()
)
a3sysUblServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblServerIpAddr.setStatus("mandatory")
_A3sysUblGwIpAddr_Type = IpAddress
_A3sysUblGwIpAddr_Object = MibTableColumn
a3sysUblGwIpAddr = _A3sysUblGwIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 23),
    _A3sysUblGwIpAddr_Type()
)
a3sysUblGwIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblGwIpAddr.setStatus("mandatory")
_A3sysUblConfigFileIpAddr_Type = IpAddress
_A3sysUblConfigFileIpAddr_Object = MibTableColumn
a3sysUblConfigFileIpAddr = _A3sysUblConfigFileIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 24),
    _A3sysUblConfigFileIpAddr_Type()
)
a3sysUblConfigFileIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblConfigFileIpAddr.setStatus("mandatory")
_A3sysUblIpMask_Type = IpAddress
_A3sysUblIpMask_Object = MibTableColumn
a3sysUblIpMask = _A3sysUblIpMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 25),
    _A3sysUblIpMask_Type()
)
a3sysUblIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblIpMask.setStatus("mandatory")


class _A3sysUblAddressDiscovery_Type(Integer32):
    """Custom type a3sysUblAddressDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("bootpRarp", 4),
          ("configAddr", 3),
          ("other", 1),
          ("rarp", 5),
          ("rarpBootp", 6))
    )


_A3sysUblAddressDiscovery_Type.__name__ = "Integer32"
_A3sysUblAddressDiscovery_Object = MibTableColumn
a3sysUblAddressDiscovery = _A3sysUblAddressDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 26),
    _A3sysUblAddressDiscovery_Type()
)
a3sysUblAddressDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblAddressDiscovery.setStatus("mandatory")


class _A3sysUblPassword_Type(DisplayString):
    """Custom type a3sysUblPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_A3sysUblPassword_Type.__name__ = "DisplayString"
_A3sysUblPassword_Object = MibTableColumn
a3sysUblPassword = _A3sysUblPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 9, 1, 27),
    _A3sysUblPassword_Type()
)
a3sysUblPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysUblPassword.setStatus("mandatory")
_A3sysIioBootTable_Object = MibTable
a3sysIioBootTable = _A3sysIioBootTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 10)
)
if mibBuilder.loadTexts:
    a3sysIioBootTable.setStatus("mandatory")
_A3sysIioBootEntry_Object = MibTableRow
a3sysIioBootEntry = _A3sysIioBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 10, 1)
)
a3sysIioBootEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysIioBootSlot"),
)
if mibBuilder.loadTexts:
    a3sysIioBootEntry.setStatus("mandatory")
_A3sysIioBootSlot_Type = Integer32
_A3sysIioBootSlot_Object = MibTableColumn
a3sysIioBootSlot = _A3sysIioBootSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 10, 1, 1),
    _A3sysIioBootSlot_Type()
)
a3sysIioBootSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysIioBootSlot.setStatus("mandatory")
_A3sysIioBootFileName_Type = DisplayString
_A3sysIioBootFileName_Object = MibTableColumn
a3sysIioBootFileName = _A3sysIioBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 10, 1, 2),
    _A3sysIioBootFileName_Type()
)
a3sysIioBootFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysIioBootFileName.setStatus("mandatory")


class _A3sysIioBootState_Type(Integer32):
    """Custom type a3sysIioBootState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("booting", 3),
          ("dumping", 5),
          ("empty", 1),
          ("error", 8),
          ("halted", 6),
          ("recovering", 4),
          ("selfTestFail", 7),
          ("up", 2))
    )


_A3sysIioBootState_Type.__name__ = "Integer32"
_A3sysIioBootState_Object = MibTableColumn
a3sysIioBootState = _A3sysIioBootState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 10, 1, 3),
    _A3sysIioBootState_Type()
)
a3sysIioBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysIioBootState.setStatus("mandatory")
_A3sysIioBootTime_Type = TimeTicks
_A3sysIioBootTime_Object = MibTableColumn
a3sysIioBootTime = _A3sysIioBootTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 10, 1, 4),
    _A3sysIioBootTime_Type()
)
a3sysIioBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysIioBootTime.setStatus("mandatory")
_A3sysIioBootImage_Type = ObjectIdentifier
_A3sysIioBootImage_Object = MibTableColumn
a3sysIioBootImage = _A3sysIioBootImage_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 10, 10, 1, 5),
    _A3sysIioBootImage_Type()
)
a3sysIioBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysIioBootImage.setStatus("mandatory")
_A3ComLastBoot_ObjectIdentity = ObjectIdentity
a3ComLastBoot = _A3ComLastBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 11)
)


class _A3sysLastBootSource_Type(Integer32):
    """Custom type a3sysLastBootSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 3),
          ("primary", 1),
          ("secondary", 2),
          ("test", 4))
    )


_A3sysLastBootSource_Type.__name__ = "Integer32"
_A3sysLastBootSource_Object = MibScalar
a3sysLastBootSource = _A3sysLastBootSource_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 11, 1),
    _A3sysLastBootSource_Type()
)
a3sysLastBootSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysLastBootSource.setStatus("mandatory")


class _A3sysLastBootError_Type(Integer32):
    """Custom type a3sysLastBootError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fileTransferFailed", 5),
          ("imageInvalid", 7),
          ("imageNotFound", 6),
          ("noServerResponse", 4),
          ("none", 1),
          ("unknownLocalAddress", 2),
          ("unknownServerAddress", 3))
    )


_A3sysLastBootError_Type.__name__ = "Integer32"
_A3sysLastBootError_Object = MibScalar
a3sysLastBootError = _A3sysLastBootError_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 11, 2),
    _A3sysLastBootError_Type()
)
a3sysLastBootError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysLastBootError.setStatus("mandatory")
_A3sysLastBootDate_Type = DisplayString
_A3sysLastBootDate_Object = MibScalar
a3sysLastBootDate = _A3sysLastBootDate_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 11, 3),
    _A3sysLastBootDate_Type()
)
a3sysLastBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysLastBootDate.setStatus("mandatory")
_A3sysLbConfigFileIpAddr_Type = IpAddress
_A3sysLbConfigFileIpAddr_Object = MibScalar
a3sysLbConfigFileIpAddr = _A3sysLbConfigFileIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 11, 4),
    _A3sysLbConfigFileIpAddr_Type()
)
a3sysLbConfigFileIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysLbConfigFileIpAddr.setStatus("mandatory")
_A3sysLbGwIpAddr_Type = IpAddress
_A3sysLbGwIpAddr_Object = MibScalar
a3sysLbGwIpAddr = _A3sysLbGwIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 11, 5),
    _A3sysLbGwIpAddr_Type()
)
a3sysLbGwIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysLbGwIpAddr.setStatus("mandatory")
_A3sysLbIpMask_Type = IpAddress
_A3sysLbIpMask_Object = MibScalar
a3sysLbIpMask = _A3sysLbIpMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 11, 6),
    _A3sysLbIpMask_Type()
)
a3sysLbIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysLbIpMask.setStatus("mandatory")


class _A3sysLbConfigDevice_Type(Integer32):
    """Custom type a3sysLbConfigDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bootDevice", 1),
          ("local", 2),
          ("network", 3),
          ("other", 4))
    )


_A3sysLbConfigDevice_Type.__name__ = "Integer32"
_A3sysLbConfigDevice_Object = MibScalar
a3sysLbConfigDevice = _A3sysLbConfigDevice_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 11, 7),
    _A3sysLbConfigDevice_Type()
)
a3sysLbConfigDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysLbConfigDevice.setStatus("mandatory")


class _A3sysLbConfigFilePath_Type(DisplayString):
    """Custom type a3sysLbConfigFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_A3sysLbConfigFilePath_Type.__name__ = "DisplayString"
_A3sysLbConfigFilePath_Object = MibScalar
a3sysLbConfigFilePath = _A3sysLbConfigFilePath_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 11, 8),
    _A3sysLbConfigFilePath_Type()
)
a3sysLbConfigFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysLbConfigFilePath.setStatus("mandatory")


class _A3sysLbConfigUserName_Type(DisplayString):
    """Custom type a3sysLbConfigUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_A3sysLbConfigUserName_Type.__name__ = "DisplayString"
_A3sysLbConfigUserName_Object = MibScalar
a3sysLbConfigUserName = _A3sysLbConfigUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 11, 9),
    _A3sysLbConfigUserName_Type()
)
a3sysLbConfigUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysLbConfigUserName.setStatus("mandatory")
_A3ComFileMgmt_ObjectIdentity = ObjectIdentity
a3ComFileMgmt = _A3ComFileMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12)
)


class _A3sysFmOperation_Type(Integer32):
    """Custom type a3sysFmOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("abortCopy", 10),
          ("checksum", 9),
          ("cleanFlash", 16),
          ("copy", 2),
          ("copySystem", 8),
          ("delete", 4),
          ("directory", 6),
          ("do", 3),
          ("format", 7),
          ("ftpGet", 14),
          ("ftpPut", 15),
          ("getFileInfo", 13),
          ("makeDir", 11),
          ("other", 1),
          ("rename", 5),
          ("rmDir", 12))
    )


_A3sysFmOperation_Type.__name__ = "Integer32"
_A3sysFmOperation_Object = MibScalar
a3sysFmOperation = _A3sysFmOperation_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 1),
    _A3sysFmOperation_Type()
)
a3sysFmOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysFmOperation.setStatus("mandatory")
_A3sysFmSourceIpAddr_Type = IpAddress
_A3sysFmSourceIpAddr_Object = MibScalar
a3sysFmSourceIpAddr = _A3sysFmSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 2),
    _A3sysFmSourceIpAddr_Type()
)
a3sysFmSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysFmSourceIpAddr.setStatus("mandatory")
_A3sysFmSourceFile_Type = DisplayString
_A3sysFmSourceFile_Object = MibScalar
a3sysFmSourceFile = _A3sysFmSourceFile_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 3),
    _A3sysFmSourceFile_Type()
)
a3sysFmSourceFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysFmSourceFile.setStatus("mandatory")
_A3sysFmTargetIpAddr_Type = IpAddress
_A3sysFmTargetIpAddr_Object = MibScalar
a3sysFmTargetIpAddr = _A3sysFmTargetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 4),
    _A3sysFmTargetIpAddr_Type()
)
a3sysFmTargetIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysFmTargetIpAddr.setStatus("mandatory")
_A3sysFmTargetFile_Type = DisplayString
_A3sysFmTargetFile_Object = MibScalar
a3sysFmTargetFile = _A3sysFmTargetFile_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 5),
    _A3sysFmTargetFile_Type()
)
a3sysFmTargetFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysFmTargetFile.setStatus("mandatory")


class _A3sysFmStatus_Type(Integer32):
    """Custom type a3sysFmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 2),
          ("inactive", 1))
    )


_A3sysFmStatus_Type.__name__ = "Integer32"
_A3sysFmStatus_Object = MibScalar
a3sysFmStatus = _A3sysFmStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 6),
    _A3sysFmStatus_Type()
)
a3sysFmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysFmStatus.setStatus("mandatory")
_A3sysFmTimeStamp_Type = TimeTicks
_A3sysFmTimeStamp_Object = MibScalar
a3sysFmTimeStamp = _A3sysFmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 7),
    _A3sysFmTimeStamp_Type()
)
a3sysFmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysFmTimeStamp.setStatus("mandatory")


class _A3sysFmError_Type(Integer32):
    """Custom type a3sysFmError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 16),
          ("badChecksum", 14),
          ("badDefaultDrv", 18),
          ("badOperation", 15),
          ("badSourceAddr", 4),
          ("badSourceFile", 5),
          ("badTargetAddr", 6),
          ("badTargetFile", 7),
          ("badTargetPort", 19),
          ("inProgress", 3),
          ("noFile", 9),
          ("noPermission", 11),
          ("noResponse", 8),
          ("noSpace", 10),
          ("none", 1),
          ("other", 17),
          ("successful", 2),
          ("timeout", 13),
          ("writeError", 12))
    )


_A3sysFmError_Type.__name__ = "Integer32"
_A3sysFmError_Object = MibScalar
a3sysFmError = _A3sysFmError_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 8),
    _A3sysFmError_Type()
)
a3sysFmError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysFmError.setStatus("mandatory")
_A3ComFileList_ObjectIdentity = ObjectIdentity
a3ComFileList = _A3ComFileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 9)
)
_A3sysDfTime_Type = TimeTicks
_A3sysDfTime_Object = MibScalar
a3sysDfTime = _A3sysDfTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 9, 1),
    _A3sysDfTime_Type()
)
a3sysDfTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysDfTime.setStatus("mandatory")
_A3sysDfPath_Type = DisplayString
_A3sysDfPath_Object = MibScalar
a3sysDfPath = _A3sysDfPath_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 9, 2),
    _A3sysDfPath_Type()
)
a3sysDfPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysDfPath.setStatus("mandatory")
_A3sysDfTable_Object = MibTable
a3sysDfTable = _A3sysDfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 9, 3)
)
if mibBuilder.loadTexts:
    a3sysDfTable.setStatus("mandatory")
_A3sysDfEntry_Object = MibTableRow
a3sysDfEntry = _A3sysDfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 9, 3, 1)
)
a3sysDfEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysDfName"),
)
if mibBuilder.loadTexts:
    a3sysDfEntry.setStatus("mandatory")
_A3sysDfName_Type = DisplayString
_A3sysDfName_Object = MibTableColumn
a3sysDfName = _A3sysDfName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 9, 3, 1, 1),
    _A3sysDfName_Type()
)
a3sysDfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysDfName.setStatus("mandatory")


class _A3sysDfDir_Type(Integer32):
    """Custom type a3sysDfDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directory", 2),
          ("file", 1))
    )


_A3sysDfDir_Type.__name__ = "Integer32"
_A3sysDfDir_Object = MibTableColumn
a3sysDfDir = _A3sysDfDir_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 9, 3, 1, 2),
    _A3sysDfDir_Type()
)
a3sysDfDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysDfDir.setStatus("mandatory")
_A3ComDfTotalSpace_Type = Integer32
_A3ComDfTotalSpace_Object = MibScalar
a3ComDfTotalSpace = _A3ComDfTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 9, 4),
    _A3ComDfTotalSpace_Type()
)
a3ComDfTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDfTotalSpace.setStatus("mandatory")
_A3ComDfAvailableSpace_Type = Integer32
_A3ComDfAvailableSpace_Object = MibScalar
a3ComDfAvailableSpace = _A3ComDfAvailableSpace_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 9, 5),
    _A3ComDfAvailableSpace_Type()
)
a3ComDfAvailableSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDfAvailableSpace.setStatus("mandatory")
_A3ComFmCksum_ObjectIdentity = ObjectIdentity
a3ComFmCksum = _A3ComFmCksum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 10)
)
_A3sysFmCksum_Type = Integer32
_A3sysFmCksum_Object = MibScalar
a3sysFmCksum = _A3sysFmCksum_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 10, 1),
    _A3sysFmCksum_Type()
)
a3sysFmCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysFmCksum.setStatus("mandatory")
_A3sysFmCksumFile_Type = DisplayString
_A3sysFmCksumFile_Object = MibScalar
a3sysFmCksumFile = _A3sysFmCksumFile_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 10, 2),
    _A3sysFmCksumFile_Type()
)
a3sysFmCksumFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysFmCksumFile.setStatus("mandatory")
_A3sysFmCksumTime_Type = TimeTicks
_A3sysFmCksumTime_Object = MibScalar
a3sysFmCksumTime = _A3sysFmCksumTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 10, 3),
    _A3sysFmCksumTime_Type()
)
a3sysFmCksumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysFmCksumTime.setStatus("mandatory")
_A3ComFileInfo_ObjectIdentity = ObjectIdentity
a3ComFileInfo = _A3ComFileInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 11)
)
_A3sysFiName_Type = DisplayString
_A3sysFiName_Object = MibScalar
a3sysFiName = _A3sysFiName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 11, 1),
    _A3sysFiName_Type()
)
a3sysFiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysFiName.setStatus("mandatory")
_A3sysFiDate_Type = DisplayString
_A3sysFiDate_Object = MibScalar
a3sysFiDate = _A3sysFiDate_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 11, 2),
    _A3sysFiDate_Type()
)
a3sysFiDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysFiDate.setStatus("mandatory")
_A3sysFiTimeStamp_Type = TimeTicks
_A3sysFiTimeStamp_Object = MibScalar
a3sysFiTimeStamp = _A3sysFiTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 11, 3),
    _A3sysFiTimeStamp_Type()
)
a3sysFiTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysFiTimeStamp.setStatus("mandatory")
_A3sysFmSize_Type = Integer32
_A3sysFmSize_Object = MibScalar
a3sysFmSize = _A3sysFmSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 12, 11, 4),
    _A3sysFmSize_Type()
)
a3sysFmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysFmSize.setStatus("mandatory")
_A3ComRecovery_ObjectIdentity = ObjectIdentity
a3ComRecovery = _A3ComRecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 13)
)
_A3sysIioRecoveryTable_Object = MibTable
a3sysIioRecoveryTable = _A3sysIioRecoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 13, 1)
)
if mibBuilder.loadTexts:
    a3sysIioRecoveryTable.setStatus("mandatory")
_A3sysIioRecoveryEntry_Object = MibTableRow
a3sysIioRecoveryEntry = _A3sysIioRecoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 13, 1, 1)
)
a3sysIioRecoveryEntry.setIndexNames(
    (0, "A3Com-System-r8-MIB", "a3sysIioRecoverySlot"),
)
if mibBuilder.loadTexts:
    a3sysIioRecoveryEntry.setStatus("mandatory")


class _A3sysIioRecoverySlot_Type(Integer32):
    """Custom type a3sysIioRecoverySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_A3sysIioRecoverySlot_Type.__name__ = "Integer32"
_A3sysIioRecoverySlot_Object = MibTableColumn
a3sysIioRecoverySlot = _A3sysIioRecoverySlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 13, 1, 1, 1),
    _A3sysIioRecoverySlot_Type()
)
a3sysIioRecoverySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3sysIioRecoverySlot.setStatus("mandatory")


class _A3sysIioRecoveryProcedure_Type(Integer32):
    """Custom type a3sysIioRecoveryProcedure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dumpAndReboot", 5),
          ("halt", 1),
          ("haltSystem", 2),
          ("reboot", 3),
          ("rebootSystem", 4),
          ("selectiveDumpAndReboot", 6))
    )


_A3sysIioRecoveryProcedure_Type.__name__ = "Integer32"
_A3sysIioRecoveryProcedure_Object = MibTableColumn
a3sysIioRecoveryProcedure = _A3sysIioRecoveryProcedure_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 13, 1, 1, 2),
    _A3sysIioRecoveryProcedure_Type()
)
a3sysIioRecoveryProcedure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysIioRecoveryProcedure.setStatus("mandatory")
_A3sysIioRecoverySelect_Type = Integer32
_A3sysIioRecoverySelect_Object = MibTableColumn
a3sysIioRecoverySelect = _A3sysIioRecoverySelect_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 13, 13, 1, 1, 3),
    _A3sysIioRecoverySelect_Type()
)
a3sysIioRecoverySelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3sysIioRecoverySelect.setStatus("mandatory")

# Managed Objects groups


# Notification objects

a3BogusDhcpSvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 100)
)
a3BogusDhcpSvr.setObjects(
    ("A3Com-System-r8-MIB", "a3sysBogusDhcpSvr")
)
if mibBuilder.loadTexts:
    a3BogusDhcpSvr.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3Com-System-r8-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "a3BogusDhcpSvr": a3BogusDhcpSvr,
       "brouterMIB": brouterMIB,
       "a3ComSys": a3ComSys,
       "a3ComSysID": a3ComSysID,
       "a3sysVersion": a3sysVersion,
       "a3sysPlatformDescr": a3sysPlatformDescr,
       "a3sysPlatformID": a3sysPlatformID,
       "a3sysCallerID": a3sysCallerID,
       "a3ComChip": a3ComChip,
       "a3sysChipTable": a3sysChipTable,
       "a3sysChipEntry": a3sysChipEntry,
       "a3sysChipSlotIndex": a3sysChipSlotIndex,
       "a3sysChipIndex": a3sysChipIndex,
       "a3sysChipName": a3sysChipName,
       "a3sysChipDescr": a3sysChipDescr,
       "a3ComMem": a3ComMem,
       "a3sysMemTable": a3sysMemTable,
       "a3sysMemEntry": a3sysMemEntry,
       "a3sysMemSlotIndex": a3sysMemSlotIndex,
       "a3sysMemIndex": a3sysMemIndex,
       "a3sysMemType": a3sysMemType,
       "a3sysMemStartAdd": a3sysMemStartAdd,
       "a3sysMemSize": a3sysMemSize,
       "a3ComBrd": a3ComBrd,
       "a3sysSlotNumber": a3sysSlotNumber,
       "a3sysBrdTable": a3sysBrdTable,
       "a3sysBrdEntry": a3sysBrdEntry,
       "a3sysSlotIndex": a3sysSlotIndex,
       "a3sysBrdDescr": a3sysBrdDescr,
       "a3sysBrdPathCapacity": a3sysBrdPathCapacity,
       "a3sysBrdOID": a3sysBrdOID,
       "a3sysBrdReset": a3sysBrdReset,
       "a3sysBrdFwVers": a3sysBrdFwVers,
       "a3ComAudit": a3ComAudit,
       "a3sysAuditTrailType": a3sysAuditTrailType,
       "a3sysLogServerAddress": a3sysLogServerAddress,
       "a3ComTime": a3ComTime,
       "a3sysDate": a3sysDate,
       "a3sysDSTime": a3sysDSTime,
       "a3sysTimeZone": a3sysTimeZone,
       "a3ComAccCtl": a3ComAccCtl,
       "a3sysRemoteAccess": a3sysRemoteAccess,
       "a3sysTelnetAccess": a3sysTelnetAccess,
       "a3sysConsoleAccess": a3sysConsoleAccess,
       "a3sysSNMPAccess": a3sysSNMPAccess,
       "a3sysSNMPCommTable": a3sysSNMPCommTable,
       "a3sysSNMPCommEntry": a3sysSNMPCommEntry,
       "a3sysSNMPCommString": a3sysSNMPCommString,
       "a3sysSNMPCommAccess": a3sysSNMPCommAccess,
       "a3sysSNMPCommTrap": a3sysSNMPCommTrap,
       "a3sysSNMPCommStatus": a3sysSNMPCommStatus,
       "a3sysSNMPMgrTable": a3sysSNMPMgrTable,
       "a3sysSNMPMgrEntry": a3sysSNMPMgrEntry,
       "a3sysSNMPMgrCommString": a3sysSNMPMgrCommString,
       "a3sysSNMPMgrAddress": a3sysSNMPMgrAddress,
       "a3sysSNMPMgrMask": a3sysSNMPMgrMask,
       "a3sysSNMPMgrStatus": a3sysSNMPMgrStatus,
       "a3sysTelnetMgrTable": a3sysTelnetMgrTable,
       "a3sysTelnetMgrEntry": a3sysTelnetMgrEntry,
       "a3sysTelnetMgrAddress": a3sysTelnetMgrAddress,
       "a3sysTelnetMgrStatus": a3sysTelnetMgrStatus,
       "a3sysPasswordTable": a3sysPasswordTable,
       "a3sysPasswordEntry": a3sysPasswordEntry,
       "a3sysPwStatus": a3sysPwStatus,
       "a3sysUserName": a3sysUserName,
       "a3sysUserLevel": a3sysUserLevel,
       "a3sysOldPassword": a3sysOldPassword,
       "a3sysNewPassword": a3sysNewPassword,
       "a3sysSnmpPasswordCtl": a3sysSnmpPasswordCtl,
       "a3ComSysMisc": a3ComSysMisc,
       "a3sysNetMapTime": a3sysNetMapTime,
       "a3sysUIBinary": a3sysUIBinary,
       "a3sysChangeTimestamp": a3sysChangeTimestamp,
       "a3sysCpuUtil": a3sysCpuUtil,
       "a3sysCpuBrdMacAddr": a3sysCpuBrdMacAddr,
       "a3sysExpMacAddr": a3sysExpMacAddr,
       "a3sysVportTimestamp": a3sysVportTimestamp,
       "a3sysDefDrive": a3sysDefDrive,
       "a3sysDefDriveType": a3sysDefDriveType,
       "a3sysDriveStatus": a3sysDriveStatus,
       "a3sysBogusDhcpSvr": a3sysBogusDhcpSvr,
       "a3sysNb2EepromVers": a3sysNb2EepromVers,
       "a3sysX25Conns": a3sysX25Conns,
       "a3ComFW": a3ComFW,
       "a3sysFwSerBaudCons": a3sysFwSerBaudCons,
       "a3sysFwSerBaudAux": a3sysFwSerBaudAux,
       "a3sysFwSelfTest": a3sysFwSelfTest,
       "a3ComBoot": a3ComBoot,
       "a3sysReBoot": a3sysReBoot,
       "a3sysTestBootTime": a3sysTestBootTime,
       "a3sysStartUpAction": a3sysStartUpAction,
       "a3sysTestRecoveryTimer": a3sysTestRecoveryTimer,
       "a3sysDirectedReBoots": a3sysDirectedReBoots,
       "a3sysExceptionReBoots": a3sysExceptionReBoots,
       "a3sysBootDump": a3sysBootDump,
       "a3sysBootSources": a3sysBootSources,
       "a3sysUserBootListTable": a3sysUserBootListTable,
       "a3sysUserBootListEntry": a3sysUserBootListEntry,
       "a3sysUblSource": a3sysUblSource,
       "a3sysUblDevice": a3sysUblDevice,
       "a3sysUblFileName": a3sysUblFileName,
       "a3sysUblNetFile": a3sysUblNetFile,
       "a3sysUblSlot": a3sysUblSlot,
       "a3sysUblInterface": a3sysUblInterface,
       "a3sysUblMaxRetries": a3sysUblMaxRetries,
       "a3sysUblConfigFileDevice": a3sysUblConfigFileDevice,
       "a3sysUblConfigFilePath": a3sysUblConfigFilePath,
       "a3sysUblConfigProt": a3sysUblConfigProt,
       "a3sysUblConfigUserName": a3sysUblConfigUserName,
       "a3sysUblConfigPassword": a3sysUblConfigPassword,
       "a3sysUblConfigAcct": a3sysUblConfigAcct,
       "a3sysUblMacAddress": a3sysUblMacAddress,
       "a3sysUblCanonicalFlag": a3sysUblCanonicalFlag,
       "a3sysUblRemoteProt": a3sysUblRemoteProt,
       "a3sysUblBaudRate": a3sysUblBaudRate,
       "a3sysUblClockSource": a3sysUblClockSource,
       "a3sysUblConnectorType": a3sysUblConnectorType,
       "a3sysUblWanAddress": a3sysUblWanAddress,
       "a3sysUblClientIpAddr": a3sysUblClientIpAddr,
       "a3sysUblServerIpAddr": a3sysUblServerIpAddr,
       "a3sysUblGwIpAddr": a3sysUblGwIpAddr,
       "a3sysUblConfigFileIpAddr": a3sysUblConfigFileIpAddr,
       "a3sysUblIpMask": a3sysUblIpMask,
       "a3sysUblAddressDiscovery": a3sysUblAddressDiscovery,
       "a3sysUblPassword": a3sysUblPassword,
       "a3sysIioBootTable": a3sysIioBootTable,
       "a3sysIioBootEntry": a3sysIioBootEntry,
       "a3sysIioBootSlot": a3sysIioBootSlot,
       "a3sysIioBootFileName": a3sysIioBootFileName,
       "a3sysIioBootState": a3sysIioBootState,
       "a3sysIioBootTime": a3sysIioBootTime,
       "a3sysIioBootImage": a3sysIioBootImage,
       "a3ComLastBoot": a3ComLastBoot,
       "a3sysLastBootSource": a3sysLastBootSource,
       "a3sysLastBootError": a3sysLastBootError,
       "a3sysLastBootDate": a3sysLastBootDate,
       "a3sysLbConfigFileIpAddr": a3sysLbConfigFileIpAddr,
       "a3sysLbGwIpAddr": a3sysLbGwIpAddr,
       "a3sysLbIpMask": a3sysLbIpMask,
       "a3sysLbConfigDevice": a3sysLbConfigDevice,
       "a3sysLbConfigFilePath": a3sysLbConfigFilePath,
       "a3sysLbConfigUserName": a3sysLbConfigUserName,
       "a3ComFileMgmt": a3ComFileMgmt,
       "a3sysFmOperation": a3sysFmOperation,
       "a3sysFmSourceIpAddr": a3sysFmSourceIpAddr,
       "a3sysFmSourceFile": a3sysFmSourceFile,
       "a3sysFmTargetIpAddr": a3sysFmTargetIpAddr,
       "a3sysFmTargetFile": a3sysFmTargetFile,
       "a3sysFmStatus": a3sysFmStatus,
       "a3sysFmTimeStamp": a3sysFmTimeStamp,
       "a3sysFmError": a3sysFmError,
       "a3ComFileList": a3ComFileList,
       "a3sysDfTime": a3sysDfTime,
       "a3sysDfPath": a3sysDfPath,
       "a3sysDfTable": a3sysDfTable,
       "a3sysDfEntry": a3sysDfEntry,
       "a3sysDfName": a3sysDfName,
       "a3sysDfDir": a3sysDfDir,
       "a3ComDfTotalSpace": a3ComDfTotalSpace,
       "a3ComDfAvailableSpace": a3ComDfAvailableSpace,
       "a3ComFmCksum": a3ComFmCksum,
       "a3sysFmCksum": a3sysFmCksum,
       "a3sysFmCksumFile": a3sysFmCksumFile,
       "a3sysFmCksumTime": a3sysFmCksumTime,
       "a3ComFileInfo": a3ComFileInfo,
       "a3sysFiName": a3sysFiName,
       "a3sysFiDate": a3sysFiDate,
       "a3sysFiTimeStamp": a3sysFiTimeStamp,
       "a3sysFmSize": a3sysFmSize,
       "a3ComRecovery": a3ComRecovery,
       "a3sysIioRecoveryTable": a3sysIioRecoveryTable,
       "a3sysIioRecoveryEntry": a3sysIioRecoveryEntry,
       "a3sysIioRecoverySlot": a3sysIioRecoverySlot,
       "a3sysIioRecoveryProcedure": a3sysIioRecoveryProcedure,
       "a3sysIioRecoverySelect": a3sysIioRecoverySelect}
)
