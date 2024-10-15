# SNMP MIB module (EXTREME-POS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(PortList,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "PortList",
    "extremeAgent")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremePOSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeAps_ObjectIdentity = ObjectIdentity
extremeAps = _ExtremeAps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1)
)
_ExtremeApsConfig_ObjectIdentity = ObjectIdentity
extremeApsConfig = _ExtremeApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1)
)
_ExtremeApsConfigEnabled_Type = TruthValue
_ExtremeApsConfigEnabled_Object = MibScalar
extremeApsConfigEnabled = _ExtremeApsConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 1),
    _ExtremeApsConfigEnabled_Type()
)
extremeApsConfigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsConfigEnabled.setStatus("current")
_ExtremeApsGroupConfigTable_Object = MibTable
extremeApsGroupConfigTable = _ExtremeApsGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 2)
)
if mibBuilder.loadTexts:
    extremeApsGroupConfigTable.setStatus("current")
_ExtremeApsGroupConfigEntry_Object = MibTableRow
extremeApsGroupConfigEntry = _ExtremeApsGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 2, 1)
)
extremeApsGroupConfigEntry.setIndexNames(
    (0, "EXTREME-POS-MIB", "extremeApsGroupConfigGroupNumber"),
)
if mibBuilder.loadTexts:
    extremeApsGroupConfigEntry.setStatus("current")


class _ExtremeApsGroupConfigGroupNumber_Type(Integer32):
    """Custom type extremeApsGroupConfigGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeApsGroupConfigGroupNumber_Type.__name__ = "Integer32"
_ExtremeApsGroupConfigGroupNumber_Object = MibTableColumn
extremeApsGroupConfigGroupNumber = _ExtremeApsGroupConfigGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 2, 1, 1),
    _ExtremeApsGroupConfigGroupNumber_Type()
)
extremeApsGroupConfigGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupConfigGroupNumber.setStatus("current")


class _ExtremeApsGroupConfigRevertMode_Type(Integer32):
    """Custom type extremeApsGroupConfigRevertMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 2),
          ("revertive", 1))
    )


_ExtremeApsGroupConfigRevertMode_Type.__name__ = "Integer32"
_ExtremeApsGroupConfigRevertMode_Object = MibTableColumn
extremeApsGroupConfigRevertMode = _ExtremeApsGroupConfigRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 2, 1, 2),
    _ExtremeApsGroupConfigRevertMode_Type()
)
extremeApsGroupConfigRevertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupConfigRevertMode.setStatus("current")


class _ExtremeApsGroupConfigRevertMinutes_Type(Integer32):
    """Custom type extremeApsGroupConfigRevertMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ExtremeApsGroupConfigRevertMinutes_Type.__name__ = "Integer32"
_ExtremeApsGroupConfigRevertMinutes_Object = MibTableColumn
extremeApsGroupConfigRevertMinutes = _ExtremeApsGroupConfigRevertMinutes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 2, 1, 3),
    _ExtremeApsGroupConfigRevertMinutes_Type()
)
extremeApsGroupConfigRevertMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupConfigRevertMinutes.setStatus("current")


class _ExtremeApsGroupConfigDirection_Type(Integer32):
    """Custom type extremeApsGroupConfigDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("unidirectional", 2))
    )


_ExtremeApsGroupConfigDirection_Type.__name__ = "Integer32"
_ExtremeApsGroupConfigDirection_Object = MibTableColumn
extremeApsGroupConfigDirection = _ExtremeApsGroupConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 2, 1, 4),
    _ExtremeApsGroupConfigDirection_Type()
)
extremeApsGroupConfigDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupConfigDirection.setStatus("current")
_ExtremeApsGroupConfigTimerInterval_Type = Integer32
_ExtremeApsGroupConfigTimerInterval_Object = MibTableColumn
extremeApsGroupConfigTimerInterval = _ExtremeApsGroupConfigTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 2, 1, 5),
    _ExtremeApsGroupConfigTimerInterval_Type()
)
extremeApsGroupConfigTimerInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupConfigTimerInterval.setStatus("current")
_ExtremeApsGroupConfigTimerMisses_Type = Integer32
_ExtremeApsGroupConfigTimerMisses_Object = MibTableColumn
extremeApsGroupConfigTimerMisses = _ExtremeApsGroupConfigTimerMisses_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 2, 1, 6),
    _ExtremeApsGroupConfigTimerMisses_Type()
)
extremeApsGroupConfigTimerMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupConfigTimerMisses.setStatus("current")
_ExtremeApsGroupConfigAuthenticate_Type = TruthValue
_ExtremeApsGroupConfigAuthenticate_Object = MibTableColumn
extremeApsGroupConfigAuthenticate = _ExtremeApsGroupConfigAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 2, 1, 7),
    _ExtremeApsGroupConfigAuthenticate_Type()
)
extremeApsGroupConfigAuthenticate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupConfigAuthenticate.setStatus("current")


