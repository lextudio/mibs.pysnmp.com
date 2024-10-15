# SNMP MIB module (RITTAL-CMC-III-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RITTAL-CMC-III-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:38 2024
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

(rittal,) = mibBuilder.importSymbols(
    "RITTAL-SMI-MIB",
    "rittal")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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

cmcIII = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7)
)
cmcIII.setRevisions(
        ("2016-02-02 00:00",
         "2015-10-27 00:00",
         "2015-01-23 00:00",
         "2014-07-10 00:00",
         "2013-11-10 00:00",
         "2013-05-01 00:00",
         "2012-08-30 00:00",
         "2011-09-02 00:00",
         "2011-04-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmcIIINotifications_ObjectIdentity = ObjectIdentity
cmcIIINotifications = _CmcIIINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 0)
)
_CmcIIIMibRev_ObjectIdentity = ObjectIdentity
cmcIIIMibRev = _CmcIIIMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 1)
)


class _CmcIIIMibMajRev_Type(Unsigned32):
    """Custom type cmcIIIMibMajRev based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIMibMajRev_Type.__name__ = "Unsigned32"
_CmcIIIMibMajRev_Object = MibScalar
cmcIIIMibMajRev = _CmcIIIMibMajRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 1, 1),
    _CmcIIIMibMajRev_Type()
)
cmcIIIMibMajRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIMibMajRev.setStatus("current")


class _CmcIIIMibMinRev_Type(Unsigned32):
    """Custom type cmcIIIMibMinRev based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmcIIIMibMinRev_Type.__name__ = "Unsigned32"
_CmcIIIMibMinRev_Object = MibScalar
cmcIIIMibMinRev = _CmcIIIMibMinRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 1, 2),
    _CmcIIIMibMinRev_Type()
)
cmcIIIMibMinRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIMibMinRev.setStatus("current")


class _CmcIIIAgentRev_Type(DisplayString):
    """Custom type cmcIIIAgentRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmcIIIAgentRev_Type.__name__ = "DisplayString"
_CmcIIIAgentRev_Object = MibScalar
cmcIIIAgentRev = _CmcIIIAgentRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 1, 3),
    _CmcIIIAgentRev_Type()
)
cmcIIIAgentRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIAgentRev.setStatus("current")


class _CmcIIICapabilityRev_Type(Unsigned32):
    """Custom type cmcIIICapabilityRev based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 39999),
    )


_CmcIIICapabilityRev_Type.__name__ = "Unsigned32"
_CmcIIICapabilityRev_Object = MibScalar
cmcIIICapabilityRev = _CmcIIICapabilityRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 1, 4),
    _CmcIIICapabilityRev_Type()
)
cmcIIICapabilityRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIICapabilityRev.setStatus("current")
_CmcIIIUnit_ObjectIdentity = ObjectIdentity
cmcIIIUnit = _CmcIIIUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2)
)


class _CmcIIIUnitStatus_Type(Integer32):
    """Custom type cmcIIIUnitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1),
          ("overload", 3))
    )


_CmcIIIUnitStatus_Type.__name__ = "Integer32"
_CmcIIIUnitStatus_Object = MibScalar
cmcIIIUnitStatus = _CmcIIIUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 1),
    _CmcIIIUnitStatus_Type()
)
cmcIIIUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitStatus.setStatus("current")


class _CmcIIIUnitURL_Type(DisplayString):
    """Custom type cmcIIIUnitURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CmcIIIUnitURL_Type.__name__ = "DisplayString"
_CmcIIIUnitURL_Object = MibScalar
cmcIIIUnitURL = _CmcIIIUnitURL_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 2),
    _CmcIIIUnitURL_Type()
)
cmcIIIUnitURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitURL.setStatus("current")


class _CmcIIIUnitHWRev_Type(DisplayString):
    """Custom type cmcIIIUnitHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CmcIIIUnitHWRev_Type.__name__ = "DisplayString"
_CmcIIIUnitHWRev_Object = MibScalar
cmcIIIUnitHWRev = _CmcIIIUnitHWRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 3),
    _CmcIIIUnitHWRev_Type()
)
cmcIIIUnitHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitHWRev.setStatus("current")


class _CmcIIIUnitFWRev_Type(DisplayString):
    """Custom type cmcIIIUnitFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CmcIIIUnitFWRev_Type.__name__ = "DisplayString"
_CmcIIIUnitFWRev_Object = MibScalar
cmcIIIUnitFWRev = _CmcIIIUnitFWRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 4),
    _CmcIIIUnitFWRev_Type()
)
cmcIIIUnitFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitFWRev.setStatus("current")


class _CmcIIIUnitOSRev_Type(DisplayString):
    """Custom type cmcIIIUnitOSRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmcIIIUnitOSRev_Type.__name__ = "DisplayString"
_CmcIIIUnitOSRev_Object = MibScalar
cmcIIIUnitOSRev = _CmcIIIUnitOSRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 5),
    _CmcIIIUnitOSRev_Type()
)
cmcIIIUnitOSRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitOSRev.setStatus("current")


class _CmcIIIUnitSerial_Type(DisplayString):
    """Custom type cmcIIIUnitSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmcIIIUnitSerial_Type.__name__ = "DisplayString"
_CmcIIIUnitSerial_Object = MibScalar
cmcIIIUnitSerial = _CmcIIIUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 6),
    _CmcIIIUnitSerial_Type()
)
cmcIIIUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitSerial.setStatus("current")


class _CmcIIIUnitProd_Type(DisplayString):
    """Custom type cmcIIIUnitProd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CmcIIIUnitProd_Type.__name__ = "DisplayString"
_CmcIIIUnitProd_Object = MibScalar
cmcIIIUnitProd = _CmcIIIUnitProd_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 7),
    _CmcIIIUnitProd_Type()
)
cmcIIIUnitProd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitProd.setStatus("current")


class _CmcIIIUnitType_Type(Integer32):
    """Custom type cmcIIIUnitType based on Integer32"""
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
        *(("compact", 3),
          ("lcp", 4),
          ("pdu", 5),
          ("pu", 2),
          ("rms", 6),
          ("unknown", 1))
    )


_CmcIIIUnitType_Type.__name__ = "Integer32"
_CmcIIIUnitType_Object = MibScalar
cmcIIIUnitType = _CmcIIIUnitType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 8),
    _CmcIIIUnitType_Type()
)
cmcIIIUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitType.setStatus("current")


class _CmcIIIUnitCurrentSource_Type(Integer32):
    """Custom type cmcIIIUnitCurrentSource based on Integer32"""
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
        *(("acAdapter", 2),
          ("poe", 4),
          ("terminalStrip", 3),
          ("unknown", 1),
          ("usb", 5))
    )


_CmcIIIUnitCurrentSource_Type.__name__ = "Integer32"
_CmcIIIUnitCurrentSource_Object = MibScalar
cmcIIIUnitCurrentSource = _CmcIIIUnitCurrentSource_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 9),
    _CmcIIIUnitCurrentSource_Type()
)
cmcIIIUnitCurrentSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitCurrentSource.setStatus("current")
_CmcIIICan0CurrentConsumption_Type = Integer32
_CmcIIICan0CurrentConsumption_Object = MibScalar
cmcIIICan0CurrentConsumption = _CmcIIICan0CurrentConsumption_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 10),
    _CmcIIICan0CurrentConsumption_Type()
)
cmcIIICan0CurrentConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIICan0CurrentConsumption.setStatus("current")
_CmcIIICan1CurrentConsumption_Type = Integer32
_CmcIIICan1CurrentConsumption_Object = MibScalar
cmcIIICan1CurrentConsumption = _CmcIIICan1CurrentConsumption_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 11),
    _CmcIIICan1CurrentConsumption_Type()
)
cmcIIICan1CurrentConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIICan1CurrentConsumption.setStatus("current")
_CmcIIIUnitUpTime_Type = Unsigned32
_CmcIIIUnitUpTime_Object = MibScalar
cmcIIIUnitUpTime = _CmcIIIUnitUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 12),
    _CmcIIIUnitUpTime_Type()
)
cmcIIIUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitUpTime.setStatus("current")


class _CmcIIIUnitMode_Type(Integer32):
    """Custom type cmcIIIUnitMode based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("collectSlaves", 6),
          ("localInit", 1),
          ("localOnline", 5),
          ("online", 8),
          ("prepareUpgrade", 9),
          ("pwrDelay", 3),
          ("reorganizeBus", 7),
          ("restartBus", 4),
          ("start", 2),
          ("terminate", 11),
          ("upgradeSensor", 10))
    )


_CmcIIIUnitMode_Type.__name__ = "Integer32"
_CmcIIIUnitMode_Object = MibScalar
cmcIIIUnitMode = _CmcIIIUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 13),
    _CmcIIIUnitMode_Type()
)
cmcIIIUnitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitMode.setStatus("current")
_CmcIIIUnitLoadTable_Object = MibTable
cmcIIIUnitLoadTable = _CmcIIIUnitLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 14)
)
if mibBuilder.loadTexts:
    cmcIIIUnitLoadTable.setStatus("current")
_CmcIIIUnitLoadEntry_Object = MibTableRow
cmcIIIUnitLoadEntry = _CmcIIIUnitLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 14, 1)
)
cmcIIIUnitLoadEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIUnitLoadIndex"),
)
if mibBuilder.loadTexts:
    cmcIIIUnitLoadEntry.setStatus("current")


class _CmcIIIUnitLoadIndex_Type(Unsigned32):
    """Custom type cmcIIIUnitLoadIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CmcIIIUnitLoadIndex_Type.__name__ = "Unsigned32"
_CmcIIIUnitLoadIndex_Object = MibTableColumn
cmcIIIUnitLoadIndex = _CmcIIIUnitLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 14, 1, 1),
    _CmcIIIUnitLoadIndex_Type()
)
cmcIIIUnitLoadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIUnitLoadIndex.setStatus("current")
_CmcIIIUnitLoadAverage_Type = Unsigned32
_CmcIIIUnitLoadAverage_Object = MibTableColumn
cmcIIIUnitLoadAverage = _CmcIIIUnitLoadAverage_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 2, 14, 1, 2),
    _CmcIIIUnitLoadAverage_Type()
)
cmcIIIUnitLoadAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIUnitLoadAverage.setStatus("current")
_CmcIIISetup_ObjectIdentity = ObjectIdentity
cmcIIISetup = _CmcIIISetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3)
)
_CmcIIILastChangeSetup_Type = Unsigned32
_CmcIIILastChangeSetup_Object = MibScalar
cmcIIILastChangeSetup = _CmcIIILastChangeSetup_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 1),
    _CmcIIILastChangeSetup_Type()
)
cmcIIILastChangeSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeSetup.setStatus("current")
_CmcIIISetupGeneral_ObjectIdentity = ObjectIdentity
cmcIIISetupGeneral = _CmcIIISetupGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2)
)


class _CmcIIISetTempUnit_Type(Integer32):
    """Custom type cmcIIISetTempUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_CmcIIISetTempUnit_Type.__name__ = "Integer32"
_CmcIIISetTempUnit_Object = MibScalar
cmcIIISetTempUnit = _CmcIIISetTempUnit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 1),
    _CmcIIISetTempUnit_Type()
)
cmcIIISetTempUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISetTempUnit.setStatus("current")


class _CmcIIISetBeeper_Type(Integer32):
    """Custom type cmcIIISetBeeper based on Integer32"""
    defaultValue = 1

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


_CmcIIISetBeeper_Type.__name__ = "Integer32"
_CmcIIISetBeeper_Object = MibScalar
cmcIIISetBeeper = _CmcIIISetBeeper_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 2),
    _CmcIIISetBeeper_Type()
)
cmcIIISetBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISetBeeper.setStatus("current")


class _CmcIIIQuitRelay_Type(Integer32):
    """Custom type cmcIIIQuitRelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIIQuitRelay_Type.__name__ = "Integer32"
_CmcIIIQuitRelay_Object = MibScalar
cmcIIIQuitRelay = _CmcIIIQuitRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 3),
    _CmcIIIQuitRelay_Type()
)
cmcIIIQuitRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIQuitRelay.setStatus("current")


class _CmcIIILogicRelay_Type(Integer32):
    """Custom type cmcIIILogicRelay based on Integer32"""
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
        *(("closeAtAlarm", 1),
          ("disabled", 3),
          ("openAtAlarm", 2))
    )


_CmcIIILogicRelay_Type.__name__ = "Integer32"
_CmcIIILogicRelay_Object = MibScalar
cmcIIILogicRelay = _CmcIIILogicRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 4),
    _CmcIIILogicRelay_Type()
)
cmcIIILogicRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILogicRelay.setStatus("current")


class _CmcIIIUnitMsgRelay_Type(Integer32):
    """Custom type cmcIIIUnitMsgRelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIIUnitMsgRelay_Type.__name__ = "Integer32"
_CmcIIIUnitMsgRelay_Object = MibScalar
cmcIIIUnitMsgRelay = _CmcIIIUnitMsgRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 5),
    _CmcIIIUnitMsgRelay_Type()
)
cmcIIIUnitMsgRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIUnitMsgRelay.setStatus("current")


class _CmcIIIFunctionRelay_Type(Integer32):
    """Custom type cmcIIIFunctionRelay based on Integer32"""
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
        *(("alarmOnly", 2),
          ("warningOnly", 1),
          ("warningOrAlarm", 3))
    )


_CmcIIIFunctionRelay_Type.__name__ = "Integer32"
_CmcIIIFunctionRelay_Object = MibScalar
cmcIIIFunctionRelay = _CmcIIIFunctionRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 6),
    _CmcIIIFunctionRelay_Type()
)
cmcIIIFunctionRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIFunctionRelay.setStatus("current")


class _CmcIIITimeZone_Type(Integer32):
    """Custom type cmcIIITimeZone based on Integer32"""
    defaultValue = 27

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 74),
    )


_CmcIIITimeZone_Type.__name__ = "Integer32"
_CmcIIITimeZone_Object = MibScalar
cmcIIITimeZone = _CmcIIITimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 7),
    _CmcIIITimeZone_Type()
)
cmcIIITimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITimeZone.setStatus("current")


class _CmcIIISetupDate_Type(DisplayString):
    """Custom type cmcIIISetupDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_CmcIIISetupDate_Type.__name__ = "DisplayString"
_CmcIIISetupDate_Object = MibScalar
cmcIIISetupDate = _CmcIIISetupDate_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 8),
    _CmcIIISetupDate_Type()
)
cmcIIISetupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISetupDate.setStatus("current")


class _CmcIIISetupTime_Type(DisplayString):
    """Custom type cmcIIISetupTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CmcIIISetupTime_Type.__name__ = "DisplayString"
_CmcIIISetupTime_Object = MibScalar
cmcIIISetupTime = _CmcIIISetupTime_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 9),
    _CmcIIISetupTime_Type()
)
cmcIIISetupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISetupTime.setStatus("current")


class _CmcIIIWebAccess_Type(Bits):
    """Custom type cmcIIIWebAccess based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("httpEnabled", 0),
          ("httpsEnabled", 1))
    )

_CmcIIIWebAccess_Type.__name__ = "Bits"
_CmcIIIWebAccess_Object = MibScalar
cmcIIIWebAccess = _CmcIIIWebAccess_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 10),
    _CmcIIIWebAccess_Type()
)
cmcIIIWebAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIWebAccess.setStatus("current")


class _CmcIIIHttpPort_Type(Unsigned32):
    """Custom type cmcIIIHttpPort based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIHttpPort_Type.__name__ = "Unsigned32"
_CmcIIIHttpPort_Object = MibScalar
cmcIIIHttpPort = _CmcIIIHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 11),
    _CmcIIIHttpPort_Type()
)
cmcIIIHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIHttpPort.setStatus("current")


class _CmcIIIHttpsPort_Type(Unsigned32):
    """Custom type cmcIIIHttpsPort based on Unsigned32"""
    defaultValue = 443

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIHttpsPort_Type.__name__ = "Unsigned32"
_CmcIIIHttpsPort_Object = MibScalar
cmcIIIHttpsPort = _CmcIIIHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 12),
    _CmcIIIHttpsPort_Type()
)
cmcIIIHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIHttpsPort.setStatus("current")


class _CmcIIIFtpAccess_Type(Integer32):
    """Custom type cmcIIIFtpAccess based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIIFtpAccess_Type.__name__ = "Integer32"
_CmcIIIFtpAccess_Object = MibScalar
cmcIIIFtpAccess = _CmcIIIFtpAccess_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 13),
    _CmcIIIFtpAccess_Type()
)
cmcIIIFtpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIFtpAccess.setStatus("current")


class _CmcIIIFtpPort_Type(Unsigned32):
    """Custom type cmcIIIFtpPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIFtpPort_Type.__name__ = "Unsigned32"
_CmcIIIFtpPort_Object = MibScalar
cmcIIIFtpPort = _CmcIIIFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 14),
    _CmcIIIFtpPort_Type()
)
cmcIIIFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIFtpPort.setStatus("current")


class _CmcIIISshAccess_Type(Integer32):
    """Custom type cmcIIISshAccess based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIISshAccess_Type.__name__ = "Integer32"
_CmcIIISshAccess_Object = MibScalar
cmcIIISshAccess = _CmcIIISshAccess_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 15),
    _CmcIIISshAccess_Type()
)
cmcIIISshAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISshAccess.setStatus("current")


class _CmcIIISshPort_Type(Unsigned32):
    """Custom type cmcIIISshPort based on Unsigned32"""
    defaultValue = 22

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIISshPort_Type.__name__ = "Unsigned32"
_CmcIIISshPort_Object = MibScalar
cmcIIISshPort = _CmcIIISshPort_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 16),
    _CmcIIISshPort_Type()
)
cmcIIISshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISshPort.setStatus("current")


class _CmcIIITelnetAccess_Type(Integer32):
    """Custom type cmcIIITelnetAccess based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIITelnetAccess_Type.__name__ = "Integer32"
_CmcIIITelnetAccess_Object = MibScalar
cmcIIITelnetAccess = _CmcIIITelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 17),
    _CmcIIITelnetAccess_Type()
)
cmcIIITelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITelnetAccess.setStatus("current")


class _CmcIIITelnetPort_Type(Unsigned32):
    """Custom type cmcIIITelnetPort based on Unsigned32"""
    defaultValue = 23

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIITelnetPort_Type.__name__ = "Unsigned32"
_CmcIIITelnetPort_Object = MibScalar
cmcIIITelnetPort = _CmcIIITelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 18),
    _CmcIIITelnetPort_Type()
)
cmcIIITelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITelnetPort.setStatus("current")


class _CmcIIILanguage_Type(Integer32):
    """Custom type cmcIIILanguage based on Integer32"""
    defaultValue = 1

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
        *(("chinese", 7),
          ("english", 1),
          ("french", 3),
          ("german", 2),
          ("japanese", 8),
          ("portuguese", 5),
          ("russian", 6),
          ("spanish", 4))
    )


_CmcIIILanguage_Type.__name__ = "Integer32"
_CmcIIILanguage_Object = MibScalar
cmcIIILanguage = _CmcIIILanguage_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 19),
    _CmcIIILanguage_Type()
)
cmcIIILanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILanguage.setStatus("current")


class _CmcIIIOpcUaAccess_Type(Integer32):
    """Custom type cmcIIIOpcUaAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIIOpcUaAccess_Type.__name__ = "Integer32"
_CmcIIIOpcUaAccess_Object = MibScalar
cmcIIIOpcUaAccess = _CmcIIIOpcUaAccess_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 20),
    _CmcIIIOpcUaAccess_Type()
)
cmcIIIOpcUaAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIOpcUaAccess.setStatus("current")


class _CmcIIIOpcUaPort_Type(Unsigned32):
    """Custom type cmcIIIOpcUaPort based on Unsigned32"""
    defaultValue = 4840

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIOpcUaPort_Type.__name__ = "Unsigned32"
_CmcIIIOpcUaPort_Object = MibScalar
cmcIIIOpcUaPort = _CmcIIIOpcUaPort_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 2, 21),
    _CmcIIIOpcUaPort_Type()
)
cmcIIIOpcUaPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIOpcUaPort.setStatus("current")
_CmcIIISetupTimer_ObjectIdentity = ObjectIdentity
cmcIIISetupTimer = _CmcIIISetupTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3)
)
_CmcIIINumberOfTimers_Type = Integer32
_CmcIIINumberOfTimers_Object = MibScalar
cmcIIINumberOfTimers = _CmcIIINumberOfTimers_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3, 1),
    _CmcIIINumberOfTimers_Type()
)
cmcIIINumberOfTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfTimers.setStatus("current")
_CmcIIITimerTable_Object = MibTable
cmcIIITimerTable = _CmcIIITimerTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3, 2)
)
if mibBuilder.loadTexts:
    cmcIIITimerTable.setStatus("current")
_CmcIIITimerEntry_Object = MibTableRow
cmcIIITimerEntry = _CmcIIITimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3, 2, 1)
)
cmcIIITimerEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIITimerIndex"),
)
if mibBuilder.loadTexts:
    cmcIIITimerEntry.setStatus("current")


class _CmcIIITimerIndex_Type(Unsigned32):
    """Custom type cmcIIITimerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIITimerIndex_Type.__name__ = "Unsigned32"
_CmcIIITimerIndex_Object = MibTableColumn
cmcIIITimerIndex = _CmcIIITimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3, 2, 1, 1),
    _CmcIIITimerIndex_Type()
)
cmcIIITimerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIITimerIndex.setStatus("current")


class _CmcIIITimerStatus_Type(Integer32):
    """Custom type cmcIIITimerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTime", 3),
          ("switchedOff", 1),
          ("switchedOn", 2))
    )


_CmcIIITimerStatus_Type.__name__ = "Integer32"
_CmcIIITimerStatus_Object = MibTableColumn
cmcIIITimerStatus = _CmcIIITimerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3, 2, 1, 2),
    _CmcIIITimerStatus_Type()
)
cmcIIITimerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIITimerStatus.setStatus("current")


class _CmcIIITimerDayOfWeek_Type(Integer32):
    """Custom type cmcIIITimerDayOfWeek based on Integer32"""
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
        *(("fri", 6),
          ("mon", 2),
          ("mon2fri", 9),
          ("mon2sun", 10),
          ("sat", 7),
          ("sat2sun", 8),
          ("sun", 1),
          ("thu", 5),
          ("tue", 3),
          ("wed", 4))
    )


_CmcIIITimerDayOfWeek_Type.__name__ = "Integer32"
_CmcIIITimerDayOfWeek_Object = MibTableColumn
cmcIIITimerDayOfWeek = _CmcIIITimerDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3, 2, 1, 3),
    _CmcIIITimerDayOfWeek_Type()
)
cmcIIITimerDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITimerDayOfWeek.setStatus("current")


class _CmcIIITimeOn_Type(DisplayString):
    """Custom type cmcIIITimeOn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_CmcIIITimeOn_Type.__name__ = "DisplayString"
_CmcIIITimeOn_Object = MibTableColumn
cmcIIITimeOn = _CmcIIITimeOn_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3, 2, 1, 4),
    _CmcIIITimeOn_Type()
)
cmcIIITimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITimeOn.setStatus("current")


