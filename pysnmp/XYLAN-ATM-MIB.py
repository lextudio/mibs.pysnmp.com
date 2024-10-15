# SNMP MIB module (XYLAN-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:54 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(LecDataFrameSize,
 lecIndex) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "LecDataFrameSize",
    "lecIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanAtmArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanAtmArch")


# MODULE-IDENTITY


# Types definitions



class AtmAdminStatCodes(Integer32):
    """Custom type AtmAdminStatCodes based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 1),
          ("enable", 2))
    )





class AtmOperStatCodes(Integer32):
    """Custom type AtmOperStatCodes based on Integer32"""
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
        *(("inService", 2),
          ("loopBack", 4),
          ("other", 1),
          ("outOfService", 3))
    )





class AtmServiceOperStatCodes(Integer32):
    """Custom type AtmServiceOperStatCodes based on Integer32"""
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
        *(("disable", 1),
          ("enabled", 3),
          ("enabling", 2),
          ("unknown", 4))
    )





class AtmConnectionOperStatCodes(Integer32):
    """Custom type AtmConnectionOperStatCodes based on Integer32"""
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
        *(("end2EndDown", 3),
          ("end2EndUp", 2),
          ("localDown", 5),
          ("localUpEnd2EndUnknown", 4),
          ("unknown", 1))
    )





class AtmTransmissionTypes(Integer32):
    """Custom type AtmTransmissionTypes based on Integer32"""
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
        *(("atm4b5b", 4),
          ("atm8b10b", 5),
          ("ds3", 3),
          ("e3", 6),
          ("sonetSTS12c", 7),
          ("sonetSTS3c", 2),
          ("unknown", 1))
    )





class AtmMediaTypes(Integer32):
    """Custom type AtmMediaTypes based on Integer32"""
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
        *(("coaxCable", 2),
          ("multiMode", 4),
          ("singleMode", 3),
          ("stp", 5),
          ("unknown", 1),
          ("utp", 6))
    )





class AtmTrafficDescrTypes(Integer32):
    """Custom type AtmTrafficDescrTypes based on Integer32"""
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
        *(("clpNoTaggingNoScr", 4),
          ("clpNoTaggingScr", 7),
          ("clpTaggingNoScr", 5),
          ("clpTaggingScr", 8),
          ("noClpNoScr", 3),
          ("noClpScr", 6),
          ("none", 1),
          ("peakrate", 2))
    )





class XylanAtmLaneAddress(DisplayString):
    """Custom type XylanAtmLaneAddress based on DisplayString"""




class VpiInteger(Integer32):
    """Custom type VpiInteger based on Integer32"""




class VciInteger(Integer32):
    """Custom type VciInteger based on Integer32"""




class LecState(Integer32):
    """Custom type LecState based on Integer32"""
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
        *(("busConnect", 6),
          ("configure", 3),
          ("initialRegistration", 5),
          ("initialState", 1),
          ("join", 4),
          ("lecsConnect", 2),
          ("operational", 7))
    )





class LecDataFrameFormat(Integer32):
    """Custom type LecDataFrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aflane8023", 2),
          ("aflane8025", 3),
          ("unspecified", 1))
    )





class LeArpTableEntryType(Integer32):
    """Custom type LeArpTableEntryType based on Integer32"""
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
        *(("learnedViaControl", 2),
          ("learnedViaData", 3),
          ("other", 1),
          ("staticNonVolatile", 5),
          ("staticVolatile", 4))
    )





class LeArpType(Integer32):
    """Custom type LeArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arpEsiType", 3),
          ("arpRdType", 2),
          ("other", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmxPortGroup_ObjectIdentity = ObjectIdentity
atmxPortGroup = _AtmxPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1)
)
_AtmxPortTable_Object = MibTable
atmxPortTable = _AtmxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    atmxPortTable.setStatus("mandatory")
_AtmxPortEntry_Object = MibTableRow
atmxPortEntry = _AtmxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1)
)
atmxPortEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxPortSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxPortPortIndex"),
)
if mibBuilder.loadTexts:
    atmxPortEntry.setStatus("mandatory")


class _AtmxPortSlotIndex_Type(Integer32):
    """Custom type atmxPortSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxPortSlotIndex_Type.__name__ = "Integer32"
_AtmxPortSlotIndex_Object = MibTableColumn
atmxPortSlotIndex = _AtmxPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 1),
    _AtmxPortSlotIndex_Type()
)
atmxPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortSlotIndex.setStatus("mandatory")


class _AtmxPortPortIndex_Type(Integer32):
    """Custom type atmxPortPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AtmxPortPortIndex_Type.__name__ = "Integer32"
_AtmxPortPortIndex_Object = MibTableColumn
atmxPortPortIndex = _AtmxPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 2),
    _AtmxPortPortIndex_Type()
)
atmxPortPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortPortIndex.setStatus("mandatory")


class _AtmxPortDescription_Type(DisplayString):
    """Custom type atmxPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxPortDescription_Type.__name__ = "DisplayString"
_AtmxPortDescription_Object = MibTableColumn
atmxPortDescription = _AtmxPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 3),
    _AtmxPortDescription_Type()
)
atmxPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortDescription.setStatus("mandatory")


class _AtmxPortConnectionType_Type(Integer32):
    """Custom type atmxPortConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_AtmxPortConnectionType_Type.__name__ = "Integer32"
_AtmxPortConnectionType_Object = MibTableColumn
atmxPortConnectionType = _AtmxPortConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 4),
    _AtmxPortConnectionType_Type()
)
atmxPortConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortConnectionType.setStatus("mandatory")
_AtmxPortTransmissionType_Type = AtmTransmissionTypes
_AtmxPortTransmissionType_Object = MibTableColumn
atmxPortTransmissionType = _AtmxPortTransmissionType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 5),
    _AtmxPortTransmissionType_Type()
)
atmxPortTransmissionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortTransmissionType.setStatus("mandatory")
_AtmxPortMediaType_Type = AtmMediaTypes
_AtmxPortMediaType_Object = MibTableColumn
atmxPortMediaType = _AtmxPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 6),
    _AtmxPortMediaType_Type()
)
atmxPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortMediaType.setStatus("mandatory")
_AtmxPortOperStatus_Type = AtmOperStatCodes
_AtmxPortOperStatus_Object = MibTableColumn
atmxPortOperStatus = _AtmxPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 7),
    _AtmxPortOperStatus_Type()
)
atmxPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortOperStatus.setStatus("mandatory")


class _AtmxPortUniType_Type(Integer32):
    """Custom type atmxPortUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_AtmxPortUniType_Type.__name__ = "Integer32"
_AtmxPortUniType_Object = MibTableColumn
atmxPortUniType = _AtmxPortUniType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 8),
    _AtmxPortUniType_Type()
)
atmxPortUniType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortUniType.setStatus("mandatory")


class _AtmxPortMaxVCCs_Type(Integer32):
    """Custom type atmxPortMaxVCCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AtmxPortMaxVCCs_Type.__name__ = "Integer32"
_AtmxPortMaxVCCs_Object = MibTableColumn
atmxPortMaxVCCs = _AtmxPortMaxVCCs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 9),
    _AtmxPortMaxVCCs_Type()
)
atmxPortMaxVCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortMaxVCCs.setStatus("mandatory")


class _AtmxPortMaxVciBits_Type(Integer32):
    """Custom type atmxPortMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AtmxPortMaxVciBits_Type.__name__ = "Integer32"
_AtmxPortMaxVciBits_Object = MibTableColumn
atmxPortMaxVciBits = _AtmxPortMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 10),
    _AtmxPortMaxVciBits_Type()
)
atmxPortMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortMaxVciBits.setStatus("mandatory")


class _AtmxPortTxSegmentSize_Type(Integer32):
    """Custom type atmxPortTxSegmentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 131072),
    )


_AtmxPortTxSegmentSize_Type.__name__ = "Integer32"
_AtmxPortTxSegmentSize_Object = MibTableColumn
atmxPortTxSegmentSize = _AtmxPortTxSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 11),
    _AtmxPortTxSegmentSize_Type()
)
atmxPortTxSegmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortTxSegmentSize.setStatus("mandatory")


class _AtmxPortRxSegmentSize_Type(Integer32):
    """Custom type atmxPortRxSegmentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 131072),
    )


_AtmxPortRxSegmentSize_Type.__name__ = "Integer32"
_AtmxPortRxSegmentSize_Object = MibTableColumn
atmxPortRxSegmentSize = _AtmxPortRxSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 12),
    _AtmxPortRxSegmentSize_Type()
)
atmxPortRxSegmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortRxSegmentSize.setStatus("mandatory")


class _AtmxPortTxBufferSize_Type(Integer32):
    """Custom type atmxPortTxBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 131072),
    )


_AtmxPortTxBufferSize_Type.__name__ = "Integer32"
_AtmxPortTxBufferSize_Object = MibTableColumn
atmxPortTxBufferSize = _AtmxPortTxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 13),
    _AtmxPortTxBufferSize_Type()
)
atmxPortTxBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortTxBufferSize.setStatus("mandatory")


class _AtmxPortRxBufferSize_Type(Integer32):
    """Custom type atmxPortRxBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 131072),
    )


_AtmxPortRxBufferSize_Type.__name__ = "Integer32"
_AtmxPortRxBufferSize_Object = MibTableColumn
atmxPortRxBufferSize = _AtmxPortRxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 14),
    _AtmxPortRxBufferSize_Type()
)
atmxPortRxBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortRxBufferSize.setStatus("mandatory")


class _AtmxPortUniPortIndex_Type(Integer32):
    """Custom type atmxPortUniPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmxPortUniPortIndex_Type.__name__ = "Integer32"
_AtmxPortUniPortIndex_Object = MibTableColumn
atmxPortUniPortIndex = _AtmxPortUniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 15),
    _AtmxPortUniPortIndex_Type()
)
atmxPortUniPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortUniPortIndex.setStatus("deprecated")


class _AtmxPortAddress_Type(DisplayString):
    """Custom type atmxPortAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AtmxPortAddress_Type.__name__ = "DisplayString"
_AtmxPortAddress_Object = MibTableColumn
atmxPortAddress = _AtmxPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 16),
    _AtmxPortAddress_Type()
)
atmxPortAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortAddress.setStatus("mandatory")


class _AtmxPortSignalingVersion_Type(Integer32):
    """Custom type atmxPortSignalingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ver30", 1),
          ("ver31", 2))
    )


_AtmxPortSignalingVersion_Type.__name__ = "Integer32"
_AtmxPortSignalingVersion_Object = MibTableColumn
atmxPortSignalingVersion = _AtmxPortSignalingVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 17),
    _AtmxPortSignalingVersion_Type()
)
atmxPortSignalingVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortSignalingVersion.setStatus("mandatory")


class _AtmxPortSignalingVci_Type(Integer32):
    """Custom type atmxPortSignalingVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AtmxPortSignalingVci_Type.__name__ = "Integer32"
_AtmxPortSignalingVci_Object = MibTableColumn
atmxPortSignalingVci = _AtmxPortSignalingVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 18),
    _AtmxPortSignalingVci_Type()
)
atmxPortSignalingVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortSignalingVci.setStatus("mandatory")


class _AtmxPortILMIVci_Type(Integer32):
    """Custom type atmxPortILMIVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AtmxPortILMIVci_Type.__name__ = "Integer32"
_AtmxPortILMIVci_Object = MibTableColumn
atmxPortILMIVci = _AtmxPortILMIVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 19),
    _AtmxPortILMIVci_Type()
)
atmxPortILMIVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortILMIVci.setStatus("mandatory")


class _AtmxPortEnableILMI_Type(Integer32):
    """Custom type atmxPortEnableILMI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxPortEnableILMI_Type.__name__ = "Integer32"
_AtmxPortEnableILMI_Object = MibTableColumn
atmxPortEnableILMI = _AtmxPortEnableILMI_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 20),
    _AtmxPortEnableILMI_Type()
)
atmxPortEnableILMI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortEnableILMI.setStatus("mandatory")


class _AtmxPortPlScramble_Type(Integer32):
    """Custom type atmxPortPlScramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxPortPlScramble_Type.__name__ = "Integer32"
_AtmxPortPlScramble_Object = MibTableColumn
atmxPortPlScramble = _AtmxPortPlScramble_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 21),
    _AtmxPortPlScramble_Type()
)
atmxPortPlScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortPlScramble.setStatus("mandatory")


class _AtmxPortTimingMode_Type(Integer32):
    """Custom type atmxPortTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("loop", 1))
    )


_AtmxPortTimingMode_Type.__name__ = "Integer32"
_AtmxPortTimingMode_Object = MibTableColumn
atmxPortTimingMode = _AtmxPortTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 22),
    _AtmxPortTimingMode_Type()
)
atmxPortTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortTimingMode.setStatus("mandatory")


class _AtmxPortProtocolType_Type(Integer32):
    """Custom type atmxPortProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 3),
          ("sdh", 2),
          ("sonet", 1))
    )


_AtmxPortProtocolType_Type.__name__ = "Integer32"
_AtmxPortProtocolType_Object = MibTableColumn
atmxPortProtocolType = _AtmxPortProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 23),
    _AtmxPortProtocolType_Type()
)
atmxPortProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortProtocolType.setStatus("mandatory")


class _AtmxPortLoopbackConfig_Type(Integer32):
    """Custom type atmxPortLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AtmxPortLoopbackConfig_Type.__name__ = "Integer32"
_AtmxPortLoopbackConfig_Object = MibTableColumn
atmxPortLoopbackConfig = _AtmxPortLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 24),
    _AtmxPortLoopbackConfig_Type()
)
atmxPortLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortLoopbackConfig.setStatus("mandatory")


class _AtmxPortSSCOPstatus_Type(Integer32):
    """Custom type atmxPortSSCOPstatus based on Integer32"""
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


_AtmxPortSSCOPstatus_Type.__name__ = "Integer32"
_AtmxPortSSCOPstatus_Object = MibTableColumn
atmxPortSSCOPstatus = _AtmxPortSSCOPstatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 25),
    _AtmxPortSSCOPstatus_Type()
)
atmxPortSSCOPstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortSSCOPstatus.setStatus("mandatory")


class _AtmxPortILMIstatus_Type(Integer32):
    """Custom type atmxPortILMIstatus based on Integer32"""
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


_AtmxPortILMIstatus_Type.__name__ = "Integer32"
_AtmxPortILMIstatus_Object = MibTableColumn
atmxPortILMIstatus = _AtmxPortILMIstatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 1, 1, 1, 26),
    _AtmxPortILMIstatus_Type()
)
atmxPortILMIstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortILMIstatus.setStatus("mandatory")
_AtmxServiceGroup_ObjectIdentity = ObjectIdentity
atmxServiceGroup = _AtmxServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2)
)
_AtmxServiceTable_Object = MibTable
atmxServiceTable = _AtmxServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    atmxServiceTable.setStatus("mandatory")
_AtmxServiceEntry_Object = MibTableRow
atmxServiceEntry = _AtmxServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1)
)
atmxServiceEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxServiceSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxServicePortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxServiceNumber"),
)
if mibBuilder.loadTexts:
    atmxServiceEntry.setStatus("mandatory")


class _AtmxServiceSlotIndex_Type(Integer32):
    """Custom type atmxServiceSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxServiceSlotIndex_Type.__name__ = "Integer32"
_AtmxServiceSlotIndex_Object = MibTableColumn
atmxServiceSlotIndex = _AtmxServiceSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 1),
    _AtmxServiceSlotIndex_Type()
)
atmxServiceSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceSlotIndex.setStatus("mandatory")


class _AtmxServicePortIndex_Type(Integer32):
    """Custom type atmxServicePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AtmxServicePortIndex_Type.__name__ = "Integer32"
_AtmxServicePortIndex_Object = MibTableColumn
atmxServicePortIndex = _AtmxServicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 2),
    _AtmxServicePortIndex_Type()
)
atmxServicePortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServicePortIndex.setStatus("mandatory")


class _AtmxServiceNumber_Type(Integer32):
    """Custom type atmxServiceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AtmxServiceNumber_Type.__name__ = "Integer32"
_AtmxServiceNumber_Object = MibTableColumn
atmxServiceNumber = _AtmxServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 3),
    _AtmxServiceNumber_Type()
)
atmxServiceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceNumber.setStatus("mandatory")


class _AtmxServiceDescription_Type(DisplayString):
    """Custom type atmxServiceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxServiceDescription_Type.__name__ = "DisplayString"
_AtmxServiceDescription_Object = MibTableColumn
atmxServiceDescription = _AtmxServiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 4),
    _AtmxServiceDescription_Type()
)
atmxServiceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceDescription.setStatus("mandatory")


class _AtmxServiceType_Type(Integer32):
    """Custom type atmxServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("classicalIP", 5),
          ("lanEmulation", 1),
          ("laneServiceModule", 8),
          ("mpoaClient", 9),
          ("ptopBridging", 6),
          ("scaling1483", 2),
          ("trunking", 4),
          ("vlanCluster", 7))
    )


_AtmxServiceType_Type.__name__ = "Integer32"
_AtmxServiceType_Object = MibTableColumn
atmxServiceType = _AtmxServiceType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 5),
    _AtmxServiceType_Type()
)
atmxServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceType.setStatus("mandatory")


class _AtmxServiceConnectionType_Type(Integer32):
    """Custom type atmxServiceConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_AtmxServiceConnectionType_Type.__name__ = "Integer32"
_AtmxServiceConnectionType_Object = MibTableColumn
atmxServiceConnectionType = _AtmxServiceConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 6),
    _AtmxServiceConnectionType_Type()
)
atmxServiceConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceConnectionType.setStatus("mandatory")
_AtmxServiceOperStatus_Type = AtmServiceOperStatCodes
_AtmxServiceOperStatus_Object = MibTableColumn
atmxServiceOperStatus = _AtmxServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 7),
    _AtmxServiceOperStatus_Type()
)
atmxServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxServiceOperStatus.setStatus("mandatory")
_AtmxServiceAdmStatus_Type = AtmAdminStatCodes
_AtmxServiceAdmStatus_Object = MibTableColumn
atmxServiceAdmStatus = _AtmxServiceAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 8),
    _AtmxServiceAdmStatus_Type()
)
atmxServiceAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceAdmStatus.setStatus("mandatory")


class _AtmxServiceEncapsType_Type(Integer32):
    """Custom type atmxServiceEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("private", 1),
          ("rfc1483", 2))
    )


_AtmxServiceEncapsType_Type.__name__ = "Integer32"
_AtmxServiceEncapsType_Object = MibTableColumn
atmxServiceEncapsType = _AtmxServiceEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 9),
    _AtmxServiceEncapsType_Type()
)
atmxServiceEncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceEncapsType.setStatus("mandatory")


class _AtmxServiceArpRequestServer_Type(Integer32):
    """Custom type atmxServiceArpRequestServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AtmxServiceArpRequestServer_Type.__name__ = "Integer32"
_AtmxServiceArpRequestServer_Object = MibTableColumn
atmxServiceArpRequestServer = _AtmxServiceArpRequestServer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 10),
    _AtmxServiceArpRequestServer_Type()
)
atmxServiceArpRequestServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceArpRequestServer.setStatus("mandatory")


class _AtmxServiceConnections_Type(OctetString):
    """Custom type atmxServiceConnections based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AtmxServiceConnections_Type.__name__ = "OctetString"
_AtmxServiceConnections_Object = MibTableColumn
atmxServiceConnections = _AtmxServiceConnections_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 11),
    _AtmxServiceConnections_Type()
)
atmxServiceConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceConnections.setStatus("mandatory")


class _AtmxServiceAddress_Type(DisplayString):
    """Custom type atmxServiceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AtmxServiceAddress_Type.__name__ = "DisplayString"
_AtmxServiceAddress_Object = MibTableColumn
atmxServiceAddress = _AtmxServiceAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 12),
    _AtmxServiceAddress_Type()
)
atmxServiceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceAddress.setStatus("mandatory")


class _AtmxServiceAddresses_Type(OctetString):
    """Custom type atmxServiceAddresses based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AtmxServiceAddresses_Type.__name__ = "OctetString"
_AtmxServiceAddresses_Object = MibTableColumn
atmxServiceAddresses = _AtmxServiceAddresses_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 13),
    _AtmxServiceAddresses_Type()
)
atmxServiceAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceAddresses.setStatus("mandatory")


class _AtmxServiceVlan_Type(OctetString):
    """Custom type atmxServiceVlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AtmxServiceVlan_Type.__name__ = "OctetString"
_AtmxServiceVlan_Object = MibTableColumn
atmxServiceVlan = _AtmxServiceVlan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 14),
    _AtmxServiceVlan_Type()
)
atmxServiceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceVlan.setStatus("mandatory")


class _AtmxServiceSEL_Type(Integer32):
    """Custom type atmxServiceSEL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmxServiceSEL_Type.__name__ = "Integer32"
_AtmxServiceSEL_Object = MibTableColumn
atmxServiceSEL = _AtmxServiceSEL_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 15),
    _AtmxServiceSEL_Type()
)
atmxServiceSEL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceSEL.setStatus("mandatory")


class _AtmxServiceLaneCfgTblIdx_Type(Integer32):
    """Custom type atmxServiceLaneCfgTblIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmxServiceLaneCfgTblIdx_Type.__name__ = "Integer32"
_AtmxServiceLaneCfgTblIdx_Object = MibTableColumn
atmxServiceLaneCfgTblIdx = _AtmxServiceLaneCfgTblIdx_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 16),
    _AtmxServiceLaneCfgTblIdx_Type()
)
atmxServiceLaneCfgTblIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceLaneCfgTblIdx.setStatus("mandatory")


