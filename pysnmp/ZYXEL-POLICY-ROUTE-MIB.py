# SNMP MIB module (ZYXEL-POLICY-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-POLICY-ROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:30 2024
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

zyxelPolicyRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPolicyRouteSetup_ObjectIdentity = ObjectIdentity
zyxelPolicyRouteSetup = _ZyxelPolicyRouteSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1)
)
_ZyPolicyRouteMaxNumberOfProfiles_Type = Integer32
_ZyPolicyRouteMaxNumberOfProfiles_Object = MibScalar
zyPolicyRouteMaxNumberOfProfiles = _ZyPolicyRouteMaxNumberOfProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 1),
    _ZyPolicyRouteMaxNumberOfProfiles_Type()
)
zyPolicyRouteMaxNumberOfProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyRouteMaxNumberOfProfiles.setStatus("current")
_ZyxelPolicyRouteProfileTable_Object = MibTable
zyxelPolicyRouteProfileTable = _ZyxelPolicyRouteProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelPolicyRouteProfileTable.setStatus("current")
_ZyxelPolicyRouteProfileEntry_Object = MibTableRow
zyxelPolicyRouteProfileEntry = _ZyxelPolicyRouteProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 2, 1)
)
zyxelPolicyRouteProfileEntry.setIndexNames(
    (0, "ZYXEL-POLICY-ROUTE-MIB", "zyPolicyRouteProfileName"),
)
if mibBuilder.loadTexts:
    zyxelPolicyRouteProfileEntry.setStatus("current")
_ZyPolicyRouteProfileState_Type = EnabledStatus
_ZyPolicyRouteProfileState_Object = MibTableColumn
zyPolicyRouteProfileState = _ZyPolicyRouteProfileState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 2, 1, 1),
    _ZyPolicyRouteProfileState_Type()
)
zyPolicyRouteProfileState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPolicyRouteProfileState.setStatus("current")
_ZyPolicyRouteProfileName_Type = DisplayString
_ZyPolicyRouteProfileName_Object = MibTableColumn
zyPolicyRouteProfileName = _ZyPolicyRouteProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 2, 1, 2),
    _ZyPolicyRouteProfileName_Type()
)
zyPolicyRouteProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPolicyRouteProfileName.setStatus("current")
_ZyPolicyRouteProfileRowStatus_Type = RowStatus
_ZyPolicyRouteProfileRowStatus_Object = MibTableColumn
zyPolicyRouteProfileRowStatus = _ZyPolicyRouteProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 2, 1, 3),
    _ZyPolicyRouteProfileRowStatus_Type()
)
zyPolicyRouteProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyPolicyRouteProfileRowStatus.setStatus("current")
_ZyPolicyRouteMaxNumberOfRules_Type = Integer32
_ZyPolicyRouteMaxNumberOfRules_Object = MibScalar
zyPolicyRouteMaxNumberOfRules = _ZyPolicyRouteMaxNumberOfRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 3),
    _ZyPolicyRouteMaxNumberOfRules_Type()
)
zyPolicyRouteMaxNumberOfRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyRouteMaxNumberOfRules.setStatus("current")
_ZyxelPolicyRouteTable_Object = MibTable
zyxelPolicyRouteTable = _ZyxelPolicyRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelPolicyRouteTable.setStatus("current")
_ZyxelPolicyRouteEntry_Object = MibTableRow
zyxelPolicyRouteEntry = _ZyxelPolicyRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1)
)
zyxelPolicyRouteEntry.setIndexNames(
    (0, "ZYXEL-POLICY-ROUTE-MIB", "zyPolicyRouteProfile"),
    (0, "ZYXEL-POLICY-ROUTE-MIB", "zyPolicyRouteSequence"),
)
if mibBuilder.loadTexts:
    zyxelPolicyRouteEntry.setStatus("current")
_ZyPolicyRouteProfile_Type = DisplayString
_ZyPolicyRouteProfile_Object = MibTableColumn
zyPolicyRouteProfile = _ZyPolicyRouteProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 1),
    _ZyPolicyRouteProfile_Type()
)
zyPolicyRouteProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPolicyRouteProfile.setStatus("current")
_ZyPolicyRouteSequence_Type = Integer32
_ZyPolicyRouteSequence_Object = MibTableColumn
zyPolicyRouteSequence = _ZyPolicyRouteSequence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 2),
    _ZyPolicyRouteSequence_Type()
)
zyPolicyRouteSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPolicyRouteSequence.setStatus("current")


class _ZyPolicyRouteStatement_Type(Integer32):
    """Custom type zyPolicyRouteStatement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_ZyPolicyRouteStatement_Type.__name__ = "Integer32"
_ZyPolicyRouteStatement_Object = MibTableColumn
zyPolicyRouteStatement = _ZyPolicyRouteStatement_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 3),
    _ZyPolicyRouteStatement_Type()
)
zyPolicyRouteStatement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPolicyRouteStatement.setStatus("current")
_ZyPolicyRouteCalssifier_Type = DisplayString
_ZyPolicyRouteCalssifier_Object = MibTableColumn
zyPolicyRouteCalssifier = _ZyPolicyRouteCalssifier_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 4),
    _ZyPolicyRouteCalssifier_Type()
)
zyPolicyRouteCalssifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPolicyRouteCalssifier.setStatus("current")
_ZyPolicyRouteNextHop_Type = IpAddress
_ZyPolicyRouteNextHop_Object = MibTableColumn
zyPolicyRouteNextHop = _ZyPolicyRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 5),
    _ZyPolicyRouteNextHop_Type()
)
zyPolicyRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPolicyRouteNextHop.setStatus("current")
_ZyPolicyRouteRowStatus_Type = RowStatus
_ZyPolicyRouteRowStatus_Object = MibTableColumn
zyPolicyRouteRowStatus = _ZyPolicyRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 60, 1, 4, 1, 6),
    _ZyPolicyRouteRowStatus_Type()
)
zyPolicyRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyPolicyRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-POLICY-ROUTE-MIB",
    **{"zyxelPolicyRoute": zyxelPolicyRoute,
       "zyxelPolicyRouteSetup": zyxelPolicyRouteSetup,
       "zyPolicyRouteMaxNumberOfProfiles": zyPolicyRouteMaxNumberOfProfiles,
       "zyxelPolicyRouteProfileTable": zyxelPolicyRouteProfileTable,
       "zyxelPolicyRouteProfileEntry": zyxelPolicyRouteProfileEntry,
       "zyPolicyRouteProfileState": zyPolicyRouteProfileState,
       "zyPolicyRouteProfileName": zyPolicyRouteProfileName,
       "zyPolicyRouteProfileRowStatus": zyPolicyRouteProfileRowStatus,
       "zyPolicyRouteMaxNumberOfRules": zyPolicyRouteMaxNumberOfRules,
       "zyxelPolicyRouteTable": zyxelPolicyRouteTable,
       "zyxelPolicyRouteEntry": zyxelPolicyRouteEntry,
       "zyPolicyRouteProfile": zyPolicyRouteProfile,
       "zyPolicyRouteSequence": zyPolicyRouteSequence,
       "zyPolicyRouteStatement": zyPolicyRouteStatement,
       "zyPolicyRouteCalssifier": zyPolicyRouteCalssifier,
       "zyPolicyRouteNextHop": zyPolicyRouteNextHop,
       "zyPolicyRouteRowStatus": zyPolicyRouteRowStatus}
)
