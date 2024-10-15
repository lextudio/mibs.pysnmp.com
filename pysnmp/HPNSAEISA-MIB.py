# SNMP MIB module (HPNSAEISA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSAEISA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:20 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaEISA_ObjectIdentity = ObjectIdentity
hpnsaEISA = _HpnsaEISA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9)
)
_HpnsaEISAMibRev_ObjectIdentity = ObjectIdentity
hpnsaEISAMibRev = _HpnsaEISAMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 1)
)


class _HpnsaEISAMibRevMajor_Type(Integer32):
    """Custom type hpnsaEISAMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaEISAMibRevMajor_Type.__name__ = "Integer32"
_HpnsaEISAMibRevMajor_Object = MibScalar
hpnsaEISAMibRevMajor = _HpnsaEISAMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 1, 1),
    _HpnsaEISAMibRevMajor_Type()
)
hpnsaEISAMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMibRevMajor.setStatus("mandatory")


class _HpnsaEISAMibRevMinor_Type(Integer32):
    """Custom type hpnsaEISAMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEISAMibRevMinor_Type.__name__ = "Integer32"
_HpnsaEISAMibRevMinor_Object = MibScalar
hpnsaEISAMibRevMinor = _HpnsaEISAMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 1, 2),
    _HpnsaEISAMibRevMinor_Type()
)
hpnsaEISAMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMibRevMinor.setStatus("mandatory")
_HpnsaEISAAgent_ObjectIdentity = ObjectIdentity
hpnsaEISAAgent = _HpnsaEISAAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2)
)
_HpnsaEISAAgentTable_Object = MibTable
hpnsaEISAAgentTable = _HpnsaEISAAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaEISAAgentTable.setStatus("mandatory")
_HpnsaEISAAgentEntry_Object = MibTableRow
hpnsaEISAAgentEntry = _HpnsaEISAAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1)
)
hpnsaEISAAgentEntry.setIndexNames(
    (0, "HPNSAEISA-MIB", "hpnsaEISAAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEISAAgentEntry.setStatus("mandatory")


class _HpnsaEISAAgentIndex_Type(Integer32):
    """Custom type hpnsaEISAAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISAAgentIndex_Type.__name__ = "Integer32"
_HpnsaEISAAgentIndex_Object = MibTableColumn
hpnsaEISAAgentIndex = _HpnsaEISAAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 1),
    _HpnsaEISAAgentIndex_Type()
)
hpnsaEISAAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAAgentIndex.setStatus("mandatory")


class _HpnsaEISAAgentName_Type(DisplayString):
    """Custom type hpnsaEISAAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEISAAgentName_Type.__name__ = "DisplayString"
_HpnsaEISAAgentName_Object = MibTableColumn
hpnsaEISAAgentName = _HpnsaEISAAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 2),
    _HpnsaEISAAgentName_Type()
)
hpnsaEISAAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAAgentName.setStatus("mandatory")


class _HpnsaEISAAgentVersion_Type(DisplayString):
    """Custom type hpnsaEISAAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnsaEISAAgentVersion_Type.__name__ = "DisplayString"
_HpnsaEISAAgentVersion_Object = MibTableColumn
hpnsaEISAAgentVersion = _HpnsaEISAAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 3),
    _HpnsaEISAAgentVersion_Type()
)
hpnsaEISAAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAAgentVersion.setStatus("mandatory")


class _HpnsaEISAAgentDate_Type(OctetString):
    """Custom type hpnsaEISAAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaEISAAgentDate_Type.__name__ = "OctetString"
_HpnsaEISAAgentDate_Object = MibTableColumn
hpnsaEISAAgentDate = _HpnsaEISAAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 4),
    _HpnsaEISAAgentDate_Type()
)
hpnsaEISAAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAAgentDate.setStatus("mandatory")
_HpnsaEISACfgUtil_ObjectIdentity = ObjectIdentity
hpnsaEISACfgUtil = _HpnsaEISACfgUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 3)
)


class _HpnsaEISACfgUtilRevMajor_Type(Integer32):
    """Custom type hpnsaEISACfgUtilRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaEISACfgUtilRevMajor_Type.__name__ = "Integer32"
_HpnsaEISACfgUtilRevMajor_Object = MibScalar
hpnsaEISACfgUtilRevMajor = _HpnsaEISACfgUtilRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 3, 1),
    _HpnsaEISACfgUtilRevMajor_Type()
)
hpnsaEISACfgUtilRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISACfgUtilRevMajor.setStatus("mandatory")


class _HpnsaEISACfgUtilRevMinor_Type(Integer32):
    """Custom type hpnsaEISACfgUtilRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEISACfgUtilRevMinor_Type.__name__ = "Integer32"
