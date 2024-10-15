# SNMP MIB module (SW-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-CFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:48 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbSwitchConfig_ObjectIdentity = ObjectIdentity
nbSwitchConfig = _NbSwitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13)
)
_NbSwMacTable_Object = MibTable
nbSwMacTable = _NbSwMacTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 5)
)
if mibBuilder.loadTexts:
    nbSwMacTable.setStatus("mandatory")
_NbSwMacEntry_Object = MibTableRow
nbSwMacEntry = _NbSwMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 5, 1)
)
nbSwMacEntry.setIndexNames(
    (0, "SW-CFG-MIB", "nbSwMac"),
    (0, "SW-CFG-MIB", "nbSwMacVid"),
)
if mibBuilder.loadTexts:
    nbSwMacEntry.setStatus("mandatory")
_NbSwMac_Type = MacAddress
_NbSwMac_Object = MibTableColumn
nbSwMac = _NbSwMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 5, 1, 1),
    _NbSwMac_Type()
)
nbSwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwMac.setStatus("mandatory")


class _NbSwMacVid_Type(Integer32):
    """Custom type nbSwMacVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_NbSwMacVid_Type.__name__ = "Integer32"
_NbSwMacVid_Object = MibTableColumn
nbSwMacVid = _NbSwMacVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 5, 1, 2),
    _NbSwMacVid_Type()
)
nbSwMacVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwMacVid.setStatus("mandatory")


class _NbSwMacVidx_Type(Integer32):
    """Custom type nbSwMacVidx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_NbSwMacVidx_Type.__name__ = "Integer32"
_NbSwMacVidx_Object = MibTableColumn
nbSwMacVidx = _NbSwMacVidx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 5, 1, 3),
    _NbSwMacVidx_Type()
)
nbSwMacVidx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSwMacVidx.setStatus("mandatory")
_NbSwMacGetViewIndex_Type = Integer32
_NbSwMacGetViewIndex_Object = MibTableColumn
nbSwMacGetViewIndex = _NbSwMacGetViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 5, 1, 4),
    _NbSwMacGetViewIndex_Type()
)
nbSwMacGetViewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwMacGetViewIndex.setStatus("mandatory")


class _NbSwMacPort_Type(Integer32):
    """Custom type nbSwMacPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NbSwMacPort_Type.__name__ = "Integer32"
_NbSwMacPort_Object = MibTableColumn
nbSwMacPort = _NbSwMacPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 5, 1, 5),
    _NbSwMacPort_Type()
)
nbSwMacPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSwMacPort.setStatus("mandatory")


class _NbSwMacMode_Type(Integer32):
    """Custom type nbSwMacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_NbSwMacMode_Type.__name__ = "Integer32"
_NbSwMacMode_Object = MibTableColumn
nbSwMacMode = _NbSwMacMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 5, 1, 6),
    _NbSwMacMode_Type()
)
nbSwMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSwMacMode.setStatus("mandatory")


class _NbSwMacTagged_Type(Integer32):
    """Custom type nbSwMacTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NbSwMacTagged_Type.__name__ = "Integer32"
_NbSwMacTagged_Object = MibTableColumn
nbSwMacTagged = _NbSwMacTagged_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 5, 1, 7),
    _NbSwMacTagged_Type()
)
nbSwMacTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSwMacTagged.setStatus("mandatory")


class _NbSwMacStatus_Type(Integer32):
    """Custom type nbSwMacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbSwMacStatus_Type.__name__ = "Integer32"
_NbSwMacStatus_Object = MibTableColumn
nbSwMacStatus = _NbSwMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 5, 1, 8),
    _NbSwMacStatus_Type()
)
nbSwMacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSwMacStatus.setStatus("mandatory")
_NbSwPortCfg_ObjectIdentity = ObjectIdentity
nbSwPortCfg = _NbSwPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6)
)
_NbSwPortsMaxNumber_Type = Integer32
_NbSwPortsMaxNumber_Object = MibScalar
nbSwPortsMaxNumber = _NbSwPortsMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 1),
    _NbSwPortsMaxNumber_Type()
)
nbSwPortsMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortsMaxNumber.setStatus("mandatory")
_NbSwPortsActualNumber_Type = Integer32
_NbSwPortsActualNumber_Object = MibScalar
nbSwPortsActualNumber = _NbSwPortsActualNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 2),
    _NbSwPortsActualNumber_Type()
)
nbSwPortsActualNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortsActualNumber.setStatus("mandatory")
_NbSwPortTable_Object = MibTable
nbSwPortTable = _NbSwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3)
)
if mibBuilder.loadTexts:
    nbSwPortTable.setStatus("mandatory")
