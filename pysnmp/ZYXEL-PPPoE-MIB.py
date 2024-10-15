# SNMP MIB module (ZYXEL-PPPoE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-PPPoE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:38 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelPppoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPppoeIaSetup_ObjectIdentity = ObjectIdentity
zyxelPppoeIaSetup = _ZyxelPppoeIaSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1)
)
_ZyPppoeIaState_Type = EnabledStatus
_ZyPppoeIaState_Object = MibScalar
zyPppoeIaState = _ZyPppoeIaState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 1),
    _ZyPppoeIaState_Type()
)
zyPppoeIaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaState.setStatus("current")
_ZyPppoeIaAccessNodeIdString_Type = DisplayString
_ZyPppoeIaAccessNodeIdString_Object = MibScalar
zyPppoeIaAccessNodeIdString = _ZyPppoeIaAccessNodeIdString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 2),
    _ZyPppoeIaAccessNodeIdString_Type()
)
zyPppoeIaAccessNodeIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaAccessNodeIdString.setStatus("current")
_ZyPppoeIaFlexibleCircuitIdSyntaxState_Type = EnabledStatus
_ZyPppoeIaFlexibleCircuitIdSyntaxState_Object = MibScalar
zyPppoeIaFlexibleCircuitIdSyntaxState = _ZyPppoeIaFlexibleCircuitIdSyntaxState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 3),
    _ZyPppoeIaFlexibleCircuitIdSyntaxState_Type()
)
zyPppoeIaFlexibleCircuitIdSyntaxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaFlexibleCircuitIdSyntaxState.setStatus("current")
_ZyPppoeIaFlexibleCircuitIdSyntaxIdString_Type = DisplayString
_ZyPppoeIaFlexibleCircuitIdSyntaxIdString_Object = MibScalar
zyPppoeIaFlexibleCircuitIdSyntaxIdString = _ZyPppoeIaFlexibleCircuitIdSyntaxIdString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 4),
    _ZyPppoeIaFlexibleCircuitIdSyntaxIdString_Type()
)
zyPppoeIaFlexibleCircuitIdSyntaxIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaFlexibleCircuitIdSyntaxIdString.setStatus("current")


class _ZyPppoeIaFlexibleCircuitIdSyntaxOption_Type(Integer32):
    """Custom type zyPppoeIaFlexibleCircuitIdSyntaxOption based on Integer32"""
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
        *(("pv", 3),
          ("sp", 1),
          ("spv", 4),
          ("sv", 2))
    )


_ZyPppoeIaFlexibleCircuitIdSyntaxOption_Type.__name__ = "Integer32"
_ZyPppoeIaFlexibleCircuitIdSyntaxOption_Object = MibScalar
zyPppoeIaFlexibleCircuitIdSyntaxOption = _ZyPppoeIaFlexibleCircuitIdSyntaxOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 5),
    _ZyPppoeIaFlexibleCircuitIdSyntaxOption_Type()
)
zyPppoeIaFlexibleCircuitIdSyntaxOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaFlexibleCircuitIdSyntaxOption.setStatus("current")


class _ZyPppoeIaFlexibleCircuitIdSyntaxDelimiter_Type(Integer32):
    """Custom type zyPppoeIaFlexibleCircuitIdSyntaxDelimiter based on Integer32"""
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
        *(("comma", 3),
          ("dot", 2),
          ("poundSign", 1),
          ("semicolon", 4),
          ("slash", 5),
          ("space", 6))
    )


_ZyPppoeIaFlexibleCircuitIdSyntaxDelimiter_Type.__name__ = "Integer32"
_ZyPppoeIaFlexibleCircuitIdSyntaxDelimiter_Object = MibScalar
zyPppoeIaFlexibleCircuitIdSyntaxDelimiter = _ZyPppoeIaFlexibleCircuitIdSyntaxDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 6),
    _ZyPppoeIaFlexibleCircuitIdSyntaxDelimiter_Type()
)
zyPppoeIaFlexibleCircuitIdSyntaxDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaFlexibleCircuitIdSyntaxDelimiter.setStatus("current")
_ZyxelPppoeIaPortTable_Object = MibTable
zyxelPppoeIaPortTable = _ZyxelPppoeIaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 7)
)
if mibBuilder.loadTexts:
    zyxelPppoeIaPortTable.setStatus("current")
