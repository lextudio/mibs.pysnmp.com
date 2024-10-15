# SNMP MIB module (BIANCA-BOX-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BOX-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:19 2024
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


# Types definitions



class Date(Integer32):
    """Custom type Date based on Integer32"""




class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Isdn_ObjectIdentity = ObjectIdentity
isdn = _Isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 2)
)
_IsdnIfTable_Object = MibTable
isdnIfTable = _IsdnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1)
)
if mibBuilder.loadTexts:
    isdnIfTable.setStatus("mandatory")
_IsdnIfEntry_Object = MibTableRow
isdnIfEntry = _IsdnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1)
)
isdnIfEntry.setIndexNames(
    (0, "BIANCA-BOX-ISDN-MIB", "isdnIfIndex"),
)
if mibBuilder.loadTexts:
    isdnIfEntry.setStatus("mandatory")
_IsdnIfIndex_Type = Integer32
_IsdnIfIndex_Object = MibTableColumn
isdnIfIndex = _IsdnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 1),
    _IsdnIfIndex_Type()
)
isdnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnIfIndex.setStatus("mandatory")


class _IsdnIfDescription_Type(DisplayString):
    """Custom type isdnIfDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IsdnIfDescription_Type.__name__ = "DisplayString"
_IsdnIfDescription_Object = MibTableColumn
isdnIfDescription = _IsdnIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 2),
    _IsdnIfDescription_Type()
)
isdnIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnIfDescription.setStatus("mandatory")


class _IsdnIfLayer1State_Type(Integer32):
    """Custom type isdnIfLayer1State based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("f1", 1),
          ("f2", 2),
          ("f3", 3),
          ("f4", 4),
          ("f5", 5),
          ("f6", 6),
          ("f7", 7),
          ("f8", 8),
          ("g1", 9),
          ("g2", 10),
          ("g3", 11),
          ("g4", 12))
    )


_IsdnIfLayer1State_Type.__name__ = "Integer32"
_IsdnIfLayer1State_Object = MibTableColumn
isdnIfLayer1State = _IsdnIfLayer1State_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 3),
    _IsdnIfLayer1State_Type()
)
isdnIfLayer1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnIfLayer1State.setStatus("mandatory")


class _IsdnIfBchannelControl_Type(Integer32):
    """Custom type isdnIfBchannelControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlled", 2),
          ("uncontrolled", 1))
    )


_IsdnIfBchannelControl_Type.__name__ = "Integer32"
_IsdnIfBchannelControl_Object = MibTableColumn
isdnIfBchannelControl = _IsdnIfBchannelControl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 4),
    _IsdnIfBchannelControl_Type()
)
isdnIfBchannelControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnIfBchannelControl.setStatus("mandatory")


class _IsdnIfActivationRequest_Type(Integer32):
    """Custom type isdnIfActivationRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("nooperation", 1))
    )


_IsdnIfActivationRequest_Type.__name__ = "Integer32"
_IsdnIfActivationRequest_Object = MibTableColumn
isdnIfActivationRequest = _IsdnIfActivationRequest_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 5),
    _IsdnIfActivationRequest_Type()
)
isdnIfActivationRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnIfActivationRequest.setStatus("mandatory")


class _IsdnIfMode_Type(Integer32):
    """Custom type isdnIfMode based on Integer32"""
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
        *(("nt", 2),
          ("pabx-terminal", 3),
          ("pabx-tie", 5),
          ("pabx-trunk", 4),
          ("te", 1))
    )


_IsdnIfMode_Type.__name__ = "Integer32"
_IsdnIfMode_Object = MibTableColumn
isdnIfMode = _IsdnIfMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 6),
    _IsdnIfMode_Type()
)
isdnIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnIfMode.setStatus("mandatory")
_IsdnIfTimerT3_Type = Integer32
_IsdnIfTimerT3_Object = MibTableColumn
isdnIfTimerT3 = _IsdnIfTimerT3_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 7),
    _IsdnIfTimerT3_Type()
)
isdnIfTimerT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnIfTimerT3.setStatus("mandatory")


class _IsdnIfUsePowerDetector_Type(Integer32):
    """Custom type isdnIfUsePowerDetector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontuse", 2),
          ("use", 1))
    )


_IsdnIfUsePowerDetector_Type.__name__ = "Integer32"
_IsdnIfUsePowerDetector_Object = MibTableColumn
isdnIfUsePowerDetector = _IsdnIfUsePowerDetector_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 8),
    _IsdnIfUsePowerDetector_Type()
)
isdnIfUsePowerDetector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnIfUsePowerDetector.setStatus("mandatory")


class _IsdnIfNumberOfChannels_Type(Integer32):
    """Custom type isdnIfNumberOfChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IsdnIfNumberOfChannels_Type.__name__ = "Integer32"
_IsdnIfNumberOfChannels_Object = MibTableColumn
isdnIfNumberOfChannels = _IsdnIfNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 9),
    _IsdnIfNumberOfChannels_Type()
)
isdnIfNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnIfNumberOfChannels.setStatus("mandatory")
_IsdnIfTimeouts_Type = Counter32
_IsdnIfTimeouts_Object = MibTableColumn
isdnIfTimeouts = _IsdnIfTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 10),
    _IsdnIfTimeouts_Type()
)
isdnIfTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnIfTimeouts.setStatus("mandatory")
_IsdnIfActivates_Type = Counter32
_IsdnIfActivates_Object = MibTableColumn
isdnIfActivates = _IsdnIfActivates_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 11),
    _IsdnIfActivates_Type()
)
isdnIfActivates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnIfActivates.setStatus("mandatory")
_IsdnIfDeactivates_Type = Counter32
_IsdnIfDeactivates_Object = MibTableColumn
isdnIfDeactivates = _IsdnIfDeactivates_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 12),
    _IsdnIfDeactivates_Type()
)
isdnIfDeactivates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnIfDeactivates.setStatus("mandatory")


class _IsdnIfAutoconfigState_Type(Integer32):
    """Custom type isdnIfAutoconfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 3),
          ("running", 2),
          ("start", 1))
    )


_IsdnIfAutoconfigState_Type.__name__ = "Integer32"
_IsdnIfAutoconfigState_Object = MibTableColumn
isdnIfAutoconfigState = _IsdnIfAutoconfigState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 13),
    _IsdnIfAutoconfigState_Type()
)
isdnIfAutoconfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnIfAutoconfigState.setStatus("mandatory")


class _IsdnIfAutoconfig_Type(Integer32):
    """Custom type isdnIfAutoconfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IsdnIfAutoconfig_Type.__name__ = "Integer32"
_IsdnIfAutoconfig_Object = MibTableColumn
isdnIfAutoconfig = _IsdnIfAutoconfig_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 14),
    _IsdnIfAutoconfig_Type()
)
isdnIfAutoconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnIfAutoconfig.setStatus("mandatory")
_IsdnIfSlips_Type = Counter32
_IsdnIfSlips_Object = MibTableColumn
isdnIfSlips = _IsdnIfSlips_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 1, 1, 21),
    _IsdnIfSlips_Type()
)
isdnIfSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnIfSlips.setStatus("mandatory")
_IsdnChTable_Object = MibTable
isdnChTable = _IsdnChTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2)
)
if mibBuilder.loadTexts:
    isdnChTable.setStatus("mandatory")
_IsdnChEntry_Object = MibTableRow
isdnChEntry = _IsdnChEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1)
)
isdnChEntry.setIndexNames(
    (0, "BIANCA-BOX-ISDN-MIB", "isdnChIsdnIfIndex"),
    (0, "BIANCA-BOX-ISDN-MIB", "isdnChNumber"),
)
if mibBuilder.loadTexts:
    isdnChEntry.setStatus("mandatory")
_IsdnChIsdnIfIndex_Type = Integer32
_IsdnChIsdnIfIndex_Object = MibTableColumn
isdnChIsdnIfIndex = _IsdnChIsdnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 1),
    _IsdnChIsdnIfIndex_Type()
)
isdnChIsdnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChIsdnIfIndex.setStatus("mandatory")
_IsdnChNumber_Type = Integer32
_IsdnChNumber_Object = MibTableColumn
isdnChNumber = _IsdnChNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 2),
    _IsdnChNumber_Type()
)
isdnChNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChNumber.setStatus("mandatory")


class _IsdnChState_Type(Integer32):
    """Custom type isdnChState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("not-connected", 1))
    )


_IsdnChState_Type.__name__ = "Integer32"
_IsdnChState_Object = MibTableColumn
isdnChState = _IsdnChState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 3),
    _IsdnChState_Type()
)
isdnChState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChState.setStatus("mandatory")


class _IsdnChType_Type(Integer32):
    """Custom type isdnChType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dialup", 1),
          ("leased-dce", 3),
          ("leased-dte", 2),
          ("loopback", 6),
          ("not-available", 7))
    )


_IsdnChType_Type.__name__ = "Integer32"
_IsdnChType_Object = MibTableColumn
isdnChType = _IsdnChType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 4),
    _IsdnChType_Type()
)
isdnChType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnChType.setStatus("mandatory")


