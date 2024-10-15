# SNMP MIB module (HUAWEI-VO-GENERAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VO-GENERAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:30 2024
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
    "HUAWEI-3COM-OID-MIB",
    "voice")

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

hwVoiceGeneralMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1)
)
hwVoiceGeneralMIB.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions



class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVoiceGeneralObjects_ObjectIdentity = ObjectIdentity
hwVoiceGeneralObjects = _HwVoiceGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1)
)
_HwVoiceGeneralGroup_ObjectIdentity = ObjectIdentity
hwVoiceGeneralGroup = _HwVoiceGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1)
)


class _HwVoGeneralJitterLen_Type(Integer32):
    """Custom type hwVoGeneralJitterLen based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HwVoGeneralJitterLen_Type.__name__ = "Integer32"
_HwVoGeneralJitterLen_Object = MibScalar
hwVoGeneralJitterLen = _HwVoGeneralJitterLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 1),
    _HwVoGeneralJitterLen_Type()
)
hwVoGeneralJitterLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralJitterLen.setStatus("current")


class _HwVoGeneralMatchPolicy_Type(Integer32):
    """Custom type hwVoGeneralMatchPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_HwVoGeneralMatchPolicy_Type.__name__ = "Integer32"
_HwVoGeneralMatchPolicy_Object = MibScalar
hwVoGeneralMatchPolicy = _HwVoGeneralMatchPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 2),
    _HwVoGeneralMatchPolicy_Type()
)
hwVoGeneralMatchPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralMatchPolicy.setStatus("current")


class _HwVoGeneralSendPerformance_Type(Integer32):
    """Custom type hwVoGeneralSendPerformance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("normal", 1))
    )


_HwVoGeneralSendPerformance_Type.__name__ = "Integer32"
_HwVoGeneralSendPerformance_Object = MibScalar
hwVoGeneralSendPerformance = _HwVoGeneralSendPerformance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 3),
    _HwVoGeneralSendPerformance_Type()
)
hwVoGeneralSendPerformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralSendPerformance.setStatus("current")


class _HwVoGeneralReceivePerformance_Type(Integer32):
    """Custom type hwVoGeneralReceivePerformance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("normal", 1))
    )


_HwVoGeneralReceivePerformance_Type.__name__ = "Integer32"
_HwVoGeneralReceivePerformance_Object = MibScalar
hwVoGeneralReceivePerformance = _HwVoGeneralReceivePerformance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 4),
    _HwVoGeneralReceivePerformance_Type()
)
hwVoGeneralReceivePerformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralReceivePerformance.setStatus("current")


class _HwVoGeneralDataStatistics_Type(Integer32):
    """Custom type hwVoGeneralDataStatistics based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoGeneralDataStatistics_Type.__name__ = "Integer32"
_HwVoGeneralDataStatistics_Object = MibScalar
hwVoGeneralDataStatistics = _HwVoGeneralDataStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 5),
    _HwVoGeneralDataStatistics_Type()
)
hwVoGeneralDataStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralDataStatistics.setStatus("current")


class _HwVoGeneralPacketPrecedence_Type(Integer32):
    """Custom type hwVoGeneralPacketPrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwVoGeneralPacketPrecedence_Type.__name__ = "Integer32"
_HwVoGeneralPacketPrecedence_Object = MibScalar
hwVoGeneralPacketPrecedence = _HwVoGeneralPacketPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 6),
    _HwVoGeneralPacketPrecedence_Type()
)
hwVoGeneralPacketPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralPacketPrecedence.setStatus("current")


class _HwVoGeneralDialTerminator_Type(OctetString):
    """Custom type hwVoGeneralDialTerminator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_HwVoGeneralDialTerminator_Type.__name__ = "OctetString"
_HwVoGeneralDialTerminator_Object = MibScalar
hwVoGeneralDialTerminator = _HwVoGeneralDialTerminator_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 7),
    _HwVoGeneralDialTerminator_Type()
)
hwVoGeneralDialTerminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralDialTerminator.setStatus("current")


class _HwVoGeneralCallStart_Type(Integer32):
    """Custom type hwVoGeneralCallStart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("normal", 2))
    )


