# SNMP MIB module (RADLAN-STORMCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-STORMCTRL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:33 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rlStormCtrl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 77)
)
rlStormCtrl.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions



class RlStormCtrlRateUnit(Integer32):
    """Custom type RlStormCtrlRateUnit based on Integer32"""
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
        *(("bytesPerSecond", 2),
          ("framesPerBuffer", 3),
          ("kiloBitsPerSecond", 6),
          ("kiloBytesPerSecond", 5),
          ("packetsPerSecond", 1),
          ("precentages", 4))
    )





class RlStormCtrlRateUnitType(Integer32):
    """Custom type RlStormCtrlRateUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kiloBitsPerSecond", 1),
          ("precentages", 2))
    )





class RlStormCtrlActionType(Integer32):
    """Custom type RlStormCtrlActionType based on Integer32"""
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
        *(("none", 1),
          ("shutdown", 3),
          ("trap", 2),
          ("trapAndShutdown", 4))
    )




# TEXTUAL-CONVENTIONS



class RlStormCtrlRateLimTrafficType(Integer32, TextualConvention):
    status = "current"
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
        *(("all", 6),
          ("broadcast", 1),
          ("multicastAll", 4),
          ("multicastRegistred", 2),
          ("multicastUnregistred", 3),
          ("unknownUnicast", 5))
    )



# MIB Managed Objects in the order of their OIDs

_RlStormCtrlSupport_Type = TruthValue
_RlStormCtrlSupport_Object = MibScalar
rlStormCtrlSupport = _RlStormCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 1),
    _RlStormCtrlSupport_Type()
)
rlStormCtrlSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlSupport.setStatus("obsolete")
_RlStormCtrlMibVersion_Type = Integer32
_RlStormCtrlMibVersion_Object = MibScalar
rlStormCtrlMibVersion = _RlStormCtrlMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 2),
    _RlStormCtrlMibVersion_Type()
)
rlStormCtrlMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlMibVersion.setStatus("obsolete")


class _RlStormCtrlRateUnitTypeSupport_Type(OctetString):
    """Custom type rlStormCtrlRateUnitTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlStormCtrlRateUnitTypeSupport_Type.__name__ = "OctetString"
_RlStormCtrlRateUnitTypeSupport_Object = MibScalar
rlStormCtrlRateUnitTypeSupport = _RlStormCtrlRateUnitTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 3),
    _RlStormCtrlRateUnitTypeSupport_Type()
)
rlStormCtrlRateUnitTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateUnitTypeSupport.setStatus("obsolete")


class _RlStormCtrlTypeSupport_Type(OctetString):
    """Custom type rlStormCtrlTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlStormCtrlTypeSupport_Type.__name__ = "OctetString"
_RlStormCtrlTypeSupport_Object = MibScalar
rlStormCtrlTypeSupport = _RlStormCtrlTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 4),
    _RlStormCtrlTypeSupport_Type()
)
rlStormCtrlTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlTypeSupport.setStatus("obsolete")


class _RlStormCtrlRateSupportPerType_Type(OctetString):
    """Custom type rlStormCtrlRateSupportPerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlStormCtrlRateSupportPerType_Type.__name__ = "OctetString"
_RlStormCtrlRateSupportPerType_Object = MibScalar
rlStormCtrlRateSupportPerType = _RlStormCtrlRateSupportPerType_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 5),
    _RlStormCtrlRateSupportPerType_Type()
)
rlStormCtrlRateSupportPerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateSupportPerType.setStatus("obsolete")


class _RlStormCtrlEnbaleDependencyBetweenTypes_Type(OctetString):
    """Custom type rlStormCtrlEnbaleDependencyBetweenTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlStormCtrlEnbaleDependencyBetweenTypes_Type.__name__ = "OctetString"
_RlStormCtrlEnbaleDependencyBetweenTypes_Object = MibScalar
rlStormCtrlEnbaleDependencyBetweenTypes = _RlStormCtrlEnbaleDependencyBetweenTypes_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 6),
    _RlStormCtrlEnbaleDependencyBetweenTypes_Type()
)
rlStormCtrlEnbaleDependencyBetweenTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlEnbaleDependencyBetweenTypes.setStatus("obsolete")


class _RlStormCtrlRateDependencyBetweenTypes_Type(OctetString):
    """Custom type rlStormCtrlRateDependencyBetweenTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlStormCtrlRateDependencyBetweenTypes_Type.__name__ = "OctetString"