class _IsdnChBundle_Type(Integer32):
    """Custom type isdnChBundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnChBundle_Type.__name__ = "Integer32"
_IsdnChBundle_Object = MibTableColumn
isdnChBundle = _IsdnChBundle_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 5),
    _IsdnChBundle_Type()
)
isdnChBundle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnChBundle.setStatus("mandatory")
_IsdnChThroughput_Type = Integer32
_IsdnChThroughput_Object = MibTableColumn
isdnChThroughput = _IsdnChThroughput_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 6),
    _IsdnChThroughput_Type()
)
isdnChThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChThroughput.setStatus("mandatory")
_IsdnChReceivedPackets_Type = Counter32
_IsdnChReceivedPackets_Object = MibTableColumn
isdnChReceivedPackets = _IsdnChReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 7),
    _IsdnChReceivedPackets_Type()
)
isdnChReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChReceivedPackets.setStatus("mandatory")
_IsdnChReceivedOctets_Type = Counter32
_IsdnChReceivedOctets_Object = MibTableColumn
isdnChReceivedOctets = _IsdnChReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 8),
    _IsdnChReceivedOctets_Type()
)
isdnChReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChReceivedOctets.setStatus("mandatory")
_IsdnChReceivedErrors_Type = Counter32
_IsdnChReceivedErrors_Object = MibTableColumn
isdnChReceivedErrors = _IsdnChReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 9),
    _IsdnChReceivedErrors_Type()
)
isdnChReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChReceivedErrors.setStatus("mandatory")
_IsdnChTransmitPackets_Type = Counter32
_IsdnChTransmitPackets_Object = MibTableColumn
isdnChTransmitPackets = _IsdnChTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 10),
    _IsdnChTransmitPackets_Type()
)
isdnChTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChTransmitPackets.setStatus("mandatory")
_IsdnChTransmitOctets_Type = Counter32
_IsdnChTransmitOctets_Object = MibTableColumn
isdnChTransmitOctets = _IsdnChTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 11),
    _IsdnChTransmitOctets_Type()
)
isdnChTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChTransmitOctets.setStatus("mandatory")
_IsdnChTransmitErrors_Type = Counter32
_IsdnChTransmitErrors_Object = MibTableColumn
isdnChTransmitErrors = _IsdnChTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 2, 1, 12),
    _IsdnChTransmitErrors_Type()
)
isdnChTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChTransmitErrors.setStatus("mandatory")
_IsdnStkTable_Object = MibTable
isdnStkTable = _IsdnStkTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3)
)
if mibBuilder.loadTexts:
    isdnStkTable.setStatus("mandatory")
_IsdnStkEntry_Object = MibTableRow
isdnStkEntry = _IsdnStkEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1)
)
isdnStkEntry.setIndexNames(
    (0, "BIANCA-BOX-ISDN-MIB", "isdnStkNumber"),
)
if mibBuilder.loadTexts:
    isdnStkEntry.setStatus("mandatory")


class _IsdnStkNumber_Type(Integer32):
    """Custom type isdnStkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IsdnStkNumber_Type.__name__ = "Integer32"
_IsdnStkNumber_Object = MibTableColumn
isdnStkNumber = _IsdnStkNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 1),
    _IsdnStkNumber_Type()
)
isdnStkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnStkNumber.setStatus("mandatory")
_IsdnStkIsdnIfIndex_Type = Integer32
_IsdnStkIsdnIfIndex_Object = MibTableColumn
isdnStkIsdnIfIndex = _IsdnStkIsdnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 3),
    _IsdnStkIsdnIfIndex_Type()
)
isdnStkIsdnIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnStkIsdnIfIndex.setStatus("mandatory")


class _IsdnStkProtocolProfile_Type(Integer32):
    """Custom type isdnStkProtocolProfile based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("d1tr6", 3),
          ("delete", 1),
          ("dms100", 8),
          ("dss1", 4),
          ("ess5", 7),
          ("ins64", 9),
          ("ni1", 5),
          ("not-used", 6),
          ("permanent", 2))
    )


_IsdnStkProtocolProfile_Type.__name__ = "Integer32"
_IsdnStkProtocolProfile_Object = MibTableColumn
isdnStkProtocolProfile = _IsdnStkProtocolProfile_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 4),
    _IsdnStkProtocolProfile_Type()
)
isdnStkProtocolProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnStkProtocolProfile.setStatus("mandatory")


class _IsdnStkConfiguration_Type(Integer32):
    """Custom type isdnStkConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("point-to-multipoint", 1),
          ("point-to-point", 2))
    )


_IsdnStkConfiguration_Type.__name__ = "Integer32"
_IsdnStkConfiguration_Object = MibTableColumn
isdnStkConfiguration = _IsdnStkConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 5),
    _IsdnStkConfiguration_Type()
)
isdnStkConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnStkConfiguration.setStatus("mandatory")
_IsdnStkSPID_Type = DisplayString
_IsdnStkSPID_Object = MibTableColumn
isdnStkSPID = _IsdnStkSPID_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 6),
    _IsdnStkSPID_Type()
)
isdnStkSPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnStkSPID.setStatus("mandatory")


class _IsdnStkTeiProc_Type(Integer32):
    """Custom type isdnStkTeiProc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_IsdnStkTeiProc_Type.__name__ = "Integer32"
_IsdnStkTeiProc_Object = MibTableColumn
isdnStkTeiProc = _IsdnStkTeiProc_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 7),
    _IsdnStkTeiProc_Type()
)
isdnStkTeiProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnStkTeiProc.setStatus("mandatory")


class _IsdnStkTeiValue_Type(Integer32):
    """Custom type isdnStkTeiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 126),
    )


_IsdnStkTeiValue_Type.__name__ = "Integer32"
_IsdnStkTeiValue_Object = MibTableColumn
isdnStkTeiValue = _IsdnStkTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 8),
    _IsdnStkTeiValue_Type()
)
isdnStkTeiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnStkTeiValue.setStatus("mandatory")


class _IsdnStkClearAllCalls_Type(Integer32):
    """Custom type isdnStkClearAllCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("no-operation", 1))
    )


_IsdnStkClearAllCalls_Type.__name__ = "Integer32"
_IsdnStkClearAllCalls_Object = MibTableColumn
isdnStkClearAllCalls = _IsdnStkClearAllCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 22),
    _IsdnStkClearAllCalls_Type()
)
isdnStkClearAllCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnStkClearAllCalls.setStatus("mandatory")


class _IsdnStkStatus_Type(Integer32):
    """Custom type isdnStkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("not-loaded", 2))
    )


_IsdnStkStatus_Type.__name__ = "Integer32"
_IsdnStkStatus_Object = MibTableColumn
isdnStkStatus = _IsdnStkStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 23),
    _IsdnStkStatus_Type()
)
isdnStkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnStkStatus.setStatus("mandatory")


class _IsdnStkLayer2State_Type(Integer32):
    """Custom type isdnStkLayer2State based on Integer32"""
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
        *(("aw-est", 3),
          ("established", 4),
          ("tei-assigned", 2),
          ("tei-unassigned", 1))
    )


_IsdnStkLayer2State_Type.__name__ = "Integer32"
_IsdnStkLayer2State_Object = MibTableColumn
isdnStkLayer2State = _IsdnStkLayer2State_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 24),
    _IsdnStkLayer2State_Type()
)
isdnStkLayer2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnStkLayer2State.setStatus("mandatory")


class _IsdnStkBchannels_Type(Integer32):
    """Custom type isdnStkBchannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IsdnStkBchannels_Type.__name__ = "Integer32"
_IsdnStkBchannels_Object = MibTableColumn
isdnStkBchannels = _IsdnStkBchannels_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 25),
    _IsdnStkBchannels_Type()
)
isdnStkBchannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnStkBchannels.setStatus("mandatory")
_IsdnStkDialOutPrefix_Type = DisplayString
_IsdnStkDialOutPrefix_Object = MibTableColumn
isdnStkDialOutPrefix = _IsdnStkDialOutPrefix_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 3, 1, 26),
    _IsdnStkDialOutPrefix_Type()
)
isdnStkDialOutPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnStkDialOutPrefix.setStatus("mandatory")
_IsdnCallTable_Object = MibTable
isdnCallTable = _IsdnCallTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4)
)
if mibBuilder.loadTexts:
    isdnCallTable.setStatus("mandatory")
_IsdnCallEntry_Object = MibTableRow
isdnCallEntry = _IsdnCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1)
)
isdnCallEntry.setIndexNames(
    (0, "BIANCA-BOX-ISDN-MIB", "isdnCallStkNumber"),
    (0, "BIANCA-BOX-ISDN-MIB", "isdnCallType"),
    (0, "BIANCA-BOX-ISDN-MIB", "isdnCallReference"),
)
if mibBuilder.loadTexts:
    isdnCallEntry.setStatus("mandatory")


class _IsdnCallStkNumber_Type(Integer32):
    """Custom type isdnCallStkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IsdnCallStkNumber_Type.__name__ = "Integer32"
_IsdnCallStkNumber_Object = MibTableColumn
isdnCallStkNumber = _IsdnCallStkNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 1),
    _IsdnCallStkNumber_Type()
)
isdnCallStkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallStkNumber.setStatus("mandatory")