_HwVoGeneralCallStart_Type.__name__ = "Integer32"
_HwVoGeneralCallStart_Object = MibScalar
hwVoGeneralCallStart = _HwVoGeneralCallStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 8),
    _HwVoGeneralCallStart_Type()
)
hwVoGeneralCallStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralCallStart.setStatus("current")


class _HwVoGeneralCalledTunnel_Type(Integer32):
    """Custom type hwVoGeneralCalledTunnel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoGeneralCalledTunnel_Type.__name__ = "Integer32"
_HwVoGeneralCalledTunnel_Object = MibScalar
hwVoGeneralCalledTunnel = _HwVoGeneralCalledTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 9),
    _HwVoGeneralCalledTunnel_Type()
)
hwVoGeneralCalledTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralCalledTunnel.setStatus("current")


class _HwVoGeneralSpecialServiceEnable_Type(Integer32):
    """Custom type hwVoGeneralSpecialServiceEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoGeneralSpecialServiceEnable_Type.__name__ = "Integer32"
_HwVoGeneralSpecialServiceEnable_Object = MibScalar
hwVoGeneralSpecialServiceEnable = _HwVoGeneralSpecialServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 10),
    _HwVoGeneralSpecialServiceEnable_Type()
)
hwVoGeneralSpecialServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralSpecialServiceEnable.setStatus("current")


class _HwVoGeneralCallTransferSpecialServiceNumber_Type(OctetString):
    """Custom type hwVoGeneralCallTransferSpecialServiceNumber based on OctetString"""
    defaultValue = OctetString("*12*")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_HwVoGeneralCallTransferSpecialServiceNumber_Type.__name__ = "OctetString"
_HwVoGeneralCallTransferSpecialServiceNumber_Object = MibScalar
hwVoGeneralCallTransferSpecialServiceNumber = _HwVoGeneralCallTransferSpecialServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 11),
    _HwVoGeneralCallTransferSpecialServiceNumber_Type()
)
hwVoGeneralCallTransferSpecialServiceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralCallTransferSpecialServiceNumber.setStatus("current")


class _HwVoGeneralPeerSearchStop_Type(Integer32):
    """Custom type hwVoGeneralPeerSearchStop based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_HwVoGeneralPeerSearchStop_Type.__name__ = "Integer32"
_HwVoGeneralPeerSearchStop_Object = MibScalar
hwVoGeneralPeerSearchStop = _HwVoGeneralPeerSearchStop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 12),
    _HwVoGeneralPeerSearchStop_Type()
)
hwVoGeneralPeerSearchStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralPeerSearchStop.setStatus("current")


class _HwVoGeneralPeerSelectOrderRule_Type(Integer32):
    """Custom type hwVoGeneralPeerSelectOrderRule based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_HwVoGeneralPeerSelectOrderRule_Type.__name__ = "Integer32"
_HwVoGeneralPeerSelectOrderRule_Object = MibScalar
hwVoGeneralPeerSelectOrderRule = _HwVoGeneralPeerSelectOrderRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 13),
    _HwVoGeneralPeerSelectOrderRule_Type()
)
hwVoGeneralPeerSelectOrderRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralPeerSelectOrderRule.setStatus("current")


