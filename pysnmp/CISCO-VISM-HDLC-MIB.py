# SNMP MIB module (CISCO-VISM-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:52 2024
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

(voice,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "voice")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoVismHdlcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 91)
)
ciscoVismHdlcMIB.setRevisions(
        ("2003-10-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismSigGrp_ObjectIdentity = ObjectIdentity
vismSigGrp = _VismSigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6)
)
_VismHdlcChanTable_Object = MibTable
vismHdlcChanTable = _VismHdlcChanTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1)
)
if mibBuilder.loadTexts:
    vismHdlcChanTable.setStatus("current")
_VismHdlcChanEntry_Object = MibTableRow
vismHdlcChanEntry = _VismHdlcChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1)
)
vismHdlcChanEntry.setIndexNames(
    (0, "CISCO-VISM-HDLC-MIB", "vismHdlcChanNum"),
)
if mibBuilder.loadTexts:
    vismHdlcChanEntry.setStatus("current")


class _VismHdlcChanNum_Type(Integer32):
    """Custom type vismHdlcChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_VismHdlcChanNum_Type.__name__ = "Integer32"
_VismHdlcChanNum_Object = MibTableColumn
vismHdlcChanNum = _VismHdlcChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 1),
    _VismHdlcChanNum_Type()
)
vismHdlcChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismHdlcChanNum.setStatus("current")
_VismHdlcRowStatus_Type = RowStatus
_VismHdlcRowStatus_Object = MibTableColumn
vismHdlcRowStatus = _VismHdlcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 2),
    _VismHdlcRowStatus_Type()
)
vismHdlcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismHdlcRowStatus.setStatus("current")


class _VismHdlcMaxFrameSize_Type(Integer32):
    """Custom type vismHdlcMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismHdlcMaxFrameSize_Type.__name__ = "Integer32"
_VismHdlcMaxFrameSize_Object = MibTableColumn
vismHdlcMaxFrameSize = _VismHdlcMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 3),
    _VismHdlcMaxFrameSize_Type()
)
vismHdlcMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismHdlcMaxFrameSize.setStatus("deprecated")