class _CmcIIITimeOff_Type(DisplayString):
    """Custom type cmcIIITimeOff based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_CmcIIITimeOff_Type.__name__ = "DisplayString"
_CmcIIITimeOff_Object = MibTableColumn
cmcIIITimeOff = _CmcIIITimeOff_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3, 2, 1, 5),
    _CmcIIITimeOff_Type()
)
cmcIIITimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITimeOff.setStatus("current")


class _CmcIIITimeControl_Type(Integer32):
    """Custom type cmcIIITimeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIITimeControl_Type.__name__ = "Integer32"
_CmcIIITimeControl_Object = MibTableColumn
cmcIIITimeControl = _CmcIIITimeControl_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3, 2, 1, 6),
    _CmcIIITimeControl_Type()
)
cmcIIITimeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITimeControl.setStatus("current")


class _CmcIIITimerFunction_Type(Integer32):
    """Custom type cmcIIITimerFunction based on Integer32"""
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
        *(("disKeypads", 1),
          ("disSMS1", 7),
          ("disSMS2", 8),
          ("disSMS3", 9),
          ("disSMS4", 10),
          ("disTrapRec1", 3),
          ("disTrapRec2", 4),
          ("disTrapRec3", 5),
          ("disTrapRec4", 6),
          ("schedule1", 11),
          ("schedule2", 12),
          ("schedule3", 13),
          ("schedule4", 14),
          ("schedule5", 15),
          ("schedule6", 16),
          ("schedule7", 17),
          ("schedule8", 18),
          ("unlDoors", 2))
    )


_CmcIIITimerFunction_Type.__name__ = "Integer32"
_CmcIIITimerFunction_Object = MibTableColumn
cmcIIITimerFunction = _CmcIIITimerFunction_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 3, 2, 1, 7),
    _CmcIIITimerFunction_Type()
)
cmcIIITimerFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITimerFunction.setStatus("current")
_CmcIIISetupTrap_ObjectIdentity = ObjectIdentity
cmcIIISetupTrap = _CmcIIISetupTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 4)
)
_CmcIIINumberOfTrapReceivers_Type = Integer32
_CmcIIINumberOfTrapReceivers_Object = MibScalar
cmcIIINumberOfTrapReceivers = _CmcIIINumberOfTrapReceivers_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 4, 1),
    _CmcIIINumberOfTrapReceivers_Type()
)
cmcIIINumberOfTrapReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfTrapReceivers.setStatus("current")
_CmcIIITrapReceiverTable_Object = MibTable
cmcIIITrapReceiverTable = _CmcIIITrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 4, 2)
)
if mibBuilder.loadTexts:
    cmcIIITrapReceiverTable.setStatus("current")
_CmcIIITrapReceiverEntry_Object = MibTableRow
cmcIIITrapReceiverEntry = _CmcIIITrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 4, 2, 1)
)
cmcIIITrapReceiverEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIITrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    cmcIIITrapReceiverEntry.setStatus("current")


class _CmcIIITrapReceiverIndex_Type(Unsigned32):
    """Custom type cmcIIITrapReceiverIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIITrapReceiverIndex_Type.__name__ = "Unsigned32"
_CmcIIITrapReceiverIndex_Object = MibTableColumn
cmcIIITrapReceiverIndex = _CmcIIITrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 4, 2, 1, 1),
    _CmcIIITrapReceiverIndex_Type()
)
cmcIIITrapReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIITrapReceiverIndex.setStatus("current")


class _CmcIIITrapReceiverStatus_Type(Integer32):
    """Custom type cmcIIITrapReceiverStatus based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("snmpv1Trap", 2),
          ("snmpv2cInform", 4),
          ("snmpv2cTrap", 3),
          ("snmpv3Inform", 6),
          ("snmpv3Trap", 5))
    )


_CmcIIITrapReceiverStatus_Type.__name__ = "Integer32"
_CmcIIITrapReceiverStatus_Object = MibTableColumn
cmcIIITrapReceiverStatus = _CmcIIITrapReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 4, 2, 1, 2),
    _CmcIIITrapReceiverStatus_Type()
)
cmcIIITrapReceiverStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITrapReceiverStatus.setStatus("current")


class _CmcIIITrapReceiverIpAddress_Type(DisplayString):
    """Custom type cmcIIITrapReceiverIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIITrapReceiverIpAddress_Type.__name__ = "DisplayString"
_CmcIIITrapReceiverIpAddress_Object = MibTableColumn
cmcIIITrapReceiverIpAddress = _CmcIIITrapReceiverIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 4, 2, 1, 3),
    _CmcIIITrapReceiverIpAddress_Type()
)
cmcIIITrapReceiverIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITrapReceiverIpAddress.setStatus("current")
_CmcIIISetupSMTP_ObjectIdentity = ObjectIdentity
cmcIIISetupSMTP = _CmcIIISetupSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5)
)


class _CmcIIISmtpStatus_Type(Integer32):
    """Custom type cmcIIISmtpStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIISmtpStatus_Type.__name__ = "Integer32"
_CmcIIISmtpStatus_Object = MibScalar
cmcIIISmtpStatus = _CmcIIISmtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 1),
    _CmcIIISmtpStatus_Type()
)
cmcIIISmtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmtpStatus.setStatus("current")


class _CmcIIISmtpServer_Type(DisplayString):
    """Custom type cmcIIISmtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIISmtpServer_Type.__name__ = "DisplayString"
_CmcIIISmtpServer_Object = MibScalar
cmcIIISmtpServer = _CmcIIISmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 2),
    _CmcIIISmtpServer_Type()
)
cmcIIISmtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmtpServer.setStatus("current")


class _CmcIIISmtpPort_Type(Unsigned32):
    """Custom type cmcIIISmtpPort based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIISmtpPort_Type.__name__ = "Unsigned32"
_CmcIIISmtpPort_Object = MibScalar
cmcIIISmtpPort = _CmcIIISmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 3),
    _CmcIIISmtpPort_Type()
)
cmcIIISmtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmtpPort.setStatus("current")


class _CmcIIISmtpAuth_Type(Integer32):
    """Custom type cmcIIISmtpAuth based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledTls", 3))
    )


_CmcIIISmtpAuth_Type.__name__ = "Integer32"
_CmcIIISmtpAuth_Object = MibScalar
cmcIIISmtpAuth = _CmcIIISmtpAuth_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 4),
    _CmcIIISmtpAuth_Type()
)
cmcIIISmtpAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmtpAuth.setStatus("current")


class _CmcIIISmtpUsername_Type(DisplayString):
    """Custom type cmcIIISmtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CmcIIISmtpUsername_Type.__name__ = "DisplayString"
_CmcIIISmtpUsername_Object = MibScalar
cmcIIISmtpUsername = _CmcIIISmtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 5),
    _CmcIIISmtpUsername_Type()
)
cmcIIISmtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmtpUsername.setStatus("current")


class _CmcIIISmtpPassword_Type(DisplayString):
    """Custom type cmcIIISmtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CmcIIISmtpPassword_Type.__name__ = "DisplayString"
_CmcIIISmtpPassword_Object = MibScalar
cmcIIISmtpPassword = _CmcIIISmtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 6),
    _CmcIIISmtpPassword_Type()
)
cmcIIISmtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmtpPassword.setStatus("current")


class _CmcIIISmtpSender_Type(DisplayString):
    """Custom type cmcIIISmtpSender based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CmcIIISmtpSender_Type.__name__ = "DisplayString"
_CmcIIISmtpSender_Object = MibScalar
cmcIIISmtpSender = _CmcIIISmtpSender_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 7),
    _CmcIIISmtpSender_Type()
)
cmcIIISmtpSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmtpSender.setStatus("current")


class _CmcIIISmtpReply_Type(DisplayString):
    """Custom type cmcIIISmtpReply based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CmcIIISmtpReply_Type.__name__ = "DisplayString"
_CmcIIISmtpReply_Object = MibScalar
cmcIIISmtpReply = _CmcIIISmtpReply_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 8),
    _CmcIIISmtpReply_Type()
)
cmcIIISmtpReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmtpReply.setStatus("current")
_CmcIIINumberOfSmtpReceivers_Type = Integer32
_CmcIIINumberOfSmtpReceivers_Object = MibScalar
cmcIIINumberOfSmtpReceivers = _CmcIIINumberOfSmtpReceivers_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 9),
    _CmcIIINumberOfSmtpReceivers_Type()
)
cmcIIINumberOfSmtpReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfSmtpReceivers.setStatus("current")
_CmcIIISmtpReceiverTable_Object = MibTable
cmcIIISmtpReceiverTable = _CmcIIISmtpReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 10)
)
if mibBuilder.loadTexts:
    cmcIIISmtpReceiverTable.setStatus("current")
_CmcIIISmtpReceiverEntry_Object = MibTableRow
cmcIIISmtpReceiverEntry = _CmcIIISmtpReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 10, 1)
)
cmcIIISmtpReceiverEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIISmtpReceiverIndex"),
)
if mibBuilder.loadTexts:
    cmcIIISmtpReceiverEntry.setStatus("current")


class _CmcIIISmtpReceiverIndex_Type(Unsigned32):
    """Custom type cmcIIISmtpReceiverIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIISmtpReceiverIndex_Type.__name__ = "Unsigned32"
_CmcIIISmtpReceiverIndex_Object = MibTableColumn
cmcIIISmtpReceiverIndex = _CmcIIISmtpReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 10, 1, 1),
    _CmcIIISmtpReceiverIndex_Type()
)
cmcIIISmtpReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIISmtpReceiverIndex.setStatus("current")


class _CmcIIISmtpReceiverStatus_Type(Integer32):
    """Custom type cmcIIISmtpReceiverStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIISmtpReceiverStatus_Type.__name__ = "Integer32"
_CmcIIISmtpReceiverStatus_Object = MibTableColumn
cmcIIISmtpReceiverStatus = _CmcIIISmtpReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 10, 1, 2),
    _CmcIIISmtpReceiverStatus_Type()
)
cmcIIISmtpReceiverStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmtpReceiverStatus.setStatus("current")


class _CmcIIISmtpReceiverAddress_Type(DisplayString):
    """Custom type cmcIIISmtpReceiverAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CmcIIISmtpReceiverAddress_Type.__name__ = "DisplayString"
_CmcIIISmtpReceiverAddress_Object = MibTableColumn
cmcIIISmtpReceiverAddress = _CmcIIISmtpReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 5, 10, 1, 3),
    _CmcIIISmtpReceiverAddress_Type()
)
cmcIIISmtpReceiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmtpReceiverAddress.setStatus("current")
_CmcIIISetupSMS_ObjectIdentity = ObjectIdentity
cmcIIISetupSMS = _CmcIIISetupSMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6)
)


class _CmcIIISmsStatus_Type(Integer32):
    """Custom type cmcIIISmsStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIISmsStatus_Type.__name__ = "Integer32"
_CmcIIISmsStatus_Object = MibScalar
cmcIIISmsStatus = _CmcIIISmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 1),
    _CmcIIISmsStatus_Type()
)
cmcIIISmsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmsStatus.setStatus("current")


class _CmcIIISmsPIN_Type(DisplayString):
    """Custom type cmcIIISmsPIN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmcIIISmsPIN_Type.__name__ = "DisplayString"
_CmcIIISmsPIN_Object = MibScalar
cmcIIISmsPIN = _CmcIIISmsPIN_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 2),
    _CmcIIISmsPIN_Type()
)
cmcIIISmsPIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmsPIN.setStatus("current")


class _CmcIIISmsService_Type(DisplayString):
    """Custom type cmcIIISmsService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CmcIIISmsService_Type.__name__ = "DisplayString"
_CmcIIISmsService_Object = MibScalar
cmcIIISmsService = _CmcIIISmsService_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 3),
    _CmcIIISmsService_Type()
)
cmcIIISmsService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmsService.setStatus("current")


class _CmcIIISmsMSN_Type(DisplayString):
    """Custom type cmcIIISmsMSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CmcIIISmsMSN_Type.__name__ = "DisplayString"
_CmcIIISmsMSN_Object = MibScalar
cmcIIISmsMSN = _CmcIIISmsMSN_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 4),
    _CmcIIISmsMSN_Type()
)
cmcIIISmsMSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmsMSN.setStatus("current")


class _CmcIIISmsPreDial_Type(DisplayString):
    """Custom type cmcIIISmsPreDial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CmcIIISmsPreDial_Type.__name__ = "DisplayString"
_CmcIIISmsPreDial_Object = MibScalar
cmcIIISmsPreDial = _CmcIIISmsPreDial_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 5),
    _CmcIIISmsPreDial_Type()
)
cmcIIISmsPreDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmsPreDial.setStatus("current")
_CmcIIINumberOfSmsReceivers_Type = Integer32
_CmcIIINumberOfSmsReceivers_Object = MibScalar
cmcIIINumberOfSmsReceivers = _CmcIIINumberOfSmsReceivers_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 6),
    _CmcIIINumberOfSmsReceivers_Type()
)
cmcIIINumberOfSmsReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfSmsReceivers.setStatus("current")
_CmcIIISmsReceiverTable_Object = MibTable
cmcIIISmsReceiverTable = _CmcIIISmsReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 7)
)
if mibBuilder.loadTexts:
    cmcIIISmsReceiverTable.setStatus("current")
_CmcIIISmsReceiverEntry_Object = MibTableRow
cmcIIISmsReceiverEntry = _CmcIIISmsReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 7, 1)
)
cmcIIISmsReceiverEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIISmsReceiverIndex"),
)
if mibBuilder.loadTexts:
    cmcIIISmsReceiverEntry.setStatus("current")


class _CmcIIISmsReceiverIndex_Type(Unsigned32):
    """Custom type cmcIIISmsReceiverIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIISmsReceiverIndex_Type.__name__ = "Unsigned32"
_CmcIIISmsReceiverIndex_Object = MibTableColumn
cmcIIISmsReceiverIndex = _CmcIIISmsReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 7, 1, 1),
    _CmcIIISmsReceiverIndex_Type()
)
cmcIIISmsReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIISmsReceiverIndex.setStatus("current")


class _CmcIIISmsReceiverStatus_Type(Integer32):
    """Custom type cmcIIISmsReceiverStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIISmsReceiverStatus_Type.__name__ = "Integer32"
_CmcIIISmsReceiverStatus_Object = MibTableColumn
cmcIIISmsReceiverStatus = _CmcIIISmsReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 7, 1, 2),
    _CmcIIISmsReceiverStatus_Type()
)
cmcIIISmsReceiverStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmsReceiverStatus.setStatus("current")


class _CmcIIISmsReceiverNumber_Type(DisplayString):
    """Custom type cmcIIISmsReceiverNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CmcIIISmsReceiverNumber_Type.__name__ = "DisplayString"
_CmcIIISmsReceiverNumber_Object = MibTableColumn
cmcIIISmsReceiverNumber = _CmcIIISmsReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 6, 7, 1, 3),
    _CmcIIISmsReceiverNumber_Type()
)
cmcIIISmsReceiverNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmsReceiverNumber.setStatus("current")
_CmcIIISetupSysLog_ObjectIdentity = ObjectIdentity
cmcIIISetupSysLog = _CmcIIISetupSysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 7)
)


class _CmcIIISysLogStatus_Type(Integer32):
    """Custom type cmcIIISysLogStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIISysLogStatus_Type.__name__ = "Integer32"
_CmcIIISysLogStatus_Object = MibScalar
cmcIIISysLogStatus = _CmcIIISysLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 7, 1),
    _CmcIIISysLogStatus_Type()
)
cmcIIISysLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISysLogStatus.setStatus("current")


class _CmcIIISysLogFacility_Type(Integer32):
    """Custom type cmcIIISysLogFacility based on Integer32"""
    defaultValue = 1

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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_CmcIIISysLogFacility_Type.__name__ = "Integer32"
_CmcIIISysLogFacility_Object = MibScalar
cmcIIISysLogFacility = _CmcIIISysLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 7, 2),
    _CmcIIISysLogFacility_Type()
)
cmcIIISysLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISysLogFacility.setStatus("current")


class _CmcIIISysLogServer1_Type(DisplayString):
    """Custom type cmcIIISysLogServer1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIISysLogServer1_Type.__name__ = "DisplayString"
_CmcIIISysLogServer1_Object = MibScalar
cmcIIISysLogServer1 = _CmcIIISysLogServer1_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 7, 3),
    _CmcIIISysLogServer1_Type()
)
cmcIIISysLogServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISysLogServer1.setStatus("current")


class _CmcIIISysLogServer2_Type(DisplayString):
    """Custom type cmcIIISysLogServer2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIISysLogServer2_Type.__name__ = "DisplayString"
_CmcIIISysLogServer2_Object = MibScalar
cmcIIISysLogServer2 = _CmcIIISysLogServer2_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 7, 4),
    _CmcIIISysLogServer2_Type()
)
cmcIIISysLogServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISysLogServer2.setStatus("current")
_CmcIIISetupNTP_ObjectIdentity = ObjectIdentity
cmcIIISetupNTP = _CmcIIISetupNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 8)
)


class _CmcIIINtpStatus_Type(Integer32):
    """Custom type cmcIIINtpStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIINtpStatus_Type.__name__ = "Integer32"
_CmcIIINtpStatus_Object = MibScalar
cmcIIINtpStatus = _CmcIIINtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 8, 1),
    _CmcIIINtpStatus_Type()
)
cmcIIINtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIINtpStatus.setStatus("current")


class _CmcIIINtpTimeZone_Type(Integer32):
    """Custom type cmcIIINtpTimeZone based on Integer32"""
    defaultValue = 27

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 74),
    )


_CmcIIINtpTimeZone_Type.__name__ = "Integer32"
_CmcIIINtpTimeZone_Object = MibScalar
cmcIIINtpTimeZone = _CmcIIINtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 8, 2),
    _CmcIIINtpTimeZone_Type()
)
cmcIIINtpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIINtpTimeZone.setStatus("current")


class _CmcIIINtpServer1_Type(DisplayString):
    """Custom type cmcIIINtpServer1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIINtpServer1_Type.__name__ = "DisplayString"
_CmcIIINtpServer1_Object = MibScalar
cmcIIINtpServer1 = _CmcIIINtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 8, 3),
    _CmcIIINtpServer1_Type()
)
cmcIIINtpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIINtpServer1.setStatus("current")


class _CmcIIINtpServer2_Type(DisplayString):
    """Custom type cmcIIINtpServer2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIINtpServer2_Type.__name__ = "DisplayString"
_CmcIIINtpServer2_Object = MibScalar
cmcIIINtpServer2 = _CmcIIINtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 8, 4),
    _CmcIIINtpServer2_Type()
)
cmcIIINtpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIINtpServer2.setStatus("current")
_CmcIIISetupLDAP_ObjectIdentity = ObjectIdentity
cmcIIISetupLDAP = _CmcIIISetupLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9)
)


class _CmcIIILdapStatus_Type(Integer32):
    """Custom type cmcIIILdapStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIILdapStatus_Type.__name__ = "Integer32"
_CmcIIILdapStatus_Object = MibScalar
cmcIIILdapStatus = _CmcIIILdapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9, 1),
    _CmcIIILdapStatus_Type()
)
cmcIIILdapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILdapStatus.setStatus("current")


class _CmcIIILdapServer_Type(DisplayString):
    """Custom type cmcIIILdapServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIILdapServer_Type.__name__ = "DisplayString"
_CmcIIILdapServer_Object = MibScalar
cmcIIILdapServer = _CmcIIILdapServer_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9, 2),
    _CmcIIILdapServer_Type()
)
cmcIIILdapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILdapServer.setStatus("current")


class _CmcIIILdapBindDN_Type(DisplayString):
    """Custom type cmcIIILdapBindDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CmcIIILdapBindDN_Type.__name__ = "DisplayString"
_CmcIIILdapBindDN_Object = MibScalar
cmcIIILdapBindDN = _CmcIIILdapBindDN_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9, 3),
    _CmcIIILdapBindDN_Type()
)
cmcIIILdapBindDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILdapBindDN.setStatus("current")


class _CmcIIILdapBindPW_Type(DisplayString):
    """Custom type cmcIIILdapBindPW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIILdapBindPW_Type.__name__ = "DisplayString"
_CmcIIILdapBindPW_Object = MibScalar
cmcIIILdapBindPW = _CmcIIILdapBindPW_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9, 4),
    _CmcIIILdapBindPW_Type()
)
cmcIIILdapBindPW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILdapBindPW.setStatus("current")


class _CmcIIILdapUserBase_Type(DisplayString):
    """Custom type cmcIIILdapUserBase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIILdapUserBase_Type.__name__ = "DisplayString"
_CmcIIILdapUserBase_Object = MibScalar
cmcIIILdapUserBase = _CmcIIILdapUserBase_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9, 5),
    _CmcIIILdapUserBase_Type()
)
cmcIIILdapUserBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILdapUserBase.setStatus("current")


class _CmcIIILdapUserSearch_Type(DisplayString):
    """Custom type cmcIIILdapUserSearch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CmcIIILdapUserSearch_Type.__name__ = "DisplayString"
_CmcIIILdapUserSearch_Object = MibScalar
cmcIIILdapUserSearch = _CmcIIILdapUserSearch_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9, 6),
    _CmcIIILdapUserSearch_Type()
)
cmcIIILdapUserSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILdapUserSearch.setStatus("current")


class _CmcIIILdapUserAttrib_Type(DisplayString):
    """Custom type cmcIIILdapUserAttrib based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmcIIILdapUserAttrib_Type.__name__ = "DisplayString"
_CmcIIILdapUserAttrib_Object = MibScalar
cmcIIILdapUserAttrib = _CmcIIILdapUserAttrib_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9, 7),
    _CmcIIILdapUserAttrib_Type()
)
cmcIIILdapUserAttrib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILdapUserAttrib.setStatus("current")


class _CmcIIILdapGroupBase_Type(DisplayString):
    """Custom type cmcIIILdapGroupBase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIILdapGroupBase_Type.__name__ = "DisplayString"
_CmcIIILdapGroupBase_Object = MibScalar
cmcIIILdapGroupBase = _CmcIIILdapGroupBase_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9, 8),
    _CmcIIILdapGroupBase_Type()
)
cmcIIILdapGroupBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILdapGroupBase.setStatus("current")


class _CmcIIILdapGroupSearch_Type(DisplayString):
    """Custom type cmcIIILdapGroupSearch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CmcIIILdapGroupSearch_Type.__name__ = "DisplayString"
_CmcIIILdapGroupSearch_Object = MibScalar
cmcIIILdapGroupSearch = _CmcIIILdapGroupSearch_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9, 9),
    _CmcIIILdapGroupSearch_Type()
)
cmcIIILdapGroupSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILdapGroupSearch.setStatus("current")


class _CmcIIILdapGroupAttrib_Type(DisplayString):
    """Custom type cmcIIILdapGroupAttrib based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmcIIILdapGroupAttrib_Type.__name__ = "DisplayString"
_CmcIIILdapGroupAttrib_Object = MibScalar
cmcIIILdapGroupAttrib = _CmcIIILdapGroupAttrib_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 9, 10),
    _CmcIIILdapGroupAttrib_Type()
)
cmcIIILdapGroupAttrib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIILdapGroupAttrib.setStatus("current")
_CmcIIISetupShutdown_ObjectIdentity = ObjectIdentity
cmcIIISetupShutdown = _CmcIIISetupShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 10)
)
_CmcIIINumberOfShutdowns_Type = Integer32
_CmcIIINumberOfShutdowns_Object = MibScalar
cmcIIINumberOfShutdowns = _CmcIIINumberOfShutdowns_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 10, 1),
    _CmcIIINumberOfShutdowns_Type()
)
cmcIIINumberOfShutdowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfShutdowns.setStatus("current")
_CmcIIIShutdownTable_Object = MibTable
cmcIIIShutdownTable = _CmcIIIShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 10, 2)
)
if mibBuilder.loadTexts:
    cmcIIIShutdownTable.setStatus("current")