_HpnsaEISACfgUtilRevMinor_Object = MibScalar
hpnsaEISACfgUtilRevMinor = _HpnsaEISACfgUtilRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 3, 2),
    _HpnsaEISACfgUtilRevMinor_Type()
)
hpnsaEISACfgUtilRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISACfgUtilRevMinor.setStatus("mandatory")
_HpnsaEISASlotInfo_ObjectIdentity = ObjectIdentity
hpnsaEISASlotInfo = _HpnsaEISASlotInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4)
)
_HpnsaEISABoardTable_Object = MibTable
hpnsaEISABoardTable = _HpnsaEISABoardTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1)
)
if mibBuilder.loadTexts:
    hpnsaEISABoardTable.setStatus("mandatory")
_HpnsaEISABoardEntry_Object = MibTableRow
hpnsaEISABoardEntry = _HpnsaEISABoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1)
)
hpnsaEISABoardEntry.setIndexNames(
    (0, "HPNSAEISA-MIB", "hpnsaEISASlotIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEISABoardEntry.setStatus("mandatory")
_HpnsaEISASlotIndex_Type = Integer32
_HpnsaEISASlotIndex_Object = MibTableColumn
hpnsaEISASlotIndex = _HpnsaEISASlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 1),
    _HpnsaEISASlotIndex_Type()
)
hpnsaEISASlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISASlotIndex.setStatus("mandatory")


class _HpnsaEISASlotType_Type(Integer32):
    """Custom type hpnsaEISASlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("embedded", 1),
          ("expansion", 0),
          ("reserved", 3),
          ("virtual", 2))
    )


_HpnsaEISASlotType_Type.__name__ = "Integer32"
_HpnsaEISASlotType_Object = MibTableColumn
hpnsaEISASlotType = _HpnsaEISASlotType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 2),
    _HpnsaEISASlotType_Type()
)
hpnsaEISASlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISASlotType.setStatus("mandatory")
_HpnsaEISACfgRevMajor_Type = Integer32
_HpnsaEISACfgRevMajor_Object = MibTableColumn
hpnsaEISACfgRevMajor = _HpnsaEISACfgRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 3),
    _HpnsaEISACfgRevMajor_Type()
)
hpnsaEISACfgRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISACfgRevMajor.setStatus("mandatory")
_HpnsaEISACfgRevMinor_Type = Integer32
_HpnsaEISACfgRevMinor_Object = MibTableColumn
hpnsaEISACfgRevMinor = _HpnsaEISACfgRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 4),
    _HpnsaEISACfgRevMinor_Type()
)
hpnsaEISACfgRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISACfgRevMinor.setStatus("mandatory")


class _HpnsaEISABoardID_Type(DisplayString):
    """Custom type hpnsaEISABoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_HpnsaEISABoardID_Type.__name__ = "DisplayString"
_HpnsaEISABoardID_Object = MibTableColumn
hpnsaEISABoardID = _HpnsaEISABoardID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 5),
    _HpnsaEISABoardID_Type()
)
hpnsaEISABoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISABoardID.setStatus("mandatory")
_HpnsaEISABoardDupCfg_Type = Integer32
_HpnsaEISABoardDupCfg_Object = MibTableColumn
hpnsaEISABoardDupCfg = _HpnsaEISABoardDupCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 6),
    _HpnsaEISABoardDupCfg_Type()
)
hpnsaEISABoardDupCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISABoardDupCfg.setStatus("mandatory")
_HpnsaEISANumFunctions_Type = Integer32
_HpnsaEISANumFunctions_Object = MibTableColumn
hpnsaEISANumFunctions = _HpnsaEISANumFunctions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 7),
    _HpnsaEISANumFunctions_Type()
)
hpnsaEISANumFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISANumFunctions.setStatus("mandatory")
_HpnsaEISAFunctTable_Object = MibTable
hpnsaEISAFunctTable = _HpnsaEISAFunctTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2)
)
if mibBuilder.loadTexts:
    hpnsaEISAFunctTable.setStatus("mandatory")