class _ExtremeApsGroupConfigAuthString_Type(DisplayString):
    """Custom type extremeApsGroupConfigAuthString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExtremeApsGroupConfigAuthString_Type.__name__ = "DisplayString"
_ExtremeApsGroupConfigAuthString_Object = MibTableColumn
extremeApsGroupConfigAuthString = _ExtremeApsGroupConfigAuthString_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 2, 1, 8),
    _ExtremeApsGroupConfigAuthString_Type()
)
extremeApsGroupConfigAuthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupConfigAuthString.setStatus("current")
_ExtremeApsPortConfigTable_Object = MibTable
extremeApsPortConfigTable = _ExtremeApsPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 3)
)
if mibBuilder.loadTexts:
    extremeApsPortConfigTable.setStatus("current")
_ExtremeApsPortConfigEntry_Object = MibTableRow
extremeApsPortConfigEntry = _ExtremeApsPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 3, 1)
)
extremeApsPortConfigEntry.setIndexNames(
    (0, "EXTREME-POS-MIB", "extremeApsPortConfigGroupNumber"),
    (0, "EXTREME-POS-MIB", "extremeApsPortConfigPortNumber"),
)
if mibBuilder.loadTexts:
    extremeApsPortConfigEntry.setStatus("current")


class _ExtremeApsPortConfigGroupNumber_Type(Integer32):
    """Custom type extremeApsPortConfigGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeApsPortConfigGroupNumber_Type.__name__ = "Integer32"
_ExtremeApsPortConfigGroupNumber_Object = MibTableColumn
extremeApsPortConfigGroupNumber = _ExtremeApsPortConfigGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 3, 1, 1),
    _ExtremeApsPortConfigGroupNumber_Type()
)
extremeApsPortConfigGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsPortConfigGroupNumber.setStatus("current")
_ExtremeApsPortConfigPortNumber_Type = Integer32
_ExtremeApsPortConfigPortNumber_Object = MibTableColumn
extremeApsPortConfigPortNumber = _ExtremeApsPortConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 3, 1, 2),
    _ExtremeApsPortConfigPortNumber_Type()
)
extremeApsPortConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsPortConfigPortNumber.setStatus("current")


class _ExtremeApsPortConfigPortType_Type(Integer32):
    """Custom type extremeApsPortConfigPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protection", 2),
          ("working", 1))
    )


_ExtremeApsPortConfigPortType_Type.__name__ = "Integer32"
_ExtremeApsPortConfigPortType_Object = MibTableColumn
extremeApsPortConfigPortType = _ExtremeApsPortConfigPortType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 3, 1, 3),
    _ExtremeApsPortConfigPortType_Type()
)
extremeApsPortConfigPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsPortConfigPortType.setStatus("current")
_ExtremeApsProtectPortConfigTable_Object = MibTable
extremeApsProtectPortConfigTable = _ExtremeApsProtectPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 4)
)
if mibBuilder.loadTexts:
    extremeApsProtectPortConfigTable.setStatus("current")
_ExtremeApsProtectPortConfigEntry_Object = MibTableRow
extremeApsProtectPortConfigEntry = _ExtremeApsProtectPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 4, 1)
)
extremeApsProtectPortConfigEntry.setIndexNames(
    (0, "EXTREME-POS-MIB", "extremeApsProtectPortConfigGroupNumber"),
    (0, "EXTREME-POS-MIB", "extremeApsProtectPortConfigPortNumber"),
)
if mibBuilder.loadTexts:
    extremeApsProtectPortConfigEntry.setStatus("current")


class _ExtremeApsProtectPortConfigGroupNumber_Type(Integer32):
    """Custom type extremeApsProtectPortConfigGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeApsProtectPortConfigGroupNumber_Type.__name__ = "Integer32"
_ExtremeApsProtectPortConfigGroupNumber_Object = MibTableColumn
extremeApsProtectPortConfigGroupNumber = _ExtremeApsProtectPortConfigGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 4, 1, 1),
    _ExtremeApsProtectPortConfigGroupNumber_Type()
)
extremeApsProtectPortConfigGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortConfigGroupNumber.setStatus("current")
_ExtremeApsProtectPortConfigPortNumber_Type = Integer32
_ExtremeApsProtectPortConfigPortNumber_Object = MibTableColumn
extremeApsProtectPortConfigPortNumber = _ExtremeApsProtectPortConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 4, 1, 2),
    _ExtremeApsProtectPortConfigPortNumber_Type()
)
extremeApsProtectPortConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortConfigPortNumber.setStatus("current")
_ExtremeApsProtectPortConfigWorkingIpAddr_Type = IpAddress
_ExtremeApsProtectPortConfigWorkingIpAddr_Object = MibTableColumn
extremeApsProtectPortConfigWorkingIpAddr = _ExtremeApsProtectPortConfigWorkingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 1, 4, 1, 3),
    _ExtremeApsProtectPortConfigWorkingIpAddr_Type()
)
extremeApsProtectPortConfigWorkingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortConfigWorkingIpAddr.setStatus("current")
_ExtremeApsStatus_ObjectIdentity = ObjectIdentity
extremeApsStatus = _ExtremeApsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2)
)
_ExtremeApsGroupTable_Object = MibTable
extremeApsGroupTable = _ExtremeApsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    extremeApsGroupTable.setStatus("current")
_ExtremeApsGroupEntry_Object = MibTableRow
extremeApsGroupEntry = _ExtremeApsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 1, 1)
)
extremeApsGroupEntry.setIndexNames(
    (0, "EXTREME-POS-MIB", "extremeApsGroupGroupNumber"),
)
if mibBuilder.loadTexts:
    extremeApsGroupEntry.setStatus("current")


