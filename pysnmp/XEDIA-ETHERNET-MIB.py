# SNMP MIB module (XEDIA-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:50 2024
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

(dot3StatsEntry,) = mibBuilder.importSymbols(
    "EtherLike-MIB",
    "dot3StatsEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xdot3Objects_ObjectIdentity = ObjectIdentity
xdot3Objects = _Xdot3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1)
)
_Xdot3StatsTable_Object = MibTable
xdot3StatsTable = _Xdot3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xdot3StatsTable.setStatus("current")
_Xdot3StatsEntry_Object = MibTableRow
xdot3StatsEntry = _Xdot3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xdot3StatsEntry.setStatus("current")
_Xdot3StatsOutUnderflows_Type = Counter32
_Xdot3StatsOutUnderflows_Object = MibTableColumn
xdot3StatsOutUnderflows = _Xdot3StatsOutUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 1),
    _Xdot3StatsOutUnderflows_Type()
)
xdot3StatsOutUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsOutUnderflows.setStatus("current")
_Xdot3StatsOutNoCarriers_Type = Counter32
_Xdot3StatsOutNoCarriers_Object = MibTableColumn
xdot3StatsOutNoCarriers = _Xdot3StatsOutNoCarriers_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 2),
    _Xdot3StatsOutNoCarriers_Type()
)
xdot3StatsOutNoCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsOutNoCarriers.setStatus("current")
_Xdot3StatsOutCarrierLosses_Type = Counter32
_Xdot3StatsOutCarrierLosses_Object = MibTableColumn
xdot3StatsOutCarrierLosses = _Xdot3StatsOutCarrierLosses_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 3),
    _Xdot3StatsOutCarrierLosses_Type()
)
xdot3StatsOutCarrierLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsOutCarrierLosses.setStatus("current")
_Xdot3StatsOutJabberTimeouts_Type = Counter32
_Xdot3StatsOutJabberTimeouts_Object = MibTableColumn
xdot3StatsOutJabberTimeouts = _Xdot3StatsOutJabberTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 4),
    _Xdot3StatsOutJabberTimeouts_Type()
)
xdot3StatsOutJabberTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsOutJabberTimeouts.setStatus("current")
_Xdot3StatsOutTotalCollisions_Type = Counter32
_Xdot3StatsOutTotalCollisions_Object = MibTableColumn
xdot3StatsOutTotalCollisions = _Xdot3StatsOutTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 5),
    _Xdot3StatsOutTotalCollisions_Type()
)
xdot3StatsOutTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsOutTotalCollisions.setStatus("current")
_Xdot3StatsInDescriptorErrors_Type = Counter32
_Xdot3StatsInDescriptorErrors_Object = MibTableColumn
xdot3StatsInDescriptorErrors = _Xdot3StatsInDescriptorErrors_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 6),
    _Xdot3StatsInDescriptorErrors_Type()
)
xdot3StatsInDescriptorErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsInDescriptorErrors.setStatus("current")
_Xdot3StatsInRunts_Type = Counter32
_Xdot3StatsInRunts_Object = MibTableColumn
xdot3StatsInRunts = _Xdot3StatsInRunts_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 7),
    _Xdot3StatsInRunts_Type()
)
xdot3StatsInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsInRunts.setStatus("current")
_Xdot3StatsInTotalCollisions_Type = Counter32
_Xdot3StatsInTotalCollisions_Object = MibTableColumn
xdot3StatsInTotalCollisions = _Xdot3StatsInTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 8),
    _Xdot3StatsInTotalCollisions_Type()
)
xdot3StatsInTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsInTotalCollisions.setStatus("current")
_Xdot3StatsInDribbles_Type = Counter32
_Xdot3StatsInDribbles_Object = MibTableColumn
xdot3StatsInDribbles = _Xdot3StatsInDribbles_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 9),
    _Xdot3StatsInDribbles_Type()
)
xdot3StatsInDribbles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsInDribbles.setStatus("current")
_Xdot3StatsInOverflows_Type = Counter32
_Xdot3StatsInOverflows_Object = MibTableColumn
xdot3StatsInOverflows = _Xdot3StatsInOverflows_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 10),
    _Xdot3StatsInOverflows_Type()
)
xdot3StatsInOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsInOverflows.setStatus("current")
_Xdot3StatsInV1EthFrames_Type = Counter32
_Xdot3StatsInV1EthFrames_Object = MibTableColumn
xdot3StatsInV1EthFrames = _Xdot3StatsInV1EthFrames_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 11),
    _Xdot3StatsInV1EthFrames_Type()
)
xdot3StatsInV1EthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsInV1EthFrames.setStatus("current")
_Xdot3StatsInV2Dot3Frames_Type = Counter32
_Xdot3StatsInV2Dot3Frames_Object = MibTableColumn
xdot3StatsInV2Dot3Frames = _Xdot3StatsInV2Dot3Frames_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 12),
    _Xdot3StatsInV2Dot3Frames_Type()
)
xdot3StatsInV2Dot3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsInV2Dot3Frames.setStatus("current")
_Xdot3StatsInMissedFrames_Type = Counter32
_Xdot3StatsInMissedFrames_Object = MibTableColumn
xdot3StatsInMissedFrames = _Xdot3StatsInMissedFrames_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 13),
    _Xdot3StatsInMissedFrames_Type()
)
xdot3StatsInMissedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3StatsInMissedFrames.setStatus("current")