_ZyxelPppoeIaPortEntry_Object = MibTableRow
zyxelPppoeIaPortEntry = _ZyxelPppoeIaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 7, 1)
)
zyxelPppoeIaPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPppoeIaPortEntry.setStatus("current")
_ZyPppoeIaPortTrustState_Type = EnabledStatus
_ZyPppoeIaPortTrustState_Object = MibTableColumn
zyPppoeIaPortTrustState = _ZyPppoeIaPortTrustState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 7, 1, 1),
    _ZyPppoeIaPortTrustState_Type()
)
zyPppoeIaPortTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaPortTrustState.setStatus("current")
_ZyPppoeIaPortCircuitIdString_Type = DisplayString
_ZyPppoeIaPortCircuitIdString_Object = MibTableColumn
zyPppoeIaPortCircuitIdString = _ZyPppoeIaPortCircuitIdString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 7, 1, 2),
    _ZyPppoeIaPortCircuitIdString_Type()
)
zyPppoeIaPortCircuitIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaPortCircuitIdString.setStatus("current")
_ZyPppoeIaPortRemoteIdString_Type = DisplayString
_ZyPppoeIaPortRemoteIdString_Object = MibTableColumn
zyPppoeIaPortRemoteIdString = _ZyPppoeIaPortRemoteIdString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 7, 1, 3),
    _ZyPppoeIaPortRemoteIdString_Type()
)
zyPppoeIaPortRemoteIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaPortRemoteIdString.setStatus("current")
_ZyPppoeIaMaxNumberOfVlans_Type = Integer32
_ZyPppoeIaMaxNumberOfVlans_Object = MibScalar
zyPppoeIaMaxNumberOfVlans = _ZyPppoeIaMaxNumberOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 8),
    _ZyPppoeIaMaxNumberOfVlans_Type()
)
zyPppoeIaMaxNumberOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPppoeIaMaxNumberOfVlans.setStatus("current")
_ZyxelPppoeIaVlanTable_Object = MibTable
zyxelPppoeIaVlanTable = _ZyxelPppoeIaVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 9)
)
if mibBuilder.loadTexts:
    zyxelPppoeIaVlanTable.setStatus("current")
