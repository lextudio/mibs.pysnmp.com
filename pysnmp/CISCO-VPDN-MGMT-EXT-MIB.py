# SNMP MIB module (CISCO-VPDN-MGMT-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VPDN-MGMT-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:34 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(cvpdnSessionAttrEntry,
 cvpdnTunnelAttrEntry) = mibBuilder.importSymbols(
    "CISCO-VPDN-MGMT-MIB",
    "cvpdnSessionAttrEntry",
    "cvpdnTunnelAttrEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVpdnMgmtExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 51)
)
ciscoVpdnMgmtExtMIB.setRevisions(
        ("2011-12-01 00:00",
         "2007-06-04 00:00",
         "1999-04-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVpdnMgmtExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVpdnMgmtExtMIBObjects = _CiscoVpdnMgmtExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1)
)
_CvpdnTunnelExtInfo_ObjectIdentity = ObjectIdentity
cvpdnTunnelExtInfo = _CvpdnTunnelExtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1)
)
_CvpdnTunnelExtTable_Object = MibTable
cvpdnTunnelExtTable = _CvpdnTunnelExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvpdnTunnelExtTable.setStatus("current")
_CvpdnTunnelExtEntry_Object = MibTableRow
cvpdnTunnelExtEntry = _CvpdnTunnelExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvpdnTunnelExtEntry.setStatus("current")


class _CvpdnTunnelLocalPort_Type(Integer32):
    """Custom type cvpdnTunnelLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnTunnelLocalPort_Type.__name__ = "Integer32"
_CvpdnTunnelLocalPort_Object = MibTableColumn
cvpdnTunnelLocalPort = _CvpdnTunnelLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 1),
    _CvpdnTunnelLocalPort_Type()
)
cvpdnTunnelLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelLocalPort.setStatus("current")


class _CvpdnTunnelRemotePort_Type(Integer32):
    """Custom type cvpdnTunnelRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnTunnelRemotePort_Type.__name__ = "Integer32"
_CvpdnTunnelRemotePort_Object = MibTableColumn
cvpdnTunnelRemotePort = _CvpdnTunnelRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 2),
    _CvpdnTunnelRemotePort_Type()
)
cvpdnTunnelRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelRemotePort.setStatus("current")
_CvpdnTunnelLastChange_Type = TimeTicks
_CvpdnTunnelLastChange_Object = MibTableColumn
cvpdnTunnelLastChange = _CvpdnTunnelLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 3),
    _CvpdnTunnelLastChange_Type()
)
cvpdnTunnelLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelLastChange.setStatus("current")
_CvpdnTunnelPacketsOut_Type = Counter32
_CvpdnTunnelPacketsOut_Object = MibTableColumn
cvpdnTunnelPacketsOut = _CvpdnTunnelPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 4),
    _CvpdnTunnelPacketsOut_Type()
)
cvpdnTunnelPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelPacketsOut.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnTunnelPacketsOut.setUnits("packets")
_CvpdnTunnelBytesOut_Type = Counter32
_CvpdnTunnelBytesOut_Object = MibTableColumn
cvpdnTunnelBytesOut = _CvpdnTunnelBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 5),
    _CvpdnTunnelBytesOut_Type()
)
cvpdnTunnelBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelBytesOut.setStatus("deprecated")
if mibBuilder.loadTexts:
    cvpdnTunnelBytesOut.setUnits("bytes")
_CvpdnTunnelPacketsIn_Type = Counter32
_CvpdnTunnelPacketsIn_Object = MibTableColumn
cvpdnTunnelPacketsIn = _CvpdnTunnelPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 6),
    _CvpdnTunnelPacketsIn_Type()
)
cvpdnTunnelPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelPacketsIn.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnTunnelPacketsIn.setUnits("packets")
_CvpdnTunnelBytesIn_Type = Counter32
_CvpdnTunnelBytesIn_Object = MibTableColumn
cvpdnTunnelBytesIn = _CvpdnTunnelBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 7),
    _CvpdnTunnelBytesIn_Type()
)
cvpdnTunnelBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelBytesIn.setStatus("deprecated")
if mibBuilder.loadTexts:
    cvpdnTunnelBytesIn.setUnits("bytes")
