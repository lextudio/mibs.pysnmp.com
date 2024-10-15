# SNMP MIB module (TPT-STACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-STACKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:11 2024
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

(tpt_products,) = mibBuilder.importSymbols(
    "TIPPINGPOINT-REG-MIB",
    "tpt-products")

(FaultCause,) = mibBuilder.importSymbols(
    "TPT-HIGH-AVAIL-MIB",
    "FaultCause")

(EnabledOrNot,) = mibBuilder.importSymbols(
    "TPT-PORT-CONFIG-MIB",
    "EnabledOrNot")

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_stack_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DeviceRti(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              16,
              21,
              32,
              48,
              64)
        )
    )
    namedValues = NamedValues(
        *(("rebooting", 5),
          ("recoverable", 21),
          ("rlinferior", 16),
          ("rtinormal", 64),
          ("rtipending", 48),
          ("unknown", 0),
          ("unrecoverable", 32))
    )



class StackRti(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              48,
              64,
              80,
              96,
              112,
              128)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 48),
          ("rebooting", 64),
          ("recoverable", 80),
          ("rlinferior", 16),
          ("rtinormal", 128),
          ("rtipending", 112),
          ("unknown", 0),
          ("unrecoverable", 96))
    )



# MIB Managed Objects in the order of their OIDs

_StackingStackRtiTimeStamp_Type = Unsigned32
_StackingStackRtiTimeStamp_Object = MibScalar
stackingStackRtiTimeStamp = _StackingStackRtiTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 20, 1),
    _StackingStackRtiTimeStamp_Type()
)
stackingStackRtiTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackingStackRtiTimeStamp.setStatus("current")
_StackingDeviceRTI_Type = DeviceRti
_StackingDeviceRTI_Object = MibScalar
stackingDeviceRTI = _StackingDeviceRTI_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 20, 2),
    _StackingDeviceRTI_Type()
)
stackingDeviceRTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackingDeviceRTI.setStatus("current")
_StackingPrevDeviceRTI_Type = DeviceRti
_StackingPrevDeviceRTI_Object = MibScalar
stackingPrevDeviceRTI = _StackingPrevDeviceRTI_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 20, 3),
    _StackingPrevDeviceRTI_Type()
)
stackingPrevDeviceRTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackingPrevDeviceRTI.setStatus("current")
_StackingDeviceFaultCause_Type = FaultCause
_StackingDeviceFaultCause_Object = MibScalar
stackingDeviceFaultCause = _StackingDeviceFaultCause_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 20, 4),
    _StackingDeviceFaultCause_Type()
)
stackingDeviceFaultCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackingDeviceFaultCause.setStatus("current")
_StackingStackRTI_Type = StackRti
_StackingStackRTI_Object = MibScalar
stackingStackRTI = _StackingStackRTI_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 20, 5),
    _StackingStackRTI_Type()
)
stackingStackRTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackingStackRTI.setStatus("current")
_StackingPrevStackRTI_Type = StackRti
_StackingPrevStackRTI_Object = MibScalar
stackingPrevStackRTI = _StackingPrevStackRTI_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 20, 6),
    _StackingPrevStackRTI_Type()
)
stackingPrevStackRTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackingPrevStackRTI.setStatus("current")


class _TptStackingNotifyDeviceID_Type(OctetString):
    """Custom type tptStackingNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptStackingNotifyDeviceID_Type.__name__ = "OctetString"
_TptStackingNotifyDeviceID_Object = MibScalar
tptStackingNotifyDeviceID = _TptStackingNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 324),
    _TptStackingNotifyDeviceID_Type()
)
tptStackingNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptStackingNotifyDeviceID.setStatus("current")


class _TptStackingNotifyKey_Type(OctetString):
    """Custom type tptStackingNotifyKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TptStackingNotifyKey_Type.__name__ = "OctetString"
_TptStackingNotifyKey_Object = MibScalar
tptStackingNotifyKey = _TptStackingNotifyKey_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 328),
    _TptStackingNotifyKey_Type()
)
tptStackingNotifyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptStackingNotifyKey.setStatus("current")
_TptStackingNotifyTimeStamp_Type = Unsigned32
_TptStackingNotifyTimeStamp_Object = MibScalar
tptStackingNotifyTimeStamp = _TptStackingNotifyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 332),
    _TptStackingNotifyTimeStamp_Type()
)
tptStackingNotifyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptStackingNotifyTimeStamp.setStatus("current")
_TptStackingNotifyDeviceRTI_Type = DeviceRti
_TptStackingNotifyDeviceRTI_Object = MibScalar
tptStackingNotifyDeviceRTI = _TptStackingNotifyDeviceRTI_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 336),
    _TptStackingNotifyDeviceRTI_Type()
)
tptStackingNotifyDeviceRTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptStackingNotifyDeviceRTI.setStatus("current")
_TptStackingNotifyPrevDeviceRTI_Type = DeviceRti
_TptStackingNotifyPrevDeviceRTI_Object = MibScalar
tptStackingNotifyPrevDeviceRTI = _TptStackingNotifyPrevDeviceRTI_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 340),
    _TptStackingNotifyPrevDeviceRTI_Type()
)
tptStackingNotifyPrevDeviceRTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptStackingNotifyPrevDeviceRTI.setStatus("current")
_TptStackingNotifyDeviceFaultCause_Type = FaultCause
_TptStackingNotifyDeviceFaultCause_Object = MibScalar
tptStackingNotifyDeviceFaultCause = _TptStackingNotifyDeviceFaultCause_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 344),
    _TptStackingNotifyDeviceFaultCause_Type()
)
tptStackingNotifyDeviceFaultCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptStackingNotifyDeviceFaultCause.setStatus("current")
_TptStackingNotifyStackRTI_Type = StackRti
_TptStackingNotifyStackRTI_Object = MibScalar
tptStackingNotifyStackRTI = _TptStackingNotifyStackRTI_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 348),
    _TptStackingNotifyStackRTI_Type()
)
tptStackingNotifyStackRTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptStackingNotifyStackRTI.setStatus("current")
_TptStackingNotifyPrevStackRTI_Type = StackRti
_TptStackingNotifyPrevStackRTI_Object = MibScalar
tptStackingNotifyPrevStackRTI = _TptStackingNotifyPrevStackRTI_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 352),
    _TptStackingNotifyPrevStackRTI_Type()
)
tptStackingNotifyPrevStackRTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptStackingNotifyPrevStackRTI.setStatus("current")