_ZyxelPppoeIaVlanEntry_Object = MibTableRow
zyxelPppoeIaVlanEntry = _ZyxelPppoeIaVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 9, 1)
)
zyxelPppoeIaVlanEntry.setIndexNames(
    (0, "ZYXEL-PPPoE-MIB", "zyPppoeIaVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelPppoeIaVlanEntry.setStatus("current")


class _ZyPppoeIaVlanVid_Type(Integer32):
    """Custom type zyPppoeIaVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyPppoeIaVlanVid_Type.__name__ = "Integer32"
_ZyPppoeIaVlanVid_Object = MibTableColumn
zyPppoeIaVlanVid = _ZyPppoeIaVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 9, 1, 1),
    _ZyPppoeIaVlanVid_Type()
)
zyPppoeIaVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPppoeIaVlanVid.setStatus("current")
_ZyPppoeIaVlanCircuitIdState_Type = EnabledStatus
_ZyPppoeIaVlanCircuitIdState_Object = MibTableColumn
zyPppoeIaVlanCircuitIdState = _ZyPppoeIaVlanCircuitIdState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 9, 1, 2),
    _ZyPppoeIaVlanCircuitIdState_Type()
)
zyPppoeIaVlanCircuitIdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaVlanCircuitIdState.setStatus("current")
_ZyPppoeIaVlanRemoteIdState_Type = EnabledStatus
_ZyPppoeIaVlanRemoteIdState_Object = MibTableColumn
zyPppoeIaVlanRemoteIdState = _ZyPppoeIaVlanRemoteIdState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 9, 1, 3),
    _ZyPppoeIaVlanRemoteIdState_Type()
)
zyPppoeIaVlanRemoteIdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaVlanRemoteIdState.setStatus("current")
_ZyPppoeIaVlanRowStatus_Type = RowStatus
_ZyPppoeIaVlanRowStatus_Object = MibTableColumn
zyPppoeIaVlanRowStatus = _ZyPppoeIaVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 9, 1, 4),
    _ZyPppoeIaVlanRowStatus_Type()
)
zyPppoeIaVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyPppoeIaVlanRowStatus.setStatus("current")
_ZyPppoeIaMaxNumberOfPortVlans_Type = Integer32
_ZyPppoeIaMaxNumberOfPortVlans_Object = MibScalar
zyPppoeIaMaxNumberOfPortVlans = _ZyPppoeIaMaxNumberOfPortVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 10),
    _ZyPppoeIaMaxNumberOfPortVlans_Type()
)
zyPppoeIaMaxNumberOfPortVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPppoeIaMaxNumberOfPortVlans.setStatus("current")
_ZyxelPppoeIaPortVlanTable_Object = MibTable
zyxelPppoeIaPortVlanTable = _ZyxelPppoeIaPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 11)
)
if mibBuilder.loadTexts:
    zyxelPppoeIaPortVlanTable.setStatus("current")
_ZyxelPppoeIaPortVlanEntry_Object = MibTableRow
zyxelPppoeIaPortVlanEntry = _ZyxelPppoeIaPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 11, 1)
)
zyxelPppoeIaPortVlanEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-PPPoE-MIB", "zyPppoeIaPortVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelPppoeIaPortVlanEntry.setStatus("current")
_ZyPppoeIaPortVlanVid_Type = Integer32
_ZyPppoeIaPortVlanVid_Object = MibTableColumn
zyPppoeIaPortVlanVid = _ZyPppoeIaPortVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 11, 1, 1),
    _ZyPppoeIaPortVlanVid_Type()
)
zyPppoeIaPortVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPppoeIaPortVlanVid.setStatus("current")
_ZyPppoeIaPortVlanCircuitIdString_Type = DisplayString
_ZyPppoeIaPortVlanCircuitIdString_Object = MibTableColumn
zyPppoeIaPortVlanCircuitIdString = _ZyPppoeIaPortVlanCircuitIdString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 11, 1, 2),
    _ZyPppoeIaPortVlanCircuitIdString_Type()
)
zyPppoeIaPortVlanCircuitIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaPortVlanCircuitIdString.setStatus("current")
_ZyPppoeIaPortVlanRemoteIdString_Type = DisplayString
_ZyPppoeIaPortVlanRemoteIdString_Object = MibTableColumn
zyPppoeIaPortVlanRemoteIdString = _ZyPppoeIaPortVlanRemoteIdString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 11, 1, 3),
    _ZyPppoeIaPortVlanRemoteIdString_Type()
)
zyPppoeIaPortVlanRemoteIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPppoeIaPortVlanRemoteIdString.setStatus("current")
_ZyPppoeIaPortVlanRowStatus_Type = RowStatus
_ZyPppoeIaPortVlanRowStatus_Object = MibTableColumn
zyPppoeIaPortVlanRowStatus = _ZyPppoeIaPortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 67, 1, 11, 1, 4),
    _ZyPppoeIaPortVlanRowStatus_Type()
)
zyPppoeIaPortVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyPppoeIaPortVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-PPPoE-MIB",
    **{"zyxelPppoe": zyxelPppoe,
       "zyxelPppoeIaSetup": zyxelPppoeIaSetup,
       "zyPppoeIaState": zyPppoeIaState,
       "zyPppoeIaAccessNodeIdString": zyPppoeIaAccessNodeIdString,
       "zyPppoeIaFlexibleCircuitIdSyntaxState": zyPppoeIaFlexibleCircuitIdSyntaxState,
       "zyPppoeIaFlexibleCircuitIdSyntaxIdString": zyPppoeIaFlexibleCircuitIdSyntaxIdString,
       "zyPppoeIaFlexibleCircuitIdSyntaxOption": zyPppoeIaFlexibleCircuitIdSyntaxOption,
       "zyPppoeIaFlexibleCircuitIdSyntaxDelimiter": zyPppoeIaFlexibleCircuitIdSyntaxDelimiter,
       "zyxelPppoeIaPortTable": zyxelPppoeIaPortTable,
       "zyxelPppoeIaPortEntry": zyxelPppoeIaPortEntry,
       "zyPppoeIaPortTrustState": zyPppoeIaPortTrustState,
       "zyPppoeIaPortCircuitIdString": zyPppoeIaPortCircuitIdString,
       "zyPppoeIaPortRemoteIdString": zyPppoeIaPortRemoteIdString,
       "zyPppoeIaMaxNumberOfVlans": zyPppoeIaMaxNumberOfVlans,
       "zyxelPppoeIaVlanTable": zyxelPppoeIaVlanTable,
       "zyxelPppoeIaVlanEntry": zyxelPppoeIaVlanEntry,
       "zyPppoeIaVlanVid": zyPppoeIaVlanVid,
       "zyPppoeIaVlanCircuitIdState": zyPppoeIaVlanCircuitIdState,
       "zyPppoeIaVlanRemoteIdState": zyPppoeIaVlanRemoteIdState,
       "zyPppoeIaVlanRowStatus": zyPppoeIaVlanRowStatus,
       "zyPppoeIaMaxNumberOfPortVlans": zyPppoeIaMaxNumberOfPortVlans,
       "zyxelPppoeIaPortVlanTable": zyxelPppoeIaPortVlanTable,
       "zyxelPppoeIaPortVlanEntry": zyxelPppoeIaPortVlanEntry,
       "zyPppoeIaPortVlanVid": zyPppoeIaPortVlanVid,
       "zyPppoeIaPortVlanCircuitIdString": zyPppoeIaPortVlanCircuitIdString,
       "zyPppoeIaPortVlanRemoteIdString": zyPppoeIaPortVlanRemoteIdString,
       "zyPppoeIaPortVlanRowStatus": zyPppoeIaPortVlanRowStatus}
)