_RlStormCtrlRateDependencyBetweenTypes_Object = MibScalar
rlStormCtrlRateDependencyBetweenTypes = _RlStormCtrlRateDependencyBetweenTypes_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 7),
    _RlStormCtrlRateDependencyBetweenTypes_Type()
)
rlStormCtrlRateDependencyBetweenTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateDependencyBetweenTypes.setStatus("obsolete")
_RlStormCtrlTable_Object = MibTable
rlStormCtrlTable = _RlStormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8)
)
if mibBuilder.loadTexts:
    rlStormCtrlTable.setStatus("obsolete")
_RlStormCtrlEntry_Object = MibTableRow
rlStormCtrlEntry = _RlStormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1)
)
rlStormCtrlEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlStormCtrlEntry.setStatus("obsolete")
_RlStormCtrlRateType_Type = RlStormCtrlRateUnit
_RlStormCtrlRateType_Object = MibTableColumn
rlStormCtrlRateType = _RlStormCtrlRateType_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 1),
    _RlStormCtrlRateType_Type()
)
rlStormCtrlRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlRateType.setStatus("obsolete")


class _RlStormCtrlUnknownUnicastEnable_Type(TruthValue):
    """Custom type rlStormCtrlUnknownUnicastEnable based on TruthValue"""


_RlStormCtrlUnknownUnicastEnable_Object = MibTableColumn
rlStormCtrlUnknownUnicastEnable = _RlStormCtrlUnknownUnicastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 2),
    _RlStormCtrlUnknownUnicastEnable_Type()
)
rlStormCtrlUnknownUnicastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownUnicastEnable.setStatus("obsolete")


class _RlStormCtrlUnknownUnicastRate_Type(Unsigned32):
    """Custom type rlStormCtrlUnknownUnicastRate based on Unsigned32"""
    defaultValue = 0


_RlStormCtrlUnknownUnicastRate_Object = MibTableColumn
rlStormCtrlUnknownUnicastRate = _RlStormCtrlUnknownUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 3),
    _RlStormCtrlUnknownUnicastRate_Type()
)
rlStormCtrlUnknownUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownUnicastRate.setStatus("obsolete")


class _RlStormCtrlUnknownMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlUnknownMulticastEnable based on TruthValue"""


_RlStormCtrlUnknownMulticastEnable_Object = MibTableColumn
rlStormCtrlUnknownMulticastEnable = _RlStormCtrlUnknownMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 4),
    _RlStormCtrlUnknownMulticastEnable_Type()
)
rlStormCtrlUnknownMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownMulticastEnable.setStatus("obsolete")


class _RlStormCtrlUnknownMulticastRate_Type(Unsigned32):
    """Custom type rlStormCtrlUnknownMulticastRate based on Unsigned32"""
    defaultValue = 0


_RlStormCtrlUnknownMulticastRate_Object = MibTableColumn
rlStormCtrlUnknownMulticastRate = _RlStormCtrlUnknownMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 5),
    _RlStormCtrlUnknownMulticastRate_Type()
)
rlStormCtrlUnknownMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownMulticastRate.setStatus("obsolete")


class _RlStormCtrlBroadcastEnable_Type(TruthValue):
    """Custom type rlStormCtrlBroadcastEnable based on TruthValue"""


_RlStormCtrlBroadcastEnable_Object = MibTableColumn
rlStormCtrlBroadcastEnable = _RlStormCtrlBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 6),
    _RlStormCtrlBroadcastEnable_Type()
)
rlStormCtrlBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlBroadcastEnable.setStatus("obsolete")


class _RlStormCtrlBroadcastRate_Type(Unsigned32):
    """Custom type rlStormCtrlBroadcastRate based on Unsigned32"""
    defaultValue = 0


_RlStormCtrlBroadcastRate_Object = MibTableColumn
rlStormCtrlBroadcastRate = _RlStormCtrlBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 7),
    _RlStormCtrlBroadcastRate_Type()
)
rlStormCtrlBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlBroadcastRate.setStatus("obsolete")


class _RlStormCtrlMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlMulticastEnable based on TruthValue"""


