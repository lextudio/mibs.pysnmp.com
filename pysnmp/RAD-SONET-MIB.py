# SNMP MIB module (RAD-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAD-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:19 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

(diverseIfWanGen,) = mibBuilder.importSymbols(
    "RAD-MIB",
    "diverseIfWanGen")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonetInterface_ObjectIdentity = ObjectIdentity
sonetInterface = _SonetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2)
)
_PrtSonetPerfHistory_ObjectIdentity = ObjectIdentity
prtSonetPerfHistory = _PrtSonetPerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1)
)
_PrtSonetMediumTable_Object = MibTable
prtSonetMediumTable = _PrtSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    prtSonetMediumTable.setStatus("current")
_PrtSonetMediumEntry_Object = MibTableRow
prtSonetMediumEntry = _PrtSonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 1, 1)
)
prtSonetMediumEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtSonetMediumEntry.setStatus("current")


class _PrtSonetMediumTimeElapsed_Type(Integer32):
    """Custom type prtSonetMediumTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_PrtSonetMediumTimeElapsed_Type.__name__ = "Integer32"
_PrtSonetMediumTimeElapsed_Object = MibTableColumn
prtSonetMediumTimeElapsed = _PrtSonetMediumTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 1, 1, 1),
    _PrtSonetMediumTimeElapsed_Type()
)
prtSonetMediumTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetMediumTimeElapsed.setStatus("current")


class _PrtSonetMediumValidIntervals_Type(Integer32):
    """Custom type prtSonetMediumValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_PrtSonetMediumValidIntervals_Type.__name__ = "Integer32"
_PrtSonetMediumValidIntervals_Object = MibTableColumn
prtSonetMediumValidIntervals = _PrtSonetMediumValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 1, 1, 2),
    _PrtSonetMediumValidIntervals_Type()
)
prtSonetMediumValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetMediumValidIntervals.setStatus("current")
_PrtSonetSectionLineCurrentTable_Object = MibTable
prtSonetSectionLineCurrentTable = _PrtSonetSectionLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    prtSonetSectionLineCurrentTable.setStatus("current")
_PrtSectionLineCurrentEntry_Object = MibTableRow
prtSectionLineCurrentEntry = _PrtSectionLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1)
)
prtSectionLineCurrentEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtSectionLineCurrentEntry.setStatus("current")
_PrtSonetCurrentLOS_Type = Gauge32
_PrtSonetCurrentLOS_Object = MibTableColumn
prtSonetCurrentLOS = _PrtSonetCurrentLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 1),
    _PrtSonetCurrentLOS_Type()
)
prtSonetCurrentLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLOS.setStatus("current")
_PrtSonetCurrentLOF_Type = Gauge32
_PrtSonetCurrentLOF_Object = MibTableColumn
prtSonetCurrentLOF = _PrtSonetCurrentLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 2),
    _PrtSonetCurrentLOF_Type()
)
prtSonetCurrentLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLOF.setStatus("current")
_PrtSonetCurrentLineAIS_Type = Gauge32
_PrtSonetCurrentLineAIS_Object = MibTableColumn
prtSonetCurrentLineAIS = _PrtSonetCurrentLineAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 3),
    _PrtSonetCurrentLineAIS_Type()
)
prtSonetCurrentLineAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLineAIS.setStatus("current")
_PrtSonetCurrentLineFERF_Type = Gauge32
_PrtSonetCurrentLineFERF_Object = MibTableColumn
prtSonetCurrentLineFERF = _PrtSonetCurrentLineFERF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 4),
    _PrtSonetCurrentLineFERF_Type()
)
prtSonetCurrentLineFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLineFERF.setStatus("current")
_PrtSonetCurrentSectionBIP_Type = Gauge32
_PrtSonetCurrentSectionBIP_Object = MibTableColumn
prtSonetCurrentSectionBIP = _PrtSonetCurrentSectionBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 5),
    _PrtSonetCurrentSectionBIP_Type()
)
prtSonetCurrentSectionBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentSectionBIP.setStatus("current")
_PrtSonetCurrentLineBIP_Type = Gauge32
_PrtSonetCurrentLineBIP_Object = MibTableColumn
prtSonetCurrentLineBIP = _PrtSonetCurrentLineBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 6),
    _PrtSonetCurrentLineBIP_Type()
)
prtSonetCurrentLineBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLineBIP.setStatus("current")
_PrtSonetCurrentLineFEBE_Type = Gauge32
_PrtSonetCurrentLineFEBE_Object = MibTableColumn
prtSonetCurrentLineFEBE = _PrtSonetCurrentLineFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 7),
    _PrtSonetCurrentLineFEBE_Type()
)
prtSonetCurrentLineFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLineFEBE.setStatus("current")
_PrtSonetCurrentUAS_Type = Gauge32
_PrtSonetCurrentUAS_Object = MibTableColumn
prtSonetCurrentUAS = _PrtSonetCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 8),
    _PrtSonetCurrentUAS_Type()
)
prtSonetCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentUAS.setStatus("current")
_PrtSonetCurrentSES_Type = Gauge32
_PrtSonetCurrentSES_Object = MibTableColumn
prtSonetCurrentSES = _PrtSonetCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 9),
    _PrtSonetCurrentSES_Type()
)
prtSonetCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentSES.setStatus("current")
_PrtSonetCurrentES_Type = Gauge32
_PrtSonetCurrentES_Object = MibTableColumn
prtSonetCurrentES = _PrtSonetCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 10),
    _PrtSonetCurrentES_Type()
)
prtSonetCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentES.setStatus("current")


class _PrtSonetCurrentStatus_Type(OctetString):
    """Custom type prtSonetCurrentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PrtSonetCurrentStatus_Type.__name__ = "OctetString"
_PrtSonetCurrentStatus_Object = MibTableColumn
prtSonetCurrentStatus = _PrtSonetCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 11),
    _PrtSonetCurrentStatus_Type()
)
prtSonetCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentStatus.setStatus("current")
_PrtSonetCurrentLSV_Type = Gauge32
_PrtSonetCurrentLSV_Object = MibTableColumn
prtSonetCurrentLSV = _PrtSonetCurrentLSV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 12),
    _PrtSonetCurrentLSV_Type()
)
prtSonetCurrentLSV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLSV.setStatus("current")
_PrtSonetSectionLineIntervalTable_Object = MibTable
prtSonetSectionLineIntervalTable = _PrtSonetSectionLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    prtSonetSectionLineIntervalTable.setStatus("current")
_PrtSectionLineIntervalEntry_Object = MibTableRow
prtSectionLineIntervalEntry = _PrtSectionLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1)
)
prtSectionLineIntervalEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
    (0, "RAD-SONET-MIB", "prtSonetLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    prtSectionLineIntervalEntry.setStatus("current")


class _PrtSonetLineIntervalNumber_Type(Integer32):
    """Custom type prtSonetLineIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PrtSonetLineIntervalNumber_Type.__name__ = "Integer32"
_PrtSonetLineIntervalNumber_Object = MibTableColumn
prtSonetLineIntervalNumber = _PrtSonetLineIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 1),
    _PrtSonetLineIntervalNumber_Type()
)
prtSonetLineIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetLineIntervalNumber.setStatus("current")
_PrtSonetIntervalLOS_Type = Gauge32
_PrtSonetIntervalLOS_Object = MibTableColumn
prtSonetIntervalLOS = _PrtSonetIntervalLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 2),
    _PrtSonetIntervalLOS_Type()
)
prtSonetIntervalLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLOS.setStatus("current")
_PrtSonetIntervalLOF_Type = Gauge32
_PrtSonetIntervalLOF_Object = MibTableColumn
prtSonetIntervalLOF = _PrtSonetIntervalLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 3),
    _PrtSonetIntervalLOF_Type()
)
prtSonetIntervalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLOF.setStatus("current")
_PrtSonetIntervalLineAIS_Type = Gauge32
_PrtSonetIntervalLineAIS_Object = MibTableColumn
prtSonetIntervalLineAIS = _PrtSonetIntervalLineAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 4),
    _PrtSonetIntervalLineAIS_Type()
)
prtSonetIntervalLineAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLineAIS.setStatus("current")
_PrtSonetIntervalLineFERF_Type = Gauge32
_PrtSonetIntervalLineFERF_Object = MibTableColumn
prtSonetIntervalLineFERF = _PrtSonetIntervalLineFERF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 5),
    _PrtSonetIntervalLineFERF_Type()
)
prtSonetIntervalLineFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLineFERF.setStatus("current")
_PrtSonetIntervalSectionBIP_Type = Gauge32
_PrtSonetIntervalSectionBIP_Object = MibTableColumn
prtSonetIntervalSectionBIP = _PrtSonetIntervalSectionBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 6),
    _PrtSonetIntervalSectionBIP_Type()
)
prtSonetIntervalSectionBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalSectionBIP.setStatus("current")
_PrtSonetIntervalLineBIP_Type = Gauge32
_PrtSonetIntervalLineBIP_Object = MibTableColumn
prtSonetIntervalLineBIP = _PrtSonetIntervalLineBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 7),
    _PrtSonetIntervalLineBIP_Type()
)
prtSonetIntervalLineBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLineBIP.setStatus("current")
_PrtSonetIntervalLineFEBE_Type = Gauge32
_PrtSonetIntervalLineFEBE_Object = MibTableColumn
prtSonetIntervalLineFEBE = _PrtSonetIntervalLineFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 8),
    _PrtSonetIntervalLineFEBE_Type()
)
prtSonetIntervalLineFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLineFEBE.setStatus("current")
_PrtSonetIntervalUAS_Type = Gauge32
_PrtSonetIntervalUAS_Object = MibTableColumn
prtSonetIntervalUAS = _PrtSonetIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 9),
    _PrtSonetIntervalUAS_Type()
)
prtSonetIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalUAS.setStatus("current")
_PrtSonetIntervalSES_Type = Gauge32
_PrtSonetIntervalSES_Object = MibTableColumn
prtSonetIntervalSES = _PrtSonetIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 10),
    _PrtSonetIntervalSES_Type()
)
prtSonetIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalSES.setStatus("current")
_PrtSonetIntervalES_Type = Gauge32
_PrtSonetIntervalES_Object = MibTableColumn
prtSonetIntervalES = _PrtSonetIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 11),
    _PrtSonetIntervalES_Type()
)
prtSonetIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalES.setStatus("current")


class _PrtSonetIntervalStatus_Type(OctetString):
    """Custom type prtSonetIntervalStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PrtSonetIntervalStatus_Type.__name__ = "OctetString"
_PrtSonetIntervalStatus_Object = MibTableColumn
prtSonetIntervalStatus = _PrtSonetIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 12),
    _PrtSonetIntervalStatus_Type()
)
prtSonetIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalStatus.setStatus("current")
_PrtSonetIntervalLSV_Type = Gauge32
_PrtSonetIntervalLSV_Object = MibTableColumn
prtSonetIntervalLSV = _PrtSonetIntervalLSV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 13),
    _PrtSonetIntervalLSV_Type()
)
prtSonetIntervalLSV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLSV.setStatus("current")
_PrtSonetPathCurrentTable_Object = MibTable
prtSonetPathCurrentTable = _PrtSonetPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    prtSonetPathCurrentTable.setStatus("current")
_PrtPathCurrentEntry_Object = MibTableRow
prtPathCurrentEntry = _PrtPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1)
)
prtPathCurrentEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtPathCurrentEntry.setStatus("current")
_PrtSonetCurrentPathAIS_Type = Gauge32
_PrtSonetCurrentPathAIS_Object = MibTableColumn
prtSonetCurrentPathAIS = _PrtSonetCurrentPathAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 1),
    _PrtSonetCurrentPathAIS_Type()
)
prtSonetCurrentPathAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentPathAIS.setStatus("current")
_PrtSonetCurrentPathFERF_Type = Gauge32
_PrtSonetCurrentPathFERF_Object = MibTableColumn
prtSonetCurrentPathFERF = _PrtSonetCurrentPathFERF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 2),
    _PrtSonetCurrentPathFERF_Type()
)
prtSonetCurrentPathFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentPathFERF.setStatus("current")
_PrtSonetCurrentLOP_Type = Gauge32
_PrtSonetCurrentLOP_Object = MibTableColumn
prtSonetCurrentLOP = _PrtSonetCurrentLOP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 3),
    _PrtSonetCurrentLOP_Type()
)
prtSonetCurrentLOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLOP.setStatus("current")
_PrtSonetCurrentSLM_Type = Gauge32
_PrtSonetCurrentSLM_Object = MibTableColumn
prtSonetCurrentSLM = _PrtSonetCurrentSLM_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 4),
    _PrtSonetCurrentSLM_Type()
)
prtSonetCurrentSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentSLM.setStatus("current")
_PrtSonetCurrentLOC_Type = Gauge32
_PrtSonetCurrentLOC_Object = MibTableColumn
prtSonetCurrentLOC = _PrtSonetCurrentLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 5),
    _PrtSonetCurrentLOC_Type()
)
prtSonetCurrentLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLOC.setStatus("current")
_PrtSonetCurrentPathBIP_Type = Gauge32
_PrtSonetCurrentPathBIP_Object = MibTableColumn
prtSonetCurrentPathBIP = _PrtSonetCurrentPathBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 6),
    _PrtSonetCurrentPathBIP_Type()
)
prtSonetCurrentPathBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentPathBIP.setStatus("current")
_PrtSonetCurrentPathFEBE_Type = Gauge32
_PrtSonetCurrentPathFEBE_Object = MibTableColumn
prtSonetCurrentPathFEBE = _PrtSonetCurrentPathFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 7),
    _PrtSonetCurrentPathFEBE_Type()
)
prtSonetCurrentPathFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentPathFEBE.setStatus("current")
_PrtSonetPathIntervalTable_Object = MibTable
prtSonetPathIntervalTable = _PrtSonetPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    prtSonetPathIntervalTable.setStatus("current")
_PrtPathIntervalEntry_Object = MibTableRow
prtPathIntervalEntry = _PrtPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1)
)
prtPathIntervalEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
    (0, "RAD-SONET-MIB", "prtSonetPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    prtPathIntervalEntry.setStatus("current")


class _PrtSonetPathIntervalNumber_Type(Integer32):
    """Custom type prtSonetPathIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PrtSonetPathIntervalNumber_Type.__name__ = "Integer32"