class _IsdnCallType_Type(Integer32):
    """Custom type isdnCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_IsdnCallType_Type.__name__ = "Integer32"
_IsdnCallType_Object = MibTableColumn
isdnCallType = _IsdnCallType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 2),
    _IsdnCallType_Type()
)
isdnCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallType.setStatus("mandatory")
_IsdnCallReference_Type = Integer32
_IsdnCallReference_Object = MibTableColumn
isdnCallReference = _IsdnCallReference_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 3),
    _IsdnCallReference_Type()
)
isdnCallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallReference.setStatus("mandatory")
_IsdnCallAge_Type = TimeTicks
_IsdnCallAge_Object = MibTableColumn
isdnCallAge = _IsdnCallAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 4),
    _IsdnCallAge_Type()
)
isdnCallAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallAge.setStatus("mandatory")


class _IsdnCallState_Type(Integer32):
    """Custom type isdnCallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              10,
              11,
              12,
              13,
              16,
              18,
              26)
        )
    )
    namedValues = NamedValues(
        *(("active", 11),
          ("c-deliverd", 5),
          ("c-initiated", 2),
          ("c-present", 7),
          ("c-recvd", 8),
          ("discon-ind", 13),
          ("discon-req", 12),
          ("ic-procd", 10),
          ("null", 1),
          ("oc-procd", 4),
          ("ovl-recv", 26),
          ("ovl-send", 3),
          ("resum-req", 18),
          ("suspd-req", 16))
    )


_IsdnCallState_Type.__name__ = "Integer32"
_IsdnCallState_Object = MibTableColumn
isdnCallState = _IsdnCallState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 5),
    _IsdnCallState_Type()
)
isdnCallState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCallState.setStatus("mandatory")
_IsdnCallIsdnIfIndex_Type = Integer32
_IsdnCallIsdnIfIndex_Object = MibTableColumn
isdnCallIsdnIfIndex = _IsdnCallIsdnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 6),
    _IsdnCallIsdnIfIndex_Type()
)
isdnCallIsdnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallIsdnIfIndex.setStatus("mandatory")


class _IsdnCallChannel_Type(Integer32):
    """Custom type isdnCallChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IsdnCallChannel_Type.__name__ = "Integer32"
_IsdnCallChannel_Object = MibTableColumn
isdnCallChannel = _IsdnCallChannel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 7),
    _IsdnCallChannel_Type()
)
isdnCallChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallChannel.setStatus("mandatory")


class _IsdnCallDspItem_Type(Integer32):
    """Custom type isdnCallDspItem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58)
        )
    )
    namedValues = NamedValues(
        *(("eaz0", 48),
          ("eaz1", 49),
          ("eaz2", 50),
          ("eaz3", 51),
          ("eaz4", 52),
          ("eaz5", 53),
          ("eaz6", 54),
          ("eaz7", 55),
          ("eaz8", 56),
          ("eaz9", 57),
          ("extern", 24),
          ("login", 2),
          ("pots", 25),
          ("ppp", 1),
          ("ppp-56k", 12),
          ("ppp-64k", 11),
          ("ppp-dovb", 14),
          ("ppp-modem", 13),
          ("ppp-modem-profile-1", 26),
          ("ppp-modem-profile-2", 27),
          ("ppp-modem-profile-3", 28),
          ("ppp-modem-profile-4", 29),
          ("ppp-modem-profile-5", 30),
          ("ppp-modem-profile-6", 31),
          ("ppp-modem-profile-7", 32),
          ("ppp-modem-profile-8", 33),
          ("ppp-v110-1200", 15),
          ("ppp-v110-14400", 19),
          ("ppp-v110-19200", 20),
          ("ppp-v110-2400", 16),
          ("ppp-v110-38400", 21),
          ("ppp-v110-4800", 17),
          ("ppp-v110-9600", 18),
          ("ppp-x75", 22),
          ("undefined", 10),
          ("x25-pad", 58))
    )


_IsdnCallDspItem_Type.__name__ = "Integer32"
_IsdnCallDspItem_Object = MibTableColumn
isdnCallDspItem = _IsdnCallDspItem_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 8),
    _IsdnCallDspItem_Type()
)
isdnCallDspItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallDspItem.setStatus("mandatory")
_IsdnCallRemoteNumber_Type = DisplayString
_IsdnCallRemoteNumber_Object = MibTableColumn
isdnCallRemoteNumber = _IsdnCallRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 9),
    _IsdnCallRemoteNumber_Type()
)
isdnCallRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallRemoteNumber.setStatus("mandatory")
_IsdnCallRemoteSubaddress_Type = OctetString
_IsdnCallRemoteSubaddress_Object = MibTableColumn
isdnCallRemoteSubaddress = _IsdnCallRemoteSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 10),
    _IsdnCallRemoteSubaddress_Type()
)
isdnCallRemoteSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallRemoteSubaddress.setStatus("mandatory")
_IsdnCallLocalNumber_Type = DisplayString
_IsdnCallLocalNumber_Object = MibTableColumn
isdnCallLocalNumber = _IsdnCallLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 11),
    _IsdnCallLocalNumber_Type()
)
isdnCallLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallLocalNumber.setStatus("mandatory")
_IsdnCallLocalSubaddress_Type = OctetString
_IsdnCallLocalSubaddress_Object = MibTableColumn
isdnCallLocalSubaddress = _IsdnCallLocalSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 12),
    _IsdnCallLocalSubaddress_Type()
)
isdnCallLocalSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallLocalSubaddress.setStatus("mandatory")


class _IsdnCallServiceIndicator_Type(Integer32):
    """Custom type isdnCallServiceIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ab-services", 2),
          ("btx", 5),
          ("data-transfer", 7),
          ("facsimile64", 9),
          ("fax-group4", 4),
          ("graphics-phone", 14),
          ("mixed-mode", 10),
          ("telecontrol", 13),
          ("telephony", 1),
          ("teletex", 15),
          ("video-phone", 16),
          ("x21-services", 3),
          ("x25-services", 8))
    )


_IsdnCallServiceIndicator_Type.__name__ = "Integer32"
_IsdnCallServiceIndicator_Object = MibTableColumn
isdnCallServiceIndicator = _IsdnCallServiceIndicator_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 13),
    _IsdnCallServiceIndicator_Type()
)
isdnCallServiceIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallServiceIndicator.setStatus("mandatory")


class _IsdnCallAddInfo_Type(Integer32):
    """Custom type isdnCallAddInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnCallAddInfo_Type.__name__ = "Integer32"
_IsdnCallAddInfo_Object = MibTableColumn
isdnCallAddInfo = _IsdnCallAddInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 14),
    _IsdnCallAddInfo_Type()
)
isdnCallAddInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallAddInfo.setStatus("mandatory")
_IsdnCallBC_Type = OctetString
_IsdnCallBC_Object = MibTableColumn
isdnCallBC = _IsdnCallBC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 15),
    _IsdnCallBC_Type()
)
isdnCallBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallBC.setStatus("mandatory")
_IsdnCallLLC_Type = OctetString
_IsdnCallLLC_Object = MibTableColumn
isdnCallLLC = _IsdnCallLLC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 16),
    _IsdnCallLLC_Type()
)
isdnCallLLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallLLC.setStatus("mandatory")
_IsdnCallHLC_Type = OctetString
_IsdnCallHLC_Object = MibTableColumn
isdnCallHLC = _IsdnCallHLC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 17),
    _IsdnCallHLC_Type()
)
isdnCallHLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHLC.setStatus("mandatory")
_IsdnCallCharge_Type = Integer32
_IsdnCallCharge_Object = MibTableColumn
isdnCallCharge = _IsdnCallCharge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 18),
    _IsdnCallCharge_Type()
)
isdnCallCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCharge.setStatus("mandatory")
_IsdnCallReceivedPackets_Type = Counter32
_IsdnCallReceivedPackets_Object = MibTableColumn
isdnCallReceivedPackets = _IsdnCallReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 19),
    _IsdnCallReceivedPackets_Type()
)
isdnCallReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallReceivedPackets.setStatus("mandatory")
_IsdnCallReceivedOctets_Type = Counter32
_IsdnCallReceivedOctets_Object = MibTableColumn
isdnCallReceivedOctets = _IsdnCallReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 20),
    _IsdnCallReceivedOctets_Type()
)
isdnCallReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallReceivedOctets.setStatus("mandatory")
_IsdnCallReceivedErrors_Type = Counter32
_IsdnCallReceivedErrors_Object = MibTableColumn
isdnCallReceivedErrors = _IsdnCallReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 21),
    _IsdnCallReceivedErrors_Type()
)
isdnCallReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallReceivedErrors.setStatus("mandatory")
_IsdnCallTransmitPackets_Type = Counter32
_IsdnCallTransmitPackets_Object = MibTableColumn
isdnCallTransmitPackets = _IsdnCallTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 22),
    _IsdnCallTransmitPackets_Type()
)
isdnCallTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallTransmitPackets.setStatus("mandatory")
_IsdnCallTransmitOctets_Type = Counter32
_IsdnCallTransmitOctets_Object = MibTableColumn
isdnCallTransmitOctets = _IsdnCallTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 23),
    _IsdnCallTransmitOctets_Type()
)
isdnCallTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallTransmitOctets.setStatus("mandatory")
_IsdnCallTransmitErrors_Type = Counter32
_IsdnCallTransmitErrors_Object = MibTableColumn
isdnCallTransmitErrors = _IsdnCallTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 24),
    _IsdnCallTransmitErrors_Type()
)
isdnCallTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallTransmitErrors.setStatus("mandatory")
_IsdnCallChargeInfo_Type = DisplayString
_IsdnCallChargeInfo_Object = MibTableColumn
isdnCallChargeInfo = _IsdnCallChargeInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 25),
    _IsdnCallChargeInfo_Type()
)
isdnCallChargeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallChargeInfo.setStatus("mandatory")