_HpnsaEISAFunctEntry_Object = MibTableRow
hpnsaEISAFunctEntry = _HpnsaEISAFunctEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1)
)
hpnsaEISAFunctEntry.setIndexNames(
    (0, "HPNSAEISA-MIB", "hpnsaEISAFunctSlotIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISAFunctIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEISAFunctEntry.setStatus("mandatory")


class _HpnsaEISAFunctSlotIndex_Type(Integer32):
    """Custom type hpnsaEISAFunctSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISAFunctSlotIndex_Type.__name__ = "Integer32"
_HpnsaEISAFunctSlotIndex_Object = MibTableColumn
hpnsaEISAFunctSlotIndex = _HpnsaEISAFunctSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 1),
    _HpnsaEISAFunctSlotIndex_Type()
)
hpnsaEISAFunctSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAFunctSlotIndex.setStatus("mandatory")


class _HpnsaEISAFunctIndex_Type(Integer32):
    """Custom type hpnsaEISAFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISAFunctIndex_Type.__name__ = "Integer32"
_HpnsaEISAFunctIndex_Object = MibTableColumn
hpnsaEISAFunctIndex = _HpnsaEISAFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 2),
    _HpnsaEISAFunctIndex_Type()
)
hpnsaEISAFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAFunctIndex.setStatus("mandatory")


class _HpnsaEISAFunctStatus_Type(Integer32):
    """Custom type hpnsaEISAFunctStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_HpnsaEISAFunctStatus_Type.__name__ = "Integer32"
_HpnsaEISAFunctStatus_Object = MibTableColumn
hpnsaEISAFunctStatus = _HpnsaEISAFunctStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 3),
    _HpnsaEISAFunctStatus_Type()
)
hpnsaEISAFunctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAFunctStatus.setStatus("mandatory")


class _HpnsaEISAFunctType_Type(DisplayString):
    """Custom type hpnsaEISAFunctType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_HpnsaEISAFunctType_Type.__name__ = "DisplayString"
_HpnsaEISAFunctType_Object = MibTableColumn
hpnsaEISAFunctType = _HpnsaEISAFunctType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 4),
    _HpnsaEISAFunctType_Type()
)
hpnsaEISAFunctType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAFunctType.setStatus("mandatory")
_HpnsaEISAMemTable_Object = MibTable
hpnsaEISAMemTable = _HpnsaEISAMemTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3)
)
if mibBuilder.loadTexts:
    hpnsaEISAMemTable.setStatus("mandatory")
_HpnsaEISAMemEntry_Object = MibTableRow
hpnsaEISAMemEntry = _HpnsaEISAMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1)
)
hpnsaEISAMemEntry.setIndexNames(
    (0, "HPNSAEISA-MIB", "hpnsaEISAMemSlotIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISAMemFunctIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISAMemAllocIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEISAMemEntry.setStatus("mandatory")


class _HpnsaEISAMemSlotIndex_Type(Integer32):
    """Custom type hpnsaEISAMemSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISAMemSlotIndex_Type.__name__ = "Integer32"
_HpnsaEISAMemSlotIndex_Object = MibTableColumn
hpnsaEISAMemSlotIndex = _HpnsaEISAMemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 1),
    _HpnsaEISAMemSlotIndex_Type()
)
hpnsaEISAMemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMemSlotIndex.setStatus("mandatory")


class _HpnsaEISAMemFunctIndex_Type(Integer32):
    """Custom type hpnsaEISAMemFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISAMemFunctIndex_Type.__name__ = "Integer32"
_HpnsaEISAMemFunctIndex_Object = MibTableColumn
hpnsaEISAMemFunctIndex = _HpnsaEISAMemFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 2),
    _HpnsaEISAMemFunctIndex_Type()
)
hpnsaEISAMemFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMemFunctIndex.setStatus("mandatory")


