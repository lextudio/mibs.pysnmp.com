# SNMP MIB module (XEDIA-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:41 2024
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

(aal5VccEntry,
 atmInterfaceConfEntry,
 atmInterfaceDs3PlcpEntry,
 atmTrafficDescrParamEntry) = mibBuilder.importSymbols(
    "ATM-MIB",
    "aal5VccEntry",
    "atmInterfaceConfEntry",
    "atmInterfaceDs3PlcpEntry",
    "atmTrafficDescrParamEntry")

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

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XAtmObjects_ObjectIdentity = ObjectIdentity
xAtmObjects = _XAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 1)
)
_XAtmTables_ObjectIdentity = ObjectIdentity
xAtmTables = _XAtmTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2)
)
_XAtmInterfaceConfTable_Object = MibTable
xAtmInterfaceConfTable = _XAtmInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 1)
)
if mibBuilder.loadTexts:
    xAtmInterfaceConfTable.setStatus("current")
_XAtmInterfaceConfEntry_Object = MibTableRow
xAtmInterfaceConfEntry = _XAtmInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xAtmInterfaceConfEntry.setStatus("current")


class _XAtmInterfaceEmptyCells_Type(Integer32):
    """Custom type xAtmInterfaceEmptyCells based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("unassigned", 2))
    )


_XAtmInterfaceEmptyCells_Type.__name__ = "Integer32"
_XAtmInterfaceEmptyCells_Object = MibTableColumn
xAtmInterfaceEmptyCells = _XAtmInterfaceEmptyCells_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 1, 1, 1),
    _XAtmInterfaceEmptyCells_Type()
)
xAtmInterfaceEmptyCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xAtmInterfaceEmptyCells.setStatus("current")
_XAtmInterfaceDs3PlcpTable_Object = MibTable
xAtmInterfaceDs3PlcpTable = _XAtmInterfaceDs3PlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 2)
)
if mibBuilder.loadTexts:
    xAtmInterfaceDs3PlcpTable.setStatus("current")
_XAtmInterfaceDs3PlcpEntry_Object = MibTableRow
xAtmInterfaceDs3PlcpEntry = _XAtmInterfaceDs3PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xAtmInterfaceDs3PlcpEntry.setStatus("current")


class _XAtmInterfaceDs3PlcpCellAlign_Type(Integer32):
    """Custom type xAtmInterfaceDs3PlcpCellAlign based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hec", 1),
          ("plcp", 2))
    )


_XAtmInterfaceDs3PlcpCellAlign_Type.__name__ = "Integer32"
_XAtmInterfaceDs3PlcpCellAlign_Object = MibTableColumn
xAtmInterfaceDs3PlcpCellAlign = _XAtmInterfaceDs3PlcpCellAlign_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 2, 1, 1),
    _XAtmInterfaceDs3PlcpCellAlign_Type()
)
xAtmInterfaceDs3PlcpCellAlign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xAtmInterfaceDs3PlcpCellAlign.setStatus("current")
_XAtmTrafficDescrTable_Object = MibTable
xAtmTrafficDescrTable = _XAtmTrafficDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 3)
)
if mibBuilder.loadTexts:
    xAtmTrafficDescrTable.setStatus("current")
_XAtmTrafficDescrEntry_Object = MibTableRow
xAtmTrafficDescrEntry = _XAtmTrafficDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 3, 1)
)
if mibBuilder.loadTexts:
    xAtmTrafficDescrEntry.setStatus("current")


class _XAtmTrafficDescrDescr_Type(DisplayString):
    """Custom type xAtmTrafficDescrDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_XAtmTrafficDescrDescr_Type.__name__ = "DisplayString"
_XAtmTrafficDescrDescr_Object = MibTableColumn
xAtmTrafficDescrDescr = _XAtmTrafficDescrDescr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 3, 1, 1),
    _XAtmTrafficDescrDescr_Type()
)
xAtmTrafficDescrDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xAtmTrafficDescrDescr.setStatus("current")


class _XAtmTrafficDescrQoSClass_Type(Integer32):
    """Custom type xAtmTrafficDescrQoSClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("ubr", 0),
          ("vbrAudioVideo", 2),
          ("vbrConnData", 3),
          ("vbrConnlessData", 4))
    )


