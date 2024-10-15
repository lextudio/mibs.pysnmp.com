# SNMP MIB module (H3C-CATV-TRANSCEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-CATV-TRANSCEIVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:57 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cCATVTransceiver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cCATVTransStatus_ObjectIdentity = ObjectIdentity
h3cCATVTransStatus = _H3cCATVTransStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1)
)
_H3cCATVTransStatusScalarObjects_ObjectIdentity = ObjectIdentity
h3cCATVTransStatusScalarObjects = _H3cCATVTransStatusScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1, 1)
)


class _H3cCATVTransState_Type(Integer32):
    """Custom type h3cCATVTransState based on Integer32"""
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


_H3cCATVTransState_Type.__name__ = "Integer32"
_H3cCATVTransState_Object = MibScalar
h3cCATVTransState = _H3cCATVTransState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1, 1, 1),
    _H3cCATVTransState_Type()
)
h3cCATVTransState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCATVTransState.setStatus("current")
_H3cCATVTransInputPwr_Type = Integer32
_H3cCATVTransInputPwr_Object = MibScalar
h3cCATVTransInputPwr = _H3cCATVTransInputPwr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1, 1, 2),
    _H3cCATVTransInputPwr_Type()
)
h3cCATVTransInputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCATVTransInputPwr.setStatus("current")
if mibBuilder.loadTexts:
    h3cCATVTransInputPwr.setUnits("dbm")
_H3cCATVTransOutputLevel_Type = Integer32
_H3cCATVTransOutputLevel_Object = MibScalar
h3cCATVTransOutputLevel = _H3cCATVTransOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1, 1, 3),
    _H3cCATVTransOutputLevel_Type()
)
h3cCATVTransOutputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCATVTransOutputLevel.setStatus("current")
if mibBuilder.loadTexts:
    h3cCATVTransOutputLevel.setUnits("dbuv")
_H3cCATVTransTemperature_Type = Integer32
_H3cCATVTransTemperature_Object = MibScalar
h3cCATVTransTemperature = _H3cCATVTransTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1, 1, 4),
    _H3cCATVTransTemperature_Type()
)
h3cCATVTransTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCATVTransTemperature.setStatus("current")
if mibBuilder.loadTexts:
    h3cCATVTransTemperature.setUnits("centigrade")
_H3cCATVTransceiverMan_ObjectIdentity = ObjectIdentity
h3cCATVTransceiverMan = _H3cCATVTransceiverMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 2)
)
_H3cCATVTransCtrlScalarObjects_ObjectIdentity = ObjectIdentity
h3cCATVTransCtrlScalarObjects = _H3cCATVTransCtrlScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 2, 1)
)
_H3cCATVTransInputPwrLowerThr_Type = Integer32
_H3cCATVTransInputPwrLowerThr_Object = MibScalar
h3cCATVTransInputPwrLowerThr = _H3cCATVTransInputPwrLowerThr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 2, 1, 1),
    _H3cCATVTransInputPwrLowerThr_Type()
)
h3cCATVTransInputPwrLowerThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCATVTransInputPwrLowerThr.setStatus("current")
if mibBuilder.loadTexts:
    h3cCATVTransInputPwrLowerThr.setUnits("dbm")
_H3cCATVTransOutputLvlLowerThr_Type = Integer32
_H3cCATVTransOutputLvlLowerThr_Object = MibScalar
h3cCATVTransOutputLvlLowerThr = _H3cCATVTransOutputLvlLowerThr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 2, 1, 2),
    _H3cCATVTransOutputLvlLowerThr_Type()
)
h3cCATVTransOutputLvlLowerThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCATVTransOutputLvlLowerThr.setStatus("current")
if mibBuilder.loadTexts:
    h3cCATVTransOutputLvlLowerThr.setUnits("dbuv")
