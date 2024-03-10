"""SNMP MIB module (QB-CESV2-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-CESV2-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 11:37:30 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(AtmConnKind,
 AtmVorXOperStatus,
 AtmVpIdentifier,
 AtmConnCastType,
 atmNoClpNoScr,
 AtmVorXLastChange,
 AtmAddr,
 AtmServiceCategory,
 AtmVorXAdminStatus,
 AtmVcIdentifier,
 AtmTrafficDescrParamIndex) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmConnKind",
    "AtmVorXOperStatus",
    "AtmVpIdentifier",
    "AtmConnCastType",
    "atmNoClpNoScr",
    "AtmVorXLastChange",
    "AtmAddr",
    "AtmServiceCategory",
    "AtmVorXAdminStatus",
    "AtmVcIdentifier",
    "AtmTrafficDescrParamIndex")

(atmfCESStatsEntry,
 atmfCESConfEntry) = mibBuilder.importSymbols(
    "ATMF-CES",
    "atmfCESStatsEntry",
    "atmfCESConfEntry")

(QbPvcConnKind,
 QbBitRate,
 QbEnableStatus) = mibBuilder.importSymbols(
    "QB-DWS-MIB",
    "QbPvcConnKind",
    "QbBitRate",
    "QbEnableStatus")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(IpAddress,
 Integer32,
 NotificationType,
 ObjectIdentity,
 MibIdentifier,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 ModuleIdentity,
 Counter64,
 iso,
 Bits,
 Gauge32,
 Counter32,
 TimeTicks,
 Unsigned32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "IpAddress",
    "Integer32",
    "NotificationType",
    "ObjectIdentity",
    "MibIdentifier",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "ModuleIdentity",
    "Counter64",
    "iso",
    "Bits",
    "Gauge32",
    "Counter32",
    "TimeTicks",
    "Unsigned32")

(TextualConvention,
 TimeStamp,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "TimeStamp",
    "DisplayString")


# MODULE-IDENTITY

qbCESMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4)
)
qbCESMIB.setLastUpdated("0002142001Z")
if mibBuilder.loadTexts:
    qbCESMIB.setOrganization("""\
Quantum Bridge Inc.
""")
qbCESMIB.setContactInfo("""\
mvaysman@quantumbridge.com
""")
if mibBuilder.loadTexts:
    qbCESMIB.setDescription("""\
This module defines additional objects for the management of DS1 links in
Quantum Bridge devices, above and beyond that is defined in the standard CESV2
mib, and proposed drafts.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QbCESObjects_ObjectIdentity = ObjectIdentity
qbCESObjects = _QbCESObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 1)
)
_QbCESTables_ObjectIdentity = ObjectIdentity
qbCESTables = _QbCESTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2)
)
_QbCESConfTable_Object = MibTable
qbCESConfTable = _QbCESConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    qbCESConfTable.setStatus("current")
if mibBuilder.loadTexts:
    qbCESConfTable.setDescription("""\
The Quantum Bridge CES Configuration Table contains extensions to the CES V2
Configuration Table.
""")
_QbCESConfEntry_Object = MibTableRow
qbCESConfEntry = _QbCESConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 1, 1)
)
atmfCESConfEntry.registerAugmentions(
    ("QB-CESV2-MIB",
     "qbCESConfEntry")
)
qbCESConfEntry.setIndexNames(*atmfCESConfEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbCESConfEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbCESConfEntry.setDescription("""\
An entry in the Quantum Bridge CES Configuration Table.
""")


class _QbCESConfConnName_Type(DisplayString):
    """Custom type qbCESConfConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbCESConfConnName_Type.__name__ = "DisplayString"
_QbCESConfConnName_Object = MibTableColumn
qbCESConfConnName = _QbCESConfConnName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 1, 1, 1),
    _QbCESConfConnName_Type()
)
qbCESConfConnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCESConfConnName.setStatus("current")
if mibBuilder.loadTexts:
    qbCESConfConnName.setDescription("""\
A textual description for the CBR traffic conection.
""")


class _QbCESConfConnRxTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type qbCESConfConnRxTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 1


_QbCESConfConnRxTrafficDescrIndex_Object = MibTableColumn
qbCESConfConnRxTrafficDescrIndex = _QbCESConfConnRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 1, 1, 2),
    _QbCESConfConnRxTrafficDescrIndex_Type()
)
qbCESConfConnRxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCESConfConnRxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbCESConfConnRxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row in the ATM Traffic Descriptor Table
which applies to the receive direction of this VCL.
""")