_PrtSonetPathIntervalNumber_Object = MibTableColumn
prtSonetPathIntervalNumber = _PrtSonetPathIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 1),
    _PrtSonetPathIntervalNumber_Type()
)
prtSonetPathIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetPathIntervalNumber.setStatus("current")
_PrtSonetIntervalPathAIS_Type = Gauge32
_PrtSonetIntervalPathAIS_Object = MibTableColumn
prtSonetIntervalPathAIS = _PrtSonetIntervalPathAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 2),
    _PrtSonetIntervalPathAIS_Type()
)
prtSonetIntervalPathAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalPathAIS.setStatus("current")
_PrtSonetIntervalPathFERF_Type = Gauge32
_PrtSonetIntervalPathFERF_Object = MibTableColumn
prtSonetIntervalPathFERF = _PrtSonetIntervalPathFERF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 3),
    _PrtSonetIntervalPathFERF_Type()
)
prtSonetIntervalPathFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalPathFERF.setStatus("current")
_PrtSonetIntervalLOP_Type = Gauge32
_PrtSonetIntervalLOP_Object = MibTableColumn
prtSonetIntervalLOP = _PrtSonetIntervalLOP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 4),
    _PrtSonetIntervalLOP_Type()
)
prtSonetIntervalLOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLOP.setStatus("current")
_PrtSonetIntervalSLM_Type = Gauge32
_PrtSonetIntervalSLM_Object = MibTableColumn
prtSonetIntervalSLM = _PrtSonetIntervalSLM_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 5),
    _PrtSonetIntervalSLM_Type()
)
prtSonetIntervalSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalSLM.setStatus("current")
_PrtSonetIntervalLOC_Type = Gauge32
_PrtSonetIntervalLOC_Object = MibTableColumn
prtSonetIntervalLOC = _PrtSonetIntervalLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 6),
    _PrtSonetIntervalLOC_Type()
)
prtSonetIntervalLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLOC.setStatus("current")
_PrtSonetIntervalPathBIP_Type = Gauge32
_PrtSonetIntervalPathBIP_Object = MibTableColumn
prtSonetIntervalPathBIP = _PrtSonetIntervalPathBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 7),
    _PrtSonetIntervalPathBIP_Type()
)
prtSonetIntervalPathBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalPathBIP.setStatus("current")
_PrtSonetIntervalPathFEBE_Type = Gauge32
_PrtSonetIntervalPathFEBE_Object = MibTableColumn
prtSonetIntervalPathFEBE = _PrtSonetIntervalPathFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 8),
    _PrtSonetIntervalPathFEBE_Type()
)
prtSonetIntervalPathFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalPathFEBE.setStatus("current")
_VirtualIfStatistics_ObjectIdentity = ObjectIdentity
virtualIfStatistics = _VirtualIfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6)
)
_VirtualIfCurrentTable_Object = MibTable
virtualIfCurrentTable = _VirtualIfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    virtualIfCurrentTable.setStatus("current")
_VirtualIfCurrentEntry_Object = MibTableRow
virtualIfCurrentEntry = _VirtualIfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1)
)
virtualIfCurrentEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    virtualIfCurrentEntry.setStatus("current")


class _VirtualIfCurrentMinActiveVC_Type(Integer32):
    """Custom type virtualIfCurrentMinActiveVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_VirtualIfCurrentMinActiveVC_Type.__name__ = "Integer32"
_VirtualIfCurrentMinActiveVC_Object = MibTableColumn
virtualIfCurrentMinActiveVC = _VirtualIfCurrentMinActiveVC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 1),
    _VirtualIfCurrentMinActiveVC_Type()
)
virtualIfCurrentMinActiveVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentMinActiveVC.setStatus("current")


class _VirtualIfCurrentMaxActiveVC_Type(Integer32):
    """Custom type virtualIfCurrentMaxActiveVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_VirtualIfCurrentMaxActiveVC_Type.__name__ = "Integer32"
_VirtualIfCurrentMaxActiveVC_Object = MibTableColumn
virtualIfCurrentMaxActiveVC = _VirtualIfCurrentMaxActiveVC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 2),
    _VirtualIfCurrentMaxActiveVC_Type()
)
virtualIfCurrentMaxActiveVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentMaxActiveVC.setStatus("current")
_VirtualIfCurrentRxFrames_Type = Counter64
_VirtualIfCurrentRxFrames_Object = MibTableColumn
virtualIfCurrentRxFrames = _VirtualIfCurrentRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 3),
    _VirtualIfCurrentRxFrames_Type()
)
virtualIfCurrentRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentRxFrames.setStatus("current")
_VirtualIfCurrentTxFrames_Type = Counter64
_VirtualIfCurrentTxFrames_Object = MibTableColumn
virtualIfCurrentTxFrames = _VirtualIfCurrentTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 4),
    _VirtualIfCurrentTxFrames_Type()
)
virtualIfCurrentTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentTxFrames.setStatus("current")
_VirtualIfCurrentRxAbortFrames_Type = PerfCurrentCount
_VirtualIfCurrentRxAbortFrames_Object = MibTableColumn
virtualIfCurrentRxAbortFrames = _VirtualIfCurrentRxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 5),
    _VirtualIfCurrentRxAbortFrames_Type()
)
virtualIfCurrentRxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentRxAbortFrames.setStatus("current")
_VirtualIfCurrentTxAbortFrames_Type = PerfCurrentCount
_VirtualIfCurrentTxAbortFrames_Object = MibTableColumn
virtualIfCurrentTxAbortFrames = _VirtualIfCurrentTxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 6),
    _VirtualIfCurrentTxAbortFrames_Type()
)
virtualIfCurrentTxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentTxAbortFrames.setStatus("current")
_VirtualIfCurrentMinLengthViolation_Type = PerfCurrentCount
_VirtualIfCurrentMinLengthViolation_Object = MibTableColumn
virtualIfCurrentMinLengthViolation = _VirtualIfCurrentMinLengthViolation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 7),
    _VirtualIfCurrentMinLengthViolation_Type()
)
virtualIfCurrentMinLengthViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentMinLengthViolation.setStatus("current")
_VirtualIfCurrentMaxLengthViolation_Type = PerfCurrentCount
_VirtualIfCurrentMaxLengthViolation_Object = MibTableColumn
virtualIfCurrentMaxLengthViolation = _VirtualIfCurrentMaxLengthViolation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 8),
    _VirtualIfCurrentMaxLengthViolation_Type()
)
virtualIfCurrentMaxLengthViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentMaxLengthViolation.setStatus("current")
_VirtualIfCurrentFcsError_Type = PerfCurrentCount
_VirtualIfCurrentFcsError_Object = MibTableColumn
virtualIfCurrentFcsError = _VirtualIfCurrentFcsError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 9),
    _VirtualIfCurrentFcsError_Type()
)
virtualIfCurrentFcsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentFcsError.setStatus("current")
_VirtualIfCurrentByteDestuffingViolation_Type = PerfCurrentCount
_VirtualIfCurrentByteDestuffingViolation_Object = MibTableColumn
virtualIfCurrentByteDestuffingViolation = _VirtualIfCurrentByteDestuffingViolation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 10),
    _VirtualIfCurrentByteDestuffingViolation_Type()
)
virtualIfCurrentByteDestuffingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentByteDestuffingViolation.setStatus("current")
_VirtualIfCurrentAdressMismatch_Type = PerfCurrentCount
_VirtualIfCurrentAdressMismatch_Object = MibTableColumn
virtualIfCurrentAdressMismatch = _VirtualIfCurrentAdressMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 11),
    _VirtualIfCurrentAdressMismatch_Type()
)
virtualIfCurrentAdressMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentAdressMismatch.setStatus("current")
_VirtualIfCurrentControlMismatch_Type = PerfCurrentCount
_VirtualIfCurrentControlMismatch_Object = MibTableColumn
virtualIfCurrentControlMismatch = _VirtualIfCurrentControlMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 12),
    _VirtualIfCurrentControlMismatch_Type()
)
virtualIfCurrentControlMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentControlMismatch.setStatus("current")


class _VirtualIfCurrentActiveVC_Type(Integer32):
    """Custom type virtualIfCurrentActiveVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_VirtualIfCurrentActiveVC_Type.__name__ = "Integer32"
_VirtualIfCurrentActiveVC_Object = MibTableColumn
virtualIfCurrentActiveVC = _VirtualIfCurrentActiveVC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 1, 1, 13),
    _VirtualIfCurrentActiveVC_Type()
)
virtualIfCurrentActiveVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfCurrentActiveVC.setStatus("current")
_VirtualIfIntervalTable_Object = MibTable
virtualIfIntervalTable = _VirtualIfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    virtualIfIntervalTable.setStatus("current")
_VirtualIfIntervalEntry_Object = MibTableRow
virtualIfIntervalEntry = _VirtualIfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1)
)
virtualIfIntervalEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
    (0, "RAD-SONET-MIB", "virtualIfIntervalNumber"),
)
if mibBuilder.loadTexts:
    virtualIfIntervalEntry.setStatus("current")


class _VirtualIfIntervalNumber_Type(Integer32):
    """Custom type virtualIfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_VirtualIfIntervalNumber_Type.__name__ = "Integer32"
_VirtualIfIntervalNumber_Object = MibTableColumn
virtualIfIntervalNumber = _VirtualIfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 1),
    _VirtualIfIntervalNumber_Type()
)
virtualIfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualIfIntervalNumber.setStatus("current")


class _VirtualIfIntervalMinActiveVC_Type(Integer32):
    """Custom type virtualIfIntervalMinActiveVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_VirtualIfIntervalMinActiveVC_Type.__name__ = "Integer32"
_VirtualIfIntervalMinActiveVC_Object = MibTableColumn
virtualIfIntervalMinActiveVC = _VirtualIfIntervalMinActiveVC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 2),
    _VirtualIfIntervalMinActiveVC_Type()
)
virtualIfIntervalMinActiveVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalMinActiveVC.setStatus("current")


class _VirtualIfIntervalMaxActiveVC_Type(Integer32):
    """Custom type virtualIfIntervalMaxActiveVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_VirtualIfIntervalMaxActiveVC_Type.__name__ = "Integer32"
