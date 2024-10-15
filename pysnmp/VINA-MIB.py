# SNMP MIB module (VINA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VINA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:35 2024
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

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

_Frame_relay_ObjectIdentity = ObjectIdentity
frame_relay = _Frame_relay_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 32)
)
_FrDlcmiTable_Object = MibTable
frDlcmiTable = _FrDlcmiTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1)
)
if mibBuilder.loadTexts:
    frDlcmiTable.setStatus("mandatory")
_FrDlcmiEntry_Object = MibTableRow
frDlcmiEntry = _FrDlcmiEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1)
)
frDlcmiEntry.setIndexNames(
    (0, "VINA-MIB", "frDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    frDlcmiEntry.setStatus("mandatory")
_FrDlcmiIfIndex_Type = Index
_FrDlcmiIfIndex_Object = MibTableColumn
frDlcmiIfIndex = _FrDlcmiIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 1),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 2),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 3),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 4),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 5),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 6),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 7),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 8),
    _FrDlcmiMonitoredEvents_Type()
)
frDlcmiMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiMonitoredEvents.setStatus("mandatory")
_FrDlcmiMaxSupportedVCs_Type = Integer32
_FrDlcmiMaxSupportedVCs_Object = MibTableColumn
frDlcmiMaxSupportedVCs = _FrDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 9),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 10),
    _FrDlcmiMulticast_Type()
)
frDlcmiMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiMulticast.setStatus("mandatory")
_FrCircuitTable_Object = MibTable
frCircuitTable = _FrCircuitTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2)
)
if mibBuilder.loadTexts:
    frCircuitTable.setStatus("mandatory")
_FrCircuitEntry_Object = MibTableRow
frCircuitEntry = _FrCircuitEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1)
)
frCircuitEntry.setIndexNames(
    (0, "VINA-MIB", "frCircuitIfIndex"),
    (0, "VINA-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    frCircuitEntry.setStatus("mandatory")
_FrCircuitIfIndex_Type = Index
_FrCircuitIfIndex_Object = MibTableColumn
frCircuitIfIndex = _FrCircuitIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 1),
    _FrCircuitIfIndex_Type()
)
frCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitIfIndex.setStatus("mandatory")
_FrCircuitDlci_Type = DLCI
_FrCircuitDlci_Object = MibTableColumn
frCircuitDlci = _FrCircuitDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 2),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 3),
    _FrCircuitState_Type()
)
frCircuitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCircuitState.setStatus("mandatory")
_FrCircuitReceivedFECNs_Type = Counter32
_FrCircuitReceivedFECNs_Object = MibTableColumn
frCircuitReceivedFECNs = _FrCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 4),
    _FrCircuitReceivedFECNs_Type()
)
frCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedFECNs.setStatus("mandatory")
_FrCircuitReceivedBECNs_Type = Counter32
_FrCircuitReceivedBECNs_Object = MibTableColumn
frCircuitReceivedBECNs = _FrCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 5),
    _FrCircuitReceivedBECNs_Type()
)
frCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedBECNs.setStatus("mandatory")
_FrCircuitSentFrames_Type = Counter32
_FrCircuitSentFrames_Object = MibTableColumn
frCircuitSentFrames = _FrCircuitSentFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 6),
    _FrCircuitSentFrames_Type()
)
frCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitSentFrames.setStatus("mandatory")
_FrCircuitSentOctets_Type = Counter32
_FrCircuitSentOctets_Object = MibTableColumn
frCircuitSentOctets = _FrCircuitSentOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 7),
    _FrCircuitSentOctets_Type()
)
frCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitSentOctets.setStatus("mandatory")
_FrCircuitReceivedFrames_Type = Counter32
_FrCircuitReceivedFrames_Object = MibTableColumn
frCircuitReceivedFrames = _FrCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 8),
    _FrCircuitReceivedFrames_Type()
)
frCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedFrames.setStatus("mandatory")
_FrCircuitReceivedOctets_Type = Counter32
_FrCircuitReceivedOctets_Object = MibTableColumn
frCircuitReceivedOctets = _FrCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 9),
    _FrCircuitReceivedOctets_Type()
)
frCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedOctets.setStatus("mandatory")
_FrCircuitCreationTime_Type = TimeTicks
_FrCircuitCreationTime_Object = MibTableColumn
frCircuitCreationTime = _FrCircuitCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 10),
    _FrCircuitCreationTime_Type()
)
frCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitCreationTime.setStatus("mandatory")
_FrCircuitLastTimeChange_Type = TimeTicks
_FrCircuitLastTimeChange_Object = MibTableColumn
frCircuitLastTimeChange = _FrCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 11),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 12),
    _FrCircuitCommittedBurst_Type()
)
frCircuitCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCircuitCommittedBurst.setStatus("mandatory")
_FrCircuitExcessBurst_Type = Integer32
_FrCircuitExcessBurst_Object = MibTableColumn
frCircuitExcessBurst = _FrCircuitExcessBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 13),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 14),
    _FrCircuitThroughput_Type()
)
frCircuitThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCircuitThroughput.setStatus("mandatory")
_FrErrTable_Object = MibTable
frErrTable = _FrErrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3)
)
if mibBuilder.loadTexts:
    frErrTable.setStatus("mandatory")