_CvpdnTunnelBytesIn64_Type = Counter64
_CvpdnTunnelBytesIn64_Object = MibTableColumn
cvpdnTunnelBytesIn64 = _CvpdnTunnelBytesIn64_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 8),
    _CvpdnTunnelBytesIn64_Type()
)
cvpdnTunnelBytesIn64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelBytesIn64.setStatus("current")
_CvpdnTunnelBytesOut64_Type = Counter64
_CvpdnTunnelBytesOut64_Object = MibTableColumn
cvpdnTunnelBytesOut64 = _CvpdnTunnelBytesOut64_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 1, 1, 1, 9),
    _CvpdnTunnelBytesOut64_Type()
)
cvpdnTunnelBytesOut64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelBytesOut64.setStatus("current")
_CvpdnSessionExtInfo_ObjectIdentity = ObjectIdentity
cvpdnSessionExtInfo = _CvpdnSessionExtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2)
)
_CvpdnSessionExtTable_Object = MibTable
cvpdnSessionExtTable = _CvpdnSessionExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvpdnSessionExtTable.setStatus("current")
_CvpdnSessionExtEntry_Object = MibTableRow
cvpdnSessionExtEntry = _CvpdnSessionExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvpdnSessionExtEntry.setStatus("current")


class _CvpdnSessionRemoteId_Type(Integer32):
    """Custom type cvpdnSessionRemoteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionRemoteId_Type.__name__ = "Integer32"
_CvpdnSessionRemoteId_Object = MibTableColumn
cvpdnSessionRemoteId = _CvpdnSessionRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 1),
    _CvpdnSessionRemoteId_Type()
)
cvpdnSessionRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionRemoteId.setStatus("current")


class _CvpdnSessionInterfaceName_Type(DisplayString):
    """Custom type cvpdnSessionInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnSessionInterfaceName_Type.__name__ = "DisplayString"
_CvpdnSessionInterfaceName_Object = MibTableColumn
cvpdnSessionInterfaceName = _CvpdnSessionInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 2),
    _CvpdnSessionInterfaceName_Type()
)
cvpdnSessionInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionInterfaceName.setStatus("current")
_CvpdnSessionLastChange_Type = TimeTicks
_CvpdnSessionLastChange_Object = MibTableColumn
cvpdnSessionLastChange = _CvpdnSessionLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 3),
    _CvpdnSessionLastChange_Type()
)
cvpdnSessionLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionLastChange.setStatus("current")
_CvpdnSessionOutOfOrderPackets_Type = Counter32
_CvpdnSessionOutOfOrderPackets_Object = MibTableColumn
cvpdnSessionOutOfOrderPackets = _CvpdnSessionOutOfOrderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 4),
    _CvpdnSessionOutOfOrderPackets_Type()
)
cvpdnSessionOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionOutOfOrderPackets.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionOutOfOrderPackets.setUnits("packets")
_CvpdnSessionSequencing_Type = TruthValue
_CvpdnSessionSequencing_Object = MibTableColumn
cvpdnSessionSequencing = _CvpdnSessionSequencing_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 5),
    _CvpdnSessionSequencing_Type()
)
cvpdnSessionSequencing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionSequencing.setStatus("current")


class _CvpdnSessionSendSequence_Type(Integer32):
    """Custom type cvpdnSessionSendSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionSendSequence_Type.__name__ = "Integer32"
_CvpdnSessionSendSequence_Object = MibTableColumn
cvpdnSessionSendSequence = _CvpdnSessionSendSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 6),
    _CvpdnSessionSendSequence_Type()
)
cvpdnSessionSendSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionSendSequence.setStatus("current")


class _CvpdnSessionRecvSequence_Type(Integer32):
    """Custom type cvpdnSessionRecvSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionRecvSequence_Type.__name__ = "Integer32"
