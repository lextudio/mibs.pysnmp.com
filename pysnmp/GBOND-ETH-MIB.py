# SNMP MIB module (GBOND-ETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBOND-ETH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:03 2024
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

(gBondMIB,) = mibBuilder.importSymbols(
    "GBOND-MIB",
    "gBondMIB")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

gBondEthMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 211, 2)
)
gBondEthMIB.setRevisions(
        ("2007-06-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class GBondEthPtmTcType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tc6465", 1),
          ("tcHDLC", 2))
    )



# MIB Managed Objects in the order of their OIDs

_GBondEthObjects_ObjectIdentity = ObjectIdentity
gBondEthObjects = _GBondEthObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 2, 1)
)
_GBondEthPort_ObjectIdentity = ObjectIdentity
gBondEthPort = _GBondEthPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1)
)
_GBondEthPortConfTable_Object = MibTable
gBondEthPortConfTable = _GBondEthPortConfTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    gBondEthPortConfTable.setStatus("current")
_GBondEthPortConfEntry_Object = MibTableRow
gBondEthPortConfEntry = _GBondEthPortConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 1, 1)
)
gBondEthPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondEthPortConfEntry.setStatus("current")
_GBondEthTcAdminType_Type = GBondEthPtmTcType
_GBondEthTcAdminType_Object = MibTableColumn
gBondEthTcAdminType = _GBondEthTcAdminType_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 1, 1, 1),
    _GBondEthTcAdminType_Type()
)
gBondEthTcAdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondEthTcAdminType.setStatus("current")
_GBondEthPortCapabilityTable_Object = MibTable
gBondEthPortCapabilityTable = _GBondEthPortCapabilityTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gBondEthPortCapabilityTable.setStatus("current")
_GBondEthPortCapabilityEntry_Object = MibTableRow
gBondEthPortCapabilityEntry = _GBondEthPortCapabilityEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 2, 1)
)
gBondEthPortCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondEthPortCapabilityEntry.setStatus("current")


class _GBondEthTcTypesSupported_Type(Bits):
    """Custom type gBondEthTcTypesSupported based on Bits"""
    namedValues = NamedValues(
        *(("tc6465", 0),
          ("tcHDLC", 1))
    )

_GBondEthTcTypesSupported_Type.__name__ = "Bits"
_GBondEthTcTypesSupported_Object = MibTableColumn
gBondEthTcTypesSupported = _GBondEthTcTypesSupported_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 2, 1, 1),
    _GBondEthTcTypesSupported_Type()
)
gBondEthTcTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthTcTypesSupported.setStatus("current")
_GBondEthPortStatusTable_Object = MibTable
gBondEthPortStatusTable = _GBondEthPortStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    gBondEthPortStatusTable.setStatus("current")
_GBondEthPortStatusEntry_Object = MibTableRow
gBondEthPortStatusEntry = _GBondEthPortStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1)
)
gBondEthPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondEthPortStatusEntry.setStatus("current")
_GBondEthTcOperType_Type = GBondEthPtmTcType
_GBondEthTcOperType_Object = MibTableColumn
gBondEthTcOperType = _GBondEthTcOperType_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 1),
    _GBondEthTcOperType_Type()
)
gBondEthTcOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthTcOperType.setStatus("current")
_GBondEthInErrors_Type = Counter32
_GBondEthInErrors_Object = MibTableColumn
gBondEthInErrors = _GBondEthInErrors_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 2),
    _GBondEthInErrors_Type()
)
gBondEthInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthInErrors.setStatus("current")
_GBondEthInSmallFragments_Type = Counter32
_GBondEthInSmallFragments_Object = MibTableColumn
gBondEthInSmallFragments = _GBondEthInSmallFragments_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 3),
    _GBondEthInSmallFragments_Type()
)
gBondEthInSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthInSmallFragments.setStatus("current")
_GBondEthInLargeFragments_Type = Counter32
_GBondEthInLargeFragments_Object = MibTableColumn
gBondEthInLargeFragments = _GBondEthInLargeFragments_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 4),
    _GBondEthInLargeFragments_Type()
)
gBondEthInLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthInLargeFragments.setStatus("current")
_GBondEthInBadFragments_Type = Counter32
_GBondEthInBadFragments_Object = MibTableColumn
gBondEthInBadFragments = _GBondEthInBadFragments_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 5),
    _GBondEthInBadFragments_Type()
)
gBondEthInBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthInBadFragments.setStatus("current")
_GBondEthInLostFragments_Type = Counter32
_GBondEthInLostFragments_Object = MibTableColumn
gBondEthInLostFragments = _GBondEthInLostFragments_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 6),
    _GBondEthInLostFragments_Type()
)
gBondEthInLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthInLostFragments.setStatus("current")
_GBondEthInLostStarts_Type = Counter32
_GBondEthInLostStarts_Object = MibTableColumn
gBondEthInLostStarts = _GBondEthInLostStarts_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 7),
    _GBondEthInLostStarts_Type()
)
gBondEthInLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthInLostStarts.setStatus("current")
_GBondEthInLostEnds_Type = Counter32
_GBondEthInLostEnds_Object = MibTableColumn
gBondEthInLostEnds = _GBondEthInLostEnds_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 8),
    _GBondEthInLostEnds_Type()
)
gBondEthInLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthInLostEnds.setStatus("current")
_GBondEthInOverflows_Type = Counter32
_GBondEthInOverflows_Object = MibTableColumn
gBondEthInOverflows = _GBondEthInOverflows_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 1, 3, 1, 9),
    _GBondEthInOverflows_Type()
)
gBondEthInOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthInOverflows.setStatus("current")
_GBondEthBce_ObjectIdentity = ObjectIdentity
gBondEthBce = _GBondEthBce_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 2)
)
_GBondEthBceStatusTable_Object = MibTable
gBondEthBceStatusTable = _GBondEthBceStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    gBondEthBceStatusTable.setStatus("current")
_GBondEthBceStatusEntry_Object = MibTableRow
gBondEthBceStatusEntry = _GBondEthBceStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 2, 1, 1)
)
gBondEthBceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondEthBceStatusEntry.setStatus("current")
_GBondEthBceTcInCodingErrors_Type = Counter32
_GBondEthBceTcInCodingErrors_Object = MibTableColumn
gBondEthBceTcInCodingErrors = _GBondEthBceTcInCodingErrors_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 2, 1, 1, 1),
    _GBondEthBceTcInCodingErrors_Type()
)
gBondEthBceTcInCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthBceTcInCodingErrors.setStatus("current")
_GBondEthBceTcInCrcErrors_Type = Counter32
_GBondEthBceTcInCrcErrors_Object = MibTableColumn
gBondEthBceTcInCrcErrors = _GBondEthBceTcInCrcErrors_Object(
    (1, 3, 6, 1, 2, 1, 211, 2, 1, 2, 1, 1, 2),
    _GBondEthBceTcInCrcErrors_Type()
)
gBondEthBceTcInCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondEthBceTcInCrcErrors.setStatus("current")
_GBondEthConformance_ObjectIdentity = ObjectIdentity
gBondEthConformance = _GBondEthConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 2, 2)
)
_GBondEthGroups_ObjectIdentity = ObjectIdentity
gBondEthGroups = _GBondEthGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 2, 2, 1)
)
_GBondEthCompliances_ObjectIdentity = ObjectIdentity
gBondEthCompliances = _GBondEthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 2, 2, 2)
)