_FrErrEntry_Object = MibTableRow
frErrEntry = _FrErrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1)
)
frErrEntry.setIndexNames(
    (0, "VINA-MIB", "frErrIfIndex"),
)
if mibBuilder.loadTexts:
    frErrEntry.setStatus("mandatory")
_FrErrIfIndex_Type = Index
_FrErrIfIndex_Object = MibTableColumn
frErrIfIndex = _FrErrIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 1),
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
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 2),
    _FrErrType_Type()
)
frErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrType.setStatus("mandatory")
_FrErrData_Type = OctetString
_FrErrData_Object = MibTableColumn
frErrData = _FrErrData_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 3),
    _FrErrData_Type()
)
frErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrData.setStatus("mandatory")
_FrErrTime_Type = TimeTicks
_FrErrTime_Object = MibTableColumn
frErrTime = _FrErrTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 4),
    _FrErrTime_Type()
)
frErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrTime.setStatus("mandatory")
_Frame_relay_globals_ObjectIdentity = ObjectIdentity
frame_relay_globals = _Frame_relay_globals_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 32, 4)
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
    (1, 3, 6, 1, 2, 1, 10, 32, 4, 1),
    _FrTrapState_Type()
)
frTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frTrapState.setStatus("mandatory")
_Vina_ObjectIdentity = ObjectIdentity
vina = _Vina_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186)
)
_VinaSys_ObjectIdentity = ObjectIdentity
vinaSys = _VinaSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1)
)
_OperatingSystem_ObjectIdentity = ObjectIdentity
operatingSystem = _OperatingSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1)
)
_Vxworks_ObjectIdentity = ObjectIdentity
vxworks = _Vxworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1)
)
_VxMemory_ObjectIdentity = ObjectIdentity
vxMemory = _VxMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1)
)
_CurrentMemory_ObjectIdentity = ObjectIdentity
currentMemory = _CurrentMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 2)
)
_CurrentMemorybytes_Type = Integer32
_CurrentMemorybytes_Object = MibScalar
currentMemorybytes = _CurrentMemorybytes_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 2, 1),
    _CurrentMemorybytes_Type()
)
currentMemorybytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMemorybytes.setStatus("mandatory")
_CurrentMemoryblocks_Type = Integer32
_CurrentMemoryblocks_Object = MibScalar
currentMemoryblocks = _CurrentMemoryblocks_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 2, 2),
    _CurrentMemoryblocks_Type()
)
currentMemoryblocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMemoryblocks.setStatus("mandatory")
_CurrentMemoryavgerage_Type = Integer32
_CurrentMemoryavgerage_Object = MibScalar
currentMemoryavgerage = _CurrentMemoryavgerage_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 2, 3),
    _CurrentMemoryavgerage_Type()
)
currentMemoryavgerage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMemoryavgerage.setStatus("mandatory")
_CurrentMemorymaximum_Type = Integer32
_CurrentMemorymaximum_Object = MibScalar
currentMemorymaximum = _CurrentMemorymaximum_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 2, 4),
    _CurrentMemorymaximum_Type()
)
currentMemorymaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMemorymaximum.setStatus("mandatory")
_FreeMemory_ObjectIdentity = ObjectIdentity
freeMemory = _FreeMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 3)
)
_FreeMemorybytes_Type = Integer32
_FreeMemorybytes_Object = MibScalar
freeMemorybytes = _FreeMemorybytes_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 3, 1),
    _FreeMemorybytes_Type()
)
freeMemorybytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMemorybytes.setStatus("mandatory")
_FreeMemoryblocks_Type = Integer32
_FreeMemoryblocks_Object = MibScalar
freeMemoryblocks = _FreeMemoryblocks_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 3, 2),
    _FreeMemoryblocks_Type()
)
freeMemoryblocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMemoryblocks.setStatus("mandatory")
_FreeMemoryaverage_Type = Integer32
_FreeMemoryaverage_Object = MibScalar
freeMemoryaverage = _FreeMemoryaverage_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 3, 3),
    _FreeMemoryaverage_Type()
)
freeMemoryaverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMemoryaverage.setStatus("mandatory")
_CumulativeMemory_ObjectIdentity = ObjectIdentity
cumulativeMemory = _CumulativeMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 4)
)
_Cumulativebytes_Type = Integer32
_Cumulativebytes_Object = MibScalar
cumulativebytes = _Cumulativebytes_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 4, 1),
    _Cumulativebytes_Type()
)
cumulativebytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cumulativebytes.setStatus("mandatory")
_Cumulativeblocks_Type = Integer32
_Cumulativeblocks_Object = MibScalar
cumulativeblocks = _Cumulativeblocks_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 4, 2),
    _Cumulativeblocks_Type()
)
cumulativeblocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cumulativeblocks.setStatus("mandatory")
_Cumulativeaverage_Type = Integer32
_Cumulativeaverage_Object = MibScalar
cumulativeaverage = _Cumulativeaverage_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 1, 4, 3),
    _Cumulativeaverage_Type()
)
cumulativeaverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cumulativeaverage.setStatus("mandatory")
_VxNetwork_ObjectIdentity = ObjectIdentity
vxNetwork = _VxNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 2)
)
_VxTcp_ObjectIdentity = ObjectIdentity
vxTcp = _VxTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 2, 1)
)
_VxTask_ObjectIdentity = ObjectIdentity
vxTask = _VxTask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3)
)
_VxNumTasks_Type = Integer32
_VxNumTasks_Object = MibScalar
vxNumTasks = _VxNumTasks_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 1),
    _VxNumTasks_Type()
)
vxNumTasks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vxNumTasks.setStatus("mandatory")
_VxTaskTable_Object = MibTable
vxTaskTable = _VxTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    vxTaskTable.setStatus("deprecated")
_VxTaskEntry_Object = MibTableRow
vxTaskEntry = _VxTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2, 1)
)
vxTaskEntry.setIndexNames(
    (0, "VINA-MIB", "taskID"),
)
if mibBuilder.loadTexts:
    vxTaskEntry.setStatus("deprecated")