class _HpnsaEISAMemAllocIndex_Type(Integer32):
    """Custom type hpnsaEISAMemAllocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISAMemAllocIndex_Type.__name__ = "Integer32"
_HpnsaEISAMemAllocIndex_Object = MibTableColumn
hpnsaEISAMemAllocIndex = _HpnsaEISAMemAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 3),
    _HpnsaEISAMemAllocIndex_Type()
)
hpnsaEISAMemAllocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMemAllocIndex.setStatus("mandatory")
_HpnsaEISAMemStartAddr_Type = Integer32
_HpnsaEISAMemStartAddr_Object = MibTableColumn
hpnsaEISAMemStartAddr = _HpnsaEISAMemStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 4),
    _HpnsaEISAMemStartAddr_Type()
)
hpnsaEISAMemStartAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMemStartAddr.setStatus("mandatory")
_HpnsaEISAMemSize_Type = Integer32
_HpnsaEISAMemSize_Object = MibTableColumn
hpnsaEISAMemSize = _HpnsaEISAMemSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 5),
    _HpnsaEISAMemSize_Type()
)
hpnsaEISAMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMemSize.setStatus("mandatory")


class _HpnsaEISAMemShare_Type(Integer32):
    """Custom type hpnsaEISAMemShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonshareable", 0),
          ("shareable", 1))
    )


_HpnsaEISAMemShare_Type.__name__ = "Integer32"
_HpnsaEISAMemShare_Object = MibTableColumn
hpnsaEISAMemShare = _HpnsaEISAMemShare_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 6),
    _HpnsaEISAMemShare_Type()
)
hpnsaEISAMemShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMemShare.setStatus("mandatory")


class _HpnsaEISAMemType_Type(Integer32):
    """Custom type hpnsaEISAMemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expanded", 2),
          ("systemBaseOrExtended", 1),
          ("unknown", 0),
          ("virtual", 3))
    )


_HpnsaEISAMemType_Type.__name__ = "Integer32"
_HpnsaEISAMemType_Object = MibTableColumn
hpnsaEISAMemType = _HpnsaEISAMemType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 7),
    _HpnsaEISAMemType_Type()
)
hpnsaEISAMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMemType.setStatus("mandatory")


class _HpnsaEISAMemCache_Type(Integer32):
    """Custom type hpnsaEISAMemCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notCached", 1),
          ("writeBackCached", 3),
          ("writeThroughCached", 2))
    )


_HpnsaEISAMemCache_Type.__name__ = "Integer32"
_HpnsaEISAMemCache_Object = MibTableColumn
hpnsaEISAMemCache = _HpnsaEISAMemCache_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 8),
    _HpnsaEISAMemCache_Type()
)
hpnsaEISAMemCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMemCache.setStatus("mandatory")


class _HpnsaEISAMemAccess_Type(Integer32):
    """Custom type hpnsaEISAMemAccess based on Integer32"""
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


_HpnsaEISAMemAccess_Type.__name__ = "Integer32"
_HpnsaEISAMemAccess_Object = MibTableColumn
hpnsaEISAMemAccess = _HpnsaEISAMemAccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 9),
    _HpnsaEISAMemAccess_Type()
)
hpnsaEISAMemAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAMemAccess.setStatus("mandatory")
_HpnsaEISAIntTable_Object = MibTable
hpnsaEISAIntTable = _HpnsaEISAIntTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4)
)
if mibBuilder.loadTexts:
    hpnsaEISAIntTable.setStatus("mandatory")
_HpnsaEISAIntEntry_Object = MibTableRow
hpnsaEISAIntEntry = _HpnsaEISAIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1)
)
hpnsaEISAIntEntry.setIndexNames(
    (0, "HPNSAEISA-MIB", "hpnsaEISAIntSlotIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISAIntFunctIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISAIntAllocIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEISAIntEntry.setStatus("mandatory")


class _HpnsaEISAIntSlotIndex_Type(Integer32):
    """Custom type hpnsaEISAIntSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISAIntSlotIndex_Type.__name__ = "Integer32"
_HpnsaEISAIntSlotIndex_Object = MibTableColumn
hpnsaEISAIntSlotIndex = _HpnsaEISAIntSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 1),
    _HpnsaEISAIntSlotIndex_Type()
)
hpnsaEISAIntSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAIntSlotIndex.setStatus("mandatory")


class _HpnsaEISAIntFunctIndex_Type(Integer32):
    """Custom type hpnsaEISAIntFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISAIntFunctIndex_Type.__name__ = "Integer32"
_HpnsaEISAIntFunctIndex_Object = MibTableColumn
hpnsaEISAIntFunctIndex = _HpnsaEISAIntFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 2),
    _HpnsaEISAIntFunctIndex_Type()
)
hpnsaEISAIntFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAIntFunctIndex.setStatus("mandatory")