_CmcIIIShutdownEntry_Object = MibTableRow
cmcIIIShutdownEntry = _CmcIIIShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 10, 2, 1)
)
cmcIIIShutdownEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIShutdownIndex"),
)
if mibBuilder.loadTexts:
    cmcIIIShutdownEntry.setStatus("current")


class _CmcIIIShutdownIndex_Type(Unsigned32):
    """Custom type cmcIIIShutdownIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIShutdownIndex_Type.__name__ = "Unsigned32"
_CmcIIIShutdownIndex_Object = MibTableColumn
cmcIIIShutdownIndex = _CmcIIIShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 10, 2, 1, 1),
    _CmcIIIShutdownIndex_Type()
)
cmcIIIShutdownIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIShutdownIndex.setStatus("current")


class _CmcIIIShutdownServer_Type(DisplayString):
    """Custom type cmcIIIShutdownServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIIShutdownServer_Type.__name__ = "DisplayString"
_CmcIIIShutdownServer_Object = MibTableColumn
cmcIIIShutdownServer = _CmcIIIShutdownServer_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 10, 2, 1, 2),
    _CmcIIIShutdownServer_Type()
)
cmcIIIShutdownServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIShutdownServer.setStatus("current")


class _CmcIIIShutdownName_Type(DisplayString):
    """Custom type cmcIIIShutdownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmcIIIShutdownName_Type.__name__ = "DisplayString"
_CmcIIIShutdownName_Object = MibTableColumn
cmcIIIShutdownName = _CmcIIIShutdownName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 10, 2, 1, 3),
    _CmcIIIShutdownName_Type()
)
cmcIIIShutdownName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIShutdownName.setStatus("current")


class _CmcIIIShutdownPort_Type(Unsigned32):
    """Custom type cmcIIIShutdownPort based on Unsigned32"""
    defaultValue = 6003

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIShutdownPort_Type.__name__ = "Unsigned32"
_CmcIIIShutdownPort_Object = MibTableColumn
cmcIIIShutdownPort = _CmcIIIShutdownPort_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 10, 2, 1, 4),
    _CmcIIIShutdownPort_Type()
)
cmcIIIShutdownPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIShutdownPort.setStatus("current")


class _CmcIIIShutdownDelay_Type(Unsigned32):
    """Custom type cmcIIIShutdownDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CmcIIIShutdownDelay_Type.__name__ = "Unsigned32"
_CmcIIIShutdownDelay_Object = MibTableColumn
cmcIIIShutdownDelay = _CmcIIIShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 10, 2, 1, 5),
    _CmcIIIShutdownDelay_Type()
)
cmcIIIShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIShutdownDelay.setStatus("current")


class _CmcIIIShutdownEnabled_Type(Integer32):
    """Custom type cmcIIIShutdownEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIIShutdownEnabled_Type.__name__ = "Integer32"
_CmcIIIShutdownEnabled_Object = MibTableColumn
cmcIIIShutdownEnabled = _CmcIIIShutdownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 10, 2, 1, 6),
    _CmcIIIShutdownEnabled_Type()
)
cmcIIIShutdownEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIShutdownEnabled.setStatus("current")
_CmcIIISetupModbus_ObjectIdentity = ObjectIdentity
cmcIIISetupModbus = _CmcIIISetupModbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 11)
)


class _CmcIIIModbusStatus_Type(Integer32):
    """Custom type cmcIIIModbusStatus based on Integer32"""
    defaultValue = 2

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
        *(("readonly", 2),
          ("readwrite", 4),
          ("shutdown", 1),
          ("writeonly", 3))
    )


_CmcIIIModbusStatus_Type.__name__ = "Integer32"
_CmcIIIModbusStatus_Object = MibScalar
cmcIIIModbusStatus = _CmcIIIModbusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 11, 1),
    _CmcIIIModbusStatus_Type()
)
cmcIIIModbusStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIModbusStatus.setStatus("current")


class _CmcIIIModbusPort_Type(Unsigned32):
    """Custom type cmcIIIModbusPort based on Unsigned32"""
    defaultValue = 502

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIModbusPort_Type.__name__ = "Unsigned32"
_CmcIIIModbusPort_Object = MibScalar
cmcIIIModbusPort = _CmcIIIModbusPort_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 11, 2),
    _CmcIIIModbusPort_Type()
)
cmcIIIModbusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIModbusPort.setStatus("current")
_CmcIIINumberOfModbusSources_Type = Unsigned32
_CmcIIINumberOfModbusSources_Object = MibScalar
cmcIIINumberOfModbusSources = _CmcIIINumberOfModbusSources_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 11, 3),
    _CmcIIINumberOfModbusSources_Type()
)
cmcIIINumberOfModbusSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfModbusSources.setStatus("current")
_CmcIIIModbusTable_Object = MibTable
cmcIIIModbusTable = _CmcIIIModbusTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 11, 4)
)
if mibBuilder.loadTexts:
    cmcIIIModbusTable.setStatus("current")
_CmcIIIModbusEntry_Object = MibTableRow
cmcIIIModbusEntry = _CmcIIIModbusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 11, 4, 1)
)
cmcIIIModbusEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIModbusIndex"),
)
if mibBuilder.loadTexts:
    cmcIIIModbusEntry.setStatus("current")


class _CmcIIIModbusIndex_Type(Unsigned32):
    """Custom type cmcIIIModbusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIModbusIndex_Type.__name__ = "Unsigned32"
_CmcIIIModbusIndex_Object = MibTableColumn
cmcIIIModbusIndex = _CmcIIIModbusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 11, 4, 1, 1),
    _CmcIIIModbusIndex_Type()
)
cmcIIIModbusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIModbusIndex.setStatus("current")


class _CmcIIIModbusAccess_Type(Integer32):
    """Custom type cmcIIIModbusAccess based on Integer32"""
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
        *(("noaccess", 1),
          ("readonly", 2),
          ("readwrite", 4),
          ("writeonly", 3))
    )


_CmcIIIModbusAccess_Type.__name__ = "Integer32"
_CmcIIIModbusAccess_Object = MibTableColumn
cmcIIIModbusAccess = _CmcIIIModbusAccess_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 11, 4, 1, 2),
    _CmcIIIModbusAccess_Type()
)
cmcIIIModbusAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIModbusAccess.setStatus("current")


class _CmcIIIModbusSource_Type(DisplayString):
    """Custom type cmcIIIModbusSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIIModbusSource_Type.__name__ = "DisplayString"
_CmcIIIModbusSource_Object = MibTableColumn
cmcIIIModbusSource = _CmcIIIModbusSource_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 11, 4, 1, 3),
    _CmcIIIModbusSource_Type()
)
cmcIIIModbusSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIModbusSource.setStatus("current")
_CmcIIISetupRadius_ObjectIdentity = ObjectIdentity
cmcIIISetupRadius = _CmcIIISetupRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 12)
)


class _CmcIIIRadiusStatus_Type(Integer32):
    """Custom type cmcIIIRadiusStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIIRadiusStatus_Type.__name__ = "Integer32"
_CmcIIIRadiusStatus_Object = MibScalar
cmcIIIRadiusStatus = _CmcIIIRadiusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 12, 1),
    _CmcIIIRadiusStatus_Type()
)
cmcIIIRadiusStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIRadiusStatus.setStatus("current")


class _CmcIIIRadiusServer_Type(DisplayString):
    """Custom type cmcIIIRadiusServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIIRadiusServer_Type.__name__ = "DisplayString"
_CmcIIIRadiusServer_Object = MibScalar
cmcIIIRadiusServer = _CmcIIIRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 12, 2),
    _CmcIIIRadiusServer_Type()
)
cmcIIIRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIRadiusServer.setStatus("current")


class _CmcIIIRadiusPort_Type(Unsigned32):
    """Custom type cmcIIIRadiusPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIRadiusPort_Type.__name__ = "Unsigned32"
_CmcIIIRadiusPort_Object = MibScalar
cmcIIIRadiusPort = _CmcIIIRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 12, 3),
    _CmcIIIRadiusPort_Type()
)
cmcIIIRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIRadiusPort.setStatus("current")


class _CmcIIIRadiusPassword_Type(DisplayString):
    """Custom type cmcIIIRadiusPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmcIIIRadiusPassword_Type.__name__ = "DisplayString"
_CmcIIIRadiusPassword_Object = MibScalar
cmcIIIRadiusPassword = _CmcIIIRadiusPassword_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 12, 4),
    _CmcIIIRadiusPassword_Type()
)
cmcIIIRadiusPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIRadiusPassword.setStatus("current")


class _CmcIIIRadiusGroupMode_Type(Integer32):
    """Custom type cmcIIIRadiusGroupMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byAttribute", 2),
          ("manual", 1))
    )


_CmcIIIRadiusGroupMode_Type.__name__ = "Integer32"
_CmcIIIRadiusGroupMode_Object = MibScalar
cmcIIIRadiusGroupMode = _CmcIIIRadiusGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 12, 5),
    _CmcIIIRadiusGroupMode_Type()
)
cmcIIIRadiusGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIRadiusGroupMode.setStatus("current")


class _CmcIIIRadiusGroupId_Type(Unsigned32):
    """Custom type cmcIIIRadiusGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CmcIIIRadiusGroupId_Type.__name__ = "Unsigned32"
_CmcIIIRadiusGroupId_Object = MibScalar
cmcIIIRadiusGroupId = _CmcIIIRadiusGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 12, 6),
    _CmcIIIRadiusGroupId_Type()
)
cmcIIIRadiusGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIRadiusGroupId.setStatus("current")


class _CmcIIIRadiusAuth_Type(Integer32):
    """Custom type cmcIIIRadiusAuth based on Integer32"""
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
        *(("auto", 1),
          ("chap", 3),
          ("md5", 5),
          ("mschap", 4),
          ("pap", 2))
    )


_CmcIIIRadiusAuth_Type.__name__ = "Integer32"
_CmcIIIRadiusAuth_Object = MibScalar
cmcIIIRadiusAuth = _CmcIIIRadiusAuth_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 12, 7),
    _CmcIIIRadiusAuth_Type()
)
cmcIIIRadiusAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIRadiusAuth.setStatus("current")
_CmcIIISetupWebCam_ObjectIdentity = ObjectIdentity
cmcIIISetupWebCam = _CmcIIISetupWebCam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 13)
)


class _CmcIIIWebCamStatus_Type(Integer32):
    """Custom type cmcIIIWebCamStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcIIIWebCamStatus_Type.__name__ = "Integer32"
_CmcIIIWebCamStatus_Object = MibScalar
cmcIIIWebCamStatus = _CmcIIIWebCamStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 13, 1),
    _CmcIIIWebCamStatus_Type()
)
cmcIIIWebCamStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIWebCamStatus.setStatus("current")


class _CmcIIIWebCamServer_Type(DisplayString):
    """Custom type cmcIIIWebCamServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIIWebCamServer_Type.__name__ = "DisplayString"
_CmcIIIWebCamServer_Object = MibScalar
cmcIIIWebCamServer = _CmcIIIWebCamServer_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 13, 2),
    _CmcIIIWebCamServer_Type()
)
cmcIIIWebCamServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIWebCamServer.setStatus("current")


class _CmcIIIWebCamUsername_Type(DisplayString):
    """Custom type cmcIIIWebCamUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CmcIIIWebCamUsername_Type.__name__ = "DisplayString"
_CmcIIIWebCamUsername_Object = MibScalar
cmcIIIWebCamUsername = _CmcIIIWebCamUsername_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 13, 3),
    _CmcIIIWebCamUsername_Type()
)
cmcIIIWebCamUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIWebCamUsername.setStatus("current")


class _CmcIIIWebCamPassword_Type(DisplayString):
    """Custom type cmcIIIWebCamPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmcIIIWebCamPassword_Type.__name__ = "DisplayString"
_CmcIIIWebCamPassword_Object = MibScalar
cmcIIIWebCamPassword = _CmcIIIWebCamPassword_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 13, 4),
    _CmcIIIWebCamPassword_Type()
)
cmcIIIWebCamPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIWebCamPassword.setStatus("current")


class _CmcIIIWebCamIntervall_Type(Unsigned32):
    """Custom type cmcIIIWebCamIntervall based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_CmcIIIWebCamIntervall_Type.__name__ = "Unsigned32"
_CmcIIIWebCamIntervall_Object = MibScalar
cmcIIIWebCamIntervall = _CmcIIIWebCamIntervall_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 13, 5),
    _CmcIIIWebCamIntervall_Type()
)
cmcIIIWebCamIntervall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIWebCamIntervall.setStatus("current")


class _CmcIIIWebCamNumberofImages_Type(Unsigned32):
    """Custom type cmcIIIWebCamNumberofImages based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CmcIIIWebCamNumberofImages_Type.__name__ = "Unsigned32"
_CmcIIIWebCamNumberofImages_Object = MibScalar
cmcIIIWebCamNumberofImages = _CmcIIIWebCamNumberofImages_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 13, 6),
    _CmcIIIWebCamNumberofImages_Type()
)
cmcIIIWebCamNumberofImages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIWebCamNumberofImages.setStatus("current")


class _CmcIIIWebCamDestination_Type(Integer32):
    """Custom type cmcIIIWebCamDestination based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sd", 2),
          ("usb", 1))
    )


_CmcIIIWebCamDestination_Type.__name__ = "Integer32"
_CmcIIIWebCamDestination_Object = MibScalar
cmcIIIWebCamDestination = _CmcIIIWebCamDestination_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 3, 13, 7),
    _CmcIIIWebCamDestination_Type()
)
cmcIIIWebCamDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIWebCamDestination.setStatus("current")
_CmcIIIDevice_ObjectIdentity = ObjectIdentity
cmcIIIDevice = _CmcIIIDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4)
)
_CmcIIIDevs_ObjectIdentity = ObjectIdentity
cmcIIIDevs = _CmcIIIDevs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1)
)
_CmcIIIDevInfo_ObjectIdentity = ObjectIdentity
cmcIIIDevInfo = _CmcIIIDevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 1)
)


class _CmcIIIOverallDevStatus_Type(Integer32):
    """Custom type cmcIIIOverallDevStatus based on Integer32"""
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
        *(("alarm", 3),
          ("changed", 6),
          ("detected", 4),
          ("lost", 5),
          ("ok", 1),
          ("update", 7),
          ("warning", 2))
    )


_CmcIIIOverallDevStatus_Type.__name__ = "Integer32"
_CmcIIIOverallDevStatus_Object = MibScalar
cmcIIIOverallDevStatus = _CmcIIIOverallDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 1, 1),
    _CmcIIIOverallDevStatus_Type()
)
cmcIIIOverallDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIOverallDevStatus.setStatus("current")
_CmcIIINumberOfDevs_Type = Integer32
_CmcIIINumberOfDevs_Object = MibScalar
cmcIIINumberOfDevs = _CmcIIINumberOfDevs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 1, 2),
    _CmcIIINumberOfDevs_Type()
)
cmcIIINumberOfDevs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfDevs.setStatus("current")
_CmcIIILastChangeOverallDevStatus_Type = Unsigned32
_CmcIIILastChangeOverallDevStatus_Object = MibScalar
cmcIIILastChangeOverallDevStatus = _CmcIIILastChangeOverallDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 1, 3),
    _CmcIIILastChangeOverallDevStatus_Type()
)
cmcIIILastChangeOverallDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeOverallDevStatus.setStatus("current")
_CmcIIILastChangeNumberOfDevs_Type = Unsigned32
_CmcIIILastChangeNumberOfDevs_Object = MibScalar
cmcIIILastChangeNumberOfDevs = _CmcIIILastChangeNumberOfDevs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 1, 4),
    _CmcIIILastChangeNumberOfDevs_Type()
)
cmcIIILastChangeNumberOfDevs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeNumberOfDevs.setStatus("current")
_CmcIIILastChangeDevSettings_Type = Unsigned32
_CmcIIILastChangeDevSettings_Object = MibScalar
cmcIIILastChangeDevSettings = _CmcIIILastChangeDevSettings_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 1, 5),
    _CmcIIILastChangeDevSettings_Type()
)
cmcIIILastChangeDevSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeDevSettings.setStatus("current")
_CmcIIILastChangeDevs_Type = Unsigned32
_CmcIIILastChangeDevs_Object = MibScalar
cmcIIILastChangeDevs = _CmcIIILastChangeDevs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 1, 6),
    _CmcIIILastChangeDevs_Type()
)
cmcIIILastChangeDevs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeDevs.setStatus("current")
_CmcIIIDevTable_Object = MibTable
cmcIIIDevTable = _CmcIIIDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cmcIIIDevTable.setStatus("current")
_CmcIIIDevEntry_Object = MibTableRow
cmcIIIDevEntry = _CmcIIIDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1)
)
cmcIIIDevEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIDevIndex"),
)
if mibBuilder.loadTexts:
    cmcIIIDevEntry.setStatus("current")


class _CmcIIIDevIndex_Type(Unsigned32):
    """Custom type cmcIIIDevIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_CmcIIIDevIndex_Type.__name__ = "Unsigned32"
_CmcIIIDevIndex_Object = MibTableColumn
cmcIIIDevIndex = _CmcIIIDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 1),
    _CmcIIIDevIndex_Type()
)
cmcIIIDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIDevIndex.setStatus("current")


class _CmcIIIDevName_Type(DisplayString):
    """Custom type cmcIIIDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CmcIIIDevName_Type.__name__ = "DisplayString"
_CmcIIIDevName_Object = MibTableColumn
cmcIIIDevName = _CmcIIIDevName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 2),
    _CmcIIIDevName_Type()
)
cmcIIIDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevName.setStatus("current")


class _CmcIIIDevAlias_Type(DisplayString):
    """Custom type cmcIIIDevAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIIDevAlias_Type.__name__ = "DisplayString"
_CmcIIIDevAlias_Object = MibTableColumn
cmcIIIDevAlias = _CmcIIIDevAlias_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 3),
    _CmcIIIDevAlias_Type()
)
cmcIIIDevAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDevAlias.setStatus("current")
_CmcIIIDevType_Type = ObjectIdentifier
_CmcIIIDevType_Object = MibTableColumn
cmcIIIDevType = _CmcIIIDevType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 4),
    _CmcIIIDevType_Type()
)
cmcIIIDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevType.setStatus("current")
_CmcIIIDevNodeID_Type = Integer32
_CmcIIIDevNodeID_Object = MibTableColumn
cmcIIIDevNodeID = _CmcIIIDevNodeID_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 5),
    _CmcIIIDevNodeID_Type()
)
cmcIIIDevNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevNodeID.setStatus("current")


class _CmcIIIDevStatus_Type(Integer32):
    """Custom type cmcIIIDevStatus based on Integer32"""
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
        *(("changed", 5),
          ("detect", 3),
          ("error", 6),
          ("fwUpdate", 7),
          ("fwUpdateRun", 8),
          ("lost", 4),
          ("notAvail", 1),
          ("ok", 2))
    )


_CmcIIIDevStatus_Type.__name__ = "Integer32"
_CmcIIIDevStatus_Object = MibTableColumn
cmcIIIDevStatus = _CmcIIIDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 6),
    _CmcIIIDevStatus_Type()
)
cmcIIIDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevStatus.setStatus("current")


class _CmcIIIDevArtNr_Type(DisplayString):
    """Custom type cmcIIIDevArtNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmcIIIDevArtNr_Type.__name__ = "DisplayString"
_CmcIIIDevArtNr_Object = MibTableColumn
cmcIIIDevArtNr = _CmcIIIDevArtNr_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 7),
    _CmcIIIDevArtNr_Type()
)
cmcIIIDevArtNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevArtNr.setStatus("current")


class _CmcIIIDevLocation_Type(DisplayString):
    """Custom type cmcIIIDevLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIIDevLocation_Type.__name__ = "DisplayString"
_CmcIIIDevLocation_Object = MibTableColumn
cmcIIIDevLocation = _CmcIIIDevLocation_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 8),
    _CmcIIIDevLocation_Type()
)
cmcIIIDevLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDevLocation.setStatus("current")


class _CmcIIIDevBus_Type(Integer32):
    """Custom type cmcIIIDevBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("canBus1", 1),
          ("canBus2", 2),
          ("virtual", 3))
    )


_CmcIIIDevBus_Type.__name__ = "Integer32"
_CmcIIIDevBus_Object = MibTableColumn
cmcIIIDevBus = _CmcIIIDevBus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 9),
    _CmcIIIDevBus_Type()
)
cmcIIIDevBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevBus.setStatus("current")
_CmcIIIDevPos_Type = Integer32
_CmcIIIDevPos_Object = MibTableColumn
cmcIIIDevPos = _CmcIIIDevPos_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 10),
    _CmcIIIDevPos_Type()
)
cmcIIIDevPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevPos.setStatus("current")


class _CmcIIIDevFW_Type(DisplayString):
    """Custom type cmcIIIDevFW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CmcIIIDevFW_Type.__name__ = "DisplayString"
_CmcIIIDevFW_Object = MibTableColumn
cmcIIIDevFW = _CmcIIIDevFW_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 11),
    _CmcIIIDevFW_Type()
)
cmcIIIDevFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevFW.setStatus("current")


class _CmcIIIDevHW_Type(DisplayString):
    """Custom type cmcIIIDevHW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CmcIIIDevHW_Type.__name__ = "DisplayString"
_CmcIIIDevHW_Object = MibTableColumn
cmcIIIDevHW = _CmcIIIDevHW_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 12),
    _CmcIIIDevHW_Type()
)
cmcIIIDevHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevHW.setStatus("current")


class _CmcIIIDevSerial_Type(DisplayString):
    """Custom type cmcIIIDevSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CmcIIIDevSerial_Type.__name__ = "DisplayString"
_CmcIIIDevSerial_Object = MibTableColumn
cmcIIIDevSerial = _CmcIIIDevSerial_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 13),
    _CmcIIIDevSerial_Type()
)
cmcIIIDevSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevSerial.setStatus("current")


class _CmcIIIDevProductWeek_Type(DisplayString):
    """Custom type cmcIIIDevProductWeek based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CmcIIIDevProductWeek_Type.__name__ = "DisplayString"
_CmcIIIDevProductWeek_Object = MibTableColumn
cmcIIIDevProductWeek = _CmcIIIDevProductWeek_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 14),
    _CmcIIIDevProductWeek_Type()
)
cmcIIIDevProductWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevProductWeek.setStatus("current")
_CmcIIIDevLastChange_Type = Unsigned32
_CmcIIIDevLastChange_Object = MibTableColumn
cmcIIIDevLastChange = _CmcIIIDevLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 15),
    _CmcIIIDevLastChange_Type()
)
cmcIIIDevLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevLastChange.setStatus("current")


