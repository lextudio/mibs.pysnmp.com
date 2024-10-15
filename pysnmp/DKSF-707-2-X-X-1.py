# SNMP MIB module (DKSF-707-2-X-X-1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DKSF-707-2-X-X-1
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:28 2024
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

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

uniPingServerSolutionV3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 707)
)
uniPingServerSolutionV3.setRevisions(
        ("2015-02-09 00:00",
         "2014-03-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lightcom_ObjectIdentity = ObjectIdentity
lightcom = _Lightcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728)
)
_NpTrapInfo_ObjectIdentity = ObjectIdentity
npTrapInfo = _NpTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 90)
)
_NpTrapEmailTo_Type = DisplayString
_NpTrapEmailTo_Object = MibScalar
npTrapEmailTo = _NpTrapEmailTo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 90, 1),
    _NpTrapEmailTo_Type()
)
npTrapEmailTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTrapEmailTo.setStatus("current")
_NpReboot_ObjectIdentity = ObjectIdentity
npReboot = _NpReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 911)
)
_NpSoftReboot_Type = Integer32
_NpSoftReboot_Object = MibScalar
npSoftReboot = _NpSoftReboot_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 1),
    _NpSoftReboot_Type()
)
npSoftReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSoftReboot.setStatus("current")
_NpResetStack_Type = Integer32
_NpResetStack_Object = MibScalar
npResetStack = _NpResetStack_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 2),
    _NpResetStack_Type()
)
npResetStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npResetStack.setStatus("current")
_NpForcedReboot_Type = Integer32
_NpForcedReboot_Object = MibScalar
npForcedReboot = _NpForcedReboot_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 3),
    _NpForcedReboot_Type()
)
npForcedReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npForcedReboot.setStatus("current")
_NpGsm_ObjectIdentity = ObjectIdentity
npGsm = _NpGsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800)
)
_NpGsmInfo_ObjectIdentity = ObjectIdentity
npGsmInfo = _NpGsmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1)
)


class _NpGsmFailed_Type(Integer32):
    """Custom type npGsmFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("fatalError", 2),
          ("ok", 0))
    )


_NpGsmFailed_Type.__name__ = "Integer32"
_NpGsmFailed_Object = MibScalar
npGsmFailed = _NpGsmFailed_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 1),
    _NpGsmFailed_Type()
)
npGsmFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmFailed.setStatus("current")


class _NpGsmRegistration_Type(Integer32):
    """Custom type npGsmRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("denied", 3),
          ("homeNetwork", 1),
          ("impossible", 0),
          ("infoUpdate", 255),
          ("roaming", 5),
          ("searching", 2),
          ("unknown", 4))
    )


_NpGsmRegistration_Type.__name__ = "Integer32"
_NpGsmRegistration_Object = MibScalar
npGsmRegistration = _NpGsmRegistration_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 2),
    _NpGsmRegistration_Type()
)
npGsmRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmRegistration.setStatus("current")


class _NpGsmStrength_Type(Integer32):
    """Custom type npGsmStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NpGsmStrength_Type.__name__ = "Integer32"
_NpGsmStrength_Object = MibScalar
npGsmStrength = _NpGsmStrength_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 3),
    _NpGsmStrength_Type()
)
npGsmStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmStrength.setStatus("current")
_NpGsmSendSms_Type = DisplayString
_NpGsmSendSms_Object = MibScalar
npGsmSendSms = _NpGsmSendSms_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 9),
    _NpGsmSendSms_Type()
)
npGsmSendSms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npGsmSendSms.setStatus("current")
_NpGsmUnparsedRxSms_Type = DisplayString
_NpGsmUnparsedRxSms_Object = MibScalar
npGsmUnparsedRxSms = _NpGsmUnparsedRxSms_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 10),
    _NpGsmUnparsedRxSms_Type()
)
npGsmUnparsedRxSms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmUnparsedRxSms.setStatus("current")
_NpGsmUnparsedRxSmsFrom_Type = DisplayString
_NpGsmUnparsedRxSmsFrom_Object = MibScalar
npGsmUnparsedRxSmsFrom = _NpGsmUnparsedRxSmsFrom_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 11),
    _NpGsmUnparsedRxSmsFrom_Type()
)
npGsmUnparsedRxSmsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmUnparsedRxSmsFrom.setStatus("current")
_NpGsmTraps_ObjectIdentity = ObjectIdentity
npGsmTraps = _NpGsmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2)
)
_NpGsmTrapPrefix_ObjectIdentity = ObjectIdentity
npGsmTrapPrefix = _NpGsmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0)
)

# Managed Objects groups


# Notification objects

npGsmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0, 1)
)
npGsmTrap.setObjects(
      *(("DKSF-707-2-X-X-1", "npGsmFailed"),
        ("DKSF-707-2-X-X-1", "npGsmRegistration"),
        ("DKSF-707-2-X-X-1", "npGsmStrength"))
)
if mibBuilder.loadTexts:
    npGsmTrap.setStatus(
        "current"
    )

npGsmTrapUnparsedSms = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0, 2)
)
npGsmTrapUnparsedSms.setObjects(
      *(("DKSF-707-2-X-X-1", "npGsmUnparsedRxSms"),
        ("DKSF-707-2-X-X-1", "npGsmUnparsedRxSmsFrom"))
)
if mibBuilder.loadTexts:
    npGsmTrapUnparsedSms.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKSF-707-2-X-X-1",
    **{"lightcom": lightcom,
       "npTrapInfo": npTrapInfo,
       "npTrapEmailTo": npTrapEmailTo,
       "uniPingServerSolutionV3": uniPingServerSolutionV3,
       "npReboot": npReboot,
       "npSoftReboot": npSoftReboot,
       "npResetStack": npResetStack,
       "npForcedReboot": npForcedReboot,
       "npGsm": npGsm,
       "npGsmInfo": npGsmInfo,
       "npGsmFailed": npGsmFailed,
       "npGsmRegistration": npGsmRegistration,
       "npGsmStrength": npGsmStrength,
       "npGsmSendSms": npGsmSendSms,
       "npGsmUnparsedRxSms": npGsmUnparsedRxSms,
       "npGsmUnparsedRxSmsFrom": npGsmUnparsedRxSmsFrom,
       "npGsmTraps": npGsmTraps,
       "npGsmTrapPrefix": npGsmTrapPrefix,
       "npGsmTrap": npGsmTrap,
       "npGsmTrapUnparsedSms": npGsmTrapUnparsedSms}
)