_H3cCATVTransTempratureUpperThr_Type = Integer32
_H3cCATVTransTempratureUpperThr_Object = MibScalar
h3cCATVTransTempratureUpperThr = _H3cCATVTransTempratureUpperThr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 2, 1, 3),
    _H3cCATVTransTempratureUpperThr_Type()
)
h3cCATVTransTempratureUpperThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCATVTransTempratureUpperThr.setStatus("current")
_H3cCATVTansTrap_ObjectIdentity = ObjectIdentity
h3cCATVTansTrap = _H3cCATVTansTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3)
)
_H3cCATVTransTrapPrefix_ObjectIdentity = ObjectIdentity
h3cCATVTransTrapPrefix = _H3cCATVTransTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cCATVTransInputPwrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 1)
)
h3cCATVTransInputPwrTrap.setObjects(
    ("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransInputPwr")
)
if mibBuilder.loadTexts:
    h3cCATVTransInputPwrTrap.setStatus(
        "current"
    )

h3cCATVTransInputPwrReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 2)
)
h3cCATVTransInputPwrReTrap.setObjects(
    ("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransInputPwr")
)
if mibBuilder.loadTexts:
    h3cCATVTransInputPwrReTrap.setStatus(
        "current"
    )

h3cCATVTransOutputLvlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 3)
)
h3cCATVTransOutputLvlTrap.setObjects(
    ("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransOutputLevel")
)
if mibBuilder.loadTexts:
    h3cCATVTransOutputLvlTrap.setStatus(
        "current"
    )

h3cCATVTransOutputLvlReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 4)
)
h3cCATVTransOutputLvlReTrap.setObjects(
    ("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransOutputLevel")
)
if mibBuilder.loadTexts:
    h3cCATVTransOutputLvlReTrap.setStatus(
        "current"
    )

h3cCATVTransTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 5)
)
h3cCATVTransTemperatureTrap.setObjects(
    ("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransTemperature")
)
if mibBuilder.loadTexts:
    h3cCATVTransTemperatureTrap.setStatus(
        "current"
    )

h3cCATVTransTemperatureReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 6)
)
h3cCATVTransTemperatureReTrap.setObjects(
    ("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransTemperature")
)
if mibBuilder.loadTexts:
    h3cCATVTransTemperatureReTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-CATV-TRANSCEIVER-MIB",
    **{"h3cCATVTransceiver": h3cCATVTransceiver,
       "h3cCATVTransStatus": h3cCATVTransStatus,
       "h3cCATVTransStatusScalarObjects": h3cCATVTransStatusScalarObjects,
       "h3cCATVTransState": h3cCATVTransState,
       "h3cCATVTransInputPwr": h3cCATVTransInputPwr,
       "h3cCATVTransOutputLevel": h3cCATVTransOutputLevel,
       "h3cCATVTransTemperature": h3cCATVTransTemperature,
       "h3cCATVTransceiverMan": h3cCATVTransceiverMan,
       "h3cCATVTransCtrlScalarObjects": h3cCATVTransCtrlScalarObjects,
       "h3cCATVTransInputPwrLowerThr": h3cCATVTransInputPwrLowerThr,
       "h3cCATVTransOutputLvlLowerThr": h3cCATVTransOutputLvlLowerThr,
       "h3cCATVTransTempratureUpperThr": h3cCATVTransTempratureUpperThr,
       "h3cCATVTansTrap": h3cCATVTansTrap,
       "h3cCATVTransTrapPrefix": h3cCATVTransTrapPrefix,
       "h3cCATVTransInputPwrTrap": h3cCATVTransInputPwrTrap,
       "h3cCATVTransInputPwrReTrap": h3cCATVTransInputPwrReTrap,
       "h3cCATVTransOutputLvlTrap": h3cCATVTransOutputLvlTrap,
       "h3cCATVTransOutputLvlReTrap": h3cCATVTransOutputLvlReTrap,
       "h3cCATVTransTemperatureTrap": h3cCATVTransTemperatureTrap,
       "h3cCATVTransTemperatureReTrap": h3cCATVTransTemperatureReTrap}
)