class _Xdot3NegotiatedConfigSpeed_Type(Integer32):
    """Custom type xdot3NegotiatedConfigSpeed based on Integer32"""
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
        *(("gbps1", 3),
          ("mbps10", 1),
          ("mbps100", 2),
          ("unknown", 4))
    )


_Xdot3NegotiatedConfigSpeed_Type.__name__ = "Integer32"
_Xdot3NegotiatedConfigSpeed_Object = MibTableColumn
xdot3NegotiatedConfigSpeed = _Xdot3NegotiatedConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 14),
    _Xdot3NegotiatedConfigSpeed_Type()
)
xdot3NegotiatedConfigSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3NegotiatedConfigSpeed.setStatus("current")


class _Xdot3NegotiatedConfigDuplexMode_Type(Integer32):
    """Custom type xdot3NegotiatedConfigDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("unknown", 3))
    )


_Xdot3NegotiatedConfigDuplexMode_Type.__name__ = "Integer32"
_Xdot3NegotiatedConfigDuplexMode_Object = MibTableColumn
xdot3NegotiatedConfigDuplexMode = _Xdot3NegotiatedConfigDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 15),
    _Xdot3NegotiatedConfigDuplexMode_Type()
)
xdot3NegotiatedConfigDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3NegotiatedConfigDuplexMode.setStatus("current")


class _Xdot3NegotiatedFlowControl_Type(Integer32):
    """Custom type xdot3NegotiatedFlowControl based on Integer32"""
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
        *(("disabled", 1),
          ("enabledRcv", 3),
          ("enabledXmit", 2),
          ("enabledXmitAndRcv", 4),
          ("unknown", 5))
    )


_Xdot3NegotiatedFlowControl_Type.__name__ = "Integer32"
_Xdot3NegotiatedFlowControl_Object = MibTableColumn
xdot3NegotiatedFlowControl = _Xdot3NegotiatedFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 16),
    _Xdot3NegotiatedFlowControl_Type()
)
xdot3NegotiatedFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3NegotiatedFlowControl.setStatus("current")


class _Xdot3IfOperStatus_Type(Integer32):
    """Custom type xdot3IfOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_Xdot3IfOperStatus_Type.__name__ = "Integer32"
_Xdot3IfOperStatus_Object = MibTableColumn
xdot3IfOperStatus = _Xdot3IfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 17),
    _Xdot3IfOperStatus_Type()
)
xdot3IfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3IfOperStatus.setStatus("current")
_Xdot3ConfigTable_Object = MibTable
xdot3ConfigTable = _Xdot3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xdot3ConfigTable.setStatus("current")
_Xdot3ConfigEntry_Object = MibTableRow
xdot3ConfigEntry = _Xdot3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xdot3ConfigEntry.setStatus("current")