_XAtmTrafficDescrQoSClass_Type.__name__ = "Integer32"
_XAtmTrafficDescrQoSClass_Object = MibTableColumn
xAtmTrafficDescrQoSClass = _XAtmTrafficDescrQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 3, 1, 2),
    _XAtmTrafficDescrQoSClass_Type()
)
xAtmTrafficDescrQoSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xAtmTrafficDescrQoSClass.setStatus("current")
_XAtmAal5VccTable_Object = MibTable
xAtmAal5VccTable = _XAtmAal5VccTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4)
)
if mibBuilder.loadTexts:
    xAtmAal5VccTable.setStatus("current")
_XAtmAal5VccEntry_Object = MibTableRow
xAtmAal5VccEntry = _XAtmAal5VccEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1)
)
if mibBuilder.loadTexts:
    xAtmAal5VccEntry.setStatus("current")
_XAtmAal5VccTxPdus_Type = Counter32
_XAtmAal5VccTxPdus_Object = MibTableColumn
xAtmAal5VccTxPdus = _XAtmAal5VccTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 1),
    _XAtmAal5VccTxPdus_Type()
)
xAtmAal5VccTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xAtmAal5VccTxPdus.setStatus("current")
_XAtmAal5VccTxOctets_Type = Counter32
_XAtmAal5VccTxOctets_Object = MibTableColumn
xAtmAal5VccTxOctets = _XAtmAal5VccTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 2),
    _XAtmAal5VccTxOctets_Type()
)
xAtmAal5VccTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xAtmAal5VccTxOctets.setStatus("current")
_XAtmAal5VccTxPduFailures_Type = Counter32
_XAtmAal5VccTxPduFailures_Object = MibTableColumn
xAtmAal5VccTxPduFailures = _XAtmAal5VccTxPduFailures_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 3),
    _XAtmAal5VccTxPduFailures_Type()
)
xAtmAal5VccTxPduFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xAtmAal5VccTxPduFailures.setStatus("current")
_XAtmAal5VccRxPdus_Type = Counter32
_XAtmAal5VccRxPdus_Object = MibTableColumn
xAtmAal5VccRxPdus = _XAtmAal5VccRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 4),
    _XAtmAal5VccRxPdus_Type()
)
xAtmAal5VccRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xAtmAal5VccRxPdus.setStatus("current")
_XAtmAal5VccRxOctets_Type = Counter32
_XAtmAal5VccRxOctets_Object = MibTableColumn
xAtmAal5VccRxOctets = _XAtmAal5VccRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 5),
    _XAtmAal5VccRxOctets_Type()
)
xAtmAal5VccRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xAtmAal5VccRxOctets.setStatus("current")
_XAtmAal5VccRxPduDiscards_Type = Counter32
_XAtmAal5VccRxPduDiscards_Object = MibTableColumn
xAtmAal5VccRxPduDiscards = _XAtmAal5VccRxPduDiscards_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 2, 4, 1, 6),
    _XAtmAal5VccRxPduDiscards_Type()
)
xAtmAal5VccRxPduDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xAtmAal5VccRxPduDiscards.setStatus("current")
_XAtmConformance_ObjectIdentity = ObjectIdentity
xAtmConformance = _XAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 3)
)
_XAtmCompliances_ObjectIdentity = ObjectIdentity
xAtmCompliances = _XAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 3, 1)
)
_XAtmGroups_ObjectIdentity = ObjectIdentity
xAtmGroups = _XAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 3, 2)
)
atmInterfaceConfEntry.registerAugmentions(
    ("XEDIA-ATM-MIB",
     "xAtmInterfaceConfEntry")
)
xAtmInterfaceConfEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
atmInterfaceDs3PlcpEntry.registerAugmentions(
    ("XEDIA-ATM-MIB",
     "xAtmInterfaceDs3PlcpEntry")
)
xAtmInterfaceDs3PlcpEntry.setIndexNames(*atmInterfaceDs3PlcpEntry.getIndexNames())
atmTrafficDescrParamEntry.registerAugmentions(
    ("XEDIA-ATM-MIB",
     "xAtmTrafficDescrEntry")
)
xAtmTrafficDescrEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
aal5VccEntry.registerAugmentions(
    ("XEDIA-ATM-MIB",
     "xAtmAal5VccEntry")
)
xAtmAal5VccEntry.setIndexNames(*aal5VccEntry.getIndexNames())