class _ExtremeApsGroupGroupNumber_Type(Integer32):
    """Custom type extremeApsGroupGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeApsGroupGroupNumber_Type.__name__ = "Integer32"
_ExtremeApsGroupGroupNumber_Object = MibTableColumn
extremeApsGroupGroupNumber = _ExtremeApsGroupGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 1, 1, 1),
    _ExtremeApsGroupGroupNumber_Type()
)
extremeApsGroupGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupGroupNumber.setStatus("current")


class _ExtremeApsGroupActivePort_Type(Integer32):
    """Custom type extremeApsGroupActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protection", 2),
          ("working", 1))
    )


_ExtremeApsGroupActivePort_Type.__name__ = "Integer32"
_ExtremeApsGroupActivePort_Object = MibTableColumn
extremeApsGroupActivePort = _ExtremeApsGroupActivePort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 1, 1, 2),
    _ExtremeApsGroupActivePort_Type()
)
extremeApsGroupActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupActivePort.setStatus("current")


class _ExtremeApsGroupEffectiveDirection_Type(Integer32):
    """Custom type extremeApsGroupEffectiveDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("unidirectional", 2))
    )


_ExtremeApsGroupEffectiveDirection_Type.__name__ = "Integer32"
_ExtremeApsGroupEffectiveDirection_Object = MibTableColumn
extremeApsGroupEffectiveDirection = _ExtremeApsGroupEffectiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 1, 1, 3),
    _ExtremeApsGroupEffectiveDirection_Type()
)
extremeApsGroupEffectiveDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupEffectiveDirection.setStatus("current")


class _ExtremeApsGroupPeerProtoStatus_Type(Integer32):
    """Custom type extremeApsGroupPeerProtoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("established", 1))
    )


_ExtremeApsGroupPeerProtoStatus_Type.__name__ = "Integer32"
_ExtremeApsGroupPeerProtoStatus_Object = MibTableColumn
extremeApsGroupPeerProtoStatus = _ExtremeApsGroupPeerProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 1, 1, 4),
    _ExtremeApsGroupPeerProtoStatus_Type()
)
extremeApsGroupPeerProtoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsGroupPeerProtoStatus.setStatus("current")
_ExtremeApsProtectPortTable_Object = MibTable
extremeApsProtectPortTable = _ExtremeApsProtectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2)
)
if mibBuilder.loadTexts:
    extremeApsProtectPortTable.setStatus("current")
_ExtremeApsProtectPortEntry_Object = MibTableRow
extremeApsProtectPortEntry = _ExtremeApsProtectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1)
)
extremeApsProtectPortEntry.setIndexNames(
    (0, "EXTREME-POS-MIB", "extremeApsProtectPortGroupNumber"),
    (0, "EXTREME-POS-MIB", "extremeApsProtectPortPortNumber"),
)
if mibBuilder.loadTexts:
    extremeApsProtectPortEntry.setStatus("current")


class _ExtremeApsProtectPortGroupNumber_Type(Integer32):
    """Custom type extremeApsProtectPortGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeApsProtectPortGroupNumber_Type.__name__ = "Integer32"
_ExtremeApsProtectPortGroupNumber_Object = MibTableColumn
extremeApsProtectPortGroupNumber = _ExtremeApsProtectPortGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 1),
    _ExtremeApsProtectPortGroupNumber_Type()
)
extremeApsProtectPortGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortGroupNumber.setStatus("current")
_ExtremeApsProtectPortPortNumber_Type = Integer32
_ExtremeApsProtectPortPortNumber_Object = MibTableColumn
extremeApsProtectPortPortNumber = _ExtremeApsProtectPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 2),
    _ExtremeApsProtectPortPortNumber_Type()
)
extremeApsProtectPortPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortPortNumber.setStatus("current")


class _ExtremeApsProtectPortTransmitK1_Type(OctetString):
    """Custom type extremeApsProtectPortTransmitK1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExtremeApsProtectPortTransmitK1_Type.__name__ = "OctetString"
_ExtremeApsProtectPortTransmitK1_Object = MibTableColumn
extremeApsProtectPortTransmitK1 = _ExtremeApsProtectPortTransmitK1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 3),
    _ExtremeApsProtectPortTransmitK1_Type()
)
extremeApsProtectPortTransmitK1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortTransmitK1.setStatus("current")


