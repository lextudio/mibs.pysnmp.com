# SNMP MIB module (HPN-ICF-CATV-TRANSCEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-CATV-TRANSCEIVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:33 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfCATVTransceiver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfCATVTransStatus_ObjectIdentity = ObjectIdentity
hpnicfCATVTransStatus = _HpnicfCATVTransStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 1)
)
_HpnicfCATVTransStatusScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfCATVTransStatusScalarObjects = _HpnicfCATVTransStatusScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 1, 1)
)


class _HpnicfCATVTransState_Type(Integer32):
    """Custom type hpnicfCATVTransState based on Integer32"""
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


_HpnicfCATVTransState_Type.__name__ = "Integer32"
_HpnicfCATVTransState_Object = MibScalar
hpnicfCATVTransState = _HpnicfCATVTransState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 1, 1, 1),
    _HpnicfCATVTransState_Type()
)
hpnicfCATVTransState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCATVTransState.setStatus("current")
_HpnicfCATVTransInputPwr_Type = Integer32
_HpnicfCATVTransInputPwr_Object = MibScalar
hpnicfCATVTransInputPwr = _HpnicfCATVTransInputPwr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 1, 1, 2),
    _HpnicfCATVTransInputPwr_Type()
)
hpnicfCATVTransInputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCATVTransInputPwr.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfCATVTransInputPwr.setUnits("dbm")
_HpnicfCATVTransOutputLevel_Type = Integer32
_HpnicfCATVTransOutputLevel_Object = MibScalar
hpnicfCATVTransOutputLevel = _HpnicfCATVTransOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 1, 1, 3),
    _HpnicfCATVTransOutputLevel_Type()
)
hpnicfCATVTransOutputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCATVTransOutputLevel.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfCATVTransOutputLevel.setUnits("dbuv")
_HpnicfCATVTransTemperature_Type = Integer32
_HpnicfCATVTransTemperature_Object = MibScalar
hpnicfCATVTransTemperature = _HpnicfCATVTransTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 1, 1, 4),
    _HpnicfCATVTransTemperature_Type()
)
hpnicfCATVTransTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCATVTransTemperature.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfCATVTransTemperature.setUnits("centigrade")
_HpnicfCATVTransceiverMan_ObjectIdentity = ObjectIdentity
hpnicfCATVTransceiverMan = _HpnicfCATVTransceiverMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 2)
)
_HpnicfCATVTransCtrlScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfCATVTransCtrlScalarObjects = _HpnicfCATVTransCtrlScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 2, 1)
)
_HpnicfCATVTransInputPwrLowerThr_Type = Integer32
_HpnicfCATVTransInputPwrLowerThr_Object = MibScalar
hpnicfCATVTransInputPwrLowerThr = _HpnicfCATVTransInputPwrLowerThr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 2, 1, 1),
    _HpnicfCATVTransInputPwrLowerThr_Type()
)
hpnicfCATVTransInputPwrLowerThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCATVTransInputPwrLowerThr.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfCATVTransInputPwrLowerThr.setUnits("dbm")
_HpnicfCATVTransOutputLvlLowerThr_Type = Integer32
_HpnicfCATVTransOutputLvlLowerThr_Object = MibScalar
hpnicfCATVTransOutputLvlLowerThr = _HpnicfCATVTransOutputLvlLowerThr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 2, 1, 2),
    _HpnicfCATVTransOutputLvlLowerThr_Type()
)
hpnicfCATVTransOutputLvlLowerThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCATVTransOutputLvlLowerThr.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfCATVTransOutputLvlLowerThr.setUnits("dbuv")
_HpnicfCATVTransTempratureUpperThr_Type = Integer32
_HpnicfCATVTransTempratureUpperThr_Object = MibScalar
hpnicfCATVTransTempratureUpperThr = _HpnicfCATVTransTempratureUpperThr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 2, 1, 3),
    _HpnicfCATVTransTempratureUpperThr_Type()
)
hpnicfCATVTransTempratureUpperThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCATVTransTempratureUpperThr.setStatus("current")
_HpnicfCATVTansTrap_ObjectIdentity = ObjectIdentity
hpnicfCATVTansTrap = _HpnicfCATVTansTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 3)
)
_HpnicfCATVTransTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfCATVTransTrapPrefix = _HpnicfCATVTransTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 3, 0)
)