_CvpdnSessionRecvSequence_Object = MibTableColumn
cvpdnSessionRecvSequence = _CvpdnSessionRecvSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 7),
    _CvpdnSessionRecvSequence_Type()
)
cvpdnSessionRecvSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionRecvSequence.setStatus("current")


class _CvpdnSessionRemoteSendSequence_Type(Integer32):
    """Custom type cvpdnSessionRemoteSendSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionRemoteSendSequence_Type.__name__ = "Integer32"
_CvpdnSessionRemoteSendSequence_Object = MibTableColumn
cvpdnSessionRemoteSendSequence = _CvpdnSessionRemoteSendSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 8),
    _CvpdnSessionRemoteSendSequence_Type()
)
cvpdnSessionRemoteSendSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionRemoteSendSequence.setStatus("current")


class _CvpdnSessionRemoteRecvSequence_Type(Integer32):
    """Custom type cvpdnSessionRemoteRecvSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionRemoteRecvSequence_Type.__name__ = "Integer32"
_CvpdnSessionRemoteRecvSequence_Object = MibTableColumn
cvpdnSessionRemoteRecvSequence = _CvpdnSessionRemoteRecvSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 9),
    _CvpdnSessionRemoteRecvSequence_Type()
)
cvpdnSessionRemoteRecvSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionRemoteRecvSequence.setStatus("current")
_CvpdnSessionSentZLB_Type = Counter32
_CvpdnSessionSentZLB_Object = MibTableColumn
cvpdnSessionSentZLB = _CvpdnSessionSentZLB_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 10),
    _CvpdnSessionSentZLB_Type()
)
cvpdnSessionSentZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionSentZLB.setStatus("current")
_CvpdnSessionRecvZLB_Type = Counter32
_CvpdnSessionRecvZLB_Object = MibTableColumn
cvpdnSessionRecvZLB = _CvpdnSessionRecvZLB_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 11),
    _CvpdnSessionRecvZLB_Type()
)
cvpdnSessionRecvZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionRecvZLB.setStatus("current")
_CvpdnSessionSentRBits_Type = Counter32
_CvpdnSessionSentRBits_Object = MibTableColumn
cvpdnSessionSentRBits = _CvpdnSessionSentRBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 12),
    _CvpdnSessionSentRBits_Type()
)
cvpdnSessionSentRBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionSentRBits.setStatus("current")
_CvpdnSessionRecvRBits_Type = Counter32
_CvpdnSessionRecvRBits_Object = MibTableColumn
cvpdnSessionRecvRBits = _CvpdnSessionRecvRBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 13),
    _CvpdnSessionRecvRBits_Type()
)
cvpdnSessionRecvRBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionRecvRBits.setStatus("current")


class _CvpdnSessionLocalWindowSize_Type(Integer32):
    """Custom type cvpdnSessionLocalWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionLocalWindowSize_Type.__name__ = "Integer32"
_CvpdnSessionLocalWindowSize_Object = MibTableColumn
cvpdnSessionLocalWindowSize = _CvpdnSessionLocalWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 14),
    _CvpdnSessionLocalWindowSize_Type()
)
cvpdnSessionLocalWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionLocalWindowSize.setStatus("current")


class _CvpdnSessionRemoteWindowSize_Type(Integer32):
    """Custom type cvpdnSessionRemoteWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionRemoteWindowSize_Type.__name__ = "Integer32"
_CvpdnSessionRemoteWindowSize_Object = MibTableColumn
cvpdnSessionRemoteWindowSize = _CvpdnSessionRemoteWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 15),
    _CvpdnSessionRemoteWindowSize_Type()
)
cvpdnSessionRemoteWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionRemoteWindowSize.setStatus("current")


