# SNMP MIB module (ALCATEL-IND1-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:49 2024
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

(softentIND1Port,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Port")

(InterfaceIndex,
 ifEntry,
 ifInErrors,
 ifIndex,
 ifOutErrors) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifEntry",
    "ifInErrors",
    "ifIndex",
    "ifOutErrors")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1PortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1)
)
alcatelIND1PortMIB.setRevisions(
        ("2013-11-22 00:00",
         "2010-05-13 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1PortNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1PortNotifications = _AlcatelIND1PortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 0)
)
_AlcatelIND1PortMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1PortMIBObjects = _AlcatelIND1PortMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1)
)
_EsmConfTrap_ObjectIdentity = ObjectIdentity
esmConfTrap = _EsmConfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 1)
)
_EsmDrvTrapDrops_Type = Integer32
_EsmDrvTrapDrops_Object = MibScalar
esmDrvTrapDrops = _EsmDrvTrapDrops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 1, 1),
    _EsmDrvTrapDrops_Type()
)
esmDrvTrapDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmDrvTrapDrops.setStatus("current")
_PhysicalPort_ObjectIdentity = ObjectIdentity
physicalPort = _PhysicalPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2)
)
_EsmConfTable_Object = MibTable
esmConfTable = _EsmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    esmConfTable.setStatus("current")
_EsmConfEntry_Object = MibTableRow
esmConfEntry = _EsmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1)
)
esmConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    esmConfEntry.setStatus("current")
_EsmPortSlot_Type = Integer32
_EsmPortSlot_Object = MibTableColumn
esmPortSlot = _EsmPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 1),
    _EsmPortSlot_Type()
)
esmPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortSlot.setStatus("current")
_EsmPortIF_Type = Integer32
_EsmPortIF_Object = MibTableColumn
esmPortIF = _EsmPortIF_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 2),
    _EsmPortIF_Type()
)
esmPortIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortIF.setStatus("current")


class _EsmPortAutoSpeed_Type(Integer32):
    """Custom type esmPortAutoSpeed based on Integer32"""
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
        *(("speed10", 2),
          ("speed100", 1),
          ("speed1000", 5),
          ("speed10000", 6),
          ("speed40000", 7),
          ("speedAuto", 3),
          ("unknown", 4))
    )


_EsmPortAutoSpeed_Type.__name__ = "Integer32"
_EsmPortAutoSpeed_Object = MibTableColumn
esmPortAutoSpeed = _EsmPortAutoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 3),
    _EsmPortAutoSpeed_Type()
)
esmPortAutoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortAutoSpeed.setStatus("current")


class _EsmPortAutoDuplexMode_Type(Integer32):
    """Custom type esmPortAutoDuplexMode based on Integer32"""
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
        *(("autoDuplex", 3),
          ("fullDuplex", 1),
          ("halfDuplex", 2),
          ("unknown", 4))
    )


_EsmPortAutoDuplexMode_Type.__name__ = "Integer32"
_EsmPortAutoDuplexMode_Object = MibTableColumn
esmPortAutoDuplexMode = _EsmPortAutoDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 4),
    _EsmPortAutoDuplexMode_Type()
)
esmPortAutoDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortAutoDuplexMode.setStatus("current")


class _EsmPortCfgSpeed_Type(Integer32):
    """Custom type esmPortCfgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 2),
          ("speed100", 1),
          ("speed1000", 5),
          ("speed10000", 6),
          ("speed40000", 7),
          ("speedAuto", 3),
          ("speedMax100", 8),
          ("speedMax1000", 9))
    )


_EsmPortCfgSpeed_Type.__name__ = "Integer32"
_EsmPortCfgSpeed_Object = MibTableColumn
esmPortCfgSpeed = _EsmPortCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 5),
    _EsmPortCfgSpeed_Type()
)
esmPortCfgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgSpeed.setStatus("current")


class _EsmPortCfgDuplexMode_Type(Integer32):
    """Custom type esmPortCfgDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDuplex", 3),
          ("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_EsmPortCfgDuplexMode_Type.__name__ = "Integer32"
_EsmPortCfgDuplexMode_Object = MibTableColumn
esmPortCfgDuplexMode = _EsmPortCfgDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 6),
    _EsmPortCfgDuplexMode_Type()
)
esmPortCfgDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgDuplexMode.setStatus("current")


class _EsmPortAdminStatus_Type(Integer32):
    """Custom type esmPortAdminStatus based on Integer32"""
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


_EsmPortAdminStatus_Type.__name__ = "Integer32"
_EsmPortAdminStatus_Object = MibTableColumn
esmPortAdminStatus = _EsmPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 7),
    _EsmPortAdminStatus_Type()
)
esmPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortAdminStatus.setStatus("current")


class _EsmPortLinkUpDownTrapEnable_Type(Integer32):
    """Custom type esmPortLinkUpDownTrapEnable based on Integer32"""
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


_EsmPortLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_EsmPortLinkUpDownTrapEnable_Object = MibTableColumn
esmPortLinkUpDownTrapEnable = _EsmPortLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 8),
    _EsmPortLinkUpDownTrapEnable_Type()
)
esmPortLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortLinkUpDownTrapEnable.setStatus("current")
_EsmPortCfgMaxFrameSize_Type = Integer32
_EsmPortCfgMaxFrameSize_Object = MibTableColumn
esmPortCfgMaxFrameSize = _EsmPortCfgMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 11),
    _EsmPortCfgMaxFrameSize_Type()
)
esmPortCfgMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgMaxFrameSize.setStatus("current")


class _EsmPortAlias_Type(SnmpAdminString):
    """Custom type esmPortAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EsmPortAlias_Type.__name__ = "SnmpAdminString"
_EsmPortAlias_Object = MibTableColumn
esmPortAlias = _EsmPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 12),
    _EsmPortAlias_Type()
)
esmPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortAlias.setStatus("current")


class _EsmPortCfgPause_Type(Integer32):
    """Custom type esmPortCfgPause based on Integer32"""
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
        *(("disabled", 1),
          ("enabledRcv", 3),
          ("enabledXmit", 2),
          ("enabledXmitAndRcv", 4))
    )


_EsmPortCfgPause_Type.__name__ = "Integer32"
_EsmPortCfgPause_Object = MibTableColumn
esmPortCfgPause = _EsmPortCfgPause_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 13),
    _EsmPortCfgPause_Type()
)
esmPortCfgPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgPause.setStatus("current")


class _EsmPortCfgAutoNegotiation_Type(Integer32):
    """Custom type esmPortCfgAutoNegotiation based on Integer32"""
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


_EsmPortCfgAutoNegotiation_Type.__name__ = "Integer32"
_EsmPortCfgAutoNegotiation_Object = MibTableColumn
esmPortCfgAutoNegotiation = _EsmPortCfgAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 15),
    _EsmPortCfgAutoNegotiation_Type()
)
esmPortCfgAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgAutoNegotiation.setStatus("current")


class _EsmPortCfgCrossover_Type(Integer32):
    """Custom type esmPortCfgCrossover based on Integer32"""
    defaultValue = 3

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
        *(("auto", 3),
          ("mdi", 1),
          ("mdix", 2),
          ("notapplicable", 4))
    )


_EsmPortCfgCrossover_Type.__name__ = "Integer32"
_EsmPortCfgCrossover_Object = MibTableColumn
esmPortCfgCrossover = _EsmPortCfgCrossover_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 16),
    _EsmPortCfgCrossover_Type()
)
esmPortCfgCrossover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgCrossover.setStatus("current")


class _EsmPortCfgHybridActiveType_Type(Integer32):
    """Custom type esmPortCfgHybridActiveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber", 1),
          ("notapplicable", 0))
    )


_EsmPortCfgHybridActiveType_Type.__name__ = "Integer32"
_EsmPortCfgHybridActiveType_Object = MibTableColumn
esmPortCfgHybridActiveType = _EsmPortCfgHybridActiveType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 18),
    _EsmPortCfgHybridActiveType_Type()
)
esmPortCfgHybridActiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortCfgHybridActiveType.setStatus("current")


class _EsmPortCfgHybridMode_Type(Integer32):
    """Custom type esmPortCfgHybridMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("forcedCopper", 2),
          ("forcedFiber", 4),
          ("notapplicable", 0),
          ("preferredCopper", 1),
          ("preferredFiber", 3))
    )


_EsmPortCfgHybridMode_Type.__name__ = "Integer32"
_EsmPortCfgHybridMode_Object = MibTableColumn
esmPortCfgHybridMode = _EsmPortCfgHybridMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 19),
    _EsmPortCfgHybridMode_Type()
)
esmPortCfgHybridMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgHybridMode.setStatus("current")


class _EsmPortOperationalHybridType_Type(Integer32):
    """Custom type esmPortOperationalHybridType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber", 1),
          ("none", 0))
    )


_EsmPortOperationalHybridType_Type.__name__ = "Integer32"
_EsmPortOperationalHybridType_Object = MibTableColumn
esmPortOperationalHybridType = _EsmPortOperationalHybridType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 20),
    _EsmPortOperationalHybridType_Type()
)
esmPortOperationalHybridType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortOperationalHybridType.setStatus("current")


class _EsmPortBcastRateLimitEnable_Type(Integer32):
    """Custom type esmPortBcastRateLimitEnable based on Integer32"""
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


_EsmPortBcastRateLimitEnable_Type.__name__ = "Integer32"
_EsmPortBcastRateLimitEnable_Object = MibTableColumn
esmPortBcastRateLimitEnable = _EsmPortBcastRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 21),
    _EsmPortBcastRateLimitEnable_Type()
)
esmPortBcastRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortBcastRateLimitEnable.setStatus("current")


class _EsmPortBcastRateLimitType_Type(Integer32):
    """Custom type esmPortBcastRateLimitType based on Integer32"""
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
        *(("mbps", 1),
          ("percentage", 2),
          ("pps", 3))
    )


_EsmPortBcastRateLimitType_Type.__name__ = "Integer32"
_EsmPortBcastRateLimitType_Object = MibTableColumn
esmPortBcastRateLimitType = _EsmPortBcastRateLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 22),
    _EsmPortBcastRateLimitType_Type()
)
esmPortBcastRateLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortBcastRateLimitType.setStatus("current")
_EsmPortBcastRateLimit_Type = Integer32
_EsmPortBcastRateLimit_Object = MibTableColumn
esmPortBcastRateLimit = _EsmPortBcastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 23),
    _EsmPortBcastRateLimit_Type()
)
esmPortBcastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortBcastRateLimit.setStatus("current")


class _EsmPortMcastRateLimitEnable_Type(Integer32):
    """Custom type esmPortMcastRateLimitEnable based on Integer32"""
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


_EsmPortMcastRateLimitEnable_Type.__name__ = "Integer32"
_EsmPortMcastRateLimitEnable_Object = MibTableColumn
esmPortMcastRateLimitEnable = _EsmPortMcastRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 24),
    _EsmPortMcastRateLimitEnable_Type()
)
esmPortMcastRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortMcastRateLimitEnable.setStatus("current")


class _EsmPortMcastRateLimitType_Type(Integer32):
    """Custom type esmPortMcastRateLimitType based on Integer32"""
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
        *(("mbps", 1),
          ("percentage", 2),
          ("pps", 3))
    )


_EsmPortMcastRateLimitType_Type.__name__ = "Integer32"
_EsmPortMcastRateLimitType_Object = MibTableColumn
esmPortMcastRateLimitType = _EsmPortMcastRateLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 25),
    _EsmPortMcastRateLimitType_Type()
)
esmPortMcastRateLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortMcastRateLimitType.setStatus("current")
_EsmPortMcastRateLimit_Type = Integer32
_EsmPortMcastRateLimit_Object = MibTableColumn
esmPortMcastRateLimit = _EsmPortMcastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 26),
    _EsmPortMcastRateLimit_Type()
)
esmPortMcastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortMcastRateLimit.setStatus("current")


class _EsmPortUucastRateLimitEnable_Type(Integer32):
    """Custom type esmPortUucastRateLimitEnable based on Integer32"""
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


_EsmPortUucastRateLimitEnable_Type.__name__ = "Integer32"
_EsmPortUucastRateLimitEnable_Object = MibTableColumn
esmPortUucastRateLimitEnable = _EsmPortUucastRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 27),
    _EsmPortUucastRateLimitEnable_Type()
)
esmPortUucastRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortUucastRateLimitEnable.setStatus("current")


class _EsmPortUucastRateLimitType_Type(Integer32):
    """Custom type esmPortUucastRateLimitType based on Integer32"""
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
        *(("mbps", 1),
          ("percentage", 2),
          ("pps", 3))
    )


_EsmPortUucastRateLimitType_Type.__name__ = "Integer32"
_EsmPortUucastRateLimitType_Object = MibTableColumn
esmPortUucastRateLimitType = _EsmPortUucastRateLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 28),
    _EsmPortUucastRateLimitType_Type()
)
esmPortUucastRateLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortUucastRateLimitType.setStatus("current")
_EsmPortUucastRateLimit_Type = Integer32
_EsmPortUucastRateLimit_Object = MibTableColumn
esmPortUucastRateLimit = _EsmPortUucastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 29),
    _EsmPortUucastRateLimit_Type()
)
esmPortUucastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortUucastRateLimit.setStatus("current")


class _EsmPortIngressRateLimitEnable_Type(Integer32):
    """Custom type esmPortIngressRateLimitEnable based on Integer32"""
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


_EsmPortIngressRateLimitEnable_Type.__name__ = "Integer32"
_EsmPortIngressRateLimitEnable_Object = MibTableColumn
esmPortIngressRateLimitEnable = _EsmPortIngressRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 30),
    _EsmPortIngressRateLimitEnable_Type()
)
esmPortIngressRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortIngressRateLimitEnable.setStatus("current")
_EsmPortIngressRateLimit_Type = Integer32
_EsmPortIngressRateLimit_Object = MibTableColumn
esmPortIngressRateLimit = _EsmPortIngressRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 31),
    _EsmPortIngressRateLimit_Type()
)
esmPortIngressRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortIngressRateLimit.setStatus("current")
_EsmPortIngressRateLimitBurst_Type = Integer32
_EsmPortIngressRateLimitBurst_Object = MibTableColumn
esmPortIngressRateLimitBurst = _EsmPortIngressRateLimitBurst_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 32),
    _EsmPortIngressRateLimitBurst_Type()
)
esmPortIngressRateLimitBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortIngressRateLimitBurst.setStatus("current")


class _EsmPortEPPEnable_Type(Integer32):
    """Custom type esmPortEPPEnable based on Integer32"""
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


_EsmPortEPPEnable_Type.__name__ = "Integer32"
_EsmPortEPPEnable_Object = MibTableColumn
esmPortEPPEnable = _EsmPortEPPEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 33),
    _EsmPortEPPEnable_Type()
)
esmPortEPPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortEPPEnable.setStatus("current")