class _HwVoGeneralPeerSelectTypePriority_Type(Integer32):
    """Custom type hwVoGeneralPeerSelectTypePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_HwVoGeneralPeerSelectTypePriority_Type.__name__ = "Integer32"
_HwVoGeneralPeerSelectTypePriority_Object = MibScalar
hwVoGeneralPeerSelectTypePriority = _HwVoGeneralPeerSelectTypePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 14),
    _HwVoGeneralPeerSelectTypePriority_Type()
)
hwVoGeneralPeerSelectTypePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoGeneralPeerSelectTypePriority.setStatus("current")
_HwVoLtoPTable_Object = MibTable
hwVoLtoPTable = _HwVoLtoPTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwVoLtoPTable.setStatus("current")
_HwVoLtoPEntry_Object = MibTableRow
hwVoLtoPEntry = _HwVoLtoPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1)
)
hwVoLtoPEntry.setIndexNames(
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoLtoPChannel"),
)
if mibBuilder.loadTexts:
    hwVoLtoPEntry.setStatus("current")
_HwVoLtoPChannel_Type = Integer32
_HwVoLtoPChannel_Object = MibTableColumn
hwVoLtoPChannel = _HwVoLtoPChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 1),
    _HwVoLtoPChannel_Type()
)
hwVoLtoPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoLtoPChannel.setStatus("current")
_HwVoLtoPSlot_Type = Integer32
_HwVoLtoPSlot_Object = MibTableColumn
hwVoLtoPSlot = _HwVoLtoPSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 2),
    _HwVoLtoPSlot_Type()
)
hwVoLtoPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoLtoPSlot.setStatus("current")
_HwVoLtoPPort_Type = Integer32
_HwVoLtoPPort_Object = MibTableColumn
hwVoLtoPPort = _HwVoLtoPPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 3),
    _HwVoLtoPPort_Type()
)
hwVoLtoPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoLtoPPort.setStatus("current")
_HwVoLtoPTimeSlot_Type = Integer32
_HwVoLtoPTimeSlot_Object = MibTableColumn
hwVoLtoPTimeSlot = _HwVoLtoPTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 4),
    _HwVoLtoPTimeSlot_Type()
)
hwVoLtoPTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoLtoPTimeSlot.setStatus("current")


class _HwVoLtoPStatus_Type(Integer32):
    """Custom type hwVoLtoPStatus based on Integer32"""
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


_HwVoLtoPStatus_Type.__name__ = "Integer32"
_HwVoLtoPStatus_Object = MibTableColumn
hwVoLtoPStatus = _HwVoLtoPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 5),
    _HwVoLtoPStatus_Type()
)
hwVoLtoPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoLtoPStatus.setStatus("current")


class _HwVoLtoPBoardType_Type(Integer32):
    """Custom type hwVoLtoPBoardType based on Integer32"""
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
        *(("e1vi", 7),
          ("em2", 3),
          ("em4", 6),
          ("fxo2", 2),
          ("fxo4", 5),
          ("fxs2", 1),
          ("fxs4", 4),
          ("sic-fxo1", 10),
          ("sic-fxo2", 12),
          ("sic-fxs1", 9),
          ("sic-fxs2", 11),
          ("t1vi", 8))
    )


_HwVoLtoPBoardType_Type.__name__ = "Integer32"
_HwVoLtoPBoardType_Object = MibTableColumn
hwVoLtoPBoardType = _HwVoLtoPBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 6),
    _HwVoLtoPBoardType_Type()
)
hwVoLtoPBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoLtoPBoardType.setStatus("current")
_HwVoLtoPPortNumber_Type = Integer32
_HwVoLtoPPortNumber_Object = MibTableColumn
hwVoLtoPPortNumber = _HwVoLtoPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 7),
    _HwVoLtoPPortNumber_Type()
)
hwVoLtoPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoLtoPPortNumber.setStatus("current")


class _HwVoLtoPGroupNumber_Type(Integer32):
    """Custom type hwVoLtoPGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 30),
        ValueRangeConstraint(255, 255),
    )


_HwVoLtoPGroupNumber_Type.__name__ = "Integer32"
_HwVoLtoPGroupNumber_Object = MibTableColumn
hwVoLtoPGroupNumber = _HwVoLtoPGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 8),
    _HwVoLtoPGroupNumber_Type()
)
hwVoLtoPGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoLtoPGroupNumber.setStatus("current")
_HwVoDialExpansionTable_Object = MibTable
hwVoDialExpansionTable = _HwVoDialExpansionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwVoDialExpansionTable.setStatus("current")
_HwVoDialExpansionEntry_Object = MibTableRow
hwVoDialExpansionEntry = _HwVoDialExpansionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3, 1)
)
hwVoDialExpansionEntry.setIndexNames(
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoDialExpansionType"),
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoDialExpansionSource"),
)
if mibBuilder.loadTexts:
    hwVoDialExpansionEntry.setStatus("current")


class _HwVoDialExpansionType_Type(Integer32):
    """Custom type hwVoDialExpansionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("callin", 0),
          ("callout", 1))
    )


_HwVoDialExpansionType_Type.__name__ = "Integer32"
_HwVoDialExpansionType_Object = MibTableColumn
hwVoDialExpansionType = _HwVoDialExpansionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3, 1, 1),
    _HwVoDialExpansionType_Type()
)
hwVoDialExpansionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoDialExpansionType.setStatus("current")


class _HwVoDialExpansionSource_Type(OctetString):
    """Custom type hwVoDialExpansionSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVoDialExpansionSource_Type.__name__ = "OctetString"