# Managed Objects groups

xAtmAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 3, 2, 1)
)
xAtmAllGroup.setObjects(
      *(("XEDIA-ATM-MIB", "xAtmInterfaceEmptyCells"),
        ("XEDIA-ATM-MIB", "xAtmInterfaceDs3PlcpCellAlign"),
        ("XEDIA-ATM-MIB", "xAtmTrafficDescrDescr"),
        ("XEDIA-ATM-MIB", "xAtmTrafficDescrQoSClass"),
        ("XEDIA-ATM-MIB", "xAtmAal5VccTxPdus"),
        ("XEDIA-ATM-MIB", "xAtmAal5VccTxOctets"),
        ("XEDIA-ATM-MIB", "xAtmAal5VccTxPduFailures"),
        ("XEDIA-ATM-MIB", "xAtmAal5VccRxPdus"),
        ("XEDIA-ATM-MIB", "xAtmAal5VccRxOctets"),
        ("XEDIA-ATM-MIB", "xAtmAal5VccRxPduDiscards"))
)
if mibBuilder.loadTexts:
    xAtmAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xAtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 12, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xAtmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-ATM-MIB",
    **{"xediaAtmMIB": xediaAtmMIB,
       "xAtmObjects": xAtmObjects,
       "xAtmTables": xAtmTables,
       "xAtmInterfaceConfTable": xAtmInterfaceConfTable,
       "xAtmInterfaceConfEntry": xAtmInterfaceConfEntry,
       "xAtmInterfaceEmptyCells": xAtmInterfaceEmptyCells,
       "xAtmInterfaceDs3PlcpTable": xAtmInterfaceDs3PlcpTable,
       "xAtmInterfaceDs3PlcpEntry": xAtmInterfaceDs3PlcpEntry,
       "xAtmInterfaceDs3PlcpCellAlign": xAtmInterfaceDs3PlcpCellAlign,
       "xAtmTrafficDescrTable": xAtmTrafficDescrTable,
       "xAtmTrafficDescrEntry": xAtmTrafficDescrEntry,
       "xAtmTrafficDescrDescr": xAtmTrafficDescrDescr,
       "xAtmTrafficDescrQoSClass": xAtmTrafficDescrQoSClass,
       "xAtmAal5VccTable": xAtmAal5VccTable,
       "xAtmAal5VccEntry": xAtmAal5VccEntry,
       "xAtmAal5VccTxPdus": xAtmAal5VccTxPdus,
       "xAtmAal5VccTxOctets": xAtmAal5VccTxOctets,
       "xAtmAal5VccTxPduFailures": xAtmAal5VccTxPduFailures,
       "xAtmAal5VccRxPdus": xAtmAal5VccRxPdus,
       "xAtmAal5VccRxOctets": xAtmAal5VccRxOctets,
       "xAtmAal5VccRxPduDiscards": xAtmAal5VccRxPduDiscards,
       "xAtmConformance": xAtmConformance,
       "xAtmCompliances": xAtmCompliances,
       "xAtmCompliance": xAtmCompliance,
       "xAtmGroups": xAtmGroups,
       "xAtmAllGroup": xAtmAllGroup}
)
