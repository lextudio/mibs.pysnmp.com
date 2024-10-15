# SNMP MIB module (TRAPEZE-NETWORKS-RF-BLACKLIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-RF-BLACKLIST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:36 2024
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzRFBlacklistMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18)
)
trpzRFBlacklistMib.setRevisions(
        ("2011-02-24 00:14",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzRFBlacklistedEntryType(Integer32, TextualConvention):
    status = "current"
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
        *(("assocReqFlood", 5),
          ("configuredDynamic", 4),
          ("configuredPermanent", 3),
          ("disassocReqFlood", 7),
          ("other", 1),
          ("reassocReqFlood", 6),
          ("unknownDynamic", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TrpzRFBlacklistMibObjects_ObjectIdentity = ObjectIdentity
trpzRFBlacklistMibObjects = _TrpzRFBlacklistMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 1)
)
_TrpzRFBlacklistXmtrTable_Object = MibTable
trpzRFBlacklistXmtrTable = _TrpzRFBlacklistXmtrTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2)
)
if mibBuilder.loadTexts:
    trpzRFBlacklistXmtrTable.setStatus("current")
_TrpzRFBlacklistXmtrEntry_Object = MibTableRow
trpzRFBlacklistXmtrEntry = _TrpzRFBlacklistXmtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1)
)
trpzRFBlacklistXmtrEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrMacAddress"),
)
if mibBuilder.loadTexts:
    trpzRFBlacklistXmtrEntry.setStatus("current")
_TrpzRFBlacklistXmtrMacAddress_Type = MacAddress
_TrpzRFBlacklistXmtrMacAddress_Object = MibTableColumn
trpzRFBlacklistXmtrMacAddress = _TrpzRFBlacklistXmtrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 1),
    _TrpzRFBlacklistXmtrMacAddress_Type()
)
trpzRFBlacklistXmtrMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzRFBlacklistXmtrMacAddress.setStatus("current")
_TrpzRFBlacklistXmtrType_Type = TrpzRFBlacklistedEntryType
_TrpzRFBlacklistXmtrType_Object = MibTableColumn
trpzRFBlacklistXmtrType = _TrpzRFBlacklistXmtrType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 2),
    _TrpzRFBlacklistXmtrType_Type()
)
trpzRFBlacklistXmtrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzRFBlacklistXmtrType.setStatus("current")
_TrpzRFBlacklistXmtrTimeToLive_Type = Unsigned32
_TrpzRFBlacklistXmtrTimeToLive_Object = MibTableColumn
trpzRFBlacklistXmtrTimeToLive = _TrpzRFBlacklistXmtrTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 3),
    _TrpzRFBlacklistXmtrTimeToLive_Type()
)
trpzRFBlacklistXmtrTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzRFBlacklistXmtrTimeToLive.setStatus("current")
_TrpzRFBlacklistConformance_ObjectIdentity = ObjectIdentity
trpzRFBlacklistConformance = _TrpzRFBlacklistConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 2)
)
_TrpzRFBlacklistCompliances_ObjectIdentity = ObjectIdentity
trpzRFBlacklistCompliances = _TrpzRFBlacklistCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 1)
)
_TrpzRFBlacklistGroups_ObjectIdentity = ObjectIdentity
trpzRFBlacklistGroups = _TrpzRFBlacklistGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 2)
)

# Managed Objects groups

trpzRFBlacklistXmtrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 2, 1)
)
trpzRFBlacklistXmtrGroup.setObjects(
      *(("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrType"),
        ("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrTimeToLive"))
)
if mibBuilder.loadTexts:
    trpzRFBlacklistXmtrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzRFBlacklistCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzRFBlacklistCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-RF-BLACKLIST-MIB",
    **{"TrpzRFBlacklistedEntryType": TrpzRFBlacklistedEntryType,
       "trpzRFBlacklistMib": trpzRFBlacklistMib,
       "trpzRFBlacklistMibObjects": trpzRFBlacklistMibObjects,
       "trpzRFBlacklistXmtrTable": trpzRFBlacklistXmtrTable,
       "trpzRFBlacklistXmtrEntry": trpzRFBlacklistXmtrEntry,
       "trpzRFBlacklistXmtrMacAddress": trpzRFBlacklistXmtrMacAddress,
       "trpzRFBlacklistXmtrType": trpzRFBlacklistXmtrType,
       "trpzRFBlacklistXmtrTimeToLive": trpzRFBlacklistXmtrTimeToLive,
       "trpzRFBlacklistConformance": trpzRFBlacklistConformance,
       "trpzRFBlacklistCompliances": trpzRFBlacklistCompliances,
       "trpzRFBlacklistCompliance": trpzRFBlacklistCompliance,
       "trpzRFBlacklistGroups": trpzRFBlacklistGroups,
       "trpzRFBlacklistXmtrGroup": trpzRFBlacklistXmtrGroup}
)