_NbSwPortEntry_Object = MibTableRow
nbSwPortEntry = _NbSwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1)
)
nbSwPortEntry.setIndexNames(
    (0, "SW-CFG-MIB", "nbSwPortIndex"),
)
if mibBuilder.loadTexts:
    nbSwPortEntry.setStatus("mandatory")
_NbSwPortIndex_Type = Integer32
_NbSwPortIndex_Object = MibTableColumn
nbSwPortIndex = _NbSwPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 1),
    _NbSwPortIndex_Type()
)
nbSwPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortIndex.setStatus("mandatory")


class _NbSwPortLanType_Type(Integer32):
    """Custom type nbSwPortLanType based on Integer32"""
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
        *(("atmLane", 7),
          ("eth10", 2),
          ("eth10-100", 4),
          ("eth10-100Grp", 9),
          ("eth100", 3),
          ("eth1000B", 6),
          ("eth100B", 5),
          ("eth100Grp", 8),
          ("fddi", 10),
          ("none", 1))
    )


_NbSwPortLanType_Type.__name__ = "Integer32"
_NbSwPortLanType_Object = MibTableColumn
nbSwPortLanType = _NbSwPortLanType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 2),
    _NbSwPortLanType_Type()
)
nbSwPortLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortLanType.setStatus("mandatory")


class _NbSwPortIfType_Type(Integer32):
    """Custom type nbSwPortIfType based on Integer32"""
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
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("aui", 1),
          ("auiTp", 3),
          ("coax", 5),
          ("foLxM", 10),
          ("foLxS1", 11),
          ("foLxS2", 12),
          ("foLxS3", 13),
          ("foM", 14),
          ("foMX", 15),
          ("foMm", 6),
          ("foS1", 16),
          ("foS2", 17),
          ("foS3", 18),
          ("foSm", 7),
          ("foSxM", 9),
          ("none", 8),
          ("tp", 2),
          ("tpfd", 4))
    )


_NbSwPortIfType_Type.__name__ = "Integer32"
_NbSwPortIfType_Object = MibTableColumn
nbSwPortIfType = _NbSwPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 3),
    _NbSwPortIfType_Type()
)
nbSwPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortIfType.setStatus("mandatory")