_VirtualIfIntervalMaxActiveVC_Object = MibTableColumn
virtualIfIntervalMaxActiveVC = _VirtualIfIntervalMaxActiveVC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 3),
    _VirtualIfIntervalMaxActiveVC_Type()
)
virtualIfIntervalMaxActiveVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalMaxActiveVC.setStatus("current")
_VirtualIfIntervalRxFrames_Type = Counter64
_VirtualIfIntervalRxFrames_Object = MibTableColumn
virtualIfIntervalRxFrames = _VirtualIfIntervalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 4),
    _VirtualIfIntervalRxFrames_Type()
)
virtualIfIntervalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalRxFrames.setStatus("current")
_VirtualIfIntervalTxFrames_Type = Counter64
_VirtualIfIntervalTxFrames_Object = MibTableColumn
virtualIfIntervalTxFrames = _VirtualIfIntervalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 5),
    _VirtualIfIntervalTxFrames_Type()
)
virtualIfIntervalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalTxFrames.setStatus("current")
_VirtualIfIntervalRxAbortFrames_Type = PerfIntervalCount
_VirtualIfIntervalRxAbortFrames_Object = MibTableColumn
virtualIfIntervalRxAbortFrames = _VirtualIfIntervalRxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 6),
    _VirtualIfIntervalRxAbortFrames_Type()
)
virtualIfIntervalRxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalRxAbortFrames.setStatus("current")
_VirtualIfIntervalTxAbortFrames_Type = PerfIntervalCount
_VirtualIfIntervalTxAbortFrames_Object = MibTableColumn
virtualIfIntervalTxAbortFrames = _VirtualIfIntervalTxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 7),
    _VirtualIfIntervalTxAbortFrames_Type()
)
virtualIfIntervalTxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalTxAbortFrames.setStatus("current")
_VirtualIfIntervalMinLengthViolation_Type = PerfIntervalCount
_VirtualIfIntervalMinLengthViolation_Object = MibTableColumn
virtualIfIntervalMinLengthViolation = _VirtualIfIntervalMinLengthViolation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 8),
    _VirtualIfIntervalMinLengthViolation_Type()
)
virtualIfIntervalMinLengthViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalMinLengthViolation.setStatus("current")
_VirtualIfIntervalMaxLengthViolation_Type = PerfIntervalCount
_VirtualIfIntervalMaxLengthViolation_Object = MibTableColumn
virtualIfIntervalMaxLengthViolation = _VirtualIfIntervalMaxLengthViolation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 9),
    _VirtualIfIntervalMaxLengthViolation_Type()
)
virtualIfIntervalMaxLengthViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalMaxLengthViolation.setStatus("current")
_VirtualIfIntervalFcsError_Type = PerfIntervalCount
_VirtualIfIntervalFcsError_Object = MibTableColumn
virtualIfIntervalFcsError = _VirtualIfIntervalFcsError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 10),
    _VirtualIfIntervalFcsError_Type()
)
virtualIfIntervalFcsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalFcsError.setStatus("current")
_VirtualIfIntervalByteDestuffingViolation_Type = PerfIntervalCount
_VirtualIfIntervalByteDestuffingViolation_Object = MibTableColumn
virtualIfIntervalByteDestuffingViolation = _VirtualIfIntervalByteDestuffingViolation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 11),
    _VirtualIfIntervalByteDestuffingViolation_Type()
)
virtualIfIntervalByteDestuffingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalByteDestuffingViolation.setStatus("current")
_VirtualIfIntervalAdressMismatch_Type = PerfIntervalCount
_VirtualIfIntervalAdressMismatch_Object = MibTableColumn
virtualIfIntervalAdressMismatch = _VirtualIfIntervalAdressMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 12),
    _VirtualIfIntervalAdressMismatch_Type()
)
virtualIfIntervalAdressMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalAdressMismatch.setStatus("current")
_VirtualIfIntervalControlMismatch_Type = PerfIntervalCount
_VirtualIfIntervalControlMismatch_Object = MibTableColumn
virtualIfIntervalControlMismatch = _VirtualIfIntervalControlMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 13),
    _VirtualIfIntervalControlMismatch_Type()
)
virtualIfIntervalControlMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalControlMismatch.setStatus("current")
_VirtualIfIntervalBelowMinThreshold_Type = PerfIntervalCount
_VirtualIfIntervalBelowMinThreshold_Object = MibTableColumn
virtualIfIntervalBelowMinThreshold = _VirtualIfIntervalBelowMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 2, 1, 14),
    _VirtualIfIntervalBelowMinThreshold_Type()
)
virtualIfIntervalBelowMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfIntervalBelowMinThreshold.setStatus("current")
_VirtualIfLAPSCurrentTable_Object = MibTable
virtualIfLAPSCurrentTable = _VirtualIfLAPSCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    virtualIfLAPSCurrentTable.setStatus("current")
_VirtualIfLAPSCurrentEntry_Object = MibTableRow
virtualIfLAPSCurrentEntry = _VirtualIfLAPSCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 3, 1)
)
virtualIfLAPSCurrentEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    virtualIfLAPSCurrentEntry.setStatus("current")
_VirtualIfLAPSCurrentSapiMismatch_Type = PerfCurrentCount
_VirtualIfLAPSCurrentSapiMismatch_Object = MibTableColumn
virtualIfLAPSCurrentSapiMismatch = _VirtualIfLAPSCurrentSapiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 3, 1, 1),
    _VirtualIfLAPSCurrentSapiMismatch_Type()
)
virtualIfLAPSCurrentSapiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPSCurrentSapiMismatch.setStatus("current")
_VirtualIfLAPSIntervalTable_Object = MibTable
virtualIfLAPSIntervalTable = _VirtualIfLAPSIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 4)
)
if mibBuilder.loadTexts:
    virtualIfLAPSIntervalTable.setStatus("current")
_VirtualIfLAPSIntervalEntry_Object = MibTableRow
virtualIfLAPSIntervalEntry = _VirtualIfLAPSIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 4, 1)
)
virtualIfLAPSIntervalEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
    (0, "RAD-SONET-MIB", "virtualIfIntervalNumber"),
)
if mibBuilder.loadTexts:
    virtualIfLAPSIntervalEntry.setStatus("current")
_VirtualIfLAPSIntervalSapiMismatch_Type = PerfIntervalCount
_VirtualIfLAPSIntervalSapiMismatch_Object = MibTableColumn
virtualIfLAPSIntervalSapiMismatch = _VirtualIfLAPSIntervalSapiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 4, 1, 1),
    _VirtualIfLAPSIntervalSapiMismatch_Type()
)
virtualIfLAPSIntervalSapiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPSIntervalSapiMismatch.setStatus("current")
_VirtualIfLAPFCurrentTable_Object = MibTable
virtualIfLAPFCurrentTable = _VirtualIfLAPFCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 5)
)
if mibBuilder.loadTexts:
    virtualIfLAPFCurrentTable.setStatus("current")
_VirtualIfLAPFCurrentEntry_Object = MibTableRow
virtualIfLAPFCurrentEntry = _VirtualIfLAPFCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 5, 1)
)
virtualIfLAPFCurrentEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    virtualIfLAPFCurrentEntry.setStatus("current")
_VirtualIfLAPFCurrentNlpidMismatch_Type = PerfCurrentCount
_VirtualIfLAPFCurrentNlpidMismatch_Object = MibTableColumn
virtualIfLAPFCurrentNlpidMismatch = _VirtualIfLAPFCurrentNlpidMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 5, 1, 1),
    _VirtualIfLAPFCurrentNlpidMismatch_Type()
)
virtualIfLAPFCurrentNlpidMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFCurrentNlpidMismatch.setStatus("current")
_VirtualIfLAPFCurrentOuiMismatch_Type = PerfCurrentCount
_VirtualIfLAPFCurrentOuiMismatch_Object = MibTableColumn
virtualIfLAPFCurrentOuiMismatch = _VirtualIfLAPFCurrentOuiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 5, 1, 2),
    _VirtualIfLAPFCurrentOuiMismatch_Type()
)
virtualIfLAPFCurrentOuiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFCurrentOuiMismatch.setStatus("current")
_VirtualIfLAPFCurrentPidMismatch_Type = PerfCurrentCount
_VirtualIfLAPFCurrentPidMismatch_Object = MibTableColumn
virtualIfLAPFCurrentPidMismatch = _VirtualIfLAPFCurrentPidMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 5, 1, 3),
    _VirtualIfLAPFCurrentPidMismatch_Type()
)
virtualIfLAPFCurrentPidMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFCurrentPidMismatch.setStatus("current")
_VirtualIfLAPFCurrentDlciMismatch_Type = PerfCurrentCount
_VirtualIfLAPFCurrentDlciMismatch_Object = MibTableColumn
virtualIfLAPFCurrentDlciMismatch = _VirtualIfLAPFCurrentDlciMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 5, 1, 4),
    _VirtualIfLAPFCurrentDlciMismatch_Type()
)
virtualIfLAPFCurrentDlciMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFCurrentDlciMismatch.setStatus("current")
_VirtualIfLAPFCurrentMacRxFrames_Type = PerfCurrentCount
_VirtualIfLAPFCurrentMacRxFrames_Object = MibTableColumn
virtualIfLAPFCurrentMacRxFrames = _VirtualIfLAPFCurrentMacRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 5, 1, 5),
    _VirtualIfLAPFCurrentMacRxFrames_Type()
)
virtualIfLAPFCurrentMacRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFCurrentMacRxFrames.setStatus("current")
_VirtualIfLAPFCurrentMacTxFrames_Type = PerfCurrentCount
_VirtualIfLAPFCurrentMacTxFrames_Object = MibTableColumn
virtualIfLAPFCurrentMacTxFrames = _VirtualIfLAPFCurrentMacTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 5, 1, 6),
    _VirtualIfLAPFCurrentMacTxFrames_Type()
)
virtualIfLAPFCurrentMacTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFCurrentMacTxFrames.setStatus("current")
_VirtualIfLAPFIntervalTable_Object = MibTable
virtualIfLAPFIntervalTable = _VirtualIfLAPFIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 6)
)
if mibBuilder.loadTexts:
    virtualIfLAPFIntervalTable.setStatus("current")
_VirtualIfLAPFIntervalEntry_Object = MibTableRow
virtualIfLAPFIntervalEntry = _VirtualIfLAPFIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 6, 1)
)
virtualIfLAPFIntervalEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
    (0, "RAD-SONET-MIB", "virtualIfIntervalNumber"),
)
if mibBuilder.loadTexts:
    virtualIfLAPFIntervalEntry.setStatus("current")
_VirtualIfLAPFIntervalNlpidMismatch_Type = PerfIntervalCount
_VirtualIfLAPFIntervalNlpidMismatch_Object = MibTableColumn
virtualIfLAPFIntervalNlpidMismatch = _VirtualIfLAPFIntervalNlpidMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 6, 1, 1),
    _VirtualIfLAPFIntervalNlpidMismatch_Type()
)
virtualIfLAPFIntervalNlpidMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFIntervalNlpidMismatch.setStatus("current")
_VirtualIfLAPFIntervalOuiMismatch_Type = PerfIntervalCount
_VirtualIfLAPFIntervalOuiMismatch_Object = MibTableColumn
virtualIfLAPFIntervalOuiMismatch = _VirtualIfLAPFIntervalOuiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 6, 1, 2),
    _VirtualIfLAPFIntervalOuiMismatch_Type()
)
virtualIfLAPFIntervalOuiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFIntervalOuiMismatch.setStatus("current")
_VirtualIfLAPFIntervalPidMismatch_Type = PerfIntervalCount
_VirtualIfLAPFIntervalPidMismatch_Object = MibTableColumn
virtualIfLAPFIntervalPidMismatch = _VirtualIfLAPFIntervalPidMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 6, 1, 3),
    _VirtualIfLAPFIntervalPidMismatch_Type()
)
virtualIfLAPFIntervalPidMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFIntervalPidMismatch.setStatus("current")
_VirtualIfLAPFIntervalDlciMismatch_Type = PerfIntervalCount
_VirtualIfLAPFIntervalDlciMismatch_Object = MibTableColumn
virtualIfLAPFIntervalDlciMismatch = _VirtualIfLAPFIntervalDlciMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 6, 1, 4),
    _VirtualIfLAPFIntervalDlciMismatch_Type()
)
virtualIfLAPFIntervalDlciMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFIntervalDlciMismatch.setStatus("current")
_VirtualIfLAPFIntervalMacRxFrames_Type = PerfIntervalCount
_VirtualIfLAPFIntervalMacRxFrames_Object = MibTableColumn
virtualIfLAPFIntervalMacRxFrames = _VirtualIfLAPFIntervalMacRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 6, 1, 5),
    _VirtualIfLAPFIntervalMacRxFrames_Type()
)
virtualIfLAPFIntervalMacRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFIntervalMacRxFrames.setStatus("current")
_VirtualIfLAPFIntervalMacTxFrames_Type = PerfIntervalCount
_VirtualIfLAPFIntervalMacTxFrames_Object = MibTableColumn
virtualIfLAPFIntervalMacTxFrames = _VirtualIfLAPFIntervalMacTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 6, 1, 6),
    _VirtualIfLAPFIntervalMacTxFrames_Type()
)
virtualIfLAPFIntervalMacTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfLAPFIntervalMacTxFrames.setStatus("current")
_VirtualIfGFPCurrentTable_Object = MibTable
virtualIfGFPCurrentTable = _VirtualIfGFPCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7)
)
if mibBuilder.loadTexts:
    virtualIfGFPCurrentTable.setStatus("current")