class _AtmxServiceMulticastOutVcc_Type(Integer32):
    """Custom type atmxServiceMulticastOutVcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AtmxServiceMulticastOutVcc_Type.__name__ = "Integer32"
_AtmxServiceMulticastOutVcc_Object = MibTableColumn
atmxServiceMulticastOutVcc = _AtmxServiceMulticastOutVcc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 17),
    _AtmxServiceMulticastOutVcc_Type()
)
atmxServiceMulticastOutVcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceMulticastOutVcc.setStatus("mandatory")


class _AtmxServiceNumVclMembers_Type(Integer32):
    """Custom type atmxServiceNumVclMembers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmxServiceNumVclMembers_Type.__name__ = "Integer32"
_AtmxServiceNumVclMembers_Object = MibTableColumn
atmxServiceNumVclMembers = _AtmxServiceNumVclMembers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 18),
    _AtmxServiceNumVclMembers_Type()
)
atmxServiceNumVclMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceNumVclMembers.setStatus("mandatory")


class _AtmxServiceVclEncapType_Type(Integer32):
    """Custom type atmxServiceVclEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AtmxServiceVclEncapType_Type.__name__ = "Integer32"
_AtmxServiceVclEncapType_Object = MibTableColumn
atmxServiceVclEncapType = _AtmxServiceVclEncapType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 19),
    _AtmxServiceVclEncapType_Type()
)
atmxServiceVclEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceVclEncapType.setStatus("mandatory")


class _AtmxServiceSahiBwgNum_Type(Integer32):
    """Custom type atmxServiceSahiBwgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtmxServiceSahiBwgNum_Type.__name__ = "Integer32"
_AtmxServiceSahiBwgNum_Object = MibTableColumn
atmxServiceSahiBwgNum = _AtmxServiceSahiBwgNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 2, 1, 1, 20),
    _AtmxServiceSahiBwgNum_Type()
)
atmxServiceSahiBwgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxServiceSahiBwgNum.setStatus("mandatory")
_AtmxLayerStatsGroup_ObjectIdentity = ObjectIdentity
atmxLayerStatsGroup = _AtmxLayerStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3)
)
_AtmxLayerStatsTable_Object = MibTable
atmxLayerStatsTable = _AtmxLayerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    atmxLayerStatsTable.setStatus("mandatory")
_AtmxLayerStatsEntry_Object = MibTableRow
atmxLayerStatsEntry = _AtmxLayerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1)
)
atmxLayerStatsEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxLayerStatsSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxLayerStatsPortIndex"),
)
if mibBuilder.loadTexts:
    atmxLayerStatsEntry.setStatus("mandatory")


class _AtmxLayerStatsSlotIndex_Type(Integer32):
    """Custom type atmxLayerStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxLayerStatsSlotIndex_Type.__name__ = "Integer32"
_AtmxLayerStatsSlotIndex_Object = MibTableColumn
atmxLayerStatsSlotIndex = _AtmxLayerStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 1),
    _AtmxLayerStatsSlotIndex_Type()
)
atmxLayerStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsSlotIndex.setStatus("mandatory")


class _AtmxLayerStatsPortIndex_Type(Integer32):
    """Custom type atmxLayerStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AtmxLayerStatsPortIndex_Type.__name__ = "Integer32"
_AtmxLayerStatsPortIndex_Object = MibTableColumn
atmxLayerStatsPortIndex = _AtmxLayerStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 2),
    _AtmxLayerStatsPortIndex_Type()
)
atmxLayerStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsPortIndex.setStatus("mandatory")
_AtmxLayerStatsTxSDUs_Type = Counter32
_AtmxLayerStatsTxSDUs_Object = MibTableColumn
atmxLayerStatsTxSDUs = _AtmxLayerStatsTxSDUs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 3),
    _AtmxLayerStatsTxSDUs_Type()
)
atmxLayerStatsTxSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxSDUs.setStatus("mandatory")
_AtmxLayerStatsTxCells_Type = Counter32
_AtmxLayerStatsTxCells_Object = MibTableColumn
atmxLayerStatsTxCells = _AtmxLayerStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 4),
    _AtmxLayerStatsTxCells_Type()
)
atmxLayerStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxCells.setStatus("mandatory")
_AtmxLayerStatsTxOctets_Type = Counter32
_AtmxLayerStatsTxOctets_Object = MibTableColumn
atmxLayerStatsTxOctets = _AtmxLayerStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 5),
    _AtmxLayerStatsTxOctets_Type()
)
atmxLayerStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxOctets.setStatus("mandatory")
_AtmxLayerStatsRxSDUs_Type = Counter32
_AtmxLayerStatsRxSDUs_Object = MibTableColumn
atmxLayerStatsRxSDUs = _AtmxLayerStatsRxSDUs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 6),
    _AtmxLayerStatsRxSDUs_Type()
)
atmxLayerStatsRxSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxSDUs.setStatus("mandatory")
_AtmxLayerStatsRxCells_Type = Counter32
_AtmxLayerStatsRxCells_Object = MibTableColumn
atmxLayerStatsRxCells = _AtmxLayerStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 7),
    _AtmxLayerStatsRxCells_Type()
)
atmxLayerStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxCells.setStatus("mandatory")
_AtmxLayerStatsRxOctets_Type = Counter32
_AtmxLayerStatsRxOctets_Object = MibTableColumn
atmxLayerStatsRxOctets = _AtmxLayerStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 8),
    _AtmxLayerStatsRxOctets_Type()
)
atmxLayerStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxOctets.setStatus("mandatory")
_AtmxLayerStatsTxSDUDiscards_Type = Counter32
_AtmxLayerStatsTxSDUDiscards_Object = MibTableColumn
atmxLayerStatsTxSDUDiscards = _AtmxLayerStatsTxSDUDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 9),
    _AtmxLayerStatsTxSDUDiscards_Type()
)
atmxLayerStatsTxSDUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxSDUDiscards.setStatus("mandatory")
_AtmxLayerStatsTxSDUErrors_Type = Counter32
_AtmxLayerStatsTxSDUErrors_Object = MibTableColumn
atmxLayerStatsTxSDUErrors = _AtmxLayerStatsTxSDUErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 10),
    _AtmxLayerStatsTxSDUErrors_Type()
)
atmxLayerStatsTxSDUErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxSDUErrors.setStatus("mandatory")
_AtmxLayerStatsTxSDUNoBuffers_Type = Counter32
_AtmxLayerStatsTxSDUNoBuffers_Object = MibTableColumn
atmxLayerStatsTxSDUNoBuffers = _AtmxLayerStatsTxSDUNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 11),
    _AtmxLayerStatsTxSDUNoBuffers_Type()
)
atmxLayerStatsTxSDUNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxSDUNoBuffers.setStatus("mandatory")
_AtmxLayerStatsTxCellDiscards_Type = Counter32
_AtmxLayerStatsTxCellDiscards_Object = MibTableColumn
atmxLayerStatsTxCellDiscards = _AtmxLayerStatsTxCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 12),
    _AtmxLayerStatsTxCellDiscards_Type()
)
atmxLayerStatsTxCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxCellDiscards.setStatus("mandatory")
_AtmxLayerStatsTxCellErrors_Type = Counter32
_AtmxLayerStatsTxCellErrors_Object = MibTableColumn
atmxLayerStatsTxCellErrors = _AtmxLayerStatsTxCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 13),
    _AtmxLayerStatsTxCellErrors_Type()
)
atmxLayerStatsTxCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxCellErrors.setStatus("mandatory")
_AtmxLayerStatsTxCellNoBuffers_Type = Counter32
_AtmxLayerStatsTxCellNoBuffers_Object = MibTableColumn
atmxLayerStatsTxCellNoBuffers = _AtmxLayerStatsTxCellNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 14),
    _AtmxLayerStatsTxCellNoBuffers_Type()
)
atmxLayerStatsTxCellNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxCellNoBuffers.setStatus("mandatory")
_AtmxLayerStatsRxSDUDiscards_Type = Counter32
_AtmxLayerStatsRxSDUDiscards_Object = MibTableColumn
atmxLayerStatsRxSDUDiscards = _AtmxLayerStatsRxSDUDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 15),
    _AtmxLayerStatsRxSDUDiscards_Type()
)
atmxLayerStatsRxSDUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxSDUDiscards.setStatus("mandatory")
_AtmxLayerStatsRxSDUErrors_Type = Counter32
_AtmxLayerStatsRxSDUErrors_Object = MibTableColumn
atmxLayerStatsRxSDUErrors = _AtmxLayerStatsRxSDUErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 16),
    _AtmxLayerStatsRxSDUErrors_Type()
)
atmxLayerStatsRxSDUErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxSDUErrors.setStatus("mandatory")
_AtmxLayerStatsRxSDUInvalidSz_Type = Counter32
_AtmxLayerStatsRxSDUInvalidSz_Object = MibTableColumn
atmxLayerStatsRxSDUInvalidSz = _AtmxLayerStatsRxSDUInvalidSz_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 17),
    _AtmxLayerStatsRxSDUInvalidSz_Type()
)
atmxLayerStatsRxSDUInvalidSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxSDUInvalidSz.setStatus("mandatory")
_AtmxLayerStatsRxSDUNoBuffers_Type = Counter32
_AtmxLayerStatsRxSDUNoBuffers_Object = MibTableColumn
atmxLayerStatsRxSDUNoBuffers = _AtmxLayerStatsRxSDUNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 18),
    _AtmxLayerStatsRxSDUNoBuffers_Type()
)
atmxLayerStatsRxSDUNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxSDUNoBuffers.setStatus("mandatory")
_AtmxLayerStatsRxSDUTrash_Type = Counter32
_AtmxLayerStatsRxSDUTrash_Object = MibTableColumn
atmxLayerStatsRxSDUTrash = _AtmxLayerStatsRxSDUTrash_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 19),
    _AtmxLayerStatsRxSDUTrash_Type()
)
atmxLayerStatsRxSDUTrash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxSDUTrash.setStatus("mandatory")
_AtmxLayerStatsRxSDUCrcErrors_Type = Counter32
_AtmxLayerStatsRxSDUCrcErrors_Object = MibTableColumn
atmxLayerStatsRxSDUCrcErrors = _AtmxLayerStatsRxSDUCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 20),
    _AtmxLayerStatsRxSDUCrcErrors_Type()
)
atmxLayerStatsRxSDUCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxSDUCrcErrors.setStatus("mandatory")
_AtmxLayerStatsRxCellDiscards_Type = Counter32
_AtmxLayerStatsRxCellDiscards_Object = MibTableColumn
atmxLayerStatsRxCellDiscards = _AtmxLayerStatsRxCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 21),
    _AtmxLayerStatsRxCellDiscards_Type()
)
atmxLayerStatsRxCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxCellDiscards.setStatus("mandatory")
_AtmxLayerStatsRxCellErrors_Type = Counter32
_AtmxLayerStatsRxCellErrors_Object = MibTableColumn
atmxLayerStatsRxCellErrors = _AtmxLayerStatsRxCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 22),
    _AtmxLayerStatsRxCellErrors_Type()
)
atmxLayerStatsRxCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxCellErrors.setStatus("mandatory")
_AtmxLayerStatsRxCellNoBuffers_Type = Counter32
_AtmxLayerStatsRxCellNoBuffers_Object = MibTableColumn
atmxLayerStatsRxCellNoBuffers = _AtmxLayerStatsRxCellNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 23),
    _AtmxLayerStatsRxCellNoBuffers_Type()
)
atmxLayerStatsRxCellNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxCellNoBuffers.setStatus("mandatory")
_AtmxLayerStatsRxCellTrash_Type = Counter32
_AtmxLayerStatsRxCellTrash_Object = MibTableColumn
atmxLayerStatsRxCellTrash = _AtmxLayerStatsRxCellTrash_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 24),
    _AtmxLayerStatsRxCellTrash_Type()
)
atmxLayerStatsRxCellTrash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxCellTrash.setStatus("mandatory")
_AtmxLayerStatsRxCellCrcErrors_Type = Counter32
_AtmxLayerStatsRxCellCrcErrors_Object = MibTableColumn
atmxLayerStatsRxCellCrcErrors = _AtmxLayerStatsRxCellCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 3, 1, 1, 25),
    _AtmxLayerStatsRxCellCrcErrors_Type()
)
atmxLayerStatsRxCellCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxCellCrcErrors.setStatus("mandatory")
_AtmxVccStatsGroup_ObjectIdentity = ObjectIdentity
atmxVccStatsGroup = _AtmxVccStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4)
)
_AtmxVccStatsTable_Object = MibTable
atmxVccStatsTable = _AtmxVccStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    atmxVccStatsTable.setStatus("mandatory")
_AtmxVccStatsEntry_Object = MibTableRow
atmxVccStatsEntry = _AtmxVccStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1)
)
atmxVccStatsEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxVccStatsSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxVccStatsPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxVccStatsVci"),
)
if mibBuilder.loadTexts:
    atmxVccStatsEntry.setStatus("mandatory")


class _AtmxVccStatsSlotIndex_Type(Integer32):
    """Custom type atmxVccStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxVccStatsSlotIndex_Type.__name__ = "Integer32"
_AtmxVccStatsSlotIndex_Object = MibTableColumn
atmxVccStatsSlotIndex = _AtmxVccStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 1),
    _AtmxVccStatsSlotIndex_Type()
)
atmxVccStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsSlotIndex.setStatus("mandatory")


class _AtmxVccStatsPortIndex_Type(Integer32):
    """Custom type atmxVccStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AtmxVccStatsPortIndex_Type.__name__ = "Integer32"
_AtmxVccStatsPortIndex_Object = MibTableColumn
atmxVccStatsPortIndex = _AtmxVccStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 2),
    _AtmxVccStatsPortIndex_Type()
)
atmxVccStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsPortIndex.setStatus("mandatory")


class _AtmxVccStatsVci_Type(Integer32):
    """Custom type atmxVccStatsVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AtmxVccStatsVci_Type.__name__ = "Integer32"
_AtmxVccStatsVci_Object = MibTableColumn
atmxVccStatsVci = _AtmxVccStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 3),
    _AtmxVccStatsVci_Type()
)
atmxVccStatsVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsVci.setStatus("mandatory")
_AtmxVccStatsTxSDUs_Type = Counter32
_AtmxVccStatsTxSDUs_Object = MibTableColumn
atmxVccStatsTxSDUs = _AtmxVccStatsTxSDUs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 4),
    _AtmxVccStatsTxSDUs_Type()
)
atmxVccStatsTxSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxSDUs.setStatus("mandatory")
_AtmxVccStatsTxCells_Type = Counter32
_AtmxVccStatsTxCells_Object = MibTableColumn
atmxVccStatsTxCells = _AtmxVccStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 5),
    _AtmxVccStatsTxCells_Type()
)
atmxVccStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxCells.setStatus("mandatory")
_AtmxVccStatsTxOctets_Type = Counter32
_AtmxVccStatsTxOctets_Object = MibTableColumn
atmxVccStatsTxOctets = _AtmxVccStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 6),
    _AtmxVccStatsTxOctets_Type()
)
atmxVccStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxOctets.setStatus("mandatory")
_AtmxVccStatsRxSDUs_Type = Counter32
_AtmxVccStatsRxSDUs_Object = MibTableColumn
atmxVccStatsRxSDUs = _AtmxVccStatsRxSDUs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 7),
    _AtmxVccStatsRxSDUs_Type()
)
atmxVccStatsRxSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxSDUs.setStatus("mandatory")
_AtmxVccStatsRxCells_Type = Counter32
_AtmxVccStatsRxCells_Object = MibTableColumn
atmxVccStatsRxCells = _AtmxVccStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 8),
    _AtmxVccStatsRxCells_Type()
)
atmxVccStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxCells.setStatus("mandatory")
_AtmxVccStatsRxOctets_Type = Counter32
_AtmxVccStatsRxOctets_Object = MibTableColumn
atmxVccStatsRxOctets = _AtmxVccStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 9),
    _AtmxVccStatsRxOctets_Type()
)
atmxVccStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxOctets.setStatus("mandatory")
_AtmxVccStatsTxSDUDiscards_Type = Counter32
_AtmxVccStatsTxSDUDiscards_Object = MibTableColumn
atmxVccStatsTxSDUDiscards = _AtmxVccStatsTxSDUDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 10),
    _AtmxVccStatsTxSDUDiscards_Type()
)
atmxVccStatsTxSDUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxSDUDiscards.setStatus("mandatory")
_AtmxVccStatsTxSDUErrors_Type = Counter32
_AtmxVccStatsTxSDUErrors_Object = MibTableColumn
atmxVccStatsTxSDUErrors = _AtmxVccStatsTxSDUErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 11),
    _AtmxVccStatsTxSDUErrors_Type()
)
atmxVccStatsTxSDUErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxSDUErrors.setStatus("mandatory")
_AtmxVccStatsTxSDUNoBuffers_Type = Counter32
_AtmxVccStatsTxSDUNoBuffers_Object = MibTableColumn
atmxVccStatsTxSDUNoBuffers = _AtmxVccStatsTxSDUNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 12),
    _AtmxVccStatsTxSDUNoBuffers_Type()
)
atmxVccStatsTxSDUNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxSDUNoBuffers.setStatus("mandatory")
_AtmxVccStatsTxCellDiscards_Type = Counter32
_AtmxVccStatsTxCellDiscards_Object = MibTableColumn
atmxVccStatsTxCellDiscards = _AtmxVccStatsTxCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 13),
    _AtmxVccStatsTxCellDiscards_Type()
)
atmxVccStatsTxCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxCellDiscards.setStatus("mandatory")
_AtmxVccStatsTxCellErrors_Type = Counter32
_AtmxVccStatsTxCellErrors_Object = MibTableColumn
atmxVccStatsTxCellErrors = _AtmxVccStatsTxCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 14),
    _AtmxVccStatsTxCellErrors_Type()
)
atmxVccStatsTxCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxCellErrors.setStatus("mandatory")
_AtmxVccStatsTxCellNoBuffers_Type = Counter32
_AtmxVccStatsTxCellNoBuffers_Object = MibTableColumn
atmxVccStatsTxCellNoBuffers = _AtmxVccStatsTxCellNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 15),
    _AtmxVccStatsTxCellNoBuffers_Type()
)
atmxVccStatsTxCellNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxCellNoBuffers.setStatus("mandatory")
_AtmxVccStatsRxSDUDiscards_Type = Counter32
_AtmxVccStatsRxSDUDiscards_Object = MibTableColumn
atmxVccStatsRxSDUDiscards = _AtmxVccStatsRxSDUDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 16),
    _AtmxVccStatsRxSDUDiscards_Type()
)
atmxVccStatsRxSDUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxSDUDiscards.setStatus("mandatory")
_AtmxVccStatsRxSDUErrors_Type = Counter32
_AtmxVccStatsRxSDUErrors_Object = MibTableColumn
atmxVccStatsRxSDUErrors = _AtmxVccStatsRxSDUErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 17),
    _AtmxVccStatsRxSDUErrors_Type()
)
atmxVccStatsRxSDUErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxSDUErrors.setStatus("mandatory")
_AtmxVccStatsRxSDUInvalidSz_Type = Counter32
_AtmxVccStatsRxSDUInvalidSz_Object = MibTableColumn
atmxVccStatsRxSDUInvalidSz = _AtmxVccStatsRxSDUInvalidSz_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 18),
    _AtmxVccStatsRxSDUInvalidSz_Type()
)
atmxVccStatsRxSDUInvalidSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxSDUInvalidSz.setStatus("mandatory")
_AtmxVccStatsRxSDUNoBuffers_Type = Counter32
_AtmxVccStatsRxSDUNoBuffers_Object = MibTableColumn
atmxVccStatsRxSDUNoBuffers = _AtmxVccStatsRxSDUNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 19),
    _AtmxVccStatsRxSDUNoBuffers_Type()
)
atmxVccStatsRxSDUNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxSDUNoBuffers.setStatus("mandatory")
_AtmxVccStatsRxSDUTrash_Type = Counter32
_AtmxVccStatsRxSDUTrash_Object = MibTableColumn
atmxVccStatsRxSDUTrash = _AtmxVccStatsRxSDUTrash_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 20),
    _AtmxVccStatsRxSDUTrash_Type()
)
atmxVccStatsRxSDUTrash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxSDUTrash.setStatus("mandatory")
_AtmxVccStatsRxSDUCrcErrors_Type = Counter32
_AtmxVccStatsRxSDUCrcErrors_Object = MibTableColumn
atmxVccStatsRxSDUCrcErrors = _AtmxVccStatsRxSDUCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 21),
    _AtmxVccStatsRxSDUCrcErrors_Type()
)
atmxVccStatsRxSDUCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxSDUCrcErrors.setStatus("mandatory")
_AtmxVccStatsRxCellDiscards_Type = Counter32
_AtmxVccStatsRxCellDiscards_Object = MibTableColumn
atmxVccStatsRxCellDiscards = _AtmxVccStatsRxCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 22),
    _AtmxVccStatsRxCellDiscards_Type()
)
atmxVccStatsRxCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxCellDiscards.setStatus("mandatory")
_AtmxVccStatsRxCellErrors_Type = Counter32
_AtmxVccStatsRxCellErrors_Object = MibTableColumn
atmxVccStatsRxCellErrors = _AtmxVccStatsRxCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 23),
    _AtmxVccStatsRxCellErrors_Type()
)
atmxVccStatsRxCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxCellErrors.setStatus("mandatory")
_AtmxVccStatsRxCellNoBuffers_Type = Counter32
_AtmxVccStatsRxCellNoBuffers_Object = MibTableColumn
atmxVccStatsRxCellNoBuffers = _AtmxVccStatsRxCellNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 24),
    _AtmxVccStatsRxCellNoBuffers_Type()
)
atmxVccStatsRxCellNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxCellNoBuffers.setStatus("mandatory")
_AtmxVccStatsRxCellTrash_Type = Counter32
_AtmxVccStatsRxCellTrash_Object = MibTableColumn
atmxVccStatsRxCellTrash = _AtmxVccStatsRxCellTrash_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 25),
    _AtmxVccStatsRxCellTrash_Type()
)
atmxVccStatsRxCellTrash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxCellTrash.setStatus("mandatory")
_AtmxVccStatsRxCellCrcErrors_Type = Counter32
_AtmxVccStatsRxCellCrcErrors_Object = MibTableColumn
atmxVccStatsRxCellCrcErrors = _AtmxVccStatsRxCellCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 4, 1, 1, 26),
    _AtmxVccStatsRxCellCrcErrors_Type()
)
atmxVccStatsRxCellCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxCellCrcErrors.setStatus("mandatory")
_AtmxVccGroup_ObjectIdentity = ObjectIdentity
atmxVccGroup = _AtmxVccGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5)
)
_AtmxVccTable_Object = MibTable
atmxVccTable = _AtmxVccTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    atmxVccTable.setStatus("mandatory")
_AtmxVccEntry_Object = MibTableRow
atmxVccEntry = _AtmxVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1)
)
atmxVccEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxVccSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxVccPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxVccVci"),
)
if mibBuilder.loadTexts:
    atmxVccEntry.setStatus("mandatory")


class _AtmxVccSlotIndex_Type(Integer32):
    """Custom type atmxVccSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxVccSlotIndex_Type.__name__ = "Integer32"