class _EsmPortEEEEnable_Type(Integer32):
    """Custom type esmPortEEEEnable based on Integer32"""
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


_EsmPortEEEEnable_Type.__name__ = "Integer32"
_EsmPortEEEEnable_Object = MibTableColumn
esmPortEEEEnable = _EsmPortEEEEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 34),
    _EsmPortEEEEnable_Type()
)
esmPortEEEEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortEEEEnable.setStatus("current")


class _EsmPortIsFiberChannelCapable_Type(Integer32):
    """Custom type esmPortIsFiberChannelCapable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_EsmPortIsFiberChannelCapable_Type.__name__ = "Integer32"
_EsmPortIsFiberChannelCapable_Object = MibTableColumn
esmPortIsFiberChannelCapable = _EsmPortIsFiberChannelCapable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 1, 1, 35),
    _EsmPortIsFiberChannelCapable_Type()
)
esmPortIsFiberChannelCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortIsFiberChannelCapable.setStatus("current")
_AlcetherStatsTable_Object = MibTable
alcetherStatsTable = _AlcetherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcetherStatsTable.setStatus("current")
_AlcetherStatsEntry_Object = MibTableRow
alcetherStatsEntry = _AlcetherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1)
)
alcetherStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alcetherStatsEntry.setStatus("current")


class _AlcetherClearStats_Type(Integer32):
    """Custom type alcetherClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlcetherClearStats_Type.__name__ = "Integer32"
_AlcetherClearStats_Object = MibTableColumn
alcetherClearStats = _AlcetherClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 1),
    _AlcetherClearStats_Type()
)
alcetherClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcetherClearStats.setStatus("current")
_AlcetherLastClearStats_Type = TimeTicks
_AlcetherLastClearStats_Object = MibTableColumn
alcetherLastClearStats = _AlcetherLastClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 2),
    _AlcetherLastClearStats_Type()
)
alcetherLastClearStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherLastClearStats.setStatus("current")
_AlcetherStatsCRCAlignErrors_Type = Counter64
_AlcetherStatsCRCAlignErrors_Object = MibTableColumn
alcetherStatsCRCAlignErrors = _AlcetherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 3),
    _AlcetherStatsCRCAlignErrors_Type()
)
alcetherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsCRCAlignErrors.setStatus("current")
_AlcetherStatsRxUndersizePkts_Type = Counter64
_AlcetherStatsRxUndersizePkts_Object = MibTableColumn
alcetherStatsRxUndersizePkts = _AlcetherStatsRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 4),
    _AlcetherStatsRxUndersizePkts_Type()
)
alcetherStatsRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxUndersizePkts.setStatus("current")
_AlcetherStatsTxUndersizePkts_Type = Counter64
_AlcetherStatsTxUndersizePkts_Object = MibTableColumn
alcetherStatsTxUndersizePkts = _AlcetherStatsTxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 5),
    _AlcetherStatsTxUndersizePkts_Type()
)
alcetherStatsTxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxUndersizePkts.setStatus("current")
_AlcetherStatsTxOversizePkts_Type = Counter64
_AlcetherStatsTxOversizePkts_Object = MibTableColumn
alcetherStatsTxOversizePkts = _AlcetherStatsTxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 6),
    _AlcetherStatsTxOversizePkts_Type()
)
alcetherStatsTxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxOversizePkts.setStatus("current")
_AlcetherStatsRxJabbers_Type = Counter64
_AlcetherStatsRxJabbers_Object = MibTableColumn
alcetherStatsRxJabbers = _AlcetherStatsRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 7),
    _AlcetherStatsRxJabbers_Type()
)
alcetherStatsRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxJabbers.setStatus("current")
_AlcetherStatsRxCollisions_Type = Counter64
_AlcetherStatsRxCollisions_Object = MibTableColumn
alcetherStatsRxCollisions = _AlcetherStatsRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 8),
    _AlcetherStatsRxCollisions_Type()
)
alcetherStatsRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxCollisions.setStatus("current")
_AlcetherStatsTxCollisions_Type = Counter64
_AlcetherStatsTxCollisions_Object = MibTableColumn
alcetherStatsTxCollisions = _AlcetherStatsTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 9),
    _AlcetherStatsTxCollisions_Type()
)
alcetherStatsTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxCollisions.setStatus("current")
_AlcetherStatsPkts64Octets_Type = Counter64
_AlcetherStatsPkts64Octets_Object = MibTableColumn
alcetherStatsPkts64Octets = _AlcetherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 10),
    _AlcetherStatsPkts64Octets_Type()
)
alcetherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts64Octets.setStatus("current")
_AlcetherStatsPkts65to127Octets_Type = Counter64
_AlcetherStatsPkts65to127Octets_Object = MibTableColumn
alcetherStatsPkts65to127Octets = _AlcetherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 11),
    _AlcetherStatsPkts65to127Octets_Type()
)
alcetherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts65to127Octets.setStatus("current")
_AlcetherStatsPkts128to255Octets_Type = Counter64
_AlcetherStatsPkts128to255Octets_Object = MibTableColumn
alcetherStatsPkts128to255Octets = _AlcetherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 12),
    _AlcetherStatsPkts128to255Octets_Type()
)
alcetherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts128to255Octets.setStatus("current")
_AlcetherStatsPkts256to511Octets_Type = Counter64
_AlcetherStatsPkts256to511Octets_Object = MibTableColumn
alcetherStatsPkts256to511Octets = _AlcetherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 13),
    _AlcetherStatsPkts256to511Octets_Type()
)
alcetherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts256to511Octets.setStatus("current")
_AlcetherStatsPkts512to1023Octets_Type = Counter64
_AlcetherStatsPkts512to1023Octets_Object = MibTableColumn
alcetherStatsPkts512to1023Octets = _AlcetherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 14),
    _AlcetherStatsPkts512to1023Octets_Type()
)
alcetherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts512to1023Octets.setStatus("current")
_AlcetherStatsPkts1024to1518Octets_Type = Counter64
_AlcetherStatsPkts1024to1518Octets_Object = MibTableColumn
alcetherStatsPkts1024to1518Octets = _AlcetherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 15),
    _AlcetherStatsPkts1024to1518Octets_Type()
)
alcetherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts1024to1518Octets.setStatus("current")
_GigaEtherStatsPkts1519to4095Octets_Type = Counter64
_GigaEtherStatsPkts1519to4095Octets_Object = MibTableColumn
gigaEtherStatsPkts1519to4095Octets = _GigaEtherStatsPkts1519to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 16),
    _GigaEtherStatsPkts1519to4095Octets_Type()
)
gigaEtherStatsPkts1519to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigaEtherStatsPkts1519to4095Octets.setStatus("current")
_GigaEtherStatsPkts4096to9215Octets_Type = Counter64
_GigaEtherStatsPkts4096to9215Octets_Object = MibTableColumn
gigaEtherStatsPkts4096to9215Octets = _GigaEtherStatsPkts4096to9215Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 17),
    _GigaEtherStatsPkts4096to9215Octets_Type()
)
gigaEtherStatsPkts4096to9215Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigaEtherStatsPkts4096to9215Octets.setStatus("current")
_AlcetherStatsPkts1519to2047Octets_Type = Counter64
_AlcetherStatsPkts1519to2047Octets_Object = MibTableColumn
alcetherStatsPkts1519to2047Octets = _AlcetherStatsPkts1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 18),
    _AlcetherStatsPkts1519to2047Octets_Type()
)
alcetherStatsPkts1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts1519to2047Octets.setStatus("current")
_AlcetherStatsPkts2048to4095Octets_Type = Counter64
_AlcetherStatsPkts2048to4095Octets_Object = MibTableColumn
alcetherStatsPkts2048to4095Octets = _AlcetherStatsPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 19),
    _AlcetherStatsPkts2048to4095Octets_Type()
)
alcetherStatsPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts2048to4095Octets.setStatus("current")
_AlcetherStatsPkts4096Octets_Type = Counter64
_AlcetherStatsPkts4096Octets_Object = MibTableColumn
alcetherStatsPkts4096Octets = _AlcetherStatsPkts4096Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 20),
    _AlcetherStatsPkts4096Octets_Type()
)
alcetherStatsPkts4096Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts4096Octets.setStatus("current")
_AlcetherStatsRxGiantPkts_Type = Counter64
_AlcetherStatsRxGiantPkts_Object = MibTableColumn
alcetherStatsRxGiantPkts = _AlcetherStatsRxGiantPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 21),
    _AlcetherStatsRxGiantPkts_Type()
)
alcetherStatsRxGiantPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxGiantPkts.setStatus("current")
_AlcetherStatsRxDribbleNibblePkts_Type = Counter64
_AlcetherStatsRxDribbleNibblePkts_Object = MibTableColumn
alcetherStatsRxDribbleNibblePkts = _AlcetherStatsRxDribbleNibblePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 22),
    _AlcetherStatsRxDribbleNibblePkts_Type()
)
alcetherStatsRxDribbleNibblePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxDribbleNibblePkts.setStatus("current")
_AlcetherStatsRxLongEventPkts_Type = Counter64
_AlcetherStatsRxLongEventPkts_Object = MibTableColumn
alcetherStatsRxLongEventPkts = _AlcetherStatsRxLongEventPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 23),
    _AlcetherStatsRxLongEventPkts_Type()
)
alcetherStatsRxLongEventPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxLongEventPkts.setStatus("current")
_AlcetherStatsRxVlanTagPkts_Type = Counter64
_AlcetherStatsRxVlanTagPkts_Object = MibTableColumn
alcetherStatsRxVlanTagPkts = _AlcetherStatsRxVlanTagPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 24),
    _AlcetherStatsRxVlanTagPkts_Type()
)
alcetherStatsRxVlanTagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxVlanTagPkts.setStatus("current")
_AlcetherStatsRxControlPkts_Type = Counter64
_AlcetherStatsRxControlPkts_Object = MibTableColumn
alcetherStatsRxControlPkts = _AlcetherStatsRxControlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 25),
    _AlcetherStatsRxControlPkts_Type()
)
alcetherStatsRxControlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxControlPkts.setStatus("current")
_AlcetherStatsRxLenChkErrPkts_Type = Counter64
_AlcetherStatsRxLenChkErrPkts_Object = MibTableColumn
alcetherStatsRxLenChkErrPkts = _AlcetherStatsRxLenChkErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 26),
    _AlcetherStatsRxLenChkErrPkts_Type()
)
alcetherStatsRxLenChkErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxLenChkErrPkts.setStatus("current")
_AlcetherStatsRxCodeErrPkts_Type = Counter64
_AlcetherStatsRxCodeErrPkts_Object = MibTableColumn
alcetherStatsRxCodeErrPkts = _AlcetherStatsRxCodeErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 27),
    _AlcetherStatsRxCodeErrPkts_Type()
)
alcetherStatsRxCodeErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxCodeErrPkts.setStatus("current")
_AlcetherStatsRxDvEventPkts_Type = Counter64
_AlcetherStatsRxDvEventPkts_Object = MibTableColumn
alcetherStatsRxDvEventPkts = _AlcetherStatsRxDvEventPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 28),
    _AlcetherStatsRxDvEventPkts_Type()
)
alcetherStatsRxDvEventPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxDvEventPkts.setStatus("current")
_AlcetherStatsRxPrevPktDropped_Type = Counter64
_AlcetherStatsRxPrevPktDropped_Object = MibTableColumn
alcetherStatsRxPrevPktDropped = _AlcetherStatsRxPrevPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 29),
    _AlcetherStatsRxPrevPktDropped_Type()
)
alcetherStatsRxPrevPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxPrevPktDropped.setStatus("current")
_AlcetherStatsTx64Octets_Type = Counter64
_AlcetherStatsTx64Octets_Object = MibTableColumn
alcetherStatsTx64Octets = _AlcetherStatsTx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 30),
    _AlcetherStatsTx64Octets_Type()
)
alcetherStatsTx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx64Octets.setStatus("current")
_AlcetherStatsTx65to127Octets_Type = Counter64
_AlcetherStatsTx65to127Octets_Object = MibTableColumn
alcetherStatsTx65to127Octets = _AlcetherStatsTx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 31),
    _AlcetherStatsTx65to127Octets_Type()
)
alcetherStatsTx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx65to127Octets.setStatus("current")
_AlcetherStatsTx128to255Octets_Type = Counter64
_AlcetherStatsTx128to255Octets_Object = MibTableColumn
alcetherStatsTx128to255Octets = _AlcetherStatsTx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 32),
    _AlcetherStatsTx128to255Octets_Type()
)
alcetherStatsTx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx128to255Octets.setStatus("current")
_AlcetherStatsTx256to511Octets_Type = Counter64
_AlcetherStatsTx256to511Octets_Object = MibTableColumn
alcetherStatsTx256to511Octets = _AlcetherStatsTx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 33),
    _AlcetherStatsTx256to511Octets_Type()
)
alcetherStatsTx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx256to511Octets.setStatus("current")
_AlcetherStatsTx512to1023Octets_Type = Counter64
_AlcetherStatsTx512to1023Octets_Object = MibTableColumn
alcetherStatsTx512to1023Octets = _AlcetherStatsTx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 34),
    _AlcetherStatsTx512to1023Octets_Type()
)
alcetherStatsTx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx512to1023Octets.setStatus("current")
_AlcetherStatsTx1024to1518Octets_Type = Counter64
_AlcetherStatsTx1024to1518Octets_Object = MibTableColumn
alcetherStatsTx1024to1518Octets = _AlcetherStatsTx1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 35),
    _AlcetherStatsTx1024to1518Octets_Type()
)
alcetherStatsTx1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx1024to1518Octets.setStatus("current")
_AlcetherStatsTx1519to2047Octets_Type = Counter64
_AlcetherStatsTx1519to2047Octets_Object = MibTableColumn
alcetherStatsTx1519to2047Octets = _AlcetherStatsTx1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 36),
    _AlcetherStatsTx1519to2047Octets_Type()
)
alcetherStatsTx1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx1519to2047Octets.setStatus("current")
_AlcetherStatsTx2048to4095Octets_Type = Counter64
_AlcetherStatsTx2048to4095Octets_Object = MibTableColumn
alcetherStatsTx2048to4095Octets = _AlcetherStatsTx2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 37),
    _AlcetherStatsTx2048to4095Octets_Type()
)
alcetherStatsTx2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx2048to4095Octets.setStatus("current")
_AlcetherStatsTx4096Octets_Type = Counter64
_AlcetherStatsTx4096Octets_Object = MibTableColumn
alcetherStatsTx4096Octets = _AlcetherStatsTx4096Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 38),
    _AlcetherStatsTx4096Octets_Type()
)
alcetherStatsTx4096Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx4096Octets.setStatus("current")
_AlcetherStatsTxRetryCount_Type = Counter64
_AlcetherStatsTxRetryCount_Object = MibTableColumn
alcetherStatsTxRetryCount = _AlcetherStatsTxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 39),
    _AlcetherStatsTxRetryCount_Type()
)
alcetherStatsTxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxRetryCount.setStatus("current")
_AlcetherStatsTxVlanTagPkts_Type = Counter64
_AlcetherStatsTxVlanTagPkts_Object = MibTableColumn
alcetherStatsTxVlanTagPkts = _AlcetherStatsTxVlanTagPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 40),
    _AlcetherStatsTxVlanTagPkts_Type()
)
alcetherStatsTxVlanTagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxVlanTagPkts.setStatus("current")
_AlcetherStatsTxControlPkts_Type = Counter64
_AlcetherStatsTxControlPkts_Object = MibTableColumn
alcetherStatsTxControlPkts = _AlcetherStatsTxControlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 41),
    _AlcetherStatsTxControlPkts_Type()
)
alcetherStatsTxControlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxControlPkts.setStatus("current")
_AlcetherStatsTxLatePkts_Type = Counter64
_AlcetherStatsTxLatePkts_Object = MibTableColumn
alcetherStatsTxLatePkts = _AlcetherStatsTxLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 42),
    _AlcetherStatsTxLatePkts_Type()
)
alcetherStatsTxLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxLatePkts.setStatus("current")
_AlcetherStatsTxTotalBytesOnWire_Type = Counter64
_AlcetherStatsTxTotalBytesOnWire_Object = MibTableColumn
alcetherStatsTxTotalBytesOnWire = _AlcetherStatsTxTotalBytesOnWire_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 43),
    _AlcetherStatsTxTotalBytesOnWire_Type()
)
alcetherStatsTxTotalBytesOnWire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxTotalBytesOnWire.setStatus("current")
_AlcetherStatsTxLenChkErrPkts_Type = Counter64
_AlcetherStatsTxLenChkErrPkts_Object = MibTableColumn
alcetherStatsTxLenChkErrPkts = _AlcetherStatsTxLenChkErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 44),
    _AlcetherStatsTxLenChkErrPkts_Type()
)
alcetherStatsTxLenChkErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxLenChkErrPkts.setStatus("current")
_AlcetherStatsTxExcDeferPkts_Type = Counter64
_AlcetherStatsTxExcDeferPkts_Object = MibTableColumn
alcetherStatsTxExcDeferPkts = _AlcetherStatsTxExcDeferPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 2, 1, 45),
    _AlcetherStatsTxExcDeferPkts_Type()
)
alcetherStatsTxExcDeferPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxExcDeferPkts.setStatus("current")
_EsmHybridConfTable_Object = MibTable
esmHybridConfTable = _EsmHybridConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    esmHybridConfTable.setStatus("current")
_EsmHybridConfEntry_Object = MibTableRow
esmHybridConfEntry = _EsmHybridConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 3, 1)
)
esmHybridConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    esmHybridConfEntry.setStatus("current")


