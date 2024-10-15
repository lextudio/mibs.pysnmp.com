# SNMP MIB module (BAY-STACK-LLDP-EXT-MED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-LLDP-EXT-MED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:08 2024
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(PolicyAppType,) = mibBuilder.importSymbols(
    "LLDP-EXT-MED-MIB",
    "PolicyAppType")

(lldpLocPortNum,) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpLocPortNum")

(VlanIdOrAnyOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrAnyOrNone")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackLldpExtMedMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 33)
)
bayStackLldpExtMedMib.setRevisions(
        ("2009-03-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsLldpExtMedNotifications_ObjectIdentity = ObjectIdentity
bsLldpExtMedNotifications = _BsLldpExtMedNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 0)
)
_BsLldpExtMedObjects_ObjectIdentity = ObjectIdentity
bsLldpExtMedObjects = _BsLldpExtMedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 1)
)
_BsLldpXMedLocMediaPolicyTable_Object = MibTable
bsLldpXMedLocMediaPolicyTable = _BsLldpXMedLocMediaPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 1, 1)
)
if mibBuilder.loadTexts:
    bsLldpXMedLocMediaPolicyTable.setStatus("current")
_BsLldpXMedLocMediaPolicyEntry_Object = MibTableRow
bsLldpXMedLocMediaPolicyEntry = _BsLldpXMedLocMediaPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 1, 1, 1)
)
bsLldpXMedLocMediaPolicyEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
    (0, "BAY-STACK-LLDP-EXT-MED-MIB", "bsLldpXMedLocMediaPolicyAppType"),
)
if mibBuilder.loadTexts:
    bsLldpXMedLocMediaPolicyEntry.setStatus("current")
_BsLldpXMedLocMediaPolicyAppType_Type = PolicyAppType
_BsLldpXMedLocMediaPolicyAppType_Object = MibTableColumn
bsLldpXMedLocMediaPolicyAppType = _BsLldpXMedLocMediaPolicyAppType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 1, 1, 1, 1),
    _BsLldpXMedLocMediaPolicyAppType_Type()
)
bsLldpXMedLocMediaPolicyAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsLldpXMedLocMediaPolicyAppType.setStatus("current")
_BsLldpXMedLocMediaPolicyVlanID_Type = VlanIdOrAnyOrNone
_BsLldpXMedLocMediaPolicyVlanID_Object = MibTableColumn
bsLldpXMedLocMediaPolicyVlanID = _BsLldpXMedLocMediaPolicyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 1, 1, 1, 2),
    _BsLldpXMedLocMediaPolicyVlanID_Type()
)
bsLldpXMedLocMediaPolicyVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsLldpXMedLocMediaPolicyVlanID.setStatus("current")


class _BsLldpXMedLocMediaPolicyPriority_Type(Integer32):
    """Custom type bsLldpXMedLocMediaPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BsLldpXMedLocMediaPolicyPriority_Type.__name__ = "Integer32"
_BsLldpXMedLocMediaPolicyPriority_Object = MibTableColumn
bsLldpXMedLocMediaPolicyPriority = _BsLldpXMedLocMediaPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 1, 1, 1, 3),
    _BsLldpXMedLocMediaPolicyPriority_Type()
)
bsLldpXMedLocMediaPolicyPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsLldpXMedLocMediaPolicyPriority.setStatus("current")
_BsLldpXMedLocMediaPolicyDscp_Type = Dscp
_BsLldpXMedLocMediaPolicyDscp_Object = MibTableColumn
bsLldpXMedLocMediaPolicyDscp = _BsLldpXMedLocMediaPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 1, 1, 1, 4),
    _BsLldpXMedLocMediaPolicyDscp_Type()
)
bsLldpXMedLocMediaPolicyDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsLldpXMedLocMediaPolicyDscp.setStatus("current")
_BsLldpXMedLocMediaPolicyUnknown_Type = TruthValue
_BsLldpXMedLocMediaPolicyUnknown_Object = MibTableColumn
bsLldpXMedLocMediaPolicyUnknown = _BsLldpXMedLocMediaPolicyUnknown_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 1, 1, 1, 5),
    _BsLldpXMedLocMediaPolicyUnknown_Type()
)
bsLldpXMedLocMediaPolicyUnknown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsLldpXMedLocMediaPolicyUnknown.setStatus("current")
_BsLldpXMedLocMediaPolicyTagged_Type = TruthValue
_BsLldpXMedLocMediaPolicyTagged_Object = MibTableColumn
bsLldpXMedLocMediaPolicyTagged = _BsLldpXMedLocMediaPolicyTagged_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 1, 1, 1, 6),
    _BsLldpXMedLocMediaPolicyTagged_Type()
)
bsLldpXMedLocMediaPolicyTagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsLldpXMedLocMediaPolicyTagged.setStatus("current")
_BsLldpXMedLocMediaPolicyRowStatus_Type = RowStatus
_BsLldpXMedLocMediaPolicyRowStatus_Object = MibTableColumn
bsLldpXMedLocMediaPolicyRowStatus = _BsLldpXMedLocMediaPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 33, 1, 1, 1, 7),
    _BsLldpXMedLocMediaPolicyRowStatus_Type()
)
bsLldpXMedLocMediaPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsLldpXMedLocMediaPolicyRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-LLDP-EXT-MED-MIB",
    **{"bayStackLldpExtMedMib": bayStackLldpExtMedMib,
       "bsLldpExtMedNotifications": bsLldpExtMedNotifications,
       "bsLldpExtMedObjects": bsLldpExtMedObjects,
       "bsLldpXMedLocMediaPolicyTable": bsLldpXMedLocMediaPolicyTable,
       "bsLldpXMedLocMediaPolicyEntry": bsLldpXMedLocMediaPolicyEntry,
       "bsLldpXMedLocMediaPolicyAppType": bsLldpXMedLocMediaPolicyAppType,
       "bsLldpXMedLocMediaPolicyVlanID": bsLldpXMedLocMediaPolicyVlanID,
       "bsLldpXMedLocMediaPolicyPriority": bsLldpXMedLocMediaPolicyPriority,
       "bsLldpXMedLocMediaPolicyDscp": bsLldpXMedLocMediaPolicyDscp,
       "bsLldpXMedLocMediaPolicyUnknown": bsLldpXMedLocMediaPolicyUnknown,
       "bsLldpXMedLocMediaPolicyTagged": bsLldpXMedLocMediaPolicyTagged,
       "bsLldpXMedLocMediaPolicyRowStatus": bsLldpXMedLocMediaPolicyRowStatus}
)