class _QbCESConfConnTxTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type qbCESConfConnTxTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 1


_QbCESConfConnTxTrafficDescrIndex_Object = MibTableColumn
qbCESConfConnTxTrafficDescrIndex = _QbCESConfConnTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 1, 1, 3),
    _QbCESConfConnTxTrafficDescrIndex_Type()
)
qbCESConfConnTxTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCESConfConnTxTrafficDescrIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbCESConfConnTxTrafficDescrIndex.setDescription("""\
The value of this object identifies the row in the ATM Traffic Descriptor Table
which applies to the transmit direction of this VCL.
""")
_QbCESConfConnLoopback_Type = QbEnableStatus
_QbCESConfConnLoopback_Object = MibTableColumn
qbCESConfConnLoopback = _QbCESConfConnLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 1, 1, 4),
    _QbCESConfConnLoopback_Type()
)
qbCESConfConnLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCESConfConnLoopback.setStatus("current")
if mibBuilder.loadTexts:
    qbCESConfConnLoopback.setDescription("""\
This object enables loopback on the IOT DS1/E1 enedpoint.
""")
_QbCESConfConnKind_Type = QbPvcConnKind
_QbCESConfConnKind_Object = MibTableColumn
qbCESConfConnKind = _QbCESConfConnKind_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 1, 1, 5),
    _QbCESConfConnKind_Type()
)
qbCESConfConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbCESConfConnKind.setStatus("current")
if mibBuilder.loadTexts:
    qbCESConfConnKind.setDescription("""\
The PVC connection type.
""")
_QbCESStatsTable_Object = MibTable
qbCESStatsTable = _QbCESStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    qbCESStatsTable.setStatus("current")
if mibBuilder.loadTexts:
    qbCESStatsTable.setDescription("""\
The Quantum Bridge CES Statistics Table contains extensions to the CES V2
Statistics Table.
""")
_QbCESStatsEntry_Object = MibTableRow
qbCESStatsEntry = _QbCESStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 2, 1)
)
atmfCESStatsEntry.registerAugmentions(
    ("QB-CESV2-MIB",
     "qbCESStatsEntry")
)
qbCESStatsEntry.setIndexNames(*atmfCESStatsEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbCESStatsEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbCESStatsEntry.setDescription("""\
An entry in the Quantum Bridge CES Statistics Table.
""")
_QbCESStatsTxCells_Type = Counter32
_QbCESStatsTxCells_Object = MibTableColumn
qbCESStatsTxCells = _QbCESStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 2, 1, 1),
    _QbCESStatsTxCells_Type()
)
qbCESStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbCESStatsTxCells.setStatus("current")
if mibBuilder.loadTexts:
    qbCESStatsTxCells.setDescription("""\
Cells transmitted on this emulated circuit.
""")
_QbCESStatsCrcErrs_Type = Counter32
_QbCESStatsCrcErrs_Object = MibTableColumn
qbCESStatsCrcErrs = _QbCESStatsCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 2, 1, 2),
    _QbCESStatsCrcErrs_Type()
)
qbCESStatsCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbCESStatsCrcErrs.setStatus("current")
if mibBuilder.loadTexts:
    qbCESStatsCrcErrs.setDescription("""\
The count of CRC errors.
""")
_QbCESStatsReplacedCells_Type = Counter32
_QbCESStatsReplacedCells_Object = MibTableColumn
qbCESStatsReplacedCells = _QbCESStatsReplacedCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 2, 1, 3),
    _QbCESStatsReplacedCells_Type()
)
qbCESStatsReplacedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbCESStatsReplacedCells.setStatus("current")
if mibBuilder.loadTexts:
    qbCESStatsReplacedCells.setDescription("""\
Replaced Cells.
""")
_QbCESStatsDroppedCells_Type = Counter32
_QbCESStatsDroppedCells_Object = MibTableColumn
qbCESStatsDroppedCells = _QbCESStatsDroppedCells_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 2, 2, 1, 4),
    _QbCESStatsDroppedCells_Type()
)
qbCESStatsDroppedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbCESStatsDroppedCells.setStatus("current")
if mibBuilder.loadTexts:
    qbCESStatsDroppedCells.setDescription("""\
Dropped Cells.
""")
_QbCESConformance_ObjectIdentity = ObjectIdentity
qbCESConformance = _QbCESConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 3)
)
_QbCESCompliances_ObjectIdentity = ObjectIdentity
qbCESCompliances = _QbCESCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 3, 1)
)
_QbCESGroups_ObjectIdentity = ObjectIdentity
qbCESGroups = _QbCESGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 3, 2)
)