class _Xdot3ConfigSpeed_Type(Integer32):
    """Custom type xdot3ConfigSpeed based on Integer32"""
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
        *(("gbps1", 3),
          ("mbps10", 1),
          ("mbps100", 2))
    )


_Xdot3ConfigSpeed_Type.__name__ = "Integer32"
_Xdot3ConfigSpeed_Object = MibTableColumn
xdot3ConfigSpeed = _Xdot3ConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1, 1),
    _Xdot3ConfigSpeed_Type()
)
xdot3ConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdot3ConfigSpeed.setStatus("current")


class _Xdot3ConfigDuplexMode_Type(Integer32):
    """Custom type xdot3ConfigDuplexMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_Xdot3ConfigDuplexMode_Type.__name__ = "Integer32"
_Xdot3ConfigDuplexMode_Object = MibTableColumn
xdot3ConfigDuplexMode = _Xdot3ConfigDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1, 2),
    _Xdot3ConfigDuplexMode_Type()
)
xdot3ConfigDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdot3ConfigDuplexMode.setStatus("current")


class _Xdot3ConfigMedia_Type(Integer32):
    """Custom type xdot3ConfigMedia based on Integer32"""
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
        *(("fx", 2),
          ("lx", 4),
          ("sx", 3),
          ("tx", 1))
    )


_Xdot3ConfigMedia_Type.__name__ = "Integer32"
_Xdot3ConfigMedia_Object = MibTableColumn
xdot3ConfigMedia = _Xdot3ConfigMedia_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1, 3),
    _Xdot3ConfigMedia_Type()
)
xdot3ConfigMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdot3ConfigMedia.setStatus("current")


class _Xdot3ConfigCaptureEffectResol_Type(Integer32):
    """Custom type xdot3ConfigCaptureEffectResol based on Integer32"""
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


_Xdot3ConfigCaptureEffectResol_Type.__name__ = "Integer32"
_Xdot3ConfigCaptureEffectResol_Object = MibTableColumn
xdot3ConfigCaptureEffectResol = _Xdot3ConfigCaptureEffectResol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1, 4),
    _Xdot3ConfigCaptureEffectResol_Type()
)
xdot3ConfigCaptureEffectResol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdot3ConfigCaptureEffectResol.setStatus("current")


class _Xdot3ConfigAutoNegotiate_Type(Integer32):
    """Custom type xdot3ConfigAutoNegotiate based on Integer32"""
    defaultValue = 1

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


_Xdot3ConfigAutoNegotiate_Type.__name__ = "Integer32"
_Xdot3ConfigAutoNegotiate_Object = MibTableColumn
xdot3ConfigAutoNegotiate = _Xdot3ConfigAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1, 5),
    _Xdot3ConfigAutoNegotiate_Type()
)
xdot3ConfigAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdot3ConfigAutoNegotiate.setStatus("current")
_Xdot3Conformance_ObjectIdentity = ObjectIdentity
xdot3Conformance = _Xdot3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 2)
)
_Xdot3Compliances_ObjectIdentity = ObjectIdentity
xdot3Compliances = _Xdot3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 2, 1)
)
_Xdot3Groups_ObjectIdentity = ObjectIdentity
xdot3Groups = _Xdot3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 2, 2)
)
dot3StatsEntry.registerAugmentions(
    ("XEDIA-ETHERNET-MIB",
     "xdot3StatsEntry")
)
xdot3StatsEntry.setIndexNames(*dot3StatsEntry.getIndexNames())
dot3StatsEntry.registerAugmentions(
    ("XEDIA-ETHERNET-MIB",
     "xdot3ConfigEntry")
)
xdot3ConfigEntry.setIndexNames(*dot3StatsEntry.getIndexNames())

# Managed Objects groups

xdot3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 2, 2, 1)
)
xdot3Group.setObjects(
      *(("XEDIA-ETHERNET-MIB", "xdot3StatsOutUnderflows"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsOutNoCarriers"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsOutCarrierLosses"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsOutJabberTimeouts"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsOutTotalCollisions"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsInDescriptorErrors"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsInRunts"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsInTotalCollisions"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsInDribbles"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsInOverflows"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsInV1EthFrames"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsInV2Dot3Frames"),
        ("XEDIA-ETHERNET-MIB", "xdot3StatsInMissedFrames"),
        ("XEDIA-ETHERNET-MIB", "xdot3ConfigSpeed"),
        ("XEDIA-ETHERNET-MIB", "xdot3ConfigDuplexMode"),
        ("XEDIA-ETHERNET-MIB", "xdot3ConfigMedia"),
        ("XEDIA-ETHERNET-MIB", "xdot3ConfigCaptureEffectResol"),
        ("XEDIA-ETHERNET-MIB", "xdot3ConfigAutoNegotiate"),
        ("XEDIA-ETHERNET-MIB", "xdot3NegotiatedConfigSpeed"),
        ("XEDIA-ETHERNET-MIB", "xdot3NegotiatedConfigDuplexMode"),
        ("XEDIA-ETHERNET-MIB", "xdot3NegotiatedFlowControl"),
        ("XEDIA-ETHERNET-MIB", "xdot3IfOperStatus"))
)
if mibBuilder.loadTexts:
    xdot3Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xdot3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xdot3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-ETHERNET-MIB",
    **{"xediaEthernetMIB": xediaEthernetMIB,
       "xdot3Objects": xdot3Objects,
       "xdot3StatsTable": xdot3StatsTable,
       "xdot3StatsEntry": xdot3StatsEntry,
       "xdot3StatsOutUnderflows": xdot3StatsOutUnderflows,
       "xdot3StatsOutNoCarriers": xdot3StatsOutNoCarriers,
       "xdot3StatsOutCarrierLosses": xdot3StatsOutCarrierLosses,
       "xdot3StatsOutJabberTimeouts": xdot3StatsOutJabberTimeouts,
       "xdot3StatsOutTotalCollisions": xdot3StatsOutTotalCollisions,
       "xdot3StatsInDescriptorErrors": xdot3StatsInDescriptorErrors,
       "xdot3StatsInRunts": xdot3StatsInRunts,
       "xdot3StatsInTotalCollisions": xdot3StatsInTotalCollisions,
       "xdot3StatsInDribbles": xdot3StatsInDribbles,
       "xdot3StatsInOverflows": xdot3StatsInOverflows,
       "xdot3StatsInV1EthFrames": xdot3StatsInV1EthFrames,
       "xdot3StatsInV2Dot3Frames": xdot3StatsInV2Dot3Frames,
       "xdot3StatsInMissedFrames": xdot3StatsInMissedFrames,
       "xdot3NegotiatedConfigSpeed": xdot3NegotiatedConfigSpeed,
       "xdot3NegotiatedConfigDuplexMode": xdot3NegotiatedConfigDuplexMode,
       "xdot3NegotiatedFlowControl": xdot3NegotiatedFlowControl,
       "xdot3IfOperStatus": xdot3IfOperStatus,
       "xdot3ConfigTable": xdot3ConfigTable,
       "xdot3ConfigEntry": xdot3ConfigEntry,
       "xdot3ConfigSpeed": xdot3ConfigSpeed,
       "xdot3ConfigDuplexMode": xdot3ConfigDuplexMode,
       "xdot3ConfigMedia": xdot3ConfigMedia,
       "xdot3ConfigCaptureEffectResol": xdot3ConfigCaptureEffectResol,
       "xdot3ConfigAutoNegotiate": xdot3ConfigAutoNegotiate,
       "xdot3Conformance": xdot3Conformance,
       "xdot3Compliances": xdot3Compliances,
       "xdot3Compliance": xdot3Compliance,
       "xdot3Groups": xdot3Groups,
       "xdot3Group": xdot3Group}
)