class _CmcIIIDevURL_Type(DisplayString):
    """Custom type cmcIIIDevURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CmcIIIDevURL_Type.__name__ = "DisplayString"
_CmcIIIDevURL_Object = MibTableColumn
cmcIIIDevURL = _CmcIIIDevURL_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 16),
    _CmcIIIDevURL_Type()
)
cmcIIIDevURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevURL.setStatus("current")
_CmcIIIDevNumberOfVars_Type = Integer32
_CmcIIIDevNumberOfVars_Object = MibTableColumn
cmcIIIDevNumberOfVars = _CmcIIIDevNumberOfVars_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 17),
    _CmcIIIDevNumberOfVars_Type()
)
cmcIIIDevNumberOfVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevNumberOfVars.setStatus("current")
_CmcIIIDevNumberOfMsgs_Type = Integer32
_CmcIIIDevNumberOfMsgs_Object = MibTableColumn
cmcIIIDevNumberOfMsgs = _CmcIIIDevNumberOfMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 18),
    _CmcIIIDevNumberOfMsgs_Type()
)
cmcIIIDevNumberOfMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevNumberOfMsgs.setStatus("current")


class _CmcIIIDevStatusText_Type(DisplayString):
    """Custom type cmcIIIDevStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_CmcIIIDevStatusText_Type.__name__ = "DisplayString"
_CmcIIIDevStatusText_Object = MibTableColumn
cmcIIIDevStatusText = _CmcIIIDevStatusText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 19),
    _CmcIIIDevStatusText_Type()
)
cmcIIIDevStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevStatusText.setStatus("current")
_CmcIIIDevCurrentMinConsumption_Type = Integer32
_CmcIIIDevCurrentMinConsumption_Object = MibTableColumn
cmcIIIDevCurrentMinConsumption = _CmcIIIDevCurrentMinConsumption_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 20),
    _CmcIIIDevCurrentMinConsumption_Type()
)
cmcIIIDevCurrentMinConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevCurrentMinConsumption.setStatus("current")
_CmcIIIDevCurrentMaxConsumption_Type = Integer32
_CmcIIIDevCurrentMaxConsumption_Object = MibTableColumn
cmcIIIDevCurrentMaxConsumption = _CmcIIIDevCurrentMaxConsumption_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 21),
    _CmcIIIDevCurrentMaxConsumption_Type()
)
cmcIIIDevCurrentMaxConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevCurrentMaxConsumption.setStatus("current")
_CmcIIIDevEntPhysicalIndex_Type = Integer32
_CmcIIIDevEntPhysicalIndex_Object = MibTableColumn
cmcIIIDevEntPhysicalIndex = _CmcIIIDevEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 22),
    _CmcIIIDevEntPhysicalIndex_Type()
)
cmcIIIDevEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevEntPhysicalIndex.setStatus("current")


class _CmcIIIDevAssembly_Type(DisplayString):
    """Custom type cmcIIIDevAssembly based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CmcIIIDevAssembly_Type.__name__ = "DisplayString"
_CmcIIIDevAssembly_Object = MibTableColumn
cmcIIIDevAssembly = _CmcIIIDevAssembly_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 1, 2, 1, 23),
    _CmcIIIDevAssembly_Type()
)
cmcIIIDevAssembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDevAssembly.setStatus("current")
_CmcIIIVars_ObjectIdentity = ObjectIdentity
cmcIIIVars = _CmcIIIVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2)
)
_CmcIIIVarInfo_ObjectIdentity = ObjectIdentity
cmcIIIVarInfo = _CmcIIIVarInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 1)
)
_CmcIIINumberOfVars_Type = Integer32
_CmcIIINumberOfVars_Object = MibScalar
cmcIIINumberOfVars = _CmcIIINumberOfVars_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 1, 1),
    _CmcIIINumberOfVars_Type()
)
cmcIIINumberOfVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfVars.setStatus("current")
_CmcIIILastChangeNumberOfVars_Type = Unsigned32
_CmcIIILastChangeNumberOfVars_Object = MibScalar
cmcIIILastChangeNumberOfVars = _CmcIIILastChangeNumberOfVars_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 1, 2),
    _CmcIIILastChangeNumberOfVars_Type()
)
cmcIIILastChangeNumberOfVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeNumberOfVars.setStatus("current")
_CmcIIILastChangeVarSettings_Type = Unsigned32
_CmcIIILastChangeVarSettings_Object = MibScalar
cmcIIILastChangeVarSettings = _CmcIIILastChangeVarSettings_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 1, 3),
    _CmcIIILastChangeVarSettings_Type()
)
cmcIIILastChangeVarSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeVarSettings.setStatus("current")
_CmcIIILastChangeVars_Type = Unsigned32
_CmcIIILastChangeVars_Object = MibScalar
cmcIIILastChangeVars = _CmcIIILastChangeVars_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 1, 4),
    _CmcIIILastChangeVars_Type()
)
cmcIIILastChangeVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeVars.setStatus("current")


class _CmcIIIVarByQualityHide_Type(Bits):
    """Custom type cmcIIIVarByQualityHide based on Bits"""
    defaultBinValue = "001"

    namedValues = NamedValues(
        *(("alarm", 4),
          ("alarmNoValue", 24),
          ("info", 5),
          ("infoNoValue", 25),
          ("notInUse", 0),
          ("ok", 2),
          ("okNoValue", 22),
          ("undefined", 1),
          ("undefinedNoValue", 21),
          ("warning", 3),
          ("warningNoValue", 23))
    )

_CmcIIIVarByQualityHide_Type.__name__ = "Bits"
_CmcIIIVarByQualityHide_Object = MibScalar
cmcIIIVarByQualityHide = _CmcIIIVarByQualityHide_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 1, 5),
    _CmcIIIVarByQualityHide_Type()
)
cmcIIIVarByQualityHide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIVarByQualityHide.setStatus("current")


class _CmcIIIDynUpdateRate_Type(Unsigned32):
    """Custom type cmcIIIDynUpdateRate based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_CmcIIIDynUpdateRate_Type.__name__ = "Unsigned32"
_CmcIIIDynUpdateRate_Object = MibScalar
cmcIIIDynUpdateRate = _CmcIIIDynUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 1, 6),
    _CmcIIIDynUpdateRate_Type()
)
cmcIIIDynUpdateRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDynUpdateRate.setStatus("current")


class _CmcIIIDynUpdateHistory_Type(Unsigned32):
    """Custom type cmcIIIDynUpdateHistory based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 2419200),
    )


_CmcIIIDynUpdateHistory_Type.__name__ = "Unsigned32"
_CmcIIIDynUpdateHistory_Object = MibScalar
cmcIIIDynUpdateHistory = _CmcIIIDynUpdateHistory_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 1, 7),
    _CmcIIIDynUpdateHistory_Type()
)
cmcIIIDynUpdateHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDynUpdateHistory.setStatus("current")
_CmcIIIVarTable_Object = MibTable
cmcIIIVarTable = _CmcIIIVarTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2)
)
if mibBuilder.loadTexts:
    cmcIIIVarTable.setStatus("current")
_CmcIIIVarEntry_Object = MibTableRow
cmcIIIVarEntry = _CmcIIIVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1)
)
cmcIIIVarEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarDeviceIndex"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarIndex"),
)
if mibBuilder.loadTexts:
    cmcIIIVarEntry.setStatus("current")


class _CmcIIIVarDeviceIndex_Type(Unsigned32):
    """Custom type cmcIIIVarDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIVarDeviceIndex_Type.__name__ = "Unsigned32"
_CmcIIIVarDeviceIndex_Object = MibTableColumn
cmcIIIVarDeviceIndex = _CmcIIIVarDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 1),
    _CmcIIIVarDeviceIndex_Type()
)
cmcIIIVarDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarDeviceIndex.setStatus("current")


class _CmcIIIVarIndex_Type(Unsigned32):
    """Custom type cmcIIIVarIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIVarIndex_Type.__name__ = "Unsigned32"
_CmcIIIVarIndex_Object = MibTableColumn
cmcIIIVarIndex = _CmcIIIVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 2),
    _CmcIIIVarIndex_Type()
)
cmcIIIVarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarIndex.setStatus("current")


class _CmcIIIVarName_Type(DisplayString):
    """Custom type cmcIIIVarName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CmcIIIVarName_Type.__name__ = "DisplayString"
_CmcIIIVarName_Object = MibTableColumn
cmcIIIVarName = _CmcIIIVarName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 3),
    _CmcIIIVarName_Type()
)
cmcIIIVarName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarName.setStatus("current")


class _CmcIIIVarType_Type(Integer32):
    """Custom type cmcIIIVarType based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
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
              34,
              35,
              36,
              40,
              41,
              42,
              43,
              44,
              45,
              50,
              51,
              52,
              53,
              54,
              55,
              80,
              81,
              82,
              83,
              84,
              85,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              100,
              110,
              111,
              112,
              113,
              120,
              121,
              122,
              123,
              124,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("accessLogic", 32),
          ("accessTime", 31),
          ("alarmDur", 11),
          ("assembly", 28),
          ("building", 131),
          ("category", 14),
          ("circuit", 42),
          ("command", 81),
          ("commandCtrl", 120),
          ("commandCtrlDP", 121),
          ("commandCtrlWdt", 122),
          ("commandEnum", 82),
          ("commandKeypad", 83),
          ("commandRack", 85),
          ("commandService", 84),
          ("config", 25),
          ("configLcpFcs", 27),
          ("configNum", 26),
          ("configPar", 13),
          ("configWiring", 29),
          ("connected", 96),
          ("connectedEnum", 97),
          ("currentMax", 55),
          ("currentMin", 54),
          ("customValue", 45),
          ("description", 1),
          ("devLocation", 53),
          ("devName", 52),
          ("fanAffect", 123),
          ("grouping", 100),
          ("gsmStatus", 95),
          ("hysteresis", 6),
          ("ignore", 254),
          ("illegal", 255),
          ("keycode", 80),
          ("level", 132),
          ("location", 130),
          ("logic", 15),
          ("logicEnum", 16),
          ("mountPos", 93),
          ("mountPosEnum", 94),
          ("numberOfRU", 137),
          ("offset", 18),
          ("operatingTime", 136),
          ("orderNr", 51),
          ("outdelayExec", 23),
          ("output", 20),
          ("outputEnum", 24),
          ("outputPWM", 40),
          ("outputaction", 22),
          ("outputdelay", 21),
          ("pin", 35),
          ("position", 33),
          ("positionEnum", 34),
          ("productDate", 50),
          ("rack", 135),
          ("rizoneArray", 43),
          ("room", 133),
          ("rotation", 41),
          ("row", 134),
          ("scaleEnd", 113),
          ("scaleStart", 112),
          ("scaleUnit", 111),
          ("scaleValue", 110),
          ("sensitivity", 30),
          ("sequence", 36),
          ("serialNumber", 92),
          ("setCntrl", 17),
          ("setHigh", 3),
          ("setLow", 5),
          ("setWarn", 4),
          ("setWarnLow", 9),
          ("socketType", 44),
          ("status", 7),
          ("statusEnum", 8),
          ("steps", 12),
          ("swVersion", 91),
          ("tagsChanged", 139),
          ("tagsQuit", 138),
          ("type", 19),
          ("uid", 140),
          ("unit", 10),
          ("unitType", 90),
          ("value", 2),
          ("waterAffect", 124))
    )


_CmcIIIVarType_Type.__name__ = "Integer32"
_CmcIIIVarType_Object = MibTableColumn
cmcIIIVarType = _CmcIIIVarType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 4),
    _CmcIIIVarType_Type()
)
cmcIIIVarType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarType.setStatus("current")


class _CmcIIIVarUnit_Type(DisplayString):
    """Custom type cmcIIIVarUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CmcIIIVarUnit_Type.__name__ = "DisplayString"
_CmcIIIVarUnit_Object = MibTableColumn
cmcIIIVarUnit = _CmcIIIVarUnit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 5),
    _CmcIIIVarUnit_Type()
)
cmcIIIVarUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarUnit.setStatus("current")


class _CmcIIIVarDataType_Type(Integer32):
    """Custom type cmcIIIVarDataType based on Integer32"""
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
        *(("enum", 4),
          ("int", 2),
          ("notAvail", 1),
          ("string", 3))
    )


_CmcIIIVarDataType_Type.__name__ = "Integer32"
_CmcIIIVarDataType_Object = MibTableColumn
cmcIIIVarDataType = _CmcIIIVarDataType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 6),
    _CmcIIIVarDataType_Type()
)
cmcIIIVarDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarDataType.setStatus("current")
_CmcIIIVarScale_Type = Integer32
_CmcIIIVarScale_Object = MibTableColumn
cmcIIIVarScale = _CmcIIIVarScale_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 7),
    _CmcIIIVarScale_Type()
)
cmcIIIVarScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarScale.setStatus("current")


class _CmcIIIVarConstraints_Type(DisplayString):
    """Custom type cmcIIIVarConstraints based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIIVarConstraints_Type.__name__ = "DisplayString"
_CmcIIIVarConstraints_Object = MibTableColumn
cmcIIIVarConstraints = _CmcIIIVarConstraints_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 8),
    _CmcIIIVarConstraints_Type()
)
cmcIIIVarConstraints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarConstraints.setStatus("current")
_CmcIIIVarSteps_Type = Integer32
_CmcIIIVarSteps_Object = MibTableColumn
cmcIIIVarSteps = _CmcIIIVarSteps_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 9),
    _CmcIIIVarSteps_Type()
)
cmcIIIVarSteps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarSteps.setStatus("current")


class _CmcIIIVarValueStr_Type(DisplayString):
    """Custom type cmcIIIVarValueStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIIVarValueStr_Type.__name__ = "DisplayString"
_CmcIIIVarValueStr_Object = MibTableColumn
cmcIIIVarValueStr = _CmcIIIVarValueStr_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 10),
    _CmcIIIVarValueStr_Type()
)
cmcIIIVarValueStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIVarValueStr.setStatus("current")
_CmcIIIVarValueInt_Type = Integer32
_CmcIIIVarValueInt_Object = MibTableColumn
cmcIIIVarValueInt = _CmcIIIVarValueInt_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 11),
    _CmcIIIVarValueInt_Type()
)
cmcIIIVarValueInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIVarValueInt.setStatus("current")
_CmcIIIVarLastChange_Type = Unsigned32
_CmcIIIVarLastChange_Object = MibTableColumn
cmcIIIVarLastChange = _CmcIIIVarLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 12),
    _CmcIIIVarLastChange_Type()
)
cmcIIIVarLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarLastChange.setStatus("current")


class _CmcIIIVarAccess_Type(Integer32):
    """Custom type cmcIIIVarAccess based on Integer32"""
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
        *(("none", 1),
          ("readonly", 2),
          ("readwrite", 3),
          ("readwriteextended", 5),
          ("readwriteswitch", 4))
    )


_CmcIIIVarAccess_Type.__name__ = "Integer32"
_CmcIIIVarAccess_Object = MibTableColumn
cmcIIIVarAccess = _CmcIIIVarAccess_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 13),
    _CmcIIIVarAccess_Type()
)
cmcIIIVarAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarAccess.setStatus("current")


class _CmcIIIVarQuality_Type(Integer32):
    """Custom type cmcIIIVarQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 4),
          ("alarmNoValue", 24),
          ("info", 5),
          ("infoNoValue", 25),
          ("ok", 2),
          ("okNoValue", 22),
          ("undefined", 1),
          ("undefinedNoValue", 21),
          ("warning", 3),
          ("warningNoValue", 23))
    )


_CmcIIIVarQuality_Type.__name__ = "Integer32"
_CmcIIIVarQuality_Object = MibTableColumn
cmcIIIVarQuality = _CmcIIIVarQuality_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 14),
    _CmcIIIVarQuality_Type()
)
cmcIIIVarQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarQuality.setStatus("current")
_CmcIIIVarEntPhysicalIndex_Type = Integer32
_CmcIIIVarEntPhysicalIndex_Object = MibTableColumn
cmcIIIVarEntPhysicalIndex = _CmcIIIVarEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 2, 1, 15),
    _CmcIIIVarEntPhysicalIndex_Type()
)
cmcIIIVarEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarEntPhysicalIndex.setStatus("current")
_CmcIIIVarByTypeTable_Object = MibTable
cmcIIIVarByTypeTable = _CmcIIIVarByTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 3)
)
if mibBuilder.loadTexts:
    cmcIIIVarByTypeTable.setStatus("current")
_CmcIIIVarByTypeEntry_Object = MibTableRow
cmcIIIVarByTypeEntry = _CmcIIIVarByTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 3, 1)
)
cmcIIIVarByTypeEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarByTypeType"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarByTypeDeviceIndex"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarByTypeIndex"),
)
if mibBuilder.loadTexts:
    cmcIIIVarByTypeEntry.setStatus("current")


class _CmcIIIVarByTypeType_Type(Integer32):
    """Custom type cmcIIIVarByTypeType based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
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
              34,
              35,
              36,
              40,
              41,
              42,
              43,
              44,
              45,
              50,
              51,
              52,
              53,
              54,
              55,
              80,
              81,
              82,
              83,
              84,
              85,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              100,
              110,
              111,
              112,
              113,
              120,
              121,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("accessLogic", 32),
          ("accessTime", 31),
          ("alarmDur", 11),
          ("assembly", 28),
          ("building", 131),
          ("category", 14),
          ("circuit", 42),
          ("command", 81),
          ("commandCtrl", 120),
          ("commandCtrlDP", 121),
          ("commandEnum", 82),
          ("commandKeypad", 83),
          ("commandRack", 85),
          ("commandService", 84),
          ("config", 25),
          ("configLcpFcs", 27),
          ("configNum", 26),
          ("configPar", 13),
          ("configWiring", 29),
          ("connected", 96),
          ("connectedEnum", 97),
          ("currentMax", 55),
          ("currentMin", 54),
          ("customValue", 45),
          ("description", 1),
          ("devLocation", 53),
          ("devName", 52),
          ("grouping", 100),
          ("gsmStatus", 95),
          ("hysteresis", 6),
          ("ignore", 254),
          ("illegal", 255),
          ("keycode", 80),
          ("level", 132),
          ("location", 130),
          ("logic", 15),
          ("logicEnum", 16),
          ("mountPos", 93),
          ("mountPosEnum", 94),
          ("numberOfRU", 137),
          ("offset", 18),
          ("operatingTime", 136),
          ("orderNr", 51),
          ("outdelayExec", 23),
          ("output", 20),
          ("outputEnum", 24),
          ("outputPWM", 40),
          ("outputaction", 22),
          ("outputdelay", 21),
          ("pin", 35),
          ("position", 33),
          ("positionEnum", 34),
          ("productDate", 50),
          ("rack", 135),
          ("rizoneArray", 43),
          ("room", 133),
          ("rotation", 41),
          ("row", 134),
          ("scaleEnd", 113),
          ("scaleStart", 112),
          ("scaleUnit", 111),
          ("scaleValue", 110),
          ("sensitivity", 30),
          ("sequence", 36),
          ("serialNumber", 92),
          ("setCntrl", 17),
          ("setHigh", 3),
          ("setLow", 5),
          ("setWarn", 4),
          ("setWarnLow", 9),
          ("socketType", 44),
          ("status", 7),
          ("statusEnum", 8),
          ("steps", 12),
          ("swVersion", 91),
          ("tagsChanged", 139),
          ("tagsQuit", 138),
          ("type", 19),
          ("uid", 140),
          ("unit", 10),
          ("unitType", 90),
          ("value", 2))
    )


_CmcIIIVarByTypeType_Type.__name__ = "Integer32"
_CmcIIIVarByTypeType_Object = MibTableColumn
cmcIIIVarByTypeType = _CmcIIIVarByTypeType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 3, 1, 1),
    _CmcIIIVarByTypeType_Type()
)
cmcIIIVarByTypeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarByTypeType.setStatus("current")


class _CmcIIIVarByTypeDeviceIndex_Type(Unsigned32):
    """Custom type cmcIIIVarByTypeDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIVarByTypeDeviceIndex_Type.__name__ = "Unsigned32"
_CmcIIIVarByTypeDeviceIndex_Object = MibTableColumn
cmcIIIVarByTypeDeviceIndex = _CmcIIIVarByTypeDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 3, 1, 2),
    _CmcIIIVarByTypeDeviceIndex_Type()
)
cmcIIIVarByTypeDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarByTypeDeviceIndex.setStatus("current")


class _CmcIIIVarByTypeIndex_Type(Unsigned32):
    """Custom type cmcIIIVarByTypeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIVarByTypeIndex_Type.__name__ = "Unsigned32"
_CmcIIIVarByTypeIndex_Object = MibTableColumn
cmcIIIVarByTypeIndex = _CmcIIIVarByTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 3, 1, 3),
    _CmcIIIVarByTypeIndex_Type()
)
cmcIIIVarByTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarByTypeIndex.setStatus("current")


class _CmcIIIVarByTypeValueStr_Type(DisplayString):
    """Custom type cmcIIIVarByTypeValueStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIIVarByTypeValueStr_Type.__name__ = "DisplayString"
_CmcIIIVarByTypeValueStr_Object = MibTableColumn
cmcIIIVarByTypeValueStr = _CmcIIIVarByTypeValueStr_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 3, 1, 4),
    _CmcIIIVarByTypeValueStr_Type()
)
cmcIIIVarByTypeValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarByTypeValueStr.setStatus("current")
_CmcIIIVarByTypeValueInt_Type = Integer32
_CmcIIIVarByTypeValueInt_Object = MibTableColumn
cmcIIIVarByTypeValueInt = _CmcIIIVarByTypeValueInt_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 3, 1, 5),
    _CmcIIIVarByTypeValueInt_Type()
)
cmcIIIVarByTypeValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarByTypeValueInt.setStatus("current")
_CmcIIIVarByTypeLastChange_Type = Unsigned32
_CmcIIIVarByTypeLastChange_Object = MibTableColumn
cmcIIIVarByTypeLastChange = _CmcIIIVarByTypeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 3, 1, 6),
    _CmcIIIVarByTypeLastChange_Type()
)
cmcIIIVarByTypeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarByTypeLastChange.setStatus("current")
_CmcIIIVarByQualityTable_Object = MibTable
cmcIIIVarByQualityTable = _CmcIIIVarByQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 4)
)
if mibBuilder.loadTexts:
    cmcIIIVarByQualityTable.setStatus("current")
_CmcIIIVarByQualityEntry_Object = MibTableRow
cmcIIIVarByQualityEntry = _CmcIIIVarByQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 4, 1)
)
cmcIIIVarByQualityEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarByQualityQuality"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarByQualityDeviceIndex"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarByQualityIndex"),
)
if mibBuilder.loadTexts:
    cmcIIIVarByQualityEntry.setStatus("current")


class _CmcIIIVarByQualityQuality_Type(Integer32):
    """Custom type cmcIIIVarByQualityQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 4),
          ("alarmNoValue", 24),
          ("info", 5),
          ("infoNoValue", 25),
          ("ok", 2),
          ("okNoValue", 22),
          ("undefined", 1),
          ("undefinedNoValue", 21),
          ("warning", 3),
          ("warningNoValue", 23))
    )


_CmcIIIVarByQualityQuality_Type.__name__ = "Integer32"
_CmcIIIVarByQualityQuality_Object = MibTableColumn
cmcIIIVarByQualityQuality = _CmcIIIVarByQualityQuality_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 4, 1, 1),
    _CmcIIIVarByQualityQuality_Type()
)
cmcIIIVarByQualityQuality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarByQualityQuality.setStatus("current")