_Name_Type = OctetString
_Name_Object = MibTableColumn
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("deprecated")
_EntryPoint_Type = OctetString
_EntryPoint_Object = MibTableColumn
entryPoint = _EntryPoint_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2, 1, 2),
    _EntryPoint_Type()
)
entryPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entryPoint.setStatus("deprecated")
_TaskID_Type = Integer32
_TaskID_Object = MibTableColumn
taskID = _TaskID_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2, 1, 3),
    _TaskID_Type()
)
taskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskID.setStatus("deprecated")
_Priority_Type = Integer32
_Priority_Object = MibTableColumn
priority = _Priority_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2, 1, 4),
    _Priority_Type()
)
priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority.setStatus("deprecated")
_Status_Type = Integer32
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2, 1, 5),
    _Status_Type()
)
status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    status.setStatus("deprecated")
_ProgramCounter_Type = Integer32
_ProgramCounter_Object = MibTableColumn
programCounter = _ProgramCounter_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2, 1, 6),
    _ProgramCounter_Type()
)
programCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programCounter.setStatus("deprecated")
_StackPointer_Type = Integer32
_StackPointer_Object = MibTableColumn
stackPointer = _StackPointer_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2, 1, 7),
    _StackPointer_Type()
)
stackPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackPointer.setStatus("deprecated")
_Errno_Type = Integer32
_Errno_Object = MibTableColumn
errno = _Errno_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2, 1, 8),
    _Errno_Type()
)
errno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errno.setStatus("deprecated")
_Delay_Type = Integer32
_Delay_Object = MibTableColumn
delay = _Delay_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 3, 2, 1, 9),
    _Delay_Type()
)
delay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delay.setStatus("deprecated")
_VxBootParams_ObjectIdentity = ObjectIdentity
vxBootParams = _VxBootParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4)
)
_BootDev_Type = OctetString
_BootDev_Object = MibScalar
bootDev = _BootDev_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 1),
    _BootDev_Type()
)
bootDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootDev.setStatus("mandatory")
_HostName_Type = OctetString
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")
_TargetName_Type = OctetString
_TargetName_Object = MibScalar
targetName = _TargetName_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 3),
    _TargetName_Type()
)
targetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetName.setStatus("mandatory")
_EthernetAddr_Type = OctetString
_EthernetAddr_Object = MibScalar
ethernetAddr = _EthernetAddr_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 4),
    _EthernetAddr_Type()
)
ethernetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetAddr.setStatus("mandatory")
_BackplaneAddr_Type = OctetString
_BackplaneAddr_Object = MibScalar
backplaneAddr = _BackplaneAddr_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 5),
    _BackplaneAddr_Type()
)
backplaneAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backplaneAddr.setStatus("mandatory")
_HostAddr_Type = OctetString
_HostAddr_Object = MibScalar
hostAddr = _HostAddr_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 6),
    _HostAddr_Type()
)
hostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostAddr.setStatus("mandatory")
_GatewayAddr_Type = OctetString
_GatewayAddr_Object = MibScalar
gatewayAddr = _GatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 7),
    _GatewayAddr_Type()
)
gatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayAddr.setStatus("mandatory")
_BootFile_Type = OctetString
_BootFile_Object = MibScalar
bootFile = _BootFile_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 8),
    _BootFile_Type()
)
bootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootFile.setStatus("mandatory")
_StartupScript_Type = OctetString
_StartupScript_Object = MibScalar
startupScript = _StartupScript_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 9),
    _StartupScript_Type()
)
startupScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startupScript.setStatus("mandatory")
_UserName_Type = OctetString
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 10),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("mandatory")
_Password_Type = OctetString
_Password_Object = MibScalar
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 11),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("mandatory")
_Other_Type = OctetString
_Other_Object = MibScalar
other = _Other_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 12),
    _Other_Type()
)
other.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    other.setStatus("mandatory")
_ProcessorNumber_Type = Integer32
_ProcessorNumber_Object = MibScalar
processorNumber = _ProcessorNumber_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 13),
    _ProcessorNumber_Type()
)
processorNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processorNumber.setStatus("mandatory")
_Flags_Type = Integer32
_Flags_Object = MibScalar
flags = _Flags_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 4, 14),
    _Flags_Type()
)
flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flags.setStatus("mandatory")
_VxKernel_ObjectIdentity = ObjectIdentity
vxKernel = _VxKernel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 5)
)
_VxClock_ObjectIdentity = ObjectIdentity
vxClock = _VxClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 5, 1)
)
_SysClkRate_Type = Integer32
_SysClkRate_Object = MibScalar
sysClkRate = _SysClkRate_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 5, 1, 1),
    _SysClkRate_Type()
)
sysClkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClkRate.setStatus("mandatory")
_Ticks_Type = Integer32
_Ticks_Object = MibScalar
ticks = _Ticks_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 1, 1, 5, 1, 2),
    _Ticks_Type()
)
ticks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ticks.setStatus("mandatory")
_Snmpd_ObjectIdentity = ObjectIdentity
snmpd = _Snmpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 2)
)
_AgentVersion_Type = OctetString
_AgentVersion_Object = MibScalar
agentVersion = _AgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 2, 1),
    _AgentVersion_Type()
)
agentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVersion.setStatus("mandatory")
_PortVersion_Type = OctetString
_PortVersion_Object = MibScalar
portVersion = _PortVersion_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 2, 2),
    _PortVersion_Type()
)
portVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVersion.setStatus("mandatory")
_TaskPriority_Type = Integer32
_TaskPriority_Object = MibScalar
taskPriority = _TaskPriority_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 2, 3),
    _TaskPriority_Type()
)
taskPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskPriority.setStatus("mandatory")
_Idle_ObjectIdentity = ObjectIdentity
idle = _Idle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 3)
)
_CurrentIdle_Type = Integer32
_CurrentIdle_Object = MibScalar
currentIdle = _CurrentIdle_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 3, 1),
    _CurrentIdle_Type()
)
currentIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentIdle.setStatus("mandatory")
_TenSecondIdle_Type = Integer32
_TenSecondIdle_Object = MibScalar
tenSecondIdle = _TenSecondIdle_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 3, 2),
    _TenSecondIdle_Type()
)
tenSecondIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenSecondIdle.setStatus("mandatory")
_SixtySecondIdle_Type = Integer32
_SixtySecondIdle_Object = MibScalar
sixtySecondIdle = _SixtySecondIdle_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 3, 3),
    _SixtySecondIdle_Type()
)
sixtySecondIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sixtySecondIdle.setStatus("mandatory")
_UserIdle_Type = Integer32
_UserIdle_Object = MibScalar
userIdle = _UserIdle_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 3, 4),
    _UserIdle_Type()
)
userIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userIdle.setStatus("mandatory")