class _CvpdnSessionCurrentWindowSize_Type(Integer32):
    """Custom type cvpdnSessionCurrentWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionCurrentWindowSize_Type.__name__ = "Integer32"
_CvpdnSessionCurrentWindowSize_Object = MibTableColumn
cvpdnSessionCurrentWindowSize = _CvpdnSessionCurrentWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 16),
    _CvpdnSessionCurrentWindowSize_Type()
)
cvpdnSessionCurrentWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionCurrentWindowSize.setStatus("current")


class _CvpdnSessionMinimumWindowSize_Type(Integer32):
    """Custom type cvpdnSessionMinimumWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionMinimumWindowSize_Type.__name__ = "Integer32"
_CvpdnSessionMinimumWindowSize_Object = MibTableColumn
cvpdnSessionMinimumWindowSize = _CvpdnSessionMinimumWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 17),
    _CvpdnSessionMinimumWindowSize_Type()
)
cvpdnSessionMinimumWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionMinimumWindowSize.setStatus("current")


class _CvpdnSessionATOTimeouts_Type(Integer32):
    """Custom type cvpdnSessionATOTimeouts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionATOTimeouts_Type.__name__ = "Integer32"
_CvpdnSessionATOTimeouts_Object = MibTableColumn
cvpdnSessionATOTimeouts = _CvpdnSessionATOTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 18),
    _CvpdnSessionATOTimeouts_Type()
)
cvpdnSessionATOTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionATOTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionATOTimeouts.setUnits("msecs")


class _CvpdnSessionOutGoingQueueSize_Type(Integer32):
    """Custom type cvpdnSessionOutGoingQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionOutGoingQueueSize_Type.__name__ = "Integer32"
_CvpdnSessionOutGoingQueueSize_Object = MibTableColumn
cvpdnSessionOutGoingQueueSize = _CvpdnSessionOutGoingQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 19),
    _CvpdnSessionOutGoingQueueSize_Type()
)
cvpdnSessionOutGoingQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionOutGoingQueueSize.setStatus("current")


class _CvpdnSessionCalculationType_Type(Integer32):
    """Custom type cvpdnSessionCalculationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("manual", 1))
    )


_CvpdnSessionCalculationType_Type.__name__ = "Integer32"
_CvpdnSessionCalculationType_Object = MibTableColumn
cvpdnSessionCalculationType = _CvpdnSessionCalculationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 20),
    _CvpdnSessionCalculationType_Type()
)
cvpdnSessionCalculationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionCalculationType.setStatus("current")


class _CvpdnSessionAdaptiveTimeOut_Type(Integer32):
    """Custom type cvpdnSessionAdaptiveTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionAdaptiveTimeOut_Type.__name__ = "Integer32"
_CvpdnSessionAdaptiveTimeOut_Object = MibTableColumn
cvpdnSessionAdaptiveTimeOut = _CvpdnSessionAdaptiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 21),
    _CvpdnSessionAdaptiveTimeOut_Type()
)
cvpdnSessionAdaptiveTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAdaptiveTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionAdaptiveTimeOut.setUnits("msecs")


class _CvpdnSessionRoundTripTime_Type(Integer32):
    """Custom type cvpdnSessionRoundTripTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionRoundTripTime_Type.__name__ = "Integer32"
_CvpdnSessionRoundTripTime_Object = MibTableColumn
cvpdnSessionRoundTripTime = _CvpdnSessionRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 22),
    _CvpdnSessionRoundTripTime_Type()
)
cvpdnSessionRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionRoundTripTime.setUnits("msecs")


class _CvpdnSessionPktProcessingDelay_Type(Integer32):
    """Custom type cvpdnSessionPktProcessingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionPktProcessingDelay_Type.__name__ = "Integer32"
_CvpdnSessionPktProcessingDelay_Object = MibTableColumn
cvpdnSessionPktProcessingDelay = _CvpdnSessionPktProcessingDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 23),
    _CvpdnSessionPktProcessingDelay_Type()
)
cvpdnSessionPktProcessingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionPktProcessingDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionPktProcessingDelay.setUnits("packets")