class _NbSwPortLink_Type(Integer32):
    """Custom type nbSwPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_NbSwPortLink_Type.__name__ = "Integer32"
_NbSwPortLink_Object = MibTableColumn
nbSwPortLink = _NbSwPortLink_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 5),
    _NbSwPortLink_Type()
)
nbSwPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortLink.setStatus("mandatory")


class _NbSwPortFctrl_Type(Integer32):
    """Custom type nbSwPortFctrl based on Integer32"""
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
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_NbSwPortFctrl_Type.__name__ = "Integer32"
_NbSwPortFctrl_Object = MibTableColumn
nbSwPortFctrl = _NbSwPortFctrl_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 6),
    _NbSwPortFctrl_Type()
)
nbSwPortFctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSwPortFctrl.setStatus("mandatory")


class _NbSwPortDplex_Type(Integer32):
    """Custom type nbSwPortDplex based on Integer32"""
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
        *(("fullDuplex", 3),
          ("halfDuplex", 2),
          ("other", 1))
    )


_NbSwPortDplex_Type.__name__ = "Integer32"
_NbSwPortDplex_Object = MibTableColumn
nbSwPortDplex = _NbSwPortDplex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 7),
    _NbSwPortDplex_Type()
)
nbSwPortDplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSwPortDplex.setStatus("mandatory")


class _NbSwPortSpeedSelect_Type(Integer32):
    """Custom type nbSwPortSpeedSelect based on Integer32"""
    defaultValue = 2

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
        *(("autoSense", 2),
          ("force10", 3),
          ("force100", 4),
          ("force1000", 5),
          ("other", 1))
    )


_NbSwPortSpeedSelect_Type.__name__ = "Integer32"
_NbSwPortSpeedSelect_Object = MibTableColumn
nbSwPortSpeedSelect = _NbSwPortSpeedSelect_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 8),
    _NbSwPortSpeedSelect_Type()
)
nbSwPortSpeedSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSwPortSpeedSelect.setStatus("mandatory")
_NbSwPortSpeed_Type = Integer32
_NbSwPortSpeed_Object = MibTableColumn
nbSwPortSpeed = _NbSwPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 9),
    _NbSwPortSpeed_Type()
)
nbSwPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortSpeed.setStatus("mandatory")


class _NbSwPortEnable_Type(Integer32):
    """Custom type nbSwPortEnable based on Integer32"""
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
        *(("other", 1),
          ("portDisable", 2),
          ("portEnable", 3))
    )


_NbSwPortEnable_Type.__name__ = "Integer32"
_NbSwPortEnable_Object = MibTableColumn
nbSwPortEnable = _NbSwPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 10),
    _NbSwPortEnable_Type()
)
nbSwPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSwPortEnable.setStatus("mandatory")


class _NbSwPortIsvpMode_Type(Integer32):
    """Custom type nbSwPortIsvpMode based on Integer32"""
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
        *(("access", 2),
          ("nonIsvp", 4),
          ("other", 1),
          ("trunk", 3))
    )


_NbSwPortIsvpMode_Type.__name__ = "Integer32"
_NbSwPortIsvpMode_Object = MibTableColumn
nbSwPortIsvpMode = _NbSwPortIsvpMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 11),
    _NbSwPortIsvpMode_Type()
)
nbSwPortIsvpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSwPortIsvpMode.setStatus("mandatory")


class _NbSwPortValid_Type(Integer32):
    """Custom type nbSwPortValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broken", 2),
          ("valid", 1))
    )


_NbSwPortValid_Type.__name__ = "Integer32"
_NbSwPortValid_Object = MibTableColumn
nbSwPortValid = _NbSwPortValid_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 6, 3, 1, 12),
    _NbSwPortValid_Type()
)
nbSwPortValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortValid.setStatus("mandatory")
_NbSwPortStatTable_Object = MibTable
nbSwPortStatTable = _NbSwPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7)
)
if mibBuilder.loadTexts:
    nbSwPortStatTable.setStatus("mandatory")
_NbSwPortStatEntry_Object = MibTableRow
nbSwPortStatEntry = _NbSwPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1)
)
nbSwPortStatEntry.setIndexNames(
    (0, "SW-CFG-MIB", "nbSwPortStatIndex"),
)
if mibBuilder.loadTexts:
    nbSwPortStatEntry.setStatus("mandatory")