class _EsmHybridPortCfgSpeed_Type(Integer32):
    """Custom type esmHybridPortCfgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 2),
          ("speed100", 1),
          ("speed1000", 5),
          ("speed10000", 6),
          ("speedAuto", 3),
          ("speedMax100", 8),
          ("speedMax1000", 9))
    )


_EsmHybridPortCfgSpeed_Type.__name__ = "Integer32"
_EsmHybridPortCfgSpeed_Object = MibTableColumn
esmHybridPortCfgSpeed = _EsmHybridPortCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 3, 1, 1),
    _EsmHybridPortCfgSpeed_Type()
)
esmHybridPortCfgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmHybridPortCfgSpeed.setStatus("current")


class _EsmHybridPortCfgDuplexMode_Type(Integer32):
    """Custom type esmHybridPortCfgDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDuplex", 3),
          ("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_EsmHybridPortCfgDuplexMode_Type.__name__ = "Integer32"
_EsmHybridPortCfgDuplexMode_Object = MibTableColumn
esmHybridPortCfgDuplexMode = _EsmHybridPortCfgDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 3, 1, 2),
    _EsmHybridPortCfgDuplexMode_Type()
)
esmHybridPortCfgDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmHybridPortCfgDuplexMode.setStatus("current")


class _EsmHybridPortCfgAutoNegotiation_Type(Integer32):
    """Custom type esmHybridPortCfgAutoNegotiation based on Integer32"""
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


_EsmHybridPortCfgAutoNegotiation_Type.__name__ = "Integer32"
_EsmHybridPortCfgAutoNegotiation_Object = MibTableColumn
esmHybridPortCfgAutoNegotiation = _EsmHybridPortCfgAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 3, 1, 3),
    _EsmHybridPortCfgAutoNegotiation_Type()
)
esmHybridPortCfgAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmHybridPortCfgAutoNegotiation.setStatus("current")


class _EsmHybridPortCfgCrossover_Type(Integer32):
    """Custom type esmHybridPortCfgCrossover based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("mdi", 1),
          ("mdix", 2))
    )


_EsmHybridPortCfgCrossover_Type.__name__ = "Integer32"
_EsmHybridPortCfgCrossover_Object = MibTableColumn
esmHybridPortCfgCrossover = _EsmHybridPortCfgCrossover_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 3, 1, 4),
    _EsmHybridPortCfgCrossover_Type()
)
esmHybridPortCfgCrossover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmHybridPortCfgCrossover.setStatus("current")


class _EsmHybridPortCfgFlow_Type(Integer32):
    """Custom type esmHybridPortCfgFlow based on Integer32"""
    defaultValue = 1

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
          ("enabledRcv", 3),
          ("enabledXmit", 2),
          ("enabledXmitAndRcv", 4))
    )


_EsmHybridPortCfgFlow_Type.__name__ = "Integer32"
_EsmHybridPortCfgFlow_Object = MibTableColumn
esmHybridPortCfgFlow = _EsmHybridPortCfgFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 3, 1, 5),
    _EsmHybridPortCfgFlow_Type()
)
esmHybridPortCfgFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmHybridPortCfgFlow.setStatus("current")


class _EsmHybridPortCfgInactiveType_Type(Integer32):
    """Custom type esmHybridPortCfgInactiveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber", 1))
    )


_EsmHybridPortCfgInactiveType_Type.__name__ = "Integer32"
_EsmHybridPortCfgInactiveType_Object = MibTableColumn
esmHybridPortCfgInactiveType = _EsmHybridPortCfgInactiveType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 3, 1, 6),
    _EsmHybridPortCfgInactiveType_Type()
)
esmHybridPortCfgInactiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmHybridPortCfgInactiveType.setStatus("current")
_DdmInfoTable_Object = MibTable
ddmInfoTable = _DdmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ddmInfoTable.setStatus("deprecated")
_DdmInfoEntry_Object = MibTableRow
ddmInfoEntry = _DdmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1)
)
ddmInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ddmInfoEntry.setStatus("current")


class _DdmTemperature_Type(Integer32):
    """Custom type ddmTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmTemperature_Type.__name__ = "Integer32"
_DdmTemperature_Object = MibTableColumn
ddmTemperature = _DdmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 1),
    _DdmTemperature_Type()
)
ddmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ddmTemperature.setUnits("thousandth of a degree celcius")


class _DdmTempLowWarning_Type(Integer32):
    """Custom type ddmTempLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmTempLowWarning_Type.__name__ = "Integer32"
_DdmTempLowWarning_Object = MibTableColumn
ddmTempLowWarning = _DdmTempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 2),
    _DdmTempLowWarning_Type()
)
ddmTempLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTempLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTempLowWarning.setUnits("thousandth of a degree celcius")


class _DdmTempLowAlarm_Type(Integer32):
    """Custom type ddmTempLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmTempLowAlarm_Type.__name__ = "Integer32"
_DdmTempLowAlarm_Object = MibTableColumn
ddmTempLowAlarm = _DdmTempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 3),
    _DdmTempLowAlarm_Type()
)
ddmTempLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTempLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTempLowAlarm.setUnits("thousandth of a degree celcius")


class _DdmTempHiWarning_Type(Integer32):
    """Custom type ddmTempHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmTempHiWarning_Type.__name__ = "Integer32"
_DdmTempHiWarning_Object = MibTableColumn
ddmTempHiWarning = _DdmTempHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 4),
    _DdmTempHiWarning_Type()
)
ddmTempHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTempHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTempHiWarning.setUnits("thousandth of a degree celcius")


class _DdmTempHiAlarm_Type(Integer32):
    """Custom type ddmTempHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmTempHiAlarm_Type.__name__ = "Integer32"
_DdmTempHiAlarm_Object = MibTableColumn
ddmTempHiAlarm = _DdmTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 5),
    _DdmTempHiAlarm_Type()
)
ddmTempHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTempHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTempHiAlarm.setUnits("thousandth of a degree celcius")


class _DdmSupplyVoltage_Type(Integer32):
    """Custom type ddmSupplyVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmSupplyVoltage_Type.__name__ = "Integer32"
_DdmSupplyVoltage_Object = MibTableColumn
ddmSupplyVoltage = _DdmSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 6),
    _DdmSupplyVoltage_Type()
)
ddmSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmSupplyVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ddmSupplyVoltage.setUnits("thousandth of a volt")


class _DdmSupplyVoltageLowWarning_Type(Integer32):
    """Custom type ddmSupplyVoltageLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmSupplyVoltageLowWarning_Type.__name__ = "Integer32"
_DdmSupplyVoltageLowWarning_Object = MibTableColumn
ddmSupplyVoltageLowWarning = _DdmSupplyVoltageLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 7),
    _DdmSupplyVoltageLowWarning_Type()
)
ddmSupplyVoltageLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmSupplyVoltageLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmSupplyVoltageLowWarning.setUnits("thousandth of a volt")


class _DdmSupplyVoltageLowAlarm_Type(Integer32):
    """Custom type ddmSupplyVoltageLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmSupplyVoltageLowAlarm_Type.__name__ = "Integer32"
_DdmSupplyVoltageLowAlarm_Object = MibTableColumn
ddmSupplyVoltageLowAlarm = _DdmSupplyVoltageLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 8),
    _DdmSupplyVoltageLowAlarm_Type()
)
ddmSupplyVoltageLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmSupplyVoltageLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmSupplyVoltageLowAlarm.setUnits("thousandth of a volt")


class _DdmSupplyVoltageHiWarning_Type(Integer32):
    """Custom type ddmSupplyVoltageHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmSupplyVoltageHiWarning_Type.__name__ = "Integer32"
_DdmSupplyVoltageHiWarning_Object = MibTableColumn
ddmSupplyVoltageHiWarning = _DdmSupplyVoltageHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 9),
    _DdmSupplyVoltageHiWarning_Type()
)
ddmSupplyVoltageHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmSupplyVoltageHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmSupplyVoltageHiWarning.setUnits("thousandth of a volt")


class _DdmSupplyVoltageHiAlarm_Type(Integer32):
    """Custom type ddmSupplyVoltageHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmSupplyVoltageHiAlarm_Type.__name__ = "Integer32"
_DdmSupplyVoltageHiAlarm_Object = MibTableColumn
ddmSupplyVoltageHiAlarm = _DdmSupplyVoltageHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 10),
    _DdmSupplyVoltageHiAlarm_Type()
)
ddmSupplyVoltageHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmSupplyVoltageHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmSupplyVoltageHiAlarm.setUnits("thousandth of a volt")


class _DdmTxBiasCurrent_Type(Integer32):
    """Custom type ddmTxBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmTxBiasCurrent_Type.__name__ = "Integer32"
_DdmTxBiasCurrent_Object = MibTableColumn
ddmTxBiasCurrent = _DdmTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 11),
    _DdmTxBiasCurrent_Type()
)
ddmTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxBiasCurrent.setUnits("thousandth of a milli-Ampere")


class _DdmTxBiasCurrentLowWarning_Type(Integer32):
    """Custom type ddmTxBiasCurrentLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmTxBiasCurrentLowWarning_Type.__name__ = "Integer32"
_DdmTxBiasCurrentLowWarning_Object = MibTableColumn
ddmTxBiasCurrentLowWarning = _DdmTxBiasCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 12),
    _DdmTxBiasCurrentLowWarning_Type()
)
ddmTxBiasCurrentLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentLowWarning.setUnits("thousandth of a milli-Ampere")


class _DdmTxBiasCurrentLowAlarm_Type(Integer32):
    """Custom type ddmTxBiasCurrentLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmTxBiasCurrentLowAlarm_Type.__name__ = "Integer32"
_DdmTxBiasCurrentLowAlarm_Object = MibTableColumn
ddmTxBiasCurrentLowAlarm = _DdmTxBiasCurrentLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 13),
    _DdmTxBiasCurrentLowAlarm_Type()
)
ddmTxBiasCurrentLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentLowAlarm.setUnits("thousandth of a milli-Ampere")


class _DdmTxBiasCurrentHiWarning_Type(Integer32):
    """Custom type ddmTxBiasCurrentHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmTxBiasCurrentHiWarning_Type.__name__ = "Integer32"
_DdmTxBiasCurrentHiWarning_Object = MibTableColumn
ddmTxBiasCurrentHiWarning = _DdmTxBiasCurrentHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 14),
    _DdmTxBiasCurrentHiWarning_Type()
)
ddmTxBiasCurrentHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentHiWarning.setUnits("thousandth of a milli-Ampere")


class _DdmTxBiasCurrentHiAlarm_Type(Integer32):
    """Custom type ddmTxBiasCurrentHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmTxBiasCurrentHiAlarm_Type.__name__ = "Integer32"
_DdmTxBiasCurrentHiAlarm_Object = MibTableColumn
ddmTxBiasCurrentHiAlarm = _DdmTxBiasCurrentHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 15),
    _DdmTxBiasCurrentHiAlarm_Type()
)
ddmTxBiasCurrentHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentHiAlarm.setUnits("thousandth of a milli-Ampere")


class _DdmTxOutputPower_Type(Integer32):
    """Custom type ddmTxOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmTxOutputPower_Type.__name__ = "Integer32"
_DdmTxOutputPower_Object = MibTableColumn
ddmTxOutputPower = _DdmTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 16),
    _DdmTxOutputPower_Type()
)
ddmTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxOutputPower.setUnits("thousandth of a dBm")


class _DdmTxOutputPowerLowWarning_Type(Integer32):
    """Custom type ddmTxOutputPowerLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmTxOutputPowerLowWarning_Type.__name__ = "Integer32"
_DdmTxOutputPowerLowWarning_Object = MibTableColumn
ddmTxOutputPowerLowWarning = _DdmTxOutputPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 17),
    _DdmTxOutputPowerLowWarning_Type()
)
ddmTxOutputPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxOutputPowerLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxOutputPowerLowWarning.setUnits("thousandth of a dBm")


class _DdmTxOutputPowerLowAlarm_Type(Integer32):
    """Custom type ddmTxOutputPowerLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmTxOutputPowerLowAlarm_Type.__name__ = "Integer32"
_DdmTxOutputPowerLowAlarm_Object = MibTableColumn
ddmTxOutputPowerLowAlarm = _DdmTxOutputPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 18),
    _DdmTxOutputPowerLowAlarm_Type()
)
ddmTxOutputPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxOutputPowerLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxOutputPowerLowAlarm.setUnits("thousandth of a dBm")


