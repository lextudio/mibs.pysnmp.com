# SNMP MIB module (CISCO-SVC-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SVC-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:00 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcNameId,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameId",
    "VsanIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY

ciscoSvcInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 378)
)
ciscoSvcInterfaceMIB.setRevisions(
        ("2004-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NportType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSvcInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSvcInterfaceMIBObjects = _CiscoSvcInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1)
)
_CSvcInterfaceConfiguration_ObjectIdentity = ObjectIdentity
cSvcInterfaceConfiguration = _CSvcInterfaceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1)
)
_CsiNportTable_Object = MibTable
csiNportTable = _CsiNportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 1)
)
if mibBuilder.loadTexts:
    csiNportTable.setStatus("current")
_CsiNportEntry_Object = MibTableRow
csiNportEntry = _CsiNportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 1, 1)
)
csiNportEntry.setIndexNames(
    (0, "CISCO-SVC-INTERFACE-MIB", "csiNportIfIndex"),
    (0, "CISCO-SVC-INTERFACE-MIB", "csiNportType"),
    (0, "CISCO-SVC-INTERFACE-MIB", "csiNportVsanId"),
)
if mibBuilder.loadTexts:
    csiNportEntry.setStatus("current")
_CsiNportIfIndex_Type = InterfaceIndex
_CsiNportIfIndex_Object = MibTableColumn
csiNportIfIndex = _CsiNportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 1, 1, 1),
    _CsiNportIfIndex_Type()
)
csiNportIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiNportIfIndex.setStatus("current")
_CsiNportType_Type = NportType
_CsiNportType_Object = MibTableColumn
csiNportType = _CsiNportType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 1, 1, 2),
    _CsiNportType_Type()
)
csiNportType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiNportType.setStatus("current")
_CsiNportVsanId_Type = VsanIndex
_CsiNportVsanId_Object = MibTableColumn
csiNportVsanId = _CsiNportVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 1, 1, 3),
    _CsiNportVsanId_Type()
)
csiNportVsanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiNportVsanId.setStatus("current")
_CsiNportPwwn_Type = FcNameId
_CsiNportPwwn_Object = MibTableColumn
csiNportPwwn = _CsiNportPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 1, 1, 4),
    _CsiNportPwwn_Type()
)
csiNportPwwn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiNportPwwn.setStatus("current")


class _CsiNportFcid_Type(Integer32):
    """Custom type csiNportFcid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_CsiNportFcid_Type.__name__ = "Integer32"
_CsiNportFcid_Object = MibTableColumn
csiNportFcid = _CsiNportFcid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 1, 1, 5),
    _CsiNportFcid_Type()
)
csiNportFcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportFcid.setStatus("current")


class _CsiNportState_Type(Integer32):
    """Custom type csiNportState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CsiNportState_Type.__name__ = "Integer32"
_CsiNportState_Object = MibTableColumn
csiNportState = _CsiNportState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 1, 1, 6),
    _CsiNportState_Type()
)
csiNportState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportState.setStatus("current")


class _CsiNportDownReason_Type(Integer32):
    """Custom type csiNportDownReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 2),
          ("ifHardwareDown", 7),
          ("ifSoftwareDown", 3),
          ("inRemovalState", 6),
          ("lineCardSwDown", 4),
          ("none", 1),
          ("uninitialized", 8),
          ("vsanDown", 5))
    )


_CsiNportDownReason_Type.__name__ = "Integer32"
_CsiNportDownReason_Object = MibTableColumn
csiNportDownReason = _CsiNportDownReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 1, 1, 7),
    _CsiNportDownReason_Type()
)
csiNportDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportDownReason.setStatus("current")
_CsiNportRowStatus_Type = RowStatus
_CsiNportRowStatus_Object = MibTableColumn
csiNportRowStatus = _CsiNportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 1, 1, 8),
    _CsiNportRowStatus_Type()
)
csiNportRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiNportRowStatus.setStatus("current")
_CsiSessionTable_Object = MibTable
csiSessionTable = _CsiSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 2)
)
if mibBuilder.loadTexts:
    csiSessionTable.setStatus("current")
_CsiSessionEntry_Object = MibTableRow
csiSessionEntry = _CsiSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 2, 1)
)
csiSessionEntry.setIndexNames(
    (0, "CISCO-SVC-INTERFACE-MIB", "csiSessionIfIndex"),
    (0, "CISCO-SVC-INTERFACE-MIB", "csiSessionType"),
    (0, "CISCO-SVC-INTERFACE-MIB", "csiSessionVsanId"),
    (0, "CISCO-SVC-INTERFACE-MIB", "csiSessionId"),
)
if mibBuilder.loadTexts:
    csiSessionEntry.setStatus("current")
_CsiSessionIfIndex_Type = InterfaceIndex
_CsiSessionIfIndex_Object = MibTableColumn
csiSessionIfIndex = _CsiSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 2, 1, 1),
    _CsiSessionIfIndex_Type()
)
csiSessionIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiSessionIfIndex.setStatus("current")
_CsiSessionType_Type = NportType
_CsiSessionType_Object = MibTableColumn
csiSessionType = _CsiSessionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 2, 1, 2),
    _CsiSessionType_Type()
)
csiSessionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiSessionType.setStatus("current")
_CsiSessionVsanId_Type = VsanIndex
_CsiSessionVsanId_Object = MibTableColumn
csiSessionVsanId = _CsiSessionVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 2, 1, 3),
    _CsiSessionVsanId_Type()
)
csiSessionVsanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiSessionVsanId.setStatus("current")


class _CsiSessionId_Type(Integer32):
    """Custom type csiSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CsiSessionId_Type.__name__ = "Integer32"