class _ExtremeApsProtectPortTransmitK2_Type(OctetString):
    """Custom type extremeApsProtectPortTransmitK2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExtremeApsProtectPortTransmitK2_Type.__name__ = "OctetString"
_ExtremeApsProtectPortTransmitK2_Object = MibTableColumn
extremeApsProtectPortTransmitK2 = _ExtremeApsProtectPortTransmitK2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 4),
    _ExtremeApsProtectPortTransmitK2_Type()
)
extremeApsProtectPortTransmitK2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortTransmitK2.setStatus("current")


class _ExtremeApsProtectPortReceiveK1_Type(OctetString):
    """Custom type extremeApsProtectPortReceiveK1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExtremeApsProtectPortReceiveK1_Type.__name__ = "OctetString"
_ExtremeApsProtectPortReceiveK1_Object = MibTableColumn
extremeApsProtectPortReceiveK1 = _ExtremeApsProtectPortReceiveK1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 5),
    _ExtremeApsProtectPortReceiveK1_Type()
)
extremeApsProtectPortReceiveK1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortReceiveK1.setStatus("current")


class _ExtremeApsProtectPortReceiveK2_Type(OctetString):
    """Custom type extremeApsProtectPortReceiveK2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExtremeApsProtectPortReceiveK2_Type.__name__ = "OctetString"
_ExtremeApsProtectPortReceiveK2_Object = MibTableColumn
extremeApsProtectPortReceiveK2 = _ExtremeApsProtectPortReceiveK2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 6),
    _ExtremeApsProtectPortReceiveK2_Type()
)
extremeApsProtectPortReceiveK2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortReceiveK2.setStatus("current")
_ExtremeApsProtectPortSwitchInitByWorking_Type = Integer32
_ExtremeApsProtectPortSwitchInitByWorking_Object = MibTableColumn
extremeApsProtectPortSwitchInitByWorking = _ExtremeApsProtectPortSwitchInitByWorking_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 7),
    _ExtremeApsProtectPortSwitchInitByWorking_Type()
)
extremeApsProtectPortSwitchInitByWorking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortSwitchInitByWorking.setStatus("current")
_ExtremeApsProtectPortSwitchInitByProtect_Type = Integer32
_ExtremeApsProtectPortSwitchInitByProtect_Object = MibTableColumn
extremeApsProtectPortSwitchInitByProtect = _ExtremeApsProtectPortSwitchInitByProtect_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 8),
    _ExtremeApsProtectPortSwitchInitByProtect_Type()
)
extremeApsProtectPortSwitchInitByProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortSwitchInitByProtect.setStatus("current")
_ExtremeApsProtectPortSwitchInitByADM_Type = Integer32
_ExtremeApsProtectPortSwitchInitByADM_Object = MibTableColumn
extremeApsProtectPortSwitchInitByADM = _ExtremeApsProtectPortSwitchInitByADM_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 9),
    _ExtremeApsProtectPortSwitchInitByADM_Type()
)
extremeApsProtectPortSwitchInitByADM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortSwitchInitByADM.setStatus("current")
_ExtremeApsProtectPortSwitchInitByCmd_Type = Integer32
_ExtremeApsProtectPortSwitchInitByCmd_Object = MibTableColumn
extremeApsProtectPortSwitchInitByCmd = _ExtremeApsProtectPortSwitchInitByCmd_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 10),
    _ExtremeApsProtectPortSwitchInitByCmd_Type()
)
extremeApsProtectPortSwitchInitByCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortSwitchInitByCmd.setStatus("current")
_ExtremeApsProtectPortSuccessfulSwitches_Type = Integer32
_ExtremeApsProtectPortSuccessfulSwitches_Object = MibTableColumn
extremeApsProtectPortSuccessfulSwitches = _ExtremeApsProtectPortSuccessfulSwitches_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 11),
    _ExtremeApsProtectPortSuccessfulSwitches_Type()
)
extremeApsProtectPortSuccessfulSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortSuccessfulSwitches.setStatus("current")
_ExtremeApsProtectPortHelloProtFails_Type = Integer32
_ExtremeApsProtectPortHelloProtFails_Object = MibTableColumn
extremeApsProtectPortHelloProtFails = _ExtremeApsProtectPortHelloProtFails_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 2, 2, 1, 12),
    _ExtremeApsProtectPortHelloProtFails_Type()
)
extremeApsProtectPortHelloProtFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtectPortHelloProtFails.setStatus("current")
_ExtremeApsErrors_ObjectIdentity = ObjectIdentity
extremeApsErrors = _ExtremeApsErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3)
)
_ExtremeApsLineErrorTable_Object = MibTable
extremeApsLineErrorTable = _ExtremeApsLineErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1)
)
if mibBuilder.loadTexts:
    extremeApsLineErrorTable.setStatus("current")
_ExtremeApsLineErrorEntry_Object = MibTableRow
extremeApsLineErrorEntry = _ExtremeApsLineErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1)
)
extremeApsLineErrorEntry.setIndexNames(
    (0, "EXTREME-POS-MIB", "extremeApsLineErrorGroupNumber"),
    (0, "EXTREME-POS-MIB", "extremeApsLineErrorPortNumber"),
)
if mibBuilder.loadTexts:
    extremeApsLineErrorEntry.setStatus("current")


class _ExtremeApsLineErrorGroupNumber_Type(Integer32):
    """Custom type extremeApsLineErrorGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeApsLineErrorGroupNumber_Type.__name__ = "Integer32"