class _UserInterval_Type(Integer32):
    """Custom type userInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_UserInterval_Type.__name__ = "Integer32"
_UserInterval_Object = MibScalar
userInterval = _UserInterval_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 3, 5),
    _UserInterval_Type()
)
userInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userInterval.setStatus("mandatory")
_Calibration_Type = Integer32
_Calibration_Object = MibScalar
calibration = _Calibration_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 3, 6),
    _Calibration_Type()
)
calibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calibration.setStatus("mandatory")
_HistorySize_Type = Integer32
_HistorySize_Object = MibScalar
historySize = _HistorySize_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 3, 7),
    _HistorySize_Type()
)
historySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historySize.setStatus("mandatory")
_HistoryValid_Type = Integer32
_HistoryValid_Object = MibScalar
historyValid = _HistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 3, 8),
    _HistoryValid_Type()
)
historyValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyValid.setStatus("mandatory")
_Vina_system_ObjectIdentity = ObjectIdentity
vina_system = _Vina_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 4)
)
_Reboot_Type = Integer32
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 4, 1),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("mandatory")
_RebootVME_Type = Integer32
_RebootVME_Object = MibScalar
rebootVME = _RebootVME_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 4, 2),
    _RebootVME_Type()
)
rebootVME.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootVME.setStatus("mandatory")
_AbortReboot_Type = Integer32
_AbortReboot_Object = MibScalar
abortReboot = _AbortReboot_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 4, 3),
    _AbortReboot_Type()
)
abortReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    abortReboot.setStatus("mandatory")
_Silent_Type = Integer32
_Silent_Object = MibScalar
silent = _Silent_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 4, 4),
    _Silent_Type()
)
silent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    silent.setStatus("mandatory")
_SpuriousInts_Type = Integer32
_SpuriousInts_Object = MibScalar
spuriousInts = _SpuriousInts_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 4, 5),
    _SpuriousInts_Type()
)
spuriousInts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spuriousInts.setStatus("mandatory")
_VinaSla_ObjectIdentity = ObjectIdentity
vinaSla = _VinaSla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5)
)
_VinaSlaConfigVars_ObjectIdentity = ObjectIdentity
vinaSlaConfigVars = _VinaSlaConfigVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 1)
)
_VinaSlaNumValidIntervals_Type = Integer32
_VinaSlaNumValidIntervals_Object = MibScalar
vinaSlaNumValidIntervals = _VinaSlaNumValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 1, 1),
    _VinaSlaNumValidIntervals_Type()
)
vinaSlaNumValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaNumValidIntervals.setStatus("mandatory")
_VinaSlaCurrentTable_Object = MibTable
vinaSlaCurrentTable = _VinaSlaCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 2)
)
if mibBuilder.loadTexts:
    vinaSlaCurrentTable.setStatus("mandatory")
_VinaSlaCurrentEntry_Object = MibTableRow
vinaSlaCurrentEntry = _VinaSlaCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 2, 1)
)
vinaSlaCurrentEntry.setIndexNames(
    (0, "VINA-MIB", "vinaSlaCurrentPvcNumber"),
)
if mibBuilder.loadTexts:
    vinaSlaCurrentEntry.setStatus("mandatory")


class _VinaSlaCurrentPvcNumber_Type(Integer32):
    """Custom type vinaSlaCurrentPvcNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VinaSlaCurrentPvcNumber_Type.__name__ = "Integer32"