_AtmxVccSlotIndex_Object = MibTableColumn
atmxVccSlotIndex = _AtmxVccSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 1),
    _AtmxVccSlotIndex_Type()
)
atmxVccSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccSlotIndex.setStatus("mandatory")


class _AtmxVccPortIndex_Type(Integer32):
    """Custom type atmxVccPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AtmxVccPortIndex_Type.__name__ = "Integer32"
_AtmxVccPortIndex_Object = MibTableColumn
atmxVccPortIndex = _AtmxVccPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 2),
    _AtmxVccPortIndex_Type()
)
atmxVccPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccPortIndex.setStatus("mandatory")


class _AtmxVccVpi_Type(Integer32):
    """Custom type atmxVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AtmxVccVpi_Type.__name__ = "Integer32"
_AtmxVccVpi_Object = MibTableColumn
atmxVccVpi = _AtmxVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 3),
    _AtmxVccVpi_Type()
)
atmxVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccVpi.setStatus("mandatory")


class _AtmxVccVci_Type(Integer32):
    """Custom type atmxVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AtmxVccVci_Type.__name__ = "Integer32"
_AtmxVccVci_Object = MibTableColumn
atmxVccVci = _AtmxVccVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 4),
    _AtmxVccVci_Type()
)
atmxVccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccVci.setStatus("mandatory")


class _AtmxVccDescription_Type(DisplayString):
    """Custom type atmxVccDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxVccDescription_Type.__name__ = "DisplayString"
_AtmxVccDescription_Object = MibTableColumn
atmxVccDescription = _AtmxVccDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 5),
    _AtmxVccDescription_Type()
)
atmxVccDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccDescription.setStatus("mandatory")


class _AtmxVccConnType_Type(Integer32):
    """Custom type atmxVccConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcc", 1),
          ("vpc", 2))
    )


_AtmxVccConnType_Type.__name__ = "Integer32"
_AtmxVccConnType_Object = MibTableColumn
atmxVccConnType = _AtmxVccConnType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 6),
    _AtmxVccConnType_Type()
)
atmxVccConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccConnType.setStatus("mandatory")


class _AtmxVccCircuitType_Type(Integer32):
    """Custom type atmxVccCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_AtmxVccCircuitType_Type.__name__ = "Integer32"
_AtmxVccCircuitType_Object = MibTableColumn
atmxVccCircuitType = _AtmxVccCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 7),
    _AtmxVccCircuitType_Type()
)
atmxVccCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccCircuitType.setStatus("mandatory")
_AtmxVccOperStatus_Type = AtmConnectionOperStatCodes
_AtmxVccOperStatus_Object = MibTableColumn
atmxVccOperStatus = _AtmxVccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 8),
    _AtmxVccOperStatus_Type()
)
atmxVccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccOperStatus.setStatus("mandatory")


class _AtmxVccUpTime_Type(DisplayString):
    """Custom type atmxVccUpTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxVccUpTime_Type.__name__ = "DisplayString"
_AtmxVccUpTime_Object = MibTableColumn
atmxVccUpTime = _AtmxVccUpTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 9),
    _AtmxVccUpTime_Type()
)
atmxVccUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccUpTime.setStatus("mandatory")


class _AtmxVccDownTime_Type(DisplayString):
    """Custom type atmxVccDownTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxVccDownTime_Type.__name__ = "DisplayString"
_AtmxVccDownTime_Object = MibTableColumn
atmxVccDownTime = _AtmxVccDownTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 10),
    _AtmxVccDownTime_Type()
)
atmxVccDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccDownTime.setStatus("mandatory")


class _AtmxVccTransmitMaxFrameSize_Type(Integer32):
    """Custom type atmxVccTransmitMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccTransmitMaxFrameSize_Type.__name__ = "Integer32"
_AtmxVccTransmitMaxFrameSize_Object = MibTableColumn
atmxVccTransmitMaxFrameSize = _AtmxVccTransmitMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 11),
    _AtmxVccTransmitMaxFrameSize_Type()
)
atmxVccTransmitMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccTransmitMaxFrameSize.setStatus("mandatory")


class _AtmxVccReceiveMaxFrameSize_Type(Integer32):
    """Custom type atmxVccReceiveMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 32678),
    )


_AtmxVccReceiveMaxFrameSize_Type.__name__ = "Integer32"
_AtmxVccReceiveMaxFrameSize_Object = MibTableColumn
atmxVccReceiveMaxFrameSize = _AtmxVccReceiveMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 12),
    _AtmxVccReceiveMaxFrameSize_Type()
)
atmxVccReceiveMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccReceiveMaxFrameSize.setStatus("mandatory")
_AtmxVccRequestedTransmitTrafficDescriptor_Type = AtmTrafficDescrTypes
_AtmxVccRequestedTransmitTrafficDescriptor_Object = MibTableColumn
atmxVccRequestedTransmitTrafficDescriptor = _AtmxVccRequestedTransmitTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 13),
    _AtmxVccRequestedTransmitTrafficDescriptor_Type()
)
atmxVccRequestedTransmitTrafficDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedTransmitTrafficDescriptor.setStatus("mandatory")


class _AtmxVccRequestedTransmitTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmxVccRequestedTransmitTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccRequestedTransmitTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmxVccRequestedTransmitTrafficDescriptorParam1_Object = MibTableColumn
atmxVccRequestedTransmitTrafficDescriptorParam1 = _AtmxVccRequestedTransmitTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 14),
    _AtmxVccRequestedTransmitTrafficDescriptorParam1_Type()
)
atmxVccRequestedTransmitTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedTransmitTrafficDescriptorParam1.setStatus("mandatory")


class _AtmxVccRequestedTransmitTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmxVccRequestedTransmitTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccRequestedTransmitTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmxVccRequestedTransmitTrafficDescriptorParam2_Object = MibTableColumn
atmxVccRequestedTransmitTrafficDescriptorParam2 = _AtmxVccRequestedTransmitTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 15),
    _AtmxVccRequestedTransmitTrafficDescriptorParam2_Type()
)
atmxVccRequestedTransmitTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedTransmitTrafficDescriptorParam2.setStatus("mandatory")


class _AtmxVccRequestedTransmitTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmxVccRequestedTransmitTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccRequestedTransmitTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmxVccRequestedTransmitTrafficDescriptorParam3_Object = MibTableColumn
atmxVccRequestedTransmitTrafficDescriptorParam3 = _AtmxVccRequestedTransmitTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 16),
    _AtmxVccRequestedTransmitTrafficDescriptorParam3_Type()
)
atmxVccRequestedTransmitTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedTransmitTrafficDescriptorParam3.setStatus("mandatory")


class _AtmxVccRequestedTransmitTrafficQoSClass_Type(Integer32):
    """Custom type atmxVccRequestedTransmitTrafficQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtmxVccRequestedTransmitTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxVccRequestedTransmitTrafficQoSClass_Object = MibTableColumn
atmxVccRequestedTransmitTrafficQoSClass = _AtmxVccRequestedTransmitTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 17),
    _AtmxVccRequestedTransmitTrafficQoSClass_Type()
)
atmxVccRequestedTransmitTrafficQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedTransmitTrafficQoSClass.setStatus("mandatory")


class _AtmxVccRequestedTransmitTrafficBestEffort_Type(Integer32):
    """Custom type atmxVccRequestedTransmitTrafficBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxVccRequestedTransmitTrafficBestEffort_Type.__name__ = "Integer32"
_AtmxVccRequestedTransmitTrafficBestEffort_Object = MibTableColumn
atmxVccRequestedTransmitTrafficBestEffort = _AtmxVccRequestedTransmitTrafficBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 18),
    _AtmxVccRequestedTransmitTrafficBestEffort_Type()
)
atmxVccRequestedTransmitTrafficBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedTransmitTrafficBestEffort.setStatus("mandatory")
_AtmxVccRequestedReceiveTrafficDescriptor_Type = AtmTrafficDescrTypes
_AtmxVccRequestedReceiveTrafficDescriptor_Object = MibTableColumn
atmxVccRequestedReceiveTrafficDescriptor = _AtmxVccRequestedReceiveTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 19),
    _AtmxVccRequestedReceiveTrafficDescriptor_Type()
)
atmxVccRequestedReceiveTrafficDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedReceiveTrafficDescriptor.setStatus("mandatory")


class _AtmxVccRequestedReceiveTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmxVccRequestedReceiveTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccRequestedReceiveTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmxVccRequestedReceiveTrafficDescriptorParam1_Object = MibTableColumn
atmxVccRequestedReceiveTrafficDescriptorParam1 = _AtmxVccRequestedReceiveTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 20),
    _AtmxVccRequestedReceiveTrafficDescriptorParam1_Type()
)
atmxVccRequestedReceiveTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedReceiveTrafficDescriptorParam1.setStatus("mandatory")


class _AtmxVccRequestedReceiveTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmxVccRequestedReceiveTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccRequestedReceiveTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmxVccRequestedReceiveTrafficDescriptorParam2_Object = MibTableColumn
atmxVccRequestedReceiveTrafficDescriptorParam2 = _AtmxVccRequestedReceiveTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 21),
    _AtmxVccRequestedReceiveTrafficDescriptorParam2_Type()
)
atmxVccRequestedReceiveTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedReceiveTrafficDescriptorParam2.setStatus("mandatory")


class _AtmxVccRequestedReceiveTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmxVccRequestedReceiveTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccRequestedReceiveTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmxVccRequestedReceiveTrafficDescriptorParam3_Object = MibTableColumn
atmxVccRequestedReceiveTrafficDescriptorParam3 = _AtmxVccRequestedReceiveTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 22),
    _AtmxVccRequestedReceiveTrafficDescriptorParam3_Type()
)
atmxVccRequestedReceiveTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedReceiveTrafficDescriptorParam3.setStatus("mandatory")


class _AtmxVccRequestedReceiveTrafficQoSClass_Type(Integer32):
    """Custom type atmxVccRequestedReceiveTrafficQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtmxVccRequestedReceiveTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxVccRequestedReceiveTrafficQoSClass_Object = MibTableColumn
atmxVccRequestedReceiveTrafficQoSClass = _AtmxVccRequestedReceiveTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 23),
    _AtmxVccRequestedReceiveTrafficQoSClass_Type()
)
atmxVccRequestedReceiveTrafficQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedReceiveTrafficQoSClass.setStatus("mandatory")


class _AtmxVccRequestedReceiveTrafficBestEffort_Type(Integer32):
    """Custom type atmxVccRequestedReceiveTrafficBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxVccRequestedReceiveTrafficBestEffort_Type.__name__ = "Integer32"
_AtmxVccRequestedReceiveTrafficBestEffort_Object = MibTableColumn
atmxVccRequestedReceiveTrafficBestEffort = _AtmxVccRequestedReceiveTrafficBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 24),
    _AtmxVccRequestedReceiveTrafficBestEffort_Type()
)
atmxVccRequestedReceiveTrafficBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccRequestedReceiveTrafficBestEffort.setStatus("mandatory")
_AtmxVccAcceptableTransmitTrafficDescriptor_Type = AtmTrafficDescrTypes
_AtmxVccAcceptableTransmitTrafficDescriptor_Object = MibTableColumn
atmxVccAcceptableTransmitTrafficDescriptor = _AtmxVccAcceptableTransmitTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 25),
    _AtmxVccAcceptableTransmitTrafficDescriptor_Type()
)
atmxVccAcceptableTransmitTrafficDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableTransmitTrafficDescriptor.setStatus("mandatory")


class _AtmxVccAcceptableTransmitTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmxVccAcceptableTransmitTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccAcceptableTransmitTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmxVccAcceptableTransmitTrafficDescriptorParam1_Object = MibTableColumn
atmxVccAcceptableTransmitTrafficDescriptorParam1 = _AtmxVccAcceptableTransmitTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 26),
    _AtmxVccAcceptableTransmitTrafficDescriptorParam1_Type()
)
atmxVccAcceptableTransmitTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableTransmitTrafficDescriptorParam1.setStatus("mandatory")


class _AtmxVccAcceptableTransmitTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmxVccAcceptableTransmitTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccAcceptableTransmitTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmxVccAcceptableTransmitTrafficDescriptorParam2_Object = MibTableColumn
atmxVccAcceptableTransmitTrafficDescriptorParam2 = _AtmxVccAcceptableTransmitTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 27),
    _AtmxVccAcceptableTransmitTrafficDescriptorParam2_Type()
)
atmxVccAcceptableTransmitTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableTransmitTrafficDescriptorParam2.setStatus("mandatory")


class _AtmxVccAcceptableTransmitTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmxVccAcceptableTransmitTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccAcceptableTransmitTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmxVccAcceptableTransmitTrafficDescriptorParam3_Object = MibTableColumn
atmxVccAcceptableTransmitTrafficDescriptorParam3 = _AtmxVccAcceptableTransmitTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 28),
    _AtmxVccAcceptableTransmitTrafficDescriptorParam3_Type()
)
atmxVccAcceptableTransmitTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableTransmitTrafficDescriptorParam3.setStatus("mandatory")


class _AtmxVccAcceptableTransmitTrafficQoSClass_Type(Integer32):
    """Custom type atmxVccAcceptableTransmitTrafficQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtmxVccAcceptableTransmitTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxVccAcceptableTransmitTrafficQoSClass_Object = MibTableColumn
atmxVccAcceptableTransmitTrafficQoSClass = _AtmxVccAcceptableTransmitTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 29),
    _AtmxVccAcceptableTransmitTrafficQoSClass_Type()
)
atmxVccAcceptableTransmitTrafficQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableTransmitTrafficQoSClass.setStatus("mandatory")


class _AtmxVccAcceptableTransmitTrafficBestEffort_Type(Integer32):
    """Custom type atmxVccAcceptableTransmitTrafficBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxVccAcceptableTransmitTrafficBestEffort_Type.__name__ = "Integer32"
_AtmxVccAcceptableTransmitTrafficBestEffort_Object = MibTableColumn
atmxVccAcceptableTransmitTrafficBestEffort = _AtmxVccAcceptableTransmitTrafficBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 30),
    _AtmxVccAcceptableTransmitTrafficBestEffort_Type()
)
atmxVccAcceptableTransmitTrafficBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableTransmitTrafficBestEffort.setStatus("mandatory")
_AtmxVccAcceptableReceiveTrafficDescriptor_Type = AtmTrafficDescrTypes
_AtmxVccAcceptableReceiveTrafficDescriptor_Object = MibTableColumn
atmxVccAcceptableReceiveTrafficDescriptor = _AtmxVccAcceptableReceiveTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 31),
    _AtmxVccAcceptableReceiveTrafficDescriptor_Type()
)
atmxVccAcceptableReceiveTrafficDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableReceiveTrafficDescriptor.setStatus("mandatory")


class _AtmxVccAcceptableReceiveTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmxVccAcceptableReceiveTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccAcceptableReceiveTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmxVccAcceptableReceiveTrafficDescriptorParam1_Object = MibTableColumn
atmxVccAcceptableReceiveTrafficDescriptorParam1 = _AtmxVccAcceptableReceiveTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 32),
    _AtmxVccAcceptableReceiveTrafficDescriptorParam1_Type()
)
atmxVccAcceptableReceiveTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableReceiveTrafficDescriptorParam1.setStatus("mandatory")


class _AtmxVccAcceptableReceiveTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmxVccAcceptableReceiveTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccAcceptableReceiveTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmxVccAcceptableReceiveTrafficDescriptorParam2_Object = MibTableColumn
atmxVccAcceptableReceiveTrafficDescriptorParam2 = _AtmxVccAcceptableReceiveTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 33),
    _AtmxVccAcceptableReceiveTrafficDescriptorParam2_Type()
)
atmxVccAcceptableReceiveTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableReceiveTrafficDescriptorParam2.setStatus("mandatory")


class _AtmxVccAcceptableReceiveTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmxVccAcceptableReceiveTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccAcceptableReceiveTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmxVccAcceptableReceiveTrafficDescriptorParam3_Object = MibTableColumn
atmxVccAcceptableReceiveTrafficDescriptorParam3 = _AtmxVccAcceptableReceiveTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 34),
    _AtmxVccAcceptableReceiveTrafficDescriptorParam3_Type()
)
atmxVccAcceptableReceiveTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableReceiveTrafficDescriptorParam3.setStatus("mandatory")


class _AtmxVccAcceptableReceiveTrafficQoSClass_Type(Integer32):
    """Custom type atmxVccAcceptableReceiveTrafficQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtmxVccAcceptableReceiveTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxVccAcceptableReceiveTrafficQoSClass_Object = MibTableColumn
atmxVccAcceptableReceiveTrafficQoSClass = _AtmxVccAcceptableReceiveTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 35),
    _AtmxVccAcceptableReceiveTrafficQoSClass_Type()
)
atmxVccAcceptableReceiveTrafficQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableReceiveTrafficQoSClass.setStatus("mandatory")


class _AtmxVccAcceptableReceiveTrafficBestEffort_Type(Integer32):
    """Custom type atmxVccAcceptableReceiveTrafficBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxVccAcceptableReceiveTrafficBestEffort_Type.__name__ = "Integer32"
_AtmxVccAcceptableReceiveTrafficBestEffort_Object = MibTableColumn
atmxVccAcceptableReceiveTrafficBestEffort = _AtmxVccAcceptableReceiveTrafficBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 36),
    _AtmxVccAcceptableReceiveTrafficBestEffort_Type()
)
atmxVccAcceptableReceiveTrafficBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAcceptableReceiveTrafficBestEffort.setStatus("mandatory")
_AtmxVccActualTransmitTrafficDescriptor_Type = AtmTrafficDescrTypes
_AtmxVccActualTransmitTrafficDescriptor_Object = MibTableColumn
atmxVccActualTransmitTrafficDescriptor = _AtmxVccActualTransmitTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 37),
    _AtmxVccActualTransmitTrafficDescriptor_Type()
)
atmxVccActualTransmitTrafficDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualTransmitTrafficDescriptor.setStatus("mandatory")


class _AtmxVccActualTransmitTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmxVccActualTransmitTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccActualTransmitTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmxVccActualTransmitTrafficDescriptorParam1_Object = MibTableColumn
atmxVccActualTransmitTrafficDescriptorParam1 = _AtmxVccActualTransmitTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 38),
    _AtmxVccActualTransmitTrafficDescriptorParam1_Type()
)
atmxVccActualTransmitTrafficDescriptorParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualTransmitTrafficDescriptorParam1.setStatus("mandatory")


class _AtmxVccActualTransmitTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmxVccActualTransmitTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccActualTransmitTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmxVccActualTransmitTrafficDescriptorParam2_Object = MibTableColumn
atmxVccActualTransmitTrafficDescriptorParam2 = _AtmxVccActualTransmitTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 39),
    _AtmxVccActualTransmitTrafficDescriptorParam2_Type()
)
atmxVccActualTransmitTrafficDescriptorParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualTransmitTrafficDescriptorParam2.setStatus("mandatory")


class _AtmxVccActualTransmitTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmxVccActualTransmitTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccActualTransmitTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmxVccActualTransmitTrafficDescriptorParam3_Object = MibTableColumn
atmxVccActualTransmitTrafficDescriptorParam3 = _AtmxVccActualTransmitTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 40),
    _AtmxVccActualTransmitTrafficDescriptorParam3_Type()
)
atmxVccActualTransmitTrafficDescriptorParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualTransmitTrafficDescriptorParam3.setStatus("mandatory")