class _IsdnCallScreening_Type(Integer32):
    """Custom type isdnCallScreening based on Integer32"""
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
        *(("network", 4),
          ("undefined", 5),
          ("user", 1),
          ("user-failed", 3),
          ("user-verified", 2))
    )


_IsdnCallScreening_Type.__name__ = "Integer32"
_IsdnCallScreening_Object = MibTableColumn
isdnCallScreening = _IsdnCallScreening_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 26),
    _IsdnCallScreening_Type()
)
isdnCallScreening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallScreening.setStatus("mandatory")
_IsdnCallInfo_Type = DisplayString
_IsdnCallInfo_Object = MibTableColumn
isdnCallInfo = _IsdnCallInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 4, 1, 27),
    _IsdnCallInfo_Type()
)
isdnCallInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallInfo.setStatus("mandatory")
_IsdnDispatchTable_Object = MibTable
isdnDispatchTable = _IsdnDispatchTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5)
)
if mibBuilder.loadTexts:
    isdnDispatchTable.setStatus("mandatory")
_IsdnDispatchEntry_Object = MibTableRow
isdnDispatchEntry = _IsdnDispatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1)
)
isdnDispatchEntry.setIndexNames(
    (0, "BIANCA-BOX-ISDN-MIB", "isdnDspStkNumber"),
    (0, "BIANCA-BOX-ISDN-MIB", "isdnDspItem"),
)
if mibBuilder.loadTexts:
    isdnDispatchEntry.setStatus("mandatory")


class _IsdnDspStkNumber_Type(Integer32):
    """Custom type isdnDspStkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_IsdnDspStkNumber_Type.__name__ = "Integer32"
_IsdnDspStkNumber_Object = MibTableColumn
isdnDspStkNumber = _IsdnDspStkNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1, 1),
    _IsdnDspStkNumber_Type()
)
isdnDspStkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDspStkNumber.setStatus("mandatory")


class _IsdnDspItem_Type(Integer32):
    """Custom type isdnDspItem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("capi2", 59),
          ("delete", 10),
          ("eaz0", 48),
          ("eaz1", 49),
          ("eaz2", 50),
          ("eaz3", 51),
          ("eaz4", 52),
          ("eaz5", 53),
          ("eaz6", 54),
          ("eaz7", 55),
          ("eaz8", 56),
          ("eaz9", 57),
          ("extern", 24),
          ("login", 2),
          ("pots", 25),
          ("ppp", 1),
          ("ppp-56k", 12),
          ("ppp-64k", 11),
          ("ppp-dovb", 14),
          ("ppp-modem", 13),
          ("ppp-modem-profile-1", 26),
          ("ppp-modem-profile-2", 27),
          ("ppp-modem-profile-3", 28),
          ("ppp-modem-profile-4", 29),
          ("ppp-modem-profile-5", 30),
          ("ppp-modem-profile-6", 31),
          ("ppp-modem-profile-7", 32),
          ("ppp-modem-profile-8", 33),
          ("ppp-v110-1200", 15),
          ("ppp-v110-14400", 19),
          ("ppp-v110-19200", 20),
          ("ppp-v110-2400", 16),
          ("ppp-v110-38400", 21),
          ("ppp-v110-4800", 17),
          ("ppp-v110-9600", 18),
          ("ppp-x75", 22),
          ("x25-pad", 58))
    )


_IsdnDspItem_Type.__name__ = "Integer32"
_IsdnDspItem_Object = MibTableColumn
isdnDspItem = _IsdnDspItem_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1, 2),
    _IsdnDspItem_Type()
)
isdnDspItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDspItem.setStatus("mandatory")
_IsdnDspLocalNumber_Type = DisplayString
_IsdnDspLocalNumber_Object = MibTableColumn
isdnDspLocalNumber = _IsdnDspLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1, 3),
    _IsdnDspLocalNumber_Type()
)
isdnDspLocalNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDspLocalNumber.setStatus("mandatory")
_IsdnDspLocalSubaddress_Type = OctetString
_IsdnDspLocalSubaddress_Object = MibTableColumn
isdnDspLocalSubaddress = _IsdnDspLocalSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1, 4),
    _IsdnDspLocalSubaddress_Type()
)
isdnDspLocalSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDspLocalSubaddress.setStatus("mandatory")


class _IsdnDspBearer_Type(Integer32):
    """Custom type isdnDspBearer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("data", 2),
          ("voice", 3))
    )


_IsdnDspBearer_Type.__name__ = "Integer32"
_IsdnDspBearer_Object = MibTableColumn
isdnDspBearer = _IsdnDspBearer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1, 5),
    _IsdnDspBearer_Type()
)
isdnDspBearer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDspBearer.setStatus("mandatory")


class _IsdnDspSlot_Type(Integer32):
    """Custom type isdnDspSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IsdnDspSlot_Type.__name__ = "Integer32"
_IsdnDspSlot_Object = MibTableColumn
isdnDspSlot = _IsdnDspSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1, 6),
    _IsdnDspSlot_Type()
)
isdnDspSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDspSlot.setStatus("mandatory")


class _IsdnDspUnit_Type(Integer32):
    """Custom type isdnDspUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IsdnDspUnit_Type.__name__ = "Integer32"
_IsdnDspUnit_Object = MibTableColumn
isdnDspUnit = _IsdnDspUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1, 7),
    _IsdnDspUnit_Type()
)
isdnDspUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDspUnit.setStatus("mandatory")


class _IsdnDspDirection_Type(Integer32):
    """Custom type isdnDspDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("incoming", 1),
          ("outgoing", 2))
    )


_IsdnDspDirection_Type.__name__ = "Integer32"
_IsdnDspDirection_Object = MibTableColumn
isdnDspDirection = _IsdnDspDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1, 8),
    _IsdnDspDirection_Type()
)
isdnDspDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDspDirection.setStatus("mandatory")


class _IsdnDspMode_Type(Integer32):
    """Custom type isdnDspMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("left-to-right", 2),
          ("right-to-left", 1))
    )


_IsdnDspMode_Type.__name__ = "Integer32"
_IsdnDspMode_Object = MibTableColumn
isdnDspMode = _IsdnDspMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1, 9),
    _IsdnDspMode_Type()
)
isdnDspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDspMode.setStatus("mandatory")


class _IsdnDspUserName_Type(DisplayString):
    """Custom type isdnDspUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IsdnDspUserName_Type.__name__ = "DisplayString"
_IsdnDspUserName_Object = MibTableColumn
isdnDspUserName = _IsdnDspUserName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 5, 1, 10),
    _IsdnDspUserName_Type()
)
isdnDspUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDspUserName.setStatus("mandatory")
_IsdnDChanX31Table_Object = MibTable
isdnDChanX31Table = _IsdnDChanX31Table_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 6)
)
if mibBuilder.loadTexts:
    isdnDChanX31Table.setStatus("mandatory")
_IsdnDChanX31Entry_Object = MibTableRow
isdnDChanX31Entry = _IsdnDChanX31Entry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 6, 1)
)
isdnDChanX31Entry.setIndexNames(
    (0, "BIANCA-BOX-ISDN-MIB", "isdnX31IsdnIfIndex"),
)
if mibBuilder.loadTexts:
    isdnDChanX31Entry.setStatus("mandatory")
_IsdnX31IsdnIfIndex_Type = Integer32
_IsdnX31IsdnIfIndex_Object = MibTableColumn
isdnX31IsdnIfIndex = _IsdnX31IsdnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 6, 1, 1),
    _IsdnX31IsdnIfIndex_Type()
)
isdnX31IsdnIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnX31IsdnIfIndex.setStatus("mandatory")


class _IsdnX31TeiProc_Type(Integer32):
    """Custom type isdnX31TeiProc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_IsdnX31TeiProc_Type.__name__ = "Integer32"
_IsdnX31TeiProc_Object = MibTableColumn
isdnX31TeiProc = _IsdnX31TeiProc_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 6, 1, 2),
    _IsdnX31TeiProc_Type()
)
isdnX31TeiProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnX31TeiProc.setStatus("mandatory")


class _IsdnX31TeiValue_Type(Integer32):
    """Custom type isdnX31TeiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 126),
    )


_IsdnX31TeiValue_Type.__name__ = "Integer32"
_IsdnX31TeiValue_Object = MibTableColumn
isdnX31TeiValue = _IsdnX31TeiValue_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 6, 1, 3),
    _IsdnX31TeiValue_Type()
)
isdnX31TeiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnX31TeiValue.setStatus("mandatory")


class _IsdnX31AssignedTo_Type(Integer32):
    """Custom type isdnX31AssignedTo based on Integer32"""
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
        *(("capi", 3),
          ("capi-default", 2),
          ("delete", 4),
          ("packet-switch", 1))
    )


_IsdnX31AssignedTo_Type.__name__ = "Integer32"
_IsdnX31AssignedTo_Object = MibTableColumn
isdnX31AssignedTo = _IsdnX31AssignedTo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 6, 1, 5),
    _IsdnX31AssignedTo_Type()
)
isdnX31AssignedTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnX31AssignedTo.setStatus("mandatory")


