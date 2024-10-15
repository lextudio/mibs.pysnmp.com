# SNMP MIB module (PDN-IFDEV-IWF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-IFDEV-IWF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:45 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

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

pdnIfDevIwfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27)
)
pdnIfDevIwfMIB.setRevisions(
        ("2004-09-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TxRxUnit(Integer32, TextualConvention):
    status = "current"
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
        *(("bits", 2),
          ("datagrams", 6),
          ("frames", 4),
          ("octets", 3),
          ("other", 1),
          ("packets", 5))
    )



# MIB Managed Objects in the order of their OIDs

_PdnIfDevIwfNotifications_ObjectIdentity = ObjectIdentity
pdnIfDevIwfNotifications = _PdnIfDevIwfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 0)
)
_PdnIfDevIwfObjects_ObjectIdentity = ObjectIdentity
pdnIfDevIwfObjects = _PdnIfDevIwfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1)
)
_PdnIfDevIwfStatsTotalTable_Object = MibTable
pdnIfDevIwfStatsTotalTable = _PdnIfDevIwfStatsTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1)
)
if mibBuilder.loadTexts:
    pdnIfDevIwfStatsTotalTable.setStatus("current")
_PdnIfDevIwfStatsTotalEntry_Object = MibTableRow
pdnIfDevIwfStatsTotalEntry = _PdnIfDevIwfStatsTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1)
)
pdnIfDevIwfStatsTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnIfDevIwfStatsTotalEntry.setStatus("current")
_PdnIfDevIwfStatsTotalBufferUnderruns_Type = Counter32
_PdnIfDevIwfStatsTotalBufferUnderruns_Object = MibTableColumn
pdnIfDevIwfStatsTotalBufferUnderruns = _PdnIfDevIwfStatsTotalBufferUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 1),
    _PdnIfDevIwfStatsTotalBufferUnderruns_Type()
)
pdnIfDevIwfStatsTotalBufferUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIfDevIwfStatsTotalBufferUnderruns.setStatus("current")
_PdnIfDevIwfStatsTotalMRUErrors_Type = Counter32
_PdnIfDevIwfStatsTotalMRUErrors_Object = MibTableColumn
pdnIfDevIwfStatsTotalMRUErrors = _PdnIfDevIwfStatsTotalMRUErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 2),
    _PdnIfDevIwfStatsTotalMRUErrors_Type()
)
pdnIfDevIwfStatsTotalMRUErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIfDevIwfStatsTotalMRUErrors.setStatus("current")
_PdnIfDevIwfStatsTotalRxUnit_Type = TxRxUnit
_PdnIfDevIwfStatsTotalRxUnit_Object = MibTableColumn
pdnIfDevIwfStatsTotalRxUnit = _PdnIfDevIwfStatsTotalRxUnit_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 3),
    _PdnIfDevIwfStatsTotalRxUnit_Type()
)
pdnIfDevIwfStatsTotalRxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIfDevIwfStatsTotalRxUnit.setStatus("current")
_PdnIfDevIwfStatsTotalRx_Type = Counter32
_PdnIfDevIwfStatsTotalRx_Object = MibTableColumn
pdnIfDevIwfStatsTotalRx = _PdnIfDevIwfStatsTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 4),
    _PdnIfDevIwfStatsTotalRx_Type()
)
pdnIfDevIwfStatsTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIfDevIwfStatsTotalRx.setStatus("current")
_PdnIfDevIwfAFNs_ObjectIdentity = ObjectIdentity
pdnIfDevIwfAFNs = _PdnIfDevIwfAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 2)
)
_PdnIfDevIwfConformance_ObjectIdentity = ObjectIdentity
pdnIfDevIwfConformance = _PdnIfDevIwfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3)
)
_PdnIfDevIwfCompliances_ObjectIdentity = ObjectIdentity
pdnIfDevIwfCompliances = _PdnIfDevIwfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 1)
)
_PdnIfDevIwfGroups_ObjectIdentity = ObjectIdentity
pdnIfDevIwfGroups = _PdnIfDevIwfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2)
)
_PdnIfDevIwfObjGroups_ObjectIdentity = ObjectIdentity
pdnIfDevIwfObjGroups = _PdnIfDevIwfObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1)
)
_PdnIfDevIwfAfnGroups_ObjectIdentity = ObjectIdentity
pdnIfDevIwfAfnGroups = _PdnIfDevIwfAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 2)
)
_PdnIfDevIwfNtfyGroups_ObjectIdentity = ObjectIdentity
pdnIfDevIwfNtfyGroups = _PdnIfDevIwfNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 3)
)

# Managed Objects groups

pdnIfDevIwfStatsTotalBufferUnderrunsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 1)
)
pdnIfDevIwfStatsTotalBufferUnderrunsGroup.setObjects(
    ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalBufferUnderruns")
)
if mibBuilder.loadTexts:
    pdnIfDevIwfStatsTotalBufferUnderrunsGroup.setStatus("current")

pdnIfDevIwfStatsTotalMRUErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 2)
)
pdnIfDevIwfStatsTotalMRUErrorsGroup.setObjects(
    ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalMRUErrors")
)
if mibBuilder.loadTexts:
    pdnIfDevIwfStatsTotalMRUErrorsGroup.setStatus("current")

pdnIfDevIwfStatsTotalRxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 3)
)
pdnIfDevIwfStatsTotalRxGroup.setObjects(
      *(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRxUnit"),
        ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRx"))
)
if mibBuilder.loadTexts:
    pdnIfDevIwfStatsTotalRxGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnIfDevIwfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnIfDevIwfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-IFDEV-IWF-MIB",
    **{"TxRxUnit": TxRxUnit,
       "pdnIfDevIwfMIB": pdnIfDevIwfMIB,
       "pdnIfDevIwfNotifications": pdnIfDevIwfNotifications,
       "pdnIfDevIwfObjects": pdnIfDevIwfObjects,
       "pdnIfDevIwfStatsTotalTable": pdnIfDevIwfStatsTotalTable,
       "pdnIfDevIwfStatsTotalEntry": pdnIfDevIwfStatsTotalEntry,
       "pdnIfDevIwfStatsTotalBufferUnderruns": pdnIfDevIwfStatsTotalBufferUnderruns,
       "pdnIfDevIwfStatsTotalMRUErrors": pdnIfDevIwfStatsTotalMRUErrors,
       "pdnIfDevIwfStatsTotalRxUnit": pdnIfDevIwfStatsTotalRxUnit,
       "pdnIfDevIwfStatsTotalRx": pdnIfDevIwfStatsTotalRx,
       "pdnIfDevIwfAFNs": pdnIfDevIwfAFNs,
       "pdnIfDevIwfConformance": pdnIfDevIwfConformance,
       "pdnIfDevIwfCompliances": pdnIfDevIwfCompliances,
       "pdnIfDevIwfCompliance": pdnIfDevIwfCompliance,
       "pdnIfDevIwfGroups": pdnIfDevIwfGroups,
       "pdnIfDevIwfObjGroups": pdnIfDevIwfObjGroups,
       "pdnIfDevIwfStatsTotalBufferUnderrunsGroup": pdnIfDevIwfStatsTotalBufferUnderrunsGroup,
       "pdnIfDevIwfStatsTotalMRUErrorsGroup": pdnIfDevIwfStatsTotalMRUErrorsGroup,
       "pdnIfDevIwfStatsTotalRxGroup": pdnIfDevIwfStatsTotalRxGroup,
       "pdnIfDevIwfAfnGroups": pdnIfDevIwfAfnGroups,
       "pdnIfDevIwfNtfyGroups": pdnIfDevIwfNtfyGroups}
)
