# SNMP MIB module (LLDP-EXT-DOT1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-EXT-DOT1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:12 2024
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

(lldpExtensions,
 lldpLocPortNum,
 lldpPortConfigEntry,
 lldpRemIndex,
 lldpRemLocalPortNum,
 lldpRemTimeMark) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpExtensions",
    "lldpLocPortNum",
    "lldpPortConfigEntry",
    "lldpRemIndex",
    "lldpRemLocalPortNum",
    "lldpRemTimeMark")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lldpXdot1MIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962)
)
lldpXdot1MIB.setRevisions(
        ("2005-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpXdot1Objects_ObjectIdentity = ObjectIdentity
lldpXdot1Objects = _LldpXdot1Objects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1)
)
_LldpXdot1Config_ObjectIdentity = ObjectIdentity
lldpXdot1Config = _LldpXdot1Config_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1)
)
_LldpXdot1ConfigPortVlanTable_Object = MibTable
lldpXdot1ConfigPortVlanTable = _LldpXdot1ConfigPortVlanTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanTable.setStatus("current")
_LldpXdot1ConfigPortVlanEntry_Object = MibTableRow
lldpXdot1ConfigPortVlanEntry = _LldpXdot1ConfigPortVlanEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanEntry.setStatus("current")


class _LldpXdot1ConfigPortVlanTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigPortVlanTxEnable based on TruthValue"""


_LldpXdot1ConfigPortVlanTxEnable_Object = MibTableColumn
lldpXdot1ConfigPortVlanTxEnable = _LldpXdot1ConfigPortVlanTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 1, 1, 1),
    _LldpXdot1ConfigPortVlanTxEnable_Type()
)
lldpXdot1ConfigPortVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanTxEnable.setStatus("current")
_LldpXdot1ConfigVlanNameTable_Object = MibTable
lldpXdot1ConfigVlanNameTable = _LldpXdot1ConfigVlanNameTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameTable.setStatus("current")
_LldpXdot1ConfigVlanNameEntry_Object = MibTableRow
lldpXdot1ConfigVlanNameEntry = _LldpXdot1ConfigVlanNameEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameEntry.setStatus("current")


class _LldpXdot1ConfigVlanNameTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigVlanNameTxEnable based on TruthValue"""


_LldpXdot1ConfigVlanNameTxEnable_Object = MibTableColumn
lldpXdot1ConfigVlanNameTxEnable = _LldpXdot1ConfigVlanNameTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 2, 1, 1),
    _LldpXdot1ConfigVlanNameTxEnable_Type()
)
lldpXdot1ConfigVlanNameTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameTxEnable.setStatus("current")
_LldpXdot1ConfigProtoVlanTable_Object = MibTable
lldpXdot1ConfigProtoVlanTable = _LldpXdot1ConfigProtoVlanTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanTable.setStatus("current")
_LldpXdot1ConfigProtoVlanEntry_Object = MibTableRow
lldpXdot1ConfigProtoVlanEntry = _LldpXdot1ConfigProtoVlanEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanEntry.setStatus("current")


class _LldpXdot1ConfigProtoVlanTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigProtoVlanTxEnable based on TruthValue"""


_LldpXdot1ConfigProtoVlanTxEnable_Object = MibTableColumn
lldpXdot1ConfigProtoVlanTxEnable = _LldpXdot1ConfigProtoVlanTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 3, 1, 1),
    _LldpXdot1ConfigProtoVlanTxEnable_Type()
)
lldpXdot1ConfigProtoVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanTxEnable.setStatus("current")
_LldpXdot1ConfigProtocolTable_Object = MibTable
lldpXdot1ConfigProtocolTable = _LldpXdot1ConfigProtocolTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolTable.setStatus("current")
_LldpXdot1ConfigProtocolEntry_Object = MibTableRow
lldpXdot1ConfigProtocolEntry = _LldpXdot1ConfigProtocolEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolEntry.setStatus("current")


class _LldpXdot1ConfigProtocolTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigProtocolTxEnable based on TruthValue"""


_LldpXdot1ConfigProtocolTxEnable_Object = MibTableColumn
lldpXdot1ConfigProtocolTxEnable = _LldpXdot1ConfigProtocolTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 4, 1, 1),
    _LldpXdot1ConfigProtocolTxEnable_Type()
)
lldpXdot1ConfigProtocolTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolTxEnable.setStatus("current")
_LldpXdot1LocalData_ObjectIdentity = ObjectIdentity
lldpXdot1LocalData = _LldpXdot1LocalData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2)
)
_LldpXdot1LocTable_Object = MibTable
lldpXdot1LocTable = _LldpXdot1LocTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1LocTable.setStatus("current")
_LldpXdot1LocEntry_Object = MibTableRow
lldpXdot1LocEntry = _LldpXdot1LocEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 1, 1)
)
lldpXdot1LocEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocEntry.setStatus("current")