class _IsdnAccountingTemplate_Type(DisplayString):
    """Custom type isdnAccountingTemplate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IsdnAccountingTemplate_Type.__name__ = "DisplayString"
_IsdnAccountingTemplate_Object = MibScalar
isdnAccountingTemplate = _IsdnAccountingTemplate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 7),
    _IsdnAccountingTemplate_Type()
)
isdnAccountingTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnAccountingTemplate.setStatus("mandatory")
_IsdnCallHistoryTable_Object = MibTable
isdnCallHistoryTable = _IsdnCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8)
)
if mibBuilder.loadTexts:
    isdnCallHistoryTable.setStatus("mandatory")
_IsdnCallHistoryEntry_Object = MibTableRow
isdnCallHistoryEntry = _IsdnCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1)
)
isdnCallHistoryEntry.setIndexNames(
    (0, "BIANCA-BOX-ISDN-MIB", "isdnCallHistoryStkNumber"),
    (0, "BIANCA-BOX-ISDN-MIB", "isdnCallHistoryType"),
)
if mibBuilder.loadTexts:
    isdnCallHistoryEntry.setStatus("mandatory")


class _IsdnCallHistoryStkNumber_Type(Integer32):
    """Custom type isdnCallHistoryStkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IsdnCallHistoryStkNumber_Type.__name__ = "Integer32"
_IsdnCallHistoryStkNumber_Object = MibTableColumn
isdnCallHistoryStkNumber = _IsdnCallHistoryStkNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 1),
    _IsdnCallHistoryStkNumber_Type()
)
isdnCallHistoryStkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryStkNumber.setStatus("mandatory")


class _IsdnCallHistoryType_Type(Integer32):
    """Custom type isdnCallHistoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_IsdnCallHistoryType_Type.__name__ = "Integer32"
_IsdnCallHistoryType_Object = MibTableColumn
isdnCallHistoryType = _IsdnCallHistoryType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 2),
    _IsdnCallHistoryType_Type()
)
isdnCallHistoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryType.setStatus("mandatory")
_IsdnCallHistoryTime_Type = Date
_IsdnCallHistoryTime_Object = MibTableColumn
isdnCallHistoryTime = _IsdnCallHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 3),
    _IsdnCallHistoryTime_Type()
)
isdnCallHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryTime.setStatus("mandatory")
_IsdnCallHistoryDuration_Type = Integer32
_IsdnCallHistoryDuration_Object = MibTableColumn
isdnCallHistoryDuration = _IsdnCallHistoryDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 4),
    _IsdnCallHistoryDuration_Type()
)
isdnCallHistoryDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryDuration.setStatus("mandatory")
_IsdnCallHistoryIsdnIfIndex_Type = Integer32
_IsdnCallHistoryIsdnIfIndex_Object = MibTableColumn
isdnCallHistoryIsdnIfIndex = _IsdnCallHistoryIsdnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 5),
    _IsdnCallHistoryIsdnIfIndex_Type()
)
isdnCallHistoryIsdnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryIsdnIfIndex.setStatus("mandatory")


class _IsdnCallHistoryChannel_Type(Integer32):
    """Custom type isdnCallHistoryChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IsdnCallHistoryChannel_Type.__name__ = "Integer32"
_IsdnCallHistoryChannel_Object = MibTableColumn
isdnCallHistoryChannel = _IsdnCallHistoryChannel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 6),
    _IsdnCallHistoryChannel_Type()
)
isdnCallHistoryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryChannel.setStatus("mandatory")


class _IsdnCallHistoryDspItem_Type(Integer32):
    """Custom type isdnCallHistoryDspItem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58)
        )
    )
    namedValues = NamedValues(
        *(("eaz0", 48),
          ("eaz1", 49),
          ("eaz2", 50),
          ("eaz3", 51),
          ("eaz4", 52),
          ("eaz5", 53),
          ("eaz6", 54),
          ("eaz7", 55),
          ("eaz8", 56),
          ("eaz9", 57),
          ("extern", 24),
          ("login", 2),
          ("pots", 25),
          ("ppp", 1),
          ("ppp-56k", 12),
          ("ppp-64k", 11),
          ("ppp-dovb", 14),
          ("ppp-modem", 13),
          ("ppp-modem-profile-1", 26),
          ("ppp-modem-profile-2", 27),
          ("ppp-modem-profile-3", 28),
          ("ppp-modem-profile-4", 29),
          ("ppp-modem-profile-5", 30),
          ("ppp-modem-profile-6", 31),
          ("ppp-modem-profile-7", 32),
          ("ppp-modem-profile-8", 33),
          ("ppp-v110-1200", 15),
          ("ppp-v110-14400", 19),
          ("ppp-v110-19200", 20),
          ("ppp-v110-2400", 16),
          ("ppp-v110-38400", 21),
          ("ppp-v110-4800", 17),
          ("ppp-v110-9600", 18),
          ("ppp-x75", 22),
          ("undefined", 10),
          ("x25-pad", 58))
    )


_IsdnCallHistoryDspItem_Type.__name__ = "Integer32"
_IsdnCallHistoryDspItem_Object = MibTableColumn
isdnCallHistoryDspItem = _IsdnCallHistoryDspItem_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 7),
    _IsdnCallHistoryDspItem_Type()
)
isdnCallHistoryDspItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryDspItem.setStatus("mandatory")
_IsdnCallHistoryRemoteNumber_Type = DisplayString
_IsdnCallHistoryRemoteNumber_Object = MibTableColumn
isdnCallHistoryRemoteNumber = _IsdnCallHistoryRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 8),
    _IsdnCallHistoryRemoteNumber_Type()
)
isdnCallHistoryRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryRemoteNumber.setStatus("mandatory")
_IsdnCallHistoryRemoteSubaddress_Type = OctetString
_IsdnCallHistoryRemoteSubaddress_Object = MibTableColumn
isdnCallHistoryRemoteSubaddress = _IsdnCallHistoryRemoteSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 9),
    _IsdnCallHistoryRemoteSubaddress_Type()
)
isdnCallHistoryRemoteSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryRemoteSubaddress.setStatus("mandatory")
_IsdnCallHistoryLocalNumber_Type = DisplayString
_IsdnCallHistoryLocalNumber_Object = MibTableColumn
isdnCallHistoryLocalNumber = _IsdnCallHistoryLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 10),
    _IsdnCallHistoryLocalNumber_Type()
)
isdnCallHistoryLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryLocalNumber.setStatus("mandatory")
_IsdnCallHistoryLocalSubaddress_Type = OctetString
_IsdnCallHistoryLocalSubaddress_Object = MibTableColumn
isdnCallHistoryLocalSubaddress = _IsdnCallHistoryLocalSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 11),
    _IsdnCallHistoryLocalSubaddress_Type()
)
isdnCallHistoryLocalSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryLocalSubaddress.setStatus("mandatory")


class _IsdnCallHistoryServiceIndicator_Type(Integer32):
    """Custom type isdnCallHistoryServiceIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ab-services", 2),
          ("btx", 5),
          ("data-transfer", 7),
          ("facsimile64", 9),
          ("fax-group4", 4),
          ("graphics-phone", 14),
          ("mixed-mode", 10),
          ("telecontrol", 13),
          ("telephony", 1),
          ("teletex", 15),
          ("video-phone", 16),
          ("x21-services", 3),
          ("x25-services", 8))
    )


_IsdnCallHistoryServiceIndicator_Type.__name__ = "Integer32"
_IsdnCallHistoryServiceIndicator_Object = MibTableColumn
isdnCallHistoryServiceIndicator = _IsdnCallHistoryServiceIndicator_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 12),
    _IsdnCallHistoryServiceIndicator_Type()
)
isdnCallHistoryServiceIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryServiceIndicator.setStatus("mandatory")


