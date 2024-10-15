# SNMP MIB module (XEDIA-L2DIAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-L2DIAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:57 2024
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

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaL2DialMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_L2DialObjects_ObjectIdentity = ObjectIdentity
l2DialObjects = _L2DialObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 30, 1)
)
_L2DialStatusTable_Object = MibTable
l2DialStatusTable = _L2DialStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1)
)
if mibBuilder.loadTexts:
    l2DialStatusTable.setStatus("current")
_L2DialStatusEntry_Object = MibTableRow
l2DialStatusEntry = _L2DialStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1, 1)
)
l2DialStatusEntry.setIndexNames(
    (0, "XEDIA-L2DIAL-MIB", "l2DialStatusIpAddress"),
)
if mibBuilder.loadTexts:
    l2DialStatusEntry.setStatus("current")
_L2DialStatusIpAddress_Type = IpAddress
_L2DialStatusIpAddress_Object = MibTableColumn
l2DialStatusIpAddress = _L2DialStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1, 1, 1),
    _L2DialStatusIpAddress_Type()
)
l2DialStatusIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2DialStatusIpAddress.setStatus("current")
_L2DialStatusSublayer_Type = Integer32
_L2DialStatusSublayer_Object = MibTableColumn
l2DialStatusSublayer = _L2DialStatusSublayer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1, 1, 2),
    _L2DialStatusSublayer_Type()
)
l2DialStatusSublayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2DialStatusSublayer.setStatus("current")
_L2DialConformance_ObjectIdentity = ObjectIdentity
l2DialConformance = _L2DialConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 30, 2)
)
_L2DialCompliances_ObjectIdentity = ObjectIdentity
l2DialCompliances = _L2DialCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 1)
)
_L2DialGroups_ObjectIdentity = ObjectIdentity
l2DialGroups = _L2DialGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 2)
)

# Managed Objects groups

l2DialStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 2, 1)
)
l2DialStatusGroup.setObjects(
    ("XEDIA-L2DIAL-MIB", "l2DialStatusSublayer")
)
if mibBuilder.loadTexts:
    l2DialStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

l2DialCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 1, 1)
)
if mibBuilder.loadTexts:
    l2DialCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-L2DIAL-MIB",
    **{"xediaL2DialMIB": xediaL2DialMIB,
       "l2DialObjects": l2DialObjects,
       "l2DialStatusTable": l2DialStatusTable,
       "l2DialStatusEntry": l2DialStatusEntry,
       "l2DialStatusIpAddress": l2DialStatusIpAddress,
       "l2DialStatusSublayer": l2DialStatusSublayer,
       "l2DialConformance": l2DialConformance,
       "l2DialCompliances": l2DialCompliances,
       "l2DialCompliance": l2DialCompliance,
       "l2DialGroups": l2DialGroups,
       "l2DialStatusGroup": l2DialStatusGroup}
)