# Managed Objects groups

gBondEthBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 2, 1, 1)
)
gBondEthBasicGroup.setObjects(
      *(("GBOND-ETH-MIB", "gBondEthTcTypesSupported"),
        ("GBOND-ETH-MIB", "gBondEthTcAdminType"),
        ("GBOND-ETH-MIB", "gBondEthTcOperType"),
        ("GBOND-ETH-MIB", "gBondEthInErrors"),
        ("GBOND-ETH-MIB", "gBondEthInSmallFragments"),
        ("GBOND-ETH-MIB", "gBondEthInLargeFragments"),
        ("GBOND-ETH-MIB", "gBondEthInBadFragments"),
        ("GBOND-ETH-MIB", "gBondEthInLostFragments"),
        ("GBOND-ETH-MIB", "gBondEthInLostStarts"),
        ("GBOND-ETH-MIB", "gBondEthInLostEnds"),
        ("GBOND-ETH-MIB", "gBondEthInOverflows"),
        ("GBOND-ETH-MIB", "gBondEthBceTcInCodingErrors"),
        ("GBOND-ETH-MIB", "gBondEthBceTcInCrcErrors"))
)
if mibBuilder.loadTexts:
    gBondEthBasicGroup.setStatus("current")

gBondEthBceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 2, 2, 1, 2)
)
gBondEthBceGroup.setObjects(
      *(("GBOND-ETH-MIB", "gBondEthBceTcInCodingErrors"),
        ("GBOND-ETH-MIB", "gBondEthBceTcInCrcErrors"))
)
if mibBuilder.loadTexts:
    gBondEthBceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gBondEthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 211, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gBondEthCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBOND-ETH-MIB",
    **{"GBondEthPtmTcType": GBondEthPtmTcType,
       "gBondEthMIB": gBondEthMIB,
       "gBondEthObjects": gBondEthObjects,
       "gBondEthPort": gBondEthPort,
       "gBondEthPortConfTable": gBondEthPortConfTable,
       "gBondEthPortConfEntry": gBondEthPortConfEntry,
       "gBondEthTcAdminType": gBondEthTcAdminType,
       "gBondEthPortCapabilityTable": gBondEthPortCapabilityTable,
       "gBondEthPortCapabilityEntry": gBondEthPortCapabilityEntry,
       "gBondEthTcTypesSupported": gBondEthTcTypesSupported,
       "gBondEthPortStatusTable": gBondEthPortStatusTable,
       "gBondEthPortStatusEntry": gBondEthPortStatusEntry,
       "gBondEthTcOperType": gBondEthTcOperType,
       "gBondEthInErrors": gBondEthInErrors,
       "gBondEthInSmallFragments": gBondEthInSmallFragments,
       "gBondEthInLargeFragments": gBondEthInLargeFragments,
       "gBondEthInBadFragments": gBondEthInBadFragments,
       "gBondEthInLostFragments": gBondEthInLostFragments,
       "gBondEthInLostStarts": gBondEthInLostStarts,
       "gBondEthInLostEnds": gBondEthInLostEnds,
       "gBondEthInOverflows": gBondEthInOverflows,
       "gBondEthBce": gBondEthBce,
       "gBondEthBceStatusTable": gBondEthBceStatusTable,
       "gBondEthBceStatusEntry": gBondEthBceStatusEntry,
       "gBondEthBceTcInCodingErrors": gBondEthBceTcInCodingErrors,
       "gBondEthBceTcInCrcErrors": gBondEthBceTcInCrcErrors,
       "gBondEthConformance": gBondEthConformance,
       "gBondEthGroups": gBondEthGroups,
       "gBondEthBasicGroup": gBondEthBasicGroup,
       "gBondEthBceGroup": gBondEthBceGroup,
       "gBondEthCompliances": gBondEthCompliances,
       "gBondEthCompliance": gBondEthCompliance}
)