class _LldpXdot1LocPortVlanId_Type(Integer32):
    """Custom type lldpXdot1LocPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1LocPortVlanId_Type.__name__ = "Integer32"
_LldpXdot1LocPortVlanId_Object = MibTableColumn
lldpXdot1LocPortVlanId = _LldpXdot1LocPortVlanId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 1, 1, 1),
    _LldpXdot1LocPortVlanId_Type()
)
lldpXdot1LocPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocPortVlanId.setStatus("current")
_LldpXdot1LocProtoVlanTable_Object = MibTable
lldpXdot1LocProtoVlanTable = _LldpXdot1LocProtoVlanTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanTable.setStatus("current")
_LldpXdot1LocProtoVlanEntry_Object = MibTableRow
lldpXdot1LocProtoVlanEntry = _LldpXdot1LocProtoVlanEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 2, 1)
)
lldpXdot1LocProtoVlanEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
    (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1LocProtoVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanEntry.setStatus("current")


class _LldpXdot1LocProtoVlanId_Type(Integer32):
    """Custom type lldpXdot1LocProtoVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1LocProtoVlanId_Type.__name__ = "Integer32"
_LldpXdot1LocProtoVlanId_Object = MibTableColumn
lldpXdot1LocProtoVlanId = _LldpXdot1LocProtoVlanId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 2, 1, 1),
    _LldpXdot1LocProtoVlanId_Type()
)
lldpXdot1LocProtoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanId.setStatus("current")
_LldpXdot1LocProtoVlanSupported_Type = TruthValue
_LldpXdot1LocProtoVlanSupported_Object = MibTableColumn
lldpXdot1LocProtoVlanSupported = _LldpXdot1LocProtoVlanSupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 2, 1, 2),
    _LldpXdot1LocProtoVlanSupported_Type()
)
lldpXdot1LocProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanSupported.setStatus("current")
_LldpXdot1LocProtoVlanEnabled_Type = TruthValue
_LldpXdot1LocProtoVlanEnabled_Object = MibTableColumn
lldpXdot1LocProtoVlanEnabled = _LldpXdot1LocProtoVlanEnabled_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 2, 1, 3),
    _LldpXdot1LocProtoVlanEnabled_Type()
)
lldpXdot1LocProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanEnabled.setStatus("current")
_LldpXdot1LocVlanNameTable_Object = MibTable
lldpXdot1LocVlanNameTable = _LldpXdot1LocVlanNameTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNameTable.setStatus("current")
_LldpXdot1LocVlanNameEntry_Object = MibTableRow
lldpXdot1LocVlanNameEntry = _LldpXdot1LocVlanNameEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 3, 1)
)
lldpXdot1LocVlanNameEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
    (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1LocVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNameEntry.setStatus("current")
_LldpXdot1LocVlanId_Type = VlanId
_LldpXdot1LocVlanId_Object = MibTableColumn
lldpXdot1LocVlanId = _LldpXdot1LocVlanId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 3, 1, 1),
    _LldpXdot1LocVlanId_Type()
)
lldpXdot1LocVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1LocVlanId.setStatus("current")


class _LldpXdot1LocVlanName_Type(SnmpAdminString):
    """Custom type lldpXdot1LocVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LldpXdot1LocVlanName_Type.__name__ = "SnmpAdminString"
_LldpXdot1LocVlanName_Object = MibTableColumn
lldpXdot1LocVlanName = _LldpXdot1LocVlanName_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 3, 1, 2),
    _LldpXdot1LocVlanName_Type()
)
lldpXdot1LocVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocVlanName.setStatus("current")
_LldpXdot1LocProtocolTable_Object = MibTable
lldpXdot1LocProtocolTable = _LldpXdot1LocProtocolTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolTable.setStatus("current")
_LldpXdot1LocProtocolEntry_Object = MibTableRow
lldpXdot1LocProtocolEntry = _LldpXdot1LocProtocolEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 4, 1)
)
lldpXdot1LocProtocolEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
    (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1LocProtocolIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolEntry.setStatus("current")


class _LldpXdot1LocProtocolIndex_Type(Integer32):
    """Custom type lldpXdot1LocProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1LocProtocolIndex_Type.__name__ = "Integer32"