class _HpnsaEISAIntAllocIndex_Type(Integer32):
    """Custom type hpnsaEISAIntAllocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISAIntAllocIndex_Type.__name__ = "Integer32"
_HpnsaEISAIntAllocIndex_Object = MibTableColumn
hpnsaEISAIntAllocIndex = _HpnsaEISAIntAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 3),
    _HpnsaEISAIntAllocIndex_Type()
)
hpnsaEISAIntAllocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAIntAllocIndex.setStatus("mandatory")


class _HpnsaEISAIntNum_Type(Integer32):
    """Custom type hpnsaEISAIntNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEISAIntNum_Type.__name__ = "Integer32"
_HpnsaEISAIntNum_Object = MibTableColumn
hpnsaEISAIntNum = _HpnsaEISAIntNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 4),
    _HpnsaEISAIntNum_Type()
)
hpnsaEISAIntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAIntNum.setStatus("mandatory")


class _HpnsaEISAIntShare_Type(Integer32):
    """Custom type hpnsaEISAIntShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notShared", 0),
          ("shared", 1))
    )


_HpnsaEISAIntShare_Type.__name__ = "Integer32"
_HpnsaEISAIntShare_Object = MibTableColumn
hpnsaEISAIntShare = _HpnsaEISAIntShare_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 5),
    _HpnsaEISAIntShare_Type()
)
hpnsaEISAIntShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAIntShare.setStatus("mandatory")


class _HpnsaEISAIntTrigger_Type(Integer32):
    """Custom type hpnsaEISAIntTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("edgeTriggered", 0),
          ("levelTriggered", 1))
    )


_HpnsaEISAIntTrigger_Type.__name__ = "Integer32"
_HpnsaEISAIntTrigger_Object = MibTableColumn
hpnsaEISAIntTrigger = _HpnsaEISAIntTrigger_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 6),
    _HpnsaEISAIntTrigger_Type()
)
hpnsaEISAIntTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAIntTrigger.setStatus("mandatory")
_HpnsaEISADmaTable_Object = MibTable
hpnsaEISADmaTable = _HpnsaEISADmaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5)
)
if mibBuilder.loadTexts:
    hpnsaEISADmaTable.setStatus("mandatory")
_HpnsaEISADmaEntry_Object = MibTableRow
hpnsaEISADmaEntry = _HpnsaEISADmaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1)
)
hpnsaEISADmaEntry.setIndexNames(
    (0, "HPNSAEISA-MIB", "hpnsaEISADmaSlotIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISADmaFunctIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISADmaAllocIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEISADmaEntry.setStatus("mandatory")


class _HpnsaEISADmaSlotIndex_Type(Integer32):
    """Custom type hpnsaEISADmaSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISADmaSlotIndex_Type.__name__ = "Integer32"
_HpnsaEISADmaSlotIndex_Object = MibTableColumn
hpnsaEISADmaSlotIndex = _HpnsaEISADmaSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 1),
    _HpnsaEISADmaSlotIndex_Type()
)
hpnsaEISADmaSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISADmaSlotIndex.setStatus("mandatory")


class _HpnsaEISADmaFunctIndex_Type(Integer32):
    """Custom type hpnsaEISADmaFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISADmaFunctIndex_Type.__name__ = "Integer32"
_HpnsaEISADmaFunctIndex_Object = MibTableColumn
hpnsaEISADmaFunctIndex = _HpnsaEISADmaFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 2),
    _HpnsaEISADmaFunctIndex_Type()
)
hpnsaEISADmaFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISADmaFunctIndex.setStatus("mandatory")


class _HpnsaEISADmaAllocIndex_Type(Integer32):
    """Custom type hpnsaEISADmaAllocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEISADmaAllocIndex_Type.__name__ = "Integer32"
_HpnsaEISADmaAllocIndex_Object = MibTableColumn
hpnsaEISADmaAllocIndex = _HpnsaEISADmaAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 3),
    _HpnsaEISADmaAllocIndex_Type()
)
hpnsaEISADmaAllocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISADmaAllocIndex.setStatus("mandatory")


class _HpnsaEISADmaChannelNum_Type(Integer32):
    """Custom type hpnsaEISADmaChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEISADmaChannelNum_Type.__name__ = "Integer32"