_HwVoDialExpansionSource_Object = MibTableColumn
hwVoDialExpansionSource = _HwVoDialExpansionSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3, 1, 2),
    _HwVoDialExpansionSource_Type()
)
hwVoDialExpansionSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoDialExpansionSource.setStatus("current")


class _HwVoDialExpansionTarget_Type(OctetString):
    """Custom type hwVoDialExpansionTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVoDialExpansionTarget_Type.__name__ = "OctetString"
_HwVoDialExpansionTarget_Object = MibTableColumn
hwVoDialExpansionTarget = _HwVoDialExpansionTarget_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3, 1, 3),
    _HwVoDialExpansionTarget_Type()
)
hwVoDialExpansionTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoDialExpansionTarget.setStatus("current")
_HwVoDialExpansionRowStatus_Type = EntryStatus
_HwVoDialExpansionRowStatus_Object = MibTableColumn
hwVoDialExpansionRowStatus = _HwVoDialExpansionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3, 1, 4),
    _HwVoDialExpansionRowStatus_Type()
)
hwVoDialExpansionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoDialExpansionRowStatus.setStatus("current")
_HwVoiceNumberSubstGroup_ObjectIdentity = ObjectIdentity
hwVoiceNumberSubstGroup = _HwVoiceNumberSubstGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4)
)
_HwVoNumSubstTable_Object = MibTable
hwVoNumSubstTable = _HwVoNumSubstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwVoNumSubstTable.setStatus("current")
_HwVoNumSubstEntry_Object = MibTableRow
hwVoNumSubstEntry = _HwVoNumSubstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1, 1)
)
hwVoNumSubstEntry.setIndexNames(
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoNumSubstIndex"),
)
if mibBuilder.loadTexts:
    hwVoNumSubstEntry.setStatus("current")


class _HwVoNumSubstIndex_Type(Integer32):
    """Custom type hwVoNumSubstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoNumSubstIndex_Type.__name__ = "Integer32"
_HwVoNumSubstIndex_Object = MibTableColumn
hwVoNumSubstIndex = _HwVoNumSubstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1, 1, 1),
    _HwVoNumSubstIndex_Type()
)
hwVoNumSubstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoNumSubstIndex.setStatus("current")


class _HwVoNumSubstFirstRule_Type(Integer32):
    """Custom type hwVoNumSubstFirstRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(65535, 65535),
    )


_HwVoNumSubstFirstRule_Type.__name__ = "Integer32"
_HwVoNumSubstFirstRule_Object = MibTableColumn
hwVoNumSubstFirstRule = _HwVoNumSubstFirstRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1, 1, 2),
    _HwVoNumSubstFirstRule_Type()
)
hwVoNumSubstFirstRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoNumSubstFirstRule.setStatus("current")


class _HwVoNumSubstDotMatchRule_Type(Integer32):
    """Custom type hwVoNumSubstDotMatchRule based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("end-only", 1),
          ("left-right", 2),
          ("right-left", 3))
    )


_HwVoNumSubstDotMatchRule_Type.__name__ = "Integer32"
_HwVoNumSubstDotMatchRule_Object = MibTableColumn
hwVoNumSubstDotMatchRule = _HwVoNumSubstDotMatchRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1, 1, 3),
    _HwVoNumSubstDotMatchRule_Type()
)
hwVoNumSubstDotMatchRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoNumSubstDotMatchRule.setStatus("current")
_HwVoNumSubstRowStatus_Type = EntryStatus
_HwVoNumSubstRowStatus_Object = MibTableColumn
hwVoNumSubstRowStatus = _HwVoNumSubstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1, 1, 4),
    _HwVoNumSubstRowStatus_Type()
)
hwVoNumSubstRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoNumSubstRowStatus.setStatus("current")
_HwVoNumSubstRuleTable_Object = MibTable
hwVoNumSubstRuleTable = _HwVoNumSubstRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hwVoNumSubstRuleTable.setStatus("current")
_HwVoNumSubstRuleEntry_Object = MibTableRow
hwVoNumSubstRuleEntry = _HwVoNumSubstRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2, 1)
)
hwVoNumSubstRuleEntry.setIndexNames(
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoNumSubstIndex"),
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoNumSubstRuleIndex"),
)
if mibBuilder.loadTexts:
    hwVoNumSubstRuleEntry.setStatus("current")