# Managed Objects groups

qbCESAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 3, 2, 1)
)
qbCESAllGroup.setObjects(
      *(("QB-CESV2-MIB", "qbCESConfConnName"),
        ("QB-CESV2-MIB", "qbCESConfConnRxTrafficDescrIndex"),
        ("QB-CESV2-MIB", "qbCESConfConnTxTrafficDescrIndex"),
        ("QB-CESV2-MIB", "qbCESConfConnLoopback"),
        ("QB-CESV2-MIB", "qbCESStatsTxCells"),
        ("QB-CESV2-MIB", "qbCESStatsCrcErrs"),
        ("QB-CESV2-MIB", "qbCESStatsReplacedCells"),
        ("QB-CESV2-MIB", "qbCESStatsDroppedCells"))
)
if mibBuilder.loadTexts:
    qbCESAllGroup.setStatus("current")
if mibBuilder.loadTexts:
    qbCESAllGroup.setDescription("""\
The set of all accessible objects in this MIB.
""")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbCESCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbCESCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    qbCESCompliance.setDescription("""\
The compliance statement for all agents that support this MIB. A compliant
agent implements all objects defined in this MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-CESV2-MIB",
    **{"qbCESMIB": qbCESMIB,
       "qbCESObjects": qbCESObjects,
       "qbCESTables": qbCESTables,
       "qbCESConfTable": qbCESConfTable,
       "qbCESConfEntry": qbCESConfEntry,
       "qbCESConfConnName": qbCESConfConnName,
       "qbCESConfConnRxTrafficDescrIndex": qbCESConfConnRxTrafficDescrIndex,
       "qbCESConfConnTxTrafficDescrIndex": qbCESConfConnTxTrafficDescrIndex,
       "qbCESConfConnLoopback": qbCESConfConnLoopback,
       "qbCESConfConnKind": qbCESConfConnKind,
       "qbCESStatsTable": qbCESStatsTable,
       "qbCESStatsEntry": qbCESStatsEntry,
       "qbCESStatsTxCells": qbCESStatsTxCells,
       "qbCESStatsCrcErrs": qbCESStatsCrcErrs,
       "qbCESStatsReplacedCells": qbCESStatsReplacedCells,
       "qbCESStatsDroppedCells": qbCESStatsDroppedCells,
       "qbCESConformance": qbCESConformance,
       "qbCESCompliances": qbCESCompliances,
       "qbCESCompliance": qbCESCompliance,
       "qbCESGroups": qbCESGroups,
       "qbCESAllGroup": qbCESAllGroup}
)