_NbSwPortStatIndex_Type = Integer32
_NbSwPortStatIndex_Object = MibTableColumn
nbSwPortStatIndex = _NbSwPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 1),
    _NbSwPortStatIndex_Type()
)
nbSwPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatIndex.setStatus("mandatory")
_NbSwPortStatBtRec_Type = Counter32
_NbSwPortStatBtRec_Object = MibTableColumn
nbSwPortStatBtRec = _NbSwPortStatBtRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 2),
    _NbSwPortStatBtRec_Type()
)
nbSwPortStatBtRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatBtRec.setStatus("mandatory")
_NbSwPortStatFrRec_Type = Counter32
_NbSwPortStatFrRec_Object = MibTableColumn
nbSwPortStatFrRec = _NbSwPortStatFrRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 3),
    _NbSwPortStatFrRec_Type()
)
nbSwPortStatFrRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatFrRec.setStatus("mandatory")
_NbSwPortStatMulticastFrRec_Type = Counter32
_NbSwPortStatMulticastFrRec_Object = MibTableColumn
nbSwPortStatMulticastFrRec = _NbSwPortStatMulticastFrRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 4),
    _NbSwPortStatMulticastFrRec_Type()
)
nbSwPortStatMulticastFrRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatMulticastFrRec.setStatus("mandatory")
_NbSwPortStatBroadcastFrRec_Type = Counter32
_NbSwPortStatBroadcastFrRec_Object = MibTableColumn
nbSwPortStatBroadcastFrRec = _NbSwPortStatBroadcastFrRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 5),
    _NbSwPortStatBroadcastFrRec_Type()
)
nbSwPortStatBroadcastFrRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatBroadcastFrRec.setStatus("mandatory")
_NbSwPortStatUnicastFrRec_Type = Counter32
_NbSwPortStatUnicastFrRec_Object = MibTableColumn
nbSwPortStatUnicastFrRec = _NbSwPortStatUnicastFrRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 6),
    _NbSwPortStatUnicastFrRec_Type()
)
nbSwPortStatUnicastFrRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatUnicastFrRec.setStatus("mandatory")
_NbSwPortStatBtSent_Type = Counter32
_NbSwPortStatBtSent_Object = MibTableColumn
nbSwPortStatBtSent = _NbSwPortStatBtSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 7),
    _NbSwPortStatBtSent_Type()
)
nbSwPortStatBtSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatBtSent.setStatus("mandatory")
_NbSwPortStatFrSent_Type = Counter32
_NbSwPortStatFrSent_Object = MibTableColumn
nbSwPortStatFrSent = _NbSwPortStatFrSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 8),
    _NbSwPortStatFrSent_Type()
)
nbSwPortStatFrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatFrSent.setStatus("mandatory")
_NbSwPortStatExcessiveCollis_Type = Counter32
_NbSwPortStatExcessiveCollis_Object = MibTableColumn
nbSwPortStatExcessiveCollis = _NbSwPortStatExcessiveCollis_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 9),
    _NbSwPortStatExcessiveCollis_Type()
)
nbSwPortStatExcessiveCollis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatExcessiveCollis.setStatus("mandatory")
_NbSwPortStatSingleCollis_Type = Counter32
_NbSwPortStatSingleCollis_Object = MibTableColumn
nbSwPortStatSingleCollis = _NbSwPortStatSingleCollis_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 10),
    _NbSwPortStatSingleCollis_Type()
)
nbSwPortStatSingleCollis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatSingleCollis.setStatus("mandatory")
_NbSwPortStatMultipleCollis_Type = Counter32
_NbSwPortStatMultipleCollis_Object = MibTableColumn
nbSwPortStatMultipleCollis = _NbSwPortStatMultipleCollis_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 11),
    _NbSwPortStatMultipleCollis_Type()
)
nbSwPortStatMultipleCollis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatMultipleCollis.setStatus("mandatory")
_NbSwPortStatLateCollis_Type = Counter32
_NbSwPortStatLateCollis_Object = MibTableColumn
nbSwPortStatLateCollis = _NbSwPortStatLateCollis_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 12),
    _NbSwPortStatLateCollis_Type()
)
nbSwPortStatLateCollis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatLateCollis.setStatus("mandatory")
_NbSwPortStatAlignmentErrors_Type = Counter32
_NbSwPortStatAlignmentErrors_Object = MibTableColumn
nbSwPortStatAlignmentErrors = _NbSwPortStatAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 13),
    _NbSwPortStatAlignmentErrors_Type()
)
nbSwPortStatAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatAlignmentErrors.setStatus("mandatory")
_NbSwPortStatFCSErrors_Type = Counter32
_NbSwPortStatFCSErrors_Object = MibTableColumn
nbSwPortStatFCSErrors = _NbSwPortStatFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 14),
    _NbSwPortStatFCSErrors_Type()
)
nbSwPortStatFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatFCSErrors.setStatus("mandatory")
_NbSwPortStatFrDiscarded_Type = Counter32
_NbSwPortStatFrDiscarded_Object = MibTableColumn
nbSwPortStatFrDiscarded = _NbSwPortStatFrDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 15),
    _NbSwPortStatFrDiscarded_Type()
)
nbSwPortStatFrDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatFrDiscarded.setStatus("mandatory")
_NbSwPortStatBadLongFr_Type = Counter32
_NbSwPortStatBadLongFr_Object = MibTableColumn
nbSwPortStatBadLongFr = _NbSwPortStatBadLongFr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 16),
    _NbSwPortStatBadLongFr_Type()
)
nbSwPortStatBadLongFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatBadLongFr.setStatus("mandatory")
_NbSwPortStatGoodLongFr_Type = Counter32
_NbSwPortStatGoodLongFr_Object = MibTableColumn
nbSwPortStatGoodLongFr = _NbSwPortStatGoodLongFr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 17),
    _NbSwPortStatGoodLongFr_Type()
)
nbSwPortStatGoodLongFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatGoodLongFr.setStatus("mandatory")
_NbSwPortStatGoodShortFr_Type = Counter32
_NbSwPortStatGoodShortFr_Object = MibTableColumn
nbSwPortStatGoodShortFr = _NbSwPortStatGoodShortFr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 18),
    _NbSwPortStatGoodShortFr_Type()
)
nbSwPortStatGoodShortFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatGoodShortFr.setStatus("mandatory")