class _AtmxVccActualTransmitTrafficQoSClass_Type(Integer32):
    """Custom type atmxVccActualTransmitTrafficQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtmxVccActualTransmitTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxVccActualTransmitTrafficQoSClass_Object = MibTableColumn
atmxVccActualTransmitTrafficQoSClass = _AtmxVccActualTransmitTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 41),
    _AtmxVccActualTransmitTrafficQoSClass_Type()
)
atmxVccActualTransmitTrafficQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualTransmitTrafficQoSClass.setStatus("mandatory")


class _AtmxVccActualTransmitTrafficBestEffort_Type(Integer32):
    """Custom type atmxVccActualTransmitTrafficBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxVccActualTransmitTrafficBestEffort_Type.__name__ = "Integer32"
_AtmxVccActualTransmitTrafficBestEffort_Object = MibTableColumn
atmxVccActualTransmitTrafficBestEffort = _AtmxVccActualTransmitTrafficBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 42),
    _AtmxVccActualTransmitTrafficBestEffort_Type()
)
atmxVccActualTransmitTrafficBestEffort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualTransmitTrafficBestEffort.setStatus("mandatory")
_AtmxVccActualReceiveTrafficDescriptor_Type = AtmTrafficDescrTypes
_AtmxVccActualReceiveTrafficDescriptor_Object = MibTableColumn
atmxVccActualReceiveTrafficDescriptor = _AtmxVccActualReceiveTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 43),
    _AtmxVccActualReceiveTrafficDescriptor_Type()
)
atmxVccActualReceiveTrafficDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualReceiveTrafficDescriptor.setStatus("mandatory")


class _AtmxVccActualReceiveTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmxVccActualReceiveTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccActualReceiveTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmxVccActualReceiveTrafficDescriptorParam1_Object = MibTableColumn
atmxVccActualReceiveTrafficDescriptorParam1 = _AtmxVccActualReceiveTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 44),
    _AtmxVccActualReceiveTrafficDescriptorParam1_Type()
)
atmxVccActualReceiveTrafficDescriptorParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualReceiveTrafficDescriptorParam1.setStatus("mandatory")


class _AtmxVccActualReceiveTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmxVccActualReceiveTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccActualReceiveTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmxVccActualReceiveTrafficDescriptorParam2_Object = MibTableColumn
atmxVccActualReceiveTrafficDescriptorParam2 = _AtmxVccActualReceiveTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 45),
    _AtmxVccActualReceiveTrafficDescriptorParam2_Type()
)
atmxVccActualReceiveTrafficDescriptorParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualReceiveTrafficDescriptorParam2.setStatus("mandatory")


class _AtmxVccActualReceiveTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmxVccActualReceiveTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxVccActualReceiveTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmxVccActualReceiveTrafficDescriptorParam3_Object = MibTableColumn
atmxVccActualReceiveTrafficDescriptorParam3 = _AtmxVccActualReceiveTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 46),
    _AtmxVccActualReceiveTrafficDescriptorParam3_Type()
)
atmxVccActualReceiveTrafficDescriptorParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualReceiveTrafficDescriptorParam3.setStatus("mandatory")


class _AtmxVccActualReceiveTrafficQoSClass_Type(Integer32):
    """Custom type atmxVccActualReceiveTrafficQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtmxVccActualReceiveTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxVccActualReceiveTrafficQoSClass_Object = MibTableColumn
atmxVccActualReceiveTrafficQoSClass = _AtmxVccActualReceiveTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 47),
    _AtmxVccActualReceiveTrafficQoSClass_Type()
)
atmxVccActualReceiveTrafficQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualReceiveTrafficQoSClass.setStatus("mandatory")


class _AtmxVccActualReceiveTrafficBestEffort_Type(Integer32):
    """Custom type atmxVccActualReceiveTrafficBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxVccActualReceiveTrafficBestEffort_Type.__name__ = "Integer32"
_AtmxVccActualReceiveTrafficBestEffort_Object = MibTableColumn
atmxVccActualReceiveTrafficBestEffort = _AtmxVccActualReceiveTrafficBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 48),
    _AtmxVccActualReceiveTrafficBestEffort_Type()
)
atmxVccActualReceiveTrafficBestEffort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccActualReceiveTrafficBestEffort.setStatus("mandatory")
_AtmxVccAdmStatus_Type = AtmAdminStatCodes
_AtmxVccAdmStatus_Object = MibTableColumn
atmxVccAdmStatus = _AtmxVccAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 49),
    _AtmxVccAdmStatus_Type()
)
atmxVccAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxVccAdmStatus.setStatus("mandatory")
_AtmxVccServiceUsed_Type = Integer32
_AtmxVccServiceUsed_Object = MibTableColumn
atmxVccServiceUsed = _AtmxVccServiceUsed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 50),
    _AtmxVccServiceUsed_Type()
)
atmxVccServiceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccServiceUsed.setStatus("mandatory")
_AtmxVccConnectionUsed_Type = Integer32
_AtmxVccConnectionUsed_Object = MibTableColumn
atmxVccConnectionUsed = _AtmxVccConnectionUsed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 5, 1, 1, 51),
    _AtmxVccConnectionUsed_Type()
)
atmxVccConnectionUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccConnectionUsed.setStatus("mandatory")
_AtmxAddressGroup_ObjectIdentity = ObjectIdentity
atmxAddressGroup = _AtmxAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6)
)
_AtmxAddressTable_Object = MibTable
atmxAddressTable = _AtmxAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1)
)
if mibBuilder.loadTexts:
    atmxAddressTable.setStatus("mandatory")
_AtmxAddressEntry_Object = MibTableRow
atmxAddressEntry = _AtmxAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1)
)
atmxAddressEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxAddressIndex"),
)
if mibBuilder.loadTexts:
    atmxAddressEntry.setStatus("mandatory")


class _AtmxAddressIndex_Type(Integer32):
    """Custom type atmxAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AtmxAddressIndex_Type.__name__ = "Integer32"
_AtmxAddressIndex_Object = MibTableColumn
atmxAddressIndex = _AtmxAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 1),
    _AtmxAddressIndex_Type()
)
atmxAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxAddressIndex.setStatus("mandatory")


class _AtmxAddressAtmAddress_Type(DisplayString):
    """Custom type atmxAddressAtmAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AtmxAddressAtmAddress_Type.__name__ = "DisplayString"
_AtmxAddressAtmAddress_Object = MibTableColumn
atmxAddressAtmAddress = _AtmxAddressAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 2),
    _AtmxAddressAtmAddress_Type()
)
atmxAddressAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAtmAddress.setStatus("mandatory")


class _AtmxAddressType_Type(Integer32):
    """Custom type atmxAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("arpServer", 1),
          ("nonArpServer", 2))
    )


_AtmxAddressType_Type.__name__ = "Integer32"
_AtmxAddressType_Object = MibTableColumn
atmxAddressType = _AtmxAddressType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 3),
    _AtmxAddressType_Type()
)
atmxAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressType.setStatus("mandatory")


class _AtmxAddressVpi_Type(Integer32):
    """Custom type atmxAddressVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AtmxAddressVpi_Type.__name__ = "Integer32"
_AtmxAddressVpi_Object = MibTableColumn
atmxAddressVpi = _AtmxAddressVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 4),
    _AtmxAddressVpi_Type()
)
atmxAddressVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxAddressVpi.setStatus("mandatory")


class _AtmxAddressVci_Type(Integer32):
    """Custom type atmxAddressVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AtmxAddressVci_Type.__name__ = "Integer32"
_AtmxAddressVci_Object = MibTableColumn
atmxAddressVci = _AtmxAddressVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 5),
    _AtmxAddressVci_Type()
)
atmxAddressVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressVci.setStatus("mandatory")


class _AtmxAddressDescription_Type(DisplayString):
    """Custom type atmxAddressDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxAddressDescription_Type.__name__ = "DisplayString"
_AtmxAddressDescription_Object = MibTableColumn
atmxAddressDescription = _AtmxAddressDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 6),
    _AtmxAddressDescription_Type()
)
atmxAddressDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressDescription.setStatus("mandatory")


class _AtmxAddressTransmitMaxSDU_Type(Integer32):
    """Custom type atmxAddressTransmitMaxSDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 32678),
    )


_AtmxAddressTransmitMaxSDU_Type.__name__ = "Integer32"
_AtmxAddressTransmitMaxSDU_Object = MibTableColumn
atmxAddressTransmitMaxSDU = _AtmxAddressTransmitMaxSDU_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 7),
    _AtmxAddressTransmitMaxSDU_Type()
)
atmxAddressTransmitMaxSDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressTransmitMaxSDU.setStatus("mandatory")


class _AtmxAddressReceiveMaxSDU_Type(Integer32):
    """Custom type atmxAddressReceiveMaxSDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 32678),
    )


_AtmxAddressReceiveMaxSDU_Type.__name__ = "Integer32"
_AtmxAddressReceiveMaxSDU_Object = MibTableColumn
atmxAddressReceiveMaxSDU = _AtmxAddressReceiveMaxSDU_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 8),
    _AtmxAddressReceiveMaxSDU_Type()
)
atmxAddressReceiveMaxSDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressReceiveMaxSDU.setStatus("mandatory")
_AtmxAddressRequestedTransmitTrafficDescriptor_Type = AtmTrafficDescrTypes
_AtmxAddressRequestedTransmitTrafficDescriptor_Object = MibTableColumn
atmxAddressRequestedTransmitTrafficDescriptor = _AtmxAddressRequestedTransmitTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 9),
    _AtmxAddressRequestedTransmitTrafficDescriptor_Type()
)
atmxAddressRequestedTransmitTrafficDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedTransmitTrafficDescriptor.setStatus("mandatory")


class _AtmxAddressRequestedTransmitTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmxAddressRequestedTransmitTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressRequestedTransmitTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmxAddressRequestedTransmitTrafficDescriptorParam1_Object = MibTableColumn
atmxAddressRequestedTransmitTrafficDescriptorParam1 = _AtmxAddressRequestedTransmitTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 10),
    _AtmxAddressRequestedTransmitTrafficDescriptorParam1_Type()
)
atmxAddressRequestedTransmitTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedTransmitTrafficDescriptorParam1.setStatus("mandatory")


class _AtmxAddressRequestedTransmitTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmxAddressRequestedTransmitTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressRequestedTransmitTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmxAddressRequestedTransmitTrafficDescriptorParam2_Object = MibTableColumn
atmxAddressRequestedTransmitTrafficDescriptorParam2 = _AtmxAddressRequestedTransmitTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 11),
    _AtmxAddressRequestedTransmitTrafficDescriptorParam2_Type()
)
atmxAddressRequestedTransmitTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedTransmitTrafficDescriptorParam2.setStatus("mandatory")


class _AtmxAddressRequestedTransmitTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmxAddressRequestedTransmitTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressRequestedTransmitTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmxAddressRequestedTransmitTrafficDescriptorParam3_Object = MibTableColumn
atmxAddressRequestedTransmitTrafficDescriptorParam3 = _AtmxAddressRequestedTransmitTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 12),
    _AtmxAddressRequestedTransmitTrafficDescriptorParam3_Type()
)
atmxAddressRequestedTransmitTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedTransmitTrafficDescriptorParam3.setStatus("mandatory")


class _AtmxAddressRequestedTransmitTrafficQoSClass_Type(Integer32):
    """Custom type atmxAddressRequestedTransmitTrafficQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtmxAddressRequestedTransmitTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxAddressRequestedTransmitTrafficQoSClass_Object = MibTableColumn
atmxAddressRequestedTransmitTrafficQoSClass = _AtmxAddressRequestedTransmitTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 13),
    _AtmxAddressRequestedTransmitTrafficQoSClass_Type()
)
atmxAddressRequestedTransmitTrafficQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedTransmitTrafficQoSClass.setStatus("mandatory")


class _AtmxAddressRequestedTransmitTrafficBestEffort_Type(Integer32):
    """Custom type atmxAddressRequestedTransmitTrafficBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxAddressRequestedTransmitTrafficBestEffort_Type.__name__ = "Integer32"
_AtmxAddressRequestedTransmitTrafficBestEffort_Object = MibTableColumn
atmxAddressRequestedTransmitTrafficBestEffort = _AtmxAddressRequestedTransmitTrafficBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 14),
    _AtmxAddressRequestedTransmitTrafficBestEffort_Type()
)
atmxAddressRequestedTransmitTrafficBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedTransmitTrafficBestEffort.setStatus("mandatory")
_AtmxAddressRequestedReceiveTrafficDescriptor_Type = AtmTrafficDescrTypes
_AtmxAddressRequestedReceiveTrafficDescriptor_Object = MibTableColumn
atmxAddressRequestedReceiveTrafficDescriptor = _AtmxAddressRequestedReceiveTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 15),
    _AtmxAddressRequestedReceiveTrafficDescriptor_Type()
)
atmxAddressRequestedReceiveTrafficDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedReceiveTrafficDescriptor.setStatus("mandatory")


class _AtmxAddressRequestedReceiveTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmxAddressRequestedReceiveTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressRequestedReceiveTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmxAddressRequestedReceiveTrafficDescriptorParam1_Object = MibTableColumn
atmxAddressRequestedReceiveTrafficDescriptorParam1 = _AtmxAddressRequestedReceiveTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 16),
    _AtmxAddressRequestedReceiveTrafficDescriptorParam1_Type()
)
atmxAddressRequestedReceiveTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedReceiveTrafficDescriptorParam1.setStatus("mandatory")


class _AtmxAddressRequestedReceiveTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmxAddressRequestedReceiveTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressRequestedReceiveTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmxAddressRequestedReceiveTrafficDescriptorParam2_Object = MibTableColumn
atmxAddressRequestedReceiveTrafficDescriptorParam2 = _AtmxAddressRequestedReceiveTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 17),
    _AtmxAddressRequestedReceiveTrafficDescriptorParam2_Type()
)
atmxAddressRequestedReceiveTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedReceiveTrafficDescriptorParam2.setStatus("mandatory")


class _AtmxAddressRequestedReceiveTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmxAddressRequestedReceiveTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressRequestedReceiveTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmxAddressRequestedReceiveTrafficDescriptorParam3_Object = MibTableColumn
atmxAddressRequestedReceiveTrafficDescriptorParam3 = _AtmxAddressRequestedReceiveTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 18),
    _AtmxAddressRequestedReceiveTrafficDescriptorParam3_Type()
)
atmxAddressRequestedReceiveTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedReceiveTrafficDescriptorParam3.setStatus("mandatory")


class _AtmxAddressRequestedReceiveTrafficQoSClass_Type(Integer32):
    """Custom type atmxAddressRequestedReceiveTrafficQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtmxAddressRequestedReceiveTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxAddressRequestedReceiveTrafficQoSClass_Object = MibTableColumn
atmxAddressRequestedReceiveTrafficQoSClass = _AtmxAddressRequestedReceiveTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 19),
    _AtmxAddressRequestedReceiveTrafficQoSClass_Type()
)
atmxAddressRequestedReceiveTrafficQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedReceiveTrafficQoSClass.setStatus("mandatory")


class _AtmxAddressRequestedReceiveTrafficBestEffort_Type(Integer32):
    """Custom type atmxAddressRequestedReceiveTrafficBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxAddressRequestedReceiveTrafficBestEffort_Type.__name__ = "Integer32"
_AtmxAddressRequestedReceiveTrafficBestEffort_Object = MibTableColumn
atmxAddressRequestedReceiveTrafficBestEffort = _AtmxAddressRequestedReceiveTrafficBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 20),
    _AtmxAddressRequestedReceiveTrafficBestEffort_Type()
)
atmxAddressRequestedReceiveTrafficBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressRequestedReceiveTrafficBestEffort.setStatus("mandatory")
_AtmxAddressAcceptableTransmitTrafficDescriptor_Type = AtmTrafficDescrTypes
_AtmxAddressAcceptableTransmitTrafficDescriptor_Object = MibTableColumn
atmxAddressAcceptableTransmitTrafficDescriptor = _AtmxAddressAcceptableTransmitTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 21),
    _AtmxAddressAcceptableTransmitTrafficDescriptor_Type()
)
atmxAddressAcceptableTransmitTrafficDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableTransmitTrafficDescriptor.setStatus("mandatory")


class _AtmxAddressAcceptableTransmitTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmxAddressAcceptableTransmitTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressAcceptableTransmitTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmxAddressAcceptableTransmitTrafficDescriptorParam1_Object = MibTableColumn
atmxAddressAcceptableTransmitTrafficDescriptorParam1 = _AtmxAddressAcceptableTransmitTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 22),
    _AtmxAddressAcceptableTransmitTrafficDescriptorParam1_Type()
)
atmxAddressAcceptableTransmitTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableTransmitTrafficDescriptorParam1.setStatus("mandatory")


class _AtmxAddressAcceptableTransmitTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmxAddressAcceptableTransmitTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressAcceptableTransmitTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmxAddressAcceptableTransmitTrafficDescriptorParam2_Object = MibTableColumn
atmxAddressAcceptableTransmitTrafficDescriptorParam2 = _AtmxAddressAcceptableTransmitTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 23),
    _AtmxAddressAcceptableTransmitTrafficDescriptorParam2_Type()
)
atmxAddressAcceptableTransmitTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableTransmitTrafficDescriptorParam2.setStatus("mandatory")


class _AtmxAddressAcceptableTransmitTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmxAddressAcceptableTransmitTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressAcceptableTransmitTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmxAddressAcceptableTransmitTrafficDescriptorParam3_Object = MibTableColumn
atmxAddressAcceptableTransmitTrafficDescriptorParam3 = _AtmxAddressAcceptableTransmitTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 24),
    _AtmxAddressAcceptableTransmitTrafficDescriptorParam3_Type()
)
atmxAddressAcceptableTransmitTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableTransmitTrafficDescriptorParam3.setStatus("mandatory")


class _AtmxAddressAcceptableTransmitTrafficQoSClass_Type(Integer32):
    """Custom type atmxAddressAcceptableTransmitTrafficQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtmxAddressAcceptableTransmitTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxAddressAcceptableTransmitTrafficQoSClass_Object = MibTableColumn
atmxAddressAcceptableTransmitTrafficQoSClass = _AtmxAddressAcceptableTransmitTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 25),
    _AtmxAddressAcceptableTransmitTrafficQoSClass_Type()
)
atmxAddressAcceptableTransmitTrafficQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableTransmitTrafficQoSClass.setStatus("mandatory")


class _AtmxAddressAcceptableTransmitTrafficBestEffort_Type(Integer32):
    """Custom type atmxAddressAcceptableTransmitTrafficBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxAddressAcceptableTransmitTrafficBestEffort_Type.__name__ = "Integer32"
_AtmxAddressAcceptableTransmitTrafficBestEffort_Object = MibTableColumn
atmxAddressAcceptableTransmitTrafficBestEffort = _AtmxAddressAcceptableTransmitTrafficBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 26),
    _AtmxAddressAcceptableTransmitTrafficBestEffort_Type()
)
atmxAddressAcceptableTransmitTrafficBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableTransmitTrafficBestEffort.setStatus("mandatory")
_AtmxAddressAcceptableReceiveTrafficDescriptor_Type = AtmTrafficDescrTypes
_AtmxAddressAcceptableReceiveTrafficDescriptor_Object = MibTableColumn
atmxAddressAcceptableReceiveTrafficDescriptor = _AtmxAddressAcceptableReceiveTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 27),
    _AtmxAddressAcceptableReceiveTrafficDescriptor_Type()
)
atmxAddressAcceptableReceiveTrafficDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableReceiveTrafficDescriptor.setStatus("mandatory")


class _AtmxAddressAcceptableReceiveTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmxAddressAcceptableReceiveTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressAcceptableReceiveTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmxAddressAcceptableReceiveTrafficDescriptorParam1_Object = MibTableColumn
atmxAddressAcceptableReceiveTrafficDescriptorParam1 = _AtmxAddressAcceptableReceiveTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 28),
    _AtmxAddressAcceptableReceiveTrafficDescriptorParam1_Type()
)
atmxAddressAcceptableReceiveTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableReceiveTrafficDescriptorParam1.setStatus("mandatory")


class _AtmxAddressAcceptableReceiveTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmxAddressAcceptableReceiveTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressAcceptableReceiveTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmxAddressAcceptableReceiveTrafficDescriptorParam2_Object = MibTableColumn
atmxAddressAcceptableReceiveTrafficDescriptorParam2 = _AtmxAddressAcceptableReceiveTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 29),
    _AtmxAddressAcceptableReceiveTrafficDescriptorParam2_Type()
)
atmxAddressAcceptableReceiveTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableReceiveTrafficDescriptorParam2.setStatus("mandatory")


class _AtmxAddressAcceptableReceiveTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmxAddressAcceptableReceiveTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmxAddressAcceptableReceiveTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmxAddressAcceptableReceiveTrafficDescriptorParam3_Object = MibTableColumn
atmxAddressAcceptableReceiveTrafficDescriptorParam3 = _AtmxAddressAcceptableReceiveTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 30),
    _AtmxAddressAcceptableReceiveTrafficDescriptorParam3_Type()
)
atmxAddressAcceptableReceiveTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableReceiveTrafficDescriptorParam3.setStatus("mandatory")