_RlStormCtrlMulticastEnable_Object = MibTableColumn
rlStormCtrlMulticastEnable = _RlStormCtrlMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 8),
    _RlStormCtrlMulticastEnable_Type()
)
rlStormCtrlMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlMulticastEnable.setStatus("obsolete")


class _RlStormCtrlMulticastRate_Type(Unsigned32):
    """Custom type rlStormCtrlMulticastRate based on Unsigned32"""
    defaultValue = 0


_RlStormCtrlMulticastRate_Object = MibTableColumn
rlStormCtrlMulticastRate = _RlStormCtrlMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 9),
    _RlStormCtrlMulticastRate_Type()
)
rlStormCtrlMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlMulticastRate.setStatus("obsolete")


class _RlStormCtrlSetDefaultRateType_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultRateType based on TruthValue"""


_RlStormCtrlSetDefaultRateType_Object = MibTableColumn
rlStormCtrlSetDefaultRateType = _RlStormCtrlSetDefaultRateType_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 10),
    _RlStormCtrlSetDefaultRateType_Type()
)
rlStormCtrlSetDefaultRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultRateType.setStatus("obsolete")


class _RlStormCtrlSetDefaultUnknownUnicastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownUnicastEnable based on TruthValue"""


_RlStormCtrlSetDefaultUnknownUnicastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownUnicastEnable = _RlStormCtrlSetDefaultUnknownUnicastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 11),
    _RlStormCtrlSetDefaultUnknownUnicastEnable_Type()
)
rlStormCtrlSetDefaultUnknownUnicastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownUnicastEnable.setStatus("obsolete")


class _RlStormCtrlSetDefaultUnknownUnicastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownUnicastRate based on TruthValue"""


_RlStormCtrlSetDefaultUnknownUnicastRate_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownUnicastRate = _RlStormCtrlSetDefaultUnknownUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 12),
    _RlStormCtrlSetDefaultUnknownUnicastRate_Type()
)
rlStormCtrlSetDefaultUnknownUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownUnicastRate.setStatus("obsolete")


class _RlStormCtrlSetDefaultUnknownMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownMulticastEnable based on TruthValue"""


_RlStormCtrlSetDefaultUnknownMulticastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownMulticastEnable = _RlStormCtrlSetDefaultUnknownMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 13),
    _RlStormCtrlSetDefaultUnknownMulticastEnable_Type()
)
rlStormCtrlSetDefaultUnknownMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownMulticastEnable.setStatus("obsolete")


class _RlStormCtrlSetDefaultUnknownMulticastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownMulticastRate based on TruthValue"""


_RlStormCtrlSetDefaultUnknownMulticastRate_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownMulticastRate = _RlStormCtrlSetDefaultUnknownMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 14),
    _RlStormCtrlSetDefaultUnknownMulticastRate_Type()
)
rlStormCtrlSetDefaultUnknownMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownMulticastRate.setStatus("obsolete")


class _RlStormCtrlSetDefaultBroadcastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultBroadcastEnable based on TruthValue"""


_RlStormCtrlSetDefaultBroadcastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultBroadcastEnable = _RlStormCtrlSetDefaultBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 15),
    _RlStormCtrlSetDefaultBroadcastEnable_Type()
)
rlStormCtrlSetDefaultBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultBroadcastEnable.setStatus("obsolete")


class _RlStormCtrlSetDefaultBroadcastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultBroadcastRate based on TruthValue"""


_RlStormCtrlSetDefaultBroadcastRate_Object = MibTableColumn
rlStormCtrlSetDefaultBroadcastRate = _RlStormCtrlSetDefaultBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 16),
    _RlStormCtrlSetDefaultBroadcastRate_Type()
)
rlStormCtrlSetDefaultBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultBroadcastRate.setStatus("obsolete")


class _RlStormCtrlSetDefaultMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultMulticastEnable based on TruthValue"""


_RlStormCtrlSetDefaultMulticastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultMulticastEnable = _RlStormCtrlSetDefaultMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 17),
    _RlStormCtrlSetDefaultMulticastEnable_Type()
)
rlStormCtrlSetDefaultMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultMulticastEnable.setStatus("obsolete")


class _RlStormCtrlSetDefaultMulticastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultMulticastRate based on TruthValue"""


_RlStormCtrlSetDefaultMulticastRate_Object = MibTableColumn
rlStormCtrlSetDefaultMulticastRate = _RlStormCtrlSetDefaultMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 18),
    _RlStormCtrlSetDefaultMulticastRate_Type()
)
rlStormCtrlSetDefaultMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultMulticastRate.setStatus("obsolete")
_RlStormCtrlBroadcastOperRate_Type = Unsigned32
_RlStormCtrlBroadcastOperRate_Object = MibTableColumn
rlStormCtrlBroadcastOperRate = _RlStormCtrlBroadcastOperRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 19),
    _RlStormCtrlBroadcastOperRate_Type()
)
rlStormCtrlBroadcastOperRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlBroadcastOperRate.setStatus("obsolete")
_RlStormCtrlGroupTable_Object = MibTable
rlStormCtrlGroupTable = _RlStormCtrlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9)
)
if mibBuilder.loadTexts:
    rlStormCtrlGroupTable.setStatus("obsolete")
_RlStormCtrlGroupEntry_Object = MibTableRow
rlStormCtrlGroupEntry = _RlStormCtrlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9, 1)
)
rlStormCtrlGroupEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlStormCtrlGroupEntry.setStatus("obsolete")
_RlStormCtrlGroupUnknownUnicastId_Type = Integer32
_RlStormCtrlGroupUnknownUnicastId_Object = MibTableColumn
rlStormCtrlGroupUnknownUnicastId = _RlStormCtrlGroupUnknownUnicastId_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9, 1, 1),
    _RlStormCtrlGroupUnknownUnicastId_Type()
)
rlStormCtrlGroupUnknownUnicastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupUnknownUnicastId.setStatus("obsolete")
_RlStormCtrlGroupUnknownMulticastId_Type = Integer32
_RlStormCtrlGroupUnknownMulticastId_Object = MibTableColumn
rlStormCtrlGroupUnknownMulticastId = _RlStormCtrlGroupUnknownMulticastId_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9, 1, 2),
    _RlStormCtrlGroupUnknownMulticastId_Type()
)
rlStormCtrlGroupUnknownMulticastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupUnknownMulticastId.setStatus("obsolete")
_RlStormCtrlGroupBroadcastId_Type = Integer32
_RlStormCtrlGroupBroadcastId_Object = MibTableColumn
rlStormCtrlGroupBroadcastId = _RlStormCtrlGroupBroadcastId_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9, 1, 3),
    _RlStormCtrlGroupBroadcastId_Type()
)
rlStormCtrlGroupBroadcastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupBroadcastId.setStatus("obsolete")
_RlStormCtrlGroupMulticastId_Type = Integer32
_RlStormCtrlGroupMulticastId_Object = MibTableColumn
rlStormCtrlGroupMulticastId = _RlStormCtrlGroupMulticastId_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9, 1, 4),
    _RlStormCtrlGroupMulticastId_Type()
)
rlStormCtrlGroupMulticastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupMulticastId.setStatus("obsolete")
_RlStormCtrlRateLimSupport_Type = TruthValue
_RlStormCtrlRateLimSupport_Object = MibScalar
rlStormCtrlRateLimSupport = _RlStormCtrlRateLimSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 10),
    _RlStormCtrlRateLimSupport_Type()
)
rlStormCtrlRateLimSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateLimSupport.setStatus("current")
_RlStormCtrlRateLimMibVersion_Type = Integer32
_RlStormCtrlRateLimMibVersion_Object = MibScalar
rlStormCtrlRateLimMibVersion = _RlStormCtrlRateLimMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 11),
    _RlStormCtrlRateLimMibVersion_Type()
)
rlStormCtrlRateLimMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateLimMibVersion.setStatus("current")
_RlStormCtrlRateLimCfgTable_Object = MibTable
rlStormCtrlRateLimCfgTable = _RlStormCtrlRateLimCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 12)
)
if mibBuilder.loadTexts:
    rlStormCtrlRateLimCfgTable.setStatus("current")
_RlStormCtrlRateLimCfgEntry_Object = MibTableRow
rlStormCtrlRateLimCfgEntry = _RlStormCtrlRateLimCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 12, 1)
)
rlStormCtrlRateLimCfgEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "RADLAN-STORMCTRL-MIB", "rlStormCtrlRateLimCfgTraffic"),
)
if mibBuilder.loadTexts:
    rlStormCtrlRateLimCfgEntry.setStatus("current")
_RlStormCtrlRateLimCfgTraffic_Type = RlStormCtrlRateLimTrafficType
_RlStormCtrlRateLimCfgTraffic_Object = MibTableColumn
rlStormCtrlRateLimCfgTraffic = _RlStormCtrlRateLimCfgTraffic_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 12, 1, 1),
    _RlStormCtrlRateLimCfgTraffic_Type()
)
rlStormCtrlRateLimCfgTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlRateLimCfgTraffic.setStatus("current")
_RlStormCtrlRateLimCfgRate_Type = Unsigned32
_RlStormCtrlRateLimCfgRate_Object = MibTableColumn
rlStormCtrlRateLimCfgRate = _RlStormCtrlRateLimCfgRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 12, 1, 2),
    _RlStormCtrlRateLimCfgRate_Type()
)
rlStormCtrlRateLimCfgRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlRateLimCfgRate.setStatus("current")
_RlStormCtrlRateLimCfgUnit_Type = RlStormCtrlRateUnitType
_RlStormCtrlRateLimCfgUnit_Object = MibTableColumn
rlStormCtrlRateLimCfgUnit = _RlStormCtrlRateLimCfgUnit_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 12, 1, 3),
    _RlStormCtrlRateLimCfgUnit_Type()
)
rlStormCtrlRateLimCfgUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlRateLimCfgUnit.setStatus("current")
_RlStormCtrlRateLimCfgAction_Type = RlStormCtrlActionType
_RlStormCtrlRateLimCfgAction_Object = MibTableColumn
rlStormCtrlRateLimCfgAction = _RlStormCtrlRateLimCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 12, 1, 4),
    _RlStormCtrlRateLimCfgAction_Type()
)
rlStormCtrlRateLimCfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlRateLimCfgAction.setStatus("current")
_RlStormCtrlRateLimCfgBurst_Type = Unsigned32
_RlStormCtrlRateLimCfgBurst_Object = MibTableColumn
rlStormCtrlRateLimCfgBurst = _RlStormCtrlRateLimCfgBurst_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 12, 1, 5),
    _RlStormCtrlRateLimCfgBurst_Type()
)
rlStormCtrlRateLimCfgBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlRateLimCfgBurst.setStatus("current")
_RlStormCtrlRateLimOperTable_Object = MibTable
rlStormCtrlRateLimOperTable = _RlStormCtrlRateLimOperTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 13)
)
if mibBuilder.loadTexts:
    rlStormCtrlRateLimOperTable.setStatus("current")
_RlStormCtrlRateLimOperEntry_Object = MibTableRow
rlStormCtrlRateLimOperEntry = _RlStormCtrlRateLimOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 13, 1)
)
rlStormCtrlRateLimOperEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "RADLAN-STORMCTRL-MIB", "rlStormCtrlRateLimCfgTraffic"),
)
if mibBuilder.loadTexts:
    rlStormCtrlRateLimOperEntry.setStatus("current")
_RlStormCtrlRateLimOperPassCnt_Type = Counter64
_RlStormCtrlRateLimOperPassCnt_Object = MibTableColumn
rlStormCtrlRateLimOperPassCnt = _RlStormCtrlRateLimOperPassCnt_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 13, 1, 1),
    _RlStormCtrlRateLimOperPassCnt_Type()
)
rlStormCtrlRateLimOperPassCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateLimOperPassCnt.setStatus("current")
_RlStormCtrlRateLimOperDropCnt_Type = Counter64
_RlStormCtrlRateLimOperDropCnt_Object = MibTableColumn
rlStormCtrlRateLimOperDropCnt = _RlStormCtrlRateLimOperDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 13, 1, 2),
    _RlStormCtrlRateLimOperDropCnt_Type()
)
rlStormCtrlRateLimOperDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateLimOperDropCnt.setStatus("current")
_RlStormCtrlRateLimOperLastDropTime_Type = DisplayString
_RlStormCtrlRateLimOperLastDropTime_Object = MibTableColumn
rlStormCtrlRateLimOperLastDropTime = _RlStormCtrlRateLimOperLastDropTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 13, 1, 3),
    _RlStormCtrlRateLimOperLastDropTime_Type()
)
rlStormCtrlRateLimOperLastDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateLimOperLastDropTime.setStatus("current")
_RlStormCtrlClearCountersTable_Object = MibTable
rlStormCtrlClearCountersTable = _RlStormCtrlClearCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 14)
)
if mibBuilder.loadTexts:
    rlStormCtrlClearCountersTable.setStatus("current")
_RlStormCtrlClearCountersEntry_Object = MibTableRow
rlStormCtrlClearCountersEntry = _RlStormCtrlClearCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 14, 1)
)
rlStormCtrlClearCountersEntry.setIndexNames(
    (0, "RADLAN-STORMCTRL-MIB", "rlStormCtrlClearCountersIndex"),
)
if mibBuilder.loadTexts:
    rlStormCtrlClearCountersEntry.setStatus("current")
_RlStormCtrlClearCountersIndex_Type = Unsigned32
_RlStormCtrlClearCountersIndex_Object = MibTableColumn
rlStormCtrlClearCountersIndex = _RlStormCtrlClearCountersIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 14, 1, 1),
    _RlStormCtrlClearCountersIndex_Type()
)
rlStormCtrlClearCountersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlClearCountersIndex.setStatus("current")
_RlStormCtrlClearCountersTraffic_Type = RlStormCtrlRateLimTrafficType
_RlStormCtrlClearCountersTraffic_Object = MibTableColumn
rlStormCtrlClearCountersTraffic = _RlStormCtrlClearCountersTraffic_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 14, 1, 2),
    _RlStormCtrlClearCountersTraffic_Type()
)
rlStormCtrlClearCountersTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlClearCountersTraffic.setStatus("current")
_RlStormCtrlClearCountersInterface_Type = InterfaceIndex
_RlStormCtrlClearCountersInterface_Object = MibTableColumn
rlStormCtrlClearCountersInterface = _RlStormCtrlClearCountersInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 14, 1, 3),
    _RlStormCtrlClearCountersInterface_Type()
)
rlStormCtrlClearCountersInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlClearCountersInterface.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-STORMCTRL-MIB",
    **{"RlStormCtrlRateUnit": RlStormCtrlRateUnit,
       "RlStormCtrlRateLimTrafficType": RlStormCtrlRateLimTrafficType,
       "RlStormCtrlRateUnitType": RlStormCtrlRateUnitType,
       "RlStormCtrlActionType": RlStormCtrlActionType,
       "rlStormCtrl": rlStormCtrl,
       "rlStormCtrlSupport": rlStormCtrlSupport,
       "rlStormCtrlMibVersion": rlStormCtrlMibVersion,
       "rlStormCtrlRateUnitTypeSupport": rlStormCtrlRateUnitTypeSupport,
       "rlStormCtrlTypeSupport": rlStormCtrlTypeSupport,
       "rlStormCtrlRateSupportPerType": rlStormCtrlRateSupportPerType,
       "rlStormCtrlEnbaleDependencyBetweenTypes": rlStormCtrlEnbaleDependencyBetweenTypes,
       "rlStormCtrlRateDependencyBetweenTypes": rlStormCtrlRateDependencyBetweenTypes,
       "rlStormCtrlTable": rlStormCtrlTable,
       "rlStormCtrlEntry": rlStormCtrlEntry,
       "rlStormCtrlRateType": rlStormCtrlRateType,
       "rlStormCtrlUnknownUnicastEnable": rlStormCtrlUnknownUnicastEnable,
       "rlStormCtrlUnknownUnicastRate": rlStormCtrlUnknownUnicastRate,
       "rlStormCtrlUnknownMulticastEnable": rlStormCtrlUnknownMulticastEnable,
       "rlStormCtrlUnknownMulticastRate": rlStormCtrlUnknownMulticastRate,
       "rlStormCtrlBroadcastEnable": rlStormCtrlBroadcastEnable,
       "rlStormCtrlBroadcastRate": rlStormCtrlBroadcastRate,
       "rlStormCtrlMulticastEnable": rlStormCtrlMulticastEnable,
       "rlStormCtrlMulticastRate": rlStormCtrlMulticastRate,
       "rlStormCtrlSetDefaultRateType": rlStormCtrlSetDefaultRateType,
       "rlStormCtrlSetDefaultUnknownUnicastEnable": rlStormCtrlSetDefaultUnknownUnicastEnable,
       "rlStormCtrlSetDefaultUnknownUnicastRate": rlStormCtrlSetDefaultUnknownUnicastRate,
       "rlStormCtrlSetDefaultUnknownMulticastEnable": rlStormCtrlSetDefaultUnknownMulticastEnable,
       "rlStormCtrlSetDefaultUnknownMulticastRate": rlStormCtrlSetDefaultUnknownMulticastRate,
       "rlStormCtrlSetDefaultBroadcastEnable": rlStormCtrlSetDefaultBroadcastEnable,
       "rlStormCtrlSetDefaultBroadcastRate": rlStormCtrlSetDefaultBroadcastRate,
       "rlStormCtrlSetDefaultMulticastEnable": rlStormCtrlSetDefaultMulticastEnable,
       "rlStormCtrlSetDefaultMulticastRate": rlStormCtrlSetDefaultMulticastRate,
       "rlStormCtrlBroadcastOperRate": rlStormCtrlBroadcastOperRate,
       "rlStormCtrlGroupTable": rlStormCtrlGroupTable,
       "rlStormCtrlGroupEntry": rlStormCtrlGroupEntry,
       "rlStormCtrlGroupUnknownUnicastId": rlStormCtrlGroupUnknownUnicastId,
       "rlStormCtrlGroupUnknownMulticastId": rlStormCtrlGroupUnknownMulticastId,
       "rlStormCtrlGroupBroadcastId": rlStormCtrlGroupBroadcastId,
       "rlStormCtrlGroupMulticastId": rlStormCtrlGroupMulticastId,
       "rlStormCtrlRateLimSupport": rlStormCtrlRateLimSupport,
       "rlStormCtrlRateLimMibVersion": rlStormCtrlRateLimMibVersion,
       "rlStormCtrlRateLimCfgTable": rlStormCtrlRateLimCfgTable,
       "rlStormCtrlRateLimCfgEntry": rlStormCtrlRateLimCfgEntry,
       "rlStormCtrlRateLimCfgTraffic": rlStormCtrlRateLimCfgTraffic,
       "rlStormCtrlRateLimCfgRate": rlStormCtrlRateLimCfgRate,
       "rlStormCtrlRateLimCfgUnit": rlStormCtrlRateLimCfgUnit,
       "rlStormCtrlRateLimCfgAction": rlStormCtrlRateLimCfgAction,
       "rlStormCtrlRateLimCfgBurst": rlStormCtrlRateLimCfgBurst,
       "rlStormCtrlRateLimOperTable": rlStormCtrlRateLimOperTable,
       "rlStormCtrlRateLimOperEntry": rlStormCtrlRateLimOperEntry,
       "rlStormCtrlRateLimOperPassCnt": rlStormCtrlRateLimOperPassCnt,
       "rlStormCtrlRateLimOperDropCnt": rlStormCtrlRateLimOperDropCnt,
       "rlStormCtrlRateLimOperLastDropTime": rlStormCtrlRateLimOperLastDropTime,
       "rlStormCtrlClearCountersTable": rlStormCtrlClearCountersTable,
       "rlStormCtrlClearCountersEntry": rlStormCtrlClearCountersEntry,
       "rlStormCtrlClearCountersIndex": rlStormCtrlClearCountersIndex,
       "rlStormCtrlClearCountersTraffic": rlStormCtrlClearCountersTraffic,
       "rlStormCtrlClearCountersInterface": rlStormCtrlClearCountersInterface}
)