class _VismHdlcLcnNum_Type(Integer32):
    """Custom type vismHdlcLcnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_VismHdlcLcnNum_Type.__name__ = "Integer32"
_VismHdlcLcnNum_Object = MibTableColumn
vismHdlcLcnNum = _VismHdlcLcnNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 4),
    _VismHdlcLcnNum_Type()
)
vismHdlcLcnNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismHdlcLcnNum.setStatus("current")
_VismHdlcXmtFrames_Type = Counter32
_VismHdlcXmtFrames_Object = MibTableColumn
vismHdlcXmtFrames = _VismHdlcXmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 5),
    _VismHdlcXmtFrames_Type()
)
vismHdlcXmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismHdlcXmtFrames.setStatus("current")
_VismHdlcRcvFrames_Type = Counter32
_VismHdlcRcvFrames_Object = MibTableColumn
vismHdlcRcvFrames = _VismHdlcRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 6),
    _VismHdlcRcvFrames_Type()
)
vismHdlcRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismHdlcRcvFrames.setStatus("current")
_VismHdlcRcvCrcErrors_Type = Counter32
_VismHdlcRcvCrcErrors_Object = MibTableColumn
vismHdlcRcvCrcErrors = _VismHdlcRcvCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 7),
    _VismHdlcRcvCrcErrors_Type()
)
vismHdlcRcvCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismHdlcRcvCrcErrors.setStatus("current")
_VismHdlcRcvBufOverflows_Type = Counter32
_VismHdlcRcvBufOverflows_Object = MibTableColumn
vismHdlcRcvBufOverflows = _VismHdlcRcvBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 8),
    _VismHdlcRcvBufOverflows_Type()
)
vismHdlcRcvBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismHdlcRcvBufOverflows.setStatus("current")
_VismHdlcTxUnderflows_Type = Counter32
_VismHdlcTxUnderflows_Object = MibTableColumn
vismHdlcTxUnderflows = _VismHdlcTxUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 9),
    _VismHdlcTxUnderflows_Type()
)
vismHdlcTxUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismHdlcTxUnderflows.setStatus("current")
_VismHdlcTxAbortFrames_Type = Counter32
_VismHdlcTxAbortFrames_Object = MibTableColumn
vismHdlcTxAbortFrames = _VismHdlcTxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 10),
    _VismHdlcTxAbortFrames_Type()
)
vismHdlcTxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismHdlcTxAbortFrames.setStatus("current")
_VismHdlcRxAbortFrames_Type = Counter32
_VismHdlcRxAbortFrames_Object = MibTableColumn
vismHdlcRxAbortFrames = _VismHdlcRxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 6, 1, 1, 11),
    _VismHdlcRxAbortFrames_Type()
)
vismHdlcRxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismHdlcRxAbortFrames.setStatus("current")
_CiscoVismHdlcMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismHdlcMIBConformance = _CiscoVismHdlcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 91, 2)
)
_CiscoVismHdlcMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismHdlcMIBGroups = _CiscoVismHdlcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 91, 2, 1)
)
_CiscoVismHdlcMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismHdlcMIBCompliances = _CiscoVismHdlcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 91, 2, 2)
)

# Managed Objects groups

ciscoVismHdlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 91, 2, 1, 1)
)
ciscoVismHdlcGroup.setObjects(
      *(("CISCO-VISM-HDLC-MIB", "vismHdlcChanNum"),
        ("CISCO-VISM-HDLC-MIB", "vismHdlcRowStatus"),
        ("CISCO-VISM-HDLC-MIB", "vismHdlcLcnNum"),
        ("CISCO-VISM-HDLC-MIB", "vismHdlcXmtFrames"),
        ("CISCO-VISM-HDLC-MIB", "vismHdlcRcvFrames"),
        ("CISCO-VISM-HDLC-MIB", "vismHdlcRcvCrcErrors"),
        ("CISCO-VISM-HDLC-MIB", "vismHdlcRcvBufOverflows"),
        ("CISCO-VISM-HDLC-MIB", "vismHdlcTxUnderflows"),
        ("CISCO-VISM-HDLC-MIB", "vismHdlcTxAbortFrames"),
        ("CISCO-VISM-HDLC-MIB", "vismHdlcRxAbortFrames"))
)
if mibBuilder.loadTexts:
    ciscoVismHdlcGroup.setStatus("current")

ciscoVismHdlcDeprecateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 91, 2, 1, 2)
)
ciscoVismHdlcDeprecateGroup.setObjects(
    ("CISCO-VISM-HDLC-MIB", "vismHdlcMaxFrameSize")
)
if mibBuilder.loadTexts:
    ciscoVismHdlcDeprecateGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismHdlcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 91, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismHdlcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-HDLC-MIB",
    **{"vismSigGrp": vismSigGrp,
       "vismHdlcChanTable": vismHdlcChanTable,
       "vismHdlcChanEntry": vismHdlcChanEntry,
       "vismHdlcChanNum": vismHdlcChanNum,
       "vismHdlcRowStatus": vismHdlcRowStatus,
       "vismHdlcMaxFrameSize": vismHdlcMaxFrameSize,
       "vismHdlcLcnNum": vismHdlcLcnNum,
       "vismHdlcXmtFrames": vismHdlcXmtFrames,
       "vismHdlcRcvFrames": vismHdlcRcvFrames,
       "vismHdlcRcvCrcErrors": vismHdlcRcvCrcErrors,
       "vismHdlcRcvBufOverflows": vismHdlcRcvBufOverflows,
       "vismHdlcTxUnderflows": vismHdlcTxUnderflows,
       "vismHdlcTxAbortFrames": vismHdlcTxAbortFrames,
       "vismHdlcRxAbortFrames": vismHdlcRxAbortFrames,
       "ciscoVismHdlcMIB": ciscoVismHdlcMIB,
       "ciscoVismHdlcMIBConformance": ciscoVismHdlcMIBConformance,
       "ciscoVismHdlcMIBGroups": ciscoVismHdlcMIBGroups,
       "ciscoVismHdlcGroup": ciscoVismHdlcGroup,
       "ciscoVismHdlcDeprecateGroup": ciscoVismHdlcDeprecateGroup,
       "ciscoVismHdlcMIBCompliances": ciscoVismHdlcMIBCompliances,
       "ciscoVismHdlcCompliance": ciscoVismHdlcCompliance}
)