class _NbSwPortStatValid_Type(Integer32):
    """Custom type nbSwPortStatValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broken", 2),
          ("valid", 1))
    )


_NbSwPortStatValid_Type.__name__ = "Integer32"
_NbSwPortStatValid_Object = MibTableColumn
nbSwPortStatValid = _NbSwPortStatValid_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 13, 7, 1, 19),
    _NbSwPortStatValid_Type()
)
nbSwPortStatValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSwPortStatValid.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-CFG-MIB",
    **{"MacAddress": MacAddress,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbSwitchConfig": nbSwitchConfig,
       "nbSwMacTable": nbSwMacTable,
       "nbSwMacEntry": nbSwMacEntry,
       "nbSwMac": nbSwMac,
       "nbSwMacVid": nbSwMacVid,
       "nbSwMacVidx": nbSwMacVidx,
       "nbSwMacGetViewIndex": nbSwMacGetViewIndex,
       "nbSwMacPort": nbSwMacPort,
       "nbSwMacMode": nbSwMacMode,
       "nbSwMacTagged": nbSwMacTagged,
       "nbSwMacStatus": nbSwMacStatus,
       "nbSwPortCfg": nbSwPortCfg,
       "nbSwPortsMaxNumber": nbSwPortsMaxNumber,
       "nbSwPortsActualNumber": nbSwPortsActualNumber,
       "nbSwPortTable": nbSwPortTable,
       "nbSwPortEntry": nbSwPortEntry,
       "nbSwPortIndex": nbSwPortIndex,
       "nbSwPortLanType": nbSwPortLanType,
       "nbSwPortIfType": nbSwPortIfType,
       "nbSwPortLink": nbSwPortLink,
       "nbSwPortFctrl": nbSwPortFctrl,
       "nbSwPortDplex": nbSwPortDplex,
       "nbSwPortSpeedSelect": nbSwPortSpeedSelect,
       "nbSwPortSpeed": nbSwPortSpeed,
       "nbSwPortEnable": nbSwPortEnable,
       "nbSwPortIsvpMode": nbSwPortIsvpMode,
       "nbSwPortValid": nbSwPortValid,
       "nbSwPortStatTable": nbSwPortStatTable,
       "nbSwPortStatEntry": nbSwPortStatEntry,
       "nbSwPortStatIndex": nbSwPortStatIndex,
       "nbSwPortStatBtRec": nbSwPortStatBtRec,
       "nbSwPortStatFrRec": nbSwPortStatFrRec,
       "nbSwPortStatMulticastFrRec": nbSwPortStatMulticastFrRec,
       "nbSwPortStatBroadcastFrRec": nbSwPortStatBroadcastFrRec,
       "nbSwPortStatUnicastFrRec": nbSwPortStatUnicastFrRec,
       "nbSwPortStatBtSent": nbSwPortStatBtSent,
       "nbSwPortStatFrSent": nbSwPortStatFrSent,
       "nbSwPortStatExcessiveCollis": nbSwPortStatExcessiveCollis,
       "nbSwPortStatSingleCollis": nbSwPortStatSingleCollis,
       "nbSwPortStatMultipleCollis": nbSwPortStatMultipleCollis,
       "nbSwPortStatLateCollis": nbSwPortStatLateCollis,
       "nbSwPortStatAlignmentErrors": nbSwPortStatAlignmentErrors,
       "nbSwPortStatFCSErrors": nbSwPortStatFCSErrors,
       "nbSwPortStatFrDiscarded": nbSwPortStatFrDiscarded,
       "nbSwPortStatBadLongFr": nbSwPortStatBadLongFr,
       "nbSwPortStatGoodLongFr": nbSwPortStatGoodLongFr,
       "nbSwPortStatGoodShortFr": nbSwPortStatGoodShortFr,
       "nbSwPortStatValid": nbSwPortStatValid}
)