_VirtualIfGFPCurrentEntry_Object = MibTableRow
virtualIfGFPCurrentEntry = _VirtualIfGFPCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1)
)
virtualIfGFPCurrentEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    virtualIfGFPCurrentEntry.setStatus("current")
_VirtualIfGFPCurrentIdleFrameError_Type = PerfCurrentCount
_VirtualIfGFPCurrentIdleFrameError_Object = MibTableColumn
virtualIfGFPCurrentIdleFrameError = _VirtualIfGFPCurrentIdleFrameError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1, 1),
    _VirtualIfGFPCurrentIdleFrameError_Type()
)
virtualIfGFPCurrentIdleFrameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPCurrentIdleFrameError.setStatus("current")
_VirtualIfGFPCurrentCHecSbError_Type = PerfCurrentCount
_VirtualIfGFPCurrentCHecSbError_Object = MibTableColumn
virtualIfGFPCurrentCHecSbError = _VirtualIfGFPCurrentCHecSbError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1, 2),
    _VirtualIfGFPCurrentCHecSbError_Type()
)
virtualIfGFPCurrentCHecSbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPCurrentCHecSbError.setStatus("current")
_VirtualIfGFPCurrentPtiMismatch_Type = PerfCurrentCount
_VirtualIfGFPCurrentPtiMismatch_Object = MibTableColumn
virtualIfGFPCurrentPtiMismatch = _VirtualIfGFPCurrentPtiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1, 3),
    _VirtualIfGFPCurrentPtiMismatch_Type()
)
virtualIfGFPCurrentPtiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPCurrentPtiMismatch.setStatus("current")
_VirtualIfGFPCurrentExiMismatch_Type = PerfCurrentCount
_VirtualIfGFPCurrentExiMismatch_Object = MibTableColumn
virtualIfGFPCurrentExiMismatch = _VirtualIfGFPCurrentExiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1, 4),
    _VirtualIfGFPCurrentExiMismatch_Type()
)
virtualIfGFPCurrentExiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPCurrentExiMismatch.setStatus("current")
_VirtualIfGFPCurrentUpiMismatch_Type = PerfCurrentCount
_VirtualIfGFPCurrentUpiMismatch_Object = MibTableColumn
virtualIfGFPCurrentUpiMismatch = _VirtualIfGFPCurrentUpiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1, 5),
    _VirtualIfGFPCurrentUpiMismatch_Type()
)
virtualIfGFPCurrentUpiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPCurrentUpiMismatch.setStatus("current")
_VirtualIfGFPCurrentTHecSbError_Type = PerfCurrentCount
_VirtualIfGFPCurrentTHecSbError_Object = MibTableColumn
virtualIfGFPCurrentTHecSbError = _VirtualIfGFPCurrentTHecSbError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1, 6),
    _VirtualIfGFPCurrentTHecSbError_Type()
)
virtualIfGFPCurrentTHecSbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPCurrentTHecSbError.setStatus("current")
_VirtualIfGFPCurrentTHecMbError_Type = PerfCurrentCount
_VirtualIfGFPCurrentTHecMbError_Object = MibTableColumn
virtualIfGFPCurrentTHecMbError = _VirtualIfGFPCurrentTHecMbError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1, 7),
    _VirtualIfGFPCurrentTHecMbError_Type()
)
virtualIfGFPCurrentTHecMbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPCurrentTHecMbError.setStatus("current")
_VirtualIfGFPCurrentCidMismatch_Type = PerfCurrentCount
_VirtualIfGFPCurrentCidMismatch_Object = MibTableColumn
virtualIfGFPCurrentCidMismatch = _VirtualIfGFPCurrentCidMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1, 8),
    _VirtualIfGFPCurrentCidMismatch_Type()
)
virtualIfGFPCurrentCidMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPCurrentCidMismatch.setStatus("current")
_VirtualIfGFPCurrentEHecSbError_Type = PerfCurrentCount
_VirtualIfGFPCurrentEHecSbError_Object = MibTableColumn
virtualIfGFPCurrentEHecSbError = _VirtualIfGFPCurrentEHecSbError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1, 9),
    _VirtualIfGFPCurrentEHecSbError_Type()
)
virtualIfGFPCurrentEHecSbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPCurrentEHecSbError.setStatus("current")
_VirtualIfGFPCurrentEHecMbError_Type = PerfCurrentCount
_VirtualIfGFPCurrentEHecMbError_Object = MibTableColumn
virtualIfGFPCurrentEHecMbError = _VirtualIfGFPCurrentEHecMbError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 7, 1, 10),
    _VirtualIfGFPCurrentEHecMbError_Type()
)
virtualIfGFPCurrentEHecMbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPCurrentEHecMbError.setStatus("current")
_VirtualIfGFPIntervalTable_Object = MibTable
virtualIfGFPIntervalTable = _VirtualIfGFPIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8)
)
if mibBuilder.loadTexts:
    virtualIfGFPIntervalTable.setStatus("current")
_VirtualIfGFPIntervalEntry_Object = MibTableRow
virtualIfGFPIntervalEntry = _VirtualIfGFPIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1)
)
virtualIfGFPIntervalEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "ifIndex"),
    (0, "RAD-SONET-MIB", "virtualIfIntervalNumber"),
)
if mibBuilder.loadTexts:
    virtualIfGFPIntervalEntry.setStatus("current")
_VirtualIfGFPIntervalIdleFrameError_Type = PerfIntervalCount
_VirtualIfGFPIntervalIdleFrameError_Object = MibTableColumn
virtualIfGFPIntervalIdleFrameError = _VirtualIfGFPIntervalIdleFrameError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1, 1),
    _VirtualIfGFPIntervalIdleFrameError_Type()
)
virtualIfGFPIntervalIdleFrameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPIntervalIdleFrameError.setStatus("current")
_VirtualIfGFPIntervalCHecSbError_Type = PerfIntervalCount
_VirtualIfGFPIntervalCHecSbError_Object = MibTableColumn
virtualIfGFPIntervalCHecSbError = _VirtualIfGFPIntervalCHecSbError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1, 2),
    _VirtualIfGFPIntervalCHecSbError_Type()
)
virtualIfGFPIntervalCHecSbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPIntervalCHecSbError.setStatus("current")
_VirtualIfGFPIntervalPtiMismatch_Type = PerfIntervalCount
_VirtualIfGFPIntervalPtiMismatch_Object = MibTableColumn
virtualIfGFPIntervalPtiMismatch = _VirtualIfGFPIntervalPtiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1, 3),
    _VirtualIfGFPIntervalPtiMismatch_Type()
)
virtualIfGFPIntervalPtiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPIntervalPtiMismatch.setStatus("current")
_VirtualIfGFPIntervalExiMismatch_Type = PerfIntervalCount
_VirtualIfGFPIntervalExiMismatch_Object = MibTableColumn
virtualIfGFPIntervalExiMismatch = _VirtualIfGFPIntervalExiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1, 4),
    _VirtualIfGFPIntervalExiMismatch_Type()
)
virtualIfGFPIntervalExiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPIntervalExiMismatch.setStatus("current")
_VirtualIfGFPIntervalUpiMismatch_Type = PerfIntervalCount
_VirtualIfGFPIntervalUpiMismatch_Object = MibTableColumn
virtualIfGFPIntervalUpiMismatch = _VirtualIfGFPIntervalUpiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1, 5),
    _VirtualIfGFPIntervalUpiMismatch_Type()
)
virtualIfGFPIntervalUpiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPIntervalUpiMismatch.setStatus("current")
_VirtualIfGFPIntervalTHecSbError_Type = PerfIntervalCount
_VirtualIfGFPIntervalTHecSbError_Object = MibTableColumn
virtualIfGFPIntervalTHecSbError = _VirtualIfGFPIntervalTHecSbError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1, 6),
    _VirtualIfGFPIntervalTHecSbError_Type()
)
virtualIfGFPIntervalTHecSbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPIntervalTHecSbError.setStatus("current")
_VirtualIfGFPIntervalTHecMbError_Type = PerfIntervalCount
_VirtualIfGFPIntervalTHecMbError_Object = MibTableColumn
virtualIfGFPIntervalTHecMbError = _VirtualIfGFPIntervalTHecMbError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1, 7),
    _VirtualIfGFPIntervalTHecMbError_Type()
)
virtualIfGFPIntervalTHecMbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPIntervalTHecMbError.setStatus("current")
_VirtualIfGFPIntervalCidMismatch_Type = PerfIntervalCount
_VirtualIfGFPIntervalCidMismatch_Object = MibTableColumn
virtualIfGFPIntervalCidMismatch = _VirtualIfGFPIntervalCidMismatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1, 8),
    _VirtualIfGFPIntervalCidMismatch_Type()
)
virtualIfGFPIntervalCidMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPIntervalCidMismatch.setStatus("current")
_VirtualIfGFPIntervalEHecSbError_Type = PerfIntervalCount
_VirtualIfGFPIntervalEHecSbError_Object = MibTableColumn
virtualIfGFPIntervalEHecSbError = _VirtualIfGFPIntervalEHecSbError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1, 9),
    _VirtualIfGFPIntervalEHecSbError_Type()
)
virtualIfGFPIntervalEHecSbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPIntervalEHecSbError.setStatus("current")
_VirtualIfGFPIntervalEHecMbError_Type = PerfIntervalCount
_VirtualIfGFPIntervalEHecMbError_Object = MibTableColumn
virtualIfGFPIntervalEHecMbError = _VirtualIfGFPIntervalEHecMbError_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 6, 8, 1, 10),
    _VirtualIfGFPIntervalEHecMbError_Type()
)
virtualIfGFPIntervalEHecMbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGFPIntervalEHecMbError.setStatus("current")
_PrtSonetConfig_ObjectIdentity = ObjectIdentity
prtSonetConfig = _PrtSonetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2)
)
_PrtSonetGen_ObjectIdentity = ObjectIdentity
prtSonetGen = _PrtSonetGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1)
)
_PrtSonetGenTable_Object = MibTable
prtSonetGenTable = _PrtSonetGenTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    prtSonetGenTable.setStatus("current")
_PrtSonetGenEntry_Object = MibTableRow
prtSonetGenEntry = _PrtSonetGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1)
)
prtSonetGenEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "prtSonetGenCnfgIdx"),
    (0, "RAD-SONET-MIB", "prtSonetGenIdx"),
)
if mibBuilder.loadTexts:
    prtSonetGenEntry.setStatus("current")


class _PrtSonetGenCnfgIdx_Type(Integer32):
    """Custom type prtSonetGenCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSonetGenCnfgIdx_Type.__name__ = "Integer32"
_PrtSonetGenCnfgIdx_Object = MibTableColumn
prtSonetGenCnfgIdx = _PrtSonetGenCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1, 1),
    _PrtSonetGenCnfgIdx_Type()
)
prtSonetGenCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetGenCnfgIdx.setStatus("current")
_PrtSonetGenIdx_Type = Integer32
_PrtSonetGenIdx_Object = MibTableColumn
prtSonetGenIdx = _PrtSonetGenIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1, 2),
    _PrtSonetGenIdx_Type()
)
prtSonetGenIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetGenIdx.setStatus("current")


class _PrtSonetGenSdThreshold_Type(Integer32):
    """Custom type prtSonetGenSdThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("notApplicable", 1))
    )


_PrtSonetGenSdThreshold_Type.__name__ = "Integer32"
_PrtSonetGenSdThreshold_Object = MibTableColumn
prtSonetGenSdThreshold = _PrtSonetGenSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1, 3),
    _PrtSonetGenSdThreshold_Type()
)
prtSonetGenSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetGenSdThreshold.setStatus("current")


class _PrtSonetGenEedThreshold_Type(Integer32):
    """Custom type prtSonetGenEedThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("notApplicable", 1))
    )


_PrtSonetGenEedThreshold_Type.__name__ = "Integer32"
_PrtSonetGenEedThreshold_Object = MibTableColumn
prtSonetGenEedThreshold = _PrtSonetGenEedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1, 4),
    _PrtSonetGenEedThreshold_Type()
)
prtSonetGenEedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetGenEedThreshold.setStatus("current")


class _PrtSonetGenBerEnable_Type(Integer32):
    """Custom type prtSonetGenBerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("notApplicable", 1))
    )


_PrtSonetGenBerEnable_Type.__name__ = "Integer32"
_PrtSonetGenBerEnable_Object = MibTableColumn
prtSonetGenBerEnable = _PrtSonetGenBerEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1, 5),
    _PrtSonetGenBerEnable_Type()
)
prtSonetGenBerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetGenBerEnable.setStatus("current")
_PrtSonetStm1_ObjectIdentity = ObjectIdentity
prtSonetStm1 = _PrtSonetStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2)
)
_PrtSonetStm1Table_Object = MibTable
prtSonetStm1Table = _PrtSonetStm1Table_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    prtSonetStm1Table.setStatus("current")
_PrtSonetStm1Entry_Object = MibTableRow
prtSonetStm1Entry = _PrtSonetStm1Entry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1)
)
prtSonetStm1Entry.setIndexNames(
    (0, "RAD-SONET-MIB", "prtSonetStm1CnfgIdx"),
    (0, "RAD-SONET-MIB", "prtSonetStm1Idx"),
)
if mibBuilder.loadTexts:
    prtSonetStm1Entry.setStatus("current")


class _PrtSonetStm1CnfgIdx_Type(Integer32):
    """Custom type prtSonetStm1CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSonetStm1CnfgIdx_Type.__name__ = "Integer32"
_PrtSonetStm1CnfgIdx_Object = MibTableColumn
prtSonetStm1CnfgIdx = _PrtSonetStm1CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 1),
    _PrtSonetStm1CnfgIdx_Type()
)
prtSonetStm1CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetStm1CnfgIdx.setStatus("current")
_PrtSonetStm1Idx_Type = Integer32
_PrtSonetStm1Idx_Object = MibTableColumn
prtSonetStm1Idx = _PrtSonetStm1Idx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 2),
    _PrtSonetStm1Idx_Type()
)
prtSonetStm1Idx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetStm1Idx.setStatus("current")


class _PrtSonetStm1ClockSrc_Type(Integer32):
    """Custom type prtSonetStm1ClockSrc based on Integer32"""
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
        *(("internal", 2),
          ("lbt", 3),
          ("notApplicable", 1),
          ("systemClk", 4))
    )


_PrtSonetStm1ClockSrc_Type.__name__ = "Integer32"
_PrtSonetStm1ClockSrc_Object = MibTableColumn
prtSonetStm1ClockSrc = _PrtSonetStm1ClockSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 3),
    _PrtSonetStm1ClockSrc_Type()
)
prtSonetStm1ClockSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1ClockSrc.setStatus("current")


class _PrtSonetStm1DccMode_Type(Integer32):
    """Custom type prtSonetStm1DccMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("d1", 5),
          ("d10", 14),
          ("d11", 15),
          ("d12", 16),
          ("d1ToD3", 3),
          ("d2", 6),
          ("d3", 7),
          ("d4", 8),
          ("d4ToD12", 4),
          ("d5", 9),
          ("d6", 10),
          ("d7", 11),
          ("d8", 12),
          ("d9", 13),
          ("none", 2),
          ("notApplicable", 1))
    )