class _DdmTxOutputPowerHiWarning_Type(Integer32):
    """Custom type ddmTxOutputPowerHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmTxOutputPowerHiWarning_Type.__name__ = "Integer32"
_DdmTxOutputPowerHiWarning_Object = MibTableColumn
ddmTxOutputPowerHiWarning = _DdmTxOutputPowerHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 19),
    _DdmTxOutputPowerHiWarning_Type()
)
ddmTxOutputPowerHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxOutputPowerHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxOutputPowerHiWarning.setUnits("thousandth of a dBm")


class _DdmTxOutputPowerHiAlarm_Type(Integer32):
    """Custom type ddmTxOutputPowerHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmTxOutputPowerHiAlarm_Type.__name__ = "Integer32"
_DdmTxOutputPowerHiAlarm_Object = MibTableColumn
ddmTxOutputPowerHiAlarm = _DdmTxOutputPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 20),
    _DdmTxOutputPowerHiAlarm_Type()
)
ddmTxOutputPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxOutputPowerHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxOutputPowerHiAlarm.setUnits("thousandth of a dBm")


class _DdmRxOpticalPower_Type(Integer32):
    """Custom type ddmRxOpticalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmRxOpticalPower_Type.__name__ = "Integer32"
_DdmRxOpticalPower_Object = MibTableColumn
ddmRxOpticalPower = _DdmRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 21),
    _DdmRxOpticalPower_Type()
)
ddmRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    ddmRxOpticalPower.setUnits("thousandth of a dBm")


class _DdmRxOpticalPowerLowWarning_Type(Integer32):
    """Custom type ddmRxOpticalPowerLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmRxOpticalPowerLowWarning_Type.__name__ = "Integer32"
_DdmRxOpticalPowerLowWarning_Object = MibTableColumn
ddmRxOpticalPowerLowWarning = _DdmRxOpticalPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 22),
    _DdmRxOpticalPowerLowWarning_Type()
)
ddmRxOpticalPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerLowWarning.setUnits("thousandth of a dBm")


class _DdmRxOpticalPowerLowAlarm_Type(Integer32):
    """Custom type ddmRxOpticalPowerLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmRxOpticalPowerLowAlarm_Type.__name__ = "Integer32"
_DdmRxOpticalPowerLowAlarm_Object = MibTableColumn
ddmRxOpticalPowerLowAlarm = _DdmRxOpticalPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 23),
    _DdmRxOpticalPowerLowAlarm_Type()
)
ddmRxOpticalPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerLowAlarm.setUnits("thousandth of a dBm")


class _DdmRxOpticalPowerHiWarning_Type(Integer32):
    """Custom type ddmRxOpticalPowerHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmRxOpticalPowerHiWarning_Type.__name__ = "Integer32"
_DdmRxOpticalPowerHiWarning_Object = MibTableColumn
ddmRxOpticalPowerHiWarning = _DdmRxOpticalPowerHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 24),
    _DdmRxOpticalPowerHiWarning_Type()
)
ddmRxOpticalPowerHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerHiWarning.setUnits("thousandth of a dBm")


class _DdmRxOpticalPowerHiAlarm_Type(Integer32):
    """Custom type ddmRxOpticalPowerHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmRxOpticalPowerHiAlarm_Type.__name__ = "Integer32"
_DdmRxOpticalPowerHiAlarm_Object = MibTableColumn
ddmRxOpticalPowerHiAlarm = _DdmRxOpticalPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 5, 1, 25),
    _DdmRxOpticalPowerHiAlarm_Type()
)
ddmRxOpticalPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerHiAlarm.setUnits("thousandth of a dBm")
_DdmPortInfoTable_Object = MibTable
ddmPortInfoTable = _DdmPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ddmPortInfoTable.setStatus("current")
_DdmPortInfoEntry_Object = MibTableRow
ddmPortInfoEntry = _DdmPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1)
)
ddmPortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALCATEL-IND1-PORT-MIB", "ddmPortChannel"),
)
if mibBuilder.loadTexts:
    ddmPortInfoEntry.setStatus("current")


class _DdmPortChannel_Type(Integer32):
    """Custom type ddmPortChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DdmPortChannel_Type.__name__ = "Integer32"
_DdmPortChannel_Object = MibTableColumn
ddmPortChannel = _DdmPortChannel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 1),
    _DdmPortChannel_Type()
)
ddmPortChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortChannel.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortChannel.setUnits("QSFP/SFP channel number")


class _DdmPortTemperature_Type(Integer32):
    """Custom type ddmPortTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmPortTemperature_Type.__name__ = "Integer32"
_DdmPortTemperature_Object = MibTableColumn
ddmPortTemperature = _DdmPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 2),
    _DdmPortTemperature_Type()
)
ddmPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTemperature.setUnits("thousandth of a degree celcius")


class _DdmPortTempLowWarning_Type(Integer32):
    """Custom type ddmPortTempLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmPortTempLowWarning_Type.__name__ = "Integer32"
_DdmPortTempLowWarning_Object = MibTableColumn
ddmPortTempLowWarning = _DdmPortTempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 3),
    _DdmPortTempLowWarning_Type()
)
ddmPortTempLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTempLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTempLowWarning.setUnits("thousandth of a degree celcius")


class _DdmPortTempLowAlarm_Type(Integer32):
    """Custom type ddmPortTempLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmPortTempLowAlarm_Type.__name__ = "Integer32"
_DdmPortTempLowAlarm_Object = MibTableColumn
ddmPortTempLowAlarm = _DdmPortTempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 4),
    _DdmPortTempLowAlarm_Type()
)
ddmPortTempLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTempLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTempLowAlarm.setUnits("thousandth of a degree celcius")


class _DdmPortTempHiWarning_Type(Integer32):
    """Custom type ddmPortTempHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmPortTempHiWarning_Type.__name__ = "Integer32"
_DdmPortTempHiWarning_Object = MibTableColumn
ddmPortTempHiWarning = _DdmPortTempHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 5),
    _DdmPortTempHiWarning_Type()
)
ddmPortTempHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTempHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTempHiWarning.setUnits("thousandth of a degree celcius")


class _DdmPortTempHiAlarm_Type(Integer32):
    """Custom type ddmPortTempHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmPortTempHiAlarm_Type.__name__ = "Integer32"
_DdmPortTempHiAlarm_Object = MibTableColumn
ddmPortTempHiAlarm = _DdmPortTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 6),
    _DdmPortTempHiAlarm_Type()
)
ddmPortTempHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTempHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTempHiAlarm.setUnits("thousandth of a degree celcius")


class _DdmPortSupplyVoltage_Type(Integer32):
    """Custom type ddmPortSupplyVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmPortSupplyVoltage_Type.__name__ = "Integer32"
_DdmPortSupplyVoltage_Object = MibTableColumn
ddmPortSupplyVoltage = _DdmPortSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 7),
    _DdmPortSupplyVoltage_Type()
)
ddmPortSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortSupplyVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortSupplyVoltage.setUnits("thousandth of a volt")


class _DdmPortSupplyVoltageLowWarning_Type(Integer32):
    """Custom type ddmPortSupplyVoltageLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmPortSupplyVoltageLowWarning_Type.__name__ = "Integer32"
_DdmPortSupplyVoltageLowWarning_Object = MibTableColumn
ddmPortSupplyVoltageLowWarning = _DdmPortSupplyVoltageLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 8),
    _DdmPortSupplyVoltageLowWarning_Type()
)
ddmPortSupplyVoltageLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortSupplyVoltageLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortSupplyVoltageLowWarning.setUnits("thousandth of a volt")


class _DdmPortSupplyVoltageLowAlarm_Type(Integer32):
    """Custom type ddmPortSupplyVoltageLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmPortSupplyVoltageLowAlarm_Type.__name__ = "Integer32"
_DdmPortSupplyVoltageLowAlarm_Object = MibTableColumn
ddmPortSupplyVoltageLowAlarm = _DdmPortSupplyVoltageLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 9),
    _DdmPortSupplyVoltageLowAlarm_Type()
)
ddmPortSupplyVoltageLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortSupplyVoltageLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortSupplyVoltageLowAlarm.setUnits("thousandth of a volt")


class _DdmPortSupplyVoltageHiWarning_Type(Integer32):
    """Custom type ddmPortSupplyVoltageHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmPortSupplyVoltageHiWarning_Type.__name__ = "Integer32"
_DdmPortSupplyVoltageHiWarning_Object = MibTableColumn
ddmPortSupplyVoltageHiWarning = _DdmPortSupplyVoltageHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 10),
    _DdmPortSupplyVoltageHiWarning_Type()
)
ddmPortSupplyVoltageHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortSupplyVoltageHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortSupplyVoltageHiWarning.setUnits("thousandth of a volt")


class _DdmPortSupplyVoltageHiAlarm_Type(Integer32):
    """Custom type ddmPortSupplyVoltageHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmPortSupplyVoltageHiAlarm_Type.__name__ = "Integer32"
_DdmPortSupplyVoltageHiAlarm_Object = MibTableColumn
ddmPortSupplyVoltageHiAlarm = _DdmPortSupplyVoltageHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 11),
    _DdmPortSupplyVoltageHiAlarm_Type()
)
ddmPortSupplyVoltageHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortSupplyVoltageHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortSupplyVoltageHiAlarm.setUnits("thousandth of a volt")


class _DdmPortTxBiasCurrent_Type(Integer32):
    """Custom type ddmPortTxBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmPortTxBiasCurrent_Type.__name__ = "Integer32"
_DdmPortTxBiasCurrent_Object = MibTableColumn
ddmPortTxBiasCurrent = _DdmPortTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 12),
    _DdmPortTxBiasCurrent_Type()
)
ddmPortTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTxBiasCurrent.setUnits("thousandth of a milli-Ampere")


class _DdmPortTxBiasCurrentLowWarning_Type(Integer32):
    """Custom type ddmPortTxBiasCurrentLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmPortTxBiasCurrentLowWarning_Type.__name__ = "Integer32"
_DdmPortTxBiasCurrentLowWarning_Object = MibTableColumn
ddmPortTxBiasCurrentLowWarning = _DdmPortTxBiasCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 13),
    _DdmPortTxBiasCurrentLowWarning_Type()
)
ddmPortTxBiasCurrentLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxBiasCurrentLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTxBiasCurrentLowWarning.setUnits("thousandth of a milli-Ampere")


class _DdmPortTxBiasCurrentLowAlarm_Type(Integer32):
    """Custom type ddmPortTxBiasCurrentLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmPortTxBiasCurrentLowAlarm_Type.__name__ = "Integer32"
_DdmPortTxBiasCurrentLowAlarm_Object = MibTableColumn
ddmPortTxBiasCurrentLowAlarm = _DdmPortTxBiasCurrentLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 14),
    _DdmPortTxBiasCurrentLowAlarm_Type()
)
ddmPortTxBiasCurrentLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxBiasCurrentLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTxBiasCurrentLowAlarm.setUnits("thousandth of a milli-Ampere")


class _DdmPortTxBiasCurrentHiWarning_Type(Integer32):
    """Custom type ddmPortTxBiasCurrentHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmPortTxBiasCurrentHiWarning_Type.__name__ = "Integer32"
_DdmPortTxBiasCurrentHiWarning_Object = MibTableColumn
ddmPortTxBiasCurrentHiWarning = _DdmPortTxBiasCurrentHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 15),
    _DdmPortTxBiasCurrentHiWarning_Type()
)
ddmPortTxBiasCurrentHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxBiasCurrentHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTxBiasCurrentHiWarning.setUnits("thousandth of a milli-Ampere")


class _DdmPortTxBiasCurrentHiAlarm_Type(Integer32):
    """Custom type ddmPortTxBiasCurrentHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmPortTxBiasCurrentHiAlarm_Type.__name__ = "Integer32"
_DdmPortTxBiasCurrentHiAlarm_Object = MibTableColumn
ddmPortTxBiasCurrentHiAlarm = _DdmPortTxBiasCurrentHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 16),
    _DdmPortTxBiasCurrentHiAlarm_Type()
)
ddmPortTxBiasCurrentHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxBiasCurrentHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTxBiasCurrentHiAlarm.setUnits("thousandth of a milli-Ampere")


class _DdmPortTxOutputPower_Type(Integer32):
    """Custom type ddmPortTxOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmPortTxOutputPower_Type.__name__ = "Integer32"
_DdmPortTxOutputPower_Object = MibTableColumn
ddmPortTxOutputPower = _DdmPortTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 17),
    _DdmPortTxOutputPower_Type()
)
ddmPortTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTxOutputPower.setUnits("thousandth of a dBm")


class _DdmPortTxOutputPowerLowWarning_Type(Integer32):
    """Custom type ddmPortTxOutputPowerLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmPortTxOutputPowerLowWarning_Type.__name__ = "Integer32"
_DdmPortTxOutputPowerLowWarning_Object = MibTableColumn
ddmPortTxOutputPowerLowWarning = _DdmPortTxOutputPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 18),
    _DdmPortTxOutputPowerLowWarning_Type()
)
ddmPortTxOutputPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxOutputPowerLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTxOutputPowerLowWarning.setUnits("thousandth of a dBm")


class _DdmPortTxOutputPowerLowAlarm_Type(Integer32):
    """Custom type ddmPortTxOutputPowerLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmPortTxOutputPowerLowAlarm_Type.__name__ = "Integer32"
_DdmPortTxOutputPowerLowAlarm_Object = MibTableColumn
ddmPortTxOutputPowerLowAlarm = _DdmPortTxOutputPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 19),
    _DdmPortTxOutputPowerLowAlarm_Type()
)
ddmPortTxOutputPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxOutputPowerLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTxOutputPowerLowAlarm.setUnits("thousandth of a dBm")


class _DdmPortTxOutputPowerHiWarning_Type(Integer32):
    """Custom type ddmPortTxOutputPowerHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmPortTxOutputPowerHiWarning_Type.__name__ = "Integer32"
_DdmPortTxOutputPowerHiWarning_Object = MibTableColumn
ddmPortTxOutputPowerHiWarning = _DdmPortTxOutputPowerHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 20),
    _DdmPortTxOutputPowerHiWarning_Type()
)
ddmPortTxOutputPowerHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxOutputPowerHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTxOutputPowerHiWarning.setUnits("thousandth of a dBm")


class _DdmPortTxOutputPowerHiAlarm_Type(Integer32):
    """Custom type ddmPortTxOutputPowerHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmPortTxOutputPowerHiAlarm_Type.__name__ = "Integer32"
_DdmPortTxOutputPowerHiAlarm_Object = MibTableColumn
ddmPortTxOutputPowerHiAlarm = _DdmPortTxOutputPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 21),
    _DdmPortTxOutputPowerHiAlarm_Type()
)
ddmPortTxOutputPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxOutputPowerHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortTxOutputPowerHiAlarm.setUnits("thousandth of a dBm")