class _CmcIIIVarByQualityDeviceIndex_Type(Unsigned32):
    """Custom type cmcIIIVarByQualityDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIVarByQualityDeviceIndex_Type.__name__ = "Unsigned32"
_CmcIIIVarByQualityDeviceIndex_Object = MibTableColumn
cmcIIIVarByQualityDeviceIndex = _CmcIIIVarByQualityDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 4, 1, 2),
    _CmcIIIVarByQualityDeviceIndex_Type()
)
cmcIIIVarByQualityDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarByQualityDeviceIndex.setStatus("current")


class _CmcIIIVarByQualityIndex_Type(Unsigned32):
    """Custom type cmcIIIVarByQualityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIVarByQualityIndex_Type.__name__ = "Unsigned32"
_CmcIIIVarByQualityIndex_Object = MibTableColumn
cmcIIIVarByQualityIndex = _CmcIIIVarByQualityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 4, 1, 3),
    _CmcIIIVarByQualityIndex_Type()
)
cmcIIIVarByQualityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarByQualityIndex.setStatus("current")


class _CmcIIIVarByQualityValueStr_Type(DisplayString):
    """Custom type cmcIIIVarByQualityValueStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIIVarByQualityValueStr_Type.__name__ = "DisplayString"
_CmcIIIVarByQualityValueStr_Object = MibTableColumn
cmcIIIVarByQualityValueStr = _CmcIIIVarByQualityValueStr_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 4, 1, 4),
    _CmcIIIVarByQualityValueStr_Type()
)
cmcIIIVarByQualityValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarByQualityValueStr.setStatus("current")
_CmcIIIVarByQualityValueInt_Type = Integer32
_CmcIIIVarByQualityValueInt_Object = MibTableColumn
cmcIIIVarByQualityValueInt = _CmcIIIVarByQualityValueInt_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 4, 1, 5),
    _CmcIIIVarByQualityValueInt_Type()
)
cmcIIIVarByQualityValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarByQualityValueInt.setStatus("current")
_CmcIIIVarByQualityLastChange_Type = Unsigned32
_CmcIIIVarByQualityLastChange_Object = MibTableColumn
cmcIIIVarByQualityLastChange = _CmcIIIVarByQualityLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 4, 1, 6),
    _CmcIIIVarByQualityLastChange_Type()
)
cmcIIIVarByQualityLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarByQualityLastChange.setStatus("current")
_CmcIIIVarIntDynTable_Object = MibTable
cmcIIIVarIntDynTable = _CmcIIIVarIntDynTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 5)
)
if mibBuilder.loadTexts:
    cmcIIIVarIntDynTable.setStatus("current")
_CmcIIIVarIntDynEntry_Object = MibTableRow
cmcIIIVarIntDynEntry = _CmcIIIVarIntDynEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 5, 1)
)
cmcIIIVarIntDynEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarIntDynDeviceIndex"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarIntDynIndex"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarIntDynLastChange"),
)
if mibBuilder.loadTexts:
    cmcIIIVarIntDynEntry.setStatus("current")


class _CmcIIIVarIntDynDeviceIndex_Type(Unsigned32):
    """Custom type cmcIIIVarIntDynDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIVarIntDynDeviceIndex_Type.__name__ = "Unsigned32"
_CmcIIIVarIntDynDeviceIndex_Object = MibTableColumn
cmcIIIVarIntDynDeviceIndex = _CmcIIIVarIntDynDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 5, 1, 1),
    _CmcIIIVarIntDynDeviceIndex_Type()
)
cmcIIIVarIntDynDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarIntDynDeviceIndex.setStatus("current")


class _CmcIIIVarIntDynIndex_Type(Unsigned32):
    """Custom type cmcIIIVarIntDynIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIVarIntDynIndex_Type.__name__ = "Unsigned32"
_CmcIIIVarIntDynIndex_Object = MibTableColumn
cmcIIIVarIntDynIndex = _CmcIIIVarIntDynIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 5, 1, 2),
    _CmcIIIVarIntDynIndex_Type()
)
cmcIIIVarIntDynIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarIntDynIndex.setStatus("current")


class _CmcIIIVarIntDynLastChange_Type(Unsigned32):
    """Custom type cmcIIIVarIntDynLastChange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CmcIIIVarIntDynLastChange_Type.__name__ = "Unsigned32"
_CmcIIIVarIntDynLastChange_Object = MibTableColumn
cmcIIIVarIntDynLastChange = _CmcIIIVarIntDynLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 5, 1, 3),
    _CmcIIIVarIntDynLastChange_Type()
)
cmcIIIVarIntDynLastChange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarIntDynLastChange.setStatus("current")
_CmcIIIVarIntDynValue_Type = Integer32
_CmcIIIVarIntDynValue_Object = MibTableColumn
cmcIIIVarIntDynValue = _CmcIIIVarIntDynValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 5, 1, 4),
    _CmcIIIVarIntDynValue_Type()
)
cmcIIIVarIntDynValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarIntDynValue.setStatus("current")
_CmcIIIVarStrDynTable_Object = MibTable
cmcIIIVarStrDynTable = _CmcIIIVarStrDynTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 6)
)
if mibBuilder.loadTexts:
    cmcIIIVarStrDynTable.setStatus("current")
_CmcIIIVarStrDynEntry_Object = MibTableRow
cmcIIIVarStrDynEntry = _CmcIIIVarStrDynEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 6, 1)
)
cmcIIIVarStrDynEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarStrDynDeviceIndex"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarStrDynIndex"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIIVarStrDynLastChange"),
)
if mibBuilder.loadTexts:
    cmcIIIVarStrDynEntry.setStatus("current")


class _CmcIIIVarStrDynDeviceIndex_Type(Unsigned32):
    """Custom type cmcIIIVarStrDynDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIVarStrDynDeviceIndex_Type.__name__ = "Unsigned32"
_CmcIIIVarStrDynDeviceIndex_Object = MibTableColumn
cmcIIIVarStrDynDeviceIndex = _CmcIIIVarStrDynDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 6, 1, 1),
    _CmcIIIVarStrDynDeviceIndex_Type()
)
cmcIIIVarStrDynDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarStrDynDeviceIndex.setStatus("current")


class _CmcIIIVarStrDynIndex_Type(Unsigned32):
    """Custom type cmcIIIVarStrDynIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIVarStrDynIndex_Type.__name__ = "Unsigned32"
_CmcIIIVarStrDynIndex_Object = MibTableColumn
cmcIIIVarStrDynIndex = _CmcIIIVarStrDynIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 6, 1, 2),
    _CmcIIIVarStrDynIndex_Type()
)
cmcIIIVarStrDynIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarStrDynIndex.setStatus("current")


class _CmcIIIVarStrDynLastChange_Type(Unsigned32):
    """Custom type cmcIIIVarStrDynLastChange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CmcIIIVarStrDynLastChange_Type.__name__ = "Unsigned32"
_CmcIIIVarStrDynLastChange_Object = MibTableColumn
cmcIIIVarStrDynLastChange = _CmcIIIVarStrDynLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 6, 1, 3),
    _CmcIIIVarStrDynLastChange_Type()
)
cmcIIIVarStrDynLastChange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIVarStrDynLastChange.setStatus("current")


class _CmcIIIVarStrDynValue_Type(DisplayString):
    """Custom type cmcIIIVarStrDynValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIIVarStrDynValue_Type.__name__ = "DisplayString"
_CmcIIIVarStrDynValue_Object = MibTableColumn
cmcIIIVarStrDynValue = _CmcIIIVarStrDynValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 2, 6, 1, 4),
    _CmcIIIVarStrDynValue_Type()
)
cmcIIIVarStrDynValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIVarStrDynValue.setStatus("current")
_CmcIIIMsgs_ObjectIdentity = ObjectIdentity
cmcIIIMsgs = _CmcIIIMsgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3)
)
_CmcIIIMsgInfo_ObjectIdentity = ObjectIdentity
cmcIIIMsgInfo = _CmcIIIMsgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 1)
)


class _CmcIIIOverallMsgStatus_Type(Integer32):
    """Custom type cmcIIIOverallMsgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("ok", 1),
          ("warning", 2))
    )


_CmcIIIOverallMsgStatus_Type.__name__ = "Integer32"
_CmcIIIOverallMsgStatus_Object = MibScalar
cmcIIIOverallMsgStatus = _CmcIIIOverallMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 1, 1),
    _CmcIIIOverallMsgStatus_Type()
)
cmcIIIOverallMsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIOverallMsgStatus.setStatus("current")
_CmcIIINumberOfMsgs_Type = Integer32
_CmcIIINumberOfMsgs_Object = MibScalar
cmcIIINumberOfMsgs = _CmcIIINumberOfMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 1, 2),
    _CmcIIINumberOfMsgs_Type()
)
cmcIIINumberOfMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfMsgs.setStatus("current")
_CmcIIILastChangeOverallMsgStatus_Type = Unsigned32
_CmcIIILastChangeOverallMsgStatus_Object = MibScalar
cmcIIILastChangeOverallMsgStatus = _CmcIIILastChangeOverallMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 1, 3),
    _CmcIIILastChangeOverallMsgStatus_Type()
)
cmcIIILastChangeOverallMsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeOverallMsgStatus.setStatus("current")
_CmcIIILastChangeNumberOfMsgs_Type = Unsigned32
_CmcIIILastChangeNumberOfMsgs_Object = MibScalar
cmcIIILastChangeNumberOfMsgs = _CmcIIILastChangeNumberOfMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 1, 4),
    _CmcIIILastChangeNumberOfMsgs_Type()
)
cmcIIILastChangeNumberOfMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeNumberOfMsgs.setStatus("current")
_CmcIIILastChangeMsgSettings_Type = Unsigned32
_CmcIIILastChangeMsgSettings_Object = MibScalar
cmcIIILastChangeMsgSettings = _CmcIIILastChangeMsgSettings_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 1, 5),
    _CmcIIILastChangeMsgSettings_Type()
)
cmcIIILastChangeMsgSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeMsgSettings.setStatus("current")
_CmcIIIMsgTable_Object = MibTable
cmcIIIMsgTable = _CmcIIIMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2)
)
if mibBuilder.loadTexts:
    cmcIIIMsgTable.setStatus("current")
_CmcIIIMsgEntry_Object = MibTableRow
cmcIIIMsgEntry = _CmcIIIMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1)
)
cmcIIIMsgEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIMsgDeviceIndex"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIIMsgIndex"),
)
if mibBuilder.loadTexts:
    cmcIIIMsgEntry.setStatus("current")


class _CmcIIIMsgDeviceIndex_Type(Unsigned32):
    """Custom type cmcIIIMsgDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIMsgDeviceIndex_Type.__name__ = "Unsigned32"
_CmcIIIMsgDeviceIndex_Object = MibTableColumn
cmcIIIMsgDeviceIndex = _CmcIIIMsgDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 1),
    _CmcIIIMsgDeviceIndex_Type()
)
cmcIIIMsgDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIMsgDeviceIndex.setStatus("current")


class _CmcIIIMsgIndex_Type(Unsigned32):
    """Custom type cmcIIIMsgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIMsgIndex_Type.__name__ = "Unsigned32"
_CmcIIIMsgIndex_Object = MibTableColumn
cmcIIIMsgIndex = _CmcIIIMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 2),
    _CmcIIIMsgIndex_Type()
)
cmcIIIMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIMsgIndex.setStatus("current")


class _CmcIIIMsgText_Type(DisplayString):
    """Custom type cmcIIIMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIIMsgText_Type.__name__ = "DisplayString"
_CmcIIIMsgText_Object = MibTableColumn
cmcIIIMsgText = _CmcIIIMsgText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 3),
    _CmcIIIMsgText_Type()
)
cmcIIIMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIMsgText.setStatus("current")


class _CmcIIIMsgStatus_Type(Integer32):
    """Custom type cmcIIIMsgStatus based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("active", 28),
          ("alarm", 5),
          ("busy", 19),
          ("calibration", 26),
          ("closed", 13),
          ("configChanged", 2),
          ("detected", 22),
          ("doorOpen", 16),
          ("error", 3),
          ("exchanged", 31),
          ("highAlarm", 8),
          ("highWarn", 6),
          ("inactive", 27),
          ("locked", 14),
          ("lost", 21),
          ("lowAlarm", 7),
          ("lowVoltage", 23),
          ("lowWarn", 9),
          ("noAccess", 20),
          ("noPower", 29),
          ("notAvail", 1),
          ("ok", 4),
          ("open", 12),
          ("probeopen", 24),
          ("probeshort", 25),
          ("readOnly", 30),
          ("service", 17),
          ("setOff", 10),
          ("setOn", 11),
          ("standby", 18),
          ("unlRemote", 15))
    )


_CmcIIIMsgStatus_Type.__name__ = "Integer32"
_CmcIIIMsgStatus_Object = MibTableColumn
cmcIIIMsgStatus = _CmcIIIMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 4),
    _CmcIIIMsgStatus_Type()
)
cmcIIIMsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIMsgStatus.setStatus("current")


class _CmcIIIMsgRelay_Type(Integer32):
    """Custom type cmcIIIMsgRelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmcIIIMsgRelay_Type.__name__ = "Integer32"
_CmcIIIMsgRelay_Object = MibTableColumn
cmcIIIMsgRelay = _CmcIIIMsgRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 5),
    _CmcIIIMsgRelay_Type()
)
cmcIIIMsgRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIMsgRelay.setStatus("current")


class _CmcIIIMsgBeeper_Type(Integer32):
    """Custom type cmcIIIMsgBeeper based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmcIIIMsgBeeper_Type.__name__ = "Integer32"
_CmcIIIMsgBeeper_Object = MibTableColumn
cmcIIIMsgBeeper = _CmcIIIMsgBeeper_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 6),
    _CmcIIIMsgBeeper_Type()
)
cmcIIIMsgBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIMsgBeeper.setStatus("current")


class _CmcIIIMsgTrap_Type(Bits):
    """Custom type cmcIIIMsgTrap based on Bits"""
    namedValues = NamedValues(
        *(("receiver1", 0),
          ("receiver10", 9),
          ("receiver11", 10),
          ("receiver12", 11),
          ("receiver13", 12),
          ("receiver14", 13),
          ("receiver15", 14),
          ("receiver16", 15),
          ("receiver2", 1),
          ("receiver3", 2),
          ("receiver4", 3),
          ("receiver5", 4),
          ("receiver6", 5),
          ("receiver7", 6),
          ("receiver8", 7),
          ("receiver9", 8))
    )

_CmcIIIMsgTrap_Type.__name__ = "Bits"
_CmcIIIMsgTrap_Object = MibTableColumn
cmcIIIMsgTrap = _CmcIIIMsgTrap_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 7),
    _CmcIIIMsgTrap_Type()
)
cmcIIIMsgTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIMsgTrap.setStatus("current")


class _CmcIIIMsgSMTP_Type(Bits):
    """Custom type cmcIIIMsgSMTP based on Bits"""
    namedValues = NamedValues(
        *(("receiver1", 0),
          ("receiver10", 9),
          ("receiver11", 10),
          ("receiver12", 11),
          ("receiver13", 12),
          ("receiver14", 13),
          ("receiver15", 14),
          ("receiver16", 15),
          ("receiver2", 1),
          ("receiver3", 2),
          ("receiver4", 3),
          ("receiver5", 4),
          ("receiver6", 5),
          ("receiver7", 6),
          ("receiver8", 7),
          ("receiver9", 8))
    )

_CmcIIIMsgSMTP_Type.__name__ = "Bits"
_CmcIIIMsgSMTP_Object = MibTableColumn
cmcIIIMsgSMTP = _CmcIIIMsgSMTP_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 8),
    _CmcIIIMsgSMTP_Type()
)
cmcIIIMsgSMTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIMsgSMTP.setStatus("current")


class _CmcIIIMsgSMS_Type(Bits):
    """Custom type cmcIIIMsgSMS based on Bits"""
    namedValues = NamedValues(
        *(("receiver1", 0),
          ("receiver10", 9),
          ("receiver11", 10),
          ("receiver12", 11),
          ("receiver13", 12),
          ("receiver14", 13),
          ("receiver15", 14),
          ("receiver16", 15),
          ("receiver2", 1),
          ("receiver3", 2),
          ("receiver4", 3),
          ("receiver5", 4),
          ("receiver6", 5),
          ("receiver7", 6),
          ("receiver8", 7),
          ("receiver9", 8))
    )

_CmcIIIMsgSMS_Type.__name__ = "Bits"
_CmcIIIMsgSMS_Object = MibTableColumn
cmcIIIMsgSMS = _CmcIIIMsgSMS_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 9),
    _CmcIIIMsgSMS_Type()
)
cmcIIIMsgSMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIMsgSMS.setStatus("current")


class _CmcIIIMsgQuit_Type(Integer32):
    """Custom type cmcIIIMsgQuit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_CmcIIIMsgQuit_Type.__name__ = "Integer32"
_CmcIIIMsgQuit_Object = MibTableColumn
cmcIIIMsgQuit = _CmcIIIMsgQuit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 10),
    _CmcIIIMsgQuit_Type()
)
cmcIIIMsgQuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIMsgQuit.setStatus("current")
_CmcIIIMsgDelay_Type = Unsigned32
_CmcIIIMsgDelay_Object = MibTableColumn
cmcIIIMsgDelay = _CmcIIIMsgDelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 11),
    _CmcIIIMsgDelay_Type()
)
cmcIIIMsgDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIMsgDelay.setStatus("current")
_CmcIIIMsgSchedAlarmOff_Type = Integer32
_CmcIIIMsgSchedAlarmOff_Object = MibTableColumn
cmcIIIMsgSchedAlarmOff = _CmcIIIMsgSchedAlarmOff_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 12),
    _CmcIIIMsgSchedAlarmOff_Type()
)
cmcIIIMsgSchedAlarmOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIMsgSchedAlarmOff.setStatus("current")


class _CmcIIIMsgQuality_Type(Integer32):
    """Custom type cmcIIIMsgQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 4),
          ("alarmNoValue", 24),
          ("info", 5),
          ("infoNoValue", 25),
          ("ok", 2),
          ("okNoValue", 22),
          ("undefined", 1),
          ("undefinedNoValue", 21),
          ("warning", 3),
          ("warningNoValue", 23))
    )


_CmcIIIMsgQuality_Type.__name__ = "Integer32"
_CmcIIIMsgQuality_Object = MibTableColumn
cmcIIIMsgQuality = _CmcIIIMsgQuality_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 13),
    _CmcIIIMsgQuality_Type()
)
cmcIIIMsgQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIMsgQuality.setStatus("current")
_CmcIIIMsgVarIdx_Type = Integer32
_CmcIIIMsgVarIdx_Object = MibTableColumn
cmcIIIMsgVarIdx = _CmcIIIMsgVarIdx_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 14),
    _CmcIIIMsgVarIdx_Type()
)
cmcIIIMsgVarIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIMsgVarIdx.setStatus("current")
_CmcIIIMsgVarValueIdx_Type = Integer32
_CmcIIIMsgVarValueIdx_Object = MibTableColumn
cmcIIIMsgVarValueIdx = _CmcIIIMsgVarValueIdx_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 15),
    _CmcIIIMsgVarValueIdx_Type()
)
cmcIIIMsgVarValueIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIMsgVarValueIdx.setStatus("current")


class _CmcIIIMsgStatusText_Type(DisplayString):
    """Custom type cmcIIIMsgStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_CmcIIIMsgStatusText_Type.__name__ = "DisplayString"
_CmcIIIMsgStatusText_Object = MibTableColumn
cmcIIIMsgStatusText = _CmcIIIMsgStatusText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 3, 2, 1, 16),
    _CmcIIIMsgStatusText_Type()
)
cmcIIIMsgStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIMsgStatusText.setStatus("current")
_CmcIIIDrcs_ObjectIdentity = ObjectIdentity
cmcIIIDrcs = _CmcIIIDrcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4)
)
_CmcIIIDrcInfo_ObjectIdentity = ObjectIdentity
cmcIIIDrcInfo = _CmcIIIDrcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 1)
)


class _CmcIIIOverallDrcStatus_Type(Integer32):
    """Custom type cmcIIIOverallDrcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("ok", 1),
          ("warning", 2))
    )


_CmcIIIOverallDrcStatus_Type.__name__ = "Integer32"
_CmcIIIOverallDrcStatus_Object = MibScalar
cmcIIIOverallDrcStatus = _CmcIIIOverallDrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 1, 1),
    _CmcIIIOverallDrcStatus_Type()
)
cmcIIIOverallDrcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIOverallDrcStatus.setStatus("current")
_CmcIIINumberOfDrcs_Type = Unsigned32
_CmcIIINumberOfDrcs_Object = MibScalar
cmcIIINumberOfDrcs = _CmcIIINumberOfDrcs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 1, 2),
    _CmcIIINumberOfDrcs_Type()
)
cmcIIINumberOfDrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfDrcs.setStatus("current")
_CmcIIIOverallLastChangeDrcStatus_Type = Unsigned32
_CmcIIIOverallLastChangeDrcStatus_Object = MibScalar
cmcIIIOverallLastChangeDrcStatus = _CmcIIIOverallLastChangeDrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 1, 3),
    _CmcIIIOverallLastChangeDrcStatus_Type()
)
cmcIIIOverallLastChangeDrcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIOverallLastChangeDrcStatus.setStatus("current")
_CmcIIILastChangeNumberOfDrcs_Type = Unsigned32
_CmcIIILastChangeNumberOfDrcs_Object = MibScalar
cmcIIILastChangeNumberOfDrcs = _CmcIIILastChangeNumberOfDrcs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 1, 4),
    _CmcIIILastChangeNumberOfDrcs_Type()
)
cmcIIILastChangeNumberOfDrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeNumberOfDrcs.setStatus("current")


class _CmcIIIOverallDrcUtilization_Type(Unsigned32):
    """Custom type cmcIIIOverallDrcUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmcIIIOverallDrcUtilization_Type.__name__ = "Unsigned32"
_CmcIIIOverallDrcUtilization_Object = MibScalar
cmcIIIOverallDrcUtilization = _CmcIIIOverallDrcUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 1, 5),
    _CmcIIIOverallDrcUtilization_Type()
)
cmcIIIOverallDrcUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIOverallDrcUtilization.setStatus("current")
_CmcIIIOverallDrcPower_Type = Unsigned32
_CmcIIIOverallDrcPower_Object = MibScalar
cmcIIIOverallDrcPower = _CmcIIIOverallDrcPower_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 1, 6),
    _CmcIIIOverallDrcPower_Type()
)
cmcIIIOverallDrcPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIOverallDrcPower.setStatus("current")
_CmcIIIDrcTable_Object = MibTable
cmcIIIDrcTable = _CmcIIIDrcTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2)
)
if mibBuilder.loadTexts:
    cmcIIIDrcTable.setStatus("current")
_CmcIIIDrcEntry_Object = MibTableRow
cmcIIIDrcEntry = _CmcIIIDrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1)
)
cmcIIIDrcEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIDrcIndex"),
)
if mibBuilder.loadTexts:
    cmcIIIDrcEntry.setStatus("current")