_HpnsaEISADmaChannelNum_Object = MibTableColumn
hpnsaEISADmaChannelNum = _HpnsaEISADmaChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 4),
    _HpnsaEISADmaChannelNum_Type()
)
hpnsaEISADmaChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISADmaChannelNum.setStatus("mandatory")


class _HpnsaEISADmaShare_Type(Integer32):
    """Custom type hpnsaEISADmaShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notShared", 0),
          ("shared", 1))
    )


_HpnsaEISADmaShare_Type.__name__ = "Integer32"
_HpnsaEISADmaShare_Object = MibTableColumn
hpnsaEISADmaShare = _HpnsaEISADmaShare_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 5),
    _HpnsaEISADmaShare_Type()
)
hpnsaEISADmaShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISADmaShare.setStatus("mandatory")


class _HpnsaEISADmaTiming_Type(Integer32):
    """Custom type hpnsaEISADmaTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("burstC", 3),
          ("defaultISACompat", 0),
          ("typeA", 1),
          ("typeB", 2))
    )


_HpnsaEISADmaTiming_Type.__name__ = "Integer32"
_HpnsaEISADmaTiming_Object = MibTableColumn
hpnsaEISADmaTiming = _HpnsaEISADmaTiming_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 6),
    _HpnsaEISADmaTiming_Type()
)
hpnsaEISADmaTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISADmaTiming.setStatus("mandatory")


class _HpnsaEISADmaXferSize_Type(Integer32):
    """Custom type hpnsaEISADmaXferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightBit", 0),
          ("sixteenBit", 1),
          ("thirtyTwoBit", 2))
    )


_HpnsaEISADmaXferSize_Type.__name__ = "Integer32"
_HpnsaEISADmaXferSize_Object = MibTableColumn
hpnsaEISADmaXferSize = _HpnsaEISADmaXferSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 7),
    _HpnsaEISADmaXferSize_Type()
)
hpnsaEISADmaXferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISADmaXferSize.setStatus("mandatory")
_HpnsaEISAPortTable_Object = MibTable
hpnsaEISAPortTable = _HpnsaEISAPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6)
)
if mibBuilder.loadTexts:
    hpnsaEISAPortTable.setStatus("mandatory")
_HpnsaEISAPortEntry_Object = MibTableRow
hpnsaEISAPortEntry = _HpnsaEISAPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1)
)
hpnsaEISAPortEntry.setIndexNames(
    (0, "HPNSAEISA-MIB", "hpnsaEISAPortSlotIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISAPortFunctIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISAPortEntryIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEISAPortEntry.setStatus("mandatory")
_HpnsaEISAPortSlotIndex_Type = Integer32
_HpnsaEISAPortSlotIndex_Object = MibTableColumn
hpnsaEISAPortSlotIndex = _HpnsaEISAPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 1),
    _HpnsaEISAPortSlotIndex_Type()
)
hpnsaEISAPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAPortSlotIndex.setStatus("mandatory")
_HpnsaEISAPortFunctIndex_Type = Integer32
_HpnsaEISAPortFunctIndex_Object = MibTableColumn
hpnsaEISAPortFunctIndex = _HpnsaEISAPortFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 2),
    _HpnsaEISAPortFunctIndex_Type()
)
hpnsaEISAPortFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAPortFunctIndex.setStatus("mandatory")
_HpnsaEISAPortEntryIndex_Type = Integer32
_HpnsaEISAPortEntryIndex_Object = MibTableColumn
hpnsaEISAPortEntryIndex = _HpnsaEISAPortEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 3),
    _HpnsaEISAPortEntryIndex_Type()
)
hpnsaEISAPortEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAPortEntryIndex.setStatus("mandatory")
_HpnsaEISAPortAddress_Type = Integer32
_HpnsaEISAPortAddress_Object = MibTableColumn
hpnsaEISAPortAddress = _HpnsaEISAPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 4),
    _HpnsaEISAPortAddress_Type()
)
hpnsaEISAPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAPortAddress.setStatus("mandatory")
_HpnsaEISAPortSize_Type = Integer32
_HpnsaEISAPortSize_Object = MibTableColumn
hpnsaEISAPortSize = _HpnsaEISAPortSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 5),
    _HpnsaEISAPortSize_Type()
)
hpnsaEISAPortSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAPortSize.setStatus("mandatory")


class _HpnsaEISAPortShared_Type(Integer32):
    """Custom type hpnsaEISAPortShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notShared", 0),
          ("shared", 1))
    )