class _AtmxAddressAcceptableReceiveTrafficQoSClass_Type(Integer32):
    """Custom type atmxAddressAcceptableReceiveTrafficQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtmxAddressAcceptableReceiveTrafficQoSClass_Type.__name__ = "Integer32"
_AtmxAddressAcceptableReceiveTrafficQoSClass_Object = MibTableColumn
atmxAddressAcceptableReceiveTrafficQoSClass = _AtmxAddressAcceptableReceiveTrafficQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 31),
    _AtmxAddressAcceptableReceiveTrafficQoSClass_Type()
)
atmxAddressAcceptableReceiveTrafficQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableReceiveTrafficQoSClass.setStatus("mandatory")


class _AtmxAddressAcceptableReceiveTrafficBestEffort_Type(Integer32):
    """Custom type atmxAddressAcceptableReceiveTrafficBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxAddressAcceptableReceiveTrafficBestEffort_Type.__name__ = "Integer32"
_AtmxAddressAcceptableReceiveTrafficBestEffort_Object = MibTableColumn
atmxAddressAcceptableReceiveTrafficBestEffort = _AtmxAddressAcceptableReceiveTrafficBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 32),
    _AtmxAddressAcceptableReceiveTrafficBestEffort_Type()
)
atmxAddressAcceptableReceiveTrafficBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAcceptableReceiveTrafficBestEffort.setStatus("mandatory")
_AtmxAddressAdmStatus_Type = AtmAdminStatCodes
_AtmxAddressAdmStatus_Object = MibTableColumn
atmxAddressAdmStatus = _AtmxAddressAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 33),
    _AtmxAddressAdmStatus_Type()
)
atmxAddressAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxAddressAdmStatus.setStatus("mandatory")
_AtmxAddressServiceUsed_Type = Integer32
_AtmxAddressServiceUsed_Object = MibTableColumn
atmxAddressServiceUsed = _AtmxAddressServiceUsed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 34),
    _AtmxAddressServiceUsed_Type()
)
atmxAddressServiceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxAddressServiceUsed.setStatus("mandatory")
_AtmxAddressAddrUsed_Type = Integer32
_AtmxAddressAddrUsed_Object = MibTableColumn
atmxAddressAddrUsed = _AtmxAddressAddrUsed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 6, 1, 1, 35),
    _AtmxAddressAddrUsed_Type()
)
atmxAddressAddrUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxAddressAddrUsed.setStatus("mandatory")
_AtmxArpGroup_ObjectIdentity = ObjectIdentity
atmxArpGroup = _AtmxArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 7)
)
_AtmxArpTable_Object = MibTable
atmxArpTable = _AtmxArpTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 7, 1)
)
if mibBuilder.loadTexts:
    atmxArpTable.setStatus("mandatory")
_AtmxArpEntry_Object = MibTableRow
atmxArpEntry = _AtmxArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 7, 1, 1)
)
atmxArpEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxArpIndex"),
)
if mibBuilder.loadTexts:
    atmxArpEntry.setStatus("mandatory")


class _AtmxArpIndex_Type(Integer32):
    """Custom type atmxArpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AtmxArpIndex_Type.__name__ = "Integer32"
_AtmxArpIndex_Object = MibTableColumn
atmxArpIndex = _AtmxArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 7, 1, 1, 1),
    _AtmxArpIndex_Type()
)
atmxArpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxArpIndex.setStatus("mandatory")
_AtmxArpIPAddress_Type = IpAddress
_AtmxArpIPAddress_Object = MibTableColumn
atmxArpIPAddress = _AtmxArpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 7, 1, 1, 2),
    _AtmxArpIPAddress_Type()
)
atmxArpIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxArpIPAddress.setStatus("mandatory")


class _AtmxArpAtmAddress_Type(DisplayString):
    """Custom type atmxArpAtmAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AtmxArpAtmAddress_Type.__name__ = "DisplayString"
_AtmxArpAtmAddress_Object = MibTableColumn
atmxArpAtmAddress = _AtmxArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 7, 1, 1, 3),
    _AtmxArpAtmAddress_Type()
)
atmxArpAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxArpAtmAddress.setStatus("mandatory")


class _AtmxArpVci_Type(Integer32):
    """Custom type atmxArpVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AtmxArpVci_Type.__name__ = "Integer32"
_AtmxArpVci_Object = MibTableColumn
atmxArpVci = _AtmxArpVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 7, 1, 1, 4),
    _AtmxArpVci_Type()
)
atmxArpVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxArpVci.setStatus("mandatory")
_AtmxArpTimeToLive_Type = Integer32
_AtmxArpTimeToLive_Object = MibTableColumn
atmxArpTimeToLive = _AtmxArpTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 7, 1, 1, 5),
    _AtmxArpTimeToLive_Type()
)
atmxArpTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxArpTimeToLive.setStatus("mandatory")


class _AtmxArpType_Type(Integer32):
    """Custom type atmxArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_AtmxArpType_Type.__name__ = "Integer32"
_AtmxArpType_Object = MibTableColumn
atmxArpType = _AtmxArpType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 7, 1, 1, 6),
    _AtmxArpType_Type()
)
atmxArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxArpType.setStatus("mandatory")
_AtmxLaneGroup_ObjectIdentity = ObjectIdentity
atmxLaneGroup = _AtmxLaneGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8)
)
_AtmLecConfigTable_Object = MibTable
atmLecConfigTable = _AtmLecConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1)
)
if mibBuilder.loadTexts:
    atmLecConfigTable.setStatus("mandatory")
_AtmLecConfigEntry_Object = MibTableRow
atmLecConfigEntry = _AtmLecConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1)
)
atmLecConfigEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxLecConfigIndex"),
)
if mibBuilder.loadTexts:
    atmLecConfigEntry.setStatus("mandatory")
_AtmxLecConfigIndex_Type = Integer32
_AtmxLecConfigIndex_Object = MibTableColumn
atmxLecConfigIndex = _AtmxLecConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 1),
    _AtmxLecConfigIndex_Type()
)
atmxLecConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecConfigIndex.setStatus("mandatory")
_AtmLecConfigLecsAtmAddress_Type = XylanAtmLaneAddress
_AtmLecConfigLecsAtmAddress_Object = MibTableColumn
atmLecConfigLecsAtmAddress = _AtmLecConfigLecsAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 2),
    _AtmLecConfigLecsAtmAddress_Type()
)
atmLecConfigLecsAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecConfigLecsAtmAddress.setStatus("mandatory")
_AtmLecConfigUseDefaultLecsAddr_Type = Integer32
_AtmLecConfigUseDefaultLecsAddr_Object = MibTableColumn
atmLecConfigUseDefaultLecsAddr = _AtmLecConfigUseDefaultLecsAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 3),
    _AtmLecConfigUseDefaultLecsAddr_Type()
)
atmLecConfigUseDefaultLecsAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecConfigUseDefaultLecsAddr.setStatus("mandatory")
_AtmLecRowStatus_Type = Integer32
_AtmLecRowStatus_Object = MibTableColumn
atmLecRowStatus = _AtmLecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 4),
    _AtmLecRowStatus_Type()
)
atmLecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecRowStatus.setStatus("mandatory")
_AtmLecRowInUse_Type = Integer32
_AtmLecRowInUse_Object = MibTableColumn
atmLecRowInUse = _AtmLecRowInUse_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 5),
    _AtmLecRowInUse_Type()
)
atmLecRowInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecRowInUse.setStatus("mandatory")


class _AtmLecConfigMode_Type(Integer32):
    """Custom type atmLecConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_AtmLecConfigMode_Type.__name__ = "Integer32"
_AtmLecConfigMode_Object = MibTableColumn
atmLecConfigMode = _AtmLecConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 6),
    _AtmLecConfigMode_Type()
)
atmLecConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecConfigMode.setStatus("mandatory")


class _AtmLecConfigLanType_Type(LecDataFrameFormat):
    """Custom type atmLecConfigLanType based on LecDataFrameFormat"""


_AtmLecConfigLanType_Object = MibTableColumn
atmLecConfigLanType = _AtmLecConfigLanType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 7),
    _AtmLecConfigLanType_Type()
)
atmLecConfigLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecConfigLanType.setStatus("mandatory")


class _AtmLecConfigMaxDataFrameSize_Type(LecDataFrameSize):
    """Custom type atmLecConfigMaxDataFrameSize based on LecDataFrameSize"""


_AtmLecConfigMaxDataFrameSize_Object = MibTableColumn
atmLecConfigMaxDataFrameSize = _AtmLecConfigMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 8),
    _AtmLecConfigMaxDataFrameSize_Type()
)
atmLecConfigMaxDataFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecConfigMaxDataFrameSize.setStatus("mandatory")


class _AtmLecConfigLanName_Type(DisplayString):
    """Custom type atmLecConfigLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtmLecConfigLanName_Type.__name__ = "DisplayString"
_AtmLecConfigLanName_Object = MibTableColumn
atmLecConfigLanName = _AtmLecConfigLanName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 9),
    _AtmLecConfigLanName_Type()
)
atmLecConfigLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecConfigLanName.setStatus("mandatory")
_AtmLecConfigLesAtmAddress_Type = XylanAtmLaneAddress
_AtmLecConfigLesAtmAddress_Object = MibTableColumn
atmLecConfigLesAtmAddress = _AtmLecConfigLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 10),
    _AtmLecConfigLesAtmAddress_Type()
)
atmLecConfigLesAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecConfigLesAtmAddress.setStatus("mandatory")


class _AtmLecControlTimeout_Type(Integer32):
    """Custom type atmLecControlTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_AtmLecControlTimeout_Type.__name__ = "Integer32"
_AtmLecControlTimeout_Object = MibTableColumn
atmLecControlTimeout = _AtmLecControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 11),
    _AtmLecControlTimeout_Type()
)
atmLecControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecControlTimeout.setStatus("mandatory")


class _AtmLecMaxUnknownFrameCount_Type(Integer32):
    """Custom type atmLecMaxUnknownFrameCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AtmLecMaxUnknownFrameCount_Type.__name__ = "Integer32"
_AtmLecMaxUnknownFrameCount_Object = MibTableColumn
atmLecMaxUnknownFrameCount = _AtmLecMaxUnknownFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 12),
    _AtmLecMaxUnknownFrameCount_Type()
)
atmLecMaxUnknownFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecMaxUnknownFrameCount.setStatus("mandatory")


class _AtmLecMaxUnknownFrameTime_Type(Integer32):
    """Custom type atmLecMaxUnknownFrameTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AtmLecMaxUnknownFrameTime_Type.__name__ = "Integer32"
_AtmLecMaxUnknownFrameTime_Object = MibTableColumn
atmLecMaxUnknownFrameTime = _AtmLecMaxUnknownFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 13),
    _AtmLecMaxUnknownFrameTime_Type()
)
atmLecMaxUnknownFrameTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecMaxUnknownFrameTime.setStatus("mandatory")


class _AtmLecVccTimeoutPeriod_Type(Integer32):
    """Custom type atmLecVccTimeoutPeriod based on Integer32"""
    defaultValue = 1200


_AtmLecVccTimeoutPeriod_Object = MibTableColumn
atmLecVccTimeoutPeriod = _AtmLecVccTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 14),
    _AtmLecVccTimeoutPeriod_Type()
)
atmLecVccTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecVccTimeoutPeriod.setStatus("mandatory")


class _AtmLecMaxRetryCount_Type(Integer32):
    """Custom type atmLecMaxRetryCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AtmLecMaxRetryCount_Type.__name__ = "Integer32"
_AtmLecMaxRetryCount_Object = MibTableColumn
atmLecMaxRetryCount = _AtmLecMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 15),
    _AtmLecMaxRetryCount_Type()
)
atmLecMaxRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecMaxRetryCount.setStatus("mandatory")


class _AtmLecAgingTime_Type(Integer32):
    """Custom type atmLecAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_AtmLecAgingTime_Type.__name__ = "Integer32"
_AtmLecAgingTime_Object = MibTableColumn
atmLecAgingTime = _AtmLecAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 16),
    _AtmLecAgingTime_Type()
)
atmLecAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecAgingTime.setStatus("mandatory")


class _AtmLecForwardDelayTime_Type(Integer32):
    """Custom type atmLecForwardDelayTime based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_AtmLecForwardDelayTime_Type.__name__ = "Integer32"
_AtmLecForwardDelayTime_Object = MibTableColumn
atmLecForwardDelayTime = _AtmLecForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 17),
    _AtmLecForwardDelayTime_Type()
)
atmLecForwardDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecForwardDelayTime.setStatus("mandatory")


class _AtmLecExpectedArpResponseTime_Type(Integer32):
    """Custom type atmLecExpectedArpResponseTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AtmLecExpectedArpResponseTime_Type.__name__ = "Integer32"
_AtmLecExpectedArpResponseTime_Object = MibTableColumn
atmLecExpectedArpResponseTime = _AtmLecExpectedArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 18),
    _AtmLecExpectedArpResponseTime_Type()
)
atmLecExpectedArpResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecExpectedArpResponseTime.setStatus("mandatory")


class _AtmLecFlushTimeOut_Type(Integer32):
    """Custom type atmLecFlushTimeOut based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AtmLecFlushTimeOut_Type.__name__ = "Integer32"
_AtmLecFlushTimeOut_Object = MibTableColumn
atmLecFlushTimeOut = _AtmLecFlushTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 19),
    _AtmLecFlushTimeOut_Type()
)
atmLecFlushTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecFlushTimeOut.setStatus("mandatory")


class _AtmLecPathSwitchingDelay_Type(Integer32):
    """Custom type atmLecPathSwitchingDelay based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtmLecPathSwitchingDelay_Type.__name__ = "Integer32"
_AtmLecPathSwitchingDelay_Object = MibTableColumn
atmLecPathSwitchingDelay = _AtmLecPathSwitchingDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 20),
    _AtmLecPathSwitchingDelay_Type()
)
atmLecPathSwitchingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecPathSwitchingDelay.setStatus("mandatory")


class _AtmLecUseForwardDelay_Type(Integer32):
    """Custom type atmLecUseForwardDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AtmLecUseForwardDelay_Type.__name__ = "Integer32"
_AtmLecUseForwardDelay_Object = MibTableColumn
atmLecUseForwardDelay = _AtmLecUseForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 21),
    _AtmLecUseForwardDelay_Type()
)
atmLecUseForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecUseForwardDelay.setStatus("mandatory")


class _AtmLecUseTranslation_Type(Integer32):
    """Custom type atmLecUseTranslation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AtmLecUseTranslation_Type.__name__ = "Integer32"
_AtmLecUseTranslation_Object = MibTableColumn
atmLecUseTranslation = _AtmLecUseTranslation_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 23),
    _AtmLecUseTranslation_Type()
)
atmLecUseTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecUseTranslation.setStatus("mandatory")


class _AtmLecSrBridgeNum_Type(Integer32):
    """Custom type atmLecSrBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AtmLecSrBridgeNum_Type.__name__ = "Integer32"
_AtmLecSrBridgeNum_Object = MibTableColumn
atmLecSrBridgeNum = _AtmLecSrBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 24),
    _AtmLecSrBridgeNum_Type()
)
atmLecSrBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecSrBridgeNum.setStatus("mandatory")


class _AtmLecSrRingNum_Type(Integer32):
    """Custom type atmLecSrRingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmLecSrRingNum_Type.__name__ = "Integer32"
_AtmLecSrRingNum_Object = MibTableColumn
atmLecSrRingNum = _AtmLecSrRingNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 1, 1, 25),
    _AtmLecSrRingNum_Type()
)
atmLecSrRingNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmLecSrRingNum.setStatus("mandatory")
_AtmLecStatusTable_Object = MibTable
atmLecStatusTable = _AtmLecStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2)
)
if mibBuilder.loadTexts:
    atmLecStatusTable.setStatus("mandatory")
_AtmLecStatusEntry_Object = MibTableRow
atmLecStatusEntry = _AtmLecStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1)
)
atmLecStatusEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxLecStatusSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxLecStatusPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxLecStatusServiceNum"),
)
if mibBuilder.loadTexts:
    atmLecStatusEntry.setStatus("mandatory")
_AtmxLecStatusSlotIndex_Type = Integer32
_AtmxLecStatusSlotIndex_Object = MibTableColumn
atmxLecStatusSlotIndex = _AtmxLecStatusSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 1),
    _AtmxLecStatusSlotIndex_Type()
)
atmxLecStatusSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatusSlotIndex.setStatus("mandatory")
_AtmxLecStatusPortIndex_Type = Integer32
_AtmxLecStatusPortIndex_Object = MibTableColumn
atmxLecStatusPortIndex = _AtmxLecStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 2),
    _AtmxLecStatusPortIndex_Type()
)
atmxLecStatusPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatusPortIndex.setStatus("mandatory")
_AtmxLecStatusServiceNum_Type = Integer32
_AtmxLecStatusServiceNum_Object = MibTableColumn
atmxLecStatusServiceNum = _AtmxLecStatusServiceNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 3),
    _AtmxLecStatusServiceNum_Type()
)
atmxLecStatusServiceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatusServiceNum.setStatus("mandatory")
_AtmLecPrimaryAtmAddress_Type = XylanAtmLaneAddress
_AtmLecPrimaryAtmAddress_Object = MibTableColumn
atmLecPrimaryAtmAddress = _AtmLecPrimaryAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 4),
    _AtmLecPrimaryAtmAddress_Type()
)
atmLecPrimaryAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecPrimaryAtmAddress.setStatus("mandatory")


class _AtmLecID_Type(Integer32):
    """Custom type atmLecID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_AtmLecID_Type.__name__ = "Integer32"
_AtmLecID_Object = MibTableColumn
atmLecID = _AtmLecID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 5),
    _AtmLecID_Type()
)
atmLecID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecID.setStatus("mandatory")
_AtmLecInterfaceState_Type = LecState
_AtmLecInterfaceState_Object = MibTableColumn
atmLecInterfaceState = _AtmLecInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 6),
    _AtmLecInterfaceState_Type()
)
atmLecInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecInterfaceState.setStatus("mandatory")


class _AtmLecLastFailureRespCode_Type(Integer32):
    """Custom type atmLecLastFailureRespCode based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 9),
          ("duplicateAtmAddress", 7),
          ("duplicateLanDestination", 6),
          ("insufficientInformation", 15),
          ("insufficientResources", 8),
          ("invalidAtmAddress", 12),
          ("invalidLanDestination", 11),
          ("invalidRequestParameters", 5),
          ("invalidRequesterId", 10),
          ("leConfigureError", 14),
          ("noConfiguration", 13),
          ("none", 1),
          ("timeout", 2),
          ("undefinedError", 3),
          ("versionNotSupported", 4))
    )


_AtmLecLastFailureRespCode_Type.__name__ = "Integer32"
_AtmLecLastFailureRespCode_Object = MibTableColumn
atmLecLastFailureRespCode = _AtmLecLastFailureRespCode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 7),
    _AtmLecLastFailureRespCode_Type()
)
atmLecLastFailureRespCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecLastFailureRespCode.setStatus("mandatory")
_AtmLecLastFailureState_Type = LecState
_AtmLecLastFailureState_Object = MibTableColumn
atmLecLastFailureState = _AtmLecLastFailureState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 8),
    _AtmLecLastFailureState_Type()
)
atmLecLastFailureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecLastFailureState.setStatus("mandatory")


class _AtmLecProtocol_Type(Integer32):
    """Custom type atmLecProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmLecProtocol_Type.__name__ = "Integer32"
_AtmLecProtocol_Object = MibTableColumn
atmLecProtocol = _AtmLecProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 9),
    _AtmLecProtocol_Type()
)
atmLecProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecProtocol.setStatus("mandatory")


class _AtmLecVersion_Type(Integer32):
    """Custom type atmLecVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmLecVersion_Type.__name__ = "Integer32"
_AtmLecVersion_Object = MibTableColumn
atmLecVersion = _AtmLecVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 10),
    _AtmLecVersion_Type()
)
atmLecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecVersion.setStatus("mandatory")
_AtmLecTopologyChange_Type = Integer32
_AtmLecTopologyChange_Object = MibTableColumn
atmLecTopologyChange = _AtmLecTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 11),
    _AtmLecTopologyChange_Type()
)
atmLecTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecTopologyChange.setStatus("mandatory")
_AtmLecConfigServerAtmAddress_Type = XylanAtmLaneAddress
_AtmLecConfigServerAtmAddress_Object = MibTableColumn
atmLecConfigServerAtmAddress = _AtmLecConfigServerAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 12),
    _AtmLecConfigServerAtmAddress_Type()
)
atmLecConfigServerAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecConfigServerAtmAddress.setStatus("mandatory")


class _AtmLecConfigSource_Type(Integer32):
    """Custom type atmLecConfigSource based on Integer32"""
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
        *(("didNotUseLecs", 4),
          ("gotAddressViaIlmi", 1),
          ("usedLecsPvc", 3),
          ("usedWellKnownAddress", 2))
    )


_AtmLecConfigSource_Type.__name__ = "Integer32"
_AtmLecConfigSource_Object = MibTableColumn
atmLecConfigSource = _AtmLecConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 13),
    _AtmLecConfigSource_Type()
)
atmLecConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecConfigSource.setStatus("mandatory")
_AtmLecActualLanType_Type = LecDataFrameFormat
_AtmLecActualLanType_Object = MibTableColumn
atmLecActualLanType = _AtmLecActualLanType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 14),
    _AtmLecActualLanType_Type()
)
atmLecActualLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecActualLanType.setStatus("mandatory")
_AtmLecActualMaxDataFrameSize_Type = LecDataFrameSize
_AtmLecActualMaxDataFrameSize_Object = MibTableColumn
atmLecActualMaxDataFrameSize = _AtmLecActualMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 15),
    _AtmLecActualMaxDataFrameSize_Type()
)
atmLecActualMaxDataFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecActualMaxDataFrameSize.setStatus("mandatory")


class _AtmLecActualLanName_Type(DisplayString):
    """Custom type atmLecActualLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtmLecActualLanName_Type.__name__ = "DisplayString"