class _IsdnCallHistoryAddInfo_Type(Integer32):
    """Custom type isdnCallHistoryAddInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnCallHistoryAddInfo_Type.__name__ = "Integer32"
_IsdnCallHistoryAddInfo_Object = MibTableColumn
isdnCallHistoryAddInfo = _IsdnCallHistoryAddInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 13),
    _IsdnCallHistoryAddInfo_Type()
)
isdnCallHistoryAddInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryAddInfo.setStatus("mandatory")
_IsdnCallHistoryBC_Type = OctetString
_IsdnCallHistoryBC_Object = MibTableColumn
isdnCallHistoryBC = _IsdnCallHistoryBC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 14),
    _IsdnCallHistoryBC_Type()
)
isdnCallHistoryBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryBC.setStatus("mandatory")
_IsdnCallHistoryLLC_Type = OctetString
_IsdnCallHistoryLLC_Object = MibTableColumn
isdnCallHistoryLLC = _IsdnCallHistoryLLC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 15),
    _IsdnCallHistoryLLC_Type()
)
isdnCallHistoryLLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryLLC.setStatus("mandatory")
_IsdnCallHistoryHLC_Type = OctetString
_IsdnCallHistoryHLC_Object = MibTableColumn
isdnCallHistoryHLC = _IsdnCallHistoryHLC_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 16),
    _IsdnCallHistoryHLC_Type()
)
isdnCallHistoryHLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryHLC.setStatus("mandatory")
_IsdnCallHistoryCharge_Type = Integer32
_IsdnCallHistoryCharge_Object = MibTableColumn
isdnCallHistoryCharge = _IsdnCallHistoryCharge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 17),
    _IsdnCallHistoryCharge_Type()
)
isdnCallHistoryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryCharge.setStatus("mandatory")
_IsdnCallHistoryDSS1Cause_Type = HexValue
_IsdnCallHistoryDSS1Cause_Object = MibTableColumn
isdnCallHistoryDSS1Cause = _IsdnCallHistoryDSS1Cause_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 18),
    _IsdnCallHistoryDSS1Cause_Type()
)
isdnCallHistoryDSS1Cause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryDSS1Cause.setStatus("mandatory")
_IsdnCallHistory1TR6Cause_Type = HexValue
_IsdnCallHistory1TR6Cause_Object = MibTableColumn
isdnCallHistory1TR6Cause = _IsdnCallHistory1TR6Cause_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 19),
    _IsdnCallHistory1TR6Cause_Type()
)
isdnCallHistory1TR6Cause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistory1TR6Cause.setStatus("mandatory")


class _IsdnCallHistoryLocalCause_Type(Integer32):
    """Custom type isdnCallHistoryLocalCause based on Integer32"""
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
        *(("busy", 10),
          ("chanbusy", 11),
          ("iemissing", 3),
          ("ienotallowed", 4),
          ("l1error", 15),
          ("l3error", 14),
          ("l3restart", 13),
          ("l3timer", 12),
          ("look", 5),
          ("nocallref", 7),
          ("nocontrl", 16),
          ("nolink", 6),
          ("nomem", 8),
          ("notready", 9),
          ("outstate", 2),
          ("unknownprim", 1))
    )


_IsdnCallHistoryLocalCause_Type.__name__ = "Integer32"
_IsdnCallHistoryLocalCause_Object = MibTableColumn
isdnCallHistoryLocalCause = _IsdnCallHistoryLocalCause_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 20),
    _IsdnCallHistoryLocalCause_Type()
)
isdnCallHistoryLocalCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryLocalCause.setStatus("mandatory")
_IsdnCallHistoryChargeInfo_Type = DisplayString
_IsdnCallHistoryChargeInfo_Object = MibTableColumn
isdnCallHistoryChargeInfo = _IsdnCallHistoryChargeInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 21),
    _IsdnCallHistoryChargeInfo_Type()
)
isdnCallHistoryChargeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryChargeInfo.setStatus("mandatory")


class _IsdnCallHistoryScreening_Type(Integer32):
    """Custom type isdnCallHistoryScreening based on Integer32"""
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
        *(("network", 4),
          ("undefined", 5),
          ("user", 1),
          ("user-failed", 3),
          ("user-verified", 2))
    )


_IsdnCallHistoryScreening_Type.__name__ = "Integer32"
_IsdnCallHistoryScreening_Object = MibTableColumn
isdnCallHistoryScreening = _IsdnCallHistoryScreening_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 22),
    _IsdnCallHistoryScreening_Type()
)
isdnCallHistoryScreening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryScreening.setStatus("mandatory")
_IsdnCallHistoryInfo_Type = DisplayString
_IsdnCallHistoryInfo_Object = MibTableColumn
isdnCallHistoryInfo = _IsdnCallHistoryInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 23),
    _IsdnCallHistoryInfo_Type()
)
isdnCallHistoryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryInfo.setStatus("mandatory")
_IsdnCallHistoryReceivedPackets_Type = Counter32
_IsdnCallHistoryReceivedPackets_Object = MibTableColumn
isdnCallHistoryReceivedPackets = _IsdnCallHistoryReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 24),
    _IsdnCallHistoryReceivedPackets_Type()
)
isdnCallHistoryReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryReceivedPackets.setStatus("mandatory")
_IsdnCallHistoryReceivedOctets_Type = Counter32
_IsdnCallHistoryReceivedOctets_Object = MibTableColumn
isdnCallHistoryReceivedOctets = _IsdnCallHistoryReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 25),
    _IsdnCallHistoryReceivedOctets_Type()
)
isdnCallHistoryReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryReceivedOctets.setStatus("mandatory")
_IsdnCallHistoryReceivedErrors_Type = Counter32
_IsdnCallHistoryReceivedErrors_Object = MibTableColumn
isdnCallHistoryReceivedErrors = _IsdnCallHistoryReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 26),
    _IsdnCallHistoryReceivedErrors_Type()
)
isdnCallHistoryReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryReceivedErrors.setStatus("mandatory")
_IsdnCallHistoryTransmitPackets_Type = Counter32
_IsdnCallHistoryTransmitPackets_Object = MibTableColumn
isdnCallHistoryTransmitPackets = _IsdnCallHistoryTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 27),
    _IsdnCallHistoryTransmitPackets_Type()
)
isdnCallHistoryTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryTransmitPackets.setStatus("mandatory")
_IsdnCallHistoryTransmitOctets_Type = Counter32
_IsdnCallHistoryTransmitOctets_Object = MibTableColumn
isdnCallHistoryTransmitOctets = _IsdnCallHistoryTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 28),
    _IsdnCallHistoryTransmitOctets_Type()
)
isdnCallHistoryTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryTransmitOctets.setStatus("mandatory")
_IsdnCallHistoryTransmitErrors_Type = Counter32
_IsdnCallHistoryTransmitErrors_Object = MibTableColumn
isdnCallHistoryTransmitErrors = _IsdnCallHistoryTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 8, 1, 29),
    _IsdnCallHistoryTransmitErrors_Type()
)
isdnCallHistoryTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallHistoryTransmitErrors.setStatus("mandatory")


class _IsdnLoginOnPPPDispatch_Type(Integer32):
    """Custom type isdnLoginOnPPPDispatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_IsdnLoginOnPPPDispatch_Type.__name__ = "Integer32"
_IsdnLoginOnPPPDispatch_Object = MibScalar
isdnLoginOnPPPDispatch = _IsdnLoginOnPPPDispatch_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 9),
    _IsdnLoginOnPPPDispatch_Type()
)
isdnLoginOnPPPDispatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnLoginOnPPPDispatch.setStatus("mandatory")


class _IsdnHistoryMaxEntries_Type(Integer32):
    """Custom type isdnHistoryMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnHistoryMaxEntries_Type.__name__ = "Integer32"
_IsdnHistoryMaxEntries_Object = MibScalar
isdnHistoryMaxEntries = _IsdnHistoryMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 10),
    _IsdnHistoryMaxEntries_Type()
)
isdnHistoryMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnHistoryMaxEntries.setStatus("mandatory")
_IsdnloginAllowTable_Object = MibTable
isdnloginAllowTable = _IsdnloginAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 11)
)
if mibBuilder.loadTexts:
    isdnloginAllowTable.setStatus("mandatory")
_IsdnloginAllowEntry_Object = MibTableRow
isdnloginAllowEntry = _IsdnloginAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 11, 1)
)
isdnloginAllowEntry.setIndexNames(
    (0, "BIANCA-BOX-ISDN-MIB", "isdnloginAllowStkNumber"),
)
if mibBuilder.loadTexts:
    isdnloginAllowEntry.setStatus("mandatory")


class _IsdnloginAllowStkNumber_Type(Integer32):
    """Custom type isdnloginAllowStkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_IsdnloginAllowStkNumber_Type.__name__ = "Integer32"
_IsdnloginAllowStkNumber_Object = MibTableColumn
isdnloginAllowStkNumber = _IsdnloginAllowStkNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 11, 1, 1),
    _IsdnloginAllowStkNumber_Type()
)
isdnloginAllowStkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnloginAllowStkNumber.setStatus("mandatory")
_IsdnloginAllowRemoteNumber_Type = DisplayString
_IsdnloginAllowRemoteNumber_Object = MibTableColumn
isdnloginAllowRemoteNumber = _IsdnloginAllowRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 11, 1, 2),
    _IsdnloginAllowRemoteNumber_Type()
)
isdnloginAllowRemoteNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnloginAllowRemoteNumber.setStatus("mandatory")
_IsdnloginAllowRemoteSubaddress_Type = OctetString
_IsdnloginAllowRemoteSubaddress_Object = MibTableColumn
isdnloginAllowRemoteSubaddress = _IsdnloginAllowRemoteSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 11, 1, 3),
    _IsdnloginAllowRemoteSubaddress_Type()
)
isdnloginAllowRemoteSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnloginAllowRemoteSubaddress.setStatus("mandatory")


class _IsdnloginAllowScreening_Type(Integer32):
    """Custom type isdnloginAllowScreening based on Integer32"""
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
        *(("delete", 6),
          ("dont-care", 5),
          ("network", 4),
          ("user", 1),
          ("user-failed", 3),
          ("user-verified", 2))
    )


_IsdnloginAllowScreening_Type.__name__ = "Integer32"
_IsdnloginAllowScreening_Object = MibTableColumn
isdnloginAllowScreening = _IsdnloginAllowScreening_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 11, 1, 4),
    _IsdnloginAllowScreening_Type()
)
isdnloginAllowScreening.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnloginAllowScreening.setStatus("mandatory")
_IsdnCreditsTable_Object = MibTable
isdnCreditsTable = _IsdnCreditsTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12)
)
if mibBuilder.loadTexts:
    isdnCreditsTable.setStatus("mandatory")