_ExtremeApsLineErrorGroupNumber_Object = MibTableColumn
extremeApsLineErrorGroupNumber = _ExtremeApsLineErrorGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1, 1),
    _ExtremeApsLineErrorGroupNumber_Type()
)
extremeApsLineErrorGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsLineErrorGroupNumber.setStatus("current")
_ExtremeApsLineErrorPortNumber_Type = Integer32
_ExtremeApsLineErrorPortNumber_Object = MibTableColumn
extremeApsLineErrorPortNumber = _ExtremeApsLineErrorPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1, 2),
    _ExtremeApsLineErrorPortNumber_Type()
)
extremeApsLineErrorPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsLineErrorPortNumber.setStatus("current")
_ExtremeApsLineErrorSignalDegradeActive_Type = TruthValue
_ExtremeApsLineErrorSignalDegradeActive_Object = MibTableColumn
extremeApsLineErrorSignalDegradeActive = _ExtremeApsLineErrorSignalDegradeActive_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1, 3),
    _ExtremeApsLineErrorSignalDegradeActive_Type()
)
extremeApsLineErrorSignalDegradeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsLineErrorSignalDegradeActive.setStatus("current")
_ExtremeApsLineErrorBERSignalDegradeActive_Type = TruthValue
_ExtremeApsLineErrorBERSignalDegradeActive_Object = MibTableColumn
extremeApsLineErrorBERSignalDegradeActive = _ExtremeApsLineErrorBERSignalDegradeActive_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1, 4),
    _ExtremeApsLineErrorBERSignalDegradeActive_Type()
)
extremeApsLineErrorBERSignalDegradeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsLineErrorBERSignalDegradeActive.setStatus("current")
_ExtremeApsLineErrorSignalFailActive_Type = TruthValue
_ExtremeApsLineErrorSignalFailActive_Object = MibTableColumn
extremeApsLineErrorSignalFailActive = _ExtremeApsLineErrorSignalFailActive_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1, 5),
    _ExtremeApsLineErrorSignalFailActive_Type()
)
extremeApsLineErrorSignalFailActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsLineErrorSignalFailActive.setStatus("current")
_ExtremeApsLineErrorBERSignalFailActive_Type = TruthValue
_ExtremeApsLineErrorBERSignalFailActive_Object = MibTableColumn
extremeApsLineErrorBERSignalFailActive = _ExtremeApsLineErrorBERSignalFailActive_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1, 6),
    _ExtremeApsLineErrorBERSignalFailActive_Type()
)
extremeApsLineErrorBERSignalFailActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsLineErrorBERSignalFailActive.setStatus("current")
_ExtremeApsLineErrorSignalDegrades_Type = Integer32
_ExtremeApsLineErrorSignalDegrades_Object = MibTableColumn
extremeApsLineErrorSignalDegrades = _ExtremeApsLineErrorSignalDegrades_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1, 7),
    _ExtremeApsLineErrorSignalDegrades_Type()
)
extremeApsLineErrorSignalDegrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsLineErrorSignalDegrades.setStatus("current")
_ExtremeApsLineErrorBERSignalDegrades_Type = Integer32
_ExtremeApsLineErrorBERSignalDegrades_Object = MibTableColumn
extremeApsLineErrorBERSignalDegrades = _ExtremeApsLineErrorBERSignalDegrades_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1, 8),
    _ExtremeApsLineErrorBERSignalDegrades_Type()
)
extremeApsLineErrorBERSignalDegrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsLineErrorBERSignalDegrades.setStatus("current")
_ExtremeApsLineErrorSignalFails_Type = Integer32
_ExtremeApsLineErrorSignalFails_Object = MibTableColumn
extremeApsLineErrorSignalFails = _ExtremeApsLineErrorSignalFails_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1, 9),
    _ExtremeApsLineErrorSignalFails_Type()
)
extremeApsLineErrorSignalFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsLineErrorSignalFails.setStatus("current")
_ExtremeApsLineErrorBERSignalFails_Type = Integer32
_ExtremeApsLineErrorBERSignalFails_Object = MibTableColumn
extremeApsLineErrorBERSignalFails = _ExtremeApsLineErrorBERSignalFails_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 1, 1, 10),
    _ExtremeApsLineErrorBERSignalFails_Type()
)
extremeApsLineErrorBERSignalFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsLineErrorBERSignalFails.setStatus("current")
_ExtremeApsProtocolErrorTable_Object = MibTable
extremeApsProtocolErrorTable = _ExtremeApsProtocolErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2)
)
if mibBuilder.loadTexts:
    extremeApsProtocolErrorTable.setStatus("current")