class _CmcIIIDrcIndex_Type(Unsigned32):
    """Custom type cmcIIIDrcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIDrcIndex_Type.__name__ = "Unsigned32"
_CmcIIIDrcIndex_Object = MibTableColumn
cmcIIIDrcIndex = _CmcIIIDrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 1),
    _CmcIIIDrcIndex_Type()
)
cmcIIIDrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIDrcIndex.setStatus("current")


class _CmcIIIDrcStatus_Type(Integer32):
    """Custom type cmcIIIDrcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              17,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 5),
          ("configChanged", 2),
          ("detected", 22),
          ("error", 3),
          ("lost", 21),
          ("notAvail", 1),
          ("ok", 4),
          ("service", 17))
    )


_CmcIIIDrcStatus_Type.__name__ = "Integer32"
_CmcIIIDrcStatus_Object = MibTableColumn
cmcIIIDrcStatus = _CmcIIIDrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 2),
    _CmcIIIDrcStatus_Type()
)
cmcIIIDrcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcStatus.setStatus("current")
_CmcIIILastChangeDrcStatus_Type = Unsigned32
_CmcIIILastChangeDrcStatus_Object = MibTableColumn
cmcIIILastChangeDrcStatus = _CmcIIILastChangeDrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 3),
    _CmcIIILastChangeDrcStatus_Type()
)
cmcIIILastChangeDrcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeDrcStatus.setStatus("current")


class _CmcIIIDrcUnitName_Type(DisplayString):
    """Custom type cmcIIIDrcUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmcIIIDrcUnitName_Type.__name__ = "DisplayString"
_CmcIIIDrcUnitName_Object = MibTableColumn
cmcIIIDrcUnitName = _CmcIIIDrcUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 4),
    _CmcIIIDrcUnitName_Type()
)
cmcIIIDrcUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDrcUnitName.setStatus("current")


class _CmcIIIDrcLocation_Type(DisplayString):
    """Custom type cmcIIIDrcLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmcIIIDrcLocation_Type.__name__ = "DisplayString"
_CmcIIIDrcLocation_Object = MibTableColumn
cmcIIIDrcLocation = _CmcIIIDrcLocation_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 5),
    _CmcIIIDrcLocation_Type()
)
cmcIIIDrcLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDrcLocation.setStatus("current")


class _CmcIIIDrcBuilding_Type(DisplayString):
    """Custom type cmcIIIDrcBuilding based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmcIIIDrcBuilding_Type.__name__ = "DisplayString"
_CmcIIIDrcBuilding_Object = MibTableColumn
cmcIIIDrcBuilding = _CmcIIIDrcBuilding_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 6),
    _CmcIIIDrcBuilding_Type()
)
cmcIIIDrcBuilding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDrcBuilding.setStatus("current")


class _CmcIIIDrcLevel_Type(DisplayString):
    """Custom type cmcIIIDrcLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmcIIIDrcLevel_Type.__name__ = "DisplayString"
_CmcIIIDrcLevel_Object = MibTableColumn
cmcIIIDrcLevel = _CmcIIIDrcLevel_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 7),
    _CmcIIIDrcLevel_Type()
)
cmcIIIDrcLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDrcLevel.setStatus("current")


class _CmcIIIDrcRoom_Type(DisplayString):
    """Custom type cmcIIIDrcRoom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmcIIIDrcRoom_Type.__name__ = "DisplayString"
_CmcIIIDrcRoom_Object = MibTableColumn
cmcIIIDrcRoom = _CmcIIIDrcRoom_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 8),
    _CmcIIIDrcRoom_Type()
)
cmcIIIDrcRoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDrcRoom.setStatus("current")


class _CmcIIIDrcRow_Type(DisplayString):
    """Custom type cmcIIIDrcRow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmcIIIDrcRow_Type.__name__ = "DisplayString"
_CmcIIIDrcRow_Object = MibTableColumn
cmcIIIDrcRow = _CmcIIIDrcRow_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 9),
    _CmcIIIDrcRow_Type()
)
cmcIIIDrcRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDrcRow.setStatus("current")


class _CmcIIIDrcRackNr_Type(DisplayString):
    """Custom type cmcIIIDrcRackNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmcIIIDrcRackNr_Type.__name__ = "DisplayString"
_CmcIIIDrcRackNr_Object = MibTableColumn
cmcIIIDrcRackNr = _CmcIIIDrcRackNr_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 10),
    _CmcIIIDrcRackNr_Type()
)
cmcIIIDrcRackNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDrcRackNr.setStatus("current")


class _CmcIIIDrcMfgDate_Type(DisplayString):
    """Custom type cmcIIIDrcMfgDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmcIIIDrcMfgDate_Type.__name__ = "DisplayString"
_CmcIIIDrcMfgDate_Object = MibTableColumn
cmcIIIDrcMfgDate = _CmcIIIDrcMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 11),
    _CmcIIIDrcMfgDate_Type()
)
cmcIIIDrcMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcMfgDate.setStatus("current")
_CmcIIIDrcSerialNr_Type = Unsigned32
_CmcIIIDrcSerialNr_Object = MibTableColumn
cmcIIIDrcSerialNr = _CmcIIIDrcSerialNr_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 12),
    _CmcIIIDrcSerialNr_Type()
)
cmcIIIDrcSerialNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcSerialNr.setStatus("current")
_CmcIIIDrcOpHours_Type = Unsigned32
_CmcIIIDrcOpHours_Object = MibTableColumn
cmcIIIDrcOpHours = _CmcIIIDrcOpHours_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 13),
    _CmcIIIDrcOpHours_Type()
)
cmcIIIDrcOpHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcOpHours.setStatus("current")
_CmcIIIDrcNumberOfRU_Type = Unsigned32
_CmcIIIDrcNumberOfRU_Object = MibTableColumn
cmcIIIDrcNumberOfRU = _CmcIIIDrcNumberOfRU_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 14),
    _CmcIIIDrcNumberOfRU_Type()
)
cmcIIIDrcNumberOfRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcNumberOfRU.setStatus("current")


class _CmcIIIDrcUtilization_Type(Unsigned32):
    """Custom type cmcIIIDrcUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmcIIIDrcUtilization_Type.__name__ = "Unsigned32"
_CmcIIIDrcUtilization_Object = MibTableColumn
cmcIIIDrcUtilization = _CmcIIIDrcUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 15),
    _CmcIIIDrcUtilization_Type()
)
cmcIIIDrcUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcUtilization.setStatus("current")
_CmcIIITotalDrcPower_Type = Unsigned32
_CmcIIITotalDrcPower_Object = MibTableColumn
cmcIIITotalDrcPower = _CmcIIITotalDrcPower_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 16),
    _CmcIIITotalDrcPower_Type()
)
cmcIIITotalDrcPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIITotalDrcPower.setStatus("current")


class _CmcIIIDrcSwController_Type(DisplayString):
    """Custom type cmcIIIDrcSwController based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmcIIIDrcSwController_Type.__name__ = "DisplayString"
_CmcIIIDrcSwController_Object = MibTableColumn
cmcIIIDrcSwController = _CmcIIIDrcSwController_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 17),
    _CmcIIIDrcSwController_Type()
)
cmcIIIDrcSwController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcSwController.setStatus("current")


class _CmcIIIDrcSwBootloader_Type(DisplayString):
    """Custom type cmcIIIDrcSwBootloader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmcIIIDrcSwBootloader_Type.__name__ = "DisplayString"
_CmcIIIDrcSwBootloader_Object = MibTableColumn
cmcIIIDrcSwBootloader = _CmcIIIDrcSwBootloader_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 18),
    _CmcIIIDrcSwBootloader_Type()
)
cmcIIIDrcSwBootloader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcSwBootloader.setStatus("current")


class _CmcIIIDrcFwController_Type(DisplayString):
    """Custom type cmcIIIDrcFwController based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmcIIIDrcFwController_Type.__name__ = "DisplayString"
_CmcIIIDrcFwController_Object = MibTableColumn
cmcIIIDrcFwController = _CmcIIIDrcFwController_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 19),
    _CmcIIIDrcFwController_Type()
)
cmcIIIDrcFwController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcFwController.setStatus("current")


class _CmcIIIDrcSwAntenna_Type(DisplayString):
    """Custom type cmcIIIDrcSwAntenna based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmcIIIDrcSwAntenna_Type.__name__ = "DisplayString"
_CmcIIIDrcSwAntenna_Object = MibTableColumn
cmcIIIDrcSwAntenna = _CmcIIIDrcSwAntenna_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 20),
    _CmcIIIDrcSwAntenna_Type()
)
cmcIIIDrcSwAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcSwAntenna.setStatus("current")


class _CmcIIIDrcSwAntennaBL_Type(DisplayString):
    """Custom type cmcIIIDrcSwAntennaBL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmcIIIDrcSwAntennaBL_Type.__name__ = "DisplayString"
_CmcIIIDrcSwAntennaBL_Object = MibTableColumn
cmcIIIDrcSwAntennaBL = _CmcIIIDrcSwAntennaBL_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 21),
    _CmcIIIDrcSwAntennaBL_Type()
)
cmcIIIDrcSwAntennaBL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIDrcSwAntennaBL.setStatus("current")


class _CmcIIIDrcCommand_Type(Integer32):
    """Custom type cmcIIIDrcCommand based on Integer32"""
    defaultValue = 1

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
        *(("ledAuto", 3),
          ("ledOnFreeRU", 5),
          ("ledOnOccupied", 4),
          ("noQuit", 1),
          ("quit", 2))
    )


_CmcIIIDrcCommand_Type.__name__ = "Integer32"
_CmcIIIDrcCommand_Object = MibTableColumn
cmcIIIDrcCommand = _CmcIIIDrcCommand_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 2, 1, 22),
    _CmcIIIDrcCommand_Type()
)
cmcIIIDrcCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIDrcCommand.setStatus("current")
_CmcIIITagTable_Object = MibTable
cmcIIITagTable = _CmcIIITagTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3)
)
if mibBuilder.loadTexts:
    cmcIIITagTable.setStatus("current")
_CmcIIITagEntry_Object = MibTableRow
cmcIIITagEntry = _CmcIIITagEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1)
)
cmcIIITagEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIITagDrcIndex"),
    (0, "RITTAL-CMC-III-MIB", "cmcIIITagRuIndex"),
)
if mibBuilder.loadTexts:
    cmcIIITagEntry.setStatus("current")


class _CmcIIITagDrcIndex_Type(Unsigned32):
    """Custom type cmcIIITagDrcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIITagDrcIndex_Type.__name__ = "Unsigned32"
_CmcIIITagDrcIndex_Object = MibTableColumn
cmcIIITagDrcIndex = _CmcIIITagDrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 1),
    _CmcIIITagDrcIndex_Type()
)
cmcIIITagDrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIITagDrcIndex.setStatus("current")


class _CmcIIITagRuIndex_Type(Unsigned32):
    """Custom type cmcIIITagRuIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIITagRuIndex_Type.__name__ = "Unsigned32"
_CmcIIITagRuIndex_Object = MibTableColumn
cmcIIITagRuIndex = _CmcIIITagRuIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 2),
    _CmcIIITagRuIndex_Type()
)
cmcIIITagRuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIITagRuIndex.setStatus("current")


class _CmcIIITagStatus_Type(Integer32):
    """Custom type cmcIIITagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              17,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 5),
          ("configChanged", 2),
          ("detected", 22),
          ("error", 3),
          ("lost", 21),
          ("notAvail", 1),
          ("ok", 4),
          ("service", 17))
    )


_CmcIIITagStatus_Type.__name__ = "Integer32"
_CmcIIITagStatus_Object = MibTableColumn
cmcIIITagStatus = _CmcIIITagStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 3),
    _CmcIIITagStatus_Type()
)
cmcIIITagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIITagStatus.setStatus("current")


class _CmcIIITagUID_Type(DisplayString):
    """Custom type cmcIIITagUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmcIIITagUID_Type.__name__ = "DisplayString"
_CmcIIITagUID_Object = MibTableColumn
cmcIIITagUID = _CmcIIITagUID_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 4),
    _CmcIIITagUID_Type()
)
cmcIIITagUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIITagUID.setStatus("current")


class _CmcIIITagPosition_Type(Unsigned32):
    """Custom type cmcIIITagPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CmcIIITagPosition_Type.__name__ = "Unsigned32"
_CmcIIITagPosition_Object = MibTableColumn
cmcIIITagPosition = _CmcIIITagPosition_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 5),
    _CmcIIITagPosition_Type()
)
cmcIIITagPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIITagPosition.setStatus("current")


class _CmcIIITagUnitFormfactor_Type(Unsigned32):
    """Custom type cmcIIITagUnitFormfactor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CmcIIITagUnitFormfactor_Type.__name__ = "Unsigned32"
_CmcIIITagUnitFormfactor_Object = MibTableColumn
cmcIIITagUnitFormfactor = _CmcIIITagUnitFormfactor_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 6),
    _CmcIIITagUnitFormfactor_Type()
)
cmcIIITagUnitFormfactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagUnitFormfactor.setStatus("current")


class _CmcIIITagOffset_Type(Unsigned32):
    """Custom type cmcIIITagOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CmcIIITagOffset_Type.__name__ = "Unsigned32"
_CmcIIITagOffset_Object = MibTableColumn
cmcIIITagOffset = _CmcIIITagOffset_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 7),
    _CmcIIITagOffset_Type()
)
cmcIIITagOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagOffset.setStatus("current")


class _CmcIIITagRuPosition_Type(Unsigned32):
    """Custom type cmcIIITagRuPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CmcIIITagRuPosition_Type.__name__ = "Unsigned32"
_CmcIIITagRuPosition_Object = MibTableColumn
cmcIIITagRuPosition = _CmcIIITagRuPosition_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 8),
    _CmcIIITagRuPosition_Type()
)
cmcIIITagRuPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIITagRuPosition.setStatus("current")


class _CmcIIITagDeviceClass_Type(Integer32):
    """Custom type cmcIIITagDeviceClass based on Integer32"""
    defaultValue = 1

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
              14)
        )
    )
    namedValues = NamedValues(
        *(("blankingPlate", 2),
          ("cableRouting", 4),
          ("componentShelf", 3),
          ("kvm", 9),
          ("monitor", 12),
          ("monitorKeyboardDrawer", 11),
          ("notDefined", 1),
          ("patchPanelCatX", 5),
          ("patchPanelFibreOptic", 6),
          ("powerSupply", 8),
          ("server", 13),
          ("storage", 14),
          ("switch", 10),
          ("ups", 7))
    )


_CmcIIITagDeviceClass_Type.__name__ = "Integer32"
_CmcIIITagDeviceClass_Object = MibTableColumn
cmcIIITagDeviceClass = _CmcIIITagDeviceClass_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 9),
    _CmcIIITagDeviceClass_Type()
)
cmcIIITagDeviceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagDeviceClass.setStatus("current")


class _CmcIIITagDescName_Type(DisplayString):
    """Custom type cmcIIITagDescName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmcIIITagDescName_Type.__name__ = "DisplayString"
_CmcIIITagDescName_Object = MibTableColumn
cmcIIITagDescName = _CmcIIITagDescName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 10),
    _CmcIIITagDescName_Type()
)
cmcIIITagDescName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagDescName.setStatus("current")


class _CmcIIITagManufacturer_Type(DisplayString):
    """Custom type cmcIIITagManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmcIIITagManufacturer_Type.__name__ = "DisplayString"
_CmcIIITagManufacturer_Object = MibTableColumn
cmcIIITagManufacturer = _CmcIIITagManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 11),
    _CmcIIITagManufacturer_Type()
)
cmcIIITagManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagManufacturer.setStatus("current")


class _CmcIIITagType_Type(DisplayString):
    """Custom type cmcIIITagType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmcIIITagType_Type.__name__ = "DisplayString"
_CmcIIITagType_Object = MibTableColumn
cmcIIITagType = _CmcIIITagType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 12),
    _CmcIIITagType_Type()
)
cmcIIITagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagType.setStatus("current")


class _CmcIIITagSerialNumber_Type(DisplayString):
    """Custom type cmcIIITagSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmcIIITagSerialNumber_Type.__name__ = "DisplayString"
_CmcIIITagSerialNumber_Object = MibTableColumn
cmcIIITagSerialNumber = _CmcIIITagSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 13),
    _CmcIIITagSerialNumber_Type()
)
cmcIIITagSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagSerialNumber.setStatus("current")


class _CmcIIITagVendor_Type(DisplayString):
    """Custom type cmcIIITagVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmcIIITagVendor_Type.__name__ = "DisplayString"
_CmcIIITagVendor_Object = MibTableColumn
cmcIIITagVendor = _CmcIIITagVendor_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 14),
    _CmcIIITagVendor_Type()
)
cmcIIITagVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagVendor.setStatus("current")


class _CmcIIITagMac1_Type(DisplayString):
    """Custom type cmcIIITagMac1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CmcIIITagMac1_Type.__name__ = "DisplayString"
_CmcIIITagMac1_Object = MibTableColumn
cmcIIITagMac1 = _CmcIIITagMac1_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 15),
    _CmcIIITagMac1_Type()
)
cmcIIITagMac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagMac1.setStatus("current")


class _CmcIIITagMac2_Type(DisplayString):
    """Custom type cmcIIITagMac2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CmcIIITagMac2_Type.__name__ = "DisplayString"
_CmcIIITagMac2_Object = MibTableColumn
cmcIIITagMac2 = _CmcIIITagMac2_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 16),
    _CmcIIITagMac2_Type()
)
cmcIIITagMac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagMac2.setStatus("current")


class _CmcIIITagService_Type(DisplayString):
    """Custom type cmcIIITagService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmcIIITagService_Type.__name__ = "DisplayString"
_CmcIIITagService_Object = MibTableColumn
cmcIIITagService = _CmcIIITagService_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 17),
    _CmcIIITagService_Type()
)
cmcIIITagService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagService.setStatus("current")


class _CmcIIITagDeviceName_Type(DisplayString):
    """Custom type cmcIIITagDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmcIIITagDeviceName_Type.__name__ = "DisplayString"
_CmcIIITagDeviceName_Object = MibTableColumn
cmcIIITagDeviceName = _CmcIIITagDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 18),
    _CmcIIITagDeviceName_Type()
)
cmcIIITagDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagDeviceName.setStatus("current")


class _CmcIIITagInventoryCode_Type(DisplayString):
    """Custom type cmcIIITagInventoryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CmcIIITagInventoryCode_Type.__name__ = "DisplayString"
_CmcIIITagInventoryCode_Object = MibTableColumn
cmcIIITagInventoryCode = _CmcIIITagInventoryCode_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 19),
    _CmcIIITagInventoryCode_Type()
)
cmcIIITagInventoryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagInventoryCode.setStatus("current")
_CmcIIITagPower_Type = Unsigned32
_CmcIIITagPower_Object = MibTableColumn
cmcIIITagPower = _CmcIIITagPower_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 20),
    _CmcIIITagPower_Type()
)
cmcIIITagPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagPower.setStatus("current")
_CmcIIITagCurrent_Type = Unsigned32
_CmcIIITagCurrent_Object = MibTableColumn
cmcIIITagCurrent = _CmcIIITagCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 21),
    _CmcIIITagCurrent_Type()
)
cmcIIITagCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagCurrent.setStatus("current")
_CmcIIITagVoltage_Type = Unsigned32
_CmcIIITagVoltage_Object = MibTableColumn
cmcIIITagVoltage = _CmcIIITagVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 22),
    _CmcIIITagVoltage_Type()
)
cmcIIITagVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagVoltage.setStatus("current")


class _CmcIIITagLastService_Type(DisplayString):
    """Custom type cmcIIITagLastService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIITagLastService_Type.__name__ = "DisplayString"
_CmcIIITagLastService_Object = MibTableColumn
cmcIIITagLastService = _CmcIIITagLastService_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 23),
    _CmcIIITagLastService_Type()
)
cmcIIITagLastService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagLastService.setStatus("current")


class _CmcIIITagNextService_Type(DisplayString):
    """Custom type cmcIIITagNextService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIITagNextService_Type.__name__ = "DisplayString"
_CmcIIITagNextService_Object = MibTableColumn
cmcIIITagNextService = _CmcIIITagNextService_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 24),
    _CmcIIITagNextService_Type()
)
cmcIIITagNextService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagNextService.setStatus("current")


class _CmcIIITagLastUpdate_Type(DisplayString):
    """Custom type cmcIIITagLastUpdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmcIIITagLastUpdate_Type.__name__ = "DisplayString"
_CmcIIITagLastUpdate_Object = MibTableColumn
cmcIIITagLastUpdate = _CmcIIITagLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 25),
    _CmcIIITagLastUpdate_Type()
)
cmcIIITagLastUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagLastUpdate.setStatus("current")


class _CmcIIITagNextUpdate_Type(DisplayString):
    """Custom type cmcIIITagNextUpdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmcIIITagNextUpdate_Type.__name__ = "DisplayString"
_CmcIIITagNextUpdate_Object = MibTableColumn
cmcIIITagNextUpdate = _CmcIIITagNextUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 26),
    _CmcIIITagNextUpdate_Type()
)
cmcIIITagNextUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagNextUpdate.setStatus("current")


class _CmcIIITagInitialStart_Type(DisplayString):
    """Custom type cmcIIITagInitialStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmcIIITagInitialStart_Type.__name__ = "DisplayString"
_CmcIIITagInitialStart_Object = MibTableColumn
cmcIIITagInitialStart = _CmcIIITagInitialStart_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 27),
    _CmcIIITagInitialStart_Type()
)
cmcIIITagInitialStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagInitialStart.setStatus("current")


class _CmcIIITagCustom_Type(DisplayString):
    """Custom type cmcIIITagCustom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIITagCustom_Type.__name__ = "DisplayString"
_CmcIIITagCustom_Object = MibTableColumn
cmcIIITagCustom = _CmcIIITagCustom_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 28),
    _CmcIIITagCustom_Type()
)
cmcIIITagCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagCustom.setStatus("current")


class _CmcIIITagCommand_Type(Integer32):
    """Custom type cmcIIITagCommand based on Integer32"""
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
        *(("ledAuto", 3),
          ("ledOn", 4),
          ("noQuit", 1),
          ("quit", 2))
    )


_CmcIIITagCommand_Type.__name__ = "Integer32"
_CmcIIITagCommand_Object = MibTableColumn
cmcIIITagCommand = _CmcIIITagCommand_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 29),
    _CmcIIITagCommand_Type()
)
cmcIIITagCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIITagCommand.setStatus("current")
_CmcIIITagStart_Type = Unsigned32
_CmcIIITagStart_Object = MibTableColumn
cmcIIITagStart = _CmcIIITagStart_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 30),
    _CmcIIITagStart_Type()
)
cmcIIITagStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIITagStart.setStatus("current")
_CmcIIITagEnd_Type = Unsigned32
_CmcIIITagEnd_Object = MibTableColumn
cmcIIITagEnd = _CmcIIITagEnd_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 31),
    _CmcIIITagEnd_Type()
)
cmcIIITagEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIITagEnd.setStatus("current")
_CmcIIITagAntennaMap_Type = Unsigned32
_CmcIIITagAntennaMap_Object = MibTableColumn
cmcIIITagAntennaMap = _CmcIIITagAntennaMap_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 4, 3, 1, 32),
    _CmcIIITagAntennaMap_Type()
)
cmcIIITagAntennaMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIITagAntennaMap.setStatus("current")
_CmcIIIFiles_ObjectIdentity = ObjectIdentity
cmcIIIFiles = _CmcIIIFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5)
)
_CmcIIIFileInfo_ObjectIdentity = ObjectIdentity
cmcIIIFileInfo = _CmcIIIFileInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 1)
)
_CmcIIINumberOfFiles_Type = Unsigned32
_CmcIIINumberOfFiles_Object = MibScalar
cmcIIINumberOfFiles = _CmcIIINumberOfFiles_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 1, 1),
    _CmcIIINumberOfFiles_Type()
)
cmcIIINumberOfFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIINumberOfFiles.setStatus("current")
_CmcIIILastChangeFiles_Type = Unsigned32
_CmcIIILastChangeFiles_Object = MibScalar
cmcIIILastChangeFiles = _CmcIIILastChangeFiles_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 1, 2),
    _CmcIIILastChangeFiles_Type()
)
cmcIIILastChangeFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeFiles.setStatus("current")
_CmcIIILastChangeNumberOfFiles_Type = Unsigned32
_CmcIIILastChangeNumberOfFiles_Object = MibScalar
cmcIIILastChangeNumberOfFiles = _CmcIIILastChangeNumberOfFiles_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 1, 3),
    _CmcIIILastChangeNumberOfFiles_Type()
)
cmcIIILastChangeNumberOfFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeNumberOfFiles.setStatus("current")
_CmcIIIFileTable_Object = MibTable
cmcIIIFileTable = _CmcIIIFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 2)
)
if mibBuilder.loadTexts:
    cmcIIIFileTable.setStatus("current")