class _DdmPortRxOpticalPower_Type(Integer32):
    """Custom type ddmPortRxOpticalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmPortRxOpticalPower_Type.__name__ = "Integer32"
_DdmPortRxOpticalPower_Object = MibTableColumn
ddmPortRxOpticalPower = _DdmPortRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 22),
    _DdmPortRxOpticalPower_Type()
)
ddmPortRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortRxOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortRxOpticalPower.setUnits("thousandth of a dBm")


class _DdmPortRxOpticalPowerLowWarning_Type(Integer32):
    """Custom type ddmPortRxOpticalPowerLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmPortRxOpticalPowerLowWarning_Type.__name__ = "Integer32"
_DdmPortRxOpticalPowerLowWarning_Object = MibTableColumn
ddmPortRxOpticalPowerLowWarning = _DdmPortRxOpticalPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 23),
    _DdmPortRxOpticalPowerLowWarning_Type()
)
ddmPortRxOpticalPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortRxOpticalPowerLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortRxOpticalPowerLowWarning.setUnits("thousandth of a dBm")


class _DdmPortRxOpticalPowerLowAlarm_Type(Integer32):
    """Custom type ddmPortRxOpticalPowerLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmPortRxOpticalPowerLowAlarm_Type.__name__ = "Integer32"
_DdmPortRxOpticalPowerLowAlarm_Object = MibTableColumn
ddmPortRxOpticalPowerLowAlarm = _DdmPortRxOpticalPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 24),
    _DdmPortRxOpticalPowerLowAlarm_Type()
)
ddmPortRxOpticalPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortRxOpticalPowerLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortRxOpticalPowerLowAlarm.setUnits("thousandth of a dBm")


class _DdmPortRxOpticalPowerHiWarning_Type(Integer32):
    """Custom type ddmPortRxOpticalPowerHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmPortRxOpticalPowerHiWarning_Type.__name__ = "Integer32"
_DdmPortRxOpticalPowerHiWarning_Object = MibTableColumn
ddmPortRxOpticalPowerHiWarning = _DdmPortRxOpticalPowerHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 25),
    _DdmPortRxOpticalPowerHiWarning_Type()
)
ddmPortRxOpticalPowerHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortRxOpticalPowerHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortRxOpticalPowerHiWarning.setUnits("thousandth of a dBm")


class _DdmPortRxOpticalPowerHiAlarm_Type(Integer32):
    """Custom type ddmPortRxOpticalPowerHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmPortRxOpticalPowerHiAlarm_Type.__name__ = "Integer32"
_DdmPortRxOpticalPowerHiAlarm_Object = MibTableColumn
ddmPortRxOpticalPowerHiAlarm = _DdmPortRxOpticalPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 6, 1, 26),
    _DdmPortRxOpticalPowerHiAlarm_Type()
)
ddmPortRxOpticalPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortRxOpticalPowerHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmPortRxOpticalPowerHiAlarm.setUnits("thousandth of a dBm")
_AlcfcStatsTable_Object = MibTable
alcfcStatsTable = _AlcfcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    alcfcStatsTable.setStatus("current")
_AlcfcStatsEntry_Object = MibTableRow
alcfcStatsEntry = _AlcfcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1)
)
alcfcStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alcfcStatsEntry.setStatus("current")


class _AlcfcClearStats_Type(Integer32):
    """Custom type alcfcClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlcfcClearStats_Type.__name__ = "Integer32"
_AlcfcClearStats_Object = MibTableColumn
alcfcClearStats = _AlcfcClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 1),
    _AlcfcClearStats_Type()
)
alcfcClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcfcClearStats.setStatus("current")
_AlcfcLastClearStats_Type = TimeTicks
_AlcfcLastClearStats_Object = MibTableColumn
alcfcLastClearStats = _AlcfcLastClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 2),
    _AlcfcLastClearStats_Type()
)
alcfcLastClearStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcLastClearStats.setStatus("current")
_AlcfcStatsRxUndersizePkts_Type = Counter64
_AlcfcStatsRxUndersizePkts_Object = MibTableColumn
alcfcStatsRxUndersizePkts = _AlcfcStatsRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 3),
    _AlcfcStatsRxUndersizePkts_Type()
)
alcfcStatsRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsRxUndersizePkts.setStatus("current")
_AlcfcStatsTxBBCreditZeros_Type = Counter64
_AlcfcStatsTxBBCreditZeros_Object = MibTableColumn
alcfcStatsTxBBCreditZeros = _AlcfcStatsTxBBCreditZeros_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 6),
    _AlcfcStatsTxBBCreditZeros_Type()
)
alcfcStatsTxBBCreditZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsTxBBCreditZeros.setStatus("current")
_AlcfcStatsRxBBCreditZeros_Type = Counter64
_AlcfcStatsRxBBCreditZeros_Object = MibTableColumn
alcfcStatsRxBBCreditZeros = _AlcfcStatsRxBBCreditZeros_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 7),
    _AlcfcStatsRxBBCreditZeros_Type()
)
alcfcStatsRxBBCreditZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsRxBBCreditZeros.setStatus("current")
_AlcfcStatsLinkFailures_Type = Counter64
_AlcfcStatsLinkFailures_Object = MibTableColumn
alcfcStatsLinkFailures = _AlcfcStatsLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 8),
    _AlcfcStatsLinkFailures_Type()
)
alcfcStatsLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsLinkFailures.setStatus("current")
_AlcfcStatsLossofSynchs_Type = Counter64
_AlcfcStatsLossofSynchs_Object = MibTableColumn
alcfcStatsLossofSynchs = _AlcfcStatsLossofSynchs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 9),
    _AlcfcStatsLossofSynchs_Type()
)
alcfcStatsLossofSynchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsLossofSynchs.setStatus("current")
_AlcfcStatsLossofSignals_Type = Counter64
_AlcfcStatsLossofSignals_Object = MibTableColumn
alcfcStatsLossofSignals = _AlcfcStatsLossofSignals_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 10),
    _AlcfcStatsLossofSignals_Type()
)
alcfcStatsLossofSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsLossofSignals.setStatus("current")
_AlcfcStatsPrimSeqProtocolErrors_Type = Counter64
_AlcfcStatsPrimSeqProtocolErrors_Object = MibTableColumn
alcfcStatsPrimSeqProtocolErrors = _AlcfcStatsPrimSeqProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 11),
    _AlcfcStatsPrimSeqProtocolErrors_Type()
)
alcfcStatsPrimSeqProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsPrimSeqProtocolErrors.setStatus("current")
_AlcfcStatsInvalidTxWords_Type = Counter64
_AlcfcStatsInvalidTxWords_Object = MibTableColumn
alcfcStatsInvalidTxWords = _AlcfcStatsInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 12),
    _AlcfcStatsInvalidTxWords_Type()
)
alcfcStatsInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsInvalidTxWords.setStatus("current")
_AlcfcStatsInvalidCRCs_Type = Counter64
_AlcfcStatsInvalidCRCs_Object = MibTableColumn
alcfcStatsInvalidCRCs = _AlcfcStatsInvalidCRCs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 13),
    _AlcfcStatsInvalidCRCs_Type()
)
alcfcStatsInvalidCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsInvalidCRCs.setStatus("current")
_AlcfcStatsInvalidOrderedSets_Type = Counter64
_AlcfcStatsInvalidOrderedSets_Object = MibTableColumn
alcfcStatsInvalidOrderedSets = _AlcfcStatsInvalidOrderedSets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 14),
    _AlcfcStatsInvalidOrderedSets_Type()
)
alcfcStatsInvalidOrderedSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsInvalidOrderedSets.setStatus("current")
_AlcfcStatsFrameTooLongs_Type = Counter64
_AlcfcStatsFrameTooLongs_Object = MibTableColumn
alcfcStatsFrameTooLongs = _AlcfcStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 15),
    _AlcfcStatsFrameTooLongs_Type()
)
alcfcStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsFrameTooLongs.setStatus("current")
_AlcfcStatsDelimiterErrors_Type = Counter64
_AlcfcStatsDelimiterErrors_Object = MibTableColumn
alcfcStatsDelimiterErrors = _AlcfcStatsDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 16),
    _AlcfcStatsDelimiterErrors_Type()
)
alcfcStatsDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsDelimiterErrors.setStatus("current")
_AlcfcStatsEncodingDisparityErrors_Type = Counter64
_AlcfcStatsEncodingDisparityErrors_Object = MibTableColumn
alcfcStatsEncodingDisparityErrors = _AlcfcStatsEncodingDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 17),
    _AlcfcStatsEncodingDisparityErrors_Type()
)
alcfcStatsEncodingDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsEncodingDisparityErrors.setStatus("current")
_AlcfcStatsOtherErrors_Type = Counter64
_AlcfcStatsOtherErrors_Object = MibTableColumn
alcfcStatsOtherErrors = _AlcfcStatsOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 2, 7, 1, 18),
    _AlcfcStatsOtherErrors_Type()
)
alcfcStatsOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcfcStatsOtherErrors.setStatus("current")
_DdmConfiguration_ObjectIdentity = ObjectIdentity
ddmConfiguration = _DdmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 4)
)


class _DdmConfig_Type(Integer32):
    """Custom type ddmConfig based on Integer32"""
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


_DdmConfig_Type.__name__ = "Integer32"
_DdmConfig_Object = MibScalar
ddmConfig = _DdmConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 4, 1),
    _DdmConfig_Type()
)
ddmConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmConfig.setStatus("current")


class _DdmTrapConfig_Type(Integer32):
    """Custom type ddmTrapConfig based on Integer32"""
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


_DdmTrapConfig_Type.__name__ = "Integer32"
_DdmTrapConfig_Object = MibScalar
ddmTrapConfig = _DdmTrapConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 4, 2),
    _DdmTrapConfig_Type()
)
ddmTrapConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmTrapConfig.setStatus("current")


class _DdmNotificationType_Type(Integer32):
    """Custom type ddmNotificationType based on Integer32"""
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
        *(("clearViolation", 1),
          ("highAlarm", 2),
          ("highWarning", 3),
          ("lowAlarm", 5),
          ("lowWarning", 4))
    )


_DdmNotificationType_Type.__name__ = "Integer32"
_DdmNotificationType_Object = MibScalar
ddmNotificationType = _DdmNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 4, 3),
    _DdmNotificationType_Type()
)
ddmNotificationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ddmNotificationType.setStatus("current")
_PortViolations_ObjectIdentity = ObjectIdentity
portViolations = _PortViolations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5)
)
_PortViolationTable_Object = MibTable
portViolationTable = _PortViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    portViolationTable.setStatus("current")
_PortViolationEntry_Object = MibTableRow
portViolationEntry = _PortViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 1, 1)
)
portViolationEntry.setIndexNames(
    (0, "ALCATEL-IND1-PORT-MIB", "portViolationIfIndex"),
    (0, "ALCATEL-IND1-PORT-MIB", "portViolationSource"),
    (0, "ALCATEL-IND1-PORT-MIB", "portViolationReason"),
)
if mibBuilder.loadTexts:
    portViolationEntry.setStatus("current")
_PortViolationIfIndex_Type = InterfaceIndex
_PortViolationIfIndex_Object = MibTableColumn
portViolationIfIndex = _PortViolationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 1, 1, 1),
    _PortViolationIfIndex_Type()
)
portViolationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portViolationIfIndex.setStatus("current")


class _PortViolationSource_Type(Integer32):
    """Custom type portViolationSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("lfp", 8),
          ("lm", 9),
          ("netsec", 3),
          ("nisup", 5),
          ("qos", 2),
          ("srcLrn", 1),
          ("udld", 4))
    )


_PortViolationSource_Type.__name__ = "Integer32"
_PortViolationSource_Object = MibTableColumn
portViolationSource = _PortViolationSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 1, 1, 2),
    _PortViolationSource_Type()
)
portViolationSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portViolationSource.setStatus("current")


class _PortViolationReason_Type(Integer32):
    """Custom type portViolationReason based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("pvLfpShutDown", 17),
          ("pvQosBgp", 6),
          ("pvQosBpdu", 5),
          ("pvQosDhcp", 10),
          ("pvQosDnsReply", 14),
          ("pvQosDvmrp", 12),
          ("pvQosIsis", 13),
          ("pvQosOspf", 7),
          ("pvQosPim", 11),
          ("pvQosPolicy", 3),
          ("pvQosRip", 8),
          ("pvQosSpoofed", 4),
          ("pvQosVrrp", 9),
          ("pvSLLpsRestrict", 2),
          ("pvSLLpsShutDown", 1),
          ("pvUdld", 15))
    )


_PortViolationReason_Type.__name__ = "Integer32"
_PortViolationReason_Object = MibTableColumn
portViolationReason = _PortViolationReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 1, 1, 3),
    _PortViolationReason_Type()
)
portViolationReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portViolationReason.setStatus("current")


class _PortViolationAction_Type(Integer32):
    """Custom type portViolationAction based on Integer32"""
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
        *(("portAdminDown", 2),
          ("portDown", 1),
          ("portTimerAdminDown", 4),
          ("portTimerDown", 3))
    )


_PortViolationAction_Type.__name__ = "Integer32"
_PortViolationAction_Object = MibTableColumn
portViolationAction = _PortViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 1, 1, 4),
    _PortViolationAction_Type()
)
portViolationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portViolationAction.setStatus("current")
_PortViolationTimer_Type = TimeTicks
_PortViolationTimer_Object = MibTableColumn
portViolationTimer = _PortViolationTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 1, 1, 5),
    _PortViolationTimer_Type()
)
portViolationTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portViolationTimer.setStatus("current")


class _PortViolationTimerAction_Type(Integer32):
    """Custom type portViolationTimerAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portDownAfterTimer", 1),
          ("portNoTimerAction", 0),
          ("portUpAfterTimer", 2))
    )


_PortViolationTimerAction_Type.__name__ = "Integer32"
_PortViolationTimerAction_Object = MibTableColumn
portViolationTimerAction = _PortViolationTimerAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 1, 1, 6),
    _PortViolationTimerAction_Type()
)
portViolationTimerAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portViolationTimerAction.setStatus("current")


class _PortViolationClearPort_Type(Integer32):
    """Custom type portViolationClearPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("set", 1))
    )


_PortViolationClearPort_Type.__name__ = "Integer32"
_PortViolationClearPort_Object = MibTableColumn
portViolationClearPort = _PortViolationClearPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 1, 1, 7),
    _PortViolationClearPort_Type()
)
portViolationClearPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portViolationClearPort.setStatus("current")
_AlaLinkMonConfigTable_Object = MibTable
alaLinkMonConfigTable = _AlaLinkMonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    alaLinkMonConfigTable.setStatus("current")
_AlaLinkMonConfigEntry_Object = MibTableRow
alaLinkMonConfigEntry = _AlaLinkMonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 2, 1)
)
alaLinkMonConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alaLinkMonConfigEntry.setStatus("current")