# Managed Objects groups


# Notification objects

hpnicfCATVTransInputPwrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 3, 0, 1)
)
hpnicfCATVTransInputPwrTrap.setObjects(
    ("HPN-ICF-CATV-TRANSCEIVER-MIB", "hpnicfCATVTransInputPwr")
)
if mibBuilder.loadTexts:
    hpnicfCATVTransInputPwrTrap.setStatus(
        "current"
    )

hpnicfCATVTransInputPwrReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 3, 0, 2)
)
hpnicfCATVTransInputPwrReTrap.setObjects(
    ("HPN-ICF-CATV-TRANSCEIVER-MIB", "hpnicfCATVTransInputPwr")
)
if mibBuilder.loadTexts:
    hpnicfCATVTransInputPwrReTrap.setStatus(
        "current"
    )

hpnicfCATVTransOutputLvlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 3, 0, 3)
)
hpnicfCATVTransOutputLvlTrap.setObjects(
    ("HPN-ICF-CATV-TRANSCEIVER-MIB", "hpnicfCATVTransOutputLevel")
)
if mibBuilder.loadTexts:
    hpnicfCATVTransOutputLvlTrap.setStatus(
        "current"
    )

hpnicfCATVTransOutputLvlReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 3, 0, 4)
)
hpnicfCATVTransOutputLvlReTrap.setObjects(
    ("HPN-ICF-CATV-TRANSCEIVER-MIB", "hpnicfCATVTransOutputLevel")
)
if mibBuilder.loadTexts:
    hpnicfCATVTransOutputLvlReTrap.setStatus(
        "current"
    )

hpnicfCATVTransTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 3, 0, 5)
)
hpnicfCATVTransTemperatureTrap.setObjects(
    ("HPN-ICF-CATV-TRANSCEIVER-MIB", "hpnicfCATVTransTemperature")
)
if mibBuilder.loadTexts:
    hpnicfCATVTransTemperatureTrap.setStatus(
        "current"
    )

hpnicfCATVTransTemperatureReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94, 3, 0, 6)
)
hpnicfCATVTransTemperatureReTrap.setObjects(
    ("HPN-ICF-CATV-TRANSCEIVER-MIB", "hpnicfCATVTransTemperature")
)
if mibBuilder.loadTexts:
    hpnicfCATVTransTemperatureReTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-CATV-TRANSCEIVER-MIB",
    **{"hpnicfCATVTransceiver": hpnicfCATVTransceiver,
       "hpnicfCATVTransStatus": hpnicfCATVTransStatus,
       "hpnicfCATVTransStatusScalarObjects": hpnicfCATVTransStatusScalarObjects,
       "hpnicfCATVTransState": hpnicfCATVTransState,
       "hpnicfCATVTransInputPwr": hpnicfCATVTransInputPwr,
       "hpnicfCATVTransOutputLevel": hpnicfCATVTransOutputLevel,
       "hpnicfCATVTransTemperature": hpnicfCATVTransTemperature,
       "hpnicfCATVTransceiverMan": hpnicfCATVTransceiverMan,
       "hpnicfCATVTransCtrlScalarObjects": hpnicfCATVTransCtrlScalarObjects,
       "hpnicfCATVTransInputPwrLowerThr": hpnicfCATVTransInputPwrLowerThr,
       "hpnicfCATVTransOutputLvlLowerThr": hpnicfCATVTransOutputLvlLowerThr,
       "hpnicfCATVTransTempratureUpperThr": hpnicfCATVTransTempratureUpperThr,
       "hpnicfCATVTansTrap": hpnicfCATVTansTrap,
       "hpnicfCATVTransTrapPrefix": hpnicfCATVTransTrapPrefix,
       "hpnicfCATVTransInputPwrTrap": hpnicfCATVTransInputPwrTrap,
       "hpnicfCATVTransInputPwrReTrap": hpnicfCATVTransInputPwrReTrap,
       "hpnicfCATVTransOutputLvlTrap": hpnicfCATVTransOutputLvlTrap,
       "hpnicfCATVTransOutputLvlReTrap": hpnicfCATVTransOutputLvlReTrap,
       "hpnicfCATVTransTemperatureTrap": hpnicfCATVTransTemperatureTrap,
       "hpnicfCATVTransTemperatureReTrap": hpnicfCATVTransTemperatureReTrap}
)