_HpnsaEISAPortShared_Type.__name__ = "Integer32"
_HpnsaEISAPortShared_Object = MibTableColumn
hpnsaEISAPortShared = _HpnsaEISAPortShared_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 6),
    _HpnsaEISAPortShared_Type()
)
hpnsaEISAPortShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAPortShared.setStatus("mandatory")
_HpnsaEISAPortInitTable_Object = MibTable
hpnsaEISAPortInitTable = _HpnsaEISAPortInitTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7)
)
if mibBuilder.loadTexts:
    hpnsaEISAPortInitTable.setStatus("mandatory")
_HpnsaEISAPortInitEntry_Object = MibTableRow
hpnsaEISAPortInitEntry = _HpnsaEISAPortInitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1)
)
hpnsaEISAPortInitEntry.setIndexNames(
    (0, "HPNSAEISA-MIB", "hpnsaEISAPortInitSlotIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISAPortInitFunctIndex"),
    (0, "HPNSAEISA-MIB", "hpnsaEISAPortInitEntryIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEISAPortInitEntry.setStatus("mandatory")
_HpnsaEISAPortInitSlotIndex_Type = Integer32
_HpnsaEISAPortInitSlotIndex_Object = MibTableColumn
hpnsaEISAPortInitSlotIndex = _HpnsaEISAPortInitSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 1),
    _HpnsaEISAPortInitSlotIndex_Type()
)
hpnsaEISAPortInitSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAPortInitSlotIndex.setStatus("mandatory")
_HpnsaEISAPortInitFunctIndex_Type = Integer32
_HpnsaEISAPortInitFunctIndex_Object = MibTableColumn
hpnsaEISAPortInitFunctIndex = _HpnsaEISAPortInitFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 2),
    _HpnsaEISAPortInitFunctIndex_Type()
)
hpnsaEISAPortInitFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAPortInitFunctIndex.setStatus("mandatory")
_HpnsaEISAPortInitEntryIndex_Type = Integer32
_HpnsaEISAPortInitEntryIndex_Object = MibTableColumn
hpnsaEISAPortInitEntryIndex = _HpnsaEISAPortInitEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 3),
    _HpnsaEISAPortInitEntryIndex_Type()
)
hpnsaEISAPortInitEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAPortInitEntryIndex.setStatus("mandatory")