_VinaSlaCurrentPvcNumber_Object = MibTableColumn
vinaSlaCurrentPvcNumber = _VinaSlaCurrentPvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 2, 1, 1),
    _VinaSlaCurrentPvcNumber_Type()
)
vinaSlaCurrentPvcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaCurrentPvcNumber.setStatus("mandatory")


class _VinaSlaCurrentEndToEndAveLatency_Type(Integer32):
    """Custom type vinaSlaCurrentEndToEndAveLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VinaSlaCurrentEndToEndAveLatency_Type.__name__ = "Integer32"
_VinaSlaCurrentEndToEndAveLatency_Object = MibTableColumn
vinaSlaCurrentEndToEndAveLatency = _VinaSlaCurrentEndToEndAveLatency_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 2, 1, 2),
    _VinaSlaCurrentEndToEndAveLatency_Type()
)
vinaSlaCurrentEndToEndAveLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaCurrentEndToEndAveLatency.setStatus("mandatory")


class _VinaSlaCurrentEndToEndPeakLatency_Type(Integer32):
    """Custom type vinaSlaCurrentEndToEndPeakLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VinaSlaCurrentEndToEndPeakLatency_Type.__name__ = "Integer32"
_VinaSlaCurrentEndToEndPeakLatency_Object = MibTableColumn
vinaSlaCurrentEndToEndPeakLatency = _VinaSlaCurrentEndToEndPeakLatency_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 2, 1, 3),
    _VinaSlaCurrentEndToEndPeakLatency_Type()
)
vinaSlaCurrentEndToEndPeakLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaCurrentEndToEndPeakLatency.setStatus("mandatory")