_LldpXdot1LocProtocolIndex_Object = MibTableColumn
lldpXdot1LocProtocolIndex = _LldpXdot1LocProtocolIndex_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 4, 1, 1),
    _LldpXdot1LocProtocolIndex_Type()
)
lldpXdot1LocProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolIndex.setStatus("current")


class _LldpXdot1LocProtocolId_Type(OctetString):
    """Custom type lldpXdot1LocProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_LldpXdot1LocProtocolId_Type.__name__ = "OctetString"
_LldpXdot1LocProtocolId_Object = MibTableColumn
lldpXdot1LocProtocolId = _LldpXdot1LocProtocolId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 4, 1, 2),
    _LldpXdot1LocProtocolId_Type()
)
lldpXdot1LocProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolId.setStatus("current")
_LldpXdot1RemoteData_ObjectIdentity = ObjectIdentity
lldpXdot1RemoteData = _LldpXdot1RemoteData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3)
)
_LldpXdot1RemTable_Object = MibTable
lldpXdot1RemTable = _LldpXdot1RemTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1RemTable.setStatus("current")
_LldpXdot1RemEntry_Object = MibTableRow
lldpXdot1RemEntry = _LldpXdot1RemEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 1, 1)
)
lldpXdot1RemEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemEntry.setStatus("current")


class _LldpXdot1RemPortVlanId_Type(Integer32):
    """Custom type lldpXdot1RemPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1RemPortVlanId_Type.__name__ = "Integer32"
_LldpXdot1RemPortVlanId_Object = MibTableColumn
lldpXdot1RemPortVlanId = _LldpXdot1RemPortVlanId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 1, 1, 1),
    _LldpXdot1RemPortVlanId_Type()
)
lldpXdot1RemPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemPortVlanId.setStatus("current")
_LldpXdot1RemProtoVlanTable_Object = MibTable
lldpXdot1RemProtoVlanTable = _LldpXdot1RemProtoVlanTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanTable.setStatus("current")
_LldpXdot1RemProtoVlanEntry_Object = MibTableRow
lldpXdot1RemProtoVlanEntry = _LldpXdot1RemProtoVlanEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 2, 1)
)
lldpXdot1RemProtoVlanEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtoVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanEntry.setStatus("current")


class _LldpXdot1RemProtoVlanId_Type(Integer32):
    """Custom type lldpXdot1RemProtoVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1RemProtoVlanId_Type.__name__ = "Integer32"
_LldpXdot1RemProtoVlanId_Object = MibTableColumn
lldpXdot1RemProtoVlanId = _LldpXdot1RemProtoVlanId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 2, 1, 1),
    _LldpXdot1RemProtoVlanId_Type()
)
lldpXdot1RemProtoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanId.setStatus("current")
_LldpXdot1RemProtoVlanSupported_Type = TruthValue
_LldpXdot1RemProtoVlanSupported_Object = MibTableColumn
lldpXdot1RemProtoVlanSupported = _LldpXdot1RemProtoVlanSupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 2, 1, 2),
    _LldpXdot1RemProtoVlanSupported_Type()
)
lldpXdot1RemProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanSupported.setStatus("current")
_LldpXdot1RemProtoVlanEnabled_Type = TruthValue
_LldpXdot1RemProtoVlanEnabled_Object = MibTableColumn
lldpXdot1RemProtoVlanEnabled = _LldpXdot1RemProtoVlanEnabled_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 2, 1, 3),
    _LldpXdot1RemProtoVlanEnabled_Type()
)
lldpXdot1RemProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanEnabled.setStatus("current")
_LldpXdot1RemVlanNameTable_Object = MibTable
lldpXdot1RemVlanNameTable = _LldpXdot1RemVlanNameTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameTable.setStatus("current")
_LldpXdot1RemVlanNameEntry_Object = MibTableRow
lldpXdot1RemVlanNameEntry = _LldpXdot1RemVlanNameEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 3, 1)
)
lldpXdot1RemVlanNameEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1RemVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameEntry.setStatus("current")
_LldpXdot1RemVlanId_Type = VlanId
_LldpXdot1RemVlanId_Object = MibTableColumn
lldpXdot1RemVlanId = _LldpXdot1RemVlanId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 3, 1, 1),
    _LldpXdot1RemVlanId_Type()
)
lldpXdot1RemVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanId.setStatus("current")


class _LldpXdot1RemVlanName_Type(SnmpAdminString):
    """Custom type lldpXdot1RemVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LldpXdot1RemVlanName_Type.__name__ = "SnmpAdminString"