_PrtSonetStm1DccMode_Type.__name__ = "Integer32"
_PrtSonetStm1DccMode_Object = MibTableColumn
prtSonetStm1DccMode = _PrtSonetStm1DccMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 4),
    _PrtSonetStm1DccMode_Type()
)
prtSonetStm1DccMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1DccMode.setStatus("current")


class _PrtSonetStm1RoutingProt_Type(Integer32):
    """Custom type prtSonetStm1RoutingProt based on Integer32"""
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
        *(("none", 2),
          ("notApplicable", 1),
          ("proprietary", 3),
          ("rip2", 4))
    )


_PrtSonetStm1RoutingProt_Type.__name__ = "Integer32"
_PrtSonetStm1RoutingProt_Object = MibTableColumn
prtSonetStm1RoutingProt = _PrtSonetStm1RoutingProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 5),
    _PrtSonetStm1RoutingProt_Type()
)
prtSonetStm1RoutingProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1RoutingProt.setStatus("current")


class _PrtSonetStm1MngProt_Type(Integer32):
    """Custom type prtSonetStm1MngProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 6),
          ("hdlc", 7),
          ("lapdOverHdlc", 8),
          ("notApplicable", 1),
          ("ppp", 5),
          ("proprietary", 3))
    )


_PrtSonetStm1MngProt_Type.__name__ = "Integer32"
_PrtSonetStm1MngProt_Object = MibTableColumn
prtSonetStm1MngProt = _PrtSonetStm1MngProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 6),
    _PrtSonetStm1MngProt_Type()
)
prtSonetStm1MngProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1MngProt.setStatus("current")


class _PrtSonetStm1OperationalMode_Type(Integer32):
    """Custom type prtSonetStm1OperationalMode based on Integer32"""
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
        *(("linear", 3),
          ("linearProtection", 4),
          ("notApplicable", 1),
          ("terminal", 2))
    )


_PrtSonetStm1OperationalMode_Type.__name__ = "Integer32"
_PrtSonetStm1OperationalMode_Object = MibTableColumn
prtSonetStm1OperationalMode = _PrtSonetStm1OperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 7),
    _PrtSonetStm1OperationalMode_Type()
)
prtSonetStm1OperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1OperationalMode.setStatus("current")


class _PrtSonetStm1VoiceChannel_Type(Integer32):
    """Custom type prtSonetStm1VoiceChannel based on Integer32"""
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
        *(("e1Byte", 3),
          ("e2Byte", 4),
          ("none", 2),
          ("notApplicable", 1))
    )


_PrtSonetStm1VoiceChannel_Type.__name__ = "Integer32"
_PrtSonetStm1VoiceChannel_Object = MibTableColumn
prtSonetStm1VoiceChannel = _PrtSonetStm1VoiceChannel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 8),
    _PrtSonetStm1VoiceChannel_Type()
)
prtSonetStm1VoiceChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1VoiceChannel.setStatus("current")
_PrtSonetStm1OutputRate_Type = Integer32
_PrtSonetStm1OutputRate_Object = MibTableColumn
prtSonetStm1OutputRate = _PrtSonetStm1OutputRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 9),
    _PrtSonetStm1OutputRate_Type()
)
prtSonetStm1OutputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1OutputRate.setStatus("current")


class _PrtSonetStm1S1ProtocolClock_Type(Integer32):
    """Custom type prtSonetStm1S1ProtocolClock based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("notApplicable", 1),
          ("transparent", 4))
    )


_PrtSonetStm1S1ProtocolClock_Type.__name__ = "Integer32"
_PrtSonetStm1S1ProtocolClock_Object = MibTableColumn
prtSonetStm1S1ProtocolClock = _PrtSonetStm1S1ProtocolClock_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 10),
    _PrtSonetStm1S1ProtocolClock_Type()
)
prtSonetStm1S1ProtocolClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1S1ProtocolClock.setStatus("current")
_PrtSonetStm1GatewayRingSubnetAddress_Type = IpAddress
_PrtSonetStm1GatewayRingSubnetAddress_Object = MibTableColumn
prtSonetStm1GatewayRingSubnetAddress = _PrtSonetStm1GatewayRingSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 11),
    _PrtSonetStm1GatewayRingSubnetAddress_Type()
)
prtSonetStm1GatewayRingSubnetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1GatewayRingSubnetAddress.setStatus("current")
_PrtSonetStm1GatewayRingSubnetMask_Type = IpAddress
_PrtSonetStm1GatewayRingSubnetMask_Object = MibTableColumn
prtSonetStm1GatewayRingSubnetMask = _PrtSonetStm1GatewayRingSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 12),
    _PrtSonetStm1GatewayRingSubnetMask_Type()
)
prtSonetStm1GatewayRingSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1GatewayRingSubnetMask.setStatus("current")


class _PrtSonetStm1MngProtDeviationType_Type(Integer32):
    """Custom type prtSonetStm1MngProtDeviationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("standard", 2),
          ("type1", 3))
    )


_PrtSonetStm1MngProtDeviationType_Type.__name__ = "Integer32"
_PrtSonetStm1MngProtDeviationType_Object = MibTableColumn
prtSonetStm1MngProtDeviationType = _PrtSonetStm1MngProtDeviationType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 13),
    _PrtSonetStm1MngProtDeviationType_Type()
)
prtSonetStm1MngProtDeviationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1MngProtDeviationType.setStatus("current")
_PrtSonetVc_ObjectIdentity = ObjectIdentity
prtSonetVc = _PrtSonetVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3)
)
_PrtSonetVcTable_Object = MibTable
prtSonetVcTable = _PrtSonetVcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    prtSonetVcTable.setStatus("current")
_PrtSonetVcEntry_Object = MibTableRow
prtSonetVcEntry = _PrtSonetVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1)
)
prtSonetVcEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "prtSonetVcCnfgIdx"),
    (0, "RAD-SONET-MIB", "prtSonetVcIdx"),
)
if mibBuilder.loadTexts:
    prtSonetVcEntry.setStatus("current")


class _PrtSonetVcCnfgIdx_Type(Integer32):
    """Custom type prtSonetVcCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSonetVcCnfgIdx_Type.__name__ = "Integer32"
_PrtSonetVcCnfgIdx_Object = MibTableColumn
prtSonetVcCnfgIdx = _PrtSonetVcCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 1),
    _PrtSonetVcCnfgIdx_Type()
)
prtSonetVcCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetVcCnfgIdx.setStatus("current")
_PrtSonetVcIdx_Type = Integer32
_PrtSonetVcIdx_Object = MibTableColumn
prtSonetVcIdx = _PrtSonetVcIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 2),
    _PrtSonetVcIdx_Type()
)
prtSonetVcIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetVcIdx.setStatus("current")


class _PrtSonetVcJTxPathTraceEnable_Type(Integer32):
    """Custom type prtSonetVcJTxPathTraceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("notApplicable", 1))
    )


_PrtSonetVcJTxPathTraceEnable_Type.__name__ = "Integer32"
_PrtSonetVcJTxPathTraceEnable_Object = MibTableColumn
prtSonetVcJTxPathTraceEnable = _PrtSonetVcJTxPathTraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 3),
    _PrtSonetVcJTxPathTraceEnable_Type()
)
prtSonetVcJTxPathTraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetVcJTxPathTraceEnable.setStatus("current")


class _PrtSonetVcJRxPathTraceEnable_Type(Integer32):
    """Custom type prtSonetVcJRxPathTraceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("notApplicable", 1))
    )


_PrtSonetVcJRxPathTraceEnable_Type.__name__ = "Integer32"
_PrtSonetVcJRxPathTraceEnable_Object = MibTableColumn
prtSonetVcJRxPathTraceEnable = _PrtSonetVcJRxPathTraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 4),
    _PrtSonetVcJRxPathTraceEnable_Type()
)
prtSonetVcJRxPathTraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetVcJRxPathTraceEnable.setStatus("current")


class _PrtSonetVcJPathTrace_Type(DisplayString):
    """Custom type prtSonetVcJPathTrace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_PrtSonetVcJPathTrace_Type.__name__ = "DisplayString"
_PrtSonetVcJPathTrace_Object = MibTableColumn
prtSonetVcJPathTrace = _PrtSonetVcJPathTrace_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 5),
    _PrtSonetVcJPathTrace_Type()
)
prtSonetVcJPathTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetVcJPathTrace.setStatus("current")


class _PrtSonetVcConnect_Type(Integer32):
    """Custom type prtSonetVcConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notApplicable", 1),
          ("yes", 3))
    )


_PrtSonetVcConnect_Type.__name__ = "Integer32"
_PrtSonetVcConnect_Object = MibTableColumn
prtSonetVcConnect = _PrtSonetVcConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 6),
    _PrtSonetVcConnect_Type()
)
prtSonetVcConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetVcConnect.setStatus("current")


class _PrtSonetVcSignalLabel_Type(OctetString):
    """Custom type prtSonetVcSignalLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PrtSonetVcSignalLabel_Type.__name__ = "OctetString"
_PrtSonetVcSignalLabel_Object = MibTableColumn
prtSonetVcSignalLabel = _PrtSonetVcSignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 7),
    _PrtSonetVcSignalLabel_Type()
)
prtSonetVcSignalLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetVcSignalLabel.setStatus("current")
_PrtSonetTuTable_Object = MibTable
prtSonetTuTable = _PrtSonetTuTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    prtSonetTuTable.setStatus("current")
_PrtSonetTuEntry_Object = MibTableRow
prtSonetTuEntry = _PrtSonetTuEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1)
)
prtSonetTuEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "prtSonetTuCnfgIdx"),
    (0, "RAD-SONET-MIB", "prtSonetTuPrtIdx"),
    (0, "RAD-SONET-MIB", "prtSonetTuIdx"),
    (0, "RAD-SONET-MIB", "prtSonetTuConPrtIdx"),
)
if mibBuilder.loadTexts:
    prtSonetTuEntry.setStatus("current")


class _PrtSonetTuCnfgIdx_Type(Integer32):
    """Custom type prtSonetTuCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSonetTuCnfgIdx_Type.__name__ = "Integer32"
_PrtSonetTuCnfgIdx_Object = MibTableColumn
prtSonetTuCnfgIdx = _PrtSonetTuCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 1),
    _PrtSonetTuCnfgIdx_Type()
)
prtSonetTuCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetTuCnfgIdx.setStatus("current")
_PrtSonetTuPrtIdx_Type = Integer32
_PrtSonetTuPrtIdx_Object = MibTableColumn
prtSonetTuPrtIdx = _PrtSonetTuPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 2),
    _PrtSonetTuPrtIdx_Type()
)
prtSonetTuPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetTuPrtIdx.setStatus("current")
_PrtSonetTuIdx_Type = Integer32
_PrtSonetTuIdx_Object = MibTableColumn
prtSonetTuIdx = _PrtSonetTuIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 3),
    _PrtSonetTuIdx_Type()
)
prtSonetTuIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetTuIdx.setStatus("current")
_PrtSonetTuConPrtIdx_Type = Integer32
_PrtSonetTuConPrtIdx_Object = MibTableColumn
prtSonetTuConPrtIdx = _PrtSonetTuConPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 4),
    _PrtSonetTuConPrtIdx_Type()
)
prtSonetTuConPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetTuConPrtIdx.setStatus("current")


class _PrtSonetTuType_Type(Integer32):
    """Custom type prtSonetTuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 3),
          ("connect", 2))
    )


_PrtSonetTuType_Type.__name__ = "Integer32"
_PrtSonetTuType_Object = MibTableColumn
prtSonetTuType = _PrtSonetTuType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 5),
    _PrtSonetTuType_Type()
)
prtSonetTuType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetTuType.setStatus("current")


class _PrtSonetTuMode_Type(Integer32):
    """Custom type prtSonetTuMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 3),
          ("addAndDrop", 2),
          ("notApplicable", 1))
    )


_PrtSonetTuMode_Type.__name__ = "Integer32"
_PrtSonetTuMode_Object = MibTableColumn
prtSonetTuMode = _PrtSonetTuMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 6),
    _PrtSonetTuMode_Type()
)
prtSonetTuMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetTuMode.setStatus("current")
_PrtSonetTuRowStatus_Type = RowStatus
_PrtSonetTuRowStatus_Object = MibTableColumn
prtSonetTuRowStatus = _PrtSonetTuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 7),
    _PrtSonetTuRowStatus_Type()
)
prtSonetTuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetTuRowStatus.setStatus("current")
_PrtVcGroupCnfg_ObjectIdentity = ObjectIdentity
prtVcGroupCnfg = _PrtVcGroupCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4)
)
_VcGroupCnfgTable_Object = MibTable
vcGroupCnfgTable = _VcGroupCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vcGroupCnfgTable.setStatus("current")
_VcGroupCnfgEntry_Object = MibTableRow
vcGroupCnfgEntry = _VcGroupCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1)
)
vcGroupCnfgEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "vcGroupCnfgIdx"),
    (0, "RAD-SONET-MIB", "vcGroupCnfgNumber"),
)
if mibBuilder.loadTexts:
    vcGroupCnfgEntry.setStatus("current")