_CsiSessionId_Object = MibTableColumn
csiSessionId = _CsiSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 2, 1, 4),
    _CsiSessionId_Type()
)
csiSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiSessionId.setStatus("current")
_CsiSessionNportPwwn_Type = FcNameId
_CsiSessionNportPwwn_Object = MibTableColumn
csiSessionNportPwwn = _CsiSessionNportPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 2, 1, 5),
    _CsiSessionNportPwwn_Type()
)
csiSessionNportPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionNportPwwn.setStatus("current")
_CsiSessionPeerPwwn_Type = FcNameId
_CsiSessionPeerPwwn_Object = MibTableColumn
csiSessionPeerPwwn = _CsiSessionPeerPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 2, 1, 6),
    _CsiSessionPeerPwwn_Type()
)
csiSessionPeerPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionPeerPwwn.setStatus("current")
_CsiSessionPeerNwwn_Type = FcNameId
_CsiSessionPeerNwwn_Object = MibTableColumn
csiSessionPeerNwwn = _CsiSessionPeerNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 2, 1, 7),
    _CsiSessionPeerNwwn_Type()
)
csiSessionPeerNwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionPeerNwwn.setStatus("current")


class _CsiSessionPeerFcid_Type(Integer32):
    """Custom type csiSessionPeerFcid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_CsiSessionPeerFcid_Type.__name__ = "Integer32"
_CsiSessionPeerFcid_Object = MibTableColumn
csiSessionPeerFcid = _CsiSessionPeerFcid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 2, 1, 8),
    _CsiSessionPeerFcid_Type()
)
csiSessionPeerFcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionPeerFcid.setStatus("current")
_CsiInterfaceStatsTable_Object = MibTable
csiInterfaceStatsTable = _CsiInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 3)
)
if mibBuilder.loadTexts:
    csiInterfaceStatsTable.setStatus("current")
_CsiInterfaceStatsEntry_Object = MibTableRow
csiInterfaceStatsEntry = _CsiInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 3, 1)
)
csiInterfaceStatsEntry.setIndexNames(
    (0, "CISCO-SVC-INTERFACE-MIB", "csiNportIfIndex"),
)
if mibBuilder.loadTexts:
    csiInterfaceStatsEntry.setStatus("current")
_CsiInterfaceInFrames_Type = Counter32
_CsiInterfaceInFrames_Object = MibTableColumn
csiInterfaceInFrames = _CsiInterfaceInFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 3, 1, 1),
    _CsiInterfaceInFrames_Type()
)
csiInterfaceInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiInterfaceInFrames.setStatus("current")
_CsiInterfaceInFrameRate_Type = Unsigned32
_CsiInterfaceInFrameRate_Object = MibTableColumn
csiInterfaceInFrameRate = _CsiInterfaceInFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 3, 1, 2),
    _CsiInterfaceInFrameRate_Type()
)
csiInterfaceInFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiInterfaceInFrameRate.setStatus("current")
_CsiInterfaceInBytes_Type = Counter32
_CsiInterfaceInBytes_Object = MibTableColumn
csiInterfaceInBytes = _CsiInterfaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 3, 1, 3),
    _CsiInterfaceInBytes_Type()
)
csiInterfaceInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiInterfaceInBytes.setStatus("current")
_CsiInterfaceInBytesRate_Type = Unsigned32
_CsiInterfaceInBytesRate_Object = MibTableColumn
csiInterfaceInBytesRate = _CsiInterfaceInBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 3, 1, 4),
    _CsiInterfaceInBytesRate_Type()
)
csiInterfaceInBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiInterfaceInBytesRate.setStatus("current")
_CsiInterfaceOutFrames_Type = Counter32
_CsiInterfaceOutFrames_Object = MibTableColumn
csiInterfaceOutFrames = _CsiInterfaceOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 3, 1, 5),
    _CsiInterfaceOutFrames_Type()
)
csiInterfaceOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiInterfaceOutFrames.setStatus("current")
_CsiInterfaceOutFrameRate_Type = Unsigned32
_CsiInterfaceOutFrameRate_Object = MibTableColumn
csiInterfaceOutFrameRate = _CsiInterfaceOutFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 3, 1, 6),
    _CsiInterfaceOutFrameRate_Type()
)
csiInterfaceOutFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiInterfaceOutFrameRate.setStatus("current")
_CsiInterfaceOutBytes_Type = Counter32
_CsiInterfaceOutBytes_Object = MibTableColumn
csiInterfaceOutBytes = _CsiInterfaceOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 3, 1, 7),
    _CsiInterfaceOutBytes_Type()
)
csiInterfaceOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiInterfaceOutBytes.setStatus("current")
_CsiInterfaceOutBytesRate_Type = Unsigned32
_CsiInterfaceOutBytesRate_Object = MibTableColumn
csiInterfaceOutBytesRate = _CsiInterfaceOutBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 3, 1, 8),
    _CsiInterfaceOutBytesRate_Type()
)
csiInterfaceOutBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiInterfaceOutBytesRate.setStatus("current")
_CsiNportStatsTable_Object = MibTable
csiNportStatsTable = _CsiNportStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4)
)
if mibBuilder.loadTexts:
    csiNportStatsTable.setStatus("current")
_CsiNportStatsEntry_Object = MibTableRow
csiNportStatsEntry = _CsiNportStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4, 1)
)
csiNportStatsEntry.setIndexNames(
    (0, "CISCO-SVC-INTERFACE-MIB", "csiNportIfIndex"),
    (0, "CISCO-SVC-INTERFACE-MIB", "csiNportType"),
    (0, "CISCO-SVC-INTERFACE-MIB", "csiNportVsanId"),
)
if mibBuilder.loadTexts:
    csiNportStatsEntry.setStatus("current")
_CsiNportSessions_Type = Counter32
_CsiNportSessions_Object = MibTableColumn
csiNportSessions = _CsiNportSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4, 1, 1),
    _CsiNportSessions_Type()
)
csiNportSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportSessions.setStatus("current")
_CsiNportInFrames_Type = Counter32
_CsiNportInFrames_Object = MibTableColumn
csiNportInFrames = _CsiNportInFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4, 1, 2),
    _CsiNportInFrames_Type()
)
csiNportInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportInFrames.setStatus("current")
_CsiNportInFrameRate_Type = Unsigned32
_CsiNportInFrameRate_Object = MibTableColumn
csiNportInFrameRate = _CsiNportInFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4, 1, 3),
    _CsiNportInFrameRate_Type()
)
csiNportInFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportInFrameRate.setStatus("current")
_CsiNportInBytes_Type = Counter32
_CsiNportInBytes_Object = MibTableColumn
csiNportInBytes = _CsiNportInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4, 1, 4),
    _CsiNportInBytes_Type()
)
csiNportInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportInBytes.setStatus("current")
_CsiNportInBytesRate_Type = Unsigned32
_CsiNportInBytesRate_Object = MibTableColumn
csiNportInBytesRate = _CsiNportInBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4, 1, 5),
    _CsiNportInBytesRate_Type()
)
csiNportInBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportInBytesRate.setStatus("current")
_CsiNportOutFrames_Type = Counter32
_CsiNportOutFrames_Object = MibTableColumn
csiNportOutFrames = _CsiNportOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4, 1, 6),
    _CsiNportOutFrames_Type()
)
csiNportOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportOutFrames.setStatus("current")
_CsiNportOutFrameRate_Type = Unsigned32
_CsiNportOutFrameRate_Object = MibTableColumn
csiNportOutFrameRate = _CsiNportOutFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4, 1, 7),
    _CsiNportOutFrameRate_Type()
)
csiNportOutFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportOutFrameRate.setStatus("current")
_CsiNportOutBytes_Type = Counter32
_CsiNportOutBytes_Object = MibTableColumn
csiNportOutBytes = _CsiNportOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4, 1, 8),
    _CsiNportOutBytes_Type()
)
csiNportOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportOutBytes.setStatus("current")
_CsiNportOutBytesRate_Type = Unsigned32
_CsiNportOutBytesRate_Object = MibTableColumn
csiNportOutBytesRate = _CsiNportOutBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 4, 1, 9),
    _CsiNportOutBytesRate_Type()
)
csiNportOutBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNportOutBytesRate.setStatus("current")
_CsiSessionStatsTable_Object = MibTable
csiSessionStatsTable = _CsiSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5)
)
if mibBuilder.loadTexts:
    csiSessionStatsTable.setStatus("current")
_CsiSessionStatsEntry_Object = MibTableRow
csiSessionStatsEntry = _CsiSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1)
)
csiSessionStatsEntry.setIndexNames(
    (0, "CISCO-SVC-INTERFACE-MIB", "csiSessionIfIndex"),
    (0, "CISCO-SVC-INTERFACE-MIB", "csiSessionType"),
    (0, "CISCO-SVC-INTERFACE-MIB", "csiSessionVsanId"),
    (0, "CISCO-SVC-INTERFACE-MIB", "csiSessionId"),
)
if mibBuilder.loadTexts:
    csiSessionStatsEntry.setStatus("current")
_CsiSessionInELSFrames_Type = Counter32
_CsiSessionInELSFrames_Object = MibTableColumn
csiSessionInELSFrames = _CsiSessionInELSFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 1),
    _CsiSessionInELSFrames_Type()
)
csiSessionInELSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInELSFrames.setStatus("current")
_CsiSessionInBLSFrames_Type = Counter32
_CsiSessionInBLSFrames_Object = MibTableColumn
csiSessionInBLSFrames = _CsiSessionInBLSFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 2),
    _CsiSessionInBLSFrames_Type()
)
csiSessionInBLSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInBLSFrames.setStatus("current")
_CsiSessionInFCPCmds_Type = Counter32
_CsiSessionInFCPCmds_Object = MibTableColumn
csiSessionInFCPCmds = _CsiSessionInFCPCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 3),
    _CsiSessionInFCPCmds_Type()
)
csiSessionInFCPCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInFCPCmds.setStatus("current")
_CsiSessionInFCPXferRdys_Type = Counter32
_CsiSessionInFCPXferRdys_Object = MibTableColumn
csiSessionInFCPXferRdys = _CsiSessionInFCPXferRdys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 4),
    _CsiSessionInFCPXferRdys_Type()
)
csiSessionInFCPXferRdys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInFCPXferRdys.setStatus("current")
_CsiSessionInFCPDataFrames_Type = Counter32
_CsiSessionInFCPDataFrames_Object = MibTableColumn
csiSessionInFCPDataFrames = _CsiSessionInFCPDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 5),
    _CsiSessionInFCPDataFrames_Type()
)
csiSessionInFCPDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInFCPDataFrames.setStatus("current")
_CsiSessionInFCPStatus_Type = Counter32
_CsiSessionInFCPStatus_Object = MibTableColumn
csiSessionInFCPStatus = _CsiSessionInFCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 6),
    _CsiSessionInFCPStatus_Type()
)
csiSessionInFCPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInFCPStatus.setStatus("current")
_CsiSessionInFCPDataBytes_Type = Counter32
_CsiSessionInFCPDataBytes_Object = MibTableColumn
csiSessionInFCPDataBytes = _CsiSessionInFCPDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 7),
    _CsiSessionInFCPDataBytes_Type()
)
csiSessionInFCPDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInFCPDataBytes.setStatus("current")
_CsiSessionInFCPOverRuns_Type = Counter32
_CsiSessionInFCPOverRuns_Object = MibTableColumn
csiSessionInFCPOverRuns = _CsiSessionInFCPOverRuns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 8),
    _CsiSessionInFCPOverRuns_Type()
)
csiSessionInFCPOverRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInFCPOverRuns.setStatus("current")
_CsiSessionInFCPUnderRuns_Type = Counter32
_CsiSessionInFCPUnderRuns_Object = MibTableColumn
csiSessionInFCPUnderRuns = _CsiSessionInFCPUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 9),
    _CsiSessionInFCPUnderRuns_Type()
)
csiSessionInFCPUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInFCPUnderRuns.setStatus("current")
_CsiSessionInAborts_Type = Counter32
_CsiSessionInAborts_Object = MibTableColumn
csiSessionInAborts = _CsiSessionInAborts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 10),
    _CsiSessionInAborts_Type()
)
csiSessionInAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInAborts.setStatus("current")
_CsiSessionOutELSFrames_Type = Counter32
_CsiSessionOutELSFrames_Object = MibTableColumn
csiSessionOutELSFrames = _CsiSessionOutELSFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 11),
    _CsiSessionOutELSFrames_Type()
)
csiSessionOutELSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOutELSFrames.setStatus("current")
_CsiSessionOutBLSFrames_Type = Counter32
_CsiSessionOutBLSFrames_Object = MibTableColumn
csiSessionOutBLSFrames = _CsiSessionOutBLSFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 12),
    _CsiSessionOutBLSFrames_Type()
)
csiSessionOutBLSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOutBLSFrames.setStatus("current")
_CsiSessionOutFCPCmds_Type = Counter32
_CsiSessionOutFCPCmds_Object = MibTableColumn
csiSessionOutFCPCmds = _CsiSessionOutFCPCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 13),
    _CsiSessionOutFCPCmds_Type()
)
csiSessionOutFCPCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOutFCPCmds.setStatus("current")
_CsiSessionOutFCPXferRdys_Type = Counter32
_CsiSessionOutFCPXferRdys_Object = MibTableColumn
csiSessionOutFCPXferRdys = _CsiSessionOutFCPXferRdys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 14),
    _CsiSessionOutFCPXferRdys_Type()
)
csiSessionOutFCPXferRdys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOutFCPXferRdys.setStatus("current")
_CsiSessionOutFCPDataFrames_Type = Counter32
_CsiSessionOutFCPDataFrames_Object = MibTableColumn
csiSessionOutFCPDataFrames = _CsiSessionOutFCPDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 15),
    _CsiSessionOutFCPDataFrames_Type()
)
csiSessionOutFCPDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOutFCPDataFrames.setStatus("current")
_CsiSessionOutFCPStatus_Type = Counter32
_CsiSessionOutFCPStatus_Object = MibTableColumn
csiSessionOutFCPStatus = _CsiSessionOutFCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 16),
    _CsiSessionOutFCPStatus_Type()
)
csiSessionOutFCPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOutFCPStatus.setStatus("current")
_CsiSessionOutFCPDataBytes_Type = Counter32
_CsiSessionOutFCPDataBytes_Object = MibTableColumn
csiSessionOutFCPDataBytes = _CsiSessionOutFCPDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 17),
    _CsiSessionOutFCPDataBytes_Type()
)
csiSessionOutFCPDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOutFCPDataBytes.setStatus("current")
_CsiSessionOutFCPOverRuns_Type = Counter32
_CsiSessionOutFCPOverRuns_Object = MibTableColumn
csiSessionOutFCPOverRuns = _CsiSessionOutFCPOverRuns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 18),
    _CsiSessionOutFCPOverRuns_Type()
)
csiSessionOutFCPOverRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOutFCPOverRuns.setStatus("current")
_CsiSessionOutFCPUnderRuns_Type = Counter32
_CsiSessionOutFCPUnderRuns_Object = MibTableColumn
csiSessionOutFCPUnderRuns = _CsiSessionOutFCPUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 19),
    _CsiSessionOutFCPUnderRuns_Type()
)
csiSessionOutFCPUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOutFCPUnderRuns.setStatus("current")
_CsiSessionOutAborts_Type = Counter32
_CsiSessionOutAborts_Object = MibTableColumn
csiSessionOutAborts = _CsiSessionOutAborts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 20),
    _CsiSessionOutAborts_Type()
)
csiSessionOutAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOutAborts.setStatus("current")
_CsiSessionOpenXchanges_Type = Counter32
_CsiSessionOpenXchanges_Object = MibTableColumn
csiSessionOpenXchanges = _CsiSessionOpenXchanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 21),
    _CsiSessionOpenXchanges_Type()
)
csiSessionOpenXchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionOpenXchanges.setStatus("current")
_CsiSessionInBadFc2Drops_Type = Counter32
_CsiSessionInBadFc2Drops_Object = MibTableColumn
csiSessionInBadFc2Drops = _CsiSessionInBadFc2Drops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 22),
    _CsiSessionInBadFc2Drops_Type()
)
csiSessionInBadFc2Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInBadFc2Drops.setStatus("current")
_CsiSessionInBadFcPDrops_Type = Counter32
_CsiSessionInBadFcPDrops_Object = MibTableColumn
csiSessionInBadFcPDrops = _CsiSessionInBadFcPDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 23),
    _CsiSessionInBadFcPDrops_Type()
)
csiSessionInBadFcPDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInBadFcPDrops.setStatus("current")
_CsiSessionInFCPDataExcess_Type = Counter32
_CsiSessionInFCPDataExcess_Object = MibTableColumn
csiSessionInFCPDataExcess = _CsiSessionInFCPDataExcess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 5, 1, 24),
    _CsiSessionInFCPDataExcess_Type()
)
csiSessionInFCPDataExcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiSessionInFCPDataExcess.setStatus("current")
_CsiInterfaceNwwnTable_Object = MibTable
csiInterfaceNwwnTable = _CsiInterfaceNwwnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 6)
)
if mibBuilder.loadTexts:
    csiInterfaceNwwnTable.setStatus("current")
_CsiInterfaceNwwnEntry_Object = MibTableRow
csiInterfaceNwwnEntry = _CsiInterfaceNwwnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 6, 1)
)
csiInterfaceNwwnEntry.setIndexNames(
    (0, "CISCO-SVC-INTERFACE-MIB", "csiNportIfIndex"),
)
if mibBuilder.loadTexts:
    csiInterfaceNwwnEntry.setStatus("current")
_CsiInterfaceNwwn_Type = FcNameId
_CsiInterfaceNwwn_Object = MibTableColumn
csiInterfaceNwwn = _CsiInterfaceNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 6, 1, 1),
    _CsiInterfaceNwwn_Type()
)
csiInterfaceNwwn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiInterfaceNwwn.setStatus("current")


class _CsiInterfaceOperStateCause_Type(SnmpAdminString):
    """Custom type csiInterfaceOperStateCause based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CsiInterfaceOperStateCause_Type.__name__ = "SnmpAdminString"