class _AlaLinkMonStatus_Type(Integer32):
    """Custom type alaLinkMonStatus based on Integer32"""
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


_AlaLinkMonStatus_Type.__name__ = "Integer32"
_AlaLinkMonStatus_Object = MibTableColumn
alaLinkMonStatus = _AlaLinkMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 2, 1, 1),
    _AlaLinkMonStatus_Type()
)
alaLinkMonStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLinkMonStatus.setStatus("current")


class _AlaLinkMonTimeWindow_Type(Integer32):
    """Custom type alaLinkMonTimeWindow based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_AlaLinkMonTimeWindow_Type.__name__ = "Integer32"
_AlaLinkMonTimeWindow_Object = MibTableColumn
alaLinkMonTimeWindow = _AlaLinkMonTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 2, 1, 2),
    _AlaLinkMonTimeWindow_Type()
)
alaLinkMonTimeWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLinkMonTimeWindow.setStatus("current")


class _AlaLinkMonLinkFlapThreshold_Type(Integer32):
    """Custom type alaLinkMonLinkFlapThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_AlaLinkMonLinkFlapThreshold_Type.__name__ = "Integer32"
_AlaLinkMonLinkFlapThreshold_Object = MibTableColumn
alaLinkMonLinkFlapThreshold = _AlaLinkMonLinkFlapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 2, 1, 3),
    _AlaLinkMonLinkFlapThreshold_Type()
)
alaLinkMonLinkFlapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLinkMonLinkFlapThreshold.setStatus("current")


class _AlaLinkMonLinkErrorThreshold_Type(Integer32):
    """Custom type alaLinkMonLinkErrorThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlaLinkMonLinkErrorThreshold_Type.__name__ = "Integer32"
_AlaLinkMonLinkErrorThreshold_Object = MibTableColumn
alaLinkMonLinkErrorThreshold = _AlaLinkMonLinkErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 2, 1, 4),
    _AlaLinkMonLinkErrorThreshold_Type()
)
alaLinkMonLinkErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLinkMonLinkErrorThreshold.setStatus("current")


class _AlaLinkMonWaitToRestoreTimer_Type(Integer32):
    """Custom type alaLinkMonWaitToRestoreTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AlaLinkMonWaitToRestoreTimer_Type.__name__ = "Integer32"
_AlaLinkMonWaitToRestoreTimer_Object = MibTableColumn
alaLinkMonWaitToRestoreTimer = _AlaLinkMonWaitToRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 2, 1, 5),
    _AlaLinkMonWaitToRestoreTimer_Type()
)
alaLinkMonWaitToRestoreTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLinkMonWaitToRestoreTimer.setStatus("current")


class _AlaLinkMonWaitToShutdownTimer_Type(Integer32):
    """Custom type alaLinkMonWaitToShutdownTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_AlaLinkMonWaitToShutdownTimer_Type.__name__ = "Integer32"
_AlaLinkMonWaitToShutdownTimer_Object = MibTableColumn
alaLinkMonWaitToShutdownTimer = _AlaLinkMonWaitToShutdownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 2, 1, 6),
    _AlaLinkMonWaitToShutdownTimer_Type()
)
alaLinkMonWaitToShutdownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLinkMonWaitToShutdownTimer.setStatus("current")
_AlaLinkMonStatsTable_Object = MibTable
alaLinkMonStatsTable = _AlaLinkMonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    alaLinkMonStatsTable.setStatus("current")
_AlaLinkMonStatsEntry_Object = MibTableRow
alaLinkMonStatsEntry = _AlaLinkMonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1)
)
alaLinkMonStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alaLinkMonStatsEntry.setStatus("current")


class _AlaLinkMonStatsClearStats_Type(Integer32):
    """Custom type alaLinkMonStatsClearStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaLinkMonStatsClearStats_Type.__name__ = "Integer32"
_AlaLinkMonStatsClearStats_Object = MibTableColumn
alaLinkMonStatsClearStats = _AlaLinkMonStatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1, 1),
    _AlaLinkMonStatsClearStats_Type()
)
alaLinkMonStatsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLinkMonStatsClearStats.setStatus("current")


class _AlaLinkMonStatsPortState_Type(Integer32):
    """Custom type alaLinkMonStatsPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("shutdown", 3),
          ("up", 1))
    )


_AlaLinkMonStatsPortState_Type.__name__ = "Integer32"
_AlaLinkMonStatsPortState_Object = MibTableColumn
alaLinkMonStatsPortState = _AlaLinkMonStatsPortState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1, 2),
    _AlaLinkMonStatsPortState_Type()
)
alaLinkMonStatsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLinkMonStatsPortState.setStatus("current")
_AlaLinkMonStatsCurrentLinkFlaps_Type = Counter64
_AlaLinkMonStatsCurrentLinkFlaps_Object = MibTableColumn
alaLinkMonStatsCurrentLinkFlaps = _AlaLinkMonStatsCurrentLinkFlaps_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1, 3),
    _AlaLinkMonStatsCurrentLinkFlaps_Type()
)
alaLinkMonStatsCurrentLinkFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLinkMonStatsCurrentLinkFlaps.setStatus("current")
_AlaLinkMonStatsCurrentErrorFrames_Type = Counter64
_AlaLinkMonStatsCurrentErrorFrames_Object = MibTableColumn
alaLinkMonStatsCurrentErrorFrames = _AlaLinkMonStatsCurrentErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1, 4),
    _AlaLinkMonStatsCurrentErrorFrames_Type()
)
alaLinkMonStatsCurrentErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLinkMonStatsCurrentErrorFrames.setStatus("current")
_AlaLinkMonStatsCurrentCRCErrors_Type = Counter64
_AlaLinkMonStatsCurrentCRCErrors_Object = MibTableColumn
alaLinkMonStatsCurrentCRCErrors = _AlaLinkMonStatsCurrentCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1, 5),
    _AlaLinkMonStatsCurrentCRCErrors_Type()
)
alaLinkMonStatsCurrentCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLinkMonStatsCurrentCRCErrors.setStatus("current")
_AlaLinkMonStatsCurrentLostFrames_Type = Counter64
_AlaLinkMonStatsCurrentLostFrames_Object = MibTableColumn
alaLinkMonStatsCurrentLostFrames = _AlaLinkMonStatsCurrentLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1, 6),
    _AlaLinkMonStatsCurrentLostFrames_Type()
)
alaLinkMonStatsCurrentLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLinkMonStatsCurrentLostFrames.setStatus("current")
_AlaLinkMonStatsCurrentAlignErrors_Type = Counter64
_AlaLinkMonStatsCurrentAlignErrors_Object = MibTableColumn
alaLinkMonStatsCurrentAlignErrors = _AlaLinkMonStatsCurrentAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1, 7),
    _AlaLinkMonStatsCurrentAlignErrors_Type()
)
alaLinkMonStatsCurrentAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLinkMonStatsCurrentAlignErrors.setStatus("current")
_AlaLinkMonStatsCurrentLinkErrors_Type = Counter64
_AlaLinkMonStatsCurrentLinkErrors_Object = MibTableColumn
alaLinkMonStatsCurrentLinkErrors = _AlaLinkMonStatsCurrentLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1, 8),
    _AlaLinkMonStatsCurrentLinkErrors_Type()
)
alaLinkMonStatsCurrentLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLinkMonStatsCurrentLinkErrors.setStatus("current")
_AlaLinkMonStatsTotalLinkFlaps_Type = Counter64
_AlaLinkMonStatsTotalLinkFlaps_Object = MibTableColumn
alaLinkMonStatsTotalLinkFlaps = _AlaLinkMonStatsTotalLinkFlaps_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1, 9),
    _AlaLinkMonStatsTotalLinkFlaps_Type()
)
alaLinkMonStatsTotalLinkFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLinkMonStatsTotalLinkFlaps.setStatus("current")
_AlaLinkMonStatsTotalLinkErrors_Type = Counter64
_AlaLinkMonStatsTotalLinkErrors_Object = MibTableColumn
alaLinkMonStatsTotalLinkErrors = _AlaLinkMonStatsTotalLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 3, 1, 10),
    _AlaLinkMonStatsTotalLinkErrors_Type()
)
alaLinkMonStatsTotalLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLinkMonStatsTotalLinkErrors.setStatus("current")
_AlaLFPGroupTable_Object = MibTable
alaLFPGroupTable = _AlaLFPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    alaLFPGroupTable.setStatus("current")
_AlaLFPGroupEntry_Object = MibTableRow
alaLFPGroupEntry = _AlaLFPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 4, 1)
)
alaLFPGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-PORT-MIB", "alaLFPGroupId"),
)
if mibBuilder.loadTexts:
    alaLFPGroupEntry.setStatus("current")


class _AlaLFPGroupId_Type(Integer32):
    """Custom type alaLFPGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaLFPGroupId_Type.__name__ = "Integer32"
_AlaLFPGroupId_Object = MibTableColumn
alaLFPGroupId = _AlaLFPGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 4, 1, 1),
    _AlaLFPGroupId_Type()
)
alaLFPGroupId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLFPGroupId.setStatus("current")


class _AlaLFPGroupAdminStatus_Type(Integer32):
    """Custom type alaLFPGroupAdminStatus based on Integer32"""
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


_AlaLFPGroupAdminStatus_Type.__name__ = "Integer32"
_AlaLFPGroupAdminStatus_Object = MibTableColumn
alaLFPGroupAdminStatus = _AlaLFPGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 4, 1, 2),
    _AlaLFPGroupAdminStatus_Type()
)
alaLFPGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLFPGroupAdminStatus.setStatus("current")


class _AlaLFPGroupOperStatus_Type(Integer32):
    """Custom type alaLFPGroupOperStatus based on Integer32"""
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


_AlaLFPGroupOperStatus_Type.__name__ = "Integer32"
_AlaLFPGroupOperStatus_Object = MibTableColumn
alaLFPGroupOperStatus = _AlaLFPGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 4, 1, 3),
    _AlaLFPGroupOperStatus_Type()
)
alaLFPGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLFPGroupOperStatus.setStatus("current")


class _AlaLFPGroupWaitToShutdown_Type(Integer32):
    """Custom type alaLFPGroupWaitToShutdown based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AlaLFPGroupWaitToShutdown_Type.__name__ = "Integer32"
_AlaLFPGroupWaitToShutdown_Object = MibTableColumn
alaLFPGroupWaitToShutdown = _AlaLFPGroupWaitToShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 4, 1, 4),
    _AlaLFPGroupWaitToShutdown_Type()
)
alaLFPGroupWaitToShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLFPGroupWaitToShutdown.setStatus("current")
_AlaLFPGroupRowStatus_Type = RowStatus
_AlaLFPGroupRowStatus_Object = MibTableColumn
alaLFPGroupRowStatus = _AlaLFPGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 4, 1, 5),
    _AlaLFPGroupRowStatus_Type()
)
alaLFPGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLFPGroupRowStatus.setStatus("current")
_AlaLFPConfigTable_Object = MibTable
alaLFPConfigTable = _AlaLFPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    alaLFPConfigTable.setStatus("current")
_AlaLFPConfigEntry_Object = MibTableRow
alaLFPConfigEntry = _AlaLFPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 5, 1)
)
alaLFPConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-PORT-MIB", "alaLFPGroupId"),
    (0, "ALCATEL-IND1-PORT-MIB", "alaLFPConfigPort"),
)
if mibBuilder.loadTexts:
    alaLFPConfigEntry.setStatus("current")
_AlaLFPConfigPort_Type = InterfaceIndex
_AlaLFPConfigPort_Object = MibTableColumn
alaLFPConfigPort = _AlaLFPConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 5, 1, 1),
    _AlaLFPConfigPort_Type()
)
alaLFPConfigPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLFPConfigPort.setStatus("current")


class _AlaLFPConfigPortType_Type(Integer32):
    """Custom type alaLFPConfigPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 1),
          ("source", 2))
    )


_AlaLFPConfigPortType_Type.__name__ = "Integer32"
_AlaLFPConfigPortType_Object = MibTableColumn
alaLFPConfigPortType = _AlaLFPConfigPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 5, 1, 2),
    _AlaLFPConfigPortType_Type()
)
alaLFPConfigPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLFPConfigPortType.setStatus("current")
_AlaLFPConfigRowStatus_Type = RowStatus
_AlaLFPConfigRowStatus_Object = MibTableColumn
alaLFPConfigRowStatus = _AlaLFPConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 5, 5, 1, 3),
    _AlaLFPConfigRowStatus_Type()
)
alaLFPConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLFPConfigRowStatus.setStatus("current")
_CsmConfTrap_ObjectIdentity = ObjectIdentity
csmConfTrap = _CsmConfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 6)
)
_AlaDyingGaspChassisId_Type = Integer32
_AlaDyingGaspChassisId_Object = MibScalar
alaDyingGaspChassisId = _AlaDyingGaspChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 6, 1),
    _AlaDyingGaspChassisId_Type()
)
alaDyingGaspChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDyingGaspChassisId.setStatus("current")