class _VcGroupCnfgIdx_Type(Integer32):
    """Custom type vcGroupCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VcGroupCnfgIdx_Type.__name__ = "Integer32"
_VcGroupCnfgIdx_Object = MibTableColumn
vcGroupCnfgIdx = _VcGroupCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 1),
    _VcGroupCnfgIdx_Type()
)
vcGroupCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcGroupCnfgIdx.setStatus("current")
_VcGroupCnfgNumber_Type = Integer32
_VcGroupCnfgNumber_Object = MibTableColumn
vcGroupCnfgNumber = _VcGroupCnfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 2),
    _VcGroupCnfgNumber_Type()
)
vcGroupCnfgNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcGroupCnfgNumber.setStatus("current")
_VcGroupCnfgRowStatus_Type = RowStatus
_VcGroupCnfgRowStatus_Object = MibTableColumn
vcGroupCnfgRowStatus = _VcGroupCnfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 3),
    _VcGroupCnfgRowStatus_Type()
)
vcGroupCnfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcGroupCnfgRowStatus.setStatus("current")


class _VcGroupCnfgVcType_Type(Integer32):
    """Custom type vcGroupCnfgVcType based on Integer32"""
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
        *(("notApplicable", 1),
          ("sts1", 6),
          ("vc12", 2),
          ("vc3", 3),
          ("vc4", 4),
          ("vt1dot5", 5))
    )


_VcGroupCnfgVcType_Type.__name__ = "Integer32"
_VcGroupCnfgVcType_Object = MibTableColumn
vcGroupCnfgVcType = _VcGroupCnfgVcType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 4),
    _VcGroupCnfgVcType_Type()
)
vcGroupCnfgVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcGroupCnfgVcType.setStatus("current")


class _VcGroupCnfgNoOfVCs_Type(Integer32):
    """Custom type vcGroupCnfgNoOfVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_VcGroupCnfgNoOfVCs_Type.__name__ = "Integer32"
_VcGroupCnfgNoOfVCs_Object = MibTableColumn
vcGroupCnfgNoOfVCs = _VcGroupCnfgNoOfVCs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 5),
    _VcGroupCnfgNoOfVCs_Type()
)
vcGroupCnfgNoOfVCs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcGroupCnfgNoOfVCs.setStatus("current")


class _VcGroupCnfgLCAS_Type(Integer32):
    """Custom type vcGroupCnfgLCAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lcasActive", 3),
          ("lcasNotActive", 2),
          ("notApplicable", 1))
    )


_VcGroupCnfgLCAS_Type.__name__ = "Integer32"
_VcGroupCnfgLCAS_Object = MibTableColumn
vcGroupCnfgLCAS = _VcGroupCnfgLCAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 6),
    _VcGroupCnfgLCAS_Type()
)
vcGroupCnfgLCAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcGroupCnfgLCAS.setStatus("current")


class _VcGroupCnfgEncapsulation_Type(Integer32):
    """Custom type vcGroupCnfgEncapsulation based on Integer32"""
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
        *(("gfp", 4),
          ("lapf", 3),
          ("laps", 2),
          ("notApplicable", 1))
    )


_VcGroupCnfgEncapsulation_Type.__name__ = "Integer32"
_VcGroupCnfgEncapsulation_Object = MibTableColumn
vcGroupCnfgEncapsulation = _VcGroupCnfgEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 7),
    _VcGroupCnfgEncapsulation_Type()
)
vcGroupCnfgEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcGroupCnfgEncapsulation.setStatus("current")
_VcGroupCnfgGroupIfIndex_Type = InterfaceIndex
_VcGroupCnfgGroupIfIndex_Object = MibTableColumn
vcGroupCnfgGroupIfIndex = _VcGroupCnfgGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 8),
    _VcGroupCnfgGroupIfIndex_Type()
)
vcGroupCnfgGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcGroupCnfgGroupIfIndex.setStatus("current")


class _VcGroupCnfgRip2_Type(Integer32):
    """Custom type vcGroupCnfgRip2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notApplicable", 1),
          ("yes", 3))
    )


_VcGroupCnfgRip2_Type.__name__ = "Integer32"
_VcGroupCnfgRip2_Object = MibTableColumn
vcGroupCnfgRip2 = _VcGroupCnfgRip2_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 9),
    _VcGroupCnfgRip2_Type()
)
vcGroupCnfgRip2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcGroupCnfgRip2.setStatus("current")


class _VcGroupCnfgGfpChId_Type(Integer32):
    """Custom type vcGroupCnfgGfpChId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VcGroupCnfgGfpChId_Type.__name__ = "Integer32"
_VcGroupCnfgGfpChId_Object = MibTableColumn
vcGroupCnfgGfpChId = _VcGroupCnfgGfpChId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 10),
    _VcGroupCnfgGfpChId_Type()
)
vcGroupCnfgGfpChId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcGroupCnfgGfpChId.setStatus("current")


class _VcGroupCnfgK4_Type(Integer32):
    """Custom type vcGroupCnfgK4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notApplicable", 1),
          ("yes", 3))
    )


_VcGroupCnfgK4_Type.__name__ = "Integer32"
_VcGroupCnfgK4_Object = MibTableColumn
vcGroupCnfgK4 = _VcGroupCnfgK4_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 11),
    _VcGroupCnfgK4_Type()
)
vcGroupCnfgK4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcGroupCnfgK4.setStatus("current")


class _VcGroupCnfgExSignalLabel_Type(OctetString):
    """Custom type vcGroupCnfgExSignalLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VcGroupCnfgExSignalLabel_Type.__name__ = "OctetString"
_VcGroupCnfgExSignalLabel_Object = MibTableColumn
vcGroupCnfgExSignalLabel = _VcGroupCnfgExSignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 12),
    _VcGroupCnfgExSignalLabel_Type()
)
vcGroupCnfgExSignalLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcGroupCnfgExSignalLabel.setStatus("current")


class _VcGroupCnfgLcasMinNoOfVCs_Type(Integer32):
    """Custom type vcGroupCnfgLcasMinNoOfVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_VcGroupCnfgLcasMinNoOfVCs_Type.__name__ = "Integer32"
_VcGroupCnfgLcasMinNoOfVCs_Object = MibTableColumn
vcGroupCnfgLcasMinNoOfVCs = _VcGroupCnfgLcasMinNoOfVCs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 13),
    _VcGroupCnfgLcasMinNoOfVCs_Type()
)
vcGroupCnfgLcasMinNoOfVCs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcGroupCnfgLcasMinNoOfVCs.setStatus("current")


class _VcGroupCnfgLcasStatus_Type(Integer32):
    """Custom type vcGroupCnfgLcasStatus based on Integer32"""
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
        *(("allNorm", 4),
          ("belowMinNoOfVCs", 2),
          ("notApplicable", 1),
          ("withinRange", 3))
    )


_VcGroupCnfgLcasStatus_Type.__name__ = "Integer32"
_VcGroupCnfgLcasStatus_Object = MibTableColumn
vcGroupCnfgLcasStatus = _VcGroupCnfgLcasStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 1, 1, 14),
    _VcGroupCnfgLcasStatus_Type()
)
vcGroupCnfgLcasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcGroupCnfgLcasStatus.setStatus("current")
_VcgGfpMuxCnfgTable_Object = MibTable
vcgGfpMuxCnfgTable = _VcgGfpMuxCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    vcgGfpMuxCnfgTable.setStatus("current")
_VcgGfpMuxCnfgEntry_Object = MibTableRow
vcgGfpMuxCnfgEntry = _VcgGfpMuxCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 2, 1)
)
vcgGfpMuxCnfgEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "vcgGfpMuxCnfgIdx"),
    (0, "RAD-SONET-MIB", "vcgGfpMuxCnfgMuxNumber"),
)
if mibBuilder.loadTexts:
    vcgGfpMuxCnfgEntry.setStatus("current")


class _VcgGfpMuxCnfgIdx_Type(Integer32):
    """Custom type vcgGfpMuxCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VcgGfpMuxCnfgIdx_Type.__name__ = "Integer32"
_VcgGfpMuxCnfgIdx_Object = MibTableColumn
vcgGfpMuxCnfgIdx = _VcgGfpMuxCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 2, 1, 1),
    _VcgGfpMuxCnfgIdx_Type()
)
vcgGfpMuxCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcgGfpMuxCnfgIdx.setStatus("current")
_VcgGfpMuxCnfgMuxNumber_Type = Integer32
_VcgGfpMuxCnfgMuxNumber_Object = MibTableColumn
vcgGfpMuxCnfgMuxNumber = _VcgGfpMuxCnfgMuxNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 2, 1, 2),
    _VcgGfpMuxCnfgMuxNumber_Type()
)
vcgGfpMuxCnfgMuxNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcgGfpMuxCnfgMuxNumber.setStatus("current")
_VcgGfpMuxCnfgRowStatus_Type = RowStatus
_VcgGfpMuxCnfgRowStatus_Object = MibTableColumn
vcgGfpMuxCnfgRowStatus = _VcgGfpMuxCnfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 2, 1, 3),
    _VcgGfpMuxCnfgRowStatus_Type()
)
vcgGfpMuxCnfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgGfpMuxCnfgRowStatus.setStatus("current")
_VcgGfpMuxCnfgMuxName_Type = SnmpAdminString
_VcgGfpMuxCnfgMuxName_Object = MibTableColumn
vcgGfpMuxCnfgMuxName = _VcgGfpMuxCnfgMuxName_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 2, 1, 4),
    _VcgGfpMuxCnfgMuxName_Type()
)
vcgGfpMuxCnfgMuxName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgGfpMuxCnfgMuxName.setStatus("current")
_VcgGfpMuxCnfgPrimeGroup_Type = Integer32
_VcgGfpMuxCnfgPrimeGroup_Object = MibTableColumn
vcgGfpMuxCnfgPrimeGroup = _VcgGfpMuxCnfgPrimeGroup_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 2, 1, 5),
    _VcgGfpMuxCnfgPrimeGroup_Type()
)
vcgGfpMuxCnfgPrimeGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgGfpMuxCnfgPrimeGroup.setStatus("current")
_VcgGfpMuxCnfgGrpBwAlloc_Type = OctetString
_VcgGfpMuxCnfgGrpBwAlloc_Object = MibTableColumn
vcgGfpMuxCnfgGrpBwAlloc = _VcgGfpMuxCnfgGrpBwAlloc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 4, 2, 1, 6),
    _VcgGfpMuxCnfgGrpBwAlloc_Type()
)
vcgGfpMuxCnfgGrpBwAlloc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgGfpMuxCnfgGrpBwAlloc.setStatus("current")
_VirtualIfConfiguration_ObjectIdentity = ObjectIdentity
virtualIfConfiguration = _VirtualIfConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 5)
)
_VirtualIfGenTable_Object = MibTable
virtualIfGenTable = _VirtualIfGenTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    virtualIfGenTable.setStatus("current")
_VirtualIfGenEntry_Object = MibTableRow
virtualIfGenEntry = _VirtualIfGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 5, 1, 1)
)
virtualIfGenEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "virtualIfGenCnfgIdx"),
    (0, "RAD-SONET-MIB", "virtualIfGenIdx"),
)
if mibBuilder.loadTexts:
    virtualIfGenEntry.setStatus("current")


class _VirtualIfGenCnfgIdx_Type(Integer32):
    """Custom type virtualIfGenCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VirtualIfGenCnfgIdx_Type.__name__ = "Integer32"
_VirtualIfGenCnfgIdx_Object = MibTableColumn
virtualIfGenCnfgIdx = _VirtualIfGenCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 5, 1, 1, 1),
    _VirtualIfGenCnfgIdx_Type()
)
virtualIfGenCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGenCnfgIdx.setStatus("current")
_VirtualIfGenIdx_Type = Integer32
_VirtualIfGenIdx_Object = MibTableColumn
virtualIfGenIdx = _VirtualIfGenIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 5, 1, 1, 2),
    _VirtualIfGenIdx_Type()
)
virtualIfGenIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIfGenIdx.setStatus("current")


class _VirtualIfGenFrameFormat_Type(Integer32):
    """Custom type virtualIfGenFrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fcsDisable", 3),
          ("fcsEnable", 2),
          ("notApplicable", 1))
    )


_VirtualIfGenFrameFormat_Type.__name__ = "Integer32"
_VirtualIfGenFrameFormat_Object = MibTableColumn
virtualIfGenFrameFormat = _VirtualIfGenFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 5, 1, 1, 3),
    _VirtualIfGenFrameFormat_Type()
)
virtualIfGenFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualIfGenFrameFormat.setStatus("current")
_PrtSonetXConnect_ObjectIdentity = ObjectIdentity
prtSonetXConnect = _PrtSonetXConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3)
)
_PrtSonetXConnectTable_Object = MibTable
prtSonetXConnectTable = _PrtSonetXConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1)
)
if mibBuilder.loadTexts:
    prtSonetXConnectTable.setStatus("current")
_PrtSonetXConnectEntry_Object = MibTableRow
prtSonetXConnectEntry = _PrtSonetXConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1)
)
prtSonetXConnectEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "prtSonetXConnectCnfgIdx"),
    (0, "RAD-SONET-MIB", "prtSonetXConnectPrtIdx"),
    (0, "RAD-SONET-MIB", "prtSonetXConnectConPrtIdx"),
    (0, "RAD-SONET-MIB", "prtSonetXConnectAUGIdx"),
    (0, "RAD-SONET-MIB", "prtSonetXConnectTUG3Idx"),
    (0, "RAD-SONET-MIB", "prtSonetXConnectTUG2Idx"),
    (0, "RAD-SONET-MIB", "prtSonetXConnectTUnIdx"),
)
if mibBuilder.loadTexts:
    prtSonetXConnectEntry.setStatus("current")


class _PrtSonetXConnectCnfgIdx_Type(Integer32):
    """Custom type prtSonetXConnectCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSonetXConnectCnfgIdx_Type.__name__ = "Integer32"