_CsiInterfaceOperStateCause_Object = MibTableColumn
csiInterfaceOperStateCause = _CsiInterfaceOperStateCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 1, 6, 1, 2),
    _CsiInterfaceOperStateCause_Type()
)
csiInterfaceOperStateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiInterfaceOperStateCause.setStatus("current")
_CSvcInterfaceTrapObjects_ObjectIdentity = ObjectIdentity
cSvcInterfaceTrapObjects = _CSvcInterfaceTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2)
)


class _CsiErrorId_Type(Integer32):
    """Custom type csiErrorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CsiErrorId_Type.__name__ = "Integer32"
_CsiErrorId_Object = MibScalar
csiErrorId = _CsiErrorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 1),
    _CsiErrorId_Type()
)
csiErrorId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiErrorId.setStatus("current")


class _CsiErrorSeqNumber_Type(Integer32):
    """Custom type csiErrorSeqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CsiErrorSeqNumber_Type.__name__ = "Integer32"
_CsiErrorSeqNumber_Object = MibScalar
csiErrorSeqNumber = _CsiErrorSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 2),
    _CsiErrorSeqNumber_Type()
)
csiErrorSeqNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiErrorSeqNumber.setStatus("current")


class _CsiSlotNumber_Type(Integer32):
    """Custom type csiSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CsiSlotNumber_Type.__name__ = "Integer32"
_CsiSlotNumber_Object = MibScalar
csiSlotNumber = _CsiSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 3),
    _CsiSlotNumber_Type()
)
csiSlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiSlotNumber.setStatus("current")


class _CsiPortNumber_Type(Integer32):
    """Custom type csiPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CsiPortNumber_Type.__name__ = "Integer32"