_LldpXdot1RemVlanName_Object = MibTableColumn
lldpXdot1RemVlanName = _LldpXdot1RemVlanName_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 3, 1, 2),
    _LldpXdot1RemVlanName_Type()
)
lldpXdot1RemVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanName.setStatus("current")
_LldpXdot1RemProtocolTable_Object = MibTable
lldpXdot1RemProtocolTable = _LldpXdot1RemProtocolTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolTable.setStatus("current")
_LldpXdot1RemProtocolEntry_Object = MibTableRow
lldpXdot1RemProtocolEntry = _LldpXdot1RemProtocolEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 4, 1)
)
lldpXdot1RemProtocolEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtocolIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolEntry.setStatus("current")


class _LldpXdot1RemProtocolIndex_Type(Integer32):
    """Custom type lldpXdot1RemProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemProtocolIndex_Type.__name__ = "Integer32"
_LldpXdot1RemProtocolIndex_Object = MibTableColumn
lldpXdot1RemProtocolIndex = _LldpXdot1RemProtocolIndex_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 4, 1, 1),
    _LldpXdot1RemProtocolIndex_Type()
)
lldpXdot1RemProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolIndex.setStatus("current")


class _LldpXdot1RemProtocolId_Type(OctetString):
    """Custom type lldpXdot1RemProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_LldpXdot1RemProtocolId_Type.__name__ = "OctetString"
_LldpXdot1RemProtocolId_Object = MibTableColumn
lldpXdot1RemProtocolId = _LldpXdot1RemProtocolId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 4, 1, 2),
    _LldpXdot1RemProtocolId_Type()
)
lldpXdot1RemProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolId.setStatus("current")
_LldpXdot1Conformance_ObjectIdentity = ObjectIdentity
lldpXdot1Conformance = _LldpXdot1Conformance_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2)
)
_LldpXdot1Compliances_ObjectIdentity = ObjectIdentity
lldpXdot1Compliances = _LldpXdot1Compliances_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 1)
)
_LldpXdot1Groups_ObjectIdentity = ObjectIdentity
lldpXdot1Groups = _LldpXdot1Groups_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 2)
)
lldpPortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-MIB",
     "lldpXdot1ConfigPortVlanEntry")
)
lldpXdot1ConfigPortVlanEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpXdot1LocVlanNameEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-MIB",
     "lldpXdot1ConfigVlanNameEntry")
)
lldpXdot1ConfigVlanNameEntry.setIndexNames(*lldpXdot1LocVlanNameEntry.getIndexNames())
lldpXdot1LocProtoVlanEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-MIB",
     "lldpXdot1ConfigProtoVlanEntry")
)
lldpXdot1ConfigProtoVlanEntry.setIndexNames(*lldpXdot1LocProtoVlanEntry.getIndexNames())
lldpXdot1LocProtocolEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-MIB",
     "lldpXdot1ConfigProtocolEntry")
)
lldpXdot1ConfigProtocolEntry.setIndexNames(*lldpXdot1LocProtocolEntry.getIndexNames())

# Managed Objects groups