_AtmLecActualLanName_Object = MibTableColumn
atmLecActualLanName = _AtmLecActualLanName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 16),
    _AtmLecActualLanName_Type()
)
atmLecActualLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecActualLanName.setStatus("mandatory")
_AtmLecActualLesAtmAddress_Type = XylanAtmLaneAddress
_AtmLecActualLesAtmAddress_Object = MibTableColumn
atmLecActualLesAtmAddress = _AtmLecActualLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 17),
    _AtmLecActualLesAtmAddress_Type()
)
atmLecActualLesAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecActualLesAtmAddress.setStatus("mandatory")
_AtmLecProxyClient_Type = Integer32
_AtmLecProxyClient_Object = MibTableColumn
atmLecProxyClient = _AtmLecProxyClient_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 2, 1, 18),
    _AtmLecProxyClient_Type()
)
atmLecProxyClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecProxyClient.setStatus("mandatory")
_AtmLecStatisticsTable_Object = MibTable
atmLecStatisticsTable = _AtmLecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3)
)
if mibBuilder.loadTexts:
    atmLecStatisticsTable.setStatus("mandatory")
_AtmLecStatisticsEntry_Object = MibTableRow
atmLecStatisticsEntry = _AtmLecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1)
)
atmLecStatisticsEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxLecStatsSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxLecStatsPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxLecStatsServiceNum"),
)
if mibBuilder.loadTexts:
    atmLecStatisticsEntry.setStatus("mandatory")
_AtmxLecStatsSlotIndex_Type = Integer32
_AtmxLecStatsSlotIndex_Object = MibTableColumn
atmxLecStatsSlotIndex = _AtmxLecStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1, 1),
    _AtmxLecStatsSlotIndex_Type()
)
atmxLecStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsSlotIndex.setStatus("mandatory")
_AtmxLecStatsPortIndex_Type = Integer32
_AtmxLecStatsPortIndex_Object = MibTableColumn
atmxLecStatsPortIndex = _AtmxLecStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1, 2),
    _AtmxLecStatsPortIndex_Type()
)
atmxLecStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsPortIndex.setStatus("mandatory")
_AtmxLecStatsServiceNum_Type = Integer32
_AtmxLecStatsServiceNum_Object = MibTableColumn
atmxLecStatsServiceNum = _AtmxLecStatsServiceNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1, 3),
    _AtmxLecStatsServiceNum_Type()
)
atmxLecStatsServiceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsServiceNum.setStatus("mandatory")
_AtmLecArpRequestsOut_Type = Counter32
_AtmLecArpRequestsOut_Object = MibTableColumn
atmLecArpRequestsOut = _AtmLecArpRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1, 4),
    _AtmLecArpRequestsOut_Type()
)
atmLecArpRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecArpRequestsOut.setStatus("mandatory")
_AtmLecArpRequestsIn_Type = Counter32
_AtmLecArpRequestsIn_Object = MibTableColumn
atmLecArpRequestsIn = _AtmLecArpRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1, 5),
    _AtmLecArpRequestsIn_Type()
)
atmLecArpRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecArpRequestsIn.setStatus("mandatory")
_AtmLecArpRepliesOut_Type = Counter32
_AtmLecArpRepliesOut_Object = MibTableColumn
atmLecArpRepliesOut = _AtmLecArpRepliesOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1, 6),
    _AtmLecArpRepliesOut_Type()
)
atmLecArpRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecArpRepliesOut.setStatus("mandatory")
_AtmLecArpRepliesIn_Type = Counter32
_AtmLecArpRepliesIn_Object = MibTableColumn
atmLecArpRepliesIn = _AtmLecArpRepliesIn_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1, 7),
    _AtmLecArpRepliesIn_Type()
)
atmLecArpRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecArpRepliesIn.setStatus("mandatory")
_AtmLecControlFramesOut_Type = Counter32
_AtmLecControlFramesOut_Object = MibTableColumn
atmLecControlFramesOut = _AtmLecControlFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1, 8),
    _AtmLecControlFramesOut_Type()
)
atmLecControlFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecControlFramesOut.setStatus("mandatory")
_AtmLecControlFramesIn_Type = Counter32
_AtmLecControlFramesIn_Object = MibTableColumn
atmLecControlFramesIn = _AtmLecControlFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1, 9),
    _AtmLecControlFramesIn_Type()
)
atmLecControlFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecControlFramesIn.setStatus("mandatory")
_AtmLecSvcFailures_Type = Counter32
_AtmLecSvcFailures_Object = MibTableColumn
atmLecSvcFailures = _AtmLecSvcFailures_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 3, 1, 10),
    _AtmLecSvcFailures_Type()
)
atmLecSvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecSvcFailures.setStatus("mandatory")
_AtmLecServerVccTable_Object = MibTable
atmLecServerVccTable = _AtmLecServerVccTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4)
)
if mibBuilder.loadTexts:
    atmLecServerVccTable.setStatus("mandatory")
_AtmLecServerVccEntry_Object = MibTableRow
atmLecServerVccEntry = _AtmLecServerVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1)
)
atmLecServerVccEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxLecSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxLecPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxLecServiceNum"),
)
if mibBuilder.loadTexts:
    atmLecServerVccEntry.setStatus("mandatory")
_AtmxLecSlotIndex_Type = Integer32
_AtmxLecSlotIndex_Object = MibTableColumn
atmxLecSlotIndex = _AtmxLecSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 1),
    _AtmxLecSlotIndex_Type()
)
atmxLecSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecSlotIndex.setStatus("mandatory")
_AtmxLecPortIndex_Type = Integer32
_AtmxLecPortIndex_Object = MibTableColumn
atmxLecPortIndex = _AtmxLecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 2),
    _AtmxLecPortIndex_Type()
)
atmxLecPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecPortIndex.setStatus("mandatory")
_AtmxLecServiceNum_Type = Integer32
_AtmxLecServiceNum_Object = MibTableColumn
atmxLecServiceNum = _AtmxLecServiceNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 3),
    _AtmxLecServiceNum_Type()
)
atmxLecServiceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecServiceNum.setStatus("mandatory")
_AtmLecConfigDirectVpi_Type = VpiInteger
_AtmLecConfigDirectVpi_Object = MibTableColumn
atmLecConfigDirectVpi = _AtmLecConfigDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 4),
    _AtmLecConfigDirectVpi_Type()
)
atmLecConfigDirectVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecConfigDirectVpi.setStatus("mandatory")
_AtmLecConfigDirectVci_Type = VciInteger
_AtmLecConfigDirectVci_Object = MibTableColumn
atmLecConfigDirectVci = _AtmLecConfigDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 5),
    _AtmLecConfigDirectVci_Type()
)
atmLecConfigDirectVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecConfigDirectVci.setStatus("mandatory")
_AtmLecControlDirectVpi_Type = VpiInteger
_AtmLecControlDirectVpi_Object = MibTableColumn
atmLecControlDirectVpi = _AtmLecControlDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 6),
    _AtmLecControlDirectVpi_Type()
)
atmLecControlDirectVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecControlDirectVpi.setStatus("mandatory")
_AtmLecControlDirectVci_Type = VciInteger
_AtmLecControlDirectVci_Object = MibTableColumn
atmLecControlDirectVci = _AtmLecControlDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 7),
    _AtmLecControlDirectVci_Type()
)
atmLecControlDirectVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecControlDirectVci.setStatus("mandatory")
_AtmLecControlDistributeVpi_Type = VpiInteger
_AtmLecControlDistributeVpi_Object = MibTableColumn
atmLecControlDistributeVpi = _AtmLecControlDistributeVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 8),
    _AtmLecControlDistributeVpi_Type()
)
atmLecControlDistributeVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecControlDistributeVpi.setStatus("mandatory")
_AtmLecControlDistributeVci_Type = VciInteger
_AtmLecControlDistributeVci_Object = MibTableColumn
atmLecControlDistributeVci = _AtmLecControlDistributeVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 9),
    _AtmLecControlDistributeVci_Type()
)
atmLecControlDistributeVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecControlDistributeVci.setStatus("mandatory")
_AtmLecMulticastSendVpi_Type = VpiInteger
_AtmLecMulticastSendVpi_Object = MibTableColumn
atmLecMulticastSendVpi = _AtmLecMulticastSendVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 10),
    _AtmLecMulticastSendVpi_Type()
)
atmLecMulticastSendVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecMulticastSendVpi.setStatus("mandatory")
_AtmLecMulticastSendVci_Type = VciInteger
_AtmLecMulticastSendVci_Object = MibTableColumn
atmLecMulticastSendVci = _AtmLecMulticastSendVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 11),
    _AtmLecMulticastSendVci_Type()
)
atmLecMulticastSendVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecMulticastSendVci.setStatus("mandatory")
_AtmLecMulticastForwardVpi_Type = VpiInteger
_AtmLecMulticastForwardVpi_Object = MibTableColumn
atmLecMulticastForwardVpi = _AtmLecMulticastForwardVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 12),
    _AtmLecMulticastForwardVpi_Type()
)
atmLecMulticastForwardVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecMulticastForwardVpi.setStatus("mandatory")
_AtmLecMulticastForwardVci_Type = VciInteger
_AtmLecMulticastForwardVci_Object = MibTableColumn
atmLecMulticastForwardVci = _AtmLecMulticastForwardVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 4, 1, 13),
    _AtmLecMulticastForwardVci_Type()
)
atmLecMulticastForwardVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLecMulticastForwardVci.setStatus("mandatory")
_AtmLeArpTable_Object = MibTable
atmLeArpTable = _AtmLeArpTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5)
)
if mibBuilder.loadTexts:
    atmLeArpTable.setStatus("mandatory")
_AtmLeArpEntry_Object = MibTableRow
atmLeArpEntry = _AtmLeArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1)
)
atmLeArpEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxLeArpSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxLeArpPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxLeArpServiceNum"),
    (0, "XYLAN-ATM-MIB", "atmLeArpIndex"),
)
if mibBuilder.loadTexts:
    atmLeArpEntry.setStatus("mandatory")
_AtmxLeArpSlotIndex_Type = Integer32
_AtmxLeArpSlotIndex_Object = MibTableColumn
atmxLeArpSlotIndex = _AtmxLeArpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 1),
    _AtmxLeArpSlotIndex_Type()
)
atmxLeArpSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLeArpSlotIndex.setStatus("mandatory")
_AtmxLeArpPortIndex_Type = Integer32
_AtmxLeArpPortIndex_Object = MibTableColumn
atmxLeArpPortIndex = _AtmxLeArpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 2),
    _AtmxLeArpPortIndex_Type()
)
atmxLeArpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLeArpPortIndex.setStatus("mandatory")
_AtmxLeArpServiceNum_Type = Integer32
_AtmxLeArpServiceNum_Object = MibTableColumn
atmxLeArpServiceNum = _AtmxLeArpServiceNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 3),
    _AtmxLeArpServiceNum_Type()
)
atmxLeArpServiceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLeArpServiceNum.setStatus("mandatory")
_AtmLeArpIndex_Type = Integer32
_AtmLeArpIndex_Object = MibTableColumn
atmLeArpIndex = _AtmLeArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 4),
    _AtmLeArpIndex_Type()
)
atmLeArpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLeArpIndex.setStatus("mandatory")
_AtmLeArpMacAddress_Type = MacAddress
_AtmLeArpMacAddress_Object = MibTableColumn
atmLeArpMacAddress = _AtmLeArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 5),
    _AtmLeArpMacAddress_Type()
)
atmLeArpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLeArpMacAddress.setStatus("mandatory")
_AtmLeArpAtmAddress_Type = XylanAtmLaneAddress
_AtmLeArpAtmAddress_Object = MibTableColumn
atmLeArpAtmAddress = _AtmLeArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 6),
    _AtmLeArpAtmAddress_Type()
)
atmLeArpAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLeArpAtmAddress.setStatus("mandatory")
_AtmLeArpIsRemoteAddress_Type = Integer32
_AtmLeArpIsRemoteAddress_Object = MibTableColumn
atmLeArpIsRemoteAddress = _AtmLeArpIsRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 7),
    _AtmLeArpIsRemoteAddress_Type()
)
atmLeArpIsRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLeArpIsRemoteAddress.setStatus("mandatory")
_AtmLeArpEntryType_Type = LeArpTableEntryType
_AtmLeArpEntryType_Object = MibTableColumn
atmLeArpEntryType = _AtmLeArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 8),
    _AtmLeArpEntryType_Type()
)
atmLeArpEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLeArpEntryType.setStatus("mandatory")
_AtmLeArpVpi_Type = VpiInteger
_AtmLeArpVpi_Object = MibTableColumn
atmLeArpVpi = _AtmLeArpVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 9),
    _AtmLeArpVpi_Type()
)
atmLeArpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLeArpVpi.setStatus("mandatory")
_AtmLeArpVci_Type = VciInteger
_AtmLeArpVci_Object = MibTableColumn
atmLeArpVci = _AtmLeArpVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 10),
    _AtmLeArpVci_Type()
)
atmLeArpVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLeArpVci.setStatus("mandatory")
_AtmLeArpAge_Type = Integer32
_AtmLeArpAge_Object = MibTableColumn
atmLeArpAge = _AtmLeArpAge_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 11),
    _AtmLeArpAge_Type()
)
atmLeArpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLeArpAge.setStatus("mandatory")
_AtmLeArpType_Type = LeArpType
_AtmLeArpType_Object = MibTableColumn
atmLeArpType = _AtmLeArpType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 5, 1, 12),
    _AtmLeArpType_Type()
)
atmLeArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLeArpType.setStatus("mandatory")
_XylanLecConfigTable_Object = MibTable
xylanLecConfigTable = _XylanLecConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 6)
)
if mibBuilder.loadTexts:
    xylanLecConfigTable.setStatus("mandatory")
_XylanLecConfigEntry_Object = MibTableRow
xylanLecConfigEntry = _XylanLecConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 6, 1)
)
xylanLecConfigEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    xylanLecConfigEntry.setStatus("mandatory")
_XylanLecSlotNumber_Type = Integer32
_XylanLecSlotNumber_Object = MibTableColumn
xylanLecSlotNumber = _XylanLecSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 6, 1, 1),
    _XylanLecSlotNumber_Type()
)
xylanLecSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanLecSlotNumber.setStatus("mandatory")
_XylanLecPortNumber_Type = Integer32
_XylanLecPortNumber_Object = MibTableColumn
xylanLecPortNumber = _XylanLecPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 6, 1, 2),
    _XylanLecPortNumber_Type()
)
xylanLecPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanLecPortNumber.setStatus("mandatory")
_XylanLecServiceNumber_Type = Integer32
_XylanLecServiceNumber_Object = MibTableColumn
xylanLecServiceNumber = _XylanLecServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 6, 1, 3),
    _XylanLecServiceNumber_Type()
)
xylanLecServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanLecServiceNumber.setStatus("mandatory")
_XylanLecGroupNumber_Type = Integer32
_XylanLecGroupNumber_Object = MibTableColumn
xylanLecGroupNumber = _XylanLecGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 8, 6, 1, 4),
    _XylanLecGroupNumber_Type()
)
xylanLecGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanLecGroupNumber.setStatus("mandatory")
_AtmxCIPstatsGroup_ObjectIdentity = ObjectIdentity
atmxCIPstatsGroup = _AtmxCIPstatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9)
)
_AtmCIPStatisticsTable_Object = MibTable
atmCIPStatisticsTable = _AtmCIPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1)
)
if mibBuilder.loadTexts:
    atmCIPStatisticsTable.setStatus("mandatory")
_AtmCIPStatisticsEntry_Object = MibTableRow
atmCIPStatisticsEntry = _AtmCIPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1)
)
atmCIPStatisticsEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxCIPSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxCIPPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxCIPServiceNum"),
)
if mibBuilder.loadTexts:
    atmCIPStatisticsEntry.setStatus("mandatory")
_AtmxCIPSlotIndex_Type = Integer32
_AtmxCIPSlotIndex_Object = MibTableColumn
atmxCIPSlotIndex = _AtmxCIPSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 1),
    _AtmxCIPSlotIndex_Type()
)
atmxCIPSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCIPSlotIndex.setStatus("mandatory")
_AtmxCIPPortIndex_Type = Integer32
_AtmxCIPPortIndex_Object = MibTableColumn
atmxCIPPortIndex = _AtmxCIPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 2),
    _AtmxCIPPortIndex_Type()
)
atmxCIPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCIPPortIndex.setStatus("mandatory")
_AtmxCIPServiceNum_Type = Integer32
_AtmxCIPServiceNum_Object = MibTableColumn
atmxCIPServiceNum = _AtmxCIPServiceNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 3),
    _AtmxCIPServiceNum_Type()
)
atmxCIPServiceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCIPServiceNum.setStatus("mandatory")
_AtmCIPpktsFromIP_Type = Counter32
_AtmCIPpktsFromIP_Object = MibTableColumn
atmCIPpktsFromIP = _AtmCIPpktsFromIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 4),
    _AtmCIPpktsFromIP_Type()
)
atmCIPpktsFromIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPpktsFromIP.setStatus("mandatory")
_AtmCIPBroadcastPktFromIP_Type = Counter32
_AtmCIPBroadcastPktFromIP_Object = MibTableColumn
atmCIPBroadcastPktFromIP = _AtmCIPBroadcastPktFromIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 5),
    _AtmCIPBroadcastPktFromIP_Type()
)
atmCIPBroadcastPktFromIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPBroadcastPktFromIP.setStatus("mandatory")
_AtmCIPPktsFromIPDiscard_Type = Counter32
_AtmCIPPktsFromIPDiscard_Object = MibTableColumn
atmCIPPktsFromIPDiscard = _AtmCIPPktsFromIPDiscard_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 6),
    _AtmCIPPktsFromIPDiscard_Type()
)
atmCIPPktsFromIPDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPPktsFromIPDiscard.setStatus("mandatory")
_AtmCIPPktsToIP_Type = Counter32
_AtmCIPPktsToIP_Object = MibTableColumn
atmCIPPktsToIP = _AtmCIPPktsToIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 7),
    _AtmCIPPktsToIP_Type()
)
atmCIPPktsToIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPPktsToIP.setStatus("mandatory")
_AtmCIPPktsFromNet_Type = Counter32
_AtmCIPPktsFromNet_Object = MibTableColumn
atmCIPPktsFromNet = _AtmCIPPktsFromNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 8),
    _AtmCIPPktsFromNet_Type()
)
atmCIPPktsFromNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPPktsFromNet.setStatus("mandatory")
_AtmCIPPktsFromNetDiscard_Type = Counter32
_AtmCIPPktsFromNetDiscard_Object = MibTableColumn
atmCIPPktsFromNetDiscard = _AtmCIPPktsFromNetDiscard_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 9),
    _AtmCIPPktsFromNetDiscard_Type()
)
atmCIPPktsFromNetDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPPktsFromNetDiscard.setStatus("mandatory")
_AtmCIPArpRespFromNet_Type = Counter32
_AtmCIPArpRespFromNet_Object = MibTableColumn
atmCIPArpRespFromNet = _AtmCIPArpRespFromNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 10),
    _AtmCIPArpRespFromNet_Type()
)
atmCIPArpRespFromNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPArpRespFromNet.setStatus("mandatory")
_AtmCIPArpReqFromNet_Type = Counter32
_AtmCIPArpReqFromNet_Object = MibTableColumn
atmCIPArpReqFromNet = _AtmCIPArpReqFromNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 11),
    _AtmCIPArpReqFromNet_Type()
)
atmCIPArpReqFromNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPArpReqFromNet.setStatus("mandatory")
_AtmCIPInvArpRespFromNet_Type = Counter32
_AtmCIPInvArpRespFromNet_Object = MibTableColumn
atmCIPInvArpRespFromNet = _AtmCIPInvArpRespFromNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 12),
    _AtmCIPInvArpRespFromNet_Type()
)
atmCIPInvArpRespFromNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPInvArpRespFromNet.setStatus("mandatory")
_AtmCIPInvArpReqFromNet_Type = Counter32
_AtmCIPInvArpReqFromNet_Object = MibTableColumn
atmCIPInvArpReqFromNet = _AtmCIPInvArpReqFromNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 13),
    _AtmCIPInvArpReqFromNet_Type()
)
atmCIPInvArpReqFromNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPInvArpReqFromNet.setStatus("mandatory")
_AtmCIPInvArpNakFromNet_Type = Counter32
_AtmCIPInvArpNakFromNet_Object = MibTableColumn
atmCIPInvArpNakFromNet = _AtmCIPInvArpNakFromNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 14),
    _AtmCIPInvArpNakFromNet_Type()
)
atmCIPInvArpNakFromNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPInvArpNakFromNet.setStatus("mandatory")
_AtmCIPPktsToNet_Type = Counter32
_AtmCIPPktsToNet_Object = MibTableColumn
atmCIPPktsToNet = _AtmCIPPktsToNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 15),
    _AtmCIPPktsToNet_Type()
)
atmCIPPktsToNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPPktsToNet.setStatus("mandatory")
_AtmCIPPktsToNetDiscard_Type = Counter32
_AtmCIPPktsToNetDiscard_Object = MibTableColumn
atmCIPPktsToNetDiscard = _AtmCIPPktsToNetDiscard_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 16),
    _AtmCIPPktsToNetDiscard_Type()
)
atmCIPPktsToNetDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPPktsToNetDiscard.setStatus("mandatory")
_AtmCIPArpRespToNet_Type = Counter32
_AtmCIPArpRespToNet_Object = MibTableColumn
atmCIPArpRespToNet = _AtmCIPArpRespToNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 17),
    _AtmCIPArpRespToNet_Type()
)
atmCIPArpRespToNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPArpRespToNet.setStatus("mandatory")
_AtmCIPArpReqToNet_Type = Counter32
_AtmCIPArpReqToNet_Object = MibTableColumn
atmCIPArpReqToNet = _AtmCIPArpReqToNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 18),
    _AtmCIPArpReqToNet_Type()
)
atmCIPArpReqToNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPArpReqToNet.setStatus("mandatory")
_AtmCIPInvArpRespToNet_Type = Counter32
_AtmCIPInvArpRespToNet_Object = MibTableColumn
atmCIPInvArpRespToNet = _AtmCIPInvArpRespToNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 19),
    _AtmCIPInvArpRespToNet_Type()
)
atmCIPInvArpRespToNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPInvArpRespToNet.setStatus("mandatory")
_AtmCIPInvArpReqToNet_Type = Counter32
_AtmCIPInvArpReqToNet_Object = MibTableColumn
atmCIPInvArpReqToNet = _AtmCIPInvArpReqToNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 20),
    _AtmCIPInvArpReqToNet_Type()
)
atmCIPInvArpReqToNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPInvArpReqToNet.setStatus("mandatory")
_AtmCIPInvArpNakToNet_Type = Counter32
_AtmCIPInvArpNakToNet_Object = MibTableColumn
atmCIPInvArpNakToNet = _AtmCIPInvArpNakToNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 9, 1, 1, 21),
    _AtmCIPInvArpNakToNet_Type()
)
atmCIPInvArpNakToNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCIPInvArpNakToNet.setStatus("mandatory")
_AtmxSahiBWGroup_ObjectIdentity = ObjectIdentity
atmxSahiBWGroup = _AtmxSahiBWGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11)
)
_AtmxBwgTable_Object = MibTable
atmxBwgTable = _AtmxBwgTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 1)
)
if mibBuilder.loadTexts:
    atmxBwgTable.setStatus("mandatory")
