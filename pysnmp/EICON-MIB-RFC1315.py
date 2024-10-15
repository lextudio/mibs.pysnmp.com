# SNMP MIB module (EICON-MIB-RFC1315) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EICON-MIB-RFC1315
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:45 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Index(Integer32):
    """Custom type Index based on Integer32"""




class DLCI(Integer32):
    """Custom type DLCI based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eicon_ObjectIdentity = ObjectIdentity
eicon = _Eicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2)
)
_Mibv2_ObjectIdentity = ObjectIdentity
mibv2 = _Mibv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2)
)
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4)
)
_Frame_relay_ObjectIdentity = ObjectIdentity
frame_relay = _Frame_relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32)
)
_FrDlcmiTable_Object = MibTable
frDlcmiTable = _FrDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1)
)
if mibBuilder.loadTexts:
    frDlcmiTable.setStatus("mandatory")
_FrDlcmiEntry_Object = MibTableRow
frDlcmiEntry = _FrDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1)
)
frDlcmiEntry.setIndexNames(
    (0, "EICON-MIB-RFC1315", "frDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    frDlcmiEntry.setStatus("mandatory")
_FrDlcmiIfIndex_Type = Index
_FrDlcmiIfIndex_Object = MibTableColumn
frDlcmiIfIndex = _FrDlcmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1, 1),
    _FrDlcmiIfIndex_Type()
)
frDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDlcmiIfIndex.setStatus("mandatory")


class _FrDlcmiState_Type(Integer32):
    """Custom type frDlcmiState based on Integer32"""
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
        *(("ansiT1-617-B", 4),
          ("ansiT1-617-D", 3),
          ("lmiRev1", 2),
          ("noLmiConfigured", 1))
    )


_FrDlcmiState_Type.__name__ = "Integer32"
_FrDlcmiState_Object = MibTableColumn
frDlcmiState = _FrDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1, 2),
    _FrDlcmiState_Type()
)
frDlcmiState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiState.setStatus("mandatory")


class _FrDlcmiAddress_Type(Integer32):
    """Custom type frDlcmiAddress based on Integer32"""
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
        *(("q921", 1),
          ("q922", 4),
          ("q922March90", 2),
          ("q922November90", 3))
    )


_FrDlcmiAddress_Type.__name__ = "Integer32"
_FrDlcmiAddress_Object = MibTableColumn
frDlcmiAddress = _FrDlcmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1, 3),
    _FrDlcmiAddress_Type()
)
frDlcmiAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiAddress.setStatus("mandatory")


class _FrDlcmiAddressLen_Type(Integer32):
    """Custom type frDlcmiAddressLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("four-octets", 4),
          ("three-octets", 3),
          ("two-octets", 2))
    )


_FrDlcmiAddressLen_Type.__name__ = "Integer32"
_FrDlcmiAddressLen_Object = MibTableColumn
frDlcmiAddressLen = _FrDlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1, 4),
    _FrDlcmiAddressLen_Type()
)
frDlcmiAddressLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiAddressLen.setStatus("mandatory")


class _FrDlcmiPollingInterval_Type(Integer32):
    """Custom type frDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrDlcmiPollingInterval_Type.__name__ = "Integer32"
_FrDlcmiPollingInterval_Object = MibTableColumn
frDlcmiPollingInterval = _FrDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1, 5),
    _FrDlcmiPollingInterval_Type()
)
frDlcmiPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiPollingInterval.setStatus("mandatory")


class _FrDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type frDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_FrDlcmiFullEnquiryInterval_Object = MibTableColumn
frDlcmiFullEnquiryInterval = _FrDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1, 6),
    _FrDlcmiFullEnquiryInterval_Type()
)
frDlcmiFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiFullEnquiryInterval.setStatus("mandatory")


class _FrDlcmiErrorThreshold_Type(Integer32):
    """Custom type frDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrDlcmiErrorThreshold_Type.__name__ = "Integer32"
_FrDlcmiErrorThreshold_Object = MibTableColumn
frDlcmiErrorThreshold = _FrDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1, 7),
    _FrDlcmiErrorThreshold_Type()
)
frDlcmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiErrorThreshold.setStatus("mandatory")


class _FrDlcmiMonitoredEvents_Type(Integer32):
    """Custom type frDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrDlcmiMonitoredEvents_Type.__name__ = "Integer32"
_FrDlcmiMonitoredEvents_Object = MibTableColumn
frDlcmiMonitoredEvents = _FrDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1, 8),
    _FrDlcmiMonitoredEvents_Type()
)
frDlcmiMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiMonitoredEvents.setStatus("mandatory")
_FrDlcmiMaxSupportedVCs_Type = Integer32
_FrDlcmiMaxSupportedVCs_Object = MibTableColumn
frDlcmiMaxSupportedVCs = _FrDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1, 9),
    _FrDlcmiMaxSupportedVCs_Type()
)
frDlcmiMaxSupportedVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiMaxSupportedVCs.setStatus("mandatory")


class _FrDlcmiMulticast_Type(Integer32):
    """Custom type frDlcmiMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("nonBroadcast", 1))
    )