_CsiPortNumber_Object = MibScalar
csiPortNumber = _CsiPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 4),
    _CsiPortNumber_Type()
)
csiPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiPortNumber.setStatus("current")
_CsiObjName_Type = SnmpAdminString
_CsiObjName_Object = MibScalar
csiObjName = _CsiObjName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 5),
    _CsiObjName_Type()
)
csiObjName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiObjName.setStatus("current")
_CsiErrorText_Type = SnmpAdminString
_CsiErrorText_Object = MibScalar
csiErrorText = _CsiErrorText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 6),
    _CsiErrorText_Type()
)
csiErrorText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiErrorText.setStatus("current")
_CsiMachineType_Type = SnmpAdminString
_CsiMachineType_Object = MibScalar
csiMachineType = _CsiMachineType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 7),
    _CsiMachineType_Type()
)
csiMachineType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiMachineType.setStatus("current")
_CsiCardSerialNo_Type = SnmpAdminString
_CsiCardSerialNo_Object = MibScalar
csiCardSerialNo = _CsiCardSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 8),
    _CsiCardSerialNo_Type()
)
csiCardSerialNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiCardSerialNo.setStatus("current")
_CsiSwVersion_Type = SnmpAdminString
_CsiSwVersion_Object = MibScalar
csiSwVersion = _CsiSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 9),
    _CsiSwVersion_Type()
)
csiSwVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiSwVersion.setStatus("current")
_CsiSwitchName_Type = SnmpAdminString
_CsiSwitchName_Object = MibScalar
csiSwitchName = _CsiSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 10),
    _CsiSwitchName_Type()
)
csiSwitchName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiSwitchName.setStatus("current")
_CsiClusterName_Type = SnmpAdminString
_CsiClusterName_Object = MibScalar
csiClusterName = _CsiClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 11),
    _CsiClusterName_Type()
)
csiClusterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiClusterName.setStatus("current")
_CsiNodeName_Type = SnmpAdminString
_CsiNodeName_Object = MibScalar
csiNodeName = _CsiNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 1, 2, 12),
    _CsiNodeName_Type()
)
csiNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csiNodeName.setStatus("current")
_CiscoSvcInterfaceMIBTrapPrefix_ObjectIdentity = ObjectIdentity
ciscoSvcInterfaceMIBTrapPrefix = _CiscoSvcInterfaceMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 2)
)
_CsiMIBTraps_ObjectIdentity = ObjectIdentity
csiMIBTraps = _CsiMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 2, 0)
)
_CiscoSvcMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSvcMIBConformance = _CiscoSvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3)
)
_CiscoSvcMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSvcMIBCompliances = _CiscoSvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 1)
)
_CiscoSvcMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSvcMIBGroups = _CiscoSvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 2)
)