_AtmxBwgEntry_Object = MibTableRow
atmxBwgEntry = _AtmxBwgEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 1, 1)
)
atmxBwgEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxBwgSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxBwgPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxBwgNum"),
)
if mibBuilder.loadTexts:
    atmxBwgEntry.setStatus("mandatory")


class _AtmxBwgSlotIndex_Type(Integer32):
    """Custom type atmxBwgSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxBwgSlotIndex_Type.__name__ = "Integer32"
_AtmxBwgSlotIndex_Object = MibTableColumn
atmxBwgSlotIndex = _AtmxBwgSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 1, 1, 1),
    _AtmxBwgSlotIndex_Type()
)
atmxBwgSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxBwgSlotIndex.setStatus("mandatory")


class _AtmxBwgPortIndex_Type(Integer32):
    """Custom type atmxBwgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AtmxBwgPortIndex_Type.__name__ = "Integer32"
_AtmxBwgPortIndex_Object = MibTableColumn
atmxBwgPortIndex = _AtmxBwgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 1, 1, 2),
    _AtmxBwgPortIndex_Type()
)
atmxBwgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxBwgPortIndex.setStatus("mandatory")


class _AtmxBwgNum_Type(Integer32):
    """Custom type atmxBwgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtmxBwgNum_Type.__name__ = "Integer32"
_AtmxBwgNum_Object = MibTableColumn
atmxBwgNum = _AtmxBwgNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 1, 1, 3),
    _AtmxBwgNum_Type()
)
atmxBwgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxBwgNum.setStatus("mandatory")


class _AtmxBwgBE_Type(Integer32):
    """Custom type atmxBwgBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmxBwgBE_Type.__name__ = "Integer32"
_AtmxBwgBE_Object = MibTableColumn
atmxBwgBE = _AtmxBwgBE_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 1, 1, 4),
    _AtmxBwgBE_Type()
)
atmxBwgBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxBwgBE.setStatus("mandatory")


class _AtmxBwgPcr_Type(Integer32):
    """Custom type atmxBwgPcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(535, 150000),
    )


_AtmxBwgPcr_Type.__name__ = "Integer32"
_AtmxBwgPcr_Object = MibTableColumn
atmxBwgPcr = _AtmxBwgPcr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 1, 1, 5),
    _AtmxBwgPcr_Type()
)
atmxBwgPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxBwgPcr.setStatus("mandatory")


class _AtmxBwgScr_Type(Integer32):
    """Custom type atmxBwgScr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 150000),
    )


_AtmxBwgScr_Type.__name__ = "Integer32"
_AtmxBwgScr_Object = MibTableColumn
atmxBwgScr = _AtmxBwgScr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 1, 1, 6),
    _AtmxBwgScr_Type()
)
atmxBwgScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxBwgScr.setStatus("mandatory")


class _AtmxBwgMbs_Type(Integer32):
    """Custom type atmxBwgMbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 124),
    )


_AtmxBwgMbs_Type.__name__ = "Integer32"
_AtmxBwgMbs_Object = MibTableColumn
atmxBwgMbs = _AtmxBwgMbs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 1, 1, 7),
    _AtmxBwgMbs_Type()
)
atmxBwgMbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxBwgMbs.setStatus("mandatory")
_AtmxBwgOperStatus_Type = AtmOperStatCodes
_AtmxBwgOperStatus_Object = MibTableColumn
atmxBwgOperStatus = _AtmxBwgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 1, 1, 8),
    _AtmxBwgOperStatus_Type()
)
atmxBwgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxBwgOperStatus.setStatus("mandatory")
_AtmxBwgServiceTable_Object = MibTable
atmxBwgServiceTable = _AtmxBwgServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 2)
)
if mibBuilder.loadTexts:
    atmxBwgServiceTable.setStatus("mandatory")
_AtmxBwgServiceEntry_Object = MibTableRow
atmxBwgServiceEntry = _AtmxBwgServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 2, 1)
)
atmxBwgServiceEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxBwgSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxBwgPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxBwgNum"),
    (0, "XYLAN-ATM-MIB", "atmxBwgServiceNum"),
)
if mibBuilder.loadTexts:
    atmxBwgServiceEntry.setStatus("mandatory")
_AtmxBwgServiceNum_Type = Integer32
_AtmxBwgServiceNum_Object = MibTableColumn
atmxBwgServiceNum = _AtmxBwgServiceNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 11, 2, 1, 1),
    _AtmxBwgServiceNum_Type()
)
atmxBwgServiceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxBwgServiceNum.setStatus("mandatory")
_Atmx1483ScaleGroup_ObjectIdentity = ObjectIdentity
atmx1483ScaleGroup = _Atmx1483ScaleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12)
)
_AtmGpToVcMappingTable_Object = MibTable
atmGpToVcMappingTable = _AtmGpToVcMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 1)
)
if mibBuilder.loadTexts:
    atmGpToVcMappingTable.setStatus("mandatory")
_AtmGpToVcMappingEntry_Object = MibTableRow
atmGpToVcMappingEntry = _AtmGpToVcMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 1, 1)
)
atmGpToVcMappingEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxGpToVcSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxGpToVcPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxGpToVcServiceNum"),
    (0, "XYLAN-ATM-MIB", "atmxGpToVcGroupId"),
)
if mibBuilder.loadTexts:
    atmGpToVcMappingEntry.setStatus("mandatory")
_AtmxGpToVcSlotIndex_Type = Integer32
_AtmxGpToVcSlotIndex_Object = MibTableColumn
atmxGpToVcSlotIndex = _AtmxGpToVcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 1, 1, 1),
    _AtmxGpToVcSlotIndex_Type()
)
atmxGpToVcSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxGpToVcSlotIndex.setStatus("mandatory")
_AtmxGpToVcPortIndex_Type = Integer32
_AtmxGpToVcPortIndex_Object = MibTableColumn
atmxGpToVcPortIndex = _AtmxGpToVcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 1, 1, 2),
    _AtmxGpToVcPortIndex_Type()
)
atmxGpToVcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxGpToVcPortIndex.setStatus("mandatory")
_AtmxGpToVcServiceNum_Type = Integer32
_AtmxGpToVcServiceNum_Object = MibTableColumn
atmxGpToVcServiceNum = _AtmxGpToVcServiceNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 1, 1, 3),
    _AtmxGpToVcServiceNum_Type()
)
atmxGpToVcServiceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxGpToVcServiceNum.setStatus("mandatory")
_AtmxGpToVcGroupId_Type = Integer32
_AtmxGpToVcGroupId_Object = MibTableColumn
atmxGpToVcGroupId = _AtmxGpToVcGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 1, 1, 4),
    _AtmxGpToVcGroupId_Type()
)
atmxGpToVcGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxGpToVcGroupId.setStatus("mandatory")
_AtmxGpToVcVpi_Type = Integer32
_AtmxGpToVcVpi_Object = MibTableColumn
atmxGpToVcVpi = _AtmxGpToVcVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 1, 1, 5),
    _AtmxGpToVcVpi_Type()
)
atmxGpToVcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxGpToVcVpi.setStatus("mandatory")
_AtmxGpToVcVci_Type = Integer32
_AtmxGpToVcVci_Object = MibTableColumn
atmxGpToVcVci = _AtmxGpToVcVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 1, 1, 6),
    _AtmxGpToVcVci_Type()
)
atmxGpToVcVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxGpToVcVci.setStatus("mandatory")


class _AtmxGpToVcRowStatus_Type(Integer32):
    """Custom type atmxGpToVcRowStatus based on Integer32"""
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
        *(("active", 3),
          ("create", 1),
          ("delete", 2),
          ("inactive", 4))
    )


_AtmxGpToVcRowStatus_Type.__name__ = "Integer32"
_AtmxGpToVcRowStatus_Object = MibTableColumn
atmxGpToVcRowStatus = _AtmxGpToVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 1, 1, 7),
    _AtmxGpToVcRowStatus_Type()
)
atmxGpToVcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxGpToVcRowStatus.setStatus("mandatory")
_AtmGpToVcBulkMappingTable_Object = MibTable
atmGpToVcBulkMappingTable = _AtmGpToVcBulkMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 2)
)
if mibBuilder.loadTexts:
    atmGpToVcBulkMappingTable.setStatus("mandatory")
_AtmGpToVcBulkMappingEntry_Object = MibTableRow
atmGpToVcBulkMappingEntry = _AtmGpToVcBulkMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 2, 1)
)
atmGpToVcBulkMappingEntry.setIndexNames(
    (0, "XYLAN-ATM-MIB", "atmxGpToVcBulkSlotIndex"),
    (0, "XYLAN-ATM-MIB", "atmxGpToVcBulkPortIndex"),
    (0, "XYLAN-ATM-MIB", "atmxGpToVcBulkServiceNum"),
)
if mibBuilder.loadTexts:
    atmGpToVcBulkMappingEntry.setStatus("mandatory")
_AtmxGpToVcBulkSlotIndex_Type = Integer32
_AtmxGpToVcBulkSlotIndex_Object = MibTableColumn
atmxGpToVcBulkSlotIndex = _AtmxGpToVcBulkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 2, 1, 1),
    _AtmxGpToVcBulkSlotIndex_Type()
)
atmxGpToVcBulkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxGpToVcBulkSlotIndex.setStatus("mandatory")
_AtmxGpToVcBulkPortIndex_Type = Integer32
_AtmxGpToVcBulkPortIndex_Object = MibTableColumn
atmxGpToVcBulkPortIndex = _AtmxGpToVcBulkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 2, 1, 2),
    _AtmxGpToVcBulkPortIndex_Type()
)
atmxGpToVcBulkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxGpToVcBulkPortIndex.setStatus("mandatory")
_AtmxGpToVcBulkServiceNum_Type = Integer32
_AtmxGpToVcBulkServiceNum_Object = MibTableColumn
atmxGpToVcBulkServiceNum = _AtmxGpToVcBulkServiceNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 2, 1, 3),
    _AtmxGpToVcBulkServiceNum_Type()
)
atmxGpToVcBulkServiceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxGpToVcBulkServiceNum.setStatus("mandatory")
_AtmxGpToVcBulkNumOfNodes_Type = Integer32
_AtmxGpToVcBulkNumOfNodes_Object = MibTableColumn
atmxGpToVcBulkNumOfNodes = _AtmxGpToVcBulkNumOfNodes_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 2, 1, 4),
    _AtmxGpToVcBulkNumOfNodes_Type()
)
atmxGpToVcBulkNumOfNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxGpToVcBulkNumOfNodes.setStatus("mandatory")


class _AtmxGpToVcBulkMappingList_Type(OctetString):
    """Custom type atmxGpToVcBulkMappingList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8000),
    )