class _CvpdnSessionZLBTime_Type(Integer32):
    """Custom type cvpdnSessionZLBTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvpdnSessionZLBTime_Type.__name__ = "Integer32"
_CvpdnSessionZLBTime_Object = MibTableColumn
cvpdnSessionZLBTime = _CvpdnSessionZLBTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 1, 2, 1, 1, 24),
    _CvpdnSessionZLBTime_Type()
)
cvpdnSessionZLBTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionZLBTime.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionZLBTime.setUnits("msecs")
_CiscoVpdnMgtExtMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoVpdnMgtExtMIBNotificationPrefix = _CiscoVpdnMgtExtMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 2)
)
_CiscoVpdnMgmtExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVpdnMgmtExtMIBConformance = _CiscoVpdnMgmtExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 3)
)
_CiscoVpdnMgmtExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVpdnMgmtExtMIBCompliances = _CiscoVpdnMgmtExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 1)
)
_CiscoVpdnMgmtExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVpdnMgmtExtMIBGroups = _CiscoVpdnMgmtExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2)
)
cvpdnTunnelAttrEntry.registerAugmentions(
    ("CISCO-VPDN-MGMT-EXT-MIB",
     "cvpdnTunnelExtEntry")
)
cvpdnTunnelExtEntry.setIndexNames(*cvpdnTunnelAttrEntry.getIndexNames())
cvpdnSessionAttrEntry.registerAugmentions(
    ("CISCO-VPDN-MGMT-EXT-MIB",
     "cvpdnSessionExtEntry")
)
cvpdnSessionExtEntry.setIndexNames(*cvpdnSessionAttrEntry.getIndexNames())

# Managed Objects groups

cvpdnTunnelExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2, 1)
)
cvpdnTunnelExtGroup.setObjects(
      *(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLocalPort"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelRemotePort"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLastChange"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsIn"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsOut"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesIn"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesOut"))
)
if mibBuilder.loadTexts:
    cvpdnTunnelExtGroup.setStatus("deprecated")

cvpdnSessionExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2, 2)
)
cvpdnSessionExtGroup.setObjects(
      *(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteId"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionInterfaceName"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionLastChange"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSequencing"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSendSequence"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRecvSequence"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteSendSequence"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteRecvSequence"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionOutOfOrderPackets"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSentZLB"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRecvZLB"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionSentRBits"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRecvRBits"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionLocalWindowSize"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRemoteWindowSize"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionCurrentWindowSize"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionMinimumWindowSize"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionATOTimeouts"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionOutGoingQueueSize"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionCalculationType"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionAdaptiveTimeOut"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionRoundTripTime"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionPktProcessingDelay"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnSessionZLBTime"))
)
if mibBuilder.loadTexts:
    cvpdnSessionExtGroup.setStatus("current")

cvpdnTunnelExtGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 2, 3)
)
cvpdnTunnelExtGroupV2.setObjects(
      *(("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLocalPort"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelRemotePort"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelLastChange"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsOut"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelPacketsIn"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesIn64"),
        ("CISCO-VPDN-MGMT-EXT-MIB", "cvpdnTunnelBytesOut64"))
)
if mibBuilder.loadTexts:
    cvpdnTunnelExtGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVpdnMgmtExtMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVpdnMgmtExtMIBBasicCompliance.setStatus(
        "deprecated"
    )

ciscoVpdnMgmtExtMIBBasicComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 51, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoVpdnMgmtExtMIBBasicComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VPDN-MGMT-EXT-MIB",
    **{"ciscoVpdnMgmtExtMIB": ciscoVpdnMgmtExtMIB,
       "ciscoVpdnMgmtExtMIBObjects": ciscoVpdnMgmtExtMIBObjects,
       "cvpdnTunnelExtInfo": cvpdnTunnelExtInfo,
       "cvpdnTunnelExtTable": cvpdnTunnelExtTable,
       "cvpdnTunnelExtEntry": cvpdnTunnelExtEntry,
       "cvpdnTunnelLocalPort": cvpdnTunnelLocalPort,
       "cvpdnTunnelRemotePort": cvpdnTunnelRemotePort,
       "cvpdnTunnelLastChange": cvpdnTunnelLastChange,
       "cvpdnTunnelPacketsOut": cvpdnTunnelPacketsOut,
       "cvpdnTunnelBytesOut": cvpdnTunnelBytesOut,
       "cvpdnTunnelPacketsIn": cvpdnTunnelPacketsIn,
       "cvpdnTunnelBytesIn": cvpdnTunnelBytesIn,
       "cvpdnTunnelBytesIn64": cvpdnTunnelBytesIn64,
       "cvpdnTunnelBytesOut64": cvpdnTunnelBytesOut64,
       "cvpdnSessionExtInfo": cvpdnSessionExtInfo,
       "cvpdnSessionExtTable": cvpdnSessionExtTable,
       "cvpdnSessionExtEntry": cvpdnSessionExtEntry,
       "cvpdnSessionRemoteId": cvpdnSessionRemoteId,
       "cvpdnSessionInterfaceName": cvpdnSessionInterfaceName,
       "cvpdnSessionLastChange": cvpdnSessionLastChange,
       "cvpdnSessionOutOfOrderPackets": cvpdnSessionOutOfOrderPackets,
       "cvpdnSessionSequencing": cvpdnSessionSequencing,
       "cvpdnSessionSendSequence": cvpdnSessionSendSequence,
       "cvpdnSessionRecvSequence": cvpdnSessionRecvSequence,
       "cvpdnSessionRemoteSendSequence": cvpdnSessionRemoteSendSequence,
       "cvpdnSessionRemoteRecvSequence": cvpdnSessionRemoteRecvSequence,
       "cvpdnSessionSentZLB": cvpdnSessionSentZLB,
       "cvpdnSessionRecvZLB": cvpdnSessionRecvZLB,
       "cvpdnSessionSentRBits": cvpdnSessionSentRBits,
       "cvpdnSessionRecvRBits": cvpdnSessionRecvRBits,
       "cvpdnSessionLocalWindowSize": cvpdnSessionLocalWindowSize,
       "cvpdnSessionRemoteWindowSize": cvpdnSessionRemoteWindowSize,
       "cvpdnSessionCurrentWindowSize": cvpdnSessionCurrentWindowSize,
       "cvpdnSessionMinimumWindowSize": cvpdnSessionMinimumWindowSize,
       "cvpdnSessionATOTimeouts": cvpdnSessionATOTimeouts,
       "cvpdnSessionOutGoingQueueSize": cvpdnSessionOutGoingQueueSize,
       "cvpdnSessionCalculationType": cvpdnSessionCalculationType,
       "cvpdnSessionAdaptiveTimeOut": cvpdnSessionAdaptiveTimeOut,
       "cvpdnSessionRoundTripTime": cvpdnSessionRoundTripTime,
       "cvpdnSessionPktProcessingDelay": cvpdnSessionPktProcessingDelay,
       "cvpdnSessionZLBTime": cvpdnSessionZLBTime,
       "ciscoVpdnMgtExtMIBNotificationPrefix": ciscoVpdnMgtExtMIBNotificationPrefix,
       "ciscoVpdnMgmtExtMIBConformance": ciscoVpdnMgmtExtMIBConformance,
       "ciscoVpdnMgmtExtMIBCompliances": ciscoVpdnMgmtExtMIBCompliances,
       "ciscoVpdnMgmtExtMIBBasicCompliance": ciscoVpdnMgmtExtMIBBasicCompliance,
       "ciscoVpdnMgmtExtMIBBasicComplianceV2": ciscoVpdnMgmtExtMIBBasicComplianceV2,
       "ciscoVpdnMgmtExtMIBGroups": ciscoVpdnMgmtExtMIBGroups,
       "cvpdnTunnelExtGroup": cvpdnTunnelExtGroup,
       "cvpdnSessionExtGroup": cvpdnSessionExtGroup,
       "cvpdnTunnelExtGroupV2": cvpdnTunnelExtGroupV2}
)