class _TptStackingNotifyMissedHeartbeatKey_Type(OctetString):
    """Custom type tptStackingNotifyMissedHeartbeatKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TptStackingNotifyMissedHeartbeatKey_Type.__name__ = "OctetString"
_TptStackingNotifyMissedHeartbeatKey_Object = MibScalar
tptStackingNotifyMissedHeartbeatKey = _TptStackingNotifyMissedHeartbeatKey_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 356),
    _TptStackingNotifyMissedHeartbeatKey_Type()
)
tptStackingNotifyMissedHeartbeatKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptStackingNotifyMissedHeartbeatKey.setStatus("current")

# Managed Objects groups


# Notification objects

tptStackingDeviceRTINotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 70)
)
tptStackingDeviceRTINotify.setObjects(
      *(("TPT-STACKING-MIB", "tptStackingNotifyDeviceID"),
        ("TPT-STACKING-MIB", "tptStackingNotifyKey"),
        ("TPT-STACKING-MIB", "tptStackingNotifyTimeStamp"),
        ("TPT-STACKING-MIB", "tptStackingNotifyDeviceRTI"),
        ("TPT-STACKING-MIB", "tptStackingNotifyPrevDeviceRTI"),
        ("TPT-STACKING-MIB", "tptStackingNotifyDeviceFaultCause"))
)
if mibBuilder.loadTexts:
    tptStackingDeviceRTINotify.setStatus(
        "current"
    )

tptStackingStackRTINotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 71)
)
tptStackingStackRTINotify.setObjects(
      *(("TPT-STACKING-MIB", "tptStackingNotifyDeviceID"),
        ("TPT-STACKING-MIB", "tptStackingNotifyKey"),
        ("TPT-STACKING-MIB", "tptStackingNotifyTimeStamp"),
        ("TPT-STACKING-MIB", "tptStackingNotifyStackRTI"),
        ("TPT-STACKING-MIB", "tptStackingNotifyPrevStackRTI"))
)
if mibBuilder.loadTexts:
    tptStackingStackRTINotify.setStatus(
        "current"
    )

tptStackingMissedHeartbeatNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 72)
)
tptStackingMissedHeartbeatNotify.setObjects(
      *(("TPT-STACKING-MIB", "tptStackingNotifyDeviceID"),
        ("TPT-STACKING-MIB", "tptStackingNotifyKey"),
        ("TPT-STACKING-MIB", "tptStackingNotifyTimeStamp"),
        ("TPT-STACKING-MIB", "tptStackingNotifyMissedHeartbeatKey"))
)
if mibBuilder.loadTexts:
    tptStackingMissedHeartbeatNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-STACKING-MIB",
    **{"DeviceRti": DeviceRti,
       "StackRti": StackRti,
       "tpt-stack-objs": tpt_stack_objs,
       "stackingStackRtiTimeStamp": stackingStackRtiTimeStamp,
       "stackingDeviceRTI": stackingDeviceRTI,
       "stackingPrevDeviceRTI": stackingPrevDeviceRTI,
       "stackingDeviceFaultCause": stackingDeviceFaultCause,
       "stackingStackRTI": stackingStackRTI,
       "stackingPrevStackRTI": stackingPrevStackRTI,
       "tptStackingDeviceRTINotify": tptStackingDeviceRTINotify,
       "tptStackingStackRTINotify": tptStackingStackRTINotify,
       "tptStackingMissedHeartbeatNotify": tptStackingMissedHeartbeatNotify,
       "tptStackingNotifyDeviceID": tptStackingNotifyDeviceID,
       "tptStackingNotifyKey": tptStackingNotifyKey,
       "tptStackingNotifyTimeStamp": tptStackingNotifyTimeStamp,
       "tptStackingNotifyDeviceRTI": tptStackingNotifyDeviceRTI,
       "tptStackingNotifyPrevDeviceRTI": tptStackingNotifyPrevDeviceRTI,
       "tptStackingNotifyDeviceFaultCause": tptStackingNotifyDeviceFaultCause,
       "tptStackingNotifyStackRTI": tptStackingNotifyStackRTI,
       "tptStackingNotifyPrevStackRTI": tptStackingNotifyPrevStackRTI,
       "tptStackingNotifyMissedHeartbeatKey": tptStackingNotifyMissedHeartbeatKey}
)