# Managed Objects groups

csiNportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 2, 1)
)
csiNportGroup.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiNportPwwn"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportFcid"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportState"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportDownReason"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportRowStatus"))
)
if mibBuilder.loadTexts:
    csiNportGroup.setStatus("current")

csiSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 2, 2)
)
csiSessionGroup.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiSessionNportPwwn"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionPeerPwwn"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionPeerNwwn"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionPeerFcid"))
)
if mibBuilder.loadTexts:
    csiSessionGroup.setStatus("current")

csiInterfaceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 2, 3)
)
csiInterfaceStatsGroup.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiInterfaceInFrames"),
        ("CISCO-SVC-INTERFACE-MIB", "csiInterfaceInFrameRate"),
        ("CISCO-SVC-INTERFACE-MIB", "csiInterfaceInBytes"),
        ("CISCO-SVC-INTERFACE-MIB", "csiInterfaceInBytesRate"),
        ("CISCO-SVC-INTERFACE-MIB", "csiInterfaceOutFrames"),
        ("CISCO-SVC-INTERFACE-MIB", "csiInterfaceOutFrameRate"),
        ("CISCO-SVC-INTERFACE-MIB", "csiInterfaceOutBytes"),
        ("CISCO-SVC-INTERFACE-MIB", "csiInterfaceOutBytesRate"))
)
if mibBuilder.loadTexts:
    csiInterfaceStatsGroup.setStatus("current")

csiNportStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 2, 4)
)
csiNportStatsGroup.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiNportSessions"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportInFrames"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportInFrameRate"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportInBytes"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportInBytesRate"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportOutFrames"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportOutFrameRate"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportOutBytes"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNportOutBytesRate"))
)
if mibBuilder.loadTexts:
    csiNportStatsGroup.setStatus("current")

csiSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 2, 5)
)
csiSessionStatsGroup.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiSessionInELSFrames"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInBLSFrames"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInFCPCmds"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInFCPXferRdys"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInFCPDataFrames"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInFCPStatus"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInFCPDataBytes"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInFCPOverRuns"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInFCPUnderRuns"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInAborts"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOutELSFrames"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOutBLSFrames"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOutFCPCmds"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOutFCPXferRdys"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOutFCPDataFrames"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOutFCPStatus"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOutFCPDataBytes"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOutFCPOverRuns"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOutFCPUnderRuns"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOutAborts"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionOpenXchanges"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInBadFc2Drops"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInBadFcPDrops"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSessionInFCPDataExcess"))
)
if mibBuilder.loadTexts:
    csiSessionStatsGroup.setStatus("current")

csiInterfaceNwwnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 2, 6)
)
csiInterfaceNwwnGroup.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiInterfaceNwwn"),
        ("CISCO-SVC-INTERFACE-MIB", "csiInterfaceOperStateCause"))
)
if mibBuilder.loadTexts:
    csiInterfaceNwwnGroup.setStatus("current")

csiNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 2, 7)
)
csiNotifObjectsGroup.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiErrorId"),
        ("CISCO-SVC-INTERFACE-MIB", "csiErrorSeqNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSlotNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiPortNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiObjName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiErrorText"),
        ("CISCO-SVC-INTERFACE-MIB", "csiMachineType"),
        ("CISCO-SVC-INTERFACE-MIB", "csiCardSerialNo"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSwVersion"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSwitchName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiClusterName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNodeName"))
)
if mibBuilder.loadTexts:
    csiNotifObjectsGroup.setStatus("current")


# Notification objects

csiErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 2, 0, 1)
)
csiErrorTrap.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiErrorId"),
        ("CISCO-SVC-INTERFACE-MIB", "csiErrorSeqNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSlotNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiPortNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiObjName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiErrorText"),
        ("CISCO-SVC-INTERFACE-MIB", "csiMachineType"),
        ("CISCO-SVC-INTERFACE-MIB", "csiCardSerialNo"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSwVersion"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSwitchName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiClusterName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNodeName"))
)
if mibBuilder.loadTexts:
    csiErrorTrap.setStatus(
        "current"
    )

csiWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 2, 0, 2)
)
csiWarningTrap.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiErrorId"),
        ("CISCO-SVC-INTERFACE-MIB", "csiErrorSeqNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSlotNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiPortNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiObjName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiErrorText"),
        ("CISCO-SVC-INTERFACE-MIB", "csiMachineType"),
        ("CISCO-SVC-INTERFACE-MIB", "csiCardSerialNo"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSwVersion"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSwitchName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiClusterName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNodeName"))
)
if mibBuilder.loadTexts:
    csiWarningTrap.setStatus(
        "current"
    )

csiInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 2, 0, 3)
)
csiInformationTrap.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiErrorId"),
        ("CISCO-SVC-INTERFACE-MIB", "csiErrorSeqNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSlotNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiPortNumber"),
        ("CISCO-SVC-INTERFACE-MIB", "csiObjName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiErrorText"),
        ("CISCO-SVC-INTERFACE-MIB", "csiMachineType"),
        ("CISCO-SVC-INTERFACE-MIB", "csiCardSerialNo"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSwVersion"),
        ("CISCO-SVC-INTERFACE-MIB", "csiSwitchName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiClusterName"),
        ("CISCO-SVC-INTERFACE-MIB", "csiNodeName"))
)
if mibBuilder.loadTexts:
    csiInformationTrap.setStatus(
        "current"
    )


# Notifications groups

cefcMgmtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 2, 8)
)
cefcMgmtNotificationsGroup.setObjects(
      *(("CISCO-SVC-INTERFACE-MIB", "csiErrorTrap"),
        ("CISCO-SVC-INTERFACE-MIB", "csiWarningTrap"),
        ("CISCO-SVC-INTERFACE-MIB", "csiInformationTrap"))
)
if mibBuilder.loadTexts:
    cefcMgmtNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSvcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 378, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSvcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SVC-INTERFACE-MIB",
    **{"NportType": NportType,
       "ciscoSvcInterfaceMIB": ciscoSvcInterfaceMIB,
       "ciscoSvcInterfaceMIBObjects": ciscoSvcInterfaceMIBObjects,
       "cSvcInterfaceConfiguration": cSvcInterfaceConfiguration,
       "csiNportTable": csiNportTable,
       "csiNportEntry": csiNportEntry,
       "csiNportIfIndex": csiNportIfIndex,
       "csiNportType": csiNportType,
       "csiNportVsanId": csiNportVsanId,
       "csiNportPwwn": csiNportPwwn,
       "csiNportFcid": csiNportFcid,
       "csiNportState": csiNportState,
       "csiNportDownReason": csiNportDownReason,
       "csiNportRowStatus": csiNportRowStatus,
       "csiSessionTable": csiSessionTable,
       "csiSessionEntry": csiSessionEntry,
       "csiSessionIfIndex": csiSessionIfIndex,
       "csiSessionType": csiSessionType,
       "csiSessionVsanId": csiSessionVsanId,
       "csiSessionId": csiSessionId,
       "csiSessionNportPwwn": csiSessionNportPwwn,
       "csiSessionPeerPwwn": csiSessionPeerPwwn,
       "csiSessionPeerNwwn": csiSessionPeerNwwn,
       "csiSessionPeerFcid": csiSessionPeerFcid,
       "csiInterfaceStatsTable": csiInterfaceStatsTable,
       "csiInterfaceStatsEntry": csiInterfaceStatsEntry,
       "csiInterfaceInFrames": csiInterfaceInFrames,
       "csiInterfaceInFrameRate": csiInterfaceInFrameRate,
       "csiInterfaceInBytes": csiInterfaceInBytes,
       "csiInterfaceInBytesRate": csiInterfaceInBytesRate,
       "csiInterfaceOutFrames": csiInterfaceOutFrames,
       "csiInterfaceOutFrameRate": csiInterfaceOutFrameRate,
       "csiInterfaceOutBytes": csiInterfaceOutBytes,
       "csiInterfaceOutBytesRate": csiInterfaceOutBytesRate,
       "csiNportStatsTable": csiNportStatsTable,
       "csiNportStatsEntry": csiNportStatsEntry,
       "csiNportSessions": csiNportSessions,
       "csiNportInFrames": csiNportInFrames,
       "csiNportInFrameRate": csiNportInFrameRate,
       "csiNportInBytes": csiNportInBytes,
       "csiNportInBytesRate": csiNportInBytesRate,
       "csiNportOutFrames": csiNportOutFrames,
       "csiNportOutFrameRate": csiNportOutFrameRate,
       "csiNportOutBytes": csiNportOutBytes,
       "csiNportOutBytesRate": csiNportOutBytesRate,
       "csiSessionStatsTable": csiSessionStatsTable,
       "csiSessionStatsEntry": csiSessionStatsEntry,
       "csiSessionInELSFrames": csiSessionInELSFrames,
       "csiSessionInBLSFrames": csiSessionInBLSFrames,
       "csiSessionInFCPCmds": csiSessionInFCPCmds,
       "csiSessionInFCPXferRdys": csiSessionInFCPXferRdys,
       "csiSessionInFCPDataFrames": csiSessionInFCPDataFrames,
       "csiSessionInFCPStatus": csiSessionInFCPStatus,
       "csiSessionInFCPDataBytes": csiSessionInFCPDataBytes,
       "csiSessionInFCPOverRuns": csiSessionInFCPOverRuns,
       "csiSessionInFCPUnderRuns": csiSessionInFCPUnderRuns,
       "csiSessionInAborts": csiSessionInAborts,
       "csiSessionOutELSFrames": csiSessionOutELSFrames,
       "csiSessionOutBLSFrames": csiSessionOutBLSFrames,
       "csiSessionOutFCPCmds": csiSessionOutFCPCmds,
       "csiSessionOutFCPXferRdys": csiSessionOutFCPXferRdys,
       "csiSessionOutFCPDataFrames": csiSessionOutFCPDataFrames,
       "csiSessionOutFCPStatus": csiSessionOutFCPStatus,
       "csiSessionOutFCPDataBytes": csiSessionOutFCPDataBytes,
       "csiSessionOutFCPOverRuns": csiSessionOutFCPOverRuns,
       "csiSessionOutFCPUnderRuns": csiSessionOutFCPUnderRuns,
       "csiSessionOutAborts": csiSessionOutAborts,
       "csiSessionOpenXchanges": csiSessionOpenXchanges,
       "csiSessionInBadFc2Drops": csiSessionInBadFc2Drops,
       "csiSessionInBadFcPDrops": csiSessionInBadFcPDrops,
       "csiSessionInFCPDataExcess": csiSessionInFCPDataExcess,
       "csiInterfaceNwwnTable": csiInterfaceNwwnTable,
       "csiInterfaceNwwnEntry": csiInterfaceNwwnEntry,
       "csiInterfaceNwwn": csiInterfaceNwwn,
       "csiInterfaceOperStateCause": csiInterfaceOperStateCause,
       "cSvcInterfaceTrapObjects": cSvcInterfaceTrapObjects,
       "csiErrorId": csiErrorId,
       "csiErrorSeqNumber": csiErrorSeqNumber,
       "csiSlotNumber": csiSlotNumber,
       "csiPortNumber": csiPortNumber,
       "csiObjName": csiObjName,
       "csiErrorText": csiErrorText,
       "csiMachineType": csiMachineType,
       "csiCardSerialNo": csiCardSerialNo,
       "csiSwVersion": csiSwVersion,
       "csiSwitchName": csiSwitchName,
       "csiClusterName": csiClusterName,
       "csiNodeName": csiNodeName,
       "ciscoSvcInterfaceMIBTrapPrefix": ciscoSvcInterfaceMIBTrapPrefix,
       "csiMIBTraps": csiMIBTraps,
       "csiErrorTrap": csiErrorTrap,
       "csiWarningTrap": csiWarningTrap,
       "csiInformationTrap": csiInformationTrap,
       "ciscoSvcMIBConformance": ciscoSvcMIBConformance,
       "ciscoSvcMIBCompliances": ciscoSvcMIBCompliances,
       "ciscoSvcMIBCompliance": ciscoSvcMIBCompliance,
       "ciscoSvcMIBGroups": ciscoSvcMIBGroups,
       "csiNportGroup": csiNportGroup,
       "csiSessionGroup": csiSessionGroup,
       "csiInterfaceStatsGroup": csiInterfaceStatsGroup,
       "csiNportStatsGroup": csiNportStatsGroup,
       "csiSessionStatsGroup": csiSessionStatsGroup,
       "csiInterfaceNwwnGroup": csiInterfaceNwwnGroup,
       "csiNotifObjectsGroup": csiNotifObjectsGroup,
       "cefcMgmtNotificationsGroup": cefcMgmtNotificationsGroup}
)