class _VinaSlaCurrentDdrAboveCir_Type(Integer32):
    """Custom type vinaSlaCurrentDdrAboveCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_VinaSlaCurrentDdrAboveCir_Type.__name__ = "Integer32"
_VinaSlaCurrentDdrAboveCir_Object = MibTableColumn
vinaSlaCurrentDdrAboveCir = _VinaSlaCurrentDdrAboveCir_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 2, 1, 4),
    _VinaSlaCurrentDdrAboveCir_Type()
)
vinaSlaCurrentDdrAboveCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaCurrentDdrAboveCir.setStatus("mandatory")


class _VinaSlaCurrentDdrBelowCir_Type(Integer32):
    """Custom type vinaSlaCurrentDdrBelowCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_VinaSlaCurrentDdrBelowCir_Type.__name__ = "Integer32"
_VinaSlaCurrentDdrBelowCir_Object = MibTableColumn
vinaSlaCurrentDdrBelowCir = _VinaSlaCurrentDdrBelowCir_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 2, 1, 5),
    _VinaSlaCurrentDdrBelowCir_Type()
)
vinaSlaCurrentDdrBelowCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaCurrentDdrBelowCir.setStatus("mandatory")


class _VinaSlaCurrentPvcDowntime_Type(Integer32):
    """Custom type vinaSlaCurrentPvcDowntime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900000),
    )


_VinaSlaCurrentPvcDowntime_Type.__name__ = "Integer32"
_VinaSlaCurrentPvcDowntime_Object = MibTableColumn
vinaSlaCurrentPvcDowntime = _VinaSlaCurrentPvcDowntime_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 2, 1, 6),
    _VinaSlaCurrentPvcDowntime_Type()
)
vinaSlaCurrentPvcDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaCurrentPvcDowntime.setStatus("mandatory")


class _VinaSlaCurrentPvcUptime_Type(Integer32):
    """Custom type vinaSlaCurrentPvcUptime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900000),
    )


_VinaSlaCurrentPvcUptime_Type.__name__ = "Integer32"
_VinaSlaCurrentPvcUptime_Object = MibTableColumn
vinaSlaCurrentPvcUptime = _VinaSlaCurrentPvcUptime_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 2, 1, 7),
    _VinaSlaCurrentPvcUptime_Type()
)
vinaSlaCurrentPvcUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaCurrentPvcUptime.setStatus("mandatory")


class _VinaSlaCurrentPvcNumTimesDown_Type(Integer32):
    """Custom type vinaSlaCurrentPvcNumTimesDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_VinaSlaCurrentPvcNumTimesDown_Type.__name__ = "Integer32"
_VinaSlaCurrentPvcNumTimesDown_Object = MibTableColumn
vinaSlaCurrentPvcNumTimesDown = _VinaSlaCurrentPvcNumTimesDown_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 2, 1, 8),
    _VinaSlaCurrentPvcNumTimesDown_Type()
)
vinaSlaCurrentPvcNumTimesDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaCurrentPvcNumTimesDown.setStatus("mandatory")
_VinaSlaIntervalTable_Object = MibTable
vinaSlaIntervalTable = _VinaSlaIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3)
)
if mibBuilder.loadTexts:
    vinaSlaIntervalTable.setStatus("mandatory")
_VinaSlaIntervalEntry_Object = MibTableRow
vinaSlaIntervalEntry = _VinaSlaIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3, 1)
)
vinaSlaIntervalEntry.setIndexNames(
    (0, "VINA-MIB", "vinaSlaIntervalPvcNumber"),
    (0, "VINA-MIB", "vinaSlaIntervalNumber"),
)
if mibBuilder.loadTexts:
    vinaSlaIntervalEntry.setStatus("mandatory")


class _VinaSlaIntervalPvcNumber_Type(Integer32):
    """Custom type vinaSlaIntervalPvcNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VinaSlaIntervalPvcNumber_Type.__name__ = "Integer32"
_VinaSlaIntervalPvcNumber_Object = MibTableColumn
vinaSlaIntervalPvcNumber = _VinaSlaIntervalPvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3, 1, 1),
    _VinaSlaIntervalPvcNumber_Type()
)
vinaSlaIntervalPvcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaIntervalPvcNumber.setStatus("mandatory")


class _VinaSlaIntervalNumber_Type(Integer32):
    """Custom type vinaSlaIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_VinaSlaIntervalNumber_Type.__name__ = "Integer32"
_VinaSlaIntervalNumber_Object = MibTableColumn
vinaSlaIntervalNumber = _VinaSlaIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3, 1, 2),
    _VinaSlaIntervalNumber_Type()
)
vinaSlaIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaIntervalNumber.setStatus("mandatory")


class _VinaSlaIntervalEndToEndAveLatency_Type(Integer32):
    """Custom type vinaSlaIntervalEndToEndAveLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VinaSlaIntervalEndToEndAveLatency_Type.__name__ = "Integer32"
_VinaSlaIntervalEndToEndAveLatency_Object = MibTableColumn
vinaSlaIntervalEndToEndAveLatency = _VinaSlaIntervalEndToEndAveLatency_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3, 1, 3),
    _VinaSlaIntervalEndToEndAveLatency_Type()
)
vinaSlaIntervalEndToEndAveLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaIntervalEndToEndAveLatency.setStatus("mandatory")