_CmcIIIFileEntry_Object = MibTableRow
cmcIIIFileEntry = _CmcIIIFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 2, 1)
)
cmcIIIFileEntry.setIndexNames(
    (0, "RITTAL-CMC-III-MIB", "cmcIIIFileIndex"),
)
if mibBuilder.loadTexts:
    cmcIIIFileEntry.setStatus("current")


class _CmcIIIFileIndex_Type(Unsigned32):
    """Custom type cmcIIIFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcIIIFileIndex_Type.__name__ = "Unsigned32"
_CmcIIIFileIndex_Object = MibTableColumn
cmcIIIFileIndex = _CmcIIIFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 2, 1, 1),
    _CmcIIIFileIndex_Type()
)
cmcIIIFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmcIIIFileIndex.setStatus("current")
_CmcIIILastChangeFile_Type = Unsigned32
_CmcIIILastChangeFile_Object = MibTableColumn
cmcIIILastChangeFile = _CmcIIILastChangeFile_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 2, 1, 2),
    _CmcIIILastChangeFile_Type()
)
cmcIIILastChangeFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIILastChangeFile.setStatus("current")
_CmcIIIFileSize_Type = Unsigned32
_CmcIIIFileSize_Object = MibTableColumn
cmcIIIFileSize = _CmcIIIFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 2, 1, 3),
    _CmcIIIFileSize_Type()
)
cmcIIIFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIFileSize.setStatus("current")
_CmcIIIFileChecksum_Type = Unsigned32
_CmcIIIFileChecksum_Object = MibTableColumn
cmcIIIFileChecksum = _CmcIIIFileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 2, 1, 4),
    _CmcIIIFileChecksum_Type()
)
cmcIIIFileChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIFileChecksum.setStatus("current")


class _CmcIIIFileName_Type(DisplayString):
    """Custom type cmcIIIFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CmcIIIFileName_Type.__name__ = "DisplayString"
_CmcIIIFileName_Object = MibTableColumn
cmcIIIFileName = _CmcIIIFileName_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 4, 5, 2, 1, 5),
    _CmcIIIFileName_Type()
)
cmcIIIFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIIIFileName.setStatus("current")
_CmcIIIControl_ObjectIdentity = ObjectIdentity
cmcIIIControl = _CmcIIIControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 5)
)


class _CmcIIIQuitUnit_Type(Integer32):
    """Custom type cmcIIIQuitUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noQuit", 1),
          ("quit", 2))
    )


_CmcIIIQuitUnit_Type.__name__ = "Integer32"
_CmcIIIQuitUnit_Object = MibScalar
cmcIIIQuitUnit = _CmcIIIQuitUnit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 5, 1),
    _CmcIIIQuitUnit_Type()
)
cmcIIIQuitUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIIQuitUnit.setStatus("current")


class _CmcIIISmsQueue_Type(DisplayString):
    """Custom type cmcIIISmsQueue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_CmcIIISmsQueue_Type.__name__ = "DisplayString"
_CmcIIISmsQueue_Object = MibScalar
cmcIIISmsQueue = _CmcIIISmsQueue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 7, 5, 2),
    _CmcIIISmsQueue_Type()
)
cmcIIISmsQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIIISmsQueue.setStatus("current")
_CmcIIIConformance_ObjectIdentity = ObjectIdentity
cmcIIIConformance = _CmcIIIConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6)
)
_CmcIIIMibCompliances_ObjectIdentity = ObjectIdentity
cmcIIIMibCompliances = _CmcIIIMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 1)
)
_CmcIIIMibGroups_ObjectIdentity = ObjectIdentity
cmcIIIMibGroups = _CmcIIIMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2)
)

# Managed Objects groups

cmcIIITrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 1)
)
cmcIIITrapGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIIDevName"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevAlias"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevStatusText"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgText"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgStatusText"))
)
if mibBuilder.loadTexts:
    cmcIIITrapGroup.setStatus("current")

cmcIIIInfoMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 3)
)
cmcIIIInfoMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIIMibMajRev"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMibMinRev"),
        ("RITTAL-CMC-III-MIB", "cmcIIIAgentRev"),
        ("RITTAL-CMC-III-MIB", "cmcIIICapabilityRev"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitURL"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitHWRev"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitFWRev"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitOSRev"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitSerial"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitProd"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitType"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitCurrentSource"),
        ("RITTAL-CMC-III-MIB", "cmcIIICan0CurrentConsumption"),
        ("RITTAL-CMC-III-MIB", "cmcIIICan1CurrentConsumption"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitUpTime"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitMode"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitLoadAverage"))
)
if mibBuilder.loadTexts:
    cmcIIIInfoMibGroup.setStatus("current")

cmcIIISetupMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 4)
)
cmcIIISetupMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIILastChangeSetup"),
        ("RITTAL-CMC-III-MIB", "cmcIIISetTempUnit"),
        ("RITTAL-CMC-III-MIB", "cmcIIITimeZone"),
        ("RITTAL-CMC-III-MIB", "cmcIIISetupDate"),
        ("RITTAL-CMC-III-MIB", "cmcIIISetupTime"),
        ("RITTAL-CMC-III-MIB", "cmcIIIWebAccess"),
        ("RITTAL-CMC-III-MIB", "cmcIIIHttpPort"),
        ("RITTAL-CMC-III-MIB", "cmcIIIHttpsPort"),
        ("RITTAL-CMC-III-MIB", "cmcIIIFtpAccess"),
        ("RITTAL-CMC-III-MIB", "cmcIIIFtpPort"),
        ("RITTAL-CMC-III-MIB", "cmcIIISshAccess"),
        ("RITTAL-CMC-III-MIB", "cmcIIISshPort"),
        ("RITTAL-CMC-III-MIB", "cmcIIITelnetAccess"),
        ("RITTAL-CMC-III-MIB", "cmcIIITelnetPort"),
        ("RITTAL-CMC-III-MIB", "cmcIIILanguage"),
        ("RITTAL-CMC-III-MIB", "cmcIIIOpcUaAccess"),
        ("RITTAL-CMC-III-MIB", "cmcIIIOpcUaPort"),
        ("RITTAL-CMC-III-MIB", "cmcIIINumberOfTrapReceivers"),
        ("RITTAL-CMC-III-MIB", "cmcIIITrapReceiverStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIITrapReceiverIpAddress"))
)
if mibBuilder.loadTexts:
    cmcIIISetupMibGroup.setStatus("current")

cmcIIIDeviceMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 5)
)
cmcIIIDeviceMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIIOverallDevStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIINumberOfDevs"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeOverallDevStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeNumberOfDevs"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeDevSettings"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeDevs"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevName"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevAlias"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevType"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevNodeID"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevArtNr"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevLocation"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevBus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevPos"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevFW"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevHW"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevSerial"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevProductWeek"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevLastChange"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevURL"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevNumberOfVars"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevNumberOfMsgs"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevStatusText"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevCurrentMinConsumption"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevCurrentMaxConsumption"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevEntPhysicalIndex"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevAssembly"),
        ("RITTAL-CMC-III-MIB", "cmcIIINumberOfVars"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeNumberOfVars"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeVarSettings"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeVars"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarByQualityHide"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDynUpdateRate"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDynUpdateHistory"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarName"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarType"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarUnit"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarDataType"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarScale"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarConstraints"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarSteps"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarValueStr"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarValueInt"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarAccess"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarLastChange"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarQuality"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarEntPhysicalIndex"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarByTypeValueStr"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarByTypeValueInt"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarByTypeLastChange"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarByQualityValueStr"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarByQualityValueInt"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarByQualityLastChange"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarIntDynValue"),
        ("RITTAL-CMC-III-MIB", "cmcIIIVarStrDynValue"),
        ("RITTAL-CMC-III-MIB", "cmcIIIOverallMsgStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIINumberOfMsgs"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeOverallMsgStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeNumberOfMsgs"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeMsgSettings"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgText"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgTrap"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgSMTP"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgQuit"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgDelay"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgSchedAlarmOff"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgQuality"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgVarIdx"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgVarValueIdx"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgStatusText"))
)
if mibBuilder.loadTexts:
    cmcIIIDeviceMibGroup.setStatus("current")

cmcIIIControlMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 6)
)
cmcIIIControlMibGroup.setObjects(
    ("RITTAL-CMC-III-MIB", "cmcIIIQuitUnit")
)
if mibBuilder.loadTexts:
    cmcIIIControlMibGroup.setStatus("current")

cmcIIIRelayMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 7)
)
cmcIIIRelayMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIISetBeeper"),
        ("RITTAL-CMC-III-MIB", "cmcIIIQuitRelay"),
        ("RITTAL-CMC-III-MIB", "cmcIIILogicRelay"),
        ("RITTAL-CMC-III-MIB", "cmcIIIUnitMsgRelay"),
        ("RITTAL-CMC-III-MIB", "cmcIIIFunctionRelay"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgRelay"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgBeeper"))
)
if mibBuilder.loadTexts:
    cmcIIIRelayMibGroup.setStatus("current")

cmcIIISmsMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 8)
)
cmcIIISmsMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIISmsStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmsPIN"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmsService"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmsMSN"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmsPreDial"),
        ("RITTAL-CMC-III-MIB", "cmcIIINumberOfSmsReceivers"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmsReceiverStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmsReceiverNumber"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgSMS"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmsQueue"))
)
if mibBuilder.loadTexts:
    cmcIIISmsMibGroup.setStatus("current")

cmcIIISmtpMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 9)
)
cmcIIISmtpMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIISmtpStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmtpServer"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmtpPort"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmtpAuth"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmtpUsername"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmtpPassword"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmtpSender"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmtpReply"),
        ("RITTAL-CMC-III-MIB", "cmcIIINumberOfSmtpReceivers"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmtpReceiverStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIISmtpReceiverAddress"))
)
if mibBuilder.loadTexts:
    cmcIIISmtpMibGroup.setStatus("current")

cmcIIISyslogMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 10)
)
cmcIIISyslogMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIISysLogStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIISysLogFacility"),
        ("RITTAL-CMC-III-MIB", "cmcIIISysLogServer1"),
        ("RITTAL-CMC-III-MIB", "cmcIIISysLogServer2"))
)
if mibBuilder.loadTexts:
    cmcIIISyslogMibGroup.setStatus("current")

cmcIIITimerMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 11)
)
cmcIIITimerMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIINumberOfTimers"),
        ("RITTAL-CMC-III-MIB", "cmcIIITimerStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIITimerDayOfWeek"),
        ("RITTAL-CMC-III-MIB", "cmcIIITimeOn"),
        ("RITTAL-CMC-III-MIB", "cmcIIITimeOff"),
        ("RITTAL-CMC-III-MIB", "cmcIIITimeControl"),
        ("RITTAL-CMC-III-MIB", "cmcIIITimerFunction"))
)
if mibBuilder.loadTexts:
    cmcIIITimerMibGroup.setStatus("current")

cmcIIILdapMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 12)
)
cmcIIILdapMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIILdapStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIILdapServer"),
        ("RITTAL-CMC-III-MIB", "cmcIIILdapBindDN"),
        ("RITTAL-CMC-III-MIB", "cmcIIILdapBindPW"),
        ("RITTAL-CMC-III-MIB", "cmcIIILdapUserBase"),
        ("RITTAL-CMC-III-MIB", "cmcIIILdapUserSearch"),
        ("RITTAL-CMC-III-MIB", "cmcIIILdapUserAttrib"),
        ("RITTAL-CMC-III-MIB", "cmcIIILdapGroupBase"),
        ("RITTAL-CMC-III-MIB", "cmcIIILdapGroupSearch"),
        ("RITTAL-CMC-III-MIB", "cmcIIILdapGroupAttrib"))
)
if mibBuilder.loadTexts:
    cmcIIILdapMibGroup.setStatus("current")

cmcIIINtpMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 13)
)
cmcIIINtpMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIINtpStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIINtpTimeZone"),
        ("RITTAL-CMC-III-MIB", "cmcIIINtpServer1"),
        ("RITTAL-CMC-III-MIB", "cmcIIINtpServer2"))
)
if mibBuilder.loadTexts:
    cmcIIINtpMibGroup.setStatus("current")

cmcIIIShutdownMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 14)
)
cmcIIIShutdownMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIINumberOfShutdowns"),
        ("RITTAL-CMC-III-MIB", "cmcIIIShutdownServer"),
        ("RITTAL-CMC-III-MIB", "cmcIIIShutdownName"),
        ("RITTAL-CMC-III-MIB", "cmcIIIShutdownPort"),
        ("RITTAL-CMC-III-MIB", "cmcIIIShutdownDelay"),
        ("RITTAL-CMC-III-MIB", "cmcIIIShutdownEnabled"))
)
if mibBuilder.loadTexts:
    cmcIIIShutdownMibGroup.setStatus("current")

cmcIIIModbusMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 15)
)
cmcIIIModbusMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIIModbusStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIModbusPort"),
        ("RITTAL-CMC-III-MIB", "cmcIIINumberOfModbusSources"),
        ("RITTAL-CMC-III-MIB", "cmcIIIModbusAccess"),
        ("RITTAL-CMC-III-MIB", "cmcIIIModbusSource"))
)
if mibBuilder.loadTexts:
    cmcIIIModbusMibGroup.setStatus("current")

cmcIIIDrcMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 16)
)
cmcIIIDrcMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIIOverallDrcStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIINumberOfDrcs"),
        ("RITTAL-CMC-III-MIB", "cmcIIIOverallLastChangeDrcStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeNumberOfDrcs"),
        ("RITTAL-CMC-III-MIB", "cmcIIIOverallDrcUtilization"),
        ("RITTAL-CMC-III-MIB", "cmcIIIOverallDrcPower"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeDrcStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcUnitName"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcLocation"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcBuilding"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcLevel"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcRoom"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcRow"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcRackNr"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcMfgDate"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcSerialNr"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcOpHours"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcNumberOfRU"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcUtilization"),
        ("RITTAL-CMC-III-MIB", "cmcIIITotalDrcPower"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcSwController"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcSwBootloader"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcFwController"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcSwAntenna"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcSwAntennaBL"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDrcCommand"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagUID"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagPosition"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagUnitFormfactor"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagOffset"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagRuPosition"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagDeviceClass"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagDescName"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagManufacturer"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagType"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagSerialNumber"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagVendor"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagMac1"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagMac2"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagService"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagDeviceName"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagInventoryCode"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagPower"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagCurrent"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagVoltage"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagLastService"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagNextService"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagLastUpdate"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagNextUpdate"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagInitialStart"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagCustom"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagCommand"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagStart"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagEnd"),
        ("RITTAL-CMC-III-MIB", "cmcIIITagAntennaMap"))
)
if mibBuilder.loadTexts:
    cmcIIIDrcMibGroup.setStatus("current")

cmcIIIFileMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 17)
)
cmcIIIFileMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIINumberOfFiles"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeFiles"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeNumberOfFiles"),
        ("RITTAL-CMC-III-MIB", "cmcIIILastChangeFile"),
        ("RITTAL-CMC-III-MIB", "cmcIIIFileSize"),
        ("RITTAL-CMC-III-MIB", "cmcIIIFileChecksum"),
        ("RITTAL-CMC-III-MIB", "cmcIIIFileName"))
)
if mibBuilder.loadTexts:
    cmcIIIFileMibGroup.setStatus("current")

cmcIIIRadiusMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 18)
)
cmcIIIRadiusMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIIRadiusStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIRadiusServer"),
        ("RITTAL-CMC-III-MIB", "cmcIIIRadiusPort"),
        ("RITTAL-CMC-III-MIB", "cmcIIIRadiusPassword"),
        ("RITTAL-CMC-III-MIB", "cmcIIIRadiusGroupMode"),
        ("RITTAL-CMC-III-MIB", "cmcIIIRadiusGroupId"),
        ("RITTAL-CMC-III-MIB", "cmcIIIRadiusAuth"))
)
if mibBuilder.loadTexts:
    cmcIIIRadiusMibGroup.setStatus("current")

cmcIIIWebCamMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 19)
)
cmcIIIWebCamMibGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIIWebCamStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIWebCamServer"),
        ("RITTAL-CMC-III-MIB", "cmcIIIWebCamUsername"),
        ("RITTAL-CMC-III-MIB", "cmcIIIWebCamPassword"),
        ("RITTAL-CMC-III-MIB", "cmcIIIWebCamIntervall"),
        ("RITTAL-CMC-III-MIB", "cmcIIIWebCamNumberofImages"),
        ("RITTAL-CMC-III-MIB", "cmcIIIWebCamDestination"))
)
if mibBuilder.loadTexts:
    cmcIIIWebCamMibGroup.setStatus("current")


# Notification objects

alarmSensorDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 7, 0, 1)
)
alarmSensorDevice.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIIDevName"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgText"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIMsgStatusText"))
)
if mibBuilder.loadTexts:
    alarmSensorDevice.setStatus(
        "current"
    )

alarmDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 7, 0, 2)
)
alarmDevice.setObjects(
      *(("RITTAL-CMC-III-MIB", "cmcIIIDevName"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevAlias"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevStatus"),
        ("RITTAL-CMC-III-MIB", "cmcIIIDevStatusText"))
)
if mibBuilder.loadTexts:
    alarmDevice.setStatus(
        "current"
    )

reConfigAgent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 7, 0, 3)
)
reConfigAgent.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    reConfigAgent.setStatus(
        "current"
    )

shutdownAgent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 7, 0, 4)
)
shutdownAgent.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    shutdownAgent.setStatus(
        "current"
    )


# Notifications groups

cmcIIINotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 2, 2)
)
cmcIIINotificationGroup.setObjects(
      *(("RITTAL-CMC-III-MIB", "alarmSensorDevice"),
        ("RITTAL-CMC-III-MIB", "alarmDevice"),
        ("RITTAL-CMC-III-MIB", "reConfigAgent"),
        ("RITTAL-CMC-III-MIB", "shutdownAgent"))
)
if mibBuilder.loadTexts:
    cmcIIINotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmcIIIMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2606, 7, 6, 1, 1)
)
if mibBuilder.loadTexts:
    cmcIIIMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RITTAL-CMC-III-MIB",
    **{"cmcIII": cmcIII,
       "cmcIIINotifications": cmcIIINotifications,
       "alarmSensorDevice": alarmSensorDevice,
       "alarmDevice": alarmDevice,
       "reConfigAgent": reConfigAgent,
       "shutdownAgent": shutdownAgent,
       "cmcIIIMibRev": cmcIIIMibRev,
       "cmcIIIMibMajRev": cmcIIIMibMajRev,
       "cmcIIIMibMinRev": cmcIIIMibMinRev,
       "cmcIIIAgentRev": cmcIIIAgentRev,
       "cmcIIICapabilityRev": cmcIIICapabilityRev,
       "cmcIIIUnit": cmcIIIUnit,
       "cmcIIIUnitStatus": cmcIIIUnitStatus,
       "cmcIIIUnitURL": cmcIIIUnitURL,
       "cmcIIIUnitHWRev": cmcIIIUnitHWRev,
       "cmcIIIUnitFWRev": cmcIIIUnitFWRev,
       "cmcIIIUnitOSRev": cmcIIIUnitOSRev,
       "cmcIIIUnitSerial": cmcIIIUnitSerial,
       "cmcIIIUnitProd": cmcIIIUnitProd,
       "cmcIIIUnitType": cmcIIIUnitType,
       "cmcIIIUnitCurrentSource": cmcIIIUnitCurrentSource,
       "cmcIIICan0CurrentConsumption": cmcIIICan0CurrentConsumption,
       "cmcIIICan1CurrentConsumption": cmcIIICan1CurrentConsumption,
       "cmcIIIUnitUpTime": cmcIIIUnitUpTime,
       "cmcIIIUnitMode": cmcIIIUnitMode,
       "cmcIIIUnitLoadTable": cmcIIIUnitLoadTable,
       "cmcIIIUnitLoadEntry": cmcIIIUnitLoadEntry,
       "cmcIIIUnitLoadIndex": cmcIIIUnitLoadIndex,
       "cmcIIIUnitLoadAverage": cmcIIIUnitLoadAverage,
       "cmcIIISetup": cmcIIISetup,
       "cmcIIILastChangeSetup": cmcIIILastChangeSetup,
       "cmcIIISetupGeneral": cmcIIISetupGeneral,
       "cmcIIISetTempUnit": cmcIIISetTempUnit,
       "cmcIIISetBeeper": cmcIIISetBeeper,
       "cmcIIIQuitRelay": cmcIIIQuitRelay,
       "cmcIIILogicRelay": cmcIIILogicRelay,
       "cmcIIIUnitMsgRelay": cmcIIIUnitMsgRelay,
       "cmcIIIFunctionRelay": cmcIIIFunctionRelay,
       "cmcIIITimeZone": cmcIIITimeZone,
       "cmcIIISetupDate": cmcIIISetupDate,
       "cmcIIISetupTime": cmcIIISetupTime,
       "cmcIIIWebAccess": cmcIIIWebAccess,
       "cmcIIIHttpPort": cmcIIIHttpPort,
       "cmcIIIHttpsPort": cmcIIIHttpsPort,
       "cmcIIIFtpAccess": cmcIIIFtpAccess,
       "cmcIIIFtpPort": cmcIIIFtpPort,
       "cmcIIISshAccess": cmcIIISshAccess,
       "cmcIIISshPort": cmcIIISshPort,
       "cmcIIITelnetAccess": cmcIIITelnetAccess,
       "cmcIIITelnetPort": cmcIIITelnetPort,
       "cmcIIILanguage": cmcIIILanguage,
       "cmcIIIOpcUaAccess": cmcIIIOpcUaAccess,
       "cmcIIIOpcUaPort": cmcIIIOpcUaPort,
       "cmcIIISetupTimer": cmcIIISetupTimer,
       "cmcIIINumberOfTimers": cmcIIINumberOfTimers,
       "cmcIIITimerTable": cmcIIITimerTable,
       "cmcIIITimerEntry": cmcIIITimerEntry,
       "cmcIIITimerIndex": cmcIIITimerIndex,
       "cmcIIITimerStatus": cmcIIITimerStatus,
       "cmcIIITimerDayOfWeek": cmcIIITimerDayOfWeek,
       "cmcIIITimeOn": cmcIIITimeOn,
       "cmcIIITimeOff": cmcIIITimeOff,
       "cmcIIITimeControl": cmcIIITimeControl,
       "cmcIIITimerFunction": cmcIIITimerFunction,
       "cmcIIISetupTrap": cmcIIISetupTrap,
       "cmcIIINumberOfTrapReceivers": cmcIIINumberOfTrapReceivers,
       "cmcIIITrapReceiverTable": cmcIIITrapReceiverTable,
       "cmcIIITrapReceiverEntry": cmcIIITrapReceiverEntry,
       "cmcIIITrapReceiverIndex": cmcIIITrapReceiverIndex,
       "cmcIIITrapReceiverStatus": cmcIIITrapReceiverStatus,
       "cmcIIITrapReceiverIpAddress": cmcIIITrapReceiverIpAddress,
       "cmcIIISetupSMTP": cmcIIISetupSMTP,
       "cmcIIISmtpStatus": cmcIIISmtpStatus,
       "cmcIIISmtpServer": cmcIIISmtpServer,
       "cmcIIISmtpPort": cmcIIISmtpPort,
       "cmcIIISmtpAuth": cmcIIISmtpAuth,
       "cmcIIISmtpUsername": cmcIIISmtpUsername,
       "cmcIIISmtpPassword": cmcIIISmtpPassword,
       "cmcIIISmtpSender": cmcIIISmtpSender,
       "cmcIIISmtpReply": cmcIIISmtpReply,
       "cmcIIINumberOfSmtpReceivers": cmcIIINumberOfSmtpReceivers,
       "cmcIIISmtpReceiverTable": cmcIIISmtpReceiverTable,
       "cmcIIISmtpReceiverEntry": cmcIIISmtpReceiverEntry,
       "cmcIIISmtpReceiverIndex": cmcIIISmtpReceiverIndex,
       "cmcIIISmtpReceiverStatus": cmcIIISmtpReceiverStatus,
       "cmcIIISmtpReceiverAddress": cmcIIISmtpReceiverAddress,
       "cmcIIISetupSMS": cmcIIISetupSMS,
       "cmcIIISmsStatus": cmcIIISmsStatus,
       "cmcIIISmsPIN": cmcIIISmsPIN,
       "cmcIIISmsService": cmcIIISmsService,
       "cmcIIISmsMSN": cmcIIISmsMSN,
       "cmcIIISmsPreDial": cmcIIISmsPreDial,
       "cmcIIINumberOfSmsReceivers": cmcIIINumberOfSmsReceivers,
       "cmcIIISmsReceiverTable": cmcIIISmsReceiverTable,
       "cmcIIISmsReceiverEntry": cmcIIISmsReceiverEntry,
       "cmcIIISmsReceiverIndex": cmcIIISmsReceiverIndex,
       "cmcIIISmsReceiverStatus": cmcIIISmsReceiverStatus,
       "cmcIIISmsReceiverNumber": cmcIIISmsReceiverNumber,
       "cmcIIISetupSysLog": cmcIIISetupSysLog,
       "cmcIIISysLogStatus": cmcIIISysLogStatus,
       "cmcIIISysLogFacility": cmcIIISysLogFacility,
       "cmcIIISysLogServer1": cmcIIISysLogServer1,
       "cmcIIISysLogServer2": cmcIIISysLogServer2,
       "cmcIIISetupNTP": cmcIIISetupNTP,
       "cmcIIINtpStatus": cmcIIINtpStatus,
       "cmcIIINtpTimeZone": cmcIIINtpTimeZone,
       "cmcIIINtpServer1": cmcIIINtpServer1,
       "cmcIIINtpServer2": cmcIIINtpServer2,
       "cmcIIISetupLDAP": cmcIIISetupLDAP,
       "cmcIIILdapStatus": cmcIIILdapStatus,
       "cmcIIILdapServer": cmcIIILdapServer,
       "cmcIIILdapBindDN": cmcIIILdapBindDN,
       "cmcIIILdapBindPW": cmcIIILdapBindPW,
       "cmcIIILdapUserBase": cmcIIILdapUserBase,
       "cmcIIILdapUserSearch": cmcIIILdapUserSearch,
       "cmcIIILdapUserAttrib": cmcIIILdapUserAttrib,
       "cmcIIILdapGroupBase": cmcIIILdapGroupBase,
       "cmcIIILdapGroupSearch": cmcIIILdapGroupSearch,
       "cmcIIILdapGroupAttrib": cmcIIILdapGroupAttrib,
       "cmcIIISetupShutdown": cmcIIISetupShutdown,
       "cmcIIINumberOfShutdowns": cmcIIINumberOfShutdowns,
       "cmcIIIShutdownTable": cmcIIIShutdownTable,
       "cmcIIIShutdownEntry": cmcIIIShutdownEntry,
       "cmcIIIShutdownIndex": cmcIIIShutdownIndex,
       "cmcIIIShutdownServer": cmcIIIShutdownServer,
       "cmcIIIShutdownName": cmcIIIShutdownName,
       "cmcIIIShutdownPort": cmcIIIShutdownPort,
       "cmcIIIShutdownDelay": cmcIIIShutdownDelay,
       "cmcIIIShutdownEnabled": cmcIIIShutdownEnabled,
       "cmcIIISetupModbus": cmcIIISetupModbus,
       "cmcIIIModbusStatus": cmcIIIModbusStatus,
       "cmcIIIModbusPort": cmcIIIModbusPort,
       "cmcIIINumberOfModbusSources": cmcIIINumberOfModbusSources,
       "cmcIIIModbusTable": cmcIIIModbusTable,
       "cmcIIIModbusEntry": cmcIIIModbusEntry,
       "cmcIIIModbusIndex": cmcIIIModbusIndex,
       "cmcIIIModbusAccess": cmcIIIModbusAccess,
       "cmcIIIModbusSource": cmcIIIModbusSource,
       "cmcIIISetupRadius": cmcIIISetupRadius,
       "cmcIIIRadiusStatus": cmcIIIRadiusStatus,
       "cmcIIIRadiusServer": cmcIIIRadiusServer,
       "cmcIIIRadiusPort": cmcIIIRadiusPort,
       "cmcIIIRadiusPassword": cmcIIIRadiusPassword,
       "cmcIIIRadiusGroupMode": cmcIIIRadiusGroupMode,
       "cmcIIIRadiusGroupId": cmcIIIRadiusGroupId,
       "cmcIIIRadiusAuth": cmcIIIRadiusAuth,
       "cmcIIISetupWebCam": cmcIIISetupWebCam,
       "cmcIIIWebCamStatus": cmcIIIWebCamStatus,
       "cmcIIIWebCamServer": cmcIIIWebCamServer,
       "cmcIIIWebCamUsername": cmcIIIWebCamUsername,
       "cmcIIIWebCamPassword": cmcIIIWebCamPassword,
       "cmcIIIWebCamIntervall": cmcIIIWebCamIntervall,
       "cmcIIIWebCamNumberofImages": cmcIIIWebCamNumberofImages,
       "cmcIIIWebCamDestination": cmcIIIWebCamDestination,
       "cmcIIIDevice": cmcIIIDevice,
       "cmcIIIDevs": cmcIIIDevs,
       "cmcIIIDevInfo": cmcIIIDevInfo,
       "cmcIIIOverallDevStatus": cmcIIIOverallDevStatus,
       "cmcIIINumberOfDevs": cmcIIINumberOfDevs,
       "cmcIIILastChangeOverallDevStatus": cmcIIILastChangeOverallDevStatus,
       "cmcIIILastChangeNumberOfDevs": cmcIIILastChangeNumberOfDevs,
       "cmcIIILastChangeDevSettings": cmcIIILastChangeDevSettings,
       "cmcIIILastChangeDevs": cmcIIILastChangeDevs,
       "cmcIIIDevTable": cmcIIIDevTable,
       "cmcIIIDevEntry": cmcIIIDevEntry,
       "cmcIIIDevIndex": cmcIIIDevIndex,
       "cmcIIIDevName": cmcIIIDevName,
       "cmcIIIDevAlias": cmcIIIDevAlias,
       "cmcIIIDevType": cmcIIIDevType,
       "cmcIIIDevNodeID": cmcIIIDevNodeID,
       "cmcIIIDevStatus": cmcIIIDevStatus,
       "cmcIIIDevArtNr": cmcIIIDevArtNr,
       "cmcIIIDevLocation": cmcIIIDevLocation,
       "cmcIIIDevBus": cmcIIIDevBus,
       "cmcIIIDevPos": cmcIIIDevPos,
       "cmcIIIDevFW": cmcIIIDevFW,
       "cmcIIIDevHW": cmcIIIDevHW,
       "cmcIIIDevSerial": cmcIIIDevSerial,
       "cmcIIIDevProductWeek": cmcIIIDevProductWeek,
       "cmcIIIDevLastChange": cmcIIIDevLastChange,
       "cmcIIIDevURL": cmcIIIDevURL,
       "cmcIIIDevNumberOfVars": cmcIIIDevNumberOfVars,
       "cmcIIIDevNumberOfMsgs": cmcIIIDevNumberOfMsgs,
       "cmcIIIDevStatusText": cmcIIIDevStatusText,
       "cmcIIIDevCurrentMinConsumption": cmcIIIDevCurrentMinConsumption,
       "cmcIIIDevCurrentMaxConsumption": cmcIIIDevCurrentMaxConsumption,
       "cmcIIIDevEntPhysicalIndex": cmcIIIDevEntPhysicalIndex,
       "cmcIIIDevAssembly": cmcIIIDevAssembly,
       "cmcIIIVars": cmcIIIVars,
       "cmcIIIVarInfo": cmcIIIVarInfo,
       "cmcIIINumberOfVars": cmcIIINumberOfVars,
       "cmcIIILastChangeNumberOfVars": cmcIIILastChangeNumberOfVars,
       "cmcIIILastChangeVarSettings": cmcIIILastChangeVarSettings,
       "cmcIIILastChangeVars": cmcIIILastChangeVars,
       "cmcIIIVarByQualityHide": cmcIIIVarByQualityHide,
       "cmcIIIDynUpdateRate": cmcIIIDynUpdateRate,
       "cmcIIIDynUpdateHistory": cmcIIIDynUpdateHistory,
       "cmcIIIVarTable": cmcIIIVarTable,
       "cmcIIIVarEntry": cmcIIIVarEntry,
       "cmcIIIVarDeviceIndex": cmcIIIVarDeviceIndex,
       "cmcIIIVarIndex": cmcIIIVarIndex,
       "cmcIIIVarName": cmcIIIVarName,
       "cmcIIIVarType": cmcIIIVarType,
       "cmcIIIVarUnit": cmcIIIVarUnit,
       "cmcIIIVarDataType": cmcIIIVarDataType,
       "cmcIIIVarScale": cmcIIIVarScale,
       "cmcIIIVarConstraints": cmcIIIVarConstraints,
       "cmcIIIVarSteps": cmcIIIVarSteps,
       "cmcIIIVarValueStr": cmcIIIVarValueStr,
       "cmcIIIVarValueInt": cmcIIIVarValueInt,
       "cmcIIIVarLastChange": cmcIIIVarLastChange,
       "cmcIIIVarAccess": cmcIIIVarAccess,
       "cmcIIIVarQuality": cmcIIIVarQuality,
       "cmcIIIVarEntPhysicalIndex": cmcIIIVarEntPhysicalIndex,
       "cmcIIIVarByTypeTable": cmcIIIVarByTypeTable,
       "cmcIIIVarByTypeEntry": cmcIIIVarByTypeEntry,
       "cmcIIIVarByTypeType": cmcIIIVarByTypeType,
       "cmcIIIVarByTypeDeviceIndex": cmcIIIVarByTypeDeviceIndex,
       "cmcIIIVarByTypeIndex": cmcIIIVarByTypeIndex,
       "cmcIIIVarByTypeValueStr": cmcIIIVarByTypeValueStr,
       "cmcIIIVarByTypeValueInt": cmcIIIVarByTypeValueInt,
       "cmcIIIVarByTypeLastChange": cmcIIIVarByTypeLastChange,
       "cmcIIIVarByQualityTable": cmcIIIVarByQualityTable,
       "cmcIIIVarByQualityEntry": cmcIIIVarByQualityEntry,
       "cmcIIIVarByQualityQuality": cmcIIIVarByQualityQuality,
       "cmcIIIVarByQualityDeviceIndex": cmcIIIVarByQualityDeviceIndex,
       "cmcIIIVarByQualityIndex": cmcIIIVarByQualityIndex,
       "cmcIIIVarByQualityValueStr": cmcIIIVarByQualityValueStr,
       "cmcIIIVarByQualityValueInt": cmcIIIVarByQualityValueInt,
       "cmcIIIVarByQualityLastChange": cmcIIIVarByQualityLastChange,
       "cmcIIIVarIntDynTable": cmcIIIVarIntDynTable,
       "cmcIIIVarIntDynEntry": cmcIIIVarIntDynEntry,
       "cmcIIIVarIntDynDeviceIndex": cmcIIIVarIntDynDeviceIndex,
       "cmcIIIVarIntDynIndex": cmcIIIVarIntDynIndex,
       "cmcIIIVarIntDynLastChange": cmcIIIVarIntDynLastChange,
       "cmcIIIVarIntDynValue": cmcIIIVarIntDynValue,
       "cmcIIIVarStrDynTable": cmcIIIVarStrDynTable,
       "cmcIIIVarStrDynEntry": cmcIIIVarStrDynEntry,
       "cmcIIIVarStrDynDeviceIndex": cmcIIIVarStrDynDeviceIndex,
       "cmcIIIVarStrDynIndex": cmcIIIVarStrDynIndex,
       "cmcIIIVarStrDynLastChange": cmcIIIVarStrDynLastChange,
       "cmcIIIVarStrDynValue": cmcIIIVarStrDynValue,
       "cmcIIIMsgs": cmcIIIMsgs,
       "cmcIIIMsgInfo": cmcIIIMsgInfo,
       "cmcIIIOverallMsgStatus": cmcIIIOverallMsgStatus,
       "cmcIIINumberOfMsgs": cmcIIINumberOfMsgs,
       "cmcIIILastChangeOverallMsgStatus": cmcIIILastChangeOverallMsgStatus,
       "cmcIIILastChangeNumberOfMsgs": cmcIIILastChangeNumberOfMsgs,
       "cmcIIILastChangeMsgSettings": cmcIIILastChangeMsgSettings,
       "cmcIIIMsgTable": cmcIIIMsgTable,
       "cmcIIIMsgEntry": cmcIIIMsgEntry,
       "cmcIIIMsgDeviceIndex": cmcIIIMsgDeviceIndex,
       "cmcIIIMsgIndex": cmcIIIMsgIndex,
       "cmcIIIMsgText": cmcIIIMsgText,
       "cmcIIIMsgStatus": cmcIIIMsgStatus,
       "cmcIIIMsgRelay": cmcIIIMsgRelay,
       "cmcIIIMsgBeeper": cmcIIIMsgBeeper,
       "cmcIIIMsgTrap": cmcIIIMsgTrap,
       "cmcIIIMsgSMTP": cmcIIIMsgSMTP,
       "cmcIIIMsgSMS": cmcIIIMsgSMS,
       "cmcIIIMsgQuit": cmcIIIMsgQuit,
       "cmcIIIMsgDelay": cmcIIIMsgDelay,
       "cmcIIIMsgSchedAlarmOff": cmcIIIMsgSchedAlarmOff,
       "cmcIIIMsgQuality": cmcIIIMsgQuality,
       "cmcIIIMsgVarIdx": cmcIIIMsgVarIdx,
       "cmcIIIMsgVarValueIdx": cmcIIIMsgVarValueIdx,
       "cmcIIIMsgStatusText": cmcIIIMsgStatusText,
       "cmcIIIDrcs": cmcIIIDrcs,
       "cmcIIIDrcInfo": cmcIIIDrcInfo,
       "cmcIIIOverallDrcStatus": cmcIIIOverallDrcStatus,
       "cmcIIINumberOfDrcs": cmcIIINumberOfDrcs,
       "cmcIIIOverallLastChangeDrcStatus": cmcIIIOverallLastChangeDrcStatus,
       "cmcIIILastChangeNumberOfDrcs": cmcIIILastChangeNumberOfDrcs,
       "cmcIIIOverallDrcUtilization": cmcIIIOverallDrcUtilization,
       "cmcIIIOverallDrcPower": cmcIIIOverallDrcPower,
       "cmcIIIDrcTable": cmcIIIDrcTable,
       "cmcIIIDrcEntry": cmcIIIDrcEntry,
       "cmcIIIDrcIndex": cmcIIIDrcIndex,
       "cmcIIIDrcStatus": cmcIIIDrcStatus,
       "cmcIIILastChangeDrcStatus": cmcIIILastChangeDrcStatus,
       "cmcIIIDrcUnitName": cmcIIIDrcUnitName,
       "cmcIIIDrcLocation": cmcIIIDrcLocation,
       "cmcIIIDrcBuilding": cmcIIIDrcBuilding,
       "cmcIIIDrcLevel": cmcIIIDrcLevel,
       "cmcIIIDrcRoom": cmcIIIDrcRoom,
       "cmcIIIDrcRow": cmcIIIDrcRow,
       "cmcIIIDrcRackNr": cmcIIIDrcRackNr,
       "cmcIIIDrcMfgDate": cmcIIIDrcMfgDate,
       "cmcIIIDrcSerialNr": cmcIIIDrcSerialNr,
       "cmcIIIDrcOpHours": cmcIIIDrcOpHours,
       "cmcIIIDrcNumberOfRU": cmcIIIDrcNumberOfRU,
       "cmcIIIDrcUtilization": cmcIIIDrcUtilization,
       "cmcIIITotalDrcPower": cmcIIITotalDrcPower,
       "cmcIIIDrcSwController": cmcIIIDrcSwController,
       "cmcIIIDrcSwBootloader": cmcIIIDrcSwBootloader,
       "cmcIIIDrcFwController": cmcIIIDrcFwController,
       "cmcIIIDrcSwAntenna": cmcIIIDrcSwAntenna,
       "cmcIIIDrcSwAntennaBL": cmcIIIDrcSwAntennaBL,
       "cmcIIIDrcCommand": cmcIIIDrcCommand,
       "cmcIIITagTable": cmcIIITagTable,
       "cmcIIITagEntry": cmcIIITagEntry,
       "cmcIIITagDrcIndex": cmcIIITagDrcIndex,
       "cmcIIITagRuIndex": cmcIIITagRuIndex,
       "cmcIIITagStatus": cmcIIITagStatus,
       "cmcIIITagUID": cmcIIITagUID,
       "cmcIIITagPosition": cmcIIITagPosition,
       "cmcIIITagUnitFormfactor": cmcIIITagUnitFormfactor,
       "cmcIIITagOffset": cmcIIITagOffset,
       "cmcIIITagRuPosition": cmcIIITagRuPosition,
       "cmcIIITagDeviceClass": cmcIIITagDeviceClass,
       "cmcIIITagDescName": cmcIIITagDescName,
       "cmcIIITagManufacturer": cmcIIITagManufacturer,
       "cmcIIITagType": cmcIIITagType,
       "cmcIIITagSerialNumber": cmcIIITagSerialNumber,
       "cmcIIITagVendor": cmcIIITagVendor,
       "cmcIIITagMac1": cmcIIITagMac1,
       "cmcIIITagMac2": cmcIIITagMac2,
       "cmcIIITagService": cmcIIITagService,
       "cmcIIITagDeviceName": cmcIIITagDeviceName,
       "cmcIIITagInventoryCode": cmcIIITagInventoryCode,
       "cmcIIITagPower": cmcIIITagPower,
       "cmcIIITagCurrent": cmcIIITagCurrent,
       "cmcIIITagVoltage": cmcIIITagVoltage,
       "cmcIIITagLastService": cmcIIITagLastService,
       "cmcIIITagNextService": cmcIIITagNextService,
       "cmcIIITagLastUpdate": cmcIIITagLastUpdate,
       "cmcIIITagNextUpdate": cmcIIITagNextUpdate,
       "cmcIIITagInitialStart": cmcIIITagInitialStart,
       "cmcIIITagCustom": cmcIIITagCustom,
       "cmcIIITagCommand": cmcIIITagCommand,
       "cmcIIITagStart": cmcIIITagStart,
       "cmcIIITagEnd": cmcIIITagEnd,
       "cmcIIITagAntennaMap": cmcIIITagAntennaMap,
       "cmcIIIFiles": cmcIIIFiles,
       "cmcIIIFileInfo": cmcIIIFileInfo,
       "cmcIIINumberOfFiles": cmcIIINumberOfFiles,
       "cmcIIILastChangeFiles": cmcIIILastChangeFiles,
       "cmcIIILastChangeNumberOfFiles": cmcIIILastChangeNumberOfFiles,
       "cmcIIIFileTable": cmcIIIFileTable,
       "cmcIIIFileEntry": cmcIIIFileEntry,
       "cmcIIIFileIndex": cmcIIIFileIndex,
       "cmcIIILastChangeFile": cmcIIILastChangeFile,
       "cmcIIIFileSize": cmcIIIFileSize,
       "cmcIIIFileChecksum": cmcIIIFileChecksum,
       "cmcIIIFileName": cmcIIIFileName,
       "cmcIIIControl": cmcIIIControl,
       "cmcIIIQuitUnit": cmcIIIQuitUnit,
       "cmcIIISmsQueue": cmcIIISmsQueue,
       "cmcIIIConformance": cmcIIIConformance,
       "cmcIIIMibCompliances": cmcIIIMibCompliances,
       "cmcIIIMibCompliance": cmcIIIMibCompliance,
       "cmcIIIMibGroups": cmcIIIMibGroups,
       "cmcIIITrapGroup": cmcIIITrapGroup,
       "cmcIIINotificationGroup": cmcIIINotificationGroup,
       "cmcIIIInfoMibGroup": cmcIIIInfoMibGroup,
       "cmcIIISetupMibGroup": cmcIIISetupMibGroup,
       "cmcIIIDeviceMibGroup": cmcIIIDeviceMibGroup,
       "cmcIIIControlMibGroup": cmcIIIControlMibGroup,
       "cmcIIIRelayMibGroup": cmcIIIRelayMibGroup,
       "cmcIIISmsMibGroup": cmcIIISmsMibGroup,
       "cmcIIISmtpMibGroup": cmcIIISmtpMibGroup,
       "cmcIIISyslogMibGroup": cmcIIISyslogMibGroup,
       "cmcIIITimerMibGroup": cmcIIITimerMibGroup,
       "cmcIIILdapMibGroup": cmcIIILdapMibGroup,
       "cmcIIINtpMibGroup": cmcIIINtpMibGroup,
       "cmcIIIShutdownMibGroup": cmcIIIShutdownMibGroup,
       "cmcIIIModbusMibGroup": cmcIIIModbusMibGroup,
       "cmcIIIDrcMibGroup": cmcIIIDrcMibGroup,
       "cmcIIIFileMibGroup": cmcIIIFileMibGroup,
       "cmcIIIRadiusMibGroup": cmcIIIRadiusMibGroup,
       "cmcIIIWebCamMibGroup": cmcIIIWebCamMibGroup}
)