class _HpnsaEISAPortInitData_Type(OctetString):
    """Custom type hpnsaEISAPortInitData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_HpnsaEISAPortInitData_Type.__name__ = "OctetString"
_HpnsaEISAPortInitData_Object = MibTableColumn
hpnsaEISAPortInitData = _HpnsaEISAPortInitData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 4),
    _HpnsaEISAPortInitData_Type()
)
hpnsaEISAPortInitData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEISAPortInitData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSAEISA-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaEISA": hpnsaEISA,
       "hpnsaEISAMibRev": hpnsaEISAMibRev,
       "hpnsaEISAMibRevMajor": hpnsaEISAMibRevMajor,
       "hpnsaEISAMibRevMinor": hpnsaEISAMibRevMinor,
       "hpnsaEISAAgent": hpnsaEISAAgent,
       "hpnsaEISAAgentTable": hpnsaEISAAgentTable,
       "hpnsaEISAAgentEntry": hpnsaEISAAgentEntry,
       "hpnsaEISAAgentIndex": hpnsaEISAAgentIndex,
       "hpnsaEISAAgentName": hpnsaEISAAgentName,
       "hpnsaEISAAgentVersion": hpnsaEISAAgentVersion,
       "hpnsaEISAAgentDate": hpnsaEISAAgentDate,
       "hpnsaEISACfgUtil": hpnsaEISACfgUtil,
       "hpnsaEISACfgUtilRevMajor": hpnsaEISACfgUtilRevMajor,
       "hpnsaEISACfgUtilRevMinor": hpnsaEISACfgUtilRevMinor,
       "hpnsaEISASlotInfo": hpnsaEISASlotInfo,
       "hpnsaEISABoardTable": hpnsaEISABoardTable,
       "hpnsaEISABoardEntry": hpnsaEISABoardEntry,
       "hpnsaEISASlotIndex": hpnsaEISASlotIndex,
       "hpnsaEISASlotType": hpnsaEISASlotType,
       "hpnsaEISACfgRevMajor": hpnsaEISACfgRevMajor,
       "hpnsaEISACfgRevMinor": hpnsaEISACfgRevMinor,
       "hpnsaEISABoardID": hpnsaEISABoardID,
       "hpnsaEISABoardDupCfg": hpnsaEISABoardDupCfg,
       "hpnsaEISANumFunctions": hpnsaEISANumFunctions,
       "hpnsaEISAFunctTable": hpnsaEISAFunctTable,
       "hpnsaEISAFunctEntry": hpnsaEISAFunctEntry,
       "hpnsaEISAFunctSlotIndex": hpnsaEISAFunctSlotIndex,
       "hpnsaEISAFunctIndex": hpnsaEISAFunctIndex,
       "hpnsaEISAFunctStatus": hpnsaEISAFunctStatus,
       "hpnsaEISAFunctType": hpnsaEISAFunctType,
       "hpnsaEISAMemTable": hpnsaEISAMemTable,
       "hpnsaEISAMemEntry": hpnsaEISAMemEntry,
       "hpnsaEISAMemSlotIndex": hpnsaEISAMemSlotIndex,
       "hpnsaEISAMemFunctIndex": hpnsaEISAMemFunctIndex,
       "hpnsaEISAMemAllocIndex": hpnsaEISAMemAllocIndex,
       "hpnsaEISAMemStartAddr": hpnsaEISAMemStartAddr,
       "hpnsaEISAMemSize": hpnsaEISAMemSize,
       "hpnsaEISAMemShare": hpnsaEISAMemShare,
       "hpnsaEISAMemType": hpnsaEISAMemType,
       "hpnsaEISAMemCache": hpnsaEISAMemCache,
       "hpnsaEISAMemAccess": hpnsaEISAMemAccess,
       "hpnsaEISAIntTable": hpnsaEISAIntTable,
       "hpnsaEISAIntEntry": hpnsaEISAIntEntry,
       "hpnsaEISAIntSlotIndex": hpnsaEISAIntSlotIndex,
       "hpnsaEISAIntFunctIndex": hpnsaEISAIntFunctIndex,
       "hpnsaEISAIntAllocIndex": hpnsaEISAIntAllocIndex,
       "hpnsaEISAIntNum": hpnsaEISAIntNum,
       "hpnsaEISAIntShare": hpnsaEISAIntShare,
       "hpnsaEISAIntTrigger": hpnsaEISAIntTrigger,
       "hpnsaEISADmaTable": hpnsaEISADmaTable,
       "hpnsaEISADmaEntry": hpnsaEISADmaEntry,
       "hpnsaEISADmaSlotIndex": hpnsaEISADmaSlotIndex,
       "hpnsaEISADmaFunctIndex": hpnsaEISADmaFunctIndex,
       "hpnsaEISADmaAllocIndex": hpnsaEISADmaAllocIndex,
       "hpnsaEISADmaChannelNum": hpnsaEISADmaChannelNum,
       "hpnsaEISADmaShare": hpnsaEISADmaShare,
       "hpnsaEISADmaTiming": hpnsaEISADmaTiming,
       "hpnsaEISADmaXferSize": hpnsaEISADmaXferSize,
       "hpnsaEISAPortTable": hpnsaEISAPortTable,
       "hpnsaEISAPortEntry": hpnsaEISAPortEntry,
       "hpnsaEISAPortSlotIndex": hpnsaEISAPortSlotIndex,
       "hpnsaEISAPortFunctIndex": hpnsaEISAPortFunctIndex,
       "hpnsaEISAPortEntryIndex": hpnsaEISAPortEntryIndex,
       "hpnsaEISAPortAddress": hpnsaEISAPortAddress,
       "hpnsaEISAPortSize": hpnsaEISAPortSize,
       "hpnsaEISAPortShared": hpnsaEISAPortShared,
       "hpnsaEISAPortInitTable": hpnsaEISAPortInitTable,
       "hpnsaEISAPortInitEntry": hpnsaEISAPortInitEntry,
       "hpnsaEISAPortInitSlotIndex": hpnsaEISAPortInitSlotIndex,
       "hpnsaEISAPortInitFunctIndex": hpnsaEISAPortInitFunctIndex,
       "hpnsaEISAPortInitEntryIndex": hpnsaEISAPortInitEntryIndex,
       "hpnsaEISAPortInitData": hpnsaEISAPortInitData}
)