lldpXdot1ConfigGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 2, 1)
)
lldpXdot1ConfigGroup.setObjects(
      *(("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigPortVlanTxEnable"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigVlanNameTxEnable"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigProtoVlanTxEnable"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigProtocolTxEnable"))
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigGroup.setStatus("current")

lldpXdot1LocSysGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 2, 2)
)
lldpXdot1LocSysGroup.setObjects(
      *(("LLDP-EXT-DOT1-MIB", "lldpXdot1LocPortVlanId"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1LocProtoVlanSupported"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1LocProtoVlanEnabled"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1LocVlanName"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1LocProtocolId"))
)
if mibBuilder.loadTexts:
    lldpXdot1LocSysGroup.setStatus("current")

lldpXdot1RemSysGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 2, 3)
)
lldpXdot1RemSysGroup.setObjects(
      *(("LLDP-EXT-DOT1-MIB", "lldpXdot1RemPortVlanId"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtoVlanSupported"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtoVlanEnabled"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemVlanName"),
        ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtocolId"))
)
if mibBuilder.loadTexts:
    lldpXdot1RemSysGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpXdot1Compliance = ModuleCompliance(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-DOT1-MIB",
    **{"lldpXdot1MIB": lldpXdot1MIB,
       "lldpXdot1Objects": lldpXdot1Objects,
       "lldpXdot1Config": lldpXdot1Config,
       "lldpXdot1ConfigPortVlanTable": lldpXdot1ConfigPortVlanTable,
       "lldpXdot1ConfigPortVlanEntry": lldpXdot1ConfigPortVlanEntry,
       "lldpXdot1ConfigPortVlanTxEnable": lldpXdot1ConfigPortVlanTxEnable,
       "lldpXdot1ConfigVlanNameTable": lldpXdot1ConfigVlanNameTable,
       "lldpXdot1ConfigVlanNameEntry": lldpXdot1ConfigVlanNameEntry,
       "lldpXdot1ConfigVlanNameTxEnable": lldpXdot1ConfigVlanNameTxEnable,
       "lldpXdot1ConfigProtoVlanTable": lldpXdot1ConfigProtoVlanTable,
       "lldpXdot1ConfigProtoVlanEntry": lldpXdot1ConfigProtoVlanEntry,
       "lldpXdot1ConfigProtoVlanTxEnable": lldpXdot1ConfigProtoVlanTxEnable,
       "lldpXdot1ConfigProtocolTable": lldpXdot1ConfigProtocolTable,
       "lldpXdot1ConfigProtocolEntry": lldpXdot1ConfigProtocolEntry,
       "lldpXdot1ConfigProtocolTxEnable": lldpXdot1ConfigProtocolTxEnable,
       "lldpXdot1LocalData": lldpXdot1LocalData,
       "lldpXdot1LocTable": lldpXdot1LocTable,
       "lldpXdot1LocEntry": lldpXdot1LocEntry,
       "lldpXdot1LocPortVlanId": lldpXdot1LocPortVlanId,
       "lldpXdot1LocProtoVlanTable": lldpXdot1LocProtoVlanTable,
       "lldpXdot1LocProtoVlanEntry": lldpXdot1LocProtoVlanEntry,
       "lldpXdot1LocProtoVlanId": lldpXdot1LocProtoVlanId,
       "lldpXdot1LocProtoVlanSupported": lldpXdot1LocProtoVlanSupported,
       "lldpXdot1LocProtoVlanEnabled": lldpXdot1LocProtoVlanEnabled,
       "lldpXdot1LocVlanNameTable": lldpXdot1LocVlanNameTable,
       "lldpXdot1LocVlanNameEntry": lldpXdot1LocVlanNameEntry,
       "lldpXdot1LocVlanId": lldpXdot1LocVlanId,
       "lldpXdot1LocVlanName": lldpXdot1LocVlanName,
       "lldpXdot1LocProtocolTable": lldpXdot1LocProtocolTable,
       "lldpXdot1LocProtocolEntry": lldpXdot1LocProtocolEntry,
       "lldpXdot1LocProtocolIndex": lldpXdot1LocProtocolIndex,
       "lldpXdot1LocProtocolId": lldpXdot1LocProtocolId,
       "lldpXdot1RemoteData": lldpXdot1RemoteData,
       "lldpXdot1RemTable": lldpXdot1RemTable,
       "lldpXdot1RemEntry": lldpXdot1RemEntry,
       "lldpXdot1RemPortVlanId": lldpXdot1RemPortVlanId,
       "lldpXdot1RemProtoVlanTable": lldpXdot1RemProtoVlanTable,
       "lldpXdot1RemProtoVlanEntry": lldpXdot1RemProtoVlanEntry,
       "lldpXdot1RemProtoVlanId": lldpXdot1RemProtoVlanId,
       "lldpXdot1RemProtoVlanSupported": lldpXdot1RemProtoVlanSupported,
       "lldpXdot1RemProtoVlanEnabled": lldpXdot1RemProtoVlanEnabled,
       "lldpXdot1RemVlanNameTable": lldpXdot1RemVlanNameTable,
       "lldpXdot1RemVlanNameEntry": lldpXdot1RemVlanNameEntry,
       "lldpXdot1RemVlanId": lldpXdot1RemVlanId,
       "lldpXdot1RemVlanName": lldpXdot1RemVlanName,
       "lldpXdot1RemProtocolTable": lldpXdot1RemProtocolTable,
       "lldpXdot1RemProtocolEntry": lldpXdot1RemProtocolEntry,
       "lldpXdot1RemProtocolIndex": lldpXdot1RemProtocolIndex,
       "lldpXdot1RemProtocolId": lldpXdot1RemProtocolId,
       "lldpXdot1Conformance": lldpXdot1Conformance,
       "lldpXdot1Compliances": lldpXdot1Compliances,
       "lldpXdot1Compliance": lldpXdot1Compliance,
       "lldpXdot1Groups": lldpXdot1Groups,
       "lldpXdot1ConfigGroup": lldpXdot1ConfigGroup,
       "lldpXdot1LocSysGroup": lldpXdot1LocSysGroup,
       "lldpXdot1RemSysGroup": lldpXdot1RemSysGroup}
)