class _AlaDyingGaspPowerSupplyType_Type(Integer32):
    """Custom type alaDyingGaspPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1),
          ("saps", 3))
    )


_AlaDyingGaspPowerSupplyType_Type.__name__ = "Integer32"
_AlaDyingGaspPowerSupplyType_Object = MibScalar
alaDyingGaspPowerSupplyType = _AlaDyingGaspPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 6, 2),
    _AlaDyingGaspPowerSupplyType_Type()
)
alaDyingGaspPowerSupplyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDyingGaspPowerSupplyType.setStatus("current")
_AlaDyingGaspTime_Type = DateAndTime
_AlaDyingGaspTime_Object = MibScalar
alaDyingGaspTime = _AlaDyingGaspTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 1, 6, 3),
    _AlaDyingGaspTime_Type()
)
alaDyingGaspTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDyingGaspTime.setStatus("current")
_AlcatelIND1PortMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1PortMIBConformance = _AlcatelIND1PortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2)
)
_AlcatelIND1PortMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1PortMIBCompliances = _AlcatelIND1PortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 1)
)
_AlcatelIND1PortMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1PortMIBGroups = _AlcatelIND1PortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2)
)

# Managed Objects groups

esmConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 1)
)
esmConfMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmPortCfgSpeed"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgDuplexMode"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgMaxFrameSize"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgAutoNegotiation"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgCrossover"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgPause"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortBcastRateLimitEnable"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortBcastRateLimitType"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortBcastRateLimit"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortMcastRateLimitEnable"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortMcastRateLimitType"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortMcastRateLimit"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortUucastRateLimitEnable"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortUucastRateLimitType"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortUucastRateLimit"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortIngressRateLimitEnable"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortIngressRateLimit"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortIngressRateLimitBurst"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortEPPEnable"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortEEEEnable"))
)
if mibBuilder.loadTexts:
    esmConfMIBGroup.setStatus("current")

esmDetectedConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 2)
)
esmDetectedConfMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmPortAutoSpeed"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortAutoDuplexMode"))
)
if mibBuilder.loadTexts:
    esmDetectedConfMIBGroup.setStatus("current")

alcEtherStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 3)
)
alcEtherStatsMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "alcetherClearStats"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherLastClearStats"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsCRCAlignErrors"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxUndersizePkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxUndersizePkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxOversizePkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxJabbers"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxCollisions"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxCollisions"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts64Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts65to127Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts128to255Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts256to511Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts512to1023Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts1024to1518Octets"),
        ("ALCATEL-IND1-PORT-MIB", "gigaEtherStatsPkts1519to4095Octets"),
        ("ALCATEL-IND1-PORT-MIB", "gigaEtherStatsPkts4096to9215Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts1519to2047Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts2048to4095Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts4096Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxGiantPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxDribbleNibblePkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxLongEventPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxVlanTagPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxControlPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxLenChkErrPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxCodeErrPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxDvEventPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxPrevPktDropped"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx64Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx65to127Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx128to255Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx256to511Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx512to1023Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx1024to1518Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx1519to2047Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx2048to4095Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx4096Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxRetryCount"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxVlanTagPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxControlPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxLatePkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxTotalBytesOnWire"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxLenChkErrPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxExcDeferPkts"))
)
if mibBuilder.loadTexts:
    alcEtherStatsMIBGroup.setStatus("current")

ddmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 6)
)
ddmInfoGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "ddmTemperature"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTempLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTempLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTempHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTempHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltage"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltageLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltageLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltageHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltageHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrent"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrentLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrentLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrentHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrentHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPower"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPowerLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPowerLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPowerHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPowerHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPower"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPowerLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPowerLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPowerHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPowerHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortChannel"))
)
if mibBuilder.loadTexts:
    ddmInfoGroup.setStatus("current")

ddmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 7)
)
ddmConfigGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "ddmConfig"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTrapConfig"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"))
)
if mibBuilder.loadTexts:
    ddmConfigGroup.setStatus("current")

esmConfTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 9)
)
esmConfTrapGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmDrvTrapDrops"),
        ("ALCATEL-IND1-PORT-MIB", "alaDyingGaspChassisId"),
        ("ALCATEL-IND1-PORT-MIB", "alaDyingGaspPowerSupplyType"),
        ("ALCATEL-IND1-PORT-MIB", "alaDyingGaspTime"))
)
if mibBuilder.loadTexts:
    esmConfTrapGroup.setStatus("current")

esmHybridConfEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 10)
)
esmHybridConfEntryGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmHybridPortCfgSpeed"),
        ("ALCATEL-IND1-PORT-MIB", "esmHybridPortCfgDuplexMode"),
        ("ALCATEL-IND1-PORT-MIB", "esmHybridPortCfgAutoNegotiation"),
        ("ALCATEL-IND1-PORT-MIB", "esmHybridPortCfgCrossover"),
        ("ALCATEL-IND1-PORT-MIB", "esmHybridPortCfgFlow"),
        ("ALCATEL-IND1-PORT-MIB", "esmHybridPortCfgInactiveType"))
)
if mibBuilder.loadTexts:
    esmHybridConfEntryGroup.setStatus("current")

esmConfEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 11)
)
esmConfEntryGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmPortAdminStatus"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortAlias"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgHybridActiveType"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgHybridMode"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortIF"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortLinkUpDownTrapEnable"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortOperationalHybridType"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortSlot"))
)
if mibBuilder.loadTexts:
    esmConfEntryGroup.setStatus("current")

portViolationEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 12)
)
portViolationEntryGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "portViolationAction"),
        ("ALCATEL-IND1-PORT-MIB", "portViolationTimer"),
        ("ALCATEL-IND1-PORT-MIB", "portViolationTimerAction"),
        ("ALCATEL-IND1-PORT-MIB", "portViolationClearPort"))
)
if mibBuilder.loadTexts:
    portViolationEntryGroup.setStatus("current")

ddmPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 13)
)
ddmPortInfoGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "ddmPortTemperature"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTempLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTempLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTempHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTempHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortSupplyVoltage"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortSupplyVoltageLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortSupplyVoltageLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortSupplyVoltageHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortSupplyVoltageHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTxBiasCurrent"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTxBiasCurrentLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTxBiasCurrentLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTxBiasCurrentHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTxBiasCurrentHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTxOutputPower"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTxOutputPowerLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTxOutputPowerLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTxOutputPowerHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortTxOutputPowerHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortRxOpticalPower"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortRxOpticalPowerLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortRxOpticalPowerLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortRxOpticalPowerHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmPortRxOpticalPowerHiAlarm"))
)
if mibBuilder.loadTexts:
    ddmPortInfoGroup.setStatus("current")

alaLinkMonConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 14)
)
alaLinkMonConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatus"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonTimeWindow"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonLinkFlapThreshold"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonLinkErrorThreshold"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonWaitToRestoreTimer"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonWaitToShutdownTimer"))
)
if mibBuilder.loadTexts:
    alaLinkMonConfigMIBGroup.setStatus("current")

alaLinkMonStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 15)
)
alaLinkMonStatsMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatsClearStats"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatsPortState"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatsCurrentLinkFlaps"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatsCurrentErrorFrames"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatsCurrentCRCErrors"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatsCurrentLostFrames"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatsCurrentAlignErrors"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatsCurrentLinkErrors"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatsTotalLinkFlaps"),
        ("ALCATEL-IND1-PORT-MIB", "alaLinkMonStatsTotalLinkErrors"))
)
if mibBuilder.loadTexts:
    alaLinkMonStatsMIBGroup.setStatus("current")

alaLFPGroupMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 16)
)
alaLFPGroupMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "alaLFPGroupId"),
        ("ALCATEL-IND1-PORT-MIB", "alaLFPGroupAdminStatus"),
        ("ALCATEL-IND1-PORT-MIB", "alaLFPGroupOperStatus"),
        ("ALCATEL-IND1-PORT-MIB", "alaLFPGroupWaitToShutdown"),
        ("ALCATEL-IND1-PORT-MIB", "alaLFPGroupRowStatus"))
)
if mibBuilder.loadTexts:
    alaLFPGroupMIBGroup.setStatus("current")

alaLFPConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 17)
)
alaLFPConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "alaLFPConfigPort"),
        ("ALCATEL-IND1-PORT-MIB", "alaLFPConfigPortType"),
        ("ALCATEL-IND1-PORT-MIB", "alaLFPConfigRowStatus"))
)
if mibBuilder.loadTexts:
    alaLFPConfigMIBGroup.setStatus("current")

csmConfTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 18)
)
csmConfTrapGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "alaDyingGaspChassisId"),
        ("ALCATEL-IND1-PORT-MIB", "alaDyingGaspPowerSupplyType"),
        ("ALCATEL-IND1-PORT-MIB", "alaDyingGaspTime"))
)
if mibBuilder.loadTexts:
    csmConfTrapGroup.setStatus("current")


# Notification objects

esmDrvTrapDropsLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 0, 1)
)
esmDrvTrapDropsLink.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmPortSlot"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortIF"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutErrors"),
        ("ALCATEL-IND1-PORT-MIB", "esmDrvTrapDrops"))
)
if mibBuilder.loadTexts:
    esmDrvTrapDropsLink.setStatus(
        "current"
    )

ddmTemperatureThresholdViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 0, 2)
)
ddmTemperatureThresholdViolated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTemperature"))
)
if mibBuilder.loadTexts:
    ddmTemperatureThresholdViolated.setStatus(
        "current"
    )

ddmVoltageThresholdViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 0, 3)
)
ddmVoltageThresholdViolated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltage"))
)
if mibBuilder.loadTexts:
    ddmVoltageThresholdViolated.setStatus(
        "current"
    )

ddmCurrentThresholdViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 0, 4)
)
ddmCurrentThresholdViolated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrent"))
)
if mibBuilder.loadTexts:
    ddmCurrentThresholdViolated.setStatus(
        "current"
    )

ddmTxPowerThresholdViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 0, 5)
)
ddmTxPowerThresholdViolated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPower"))
)
if mibBuilder.loadTexts:
    ddmTxPowerThresholdViolated.setStatus(
        "current"
    )

ddmRxPowerThresholdViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 0, 6)
)
ddmRxPowerThresholdViolated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPower"))
)
if mibBuilder.loadTexts:
    ddmRxPowerThresholdViolated.setStatus(
        "current"
    )

portViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 0, 7)
)
portViolationTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "portViolationSource"),
        ("ALCATEL-IND1-PORT-MIB", "portViolationReason"))
)
if mibBuilder.loadTexts:
    portViolationTrap.setStatus(
        "current"
    )

portViolationNotificationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 0, 8)
)
portViolationNotificationTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portViolationNotificationTrap.setStatus(
        "current"
    )

alaDyingGaspTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 0, 9)
)
alaDyingGaspTrap.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "alaDyingGaspChassisId"),
        ("ALCATEL-IND1-PORT-MIB", "alaDyingGaspPowerSupplyType"),
        ("ALCATEL-IND1-PORT-MIB", "alaDyingGaspTime"))
)
if mibBuilder.loadTexts:
    alaDyingGaspTrap.setStatus(
        "current"
    )


# Notifications groups

alcPortNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 4)
)
alcPortNotificationGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmDrvTrapDropsLink"),
        ("ALCATEL-IND1-PORT-MIB", "portViolationTrap"),
        ("ALCATEL-IND1-PORT-MIB", "portViolationNotificationTrap"),
        ("ALCATEL-IND1-PORT-MIB", "alaDyingGaspTrap"))
)
if mibBuilder.loadTexts:
    alcPortNotificationGroup.setStatus(
        "current"
    )

ddmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 2, 8)
)
ddmNotificationsGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "ddmTemperatureThresholdViolated"),
        ("ALCATEL-IND1-PORT-MIB", "ddmVoltageThresholdViolated"),
        ("ALCATEL-IND1-PORT-MIB", "ddmCurrentThresholdViolated"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxPowerThresholdViolated"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxPowerThresholdViolated"))
)
if mibBuilder.loadTexts:
    ddmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

esmConfPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    esmConfPortCompliance.setStatus(
        "current"
    )

alcEtherStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    alcEtherStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PORT-MIB",
    **{"alcatelIND1PortMIB": alcatelIND1PortMIB,
       "alcatelIND1PortNotifications": alcatelIND1PortNotifications,
       "esmDrvTrapDropsLink": esmDrvTrapDropsLink,
       "ddmTemperatureThresholdViolated": ddmTemperatureThresholdViolated,
       "ddmVoltageThresholdViolated": ddmVoltageThresholdViolated,
       "ddmCurrentThresholdViolated": ddmCurrentThresholdViolated,
       "ddmTxPowerThresholdViolated": ddmTxPowerThresholdViolated,
       "ddmRxPowerThresholdViolated": ddmRxPowerThresholdViolated,
       "portViolationTrap": portViolationTrap,
       "portViolationNotificationTrap": portViolationNotificationTrap,
       "alaDyingGaspTrap": alaDyingGaspTrap,
       "alcatelIND1PortMIBObjects": alcatelIND1PortMIBObjects,
       "esmConfTrap": esmConfTrap,
       "esmDrvTrapDrops": esmDrvTrapDrops,
       "physicalPort": physicalPort,
       "esmConfTable": esmConfTable,
       "esmConfEntry": esmConfEntry,
       "esmPortSlot": esmPortSlot,
       "esmPortIF": esmPortIF,
       "esmPortAutoSpeed": esmPortAutoSpeed,
       "esmPortAutoDuplexMode": esmPortAutoDuplexMode,
       "esmPortCfgSpeed": esmPortCfgSpeed,
       "esmPortCfgDuplexMode": esmPortCfgDuplexMode,
       "esmPortAdminStatus": esmPortAdminStatus,
       "esmPortLinkUpDownTrapEnable": esmPortLinkUpDownTrapEnable,
       "esmPortCfgMaxFrameSize": esmPortCfgMaxFrameSize,
       "esmPortAlias": esmPortAlias,
       "esmPortCfgPause": esmPortCfgPause,
       "esmPortCfgAutoNegotiation": esmPortCfgAutoNegotiation,
       "esmPortCfgCrossover": esmPortCfgCrossover,
       "esmPortCfgHybridActiveType": esmPortCfgHybridActiveType,
       "esmPortCfgHybridMode": esmPortCfgHybridMode,
       "esmPortOperationalHybridType": esmPortOperationalHybridType,
       "esmPortBcastRateLimitEnable": esmPortBcastRateLimitEnable,
       "esmPortBcastRateLimitType": esmPortBcastRateLimitType,
       "esmPortBcastRateLimit": esmPortBcastRateLimit,
       "esmPortMcastRateLimitEnable": esmPortMcastRateLimitEnable,
       "esmPortMcastRateLimitType": esmPortMcastRateLimitType,
       "esmPortMcastRateLimit": esmPortMcastRateLimit,
       "esmPortUucastRateLimitEnable": esmPortUucastRateLimitEnable,
       "esmPortUucastRateLimitType": esmPortUucastRateLimitType,
       "esmPortUucastRateLimit": esmPortUucastRateLimit,
       "esmPortIngressRateLimitEnable": esmPortIngressRateLimitEnable,
       "esmPortIngressRateLimit": esmPortIngressRateLimit,
       "esmPortIngressRateLimitBurst": esmPortIngressRateLimitBurst,
       "esmPortEPPEnable": esmPortEPPEnable,
       "esmPortEEEEnable": esmPortEEEEnable,
       "esmPortIsFiberChannelCapable": esmPortIsFiberChannelCapable,
       "alcetherStatsTable": alcetherStatsTable,
       "alcetherStatsEntry": alcetherStatsEntry,
       "alcetherClearStats": alcetherClearStats,
       "alcetherLastClearStats": alcetherLastClearStats,
       "alcetherStatsCRCAlignErrors": alcetherStatsCRCAlignErrors,
       "alcetherStatsRxUndersizePkts": alcetherStatsRxUndersizePkts,
       "alcetherStatsTxUndersizePkts": alcetherStatsTxUndersizePkts,
       "alcetherStatsTxOversizePkts": alcetherStatsTxOversizePkts,
       "alcetherStatsRxJabbers": alcetherStatsRxJabbers,
       "alcetherStatsRxCollisions": alcetherStatsRxCollisions,
       "alcetherStatsTxCollisions": alcetherStatsTxCollisions,
       "alcetherStatsPkts64Octets": alcetherStatsPkts64Octets,
       "alcetherStatsPkts65to127Octets": alcetherStatsPkts65to127Octets,
       "alcetherStatsPkts128to255Octets": alcetherStatsPkts128to255Octets,
       "alcetherStatsPkts256to511Octets": alcetherStatsPkts256to511Octets,
       "alcetherStatsPkts512to1023Octets": alcetherStatsPkts512to1023Octets,
       "alcetherStatsPkts1024to1518Octets": alcetherStatsPkts1024to1518Octets,
       "gigaEtherStatsPkts1519to4095Octets": gigaEtherStatsPkts1519to4095Octets,
       "gigaEtherStatsPkts4096to9215Octets": gigaEtherStatsPkts4096to9215Octets,
       "alcetherStatsPkts1519to2047Octets": alcetherStatsPkts1519to2047Octets,
       "alcetherStatsPkts2048to4095Octets": alcetherStatsPkts2048to4095Octets,
       "alcetherStatsPkts4096Octets": alcetherStatsPkts4096Octets,
       "alcetherStatsRxGiantPkts": alcetherStatsRxGiantPkts,
       "alcetherStatsRxDribbleNibblePkts": alcetherStatsRxDribbleNibblePkts,
       "alcetherStatsRxLongEventPkts": alcetherStatsRxLongEventPkts,
       "alcetherStatsRxVlanTagPkts": alcetherStatsRxVlanTagPkts,
       "alcetherStatsRxControlPkts": alcetherStatsRxControlPkts,
       "alcetherStatsRxLenChkErrPkts": alcetherStatsRxLenChkErrPkts,
       "alcetherStatsRxCodeErrPkts": alcetherStatsRxCodeErrPkts,
       "alcetherStatsRxDvEventPkts": alcetherStatsRxDvEventPkts,
       "alcetherStatsRxPrevPktDropped": alcetherStatsRxPrevPktDropped,
       "alcetherStatsTx64Octets": alcetherStatsTx64Octets,
       "alcetherStatsTx65to127Octets": alcetherStatsTx65to127Octets,
       "alcetherStatsTx128to255Octets": alcetherStatsTx128to255Octets,
       "alcetherStatsTx256to511Octets": alcetherStatsTx256to511Octets,
       "alcetherStatsTx512to1023Octets": alcetherStatsTx512to1023Octets,
       "alcetherStatsTx1024to1518Octets": alcetherStatsTx1024to1518Octets,
       "alcetherStatsTx1519to2047Octets": alcetherStatsTx1519to2047Octets,
       "alcetherStatsTx2048to4095Octets": alcetherStatsTx2048to4095Octets,
       "alcetherStatsTx4096Octets": alcetherStatsTx4096Octets,
       "alcetherStatsTxRetryCount": alcetherStatsTxRetryCount,
       "alcetherStatsTxVlanTagPkts": alcetherStatsTxVlanTagPkts,
       "alcetherStatsTxControlPkts": alcetherStatsTxControlPkts,
       "alcetherStatsTxLatePkts": alcetherStatsTxLatePkts,
       "alcetherStatsTxTotalBytesOnWire": alcetherStatsTxTotalBytesOnWire,
       "alcetherStatsTxLenChkErrPkts": alcetherStatsTxLenChkErrPkts,
       "alcetherStatsTxExcDeferPkts": alcetherStatsTxExcDeferPkts,
       "esmHybridConfTable": esmHybridConfTable,
       "esmHybridConfEntry": esmHybridConfEntry,
       "esmHybridPortCfgSpeed": esmHybridPortCfgSpeed,
       "esmHybridPortCfgDuplexMode": esmHybridPortCfgDuplexMode,
       "esmHybridPortCfgAutoNegotiation": esmHybridPortCfgAutoNegotiation,
       "esmHybridPortCfgCrossover": esmHybridPortCfgCrossover,
       "esmHybridPortCfgFlow": esmHybridPortCfgFlow,
       "esmHybridPortCfgInactiveType": esmHybridPortCfgInactiveType,
       "ddmInfoTable": ddmInfoTable,
       "ddmInfoEntry": ddmInfoEntry,
       "ddmTemperature": ddmTemperature,
       "ddmTempLowWarning": ddmTempLowWarning,
       "ddmTempLowAlarm": ddmTempLowAlarm,
       "ddmTempHiWarning": ddmTempHiWarning,
       "ddmTempHiAlarm": ddmTempHiAlarm,
       "ddmSupplyVoltage": ddmSupplyVoltage,
       "ddmSupplyVoltageLowWarning": ddmSupplyVoltageLowWarning,
       "ddmSupplyVoltageLowAlarm": ddmSupplyVoltageLowAlarm,
       "ddmSupplyVoltageHiWarning": ddmSupplyVoltageHiWarning,
       "ddmSupplyVoltageHiAlarm": ddmSupplyVoltageHiAlarm,
       "ddmTxBiasCurrent": ddmTxBiasCurrent,
       "ddmTxBiasCurrentLowWarning": ddmTxBiasCurrentLowWarning,
       "ddmTxBiasCurrentLowAlarm": ddmTxBiasCurrentLowAlarm,
       "ddmTxBiasCurrentHiWarning": ddmTxBiasCurrentHiWarning,
       "ddmTxBiasCurrentHiAlarm": ddmTxBiasCurrentHiAlarm,
       "ddmTxOutputPower": ddmTxOutputPower,
       "ddmTxOutputPowerLowWarning": ddmTxOutputPowerLowWarning,
       "ddmTxOutputPowerLowAlarm": ddmTxOutputPowerLowAlarm,
       "ddmTxOutputPowerHiWarning": ddmTxOutputPowerHiWarning,
       "ddmTxOutputPowerHiAlarm": ddmTxOutputPowerHiAlarm,
       "ddmRxOpticalPower": ddmRxOpticalPower,
       "ddmRxOpticalPowerLowWarning": ddmRxOpticalPowerLowWarning,
       "ddmRxOpticalPowerLowAlarm": ddmRxOpticalPowerLowAlarm,
       "ddmRxOpticalPowerHiWarning": ddmRxOpticalPowerHiWarning,
       "ddmRxOpticalPowerHiAlarm": ddmRxOpticalPowerHiAlarm,
       "ddmPortInfoTable": ddmPortInfoTable,
       "ddmPortInfoEntry": ddmPortInfoEntry,
       "ddmPortChannel": ddmPortChannel,
       "ddmPortTemperature": ddmPortTemperature,
       "ddmPortTempLowWarning": ddmPortTempLowWarning,
       "ddmPortTempLowAlarm": ddmPortTempLowAlarm,
       "ddmPortTempHiWarning": ddmPortTempHiWarning,
       "ddmPortTempHiAlarm": ddmPortTempHiAlarm,
       "ddmPortSupplyVoltage": ddmPortSupplyVoltage,
       "ddmPortSupplyVoltageLowWarning": ddmPortSupplyVoltageLowWarning,
       "ddmPortSupplyVoltageLowAlarm": ddmPortSupplyVoltageLowAlarm,
       "ddmPortSupplyVoltageHiWarning": ddmPortSupplyVoltageHiWarning,
       "ddmPortSupplyVoltageHiAlarm": ddmPortSupplyVoltageHiAlarm,
       "ddmPortTxBiasCurrent": ddmPortTxBiasCurrent,
       "ddmPortTxBiasCurrentLowWarning": ddmPortTxBiasCurrentLowWarning,
       "ddmPortTxBiasCurrentLowAlarm": ddmPortTxBiasCurrentLowAlarm,
       "ddmPortTxBiasCurrentHiWarning": ddmPortTxBiasCurrentHiWarning,
       "ddmPortTxBiasCurrentHiAlarm": ddmPortTxBiasCurrentHiAlarm,
       "ddmPortTxOutputPower": ddmPortTxOutputPower,
       "ddmPortTxOutputPowerLowWarning": ddmPortTxOutputPowerLowWarning,
       "ddmPortTxOutputPowerLowAlarm": ddmPortTxOutputPowerLowAlarm,
       "ddmPortTxOutputPowerHiWarning": ddmPortTxOutputPowerHiWarning,
       "ddmPortTxOutputPowerHiAlarm": ddmPortTxOutputPowerHiAlarm,
       "ddmPortRxOpticalPower": ddmPortRxOpticalPower,
       "ddmPortRxOpticalPowerLowWarning": ddmPortRxOpticalPowerLowWarning,
       "ddmPortRxOpticalPowerLowAlarm": ddmPortRxOpticalPowerLowAlarm,
       "ddmPortRxOpticalPowerHiWarning": ddmPortRxOpticalPowerHiWarning,
       "ddmPortRxOpticalPowerHiAlarm": ddmPortRxOpticalPowerHiAlarm,
       "alcfcStatsTable": alcfcStatsTable,
       "alcfcStatsEntry": alcfcStatsEntry,
       "alcfcClearStats": alcfcClearStats,
       "alcfcLastClearStats": alcfcLastClearStats,
       "alcfcStatsRxUndersizePkts": alcfcStatsRxUndersizePkts,
       "alcfcStatsTxBBCreditZeros": alcfcStatsTxBBCreditZeros,
       "alcfcStatsRxBBCreditZeros": alcfcStatsRxBBCreditZeros,
       "alcfcStatsLinkFailures": alcfcStatsLinkFailures,
       "alcfcStatsLossofSynchs": alcfcStatsLossofSynchs,
       "alcfcStatsLossofSignals": alcfcStatsLossofSignals,
       "alcfcStatsPrimSeqProtocolErrors": alcfcStatsPrimSeqProtocolErrors,
       "alcfcStatsInvalidTxWords": alcfcStatsInvalidTxWords,
       "alcfcStatsInvalidCRCs": alcfcStatsInvalidCRCs,
       "alcfcStatsInvalidOrderedSets": alcfcStatsInvalidOrderedSets,
       "alcfcStatsFrameTooLongs": alcfcStatsFrameTooLongs,
       "alcfcStatsDelimiterErrors": alcfcStatsDelimiterErrors,
       "alcfcStatsEncodingDisparityErrors": alcfcStatsEncodingDisparityErrors,
       "alcfcStatsOtherErrors": alcfcStatsOtherErrors,
       "ddmConfiguration": ddmConfiguration,
       "ddmConfig": ddmConfig,
       "ddmTrapConfig": ddmTrapConfig,
       "ddmNotificationType": ddmNotificationType,
       "portViolations": portViolations,
       "portViolationTable": portViolationTable,
       "portViolationEntry": portViolationEntry,
       "portViolationIfIndex": portViolationIfIndex,
       "portViolationSource": portViolationSource,
       "portViolationReason": portViolationReason,
       "portViolationAction": portViolationAction,
       "portViolationTimer": portViolationTimer,
       "portViolationTimerAction": portViolationTimerAction,
       "portViolationClearPort": portViolationClearPort,
       "alaLinkMonConfigTable": alaLinkMonConfigTable,
       "alaLinkMonConfigEntry": alaLinkMonConfigEntry,
       "alaLinkMonStatus": alaLinkMonStatus,
       "alaLinkMonTimeWindow": alaLinkMonTimeWindow,
       "alaLinkMonLinkFlapThreshold": alaLinkMonLinkFlapThreshold,
       "alaLinkMonLinkErrorThreshold": alaLinkMonLinkErrorThreshold,
       "alaLinkMonWaitToRestoreTimer": alaLinkMonWaitToRestoreTimer,
       "alaLinkMonWaitToShutdownTimer": alaLinkMonWaitToShutdownTimer,
       "alaLinkMonStatsTable": alaLinkMonStatsTable,
       "alaLinkMonStatsEntry": alaLinkMonStatsEntry,
       "alaLinkMonStatsClearStats": alaLinkMonStatsClearStats,
       "alaLinkMonStatsPortState": alaLinkMonStatsPortState,
       "alaLinkMonStatsCurrentLinkFlaps": alaLinkMonStatsCurrentLinkFlaps,
       "alaLinkMonStatsCurrentErrorFrames": alaLinkMonStatsCurrentErrorFrames,
       "alaLinkMonStatsCurrentCRCErrors": alaLinkMonStatsCurrentCRCErrors,
       "alaLinkMonStatsCurrentLostFrames": alaLinkMonStatsCurrentLostFrames,
       "alaLinkMonStatsCurrentAlignErrors": alaLinkMonStatsCurrentAlignErrors,
       "alaLinkMonStatsCurrentLinkErrors": alaLinkMonStatsCurrentLinkErrors,
       "alaLinkMonStatsTotalLinkFlaps": alaLinkMonStatsTotalLinkFlaps,
       "alaLinkMonStatsTotalLinkErrors": alaLinkMonStatsTotalLinkErrors,
       "alaLFPGroupTable": alaLFPGroupTable,
       "alaLFPGroupEntry": alaLFPGroupEntry,
       "alaLFPGroupId": alaLFPGroupId,
       "alaLFPGroupAdminStatus": alaLFPGroupAdminStatus,
       "alaLFPGroupOperStatus": alaLFPGroupOperStatus,
       "alaLFPGroupWaitToShutdown": alaLFPGroupWaitToShutdown,
       "alaLFPGroupRowStatus": alaLFPGroupRowStatus,
       "alaLFPConfigTable": alaLFPConfigTable,
       "alaLFPConfigEntry": alaLFPConfigEntry,
       "alaLFPConfigPort": alaLFPConfigPort,
       "alaLFPConfigPortType": alaLFPConfigPortType,
       "alaLFPConfigRowStatus": alaLFPConfigRowStatus,
       "csmConfTrap": csmConfTrap,
       "alaDyingGaspChassisId": alaDyingGaspChassisId,
       "alaDyingGaspPowerSupplyType": alaDyingGaspPowerSupplyType,
       "alaDyingGaspTime": alaDyingGaspTime,
       "alcatelIND1PortMIBConformance": alcatelIND1PortMIBConformance,
       "alcatelIND1PortMIBCompliances": alcatelIND1PortMIBCompliances,
       "esmConfPortCompliance": esmConfPortCompliance,
       "alcEtherStatsCompliance": alcEtherStatsCompliance,
       "alcatelIND1PortMIBGroups": alcatelIND1PortMIBGroups,
       "esmConfMIBGroup": esmConfMIBGroup,
       "esmDetectedConfMIBGroup": esmDetectedConfMIBGroup,
       "alcEtherStatsMIBGroup": alcEtherStatsMIBGroup,
       "alcPortNotificationGroup": alcPortNotificationGroup,
       "ddmInfoGroup": ddmInfoGroup,
       "ddmConfigGroup": ddmConfigGroup,
       "ddmNotificationsGroup": ddmNotificationsGroup,
       "esmConfTrapGroup": esmConfTrapGroup,
       "esmHybridConfEntryGroup": esmHybridConfEntryGroup,
       "esmConfEntryGroup": esmConfEntryGroup,
       "portViolationEntryGroup": portViolationEntryGroup,
       "ddmPortInfoGroup": ddmPortInfoGroup,
       "alaLinkMonConfigMIBGroup": alaLinkMonConfigMIBGroup,
       "alaLinkMonStatsMIBGroup": alaLinkMonStatsMIBGroup,
       "alaLFPGroupMIBGroup": alaLFPGroupMIBGroup,
       "alaLFPConfigMIBGroup": alaLFPConfigMIBGroup,
       "csmConfTrapGroup": csmConfTrapGroup}
)