class _HwVoNumSubstRuleIndex_Type(Integer32):
    """Custom type hwVoNumSubstRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwVoNumSubstRuleIndex_Type.__name__ = "Integer32"
_HwVoNumSubstRuleIndex_Object = MibTableColumn
hwVoNumSubstRuleIndex = _HwVoNumSubstRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2, 1, 1),
    _HwVoNumSubstRuleIndex_Type()
)
hwVoNumSubstRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoNumSubstRuleIndex.setStatus("current")


class _HwVoNumSubstRuleInputFormat_Type(OctetString):
    """Custom type hwVoNumSubstRuleInputFormat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVoNumSubstRuleInputFormat_Type.__name__ = "OctetString"
_HwVoNumSubstRuleInputFormat_Object = MibTableColumn
hwVoNumSubstRuleInputFormat = _HwVoNumSubstRuleInputFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2, 1, 2),
    _HwVoNumSubstRuleInputFormat_Type()
)
hwVoNumSubstRuleInputFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoNumSubstRuleInputFormat.setStatus("current")


class _HwVoNumSubstRuleOutputFormat_Type(OctetString):
    """Custom type hwVoNumSubstRuleOutputFormat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVoNumSubstRuleOutputFormat_Type.__name__ = "OctetString"
_HwVoNumSubstRuleOutputFormat_Object = MibTableColumn
hwVoNumSubstRuleOutputFormat = _HwVoNumSubstRuleOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2, 1, 3),
    _HwVoNumSubstRuleOutputFormat_Type()
)
hwVoNumSubstRuleOutputFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoNumSubstRuleOutputFormat.setStatus("current")
_HwVoNumSubstRuleRowStatus_Type = EntryStatus
_HwVoNumSubstRuleRowStatus_Object = MibTableColumn
hwVoNumSubstRuleRowStatus = _HwVoNumSubstRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2, 1, 4),
    _HwVoNumSubstRuleRowStatus_Type()
)
hwVoNumSubstRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoNumSubstRuleRowStatus.setStatus("current")
_HwVoMaxCallTable_Object = MibTable
hwVoMaxCallTable = _HwVoMaxCallTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwVoMaxCallTable.setStatus("current")
_HwVoMaxCallEntry_Object = MibTableRow
hwVoMaxCallEntry = _HwVoMaxCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 5, 1)
)
hwVoMaxCallEntry.setIndexNames(
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoMaxCallTableIndex"),
)
if mibBuilder.loadTexts:
    hwVoMaxCallEntry.setStatus("current")


class _HwVoMaxCallTableIndex_Type(Integer32):
    """Custom type hwVoMaxCallTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoMaxCallTableIndex_Type.__name__ = "Integer32"
_HwVoMaxCallTableIndex_Object = MibTableColumn
hwVoMaxCallTableIndex = _HwVoMaxCallTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 5, 1, 1),
    _HwVoMaxCallTableIndex_Type()
)
hwVoMaxCallTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoMaxCallTableIndex.setStatus("current")


class _HwVoMaxCallValue_Type(Integer32):
    """Custom type hwVoMaxCallValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HwVoMaxCallValue_Type.__name__ = "Integer32"
_HwVoMaxCallValue_Object = MibTableColumn
hwVoMaxCallValue = _HwVoMaxCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 5, 1, 2),
    _HwVoMaxCallValue_Type()
)
hwVoMaxCallValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoMaxCallValue.setStatus("current")
_HwVoMaxCallTableRowStatus_Type = EntryStatus
_HwVoMaxCallTableRowStatus_Object = MibTableColumn
hwVoMaxCallTableRowStatus = _HwVoMaxCallTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 5, 1, 3),
    _HwVoMaxCallTableRowStatus_Type()
)
hwVoMaxCallTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoMaxCallTableRowStatus.setStatus("current")
_HwVoIncomingCallingNumSubstTable_Object = MibTable
hwVoIncomingCallingNumSubstTable = _HwVoIncomingCallingNumSubstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwVoIncomingCallingNumSubstTable.setStatus("current")
_HwVoIncomingCallingNumSubstEntry_Object = MibTableRow
hwVoIncomingCallingNumSubstEntry = _HwVoIncomingCallingNumSubstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 6, 1)
)
hwVoIncomingCallingNumSubstEntry.setIndexNames(
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoIncomingCallingNumSubstIndex"),
)
if mibBuilder.loadTexts:
    hwVoIncomingCallingNumSubstEntry.setStatus("current")


class _HwVoIncomingCallingNumSubstIndex_Type(Integer32):
    """Custom type hwVoIncomingCallingNumSubstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoIncomingCallingNumSubstIndex_Type.__name__ = "Integer32"