_PrtSonetXConnectCnfgIdx_Object = MibTableColumn
prtSonetXConnectCnfgIdx = _PrtSonetXConnectCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 1),
    _PrtSonetXConnectCnfgIdx_Type()
)
prtSonetXConnectCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectCnfgIdx.setStatus("current")
_PrtSonetXConnectPrtIdx_Type = Integer32
_PrtSonetXConnectPrtIdx_Object = MibTableColumn
prtSonetXConnectPrtIdx = _PrtSonetXConnectPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 2),
    _PrtSonetXConnectPrtIdx_Type()
)
prtSonetXConnectPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectPrtIdx.setStatus("current")
_PrtSonetXConnectConPrtIdx_Type = Integer32
_PrtSonetXConnectConPrtIdx_Object = MibTableColumn
prtSonetXConnectConPrtIdx = _PrtSonetXConnectConPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 3),
    _PrtSonetXConnectConPrtIdx_Type()
)
prtSonetXConnectConPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectConPrtIdx.setStatus("current")
_PrtSonetXConnectAUGIdx_Type = Integer32
_PrtSonetXConnectAUGIdx_Object = MibTableColumn
prtSonetXConnectAUGIdx = _PrtSonetXConnectAUGIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 4),
    _PrtSonetXConnectAUGIdx_Type()
)
prtSonetXConnectAUGIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectAUGIdx.setStatus("current")
_PrtSonetXConnectTUG3Idx_Type = Integer32
_PrtSonetXConnectTUG3Idx_Object = MibTableColumn
prtSonetXConnectTUG3Idx = _PrtSonetXConnectTUG3Idx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 5),
    _PrtSonetXConnectTUG3Idx_Type()
)
prtSonetXConnectTUG3Idx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectTUG3Idx.setStatus("current")
_PrtSonetXConnectTUG2Idx_Type = Integer32
_PrtSonetXConnectTUG2Idx_Object = MibTableColumn
prtSonetXConnectTUG2Idx = _PrtSonetXConnectTUG2Idx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 6),
    _PrtSonetXConnectTUG2Idx_Type()
)
prtSonetXConnectTUG2Idx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectTUG2Idx.setStatus("current")
_PrtSonetXConnectTUnIdx_Type = Integer32
_PrtSonetXConnectTUnIdx_Object = MibTableColumn
prtSonetXConnectTUnIdx = _PrtSonetXConnectTUnIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 7),
    _PrtSonetXConnectTUnIdx_Type()
)
prtSonetXConnectTUnIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectTUnIdx.setStatus("current")
_PrtSonetXConnectRowStatus_Type = RowStatus
_PrtSonetXConnectRowStatus_Object = MibTableColumn
prtSonetXConnectRowStatus = _PrtSonetXConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 8),
    _PrtSonetXConnectRowStatus_Type()
)
prtSonetXConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetXConnectRowStatus.setStatus("current")


class _PrtSonetXConnectDirection_Type(Integer32):
    """Custom type prtSonetXConnectDirection based on Integer32"""
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
        *(("both", 4),
          ("notApplicable", 1),
          ("rx", 2),
          ("tx", 3))
    )


_PrtSonetXConnectDirection_Type.__name__ = "Integer32"
_PrtSonetXConnectDirection_Object = MibTableColumn
prtSonetXConnectDirection = _PrtSonetXConnectDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 9),
    _PrtSonetXConnectDirection_Type()
)
prtSonetXConnectDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetXConnectDirection.setStatus("current")


class _PrtSonetXConnectTuNumber_Type(Integer32):
    """Custom type prtSonetXConnectTuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("tu11", 4),
          ("tu12", 5),
          ("tu2", 2),
          ("tu3", 3))
    )


_PrtSonetXConnectTuNumber_Type.__name__ = "Integer32"
_PrtSonetXConnectTuNumber_Object = MibTableColumn
prtSonetXConnectTuNumber = _PrtSonetXConnectTuNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 10),
    _PrtSonetXConnectTuNumber_Type()
)
prtSonetXConnectTuNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetXConnectTuNumber.setStatus("current")
_PrtSonetStatus_ObjectIdentity = ObjectIdentity
prtSonetStatus = _PrtSonetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 4)
)
_PrtSonetVcStatTable_Object = MibTable
prtSonetVcStatTable = _PrtSonetVcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 4, 1)
)
if mibBuilder.loadTexts:
    prtSonetVcStatTable.setStatus("current")
_PrtSonetVcStatEntry_Object = MibTableRow
prtSonetVcStatEntry = _PrtSonetVcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 4, 1, 1)
)
prtSonetVcStatEntry.setIndexNames(
    (0, "RAD-SONET-MIB", "prtSonetVcIdx"),
)
if mibBuilder.loadTexts:
    prtSonetVcStatEntry.setStatus("current")


class _PrtSonetVcRxJPathTrace_Type(SnmpAdminString):
    """Custom type prtSonetVcRxJPathTrace based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_PrtSonetVcRxJPathTrace_Type.__name__ = "SnmpAdminString"
_PrtSonetVcRxJPathTrace_Object = MibTableColumn
prtSonetVcRxJPathTrace = _PrtSonetVcRxJPathTrace_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 4, 1, 1, 1),
    _PrtSonetVcRxJPathTrace_Type()
)
prtSonetVcRxJPathTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetVcRxJPathTrace.setStatus("current")