_IsdnCreditsEntry_Object = MibTableRow
isdnCreditsEntry = _IsdnCreditsEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1)
)
isdnCreditsEntry.setIndexNames(
    (0, "BIANCA-BOX-ISDN-MIB", "isdnCreditsSubsysNumber"),
)
if mibBuilder.loadTexts:
    isdnCreditsEntry.setStatus("mandatory")


class _IsdnCreditsSubsysNumber_Type(Integer32):
    """Custom type isdnCreditsSubsysNumber based on Integer32"""
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
        *(("capi", 2),
          ("doorintercom", 5),
          ("isdnlogin", 3),
          ("pots", 4),
          ("ppp", 1))
    )


_IsdnCreditsSubsysNumber_Type.__name__ = "Integer32"
_IsdnCreditsSubsysNumber_Object = MibTableColumn
isdnCreditsSubsysNumber = _IsdnCreditsSubsysNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 1),
    _IsdnCreditsSubsysNumber_Type()
)
isdnCreditsSubsysNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCreditsSubsysNumber.setStatus("mandatory")


class _IsdnCreditsSurveillance_Type(Integer32):
    """Custom type isdnCreditsSurveillance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IsdnCreditsSurveillance_Type.__name__ = "Integer32"
_IsdnCreditsSurveillance_Object = MibTableColumn
isdnCreditsSurveillance = _IsdnCreditsSurveillance_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 2),
    _IsdnCreditsSurveillance_Type()
)
isdnCreditsSurveillance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsSurveillance.setStatus("mandatory")
_IsdnCreditsMeasuretime_Type = Integer32
_IsdnCreditsMeasuretime_Object = MibTableColumn
isdnCreditsMeasuretime = _IsdnCreditsMeasuretime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 3),
    _IsdnCreditsMeasuretime_Type()
)
isdnCreditsMeasuretime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsMeasuretime.setStatus("mandatory")
_IsdnCreditsMaxInCon_Type = Integer32
_IsdnCreditsMaxInCon_Object = MibTableColumn
isdnCreditsMaxInCon = _IsdnCreditsMaxInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 4),
    _IsdnCreditsMaxInCon_Type()
)
isdnCreditsMaxInCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsMaxInCon.setStatus("mandatory")
_IsdnCreditsMaxOutCon_Type = Integer32
_IsdnCreditsMaxOutCon_Object = MibTableColumn
isdnCreditsMaxOutCon = _IsdnCreditsMaxOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 5),
    _IsdnCreditsMaxOutCon_Type()
)
isdnCreditsMaxOutCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsMaxOutCon.setStatus("mandatory")
_IsdnCreditsMaxCharge_Type = Integer32
_IsdnCreditsMaxCharge_Object = MibTableColumn
isdnCreditsMaxCharge = _IsdnCreditsMaxCharge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 6),
    _IsdnCreditsMaxCharge_Type()
)
isdnCreditsMaxCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsMaxCharge.setStatus("mandatory")
_IsdnCreditsMaxInDuration_Type = Integer32
_IsdnCreditsMaxInDuration_Object = MibTableColumn
isdnCreditsMaxInDuration = _IsdnCreditsMaxInDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 7),
    _IsdnCreditsMaxInDuration_Type()
)
isdnCreditsMaxInDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsMaxInDuration.setStatus("mandatory")
_IsdnCreditsMaxOutDuration_Type = Integer32
_IsdnCreditsMaxOutDuration_Object = MibTableColumn
isdnCreditsMaxOutDuration = _IsdnCreditsMaxOutDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 8),
    _IsdnCreditsMaxOutDuration_Type()
)
isdnCreditsMaxOutDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsMaxOutDuration.setStatus("mandatory")
_IsdnCreditsTimeleft_Type = Integer32
_IsdnCreditsTimeleft_Object = MibTableColumn
isdnCreditsTimeleft = _IsdnCreditsTimeleft_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 9),
    _IsdnCreditsTimeleft_Type()
)
isdnCreditsTimeleft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsTimeleft.setStatus("mandatory")
_IsdnCreditsCurrentInCon_Type = Integer32
_IsdnCreditsCurrentInCon_Object = MibTableColumn
isdnCreditsCurrentInCon = _IsdnCreditsCurrentInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 10),
    _IsdnCreditsCurrentInCon_Type()
)
isdnCreditsCurrentInCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCreditsCurrentInCon.setStatus("mandatory")
_IsdnCreditsCurrentOutCon_Type = Integer32
_IsdnCreditsCurrentOutCon_Object = MibTableColumn
isdnCreditsCurrentOutCon = _IsdnCreditsCurrentOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 11),
    _IsdnCreditsCurrentOutCon_Type()
)
isdnCreditsCurrentOutCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCreditsCurrentOutCon.setStatus("mandatory")
_IsdnCreditsTotalInCon_Type = Integer32
_IsdnCreditsTotalInCon_Object = MibTableColumn
isdnCreditsTotalInCon = _IsdnCreditsTotalInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 12),
    _IsdnCreditsTotalInCon_Type()
)
isdnCreditsTotalInCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCreditsTotalInCon.setStatus("mandatory")
_IsdnCreditsTotalOutCon_Type = Integer32
_IsdnCreditsTotalOutCon_Object = MibTableColumn
isdnCreditsTotalOutCon = _IsdnCreditsTotalOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 13),
    _IsdnCreditsTotalOutCon_Type()
)
isdnCreditsTotalOutCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCreditsTotalOutCon.setStatus("mandatory")
_IsdnCreditsTotalMaxCon_Type = Integer32
_IsdnCreditsTotalMaxCon_Object = MibTableColumn
isdnCreditsTotalMaxCon = _IsdnCreditsTotalMaxCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 14),
    _IsdnCreditsTotalMaxCon_Type()
)
isdnCreditsTotalMaxCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCreditsTotalMaxCon.setStatus("mandatory")
_IsdnCreditsTotalCharge_Type = Integer32
_IsdnCreditsTotalCharge_Object = MibTableColumn
isdnCreditsTotalCharge = _IsdnCreditsTotalCharge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 15),
    _IsdnCreditsTotalCharge_Type()
)
isdnCreditsTotalCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCreditsTotalCharge.setStatus("mandatory")
_IsdnCreditsTotalInDuration_Type = Integer32
_IsdnCreditsTotalInDuration_Object = MibTableColumn
isdnCreditsTotalInDuration = _IsdnCreditsTotalInDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 16),
    _IsdnCreditsTotalInDuration_Type()
)
isdnCreditsTotalInDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCreditsTotalInDuration.setStatus("mandatory")
_IsdnCreditsTotalOutDuration_Type = Integer32
_IsdnCreditsTotalOutDuration_Object = MibTableColumn
isdnCreditsTotalOutDuration = _IsdnCreditsTotalOutDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 17),
    _IsdnCreditsTotalOutDuration_Type()
)
isdnCreditsTotalOutDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCreditsTotalOutDuration.setStatus("mandatory")
_IsdnCreditsMaxCurrentInCon_Type = Integer32
_IsdnCreditsMaxCurrentInCon_Object = MibTableColumn
isdnCreditsMaxCurrentInCon = _IsdnCreditsMaxCurrentInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 18),
    _IsdnCreditsMaxCurrentInCon_Type()
)
isdnCreditsMaxCurrentInCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsMaxCurrentInCon.setStatus("mandatory")
_IsdnCreditsMaxCurrentOutCon_Type = Integer32
_IsdnCreditsMaxCurrentOutCon_Object = MibTableColumn
isdnCreditsMaxCurrentOutCon = _IsdnCreditsMaxCurrentOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 19),
    _IsdnCreditsMaxCurrentOutCon_Type()
)
isdnCreditsMaxCurrentOutCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsMaxCurrentOutCon.setStatus("mandatory")
_IsdnCreditsMaxCurrentCon_Type = Integer32
_IsdnCreditsMaxCurrentCon_Object = MibTableColumn
isdnCreditsMaxCurrentCon = _IsdnCreditsMaxCurrentCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 12, 1, 20),
    _IsdnCreditsMaxCurrentCon_Type()
)
isdnCreditsMaxCurrentCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCreditsMaxCurrentCon.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BOX-ISDN-MIB",
    **{"Date": Date,
       "HexValue": HexValue,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "isdn": isdn,
       "isdnIfTable": isdnIfTable,
       "isdnIfEntry": isdnIfEntry,
       "isdnIfIndex": isdnIfIndex,
       "isdnIfDescription": isdnIfDescription,
       "isdnIfLayer1State": isdnIfLayer1State,
       "isdnIfBchannelControl": isdnIfBchannelControl,
       "isdnIfActivationRequest": isdnIfActivationRequest,
       "isdnIfMode": isdnIfMode,
       "isdnIfTimerT3": isdnIfTimerT3,
       "isdnIfUsePowerDetector": isdnIfUsePowerDetector,
       "isdnIfNumberOfChannels": isdnIfNumberOfChannels,
       "isdnIfTimeouts": isdnIfTimeouts,
       "isdnIfActivates": isdnIfActivates,
       "isdnIfDeactivates": isdnIfDeactivates,
       "isdnIfAutoconfigState": isdnIfAutoconfigState,
       "isdnIfAutoconfig": isdnIfAutoconfig,
       "isdnIfSlips": isdnIfSlips,
       "isdnChTable": isdnChTable,
       "isdnChEntry": isdnChEntry,
       "isdnChIsdnIfIndex": isdnChIsdnIfIndex,
       "isdnChNumber": isdnChNumber,
       "isdnChState": isdnChState,
       "isdnChType": isdnChType,
       "isdnChBundle": isdnChBundle,
       "isdnChThroughput": isdnChThroughput,
       "isdnChReceivedPackets": isdnChReceivedPackets,
       "isdnChReceivedOctets": isdnChReceivedOctets,
       "isdnChReceivedErrors": isdnChReceivedErrors,
       "isdnChTransmitPackets": isdnChTransmitPackets,
       "isdnChTransmitOctets": isdnChTransmitOctets,
       "isdnChTransmitErrors": isdnChTransmitErrors,
       "isdnStkTable": isdnStkTable,
       "isdnStkEntry": isdnStkEntry,
       "isdnStkNumber": isdnStkNumber,
       "isdnStkIsdnIfIndex": isdnStkIsdnIfIndex,
       "isdnStkProtocolProfile": isdnStkProtocolProfile,
       "isdnStkConfiguration": isdnStkConfiguration,
       "isdnStkSPID": isdnStkSPID,
       "isdnStkTeiProc": isdnStkTeiProc,
       "isdnStkTeiValue": isdnStkTeiValue,
       "isdnStkClearAllCalls": isdnStkClearAllCalls,
       "isdnStkStatus": isdnStkStatus,
       "isdnStkLayer2State": isdnStkLayer2State,
       "isdnStkBchannels": isdnStkBchannels,
       "isdnStkDialOutPrefix": isdnStkDialOutPrefix,
       "isdnCallTable": isdnCallTable,
       "isdnCallEntry": isdnCallEntry,
       "isdnCallStkNumber": isdnCallStkNumber,
       "isdnCallType": isdnCallType,
       "isdnCallReference": isdnCallReference,
       "isdnCallAge": isdnCallAge,
       "isdnCallState": isdnCallState,
       "isdnCallIsdnIfIndex": isdnCallIsdnIfIndex,
       "isdnCallChannel": isdnCallChannel,
       "isdnCallDspItem": isdnCallDspItem,
       "isdnCallRemoteNumber": isdnCallRemoteNumber,
       "isdnCallRemoteSubaddress": isdnCallRemoteSubaddress,
       "isdnCallLocalNumber": isdnCallLocalNumber,
       "isdnCallLocalSubaddress": isdnCallLocalSubaddress,
       "isdnCallServiceIndicator": isdnCallServiceIndicator,
       "isdnCallAddInfo": isdnCallAddInfo,
       "isdnCallBC": isdnCallBC,
       "isdnCallLLC": isdnCallLLC,
       "isdnCallHLC": isdnCallHLC,
       "isdnCallCharge": isdnCallCharge,
       "isdnCallReceivedPackets": isdnCallReceivedPackets,
       "isdnCallReceivedOctets": isdnCallReceivedOctets,
       "isdnCallReceivedErrors": isdnCallReceivedErrors,
       "isdnCallTransmitPackets": isdnCallTransmitPackets,
       "isdnCallTransmitOctets": isdnCallTransmitOctets,
       "isdnCallTransmitErrors": isdnCallTransmitErrors,
       "isdnCallChargeInfo": isdnCallChargeInfo,
       "isdnCallScreening": isdnCallScreening,
       "isdnCallInfo": isdnCallInfo,
       "isdnDispatchTable": isdnDispatchTable,
       "isdnDispatchEntry": isdnDispatchEntry,
       "isdnDspStkNumber": isdnDspStkNumber,
       "isdnDspItem": isdnDspItem,
       "isdnDspLocalNumber": isdnDspLocalNumber,
       "isdnDspLocalSubaddress": isdnDspLocalSubaddress,
       "isdnDspBearer": isdnDspBearer,
       "isdnDspSlot": isdnDspSlot,
       "isdnDspUnit": isdnDspUnit,
       "isdnDspDirection": isdnDspDirection,
       "isdnDspMode": isdnDspMode,
       "isdnDspUserName": isdnDspUserName,
       "isdnDChanX31Table": isdnDChanX31Table,
       "isdnDChanX31Entry": isdnDChanX31Entry,
       "isdnX31IsdnIfIndex": isdnX31IsdnIfIndex,
       "isdnX31TeiProc": isdnX31TeiProc,
       "isdnX31TeiValue": isdnX31TeiValue,
       "isdnX31AssignedTo": isdnX31AssignedTo,
       "isdnAccountingTemplate": isdnAccountingTemplate,
       "isdnCallHistoryTable": isdnCallHistoryTable,
       "isdnCallHistoryEntry": isdnCallHistoryEntry,
       "isdnCallHistoryStkNumber": isdnCallHistoryStkNumber,
       "isdnCallHistoryType": isdnCallHistoryType,
       "isdnCallHistoryTime": isdnCallHistoryTime,
       "isdnCallHistoryDuration": isdnCallHistoryDuration,
       "isdnCallHistoryIsdnIfIndex": isdnCallHistoryIsdnIfIndex,
       "isdnCallHistoryChannel": isdnCallHistoryChannel,
       "isdnCallHistoryDspItem": isdnCallHistoryDspItem,
       "isdnCallHistoryRemoteNumber": isdnCallHistoryRemoteNumber,
       "isdnCallHistoryRemoteSubaddress": isdnCallHistoryRemoteSubaddress,
       "isdnCallHistoryLocalNumber": isdnCallHistoryLocalNumber,
       "isdnCallHistoryLocalSubaddress": isdnCallHistoryLocalSubaddress,
       "isdnCallHistoryServiceIndicator": isdnCallHistoryServiceIndicator,
       "isdnCallHistoryAddInfo": isdnCallHistoryAddInfo,
       "isdnCallHistoryBC": isdnCallHistoryBC,
       "isdnCallHistoryLLC": isdnCallHistoryLLC,
       "isdnCallHistoryHLC": isdnCallHistoryHLC,
       "isdnCallHistoryCharge": isdnCallHistoryCharge,
       "isdnCallHistoryDSS1Cause": isdnCallHistoryDSS1Cause,
       "isdnCallHistory1TR6Cause": isdnCallHistory1TR6Cause,
       "isdnCallHistoryLocalCause": isdnCallHistoryLocalCause,
       "isdnCallHistoryChargeInfo": isdnCallHistoryChargeInfo,
       "isdnCallHistoryScreening": isdnCallHistoryScreening,
       "isdnCallHistoryInfo": isdnCallHistoryInfo,
       "isdnCallHistoryReceivedPackets": isdnCallHistoryReceivedPackets,
       "isdnCallHistoryReceivedOctets": isdnCallHistoryReceivedOctets,
       "isdnCallHistoryReceivedErrors": isdnCallHistoryReceivedErrors,
       "isdnCallHistoryTransmitPackets": isdnCallHistoryTransmitPackets,
       "isdnCallHistoryTransmitOctets": isdnCallHistoryTransmitOctets,
       "isdnCallHistoryTransmitErrors": isdnCallHistoryTransmitErrors,
       "isdnLoginOnPPPDispatch": isdnLoginOnPPPDispatch,
       "isdnHistoryMaxEntries": isdnHistoryMaxEntries,
       "isdnloginAllowTable": isdnloginAllowTable,
       "isdnloginAllowEntry": isdnloginAllowEntry,
       "isdnloginAllowStkNumber": isdnloginAllowStkNumber,
       "isdnloginAllowRemoteNumber": isdnloginAllowRemoteNumber,
       "isdnloginAllowRemoteSubaddress": isdnloginAllowRemoteSubaddress,
       "isdnloginAllowScreening": isdnloginAllowScreening,
       "isdnCreditsTable": isdnCreditsTable,
       "isdnCreditsEntry": isdnCreditsEntry,
       "isdnCreditsSubsysNumber": isdnCreditsSubsysNumber,
       "isdnCreditsSurveillance": isdnCreditsSurveillance,
       "isdnCreditsMeasuretime": isdnCreditsMeasuretime,
       "isdnCreditsMaxInCon": isdnCreditsMaxInCon,
       "isdnCreditsMaxOutCon": isdnCreditsMaxOutCon,
       "isdnCreditsMaxCharge": isdnCreditsMaxCharge,
       "isdnCreditsMaxInDuration": isdnCreditsMaxInDuration,
       "isdnCreditsMaxOutDuration": isdnCreditsMaxOutDuration,
       "isdnCreditsTimeleft": isdnCreditsTimeleft,
       "isdnCreditsCurrentInCon": isdnCreditsCurrentInCon,
       "isdnCreditsCurrentOutCon": isdnCreditsCurrentOutCon,
       "isdnCreditsTotalInCon": isdnCreditsTotalInCon,
       "isdnCreditsTotalOutCon": isdnCreditsTotalOutCon,
       "isdnCreditsTotalMaxCon": isdnCreditsTotalMaxCon,
       "isdnCreditsTotalCharge": isdnCreditsTotalCharge,
       "isdnCreditsTotalInDuration": isdnCreditsTotalInDuration,
       "isdnCreditsTotalOutDuration": isdnCreditsTotalOutDuration,
       "isdnCreditsMaxCurrentInCon": isdnCreditsMaxCurrentInCon,
       "isdnCreditsMaxCurrentOutCon": isdnCreditsMaxCurrentOutCon,
       "isdnCreditsMaxCurrentCon": isdnCreditsMaxCurrentCon}
)