_ExtremeApsProtocolErrorEntry_Object = MibTableRow
extremeApsProtocolErrorEntry = _ExtremeApsProtocolErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1)
)
extremeApsProtocolErrorEntry.setIndexNames(
    (0, "EXTREME-POS-MIB", "extremeApsProtocolErrorGroupNumber"),
    (0, "EXTREME-POS-MIB", "extremeApsProtocolErrorPortNumber"),
)
if mibBuilder.loadTexts:
    extremeApsProtocolErrorEntry.setStatus("current")


class _ExtremeApsProtocolErrorGroupNumber_Type(Integer32):
    """Custom type extremeApsProtocolErrorGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeApsProtocolErrorGroupNumber_Type.__name__ = "Integer32"
_ExtremeApsProtocolErrorGroupNumber_Object = MibTableColumn
extremeApsProtocolErrorGroupNumber = _ExtremeApsProtocolErrorGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 1),
    _ExtremeApsProtocolErrorGroupNumber_Type()
)
extremeApsProtocolErrorGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorGroupNumber.setStatus("current")
_ExtremeApsProtocolErrorPortNumber_Type = Integer32
_ExtremeApsProtocolErrorPortNumber_Object = MibTableColumn
extremeApsProtocolErrorPortNumber = _ExtremeApsProtocolErrorPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 2),
    _ExtremeApsProtocolErrorPortNumber_Type()
)
extremeApsProtocolErrorPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorPortNumber.setStatus("current")
_ExtremeApsProtocolErrorModeMismatchDefect_Type = TruthValue
_ExtremeApsProtocolErrorModeMismatchDefect_Object = MibTableColumn
extremeApsProtocolErrorModeMismatchDefect = _ExtremeApsProtocolErrorModeMismatchDefect_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 3),
    _ExtremeApsProtocolErrorModeMismatchDefect_Type()
)
extremeApsProtocolErrorModeMismatchDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorModeMismatchDefect.setStatus("current")
_ExtremeApsProtocolErrorProtSwitchByteDefect_Type = TruthValue
_ExtremeApsProtocolErrorProtSwitchByteDefect_Object = MibTableColumn
extremeApsProtocolErrorProtSwitchByteDefect = _ExtremeApsProtocolErrorProtSwitchByteDefect_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 4),
    _ExtremeApsProtocolErrorProtSwitchByteDefect_Type()
)
extremeApsProtocolErrorProtSwitchByteDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorProtSwitchByteDefect.setStatus("current")
_ExtremeApsProtocolErrorChannelMismatchDefect_Type = TruthValue
_ExtremeApsProtocolErrorChannelMismatchDefect_Object = MibTableColumn
extremeApsProtocolErrorChannelMismatchDefect = _ExtremeApsProtocolErrorChannelMismatchDefect_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 5),
    _ExtremeApsProtocolErrorChannelMismatchDefect_Type()
)
extremeApsProtocolErrorChannelMismatchDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorChannelMismatchDefect.setStatus("current")
_ExtremeApsProtocolErrorFarEndProtectDefect_Type = TruthValue
_ExtremeApsProtocolErrorFarEndProtectDefect_Object = MibTableColumn
extremeApsProtocolErrorFarEndProtectDefect = _ExtremeApsProtocolErrorFarEndProtectDefect_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 6),
    _ExtremeApsProtocolErrorFarEndProtectDefect_Type()
)
extremeApsProtocolErrorFarEndProtectDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorFarEndProtectDefect.setStatus("current")
_ExtremeApsProtocolErrorModeMismatchFailure_Type = TruthValue
_ExtremeApsProtocolErrorModeMismatchFailure_Object = MibTableColumn
extremeApsProtocolErrorModeMismatchFailure = _ExtremeApsProtocolErrorModeMismatchFailure_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 7),
    _ExtremeApsProtocolErrorModeMismatchFailure_Type()
)
extremeApsProtocolErrorModeMismatchFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorModeMismatchFailure.setStatus("current")
_ExtremeApsProtocolErrorProtSwitchByteFailure_Type = TruthValue
_ExtremeApsProtocolErrorProtSwitchByteFailure_Object = MibTableColumn
extremeApsProtocolErrorProtSwitchByteFailure = _ExtremeApsProtocolErrorProtSwitchByteFailure_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 8),
    _ExtremeApsProtocolErrorProtSwitchByteFailure_Type()
)
extremeApsProtocolErrorProtSwitchByteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorProtSwitchByteFailure.setStatus("current")
_ExtremeApsProtocolErrorChannelMismatchFailure_Type = TruthValue
_ExtremeApsProtocolErrorChannelMismatchFailure_Object = MibTableColumn
extremeApsProtocolErrorChannelMismatchFailure = _ExtremeApsProtocolErrorChannelMismatchFailure_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 9),
    _ExtremeApsProtocolErrorChannelMismatchFailure_Type()
)
extremeApsProtocolErrorChannelMismatchFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorChannelMismatchFailure.setStatus("current")
_ExtremeApsProtocolErrorFarEndProtectFailure_Type = TruthValue
_ExtremeApsProtocolErrorFarEndProtectFailure_Object = MibTableColumn
extremeApsProtocolErrorFarEndProtectFailure = _ExtremeApsProtocolErrorFarEndProtectFailure_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 10),
    _ExtremeApsProtocolErrorFarEndProtectFailure_Type()
)
extremeApsProtocolErrorFarEndProtectFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorFarEndProtectFailure.setStatus("current")
_ExtremeApsProtocolErrorModeMismatchNumFails_Type = Integer32
_ExtremeApsProtocolErrorModeMismatchNumFails_Object = MibTableColumn
extremeApsProtocolErrorModeMismatchNumFails = _ExtremeApsProtocolErrorModeMismatchNumFails_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 11),
    _ExtremeApsProtocolErrorModeMismatchNumFails_Type()
)
extremeApsProtocolErrorModeMismatchNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorModeMismatchNumFails.setStatus("current")
_ExtremeApsProtocolErrorProtSwitchByteNumFails_Type = Integer32
_ExtremeApsProtocolErrorProtSwitchByteNumFails_Object = MibTableColumn
extremeApsProtocolErrorProtSwitchByteNumFails = _ExtremeApsProtocolErrorProtSwitchByteNumFails_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 12),
    _ExtremeApsProtocolErrorProtSwitchByteNumFails_Type()
)
extremeApsProtocolErrorProtSwitchByteNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorProtSwitchByteNumFails.setStatus("current")
_ExtremeApsProtocolErrorChannelMismatchNumFails_Type = Integer32
_ExtremeApsProtocolErrorChannelMismatchNumFails_Object = MibTableColumn
extremeApsProtocolErrorChannelMismatchNumFails = _ExtremeApsProtocolErrorChannelMismatchNumFails_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 13),
    _ExtremeApsProtocolErrorChannelMismatchNumFails_Type()
)
extremeApsProtocolErrorChannelMismatchNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorChannelMismatchNumFails.setStatus("current")
_ExtremeApsProtocolErrorFarEndProtectNumFails_Type = Integer32
_ExtremeApsProtocolErrorFarEndProtectNumFails_Object = MibTableColumn
extremeApsProtocolErrorFarEndProtectNumFails = _ExtremeApsProtocolErrorFarEndProtectNumFails_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20, 1, 3, 2, 1, 14),
    _ExtremeApsProtocolErrorFarEndProtectNumFails_Type()
)
extremeApsProtocolErrorFarEndProtectNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeApsProtocolErrorFarEndProtectNumFails.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-POS-MIB",
    **{"extremePOSMib": extremePOSMib,
       "extremeAps": extremeAps,
       "extremeApsConfig": extremeApsConfig,
       "extremeApsConfigEnabled": extremeApsConfigEnabled,
       "extremeApsGroupConfigTable": extremeApsGroupConfigTable,
       "extremeApsGroupConfigEntry": extremeApsGroupConfigEntry,
       "extremeApsGroupConfigGroupNumber": extremeApsGroupConfigGroupNumber,
       "extremeApsGroupConfigRevertMode": extremeApsGroupConfigRevertMode,
       "extremeApsGroupConfigRevertMinutes": extremeApsGroupConfigRevertMinutes,
       "extremeApsGroupConfigDirection": extremeApsGroupConfigDirection,
       "extremeApsGroupConfigTimerInterval": extremeApsGroupConfigTimerInterval,
       "extremeApsGroupConfigTimerMisses": extremeApsGroupConfigTimerMisses,
       "extremeApsGroupConfigAuthenticate": extremeApsGroupConfigAuthenticate,
       "extremeApsGroupConfigAuthString": extremeApsGroupConfigAuthString,
       "extremeApsPortConfigTable": extremeApsPortConfigTable,
       "extremeApsPortConfigEntry": extremeApsPortConfigEntry,
       "extremeApsPortConfigGroupNumber": extremeApsPortConfigGroupNumber,
       "extremeApsPortConfigPortNumber": extremeApsPortConfigPortNumber,
       "extremeApsPortConfigPortType": extremeApsPortConfigPortType,
       "extremeApsProtectPortConfigTable": extremeApsProtectPortConfigTable,
       "extremeApsProtectPortConfigEntry": extremeApsProtectPortConfigEntry,
       "extremeApsProtectPortConfigGroupNumber": extremeApsProtectPortConfigGroupNumber,
       "extremeApsProtectPortConfigPortNumber": extremeApsProtectPortConfigPortNumber,
       "extremeApsProtectPortConfigWorkingIpAddr": extremeApsProtectPortConfigWorkingIpAddr,
       "extremeApsStatus": extremeApsStatus,
       "extremeApsGroupTable": extremeApsGroupTable,
       "extremeApsGroupEntry": extremeApsGroupEntry,
       "extremeApsGroupGroupNumber": extremeApsGroupGroupNumber,
       "extremeApsGroupActivePort": extremeApsGroupActivePort,
       "extremeApsGroupEffectiveDirection": extremeApsGroupEffectiveDirection,
       "extremeApsGroupPeerProtoStatus": extremeApsGroupPeerProtoStatus,
       "extremeApsProtectPortTable": extremeApsProtectPortTable,
       "extremeApsProtectPortEntry": extremeApsProtectPortEntry,
       "extremeApsProtectPortGroupNumber": extremeApsProtectPortGroupNumber,
       "extremeApsProtectPortPortNumber": extremeApsProtectPortPortNumber,
       "extremeApsProtectPortTransmitK1": extremeApsProtectPortTransmitK1,
       "extremeApsProtectPortTransmitK2": extremeApsProtectPortTransmitK2,
       "extremeApsProtectPortReceiveK1": extremeApsProtectPortReceiveK1,
       "extremeApsProtectPortReceiveK2": extremeApsProtectPortReceiveK2,
       "extremeApsProtectPortSwitchInitByWorking": extremeApsProtectPortSwitchInitByWorking,
       "extremeApsProtectPortSwitchInitByProtect": extremeApsProtectPortSwitchInitByProtect,
       "extremeApsProtectPortSwitchInitByADM": extremeApsProtectPortSwitchInitByADM,
       "extremeApsProtectPortSwitchInitByCmd": extremeApsProtectPortSwitchInitByCmd,
       "extremeApsProtectPortSuccessfulSwitches": extremeApsProtectPortSuccessfulSwitches,
       "extremeApsProtectPortHelloProtFails": extremeApsProtectPortHelloProtFails,
       "extremeApsErrors": extremeApsErrors,
       "extremeApsLineErrorTable": extremeApsLineErrorTable,
       "extremeApsLineErrorEntry": extremeApsLineErrorEntry,
       "extremeApsLineErrorGroupNumber": extremeApsLineErrorGroupNumber,
       "extremeApsLineErrorPortNumber": extremeApsLineErrorPortNumber,
       "extremeApsLineErrorSignalDegradeActive": extremeApsLineErrorSignalDegradeActive,
       "extremeApsLineErrorBERSignalDegradeActive": extremeApsLineErrorBERSignalDegradeActive,
       "extremeApsLineErrorSignalFailActive": extremeApsLineErrorSignalFailActive,
       "extremeApsLineErrorBERSignalFailActive": extremeApsLineErrorBERSignalFailActive,
       "extremeApsLineErrorSignalDegrades": extremeApsLineErrorSignalDegrades,
       "extremeApsLineErrorBERSignalDegrades": extremeApsLineErrorBERSignalDegrades,
       "extremeApsLineErrorSignalFails": extremeApsLineErrorSignalFails,
       "extremeApsLineErrorBERSignalFails": extremeApsLineErrorBERSignalFails,
       "extremeApsProtocolErrorTable": extremeApsProtocolErrorTable,
       "extremeApsProtocolErrorEntry": extremeApsProtocolErrorEntry,
       "extremeApsProtocolErrorGroupNumber": extremeApsProtocolErrorGroupNumber,
       "extremeApsProtocolErrorPortNumber": extremeApsProtocolErrorPortNumber,
       "extremeApsProtocolErrorModeMismatchDefect": extremeApsProtocolErrorModeMismatchDefect,
       "extremeApsProtocolErrorProtSwitchByteDefect": extremeApsProtocolErrorProtSwitchByteDefect,
       "extremeApsProtocolErrorChannelMismatchDefect": extremeApsProtocolErrorChannelMismatchDefect,
       "extremeApsProtocolErrorFarEndProtectDefect": extremeApsProtocolErrorFarEndProtectDefect,
       "extremeApsProtocolErrorModeMismatchFailure": extremeApsProtocolErrorModeMismatchFailure,
       "extremeApsProtocolErrorProtSwitchByteFailure": extremeApsProtocolErrorProtSwitchByteFailure,
       "extremeApsProtocolErrorChannelMismatchFailure": extremeApsProtocolErrorChannelMismatchFailure,
       "extremeApsProtocolErrorFarEndProtectFailure": extremeApsProtocolErrorFarEndProtectFailure,
       "extremeApsProtocolErrorModeMismatchNumFails": extremeApsProtocolErrorModeMismatchNumFails,
       "extremeApsProtocolErrorProtSwitchByteNumFails": extremeApsProtocolErrorProtSwitchByteNumFails,
       "extremeApsProtocolErrorChannelMismatchNumFails": extremeApsProtocolErrorChannelMismatchNumFails,
       "extremeApsProtocolErrorFarEndProtectNumFails": extremeApsProtocolErrorFarEndProtectNumFails}
)