class _PrtSonetVcRxSignalLabel_Type(OctetString):
    """Custom type prtSonetVcRxSignalLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PrtSonetVcRxSignalLabel_Type.__name__ = "OctetString"
_PrtSonetVcRxSignalLabel_Object = MibTableColumn
prtSonetVcRxSignalLabel = _PrtSonetVcRxSignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 4, 1, 1, 2),
    _PrtSonetVcRxSignalLabel_Type()
)
prtSonetVcRxSignalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetVcRxSignalLabel.setStatus("current")


class _PrtSonetVcLcasSourceState_Type(Integer32):
    """Custom type prtSonetVcLcasSourceState based on Integer32"""
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
        *(("add", 3),
          ("dnu", 7),
          ("eos", 5),
          ("fixed", 2),
          ("idle", 6),
          ("norm", 4),
          ("notApplicable", 1))
    )


_PrtSonetVcLcasSourceState_Type.__name__ = "Integer32"
_PrtSonetVcLcasSourceState_Object = MibTableColumn
prtSonetVcLcasSourceState = _PrtSonetVcLcasSourceState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 4, 1, 1, 3),
    _PrtSonetVcLcasSourceState_Type()
)
prtSonetVcLcasSourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetVcLcasSourceState.setStatus("current")


class _PrtSonetVcLcasSinkState_Type(Integer32):
    """Custom type prtSonetVcLcasSinkState based on Integer32"""
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
        *(("add", 3),
          ("dnu", 7),
          ("eos", 5),
          ("fixed", 2),
          ("idle", 6),
          ("norm", 4),
          ("notApplicable", 1))
    )


_PrtSonetVcLcasSinkState_Type.__name__ = "Integer32"
_PrtSonetVcLcasSinkState_Object = MibTableColumn
prtSonetVcLcasSinkState = _PrtSonetVcLcasSinkState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 4, 1, 1, 4),
    _PrtSonetVcLcasSinkState_Type()
)
prtSonetVcLcasSinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetVcLcasSinkState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-SONET-MIB",
    **{"sonetInterface": sonetInterface,
       "prtSonetPerfHistory": prtSonetPerfHistory,
       "prtSonetMediumTable": prtSonetMediumTable,
       "prtSonetMediumEntry": prtSonetMediumEntry,
       "prtSonetMediumTimeElapsed": prtSonetMediumTimeElapsed,
       "prtSonetMediumValidIntervals": prtSonetMediumValidIntervals,
       "prtSonetSectionLineCurrentTable": prtSonetSectionLineCurrentTable,
       "prtSectionLineCurrentEntry": prtSectionLineCurrentEntry,
       "prtSonetCurrentLOS": prtSonetCurrentLOS,
       "prtSonetCurrentLOF": prtSonetCurrentLOF,
       "prtSonetCurrentLineAIS": prtSonetCurrentLineAIS,
       "prtSonetCurrentLineFERF": prtSonetCurrentLineFERF,
       "prtSonetCurrentSectionBIP": prtSonetCurrentSectionBIP,
       "prtSonetCurrentLineBIP": prtSonetCurrentLineBIP,
       "prtSonetCurrentLineFEBE": prtSonetCurrentLineFEBE,
       "prtSonetCurrentUAS": prtSonetCurrentUAS,
       "prtSonetCurrentSES": prtSonetCurrentSES,
       "prtSonetCurrentES": prtSonetCurrentES,
       "prtSonetCurrentStatus": prtSonetCurrentStatus,
       "prtSonetCurrentLSV": prtSonetCurrentLSV,
       "prtSonetSectionLineIntervalTable": prtSonetSectionLineIntervalTable,
       "prtSectionLineIntervalEntry": prtSectionLineIntervalEntry,
       "prtSonetLineIntervalNumber": prtSonetLineIntervalNumber,
       "prtSonetIntervalLOS": prtSonetIntervalLOS,
       "prtSonetIntervalLOF": prtSonetIntervalLOF,
       "prtSonetIntervalLineAIS": prtSonetIntervalLineAIS,
       "prtSonetIntervalLineFERF": prtSonetIntervalLineFERF,
       "prtSonetIntervalSectionBIP": prtSonetIntervalSectionBIP,
       "prtSonetIntervalLineBIP": prtSonetIntervalLineBIP,
       "prtSonetIntervalLineFEBE": prtSonetIntervalLineFEBE,
       "prtSonetIntervalUAS": prtSonetIntervalUAS,
       "prtSonetIntervalSES": prtSonetIntervalSES,
       "prtSonetIntervalES": prtSonetIntervalES,
       "prtSonetIntervalStatus": prtSonetIntervalStatus,
       "prtSonetIntervalLSV": prtSonetIntervalLSV,
       "prtSonetPathCurrentTable": prtSonetPathCurrentTable,
       "prtPathCurrentEntry": prtPathCurrentEntry,
       "prtSonetCurrentPathAIS": prtSonetCurrentPathAIS,
       "prtSonetCurrentPathFERF": prtSonetCurrentPathFERF,
       "prtSonetCurrentLOP": prtSonetCurrentLOP,
       "prtSonetCurrentSLM": prtSonetCurrentSLM,
       "prtSonetCurrentLOC": prtSonetCurrentLOC,
       "prtSonetCurrentPathBIP": prtSonetCurrentPathBIP,
       "prtSonetCurrentPathFEBE": prtSonetCurrentPathFEBE,
       "prtSonetPathIntervalTable": prtSonetPathIntervalTable,
       "prtPathIntervalEntry": prtPathIntervalEntry,
       "prtSonetPathIntervalNumber": prtSonetPathIntervalNumber,
       "prtSonetIntervalPathAIS": prtSonetIntervalPathAIS,
       "prtSonetIntervalPathFERF": prtSonetIntervalPathFERF,
       "prtSonetIntervalLOP": prtSonetIntervalLOP,
       "prtSonetIntervalSLM": prtSonetIntervalSLM,
       "prtSonetIntervalLOC": prtSonetIntervalLOC,
       "prtSonetIntervalPathBIP": prtSonetIntervalPathBIP,
       "prtSonetIntervalPathFEBE": prtSonetIntervalPathFEBE,
       "virtualIfStatistics": virtualIfStatistics,
       "virtualIfCurrentTable": virtualIfCurrentTable,
       "virtualIfCurrentEntry": virtualIfCurrentEntry,
       "virtualIfCurrentMinActiveVC": virtualIfCurrentMinActiveVC,
       "virtualIfCurrentMaxActiveVC": virtualIfCurrentMaxActiveVC,
       "virtualIfCurrentRxFrames": virtualIfCurrentRxFrames,
       "virtualIfCurrentTxFrames": virtualIfCurrentTxFrames,
       "virtualIfCurrentRxAbortFrames": virtualIfCurrentRxAbortFrames,
       "virtualIfCurrentTxAbortFrames": virtualIfCurrentTxAbortFrames,
       "virtualIfCurrentMinLengthViolation": virtualIfCurrentMinLengthViolation,
       "virtualIfCurrentMaxLengthViolation": virtualIfCurrentMaxLengthViolation,
       "virtualIfCurrentFcsError": virtualIfCurrentFcsError,
       "virtualIfCurrentByteDestuffingViolation": virtualIfCurrentByteDestuffingViolation,
       "virtualIfCurrentAdressMismatch": virtualIfCurrentAdressMismatch,
       "virtualIfCurrentControlMismatch": virtualIfCurrentControlMismatch,
       "virtualIfCurrentActiveVC": virtualIfCurrentActiveVC,
       "virtualIfIntervalTable": virtualIfIntervalTable,
       "virtualIfIntervalEntry": virtualIfIntervalEntry,
       "virtualIfIntervalNumber": virtualIfIntervalNumber,
       "virtualIfIntervalMinActiveVC": virtualIfIntervalMinActiveVC,
       "virtualIfIntervalMaxActiveVC": virtualIfIntervalMaxActiveVC,
       "virtualIfIntervalRxFrames": virtualIfIntervalRxFrames,
       "virtualIfIntervalTxFrames": virtualIfIntervalTxFrames,
       "virtualIfIntervalRxAbortFrames": virtualIfIntervalRxAbortFrames,
       "virtualIfIntervalTxAbortFrames": virtualIfIntervalTxAbortFrames,
       "virtualIfIntervalMinLengthViolation": virtualIfIntervalMinLengthViolation,
       "virtualIfIntervalMaxLengthViolation": virtualIfIntervalMaxLengthViolation,
       "virtualIfIntervalFcsError": virtualIfIntervalFcsError,
       "virtualIfIntervalByteDestuffingViolation": virtualIfIntervalByteDestuffingViolation,
       "virtualIfIntervalAdressMismatch": virtualIfIntervalAdressMismatch,
       "virtualIfIntervalControlMismatch": virtualIfIntervalControlMismatch,
       "virtualIfIntervalBelowMinThreshold": virtualIfIntervalBelowMinThreshold,
       "virtualIfLAPSCurrentTable": virtualIfLAPSCurrentTable,
       "virtualIfLAPSCurrentEntry": virtualIfLAPSCurrentEntry,
       "virtualIfLAPSCurrentSapiMismatch": virtualIfLAPSCurrentSapiMismatch,
       "virtualIfLAPSIntervalTable": virtualIfLAPSIntervalTable,
       "virtualIfLAPSIntervalEntry": virtualIfLAPSIntervalEntry,
       "virtualIfLAPSIntervalSapiMismatch": virtualIfLAPSIntervalSapiMismatch,
       "virtualIfLAPFCurrentTable": virtualIfLAPFCurrentTable,
       "virtualIfLAPFCurrentEntry": virtualIfLAPFCurrentEntry,
       "virtualIfLAPFCurrentNlpidMismatch": virtualIfLAPFCurrentNlpidMismatch,
       "virtualIfLAPFCurrentOuiMismatch": virtualIfLAPFCurrentOuiMismatch,
       "virtualIfLAPFCurrentPidMismatch": virtualIfLAPFCurrentPidMismatch,
       "virtualIfLAPFCurrentDlciMismatch": virtualIfLAPFCurrentDlciMismatch,
       "virtualIfLAPFCurrentMacRxFrames": virtualIfLAPFCurrentMacRxFrames,
       "virtualIfLAPFCurrentMacTxFrames": virtualIfLAPFCurrentMacTxFrames,
       "virtualIfLAPFIntervalTable": virtualIfLAPFIntervalTable,
       "virtualIfLAPFIntervalEntry": virtualIfLAPFIntervalEntry,
       "virtualIfLAPFIntervalNlpidMismatch": virtualIfLAPFIntervalNlpidMismatch,
       "virtualIfLAPFIntervalOuiMismatch": virtualIfLAPFIntervalOuiMismatch,
       "virtualIfLAPFIntervalPidMismatch": virtualIfLAPFIntervalPidMismatch,
       "virtualIfLAPFIntervalDlciMismatch": virtualIfLAPFIntervalDlciMismatch,
       "virtualIfLAPFIntervalMacRxFrames": virtualIfLAPFIntervalMacRxFrames,
       "virtualIfLAPFIntervalMacTxFrames": virtualIfLAPFIntervalMacTxFrames,
       "virtualIfGFPCurrentTable": virtualIfGFPCurrentTable,
       "virtualIfGFPCurrentEntry": virtualIfGFPCurrentEntry,
       "virtualIfGFPCurrentIdleFrameError": virtualIfGFPCurrentIdleFrameError,
       "virtualIfGFPCurrentCHecSbError": virtualIfGFPCurrentCHecSbError,
       "virtualIfGFPCurrentPtiMismatch": virtualIfGFPCurrentPtiMismatch,
       "virtualIfGFPCurrentExiMismatch": virtualIfGFPCurrentExiMismatch,
       "virtualIfGFPCurrentUpiMismatch": virtualIfGFPCurrentUpiMismatch,
       "virtualIfGFPCurrentTHecSbError": virtualIfGFPCurrentTHecSbError,
       "virtualIfGFPCurrentTHecMbError": virtualIfGFPCurrentTHecMbError,
       "virtualIfGFPCurrentCidMismatch": virtualIfGFPCurrentCidMismatch,
       "virtualIfGFPCurrentEHecSbError": virtualIfGFPCurrentEHecSbError,
       "virtualIfGFPCurrentEHecMbError": virtualIfGFPCurrentEHecMbError,
       "virtualIfGFPIntervalTable": virtualIfGFPIntervalTable,
       "virtualIfGFPIntervalEntry": virtualIfGFPIntervalEntry,
       "virtualIfGFPIntervalIdleFrameError": virtualIfGFPIntervalIdleFrameError,
       "virtualIfGFPIntervalCHecSbError": virtualIfGFPIntervalCHecSbError,
       "virtualIfGFPIntervalPtiMismatch": virtualIfGFPIntervalPtiMismatch,
       "virtualIfGFPIntervalExiMismatch": virtualIfGFPIntervalExiMismatch,
       "virtualIfGFPIntervalUpiMismatch": virtualIfGFPIntervalUpiMismatch,
       "virtualIfGFPIntervalTHecSbError": virtualIfGFPIntervalTHecSbError,
       "virtualIfGFPIntervalTHecMbError": virtualIfGFPIntervalTHecMbError,
       "virtualIfGFPIntervalCidMismatch": virtualIfGFPIntervalCidMismatch,
       "virtualIfGFPIntervalEHecSbError": virtualIfGFPIntervalEHecSbError,
       "virtualIfGFPIntervalEHecMbError": virtualIfGFPIntervalEHecMbError,
       "prtSonetConfig": prtSonetConfig,
       "prtSonetGen": prtSonetGen,
       "prtSonetGenTable": prtSonetGenTable,
       "prtSonetGenEntry": prtSonetGenEntry,
       "prtSonetGenCnfgIdx": prtSonetGenCnfgIdx,
       "prtSonetGenIdx": prtSonetGenIdx,
       "prtSonetGenSdThreshold": prtSonetGenSdThreshold,
       "prtSonetGenEedThreshold": prtSonetGenEedThreshold,
       "prtSonetGenBerEnable": prtSonetGenBerEnable,
       "prtSonetStm1": prtSonetStm1,
       "prtSonetStm1Table": prtSonetStm1Table,
       "prtSonetStm1Entry": prtSonetStm1Entry,
       "prtSonetStm1CnfgIdx": prtSonetStm1CnfgIdx,
       "prtSonetStm1Idx": prtSonetStm1Idx,
       "prtSonetStm1ClockSrc": prtSonetStm1ClockSrc,
       "prtSonetStm1DccMode": prtSonetStm1DccMode,
       "prtSonetStm1RoutingProt": prtSonetStm1RoutingProt,
       "prtSonetStm1MngProt": prtSonetStm1MngProt,
       "prtSonetStm1OperationalMode": prtSonetStm1OperationalMode,
       "prtSonetStm1VoiceChannel": prtSonetStm1VoiceChannel,
       "prtSonetStm1OutputRate": prtSonetStm1OutputRate,
       "prtSonetStm1S1ProtocolClock": prtSonetStm1S1ProtocolClock,
       "prtSonetStm1GatewayRingSubnetAddress": prtSonetStm1GatewayRingSubnetAddress,
       "prtSonetStm1GatewayRingSubnetMask": prtSonetStm1GatewayRingSubnetMask,
       "prtSonetStm1MngProtDeviationType": prtSonetStm1MngProtDeviationType,
       "prtSonetVc": prtSonetVc,
       "prtSonetVcTable": prtSonetVcTable,
       "prtSonetVcEntry": prtSonetVcEntry,
       "prtSonetVcCnfgIdx": prtSonetVcCnfgIdx,
       "prtSonetVcIdx": prtSonetVcIdx,
       "prtSonetVcJTxPathTraceEnable": prtSonetVcJTxPathTraceEnable,
       "prtSonetVcJRxPathTraceEnable": prtSonetVcJRxPathTraceEnable,
       "prtSonetVcJPathTrace": prtSonetVcJPathTrace,
       "prtSonetVcConnect": prtSonetVcConnect,
       "prtSonetVcSignalLabel": prtSonetVcSignalLabel,
       "prtSonetTuTable": prtSonetTuTable,
       "prtSonetTuEntry": prtSonetTuEntry,
       "prtSonetTuCnfgIdx": prtSonetTuCnfgIdx,
       "prtSonetTuPrtIdx": prtSonetTuPrtIdx,
       "prtSonetTuIdx": prtSonetTuIdx,
       "prtSonetTuConPrtIdx": prtSonetTuConPrtIdx,
       "prtSonetTuType": prtSonetTuType,
       "prtSonetTuMode": prtSonetTuMode,
       "prtSonetTuRowStatus": prtSonetTuRowStatus,
       "prtVcGroupCnfg": prtVcGroupCnfg,
       "vcGroupCnfgTable": vcGroupCnfgTable,
       "vcGroupCnfgEntry": vcGroupCnfgEntry,
       "vcGroupCnfgIdx": vcGroupCnfgIdx,
       "vcGroupCnfgNumber": vcGroupCnfgNumber,
       "vcGroupCnfgRowStatus": vcGroupCnfgRowStatus,
       "vcGroupCnfgVcType": vcGroupCnfgVcType,
       "vcGroupCnfgNoOfVCs": vcGroupCnfgNoOfVCs,
       "vcGroupCnfgLCAS": vcGroupCnfgLCAS,
       "vcGroupCnfgEncapsulation": vcGroupCnfgEncapsulation,
       "vcGroupCnfgGroupIfIndex": vcGroupCnfgGroupIfIndex,
       "vcGroupCnfgRip2": vcGroupCnfgRip2,
       "vcGroupCnfgGfpChId": vcGroupCnfgGfpChId,
       "vcGroupCnfgK4": vcGroupCnfgK4,
       "vcGroupCnfgExSignalLabel": vcGroupCnfgExSignalLabel,
       "vcGroupCnfgLcasMinNoOfVCs": vcGroupCnfgLcasMinNoOfVCs,
       "vcGroupCnfgLcasStatus": vcGroupCnfgLcasStatus,
       "vcgGfpMuxCnfgTable": vcgGfpMuxCnfgTable,
       "vcgGfpMuxCnfgEntry": vcgGfpMuxCnfgEntry,
       "vcgGfpMuxCnfgIdx": vcgGfpMuxCnfgIdx,
       "vcgGfpMuxCnfgMuxNumber": vcgGfpMuxCnfgMuxNumber,
       "vcgGfpMuxCnfgRowStatus": vcgGfpMuxCnfgRowStatus,
       "vcgGfpMuxCnfgMuxName": vcgGfpMuxCnfgMuxName,
       "vcgGfpMuxCnfgPrimeGroup": vcgGfpMuxCnfgPrimeGroup,
       "vcgGfpMuxCnfgGrpBwAlloc": vcgGfpMuxCnfgGrpBwAlloc,
       "virtualIfConfiguration": virtualIfConfiguration,
       "virtualIfGenTable": virtualIfGenTable,
       "virtualIfGenEntry": virtualIfGenEntry,
       "virtualIfGenCnfgIdx": virtualIfGenCnfgIdx,
       "virtualIfGenIdx": virtualIfGenIdx,
       "virtualIfGenFrameFormat": virtualIfGenFrameFormat,
       "prtSonetXConnect": prtSonetXConnect,
       "prtSonetXConnectTable": prtSonetXConnectTable,
       "prtSonetXConnectEntry": prtSonetXConnectEntry,
       "prtSonetXConnectCnfgIdx": prtSonetXConnectCnfgIdx,
       "prtSonetXConnectPrtIdx": prtSonetXConnectPrtIdx,
       "prtSonetXConnectConPrtIdx": prtSonetXConnectConPrtIdx,
       "prtSonetXConnectAUGIdx": prtSonetXConnectAUGIdx,
       "prtSonetXConnectTUG3Idx": prtSonetXConnectTUG3Idx,
       "prtSonetXConnectTUG2Idx": prtSonetXConnectTUG2Idx,
       "prtSonetXConnectTUnIdx": prtSonetXConnectTUnIdx,
       "prtSonetXConnectRowStatus": prtSonetXConnectRowStatus,
       "prtSonetXConnectDirection": prtSonetXConnectDirection,
       "prtSonetXConnectTuNumber": prtSonetXConnectTuNumber,
       "prtSonetStatus": prtSonetStatus,
       "prtSonetVcStatTable": prtSonetVcStatTable,
       "prtSonetVcStatEntry": prtSonetVcStatEntry,
       "prtSonetVcRxJPathTrace": prtSonetVcRxJPathTrace,
       "prtSonetVcRxSignalLabel": prtSonetVcRxSignalLabel,
       "prtSonetVcLcasSourceState": prtSonetVcLcasSourceState,
       "prtSonetVcLcasSinkState": prtSonetVcLcasSinkState}
)