_HwVoIncomingCallingNumSubstIndex_Object = MibTableColumn
hwVoIncomingCallingNumSubstIndex = _HwVoIncomingCallingNumSubstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 6, 1, 1),
    _HwVoIncomingCallingNumSubstIndex_Type()
)
hwVoIncomingCallingNumSubstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoIncomingCallingNumSubstIndex.setStatus("current")
_HwVoIncomingCallingNumSubstRowStatus_Type = EntryStatus
_HwVoIncomingCallingNumSubstRowStatus_Object = MibTableColumn
hwVoIncomingCallingNumSubstRowStatus = _HwVoIncomingCallingNumSubstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 6, 1, 2),
    _HwVoIncomingCallingNumSubstRowStatus_Type()
)
hwVoIncomingCallingNumSubstRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIncomingCallingNumSubstRowStatus.setStatus("current")
_HwVoIncomingCalledNumSubstTable_Object = MibTable
hwVoIncomingCalledNumSubstTable = _HwVoIncomingCalledNumSubstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwVoIncomingCalledNumSubstTable.setStatus("current")
_HwVoIncomingCalledNumSubstEntry_Object = MibTableRow
hwVoIncomingCalledNumSubstEntry = _HwVoIncomingCalledNumSubstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 7, 1)
)
hwVoIncomingCalledNumSubstEntry.setIndexNames(
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoIncomingCalledNumSubstIndex"),
)
if mibBuilder.loadTexts:
    hwVoIncomingCalledNumSubstEntry.setStatus("current")


class _HwVoIncomingCalledNumSubstIndex_Type(Integer32):
    """Custom type hwVoIncomingCalledNumSubstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoIncomingCalledNumSubstIndex_Type.__name__ = "Integer32"
_HwVoIncomingCalledNumSubstIndex_Object = MibTableColumn
hwVoIncomingCalledNumSubstIndex = _HwVoIncomingCalledNumSubstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 7, 1, 1),
    _HwVoIncomingCalledNumSubstIndex_Type()
)
hwVoIncomingCalledNumSubstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoIncomingCalledNumSubstIndex.setStatus("current")
_HwVoIncomingCalledNumSubstRowStatus_Type = EntryStatus
_HwVoIncomingCalledNumSubstRowStatus_Object = MibTableColumn
hwVoIncomingCalledNumSubstRowStatus = _HwVoIncomingCalledNumSubstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 7, 1, 2),
    _HwVoIncomingCalledNumSubstRowStatus_Type()
)
hwVoIncomingCalledNumSubstRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIncomingCalledNumSubstRowStatus.setStatus("current")
_HwVoOutgoingCallingNumSubstTable_Object = MibTable
hwVoOutgoingCallingNumSubstTable = _HwVoOutgoingCallingNumSubstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hwVoOutgoingCallingNumSubstTable.setStatus("current")
_HwVoOutgoingCallingNumSubstEntry_Object = MibTableRow
hwVoOutgoingCallingNumSubstEntry = _HwVoOutgoingCallingNumSubstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 8, 1)
)
hwVoOutgoingCallingNumSubstEntry.setIndexNames(
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoOutgoingCallingNumSubstIndex"),
)
if mibBuilder.loadTexts:
    hwVoOutgoingCallingNumSubstEntry.setStatus("current")


class _HwVoOutgoingCallingNumSubstIndex_Type(Integer32):
    """Custom type hwVoOutgoingCallingNumSubstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoOutgoingCallingNumSubstIndex_Type.__name__ = "Integer32"
