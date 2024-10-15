# SNMP MIB module (ELTEX-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-CFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:06 2024
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(Dot1agCfmMpDirection,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMpDirection")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 MacAddress,
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eltexCfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 36)
)
eltexCfmMIB.setRevisions(
        ("2013-03-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltexCfmNotifications_ObjectIdentity = ObjectIdentity
eltexCfmNotifications = _EltexCfmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 36, 0)
)
_EltexCfmMIBObjects_ObjectIdentity = ObjectIdentity
eltexCfmMIBObjects = _EltexCfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1)
)
_EltexCfmMd_ObjectIdentity = ObjectIdentity
eltexCfmMd = _EltexCfmMd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 1)
)
_EltexCfmMdTable_Object = MibTable
eltexCfmMdTable = _EltexCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltexCfmMdTable.setStatus("current")
_EltexCfmMdEntry_Object = MibTableRow
eltexCfmMdEntry = _EltexCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 1, 1, 1)
)
eltexCfmMdEntry.setIndexNames(
    (0, "ELTEX-CFM-MIB", "eltexCfmMdName"),
)
if mibBuilder.loadTexts:
    eltexCfmMdEntry.setStatus("current")


class _EltexCfmMdName_Type(OctetString):
    """Custom type eltexCfmMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EltexCfmMdName_Type.__name__ = "OctetString"
_EltexCfmMdName_Object = MibTableColumn
eltexCfmMdName = _EltexCfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 1, 1, 1, 1),
    _EltexCfmMdName_Type()
)
eltexCfmMdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexCfmMdName.setStatus("current")


class _EltexCfmMdIndex_Type(Unsigned32):
    """Custom type eltexCfmMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EltexCfmMdIndex_Type.__name__ = "Unsigned32"
_EltexCfmMdIndex_Object = MibTableColumn
eltexCfmMdIndex = _EltexCfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 1, 1, 1, 2),
    _EltexCfmMdIndex_Type()
)
eltexCfmMdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexCfmMdIndex.setStatus("current")
_EltexCfmMdRowStatus_Type = RowStatus
_EltexCfmMdRowStatus_Object = MibTableColumn
eltexCfmMdRowStatus = _EltexCfmMdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 1, 1, 1, 3),
    _EltexCfmMdRowStatus_Type()
)
eltexCfmMdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexCfmMdRowStatus.setStatus("current")
_EltexCfmMa_ObjectIdentity = ObjectIdentity
eltexCfmMa = _EltexCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 2)
)
_EltexCfmMaTable_Object = MibTable
eltexCfmMaTable = _EltexCfmMaTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltexCfmMaTable.setStatus("current")
_EltexCfmMaEntry_Object = MibTableRow
eltexCfmMaEntry = _EltexCfmMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 2, 1, 1)
)
eltexCfmMaEntry.setIndexNames(
    (0, "ELTEX-CFM-MIB", "eltexCfmMdIndex"),
    (0, "ELTEX-CFM-MIB", "eltexCfmMaIndex"),
)
if mibBuilder.loadTexts:
    eltexCfmMaEntry.setStatus("current")


class _EltexCfmMaIndex_Type(Unsigned32):
    """Custom type eltexCfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EltexCfmMaIndex_Type.__name__ = "Unsigned32"
_EltexCfmMaIndex_Object = MibTableColumn
eltexCfmMaIndex = _EltexCfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 2, 1, 1, 1),
    _EltexCfmMaIndex_Type()
)
eltexCfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexCfmMaIndex.setStatus("current")
_EltexCfmMaDirection_Type = Dot1agCfmMpDirection
_EltexCfmMaDirection_Object = MibTableColumn
eltexCfmMaDirection = _EltexCfmMaDirection_Object(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 2, 1, 1, 2),
    _EltexCfmMaDirection_Type()
)
eltexCfmMaDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexCfmMaDirection.setStatus("current")
_EltexCfmMaRowStatus_Type = RowStatus
_EltexCfmMaRowStatus_Object = MibTableColumn
eltexCfmMaRowStatus = _EltexCfmMaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 36, 1, 2, 1, 1, 3),
    _EltexCfmMaRowStatus_Type()
)
eltexCfmMaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexCfmMaRowStatus.setStatus("current")
_EltexCfmConformance_ObjectIdentity = ObjectIdentity
eltexCfmConformance = _EltexCfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 36, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-CFM-MIB",
    **{"eltexCfmMIB": eltexCfmMIB,
       "eltexCfmNotifications": eltexCfmNotifications,
       "eltexCfmMIBObjects": eltexCfmMIBObjects,
       "eltexCfmMd": eltexCfmMd,
       "eltexCfmMdTable": eltexCfmMdTable,
       "eltexCfmMdEntry": eltexCfmMdEntry,
       "eltexCfmMdName": eltexCfmMdName,
       "eltexCfmMdIndex": eltexCfmMdIndex,
       "eltexCfmMdRowStatus": eltexCfmMdRowStatus,
       "eltexCfmMa": eltexCfmMa,
       "eltexCfmMaTable": eltexCfmMaTable,
       "eltexCfmMaEntry": eltexCfmMaEntry,
       "eltexCfmMaIndex": eltexCfmMaIndex,
       "eltexCfmMaDirection": eltexCfmMaDirection,
       "eltexCfmMaRowStatus": eltexCfmMaRowStatus,
       "eltexCfmConformance": eltexCfmConformance}
)