class _VinaSlaIntervalEndToEndPeakLatency_Type(Integer32):
    """Custom type vinaSlaIntervalEndToEndPeakLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VinaSlaIntervalEndToEndPeakLatency_Type.__name__ = "Integer32"
_VinaSlaIntervalEndToEndPeakLatency_Object = MibTableColumn
vinaSlaIntervalEndToEndPeakLatency = _VinaSlaIntervalEndToEndPeakLatency_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3, 1, 4),
    _VinaSlaIntervalEndToEndPeakLatency_Type()
)
vinaSlaIntervalEndToEndPeakLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaIntervalEndToEndPeakLatency.setStatus("mandatory")


class _VinaSlaIntervalDdrAboveCir_Type(Integer32):
    """Custom type vinaSlaIntervalDdrAboveCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_VinaSlaIntervalDdrAboveCir_Type.__name__ = "Integer32"
_VinaSlaIntervalDdrAboveCir_Object = MibTableColumn
vinaSlaIntervalDdrAboveCir = _VinaSlaIntervalDdrAboveCir_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3, 1, 5),
    _VinaSlaIntervalDdrAboveCir_Type()
)
vinaSlaIntervalDdrAboveCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaIntervalDdrAboveCir.setStatus("mandatory")


class _VinaSlaIntervalDdrBelowCir_Type(Integer32):
    """Custom type vinaSlaIntervalDdrBelowCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_VinaSlaIntervalDdrBelowCir_Type.__name__ = "Integer32"
_VinaSlaIntervalDdrBelowCir_Object = MibTableColumn
vinaSlaIntervalDdrBelowCir = _VinaSlaIntervalDdrBelowCir_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3, 1, 6),
    _VinaSlaIntervalDdrBelowCir_Type()
)
vinaSlaIntervalDdrBelowCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaIntervalDdrBelowCir.setStatus("mandatory")


class _VinaSlaIntervalPvcDowntime_Type(Integer32):
    """Custom type vinaSlaIntervalPvcDowntime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900000),
    )


_VinaSlaIntervalPvcDowntime_Type.__name__ = "Integer32"
_VinaSlaIntervalPvcDowntime_Object = MibTableColumn
vinaSlaIntervalPvcDowntime = _VinaSlaIntervalPvcDowntime_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3, 1, 7),
    _VinaSlaIntervalPvcDowntime_Type()
)
vinaSlaIntervalPvcDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaIntervalPvcDowntime.setStatus("mandatory")


class _VinaSlaIntervalPvcUptime_Type(Integer32):
    """Custom type vinaSlaIntervalPvcUptime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900000),
    )


_VinaSlaIntervalPvcUptime_Type.__name__ = "Integer32"
_VinaSlaIntervalPvcUptime_Object = MibTableColumn
vinaSlaIntervalPvcUptime = _VinaSlaIntervalPvcUptime_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3, 1, 8),
    _VinaSlaIntervalPvcUptime_Type()
)
vinaSlaIntervalPvcUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaIntervalPvcUptime.setStatus("mandatory")


class _VinaSlaIntervalPvcNumTimesDown_Type(Integer32):
    """Custom type vinaSlaIntervalPvcNumTimesDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_VinaSlaIntervalPvcNumTimesDown_Type.__name__ = "Integer32"
_VinaSlaIntervalPvcNumTimesDown_Object = MibTableColumn
vinaSlaIntervalPvcNumTimesDown = _VinaSlaIntervalPvcNumTimesDown_Object(
    (1, 3, 6, 1, 4, 1, 2186, 1, 5, 3, 1, 9),
    _VinaSlaIntervalPvcNumTimesDown_Type()
)
vinaSlaIntervalPvcNumTimesDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinaSlaIntervalPvcNumTimesDown.setStatus("mandatory")
_VinaTraps_ObjectIdentity = ObjectIdentity
vinaTraps = _VinaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2186, 2)
)

# Managed Objects groups


# Notification objects

frDLCIStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 32, 0, 1)
)
frDLCIStatusChange.setObjects(
      *(("VINA-MIB", "frCircuitIfIndex"),
        ("VINA-MIB", "frCircuitDlci"),
        ("VINA-MIB", "frCircuitState"))
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
    "VINA-MIB",
    **{"Index": Index,
       "DLCI": DLCI,
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
       "frTrapState": frTrapState,
       "vina": vina,
       "vinaSys": vinaSys,
       "operatingSystem": operatingSystem,
       "vxworks": vxworks,
       "vxMemory": vxMemory,
       "currentMemory": currentMemory,
       "currentMemorybytes": currentMemorybytes,
       "currentMemoryblocks": currentMemoryblocks,
       "currentMemoryavgerage": currentMemoryavgerage,
       "currentMemorymaximum": currentMemorymaximum,
       "freeMemory": freeMemory,
       "freeMemorybytes": freeMemorybytes,
       "freeMemoryblocks": freeMemoryblocks,
       "freeMemoryaverage": freeMemoryaverage,
       "cumulativeMemory": cumulativeMemory,
       "cumulativebytes": cumulativebytes,
       "cumulativeblocks": cumulativeblocks,
       "cumulativeaverage": cumulativeaverage,
       "vxNetwork": vxNetwork,
       "vxTcp": vxTcp,
       "vxTask": vxTask,
       "vxNumTasks": vxNumTasks,
       "vxTaskTable": vxTaskTable,
       "vxTaskEntry": vxTaskEntry,
       "name": name,
       "entryPoint": entryPoint,
       "taskID": taskID,
       "priority": priority,
       "status": status,
       "programCounter": programCounter,
       "stackPointer": stackPointer,
       "errno": errno,
       "delay": delay,
       "vxBootParams": vxBootParams,
       "bootDev": bootDev,
       "hostName": hostName,
       "targetName": targetName,
       "ethernetAddr": ethernetAddr,
       "backplaneAddr": backplaneAddr,
       "hostAddr": hostAddr,
       "gatewayAddr": gatewayAddr,
       "bootFile": bootFile,
       "startupScript": startupScript,
       "userName": userName,
       "password": password,
       "other": other,
       "processorNumber": processorNumber,
       "flags": flags,
       "vxKernel": vxKernel,
       "vxClock": vxClock,
       "sysClkRate": sysClkRate,
       "ticks": ticks,
       "snmpd": snmpd,
       "agentVersion": agentVersion,
       "portVersion": portVersion,
       "taskPriority": taskPriority,
       "idle": idle,
       "currentIdle": currentIdle,
       "tenSecondIdle": tenSecondIdle,
       "sixtySecondIdle": sixtySecondIdle,
       "userIdle": userIdle,
       "userInterval": userInterval,
       "calibration": calibration,
       "historySize": historySize,
       "historyValid": historyValid,
       "vina-system": vina_system,
       "reboot": reboot,
       "rebootVME": rebootVME,
       "abortReboot": abortReboot,
       "silent": silent,
       "spuriousInts": spuriousInts,
       "vinaSla": vinaSla,
       "vinaSlaConfigVars": vinaSlaConfigVars,
       "vinaSlaNumValidIntervals": vinaSlaNumValidIntervals,
       "vinaSlaCurrentTable": vinaSlaCurrentTable,
       "vinaSlaCurrentEntry": vinaSlaCurrentEntry,
       "vinaSlaCurrentPvcNumber": vinaSlaCurrentPvcNumber,
       "vinaSlaCurrentEndToEndAveLatency": vinaSlaCurrentEndToEndAveLatency,
       "vinaSlaCurrentEndToEndPeakLatency": vinaSlaCurrentEndToEndPeakLatency,
       "vinaSlaCurrentDdrAboveCir": vinaSlaCurrentDdrAboveCir,
       "vinaSlaCurrentDdrBelowCir": vinaSlaCurrentDdrBelowCir,
       "vinaSlaCurrentPvcDowntime": vinaSlaCurrentPvcDowntime,
       "vinaSlaCurrentPvcUptime": vinaSlaCurrentPvcUptime,
       "vinaSlaCurrentPvcNumTimesDown": vinaSlaCurrentPvcNumTimesDown,
       "vinaSlaIntervalTable": vinaSlaIntervalTable,
       "vinaSlaIntervalEntry": vinaSlaIntervalEntry,
       "vinaSlaIntervalPvcNumber": vinaSlaIntervalPvcNumber,
       "vinaSlaIntervalNumber": vinaSlaIntervalNumber,
       "vinaSlaIntervalEndToEndAveLatency": vinaSlaIntervalEndToEndAveLatency,
       "vinaSlaIntervalEndToEndPeakLatency": vinaSlaIntervalEndToEndPeakLatency,
       "vinaSlaIntervalDdrAboveCir": vinaSlaIntervalDdrAboveCir,
       "vinaSlaIntervalDdrBelowCir": vinaSlaIntervalDdrBelowCir,
       "vinaSlaIntervalPvcDowntime": vinaSlaIntervalPvcDowntime,
       "vinaSlaIntervalPvcUptime": vinaSlaIntervalPvcUptime,
       "vinaSlaIntervalPvcNumTimesDown": vinaSlaIntervalPvcNumTimesDown,
       "vinaTraps": vinaTraps}
)
