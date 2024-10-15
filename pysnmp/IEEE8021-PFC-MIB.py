# SNMP MIB module (IEEE8021-PFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-PFC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:34 2024
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

(ieee802dot1mibs,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "ieee802dot1mibs")

(ifEntry,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifGeneralInformationGroup")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(systemGroup,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "systemGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ieee8021PFCMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 21)
)
ieee8021PFCMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2010-02-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021PfcMIBObjects_ObjectIdentity = ObjectIdentity
ieee8021PfcMIBObjects = _Ieee8021PfcMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 21, 1)
)
_Ieee8021PfcIfTable_Object = MibTable
ieee8021PfcIfTable = _Ieee8021PfcIfTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 21, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021PfcIfTable.setStatus("current")
_Ieee8021PfcIfEntry_Object = MibTableRow
ieee8021PfcIfEntry = _Ieee8021PfcIfEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021PfcIfEntry.setStatus("current")
_Ieee8021PfcLinkDelayAllowance_Type = Unsigned32
_Ieee8021PfcLinkDelayAllowance_Object = MibTableColumn
ieee8021PfcLinkDelayAllowance = _Ieee8021PfcLinkDelayAllowance_Object(
    (1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 1),
    _Ieee8021PfcLinkDelayAllowance_Type()
)
ieee8021PfcLinkDelayAllowance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PfcLinkDelayAllowance.setStatus("current")
_Ieee8021PfcRequests_Type = Counter32
_Ieee8021PfcRequests_Object = MibTableColumn
ieee8021PfcRequests = _Ieee8021PfcRequests_Object(
    (1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 2),
    _Ieee8021PfcRequests_Type()
)
ieee8021PfcRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PfcRequests.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021PfcRequests.setUnits("Requests")
_Ieee8021PfcIndications_Type = Counter32
_Ieee8021PfcIndications_Object = MibTableColumn
ieee8021PfcIndications = _Ieee8021PfcIndications_Object(
    (1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 3),
    _Ieee8021PfcIndications_Type()
)
ieee8021PfcIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PfcIndications.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021PfcIndications.setUnits("Indications")
_Ieee8021PfcConformance_ObjectIdentity = ObjectIdentity
ieee8021PfcConformance = _Ieee8021PfcConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 21, 2)
)
_Ieee8021PfcCompliances_ObjectIdentity = ObjectIdentity
ieee8021PfcCompliances = _Ieee8021PfcCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 21, 2, 1)
)
_Ieee8021PfcGroups_ObjectIdentity = ObjectIdentity
ieee8021PfcGroups = _Ieee8021PfcGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 21, 2, 2)
)
ifEntry.registerAugmentions(
    ("IEEE8021-PFC-MIB",
     "ieee8021PfcIfEntry")
)
ieee8021PfcIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

ieee8021PfcGlobalReqdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 21, 2, 2, 1)
)
ieee8021PfcGlobalReqdGroup.setObjects(
      *(("IEEE8021-PFC-MIB", "ieee8021PfcLinkDelayAllowance"),
        ("IEEE8021-PFC-MIB", "ieee8021PfcRequests"),
        ("IEEE8021-PFC-MIB", "ieee8021PfcIndications"))
)
if mibBuilder.loadTexts:
    ieee8021PfcGlobalReqdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021PfcCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 21, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021PfcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-PFC-MIB",
    **{"ieee8021PFCMib": ieee8021PFCMib,
       "ieee8021PfcMIBObjects": ieee8021PfcMIBObjects,
       "ieee8021PfcIfTable": ieee8021PfcIfTable,
       "ieee8021PfcIfEntry": ieee8021PfcIfEntry,
       "ieee8021PfcLinkDelayAllowance": ieee8021PfcLinkDelayAllowance,
       "ieee8021PfcRequests": ieee8021PfcRequests,
       "ieee8021PfcIndications": ieee8021PfcIndications,
       "ieee8021PfcConformance": ieee8021PfcConformance,
       "ieee8021PfcCompliances": ieee8021PfcCompliances,
       "ieee8021PfcCompliance": ieee8021PfcCompliance,
       "ieee8021PfcGroups": ieee8021PfcGroups,
       "ieee8021PfcGlobalReqdGroup": ieee8021PfcGlobalReqdGroup}
)