_HwVoOutgoingCallingNumSubstIndex_Object = MibTableColumn
hwVoOutgoingCallingNumSubstIndex = _HwVoOutgoingCallingNumSubstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 8, 1, 1),
    _HwVoOutgoingCallingNumSubstIndex_Type()
)
hwVoOutgoingCallingNumSubstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoOutgoingCallingNumSubstIndex.setStatus("current")
_HwVoOutgoingCallingNumSubstRowStatus_Type = EntryStatus
_HwVoOutgoingCallingNumSubstRowStatus_Object = MibTableColumn
hwVoOutgoingCallingNumSubstRowStatus = _HwVoOutgoingCallingNumSubstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 8, 1, 2),
    _HwVoOutgoingCallingNumSubstRowStatus_Type()
)
hwVoOutgoingCallingNumSubstRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoOutgoingCallingNumSubstRowStatus.setStatus("current")
_HwVoOutgoingCalledNumSubstTable_Object = MibTable
hwVoOutgoingCalledNumSubstTable = _HwVoOutgoingCalledNumSubstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hwVoOutgoingCalledNumSubstTable.setStatus("current")
_HwVoOutgoingCalledNumSubstEntry_Object = MibTableRow
hwVoOutgoingCalledNumSubstEntry = _HwVoOutgoingCalledNumSubstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 9, 1)
)
hwVoOutgoingCalledNumSubstEntry.setIndexNames(
    (0, "HUAWEI-VO-GENERAL-MIB", "hwVoOutgoingCalledNumSubstIndex"),
)
if mibBuilder.loadTexts:
    hwVoOutgoingCalledNumSubstEntry.setStatus("current")