_FrDlcmiMulticast_Type.__name__ = "Integer32"
_FrDlcmiMulticast_Object = MibTableColumn
frDlcmiMulticast = _FrDlcmiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 1, 1, 10),
    _FrDlcmiMulticast_Type()
)
frDlcmiMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiMulticast.setStatus("mandatory")
_FrCircuitTable_Object = MibTable
frCircuitTable = _FrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2)
)
if mibBuilder.loadTexts:
    frCircuitTable.setStatus("mandatory")
_FrCircuitEntry_Object = MibTableRow
frCircuitEntry = _FrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1)
)
frCircuitEntry.setIndexNames(
    (0, "EICON-MIB-RFC1315", "frCircuitIfIndex"),
    (0, "EICON-MIB-RFC1315", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    frCircuitEntry.setStatus("mandatory")
_FrCircuitIfIndex_Type = Index
_FrCircuitIfIndex_Object = MibTableColumn
frCircuitIfIndex = _FrCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 1),
    _FrCircuitIfIndex_Type()
)
frCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitIfIndex.setStatus("mandatory")
_FrCircuitDlci_Type = DLCI
_FrCircuitDlci_Object = MibTableColumn
frCircuitDlci = _FrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 2),
    _FrCircuitDlci_Type()
)
frCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitDlci.setStatus("mandatory")


class _FrCircuitState_Type(Integer32):
    """Custom type frCircuitState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_FrCircuitState_Type.__name__ = "Integer32"
_FrCircuitState_Object = MibTableColumn
frCircuitState = _FrCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 3),
    _FrCircuitState_Type()
)
frCircuitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCircuitState.setStatus("mandatory")
_FrCircuitReceivedFECNs_Type = Counter32
_FrCircuitReceivedFECNs_Object = MibTableColumn
frCircuitReceivedFECNs = _FrCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 4),
    _FrCircuitReceivedFECNs_Type()
)
frCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedFECNs.setStatus("mandatory")
_FrCircuitReceivedBECNs_Type = Counter32
_FrCircuitReceivedBECNs_Object = MibTableColumn
frCircuitReceivedBECNs = _FrCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 5),
    _FrCircuitReceivedBECNs_Type()
)
frCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedBECNs.setStatus("mandatory")
_FrCircuitSentFrames_Type = Counter32
_FrCircuitSentFrames_Object = MibTableColumn
frCircuitSentFrames = _FrCircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 6),
    _FrCircuitSentFrames_Type()
)
frCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitSentFrames.setStatus("mandatory")
_FrCircuitSentOctets_Type = Counter32
_FrCircuitSentOctets_Object = MibTableColumn
frCircuitSentOctets = _FrCircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 7),
    _FrCircuitSentOctets_Type()
)
frCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitSentOctets.setStatus("mandatory")
_FrCircuitReceivedFrames_Type = Counter32
_FrCircuitReceivedFrames_Object = MibTableColumn
frCircuitReceivedFrames = _FrCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 8),
    _FrCircuitReceivedFrames_Type()
)
frCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedFrames.setStatus("mandatory")
_FrCircuitReceivedOctets_Type = Counter32
_FrCircuitReceivedOctets_Object = MibTableColumn
frCircuitReceivedOctets = _FrCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 9),
    _FrCircuitReceivedOctets_Type()
)
frCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedOctets.setStatus("mandatory")
_FrCircuitCreationTime_Type = TimeTicks
_FrCircuitCreationTime_Object = MibTableColumn
frCircuitCreationTime = _FrCircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 10),
    _FrCircuitCreationTime_Type()
)
frCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitCreationTime.setStatus("mandatory")
_FrCircuitLastTimeChange_Type = TimeTicks
_FrCircuitLastTimeChange_Object = MibTableColumn
frCircuitLastTimeChange = _FrCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 11),
    _FrCircuitLastTimeChange_Type()
)
frCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitLastTimeChange.setStatus("mandatory")


class _FrCircuitCommittedBurst_Type(Integer32):
    """Custom type frCircuitCommittedBurst based on Integer32"""
    defaultValue = 0


_FrCircuitCommittedBurst_Object = MibTableColumn
frCircuitCommittedBurst = _FrCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 12),
    _FrCircuitCommittedBurst_Type()
)
frCircuitCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCircuitCommittedBurst.setStatus("mandatory")
_FrCircuitExcessBurst_Type = Integer32
_FrCircuitExcessBurst_Object = MibTableColumn
frCircuitExcessBurst = _FrCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 13),
    _FrCircuitExcessBurst_Type()
)
frCircuitExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCircuitExcessBurst.setStatus("mandatory")


class _FrCircuitThroughput_Type(Integer32):
    """Custom type frCircuitThroughput based on Integer32"""
    defaultValue = 0


_FrCircuitThroughput_Object = MibTableColumn
frCircuitThroughput = _FrCircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 2, 1, 14),
    _FrCircuitThroughput_Type()
)
frCircuitThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCircuitThroughput.setStatus("mandatory")
_FrErrTable_Object = MibTable
frErrTable = _FrErrTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 3)
)
if mibBuilder.loadTexts:
    frErrTable.setStatus("mandatory")
_FrErrEntry_Object = MibTableRow
frErrEntry = _FrErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 3, 1)
)
frErrEntry.setIndexNames(
    (0, "EICON-MIB-RFC1315", "frErrIfIndex"),
)
if mibBuilder.loadTexts:
    frErrEntry.setStatus("mandatory")
_FrErrIfIndex_Type = Index
_FrErrIfIndex_Object = MibTableColumn
frErrIfIndex = _FrErrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 3, 1, 1),
    _FrErrIfIndex_Type()
)
frErrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrIfIndex.setStatus("mandatory")


class _FrErrType_Type(Integer32):
    """Custom type frErrType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dlcmiProtoErr", 6),
          ("dlcmiSequenceErr", 8),
          ("dlcmiUnknownIE", 7),
          ("dlcmiUnknownRpt", 9),
          ("illegalDLCI", 4),
          ("noErrorSinceReset", 10),
          ("receiveLong", 3),
          ("receiveShort", 2),
          ("unknownDLCI", 5),
          ("unknownError", 1))
    )