_AtmxGpToVcBulkMappingList_Type.__name__ = "OctetString"
_AtmxGpToVcBulkMappingList_Object = MibTableColumn
atmxGpToVcBulkMappingList = _AtmxGpToVcBulkMappingList_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 12, 2, 1, 5),
    _AtmxGpToVcBulkMappingList_Type()
)
atmxGpToVcBulkMappingList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxGpToVcBulkMappingList.setStatus("mandatory")
_AtmxLsmGroup_ObjectIdentity = ObjectIdentity
atmxLsmGroup = _AtmxLsmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 13)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-ATM-MIB",
    **{"AtmAdminStatCodes": AtmAdminStatCodes,
       "AtmOperStatCodes": AtmOperStatCodes,
       "AtmServiceOperStatCodes": AtmServiceOperStatCodes,
       "AtmConnectionOperStatCodes": AtmConnectionOperStatCodes,
       "AtmTransmissionTypes": AtmTransmissionTypes,
       "AtmMediaTypes": AtmMediaTypes,
       "AtmTrafficDescrTypes": AtmTrafficDescrTypes,
       "XylanAtmLaneAddress": XylanAtmLaneAddress,
       "VpiInteger": VpiInteger,
       "VciInteger": VciInteger,
       "LecState": LecState,
       "LecDataFrameFormat": LecDataFrameFormat,
       "LeArpTableEntryType": LeArpTableEntryType,
       "LeArpType": LeArpType,
       "atmxPortGroup": atmxPortGroup,
       "atmxPortTable": atmxPortTable,
       "atmxPortEntry": atmxPortEntry,
       "atmxPortSlotIndex": atmxPortSlotIndex,
       "atmxPortPortIndex": atmxPortPortIndex,
       "atmxPortDescription": atmxPortDescription,
       "atmxPortConnectionType": atmxPortConnectionType,
       "atmxPortTransmissionType": atmxPortTransmissionType,
       "atmxPortMediaType": atmxPortMediaType,
       "atmxPortOperStatus": atmxPortOperStatus,
       "atmxPortUniType": atmxPortUniType,
       "atmxPortMaxVCCs": atmxPortMaxVCCs,
       "atmxPortMaxVciBits": atmxPortMaxVciBits,
       "atmxPortTxSegmentSize": atmxPortTxSegmentSize,
       "atmxPortRxSegmentSize": atmxPortRxSegmentSize,
       "atmxPortTxBufferSize": atmxPortTxBufferSize,
       "atmxPortRxBufferSize": atmxPortRxBufferSize,
       "atmxPortUniPortIndex": atmxPortUniPortIndex,
       "atmxPortAddress": atmxPortAddress,
       "atmxPortSignalingVersion": atmxPortSignalingVersion,
       "atmxPortSignalingVci": atmxPortSignalingVci,
       "atmxPortILMIVci": atmxPortILMIVci,
       "atmxPortEnableILMI": atmxPortEnableILMI,
       "atmxPortPlScramble": atmxPortPlScramble,
       "atmxPortTimingMode": atmxPortTimingMode,
       "atmxPortProtocolType": atmxPortProtocolType,
       "atmxPortLoopbackConfig": atmxPortLoopbackConfig,
       "atmxPortSSCOPstatus": atmxPortSSCOPstatus,
       "atmxPortILMIstatus": atmxPortILMIstatus,
       "atmxServiceGroup": atmxServiceGroup,
       "atmxServiceTable": atmxServiceTable,
       "atmxServiceEntry": atmxServiceEntry,
       "atmxServiceSlotIndex": atmxServiceSlotIndex,
       "atmxServicePortIndex": atmxServicePortIndex,
       "atmxServiceNumber": atmxServiceNumber,
       "atmxServiceDescription": atmxServiceDescription,
       "atmxServiceType": atmxServiceType,
       "atmxServiceConnectionType": atmxServiceConnectionType,
       "atmxServiceOperStatus": atmxServiceOperStatus,
       "atmxServiceAdmStatus": atmxServiceAdmStatus,
       "atmxServiceEncapsType": atmxServiceEncapsType,
       "atmxServiceArpRequestServer": atmxServiceArpRequestServer,
       "atmxServiceConnections": atmxServiceConnections,
       "atmxServiceAddress": atmxServiceAddress,
       "atmxServiceAddresses": atmxServiceAddresses,
       "atmxServiceVlan": atmxServiceVlan,
       "atmxServiceSEL": atmxServiceSEL,
       "atmxServiceLaneCfgTblIdx": atmxServiceLaneCfgTblIdx,
       "atmxServiceMulticastOutVcc": atmxServiceMulticastOutVcc,
       "atmxServiceNumVclMembers": atmxServiceNumVclMembers,
       "atmxServiceVclEncapType": atmxServiceVclEncapType,
       "atmxServiceSahiBwgNum": atmxServiceSahiBwgNum,
       "atmxLayerStatsGroup": atmxLayerStatsGroup,
       "atmxLayerStatsTable": atmxLayerStatsTable,
       "atmxLayerStatsEntry": atmxLayerStatsEntry,
       "atmxLayerStatsSlotIndex": atmxLayerStatsSlotIndex,
       "atmxLayerStatsPortIndex": atmxLayerStatsPortIndex,
       "atmxLayerStatsTxSDUs": atmxLayerStatsTxSDUs,
       "atmxLayerStatsTxCells": atmxLayerStatsTxCells,
       "atmxLayerStatsTxOctets": atmxLayerStatsTxOctets,
       "atmxLayerStatsRxSDUs": atmxLayerStatsRxSDUs,
       "atmxLayerStatsRxCells": atmxLayerStatsRxCells,
       "atmxLayerStatsRxOctets": atmxLayerStatsRxOctets,
       "atmxLayerStatsTxSDUDiscards": atmxLayerStatsTxSDUDiscards,
       "atmxLayerStatsTxSDUErrors": atmxLayerStatsTxSDUErrors,
       "atmxLayerStatsTxSDUNoBuffers": atmxLayerStatsTxSDUNoBuffers,
       "atmxLayerStatsTxCellDiscards": atmxLayerStatsTxCellDiscards,
       "atmxLayerStatsTxCellErrors": atmxLayerStatsTxCellErrors,
       "atmxLayerStatsTxCellNoBuffers": atmxLayerStatsTxCellNoBuffers,
       "atmxLayerStatsRxSDUDiscards": atmxLayerStatsRxSDUDiscards,
       "atmxLayerStatsRxSDUErrors": atmxLayerStatsRxSDUErrors,
       "atmxLayerStatsRxSDUInvalidSz": atmxLayerStatsRxSDUInvalidSz,
       "atmxLayerStatsRxSDUNoBuffers": atmxLayerStatsRxSDUNoBuffers,
       "atmxLayerStatsRxSDUTrash": atmxLayerStatsRxSDUTrash,
       "atmxLayerStatsRxSDUCrcErrors": atmxLayerStatsRxSDUCrcErrors,
       "atmxLayerStatsRxCellDiscards": atmxLayerStatsRxCellDiscards,
       "atmxLayerStatsRxCellErrors": atmxLayerStatsRxCellErrors,
       "atmxLayerStatsRxCellNoBuffers": atmxLayerStatsRxCellNoBuffers,
       "atmxLayerStatsRxCellTrash": atmxLayerStatsRxCellTrash,
       "atmxLayerStatsRxCellCrcErrors": atmxLayerStatsRxCellCrcErrors,
       "atmxVccStatsGroup": atmxVccStatsGroup,
       "atmxVccStatsTable": atmxVccStatsTable,
       "atmxVccStatsEntry": atmxVccStatsEntry,
       "atmxVccStatsSlotIndex": atmxVccStatsSlotIndex,
       "atmxVccStatsPortIndex": atmxVccStatsPortIndex,
       "atmxVccStatsVci": atmxVccStatsVci,
       "atmxVccStatsTxSDUs": atmxVccStatsTxSDUs,
       "atmxVccStatsTxCells": atmxVccStatsTxCells,
       "atmxVccStatsTxOctets": atmxVccStatsTxOctets,
       "atmxVccStatsRxSDUs": atmxVccStatsRxSDUs,
       "atmxVccStatsRxCells": atmxVccStatsRxCells,
       "atmxVccStatsRxOctets": atmxVccStatsRxOctets,
       "atmxVccStatsTxSDUDiscards": atmxVccStatsTxSDUDiscards,
       "atmxVccStatsTxSDUErrors": atmxVccStatsTxSDUErrors,
       "atmxVccStatsTxSDUNoBuffers": atmxVccStatsTxSDUNoBuffers,
       "atmxVccStatsTxCellDiscards": atmxVccStatsTxCellDiscards,
       "atmxVccStatsTxCellErrors": atmxVccStatsTxCellErrors,
       "atmxVccStatsTxCellNoBuffers": atmxVccStatsTxCellNoBuffers,
       "atmxVccStatsRxSDUDiscards": atmxVccStatsRxSDUDiscards,
       "atmxVccStatsRxSDUErrors": atmxVccStatsRxSDUErrors,
       "atmxVccStatsRxSDUInvalidSz": atmxVccStatsRxSDUInvalidSz,
       "atmxVccStatsRxSDUNoBuffers": atmxVccStatsRxSDUNoBuffers,
       "atmxVccStatsRxSDUTrash": atmxVccStatsRxSDUTrash,
       "atmxVccStatsRxSDUCrcErrors": atmxVccStatsRxSDUCrcErrors,
       "atmxVccStatsRxCellDiscards": atmxVccStatsRxCellDiscards,
       "atmxVccStatsRxCellErrors": atmxVccStatsRxCellErrors,
       "atmxVccStatsRxCellNoBuffers": atmxVccStatsRxCellNoBuffers,
       "atmxVccStatsRxCellTrash": atmxVccStatsRxCellTrash,
       "atmxVccStatsRxCellCrcErrors": atmxVccStatsRxCellCrcErrors,
       "atmxVccGroup": atmxVccGroup,
       "atmxVccTable": atmxVccTable,
       "atmxVccEntry": atmxVccEntry,
       "atmxVccSlotIndex": atmxVccSlotIndex,
       "atmxVccPortIndex": atmxVccPortIndex,
       "atmxVccVpi": atmxVccVpi,
       "atmxVccVci": atmxVccVci,
       "atmxVccDescription": atmxVccDescription,
       "atmxVccConnType": atmxVccConnType,
       "atmxVccCircuitType": atmxVccCircuitType,
       "atmxVccOperStatus": atmxVccOperStatus,
       "atmxVccUpTime": atmxVccUpTime,
       "atmxVccDownTime": atmxVccDownTime,
       "atmxVccTransmitMaxFrameSize": atmxVccTransmitMaxFrameSize,
       "atmxVccReceiveMaxFrameSize": atmxVccReceiveMaxFrameSize,
       "atmxVccRequestedTransmitTrafficDescriptor": atmxVccRequestedTransmitTrafficDescriptor,
       "atmxVccRequestedTransmitTrafficDescriptorParam1": atmxVccRequestedTransmitTrafficDescriptorParam1,
       "atmxVccRequestedTransmitTrafficDescriptorParam2": atmxVccRequestedTransmitTrafficDescriptorParam2,
       "atmxVccRequestedTransmitTrafficDescriptorParam3": atmxVccRequestedTransmitTrafficDescriptorParam3,
       "atmxVccRequestedTransmitTrafficQoSClass": atmxVccRequestedTransmitTrafficQoSClass,
       "atmxVccRequestedTransmitTrafficBestEffort": atmxVccRequestedTransmitTrafficBestEffort,
       "atmxVccRequestedReceiveTrafficDescriptor": atmxVccRequestedReceiveTrafficDescriptor,
       "atmxVccRequestedReceiveTrafficDescriptorParam1": atmxVccRequestedReceiveTrafficDescriptorParam1,
       "atmxVccRequestedReceiveTrafficDescriptorParam2": atmxVccRequestedReceiveTrafficDescriptorParam2,
       "atmxVccRequestedReceiveTrafficDescriptorParam3": atmxVccRequestedReceiveTrafficDescriptorParam3,
       "atmxVccRequestedReceiveTrafficQoSClass": atmxVccRequestedReceiveTrafficQoSClass,
       "atmxVccRequestedReceiveTrafficBestEffort": atmxVccRequestedReceiveTrafficBestEffort,
       "atmxVccAcceptableTransmitTrafficDescriptor": atmxVccAcceptableTransmitTrafficDescriptor,
       "atmxVccAcceptableTransmitTrafficDescriptorParam1": atmxVccAcceptableTransmitTrafficDescriptorParam1,
       "atmxVccAcceptableTransmitTrafficDescriptorParam2": atmxVccAcceptableTransmitTrafficDescriptorParam2,
       "atmxVccAcceptableTransmitTrafficDescriptorParam3": atmxVccAcceptableTransmitTrafficDescriptorParam3,
       "atmxVccAcceptableTransmitTrafficQoSClass": atmxVccAcceptableTransmitTrafficQoSClass,
       "atmxVccAcceptableTransmitTrafficBestEffort": atmxVccAcceptableTransmitTrafficBestEffort,
       "atmxVccAcceptableReceiveTrafficDescriptor": atmxVccAcceptableReceiveTrafficDescriptor,
       "atmxVccAcceptableReceiveTrafficDescriptorParam1": atmxVccAcceptableReceiveTrafficDescriptorParam1,
       "atmxVccAcceptableReceiveTrafficDescriptorParam2": atmxVccAcceptableReceiveTrafficDescriptorParam2,
       "atmxVccAcceptableReceiveTrafficDescriptorParam3": atmxVccAcceptableReceiveTrafficDescriptorParam3,
       "atmxVccAcceptableReceiveTrafficQoSClass": atmxVccAcceptableReceiveTrafficQoSClass,
       "atmxVccAcceptableReceiveTrafficBestEffort": atmxVccAcceptableReceiveTrafficBestEffort,
       "atmxVccActualTransmitTrafficDescriptor": atmxVccActualTransmitTrafficDescriptor,
       "atmxVccActualTransmitTrafficDescriptorParam1": atmxVccActualTransmitTrafficDescriptorParam1,
       "atmxVccActualTransmitTrafficDescriptorParam2": atmxVccActualTransmitTrafficDescriptorParam2,
       "atmxVccActualTransmitTrafficDescriptorParam3": atmxVccActualTransmitTrafficDescriptorParam3,
       "atmxVccActualTransmitTrafficQoSClass": atmxVccActualTransmitTrafficQoSClass,
       "atmxVccActualTransmitTrafficBestEffort": atmxVccActualTransmitTrafficBestEffort,
       "atmxVccActualReceiveTrafficDescriptor": atmxVccActualReceiveTrafficDescriptor,
       "atmxVccActualReceiveTrafficDescriptorParam1": atmxVccActualReceiveTrafficDescriptorParam1,
       "atmxVccActualReceiveTrafficDescriptorParam2": atmxVccActualReceiveTrafficDescriptorParam2,
       "atmxVccActualReceiveTrafficDescriptorParam3": atmxVccActualReceiveTrafficDescriptorParam3,
       "atmxVccActualReceiveTrafficQoSClass": atmxVccActualReceiveTrafficQoSClass,
       "atmxVccActualReceiveTrafficBestEffort": atmxVccActualReceiveTrafficBestEffort,
       "atmxVccAdmStatus": atmxVccAdmStatus,
       "atmxVccServiceUsed": atmxVccServiceUsed,
       "atmxVccConnectionUsed": atmxVccConnectionUsed,
       "atmxAddressGroup": atmxAddressGroup,
       "atmxAddressTable": atmxAddressTable,
       "atmxAddressEntry": atmxAddressEntry,
       "atmxAddressIndex": atmxAddressIndex,
       "atmxAddressAtmAddress": atmxAddressAtmAddress,
       "atmxAddressType": atmxAddressType,
       "atmxAddressVpi": atmxAddressVpi,
       "atmxAddressVci": atmxAddressVci,
       "atmxAddressDescription": atmxAddressDescription,
       "atmxAddressTransmitMaxSDU": atmxAddressTransmitMaxSDU,
       "atmxAddressReceiveMaxSDU": atmxAddressReceiveMaxSDU,
       "atmxAddressRequestedTransmitTrafficDescriptor": atmxAddressRequestedTransmitTrafficDescriptor,
       "atmxAddressRequestedTransmitTrafficDescriptorParam1": atmxAddressRequestedTransmitTrafficDescriptorParam1,
       "atmxAddressRequestedTransmitTrafficDescriptorParam2": atmxAddressRequestedTransmitTrafficDescriptorParam2,
       "atmxAddressRequestedTransmitTrafficDescriptorParam3": atmxAddressRequestedTransmitTrafficDescriptorParam3,
       "atmxAddressRequestedTransmitTrafficQoSClass": atmxAddressRequestedTransmitTrafficQoSClass,
       "atmxAddressRequestedTransmitTrafficBestEffort": atmxAddressRequestedTransmitTrafficBestEffort,
       "atmxAddressRequestedReceiveTrafficDescriptor": atmxAddressRequestedReceiveTrafficDescriptor,
       "atmxAddressRequestedReceiveTrafficDescriptorParam1": atmxAddressRequestedReceiveTrafficDescriptorParam1,
       "atmxAddressRequestedReceiveTrafficDescriptorParam2": atmxAddressRequestedReceiveTrafficDescriptorParam2,
       "atmxAddressRequestedReceiveTrafficDescriptorParam3": atmxAddressRequestedReceiveTrafficDescriptorParam3,
       "atmxAddressRequestedReceiveTrafficQoSClass": atmxAddressRequestedReceiveTrafficQoSClass,
       "atmxAddressRequestedReceiveTrafficBestEffort": atmxAddressRequestedReceiveTrafficBestEffort,
       "atmxAddressAcceptableTransmitTrafficDescriptor": atmxAddressAcceptableTransmitTrafficDescriptor,
       "atmxAddressAcceptableTransmitTrafficDescriptorParam1": atmxAddressAcceptableTransmitTrafficDescriptorParam1,
       "atmxAddressAcceptableTransmitTrafficDescriptorParam2": atmxAddressAcceptableTransmitTrafficDescriptorParam2,
       "atmxAddressAcceptableTransmitTrafficDescriptorParam3": atmxAddressAcceptableTransmitTrafficDescriptorParam3,
       "atmxAddressAcceptableTransmitTrafficQoSClass": atmxAddressAcceptableTransmitTrafficQoSClass,
       "atmxAddressAcceptableTransmitTrafficBestEffort": atmxAddressAcceptableTransmitTrafficBestEffort,
       "atmxAddressAcceptableReceiveTrafficDescriptor": atmxAddressAcceptableReceiveTrafficDescriptor,
       "atmxAddressAcceptableReceiveTrafficDescriptorParam1": atmxAddressAcceptableReceiveTrafficDescriptorParam1,
       "atmxAddressAcceptableReceiveTrafficDescriptorParam2": atmxAddressAcceptableReceiveTrafficDescriptorParam2,
       "atmxAddressAcceptableReceiveTrafficDescriptorParam3": atmxAddressAcceptableReceiveTrafficDescriptorParam3,
       "atmxAddressAcceptableReceiveTrafficQoSClass": atmxAddressAcceptableReceiveTrafficQoSClass,
       "atmxAddressAcceptableReceiveTrafficBestEffort": atmxAddressAcceptableReceiveTrafficBestEffort,
       "atmxAddressAdmStatus": atmxAddressAdmStatus,
       "atmxAddressServiceUsed": atmxAddressServiceUsed,
       "atmxAddressAddrUsed": atmxAddressAddrUsed,
       "atmxArpGroup": atmxArpGroup,
       "atmxArpTable": atmxArpTable,
       "atmxArpEntry": atmxArpEntry,
       "atmxArpIndex": atmxArpIndex,
       "atmxArpIPAddress": atmxArpIPAddress,
       "atmxArpAtmAddress": atmxArpAtmAddress,
       "atmxArpVci": atmxArpVci,
       "atmxArpTimeToLive": atmxArpTimeToLive,
       "atmxArpType": atmxArpType,
       "atmxLaneGroup": atmxLaneGroup,
       "atmLecConfigTable": atmLecConfigTable,
       "atmLecConfigEntry": atmLecConfigEntry,
       "atmxLecConfigIndex": atmxLecConfigIndex,
       "atmLecConfigLecsAtmAddress": atmLecConfigLecsAtmAddress,
       "atmLecConfigUseDefaultLecsAddr": atmLecConfigUseDefaultLecsAddr,
       "atmLecRowStatus": atmLecRowStatus,
       "atmLecRowInUse": atmLecRowInUse,
       "atmLecConfigMode": atmLecConfigMode,
       "atmLecConfigLanType": atmLecConfigLanType,
       "atmLecConfigMaxDataFrameSize": atmLecConfigMaxDataFrameSize,
       "atmLecConfigLanName": atmLecConfigLanName,
       "atmLecConfigLesAtmAddress": atmLecConfigLesAtmAddress,
       "atmLecControlTimeout": atmLecControlTimeout,
       "atmLecMaxUnknownFrameCount": atmLecMaxUnknownFrameCount,
       "atmLecMaxUnknownFrameTime": atmLecMaxUnknownFrameTime,
       "atmLecVccTimeoutPeriod": atmLecVccTimeoutPeriod,
       "atmLecMaxRetryCount": atmLecMaxRetryCount,
       "atmLecAgingTime": atmLecAgingTime,
       "atmLecForwardDelayTime": atmLecForwardDelayTime,
       "atmLecExpectedArpResponseTime": atmLecExpectedArpResponseTime,
       "atmLecFlushTimeOut": atmLecFlushTimeOut,
       "atmLecPathSwitchingDelay": atmLecPathSwitchingDelay,
       "atmLecUseForwardDelay": atmLecUseForwardDelay,
       "atmLecUseTranslation": atmLecUseTranslation,
       "atmLecSrBridgeNum": atmLecSrBridgeNum,
       "atmLecSrRingNum": atmLecSrRingNum,
       "atmLecStatusTable": atmLecStatusTable,
       "atmLecStatusEntry": atmLecStatusEntry,
       "atmxLecStatusSlotIndex": atmxLecStatusSlotIndex,
       "atmxLecStatusPortIndex": atmxLecStatusPortIndex,
       "atmxLecStatusServiceNum": atmxLecStatusServiceNum,
       "atmLecPrimaryAtmAddress": atmLecPrimaryAtmAddress,
       "atmLecID": atmLecID,
       "atmLecInterfaceState": atmLecInterfaceState,
       "atmLecLastFailureRespCode": atmLecLastFailureRespCode,
       "atmLecLastFailureState": atmLecLastFailureState,
       "atmLecProtocol": atmLecProtocol,
       "atmLecVersion": atmLecVersion,
       "atmLecTopologyChange": atmLecTopologyChange,
       "atmLecConfigServerAtmAddress": atmLecConfigServerAtmAddress,
       "atmLecConfigSource": atmLecConfigSource,
       "atmLecActualLanType": atmLecActualLanType,
       "atmLecActualMaxDataFrameSize": atmLecActualMaxDataFrameSize,
       "atmLecActualLanName": atmLecActualLanName,
       "atmLecActualLesAtmAddress": atmLecActualLesAtmAddress,
       "atmLecProxyClient": atmLecProxyClient,
       "atmLecStatisticsTable": atmLecStatisticsTable,
       "atmLecStatisticsEntry": atmLecStatisticsEntry,
       "atmxLecStatsSlotIndex": atmxLecStatsSlotIndex,
       "atmxLecStatsPortIndex": atmxLecStatsPortIndex,
       "atmxLecStatsServiceNum": atmxLecStatsServiceNum,
       "atmLecArpRequestsOut": atmLecArpRequestsOut,
       "atmLecArpRequestsIn": atmLecArpRequestsIn,
       "atmLecArpRepliesOut": atmLecArpRepliesOut,
       "atmLecArpRepliesIn": atmLecArpRepliesIn,
       "atmLecControlFramesOut": atmLecControlFramesOut,
       "atmLecControlFramesIn": atmLecControlFramesIn,
       "atmLecSvcFailures": atmLecSvcFailures,
       "atmLecServerVccTable": atmLecServerVccTable,
       "atmLecServerVccEntry": atmLecServerVccEntry,
       "atmxLecSlotIndex": atmxLecSlotIndex,
       "atmxLecPortIndex": atmxLecPortIndex,
       "atmxLecServiceNum": atmxLecServiceNum,
       "atmLecConfigDirectVpi": atmLecConfigDirectVpi,
       "atmLecConfigDirectVci": atmLecConfigDirectVci,
       "atmLecControlDirectVpi": atmLecControlDirectVpi,
       "atmLecControlDirectVci": atmLecControlDirectVci,
       "atmLecControlDistributeVpi": atmLecControlDistributeVpi,
       "atmLecControlDistributeVci": atmLecControlDistributeVci,
       "atmLecMulticastSendVpi": atmLecMulticastSendVpi,
       "atmLecMulticastSendVci": atmLecMulticastSendVci,
       "atmLecMulticastForwardVpi": atmLecMulticastForwardVpi,
       "atmLecMulticastForwardVci": atmLecMulticastForwardVci,
       "atmLeArpTable": atmLeArpTable,
       "atmLeArpEntry": atmLeArpEntry,
       "atmxLeArpSlotIndex": atmxLeArpSlotIndex,
       "atmxLeArpPortIndex": atmxLeArpPortIndex,
       "atmxLeArpServiceNum": atmxLeArpServiceNum,
       "atmLeArpIndex": atmLeArpIndex,
       "atmLeArpMacAddress": atmLeArpMacAddress,
       "atmLeArpAtmAddress": atmLeArpAtmAddress,
       "atmLeArpIsRemoteAddress": atmLeArpIsRemoteAddress,
       "atmLeArpEntryType": atmLeArpEntryType,
       "atmLeArpVpi": atmLeArpVpi,
       "atmLeArpVci": atmLeArpVci,
       "atmLeArpAge": atmLeArpAge,
       "atmLeArpType": atmLeArpType,
       "xylanLecConfigTable": xylanLecConfigTable,
       "xylanLecConfigEntry": xylanLecConfigEntry,
       "xylanLecSlotNumber": xylanLecSlotNumber,
       "xylanLecPortNumber": xylanLecPortNumber,
       "xylanLecServiceNumber": xylanLecServiceNumber,
       "xylanLecGroupNumber": xylanLecGroupNumber,
       "atmxCIPstatsGroup": atmxCIPstatsGroup,
       "atmCIPStatisticsTable": atmCIPStatisticsTable,
       "atmCIPStatisticsEntry": atmCIPStatisticsEntry,
       "atmxCIPSlotIndex": atmxCIPSlotIndex,
       "atmxCIPPortIndex": atmxCIPPortIndex,
       "atmxCIPServiceNum": atmxCIPServiceNum,
       "atmCIPpktsFromIP": atmCIPpktsFromIP,
       "atmCIPBroadcastPktFromIP": atmCIPBroadcastPktFromIP,
       "atmCIPPktsFromIPDiscard": atmCIPPktsFromIPDiscard,
       "atmCIPPktsToIP": atmCIPPktsToIP,
       "atmCIPPktsFromNet": atmCIPPktsFromNet,
       "atmCIPPktsFromNetDiscard": atmCIPPktsFromNetDiscard,
       "atmCIPArpRespFromNet": atmCIPArpRespFromNet,
       "atmCIPArpReqFromNet": atmCIPArpReqFromNet,
       "atmCIPInvArpRespFromNet": atmCIPInvArpRespFromNet,
       "atmCIPInvArpReqFromNet": atmCIPInvArpReqFromNet,
       "atmCIPInvArpNakFromNet": atmCIPInvArpNakFromNet,
       "atmCIPPktsToNet": atmCIPPktsToNet,
       "atmCIPPktsToNetDiscard": atmCIPPktsToNetDiscard,
       "atmCIPArpRespToNet": atmCIPArpRespToNet,
       "atmCIPArpReqToNet": atmCIPArpReqToNet,
       "atmCIPInvArpRespToNet": atmCIPInvArpRespToNet,
       "atmCIPInvArpReqToNet": atmCIPInvArpReqToNet,
       "atmCIPInvArpNakToNet": atmCIPInvArpNakToNet,
       "atmxSahiBWGroup": atmxSahiBWGroup,
       "atmxBwgTable": atmxBwgTable,
       "atmxBwgEntry": atmxBwgEntry,
       "atmxBwgSlotIndex": atmxBwgSlotIndex,
       "atmxBwgPortIndex": atmxBwgPortIndex,
       "atmxBwgNum": atmxBwgNum,
       "atmxBwgBE": atmxBwgBE,
       "atmxBwgPcr": atmxBwgPcr,
       "atmxBwgScr": atmxBwgScr,
       "atmxBwgMbs": atmxBwgMbs,
       "atmxBwgOperStatus": atmxBwgOperStatus,
       "atmxBwgServiceTable": atmxBwgServiceTable,
       "atmxBwgServiceEntry": atmxBwgServiceEntry,
       "atmxBwgServiceNum": atmxBwgServiceNum,
       "atmx1483ScaleGroup": atmx1483ScaleGroup,
       "atmGpToVcMappingTable": atmGpToVcMappingTable,
       "atmGpToVcMappingEntry": atmGpToVcMappingEntry,
       "atmxGpToVcSlotIndex": atmxGpToVcSlotIndex,
       "atmxGpToVcPortIndex": atmxGpToVcPortIndex,
       "atmxGpToVcServiceNum": atmxGpToVcServiceNum,
       "atmxGpToVcGroupId": atmxGpToVcGroupId,
       "atmxGpToVcVpi": atmxGpToVcVpi,
       "atmxGpToVcVci": atmxGpToVcVci,
       "atmxGpToVcRowStatus": atmxGpToVcRowStatus,
       "atmGpToVcBulkMappingTable": atmGpToVcBulkMappingTable,
       "atmGpToVcBulkMappingEntry": atmGpToVcBulkMappingEntry,
       "atmxGpToVcBulkSlotIndex": atmxGpToVcBulkSlotIndex,
       "atmxGpToVcBulkPortIndex": atmxGpToVcBulkPortIndex,
       "atmxGpToVcBulkServiceNum": atmxGpToVcBulkServiceNum,
       "atmxGpToVcBulkNumOfNodes": atmxGpToVcBulkNumOfNodes,
       "atmxGpToVcBulkMappingList": atmxGpToVcBulkMappingList,
       "atmxLsmGroup": atmxLsmGroup}
)