class _HwVoOutgoingCalledNumSubstIndex_Type(Integer32):
    """Custom type hwVoOutgoingCalledNumSubstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoOutgoingCalledNumSubstIndex_Type.__name__ = "Integer32"
_HwVoOutgoingCalledNumSubstIndex_Object = MibTableColumn
hwVoOutgoingCalledNumSubstIndex = _HwVoOutgoingCalledNumSubstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 9, 1, 1),
    _HwVoOutgoingCalledNumSubstIndex_Type()
)
hwVoOutgoingCalledNumSubstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoOutgoingCalledNumSubstIndex.setStatus("current")
_HwVoOutgoingCalledNumSubstRowStatus_Type = EntryStatus
_HwVoOutgoingCalledNumSubstRowStatus_Object = MibTableColumn
hwVoOutgoingCalledNumSubstRowStatus = _HwVoOutgoingCalledNumSubstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 9, 1, 2),
    _HwVoOutgoingCalledNumSubstRowStatus_Type()
)
hwVoOutgoingCalledNumSubstRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoOutgoingCalledNumSubstRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VO-GENERAL-MIB",
    **{"EntryStatus": EntryStatus,
       "hwVoiceGeneralMIB": hwVoiceGeneralMIB,
       "hwVoiceGeneralObjects": hwVoiceGeneralObjects,
       "hwVoiceGeneralGroup": hwVoiceGeneralGroup,
       "hwVoGeneralJitterLen": hwVoGeneralJitterLen,
       "hwVoGeneralMatchPolicy": hwVoGeneralMatchPolicy,
       "hwVoGeneralSendPerformance": hwVoGeneralSendPerformance,
       "hwVoGeneralReceivePerformance": hwVoGeneralReceivePerformance,
       "hwVoGeneralDataStatistics": hwVoGeneralDataStatistics,
       "hwVoGeneralPacketPrecedence": hwVoGeneralPacketPrecedence,
       "hwVoGeneralDialTerminator": hwVoGeneralDialTerminator,
       "hwVoGeneralCallStart": hwVoGeneralCallStart,
       "hwVoGeneralCalledTunnel": hwVoGeneralCalledTunnel,
       "hwVoGeneralSpecialServiceEnable": hwVoGeneralSpecialServiceEnable,
       "hwVoGeneralCallTransferSpecialServiceNumber": hwVoGeneralCallTransferSpecialServiceNumber,
       "hwVoGeneralPeerSearchStop": hwVoGeneralPeerSearchStop,
       "hwVoGeneralPeerSelectOrderRule": hwVoGeneralPeerSelectOrderRule,
       "hwVoGeneralPeerSelectTypePriority": hwVoGeneralPeerSelectTypePriority,
       "hwVoLtoPTable": hwVoLtoPTable,
       "hwVoLtoPEntry": hwVoLtoPEntry,
       "hwVoLtoPChannel": hwVoLtoPChannel,
       "hwVoLtoPSlot": hwVoLtoPSlot,
       "hwVoLtoPPort": hwVoLtoPPort,
       "hwVoLtoPTimeSlot": hwVoLtoPTimeSlot,
       "hwVoLtoPStatus": hwVoLtoPStatus,
       "hwVoLtoPBoardType": hwVoLtoPBoardType,
       "hwVoLtoPPortNumber": hwVoLtoPPortNumber,
       "hwVoLtoPGroupNumber": hwVoLtoPGroupNumber,
       "hwVoDialExpansionTable": hwVoDialExpansionTable,
       "hwVoDialExpansionEntry": hwVoDialExpansionEntry,
       "hwVoDialExpansionType": hwVoDialExpansionType,
       "hwVoDialExpansionSource": hwVoDialExpansionSource,
       "hwVoDialExpansionTarget": hwVoDialExpansionTarget,
       "hwVoDialExpansionRowStatus": hwVoDialExpansionRowStatus,
       "hwVoiceNumberSubstGroup": hwVoiceNumberSubstGroup,
       "hwVoNumSubstTable": hwVoNumSubstTable,
       "hwVoNumSubstEntry": hwVoNumSubstEntry,
       "hwVoNumSubstIndex": hwVoNumSubstIndex,
       "hwVoNumSubstFirstRule": hwVoNumSubstFirstRule,
       "hwVoNumSubstDotMatchRule": hwVoNumSubstDotMatchRule,
       "hwVoNumSubstRowStatus": hwVoNumSubstRowStatus,
       "hwVoNumSubstRuleTable": hwVoNumSubstRuleTable,
       "hwVoNumSubstRuleEntry": hwVoNumSubstRuleEntry,
       "hwVoNumSubstRuleIndex": hwVoNumSubstRuleIndex,
       "hwVoNumSubstRuleInputFormat": hwVoNumSubstRuleInputFormat,
       "hwVoNumSubstRuleOutputFormat": hwVoNumSubstRuleOutputFormat,
       "hwVoNumSubstRuleRowStatus": hwVoNumSubstRuleRowStatus,
       "hwVoMaxCallTable": hwVoMaxCallTable,
       "hwVoMaxCallEntry": hwVoMaxCallEntry,
       "hwVoMaxCallTableIndex": hwVoMaxCallTableIndex,
       "hwVoMaxCallValue": hwVoMaxCallValue,
       "hwVoMaxCallTableRowStatus": hwVoMaxCallTableRowStatus,
       "hwVoIncomingCallingNumSubstTable": hwVoIncomingCallingNumSubstTable,
       "hwVoIncomingCallingNumSubstEntry": hwVoIncomingCallingNumSubstEntry,
       "hwVoIncomingCallingNumSubstIndex": hwVoIncomingCallingNumSubstIndex,
       "hwVoIncomingCallingNumSubstRowStatus": hwVoIncomingCallingNumSubstRowStatus,
       "hwVoIncomingCalledNumSubstTable": hwVoIncomingCalledNumSubstTable,
       "hwVoIncomingCalledNumSubstEntry": hwVoIncomingCalledNumSubstEntry,
       "hwVoIncomingCalledNumSubstIndex": hwVoIncomingCalledNumSubstIndex,
       "hwVoIncomingCalledNumSubstRowStatus": hwVoIncomingCalledNumSubstRowStatus,
       "hwVoOutgoingCallingNumSubstTable": hwVoOutgoingCallingNumSubstTable,
       "hwVoOutgoingCallingNumSubstEntry": hwVoOutgoingCallingNumSubstEntry,
       "hwVoOutgoingCallingNumSubstIndex": hwVoOutgoingCallingNumSubstIndex,
       "hwVoOutgoingCallingNumSubstRowStatus": hwVoOutgoingCallingNumSubstRowStatus,
       "hwVoOutgoingCalledNumSubstTable": hwVoOutgoingCalledNumSubstTable,
       "hwVoOutgoingCalledNumSubstEntry": hwVoOutgoingCalledNumSubstEntry,
       "hwVoOutgoingCalledNumSubstIndex": hwVoOutgoingCalledNumSubstIndex,
       "hwVoOutgoingCalledNumSubstRowStatus": hwVoOutgoingCalledNumSubstRowStatus}
)