_FrErrType_Type.__name__ = "Integer32"
_FrErrType_Object = MibTableColumn
frErrType = _FrErrType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 3, 1, 2),
    _FrErrType_Type()
)
frErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrType.setStatus("mandatory")
_FrErrData_Type = OctetString
_FrErrData_Object = MibTableColumn
frErrData = _FrErrData_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 3, 1, 3),
    _FrErrData_Type()
)
frErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrData.setStatus("mandatory")
_FrErrTime_Type = TimeTicks
_FrErrTime_Object = MibTableColumn
frErrTime = _FrErrTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 3, 1, 4),
    _FrErrTime_Type()
)
frErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrTime.setStatus("mandatory")
_Frame_relay_globals_ObjectIdentity = ObjectIdentity
frame_relay_globals = _Frame_relay_globals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 4)
)


class _FrTrapState_Type(Integer32):
    """Custom type frTrapState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FrTrapState_Type.__name__ = "Integer32"
_FrTrapState_Object = MibScalar
frTrapState = _FrTrapState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 4, 1),
    _FrTrapState_Type()
)
frTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frTrapState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

frDLCIStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 32, 0, 1)
)
frDLCIStatusChange.setObjects(
      *(("EICON-MIB-RFC1315", "frCircuitIfIndex"),
        ("EICON-MIB-RFC1315", "frCircuitDlci"),
        ("EICON-MIB-RFC1315", "frCircuitState"))
)
if mibBuilder.loadTexts:
    frDLCIStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EICON-MIB-RFC1315",
    **{"Index": Index,
       "DLCI": DLCI,
       "eicon": eicon,
       "management": management,
       "mibv2": mibv2,
       "module": module,
       "frame-relay": frame_relay,
       "frDLCIStatusChange": frDLCIStatusChange,
       "frDlcmiTable": frDlcmiTable,
       "frDlcmiEntry": frDlcmiEntry,
       "frDlcmiIfIndex": frDlcmiIfIndex,
       "frDlcmiState": frDlcmiState,
       "frDlcmiAddress": frDlcmiAddress,
       "frDlcmiAddressLen": frDlcmiAddressLen,
       "frDlcmiPollingInterval": frDlcmiPollingInterval,
       "frDlcmiFullEnquiryInterval": frDlcmiFullEnquiryInterval,
       "frDlcmiErrorThreshold": frDlcmiErrorThreshold,
       "frDlcmiMonitoredEvents": frDlcmiMonitoredEvents,
       "frDlcmiMaxSupportedVCs": frDlcmiMaxSupportedVCs,
       "frDlcmiMulticast": frDlcmiMulticast,
       "frCircuitTable": frCircuitTable,
       "frCircuitEntry": frCircuitEntry,
       "frCircuitIfIndex": frCircuitIfIndex,
       "frCircuitDlci": frCircuitDlci,
       "frCircuitState": frCircuitState,
       "frCircuitReceivedFECNs": frCircuitReceivedFECNs,
       "frCircuitReceivedBECNs": frCircuitReceivedBECNs,
       "frCircuitSentFrames": frCircuitSentFrames,
       "frCircuitSentOctets": frCircuitSentOctets,
       "frCircuitReceivedFrames": frCircuitReceivedFrames,
       "frCircuitReceivedOctets": frCircuitReceivedOctets,
       "frCircuitCreationTime": frCircuitCreationTime,
       "frCircuitLastTimeChange": frCircuitLastTimeChange,
       "frCircuitCommittedBurst": frCircuitCommittedBurst,
       "frCircuitExcessBurst": frCircuitExcessBurst,
       "frCircuitThroughput": frCircuitThroughput,
       "frErrTable": frErrTable,
       "frErrEntry": frErrEntry,
       "frErrIfIndex": frErrIfIndex,
       "frErrType": frErrType,
       "frErrData": frErrData,
       "frErrTime": frErrTime,
       "frame-relay-globals": frame_relay_globals,
       "frTrapState": frTrapState}
)
