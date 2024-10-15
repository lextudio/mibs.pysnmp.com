# SNMP MIB module (CISCO-AAA-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AAA-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:22 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoAAAClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 158)
)
ciscoAAAClientMIB.setRevisions(
        ("2001-11-19 00:00",
         "2001-05-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SessionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 2),
          ("http", 3),
          ("telnet", 1))
    )



class AuthenMethod(Integer32, TextualConvention):
    status = "current"
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
        *(("kerberos", 3),
          ("local", 4),
          ("radius", 2),
          ("tacacs", 1))
    )



class LoginMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("login", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CacMIBObjects_ObjectIdentity = ObjectIdentity
cacMIBObjects = _CacMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1)
)
_CacPriority_ObjectIdentity = ObjectIdentity
cacPriority = _CacPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1)
)
_CacPriorityTable_Object = MibTable
cacPriorityTable = _CacPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cacPriorityTable.setStatus("current")
_CacPriorityEntry_Object = MibTableRow
cacPriorityEntry = _CacPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1)
)
cacPriorityEntry.setIndexNames(
    (0, "CISCO-AAA-CLIENT-MIB", "cacSession"),
    (0, "CISCO-AAA-CLIENT-MIB", "cacAuthen"),
    (0, "CISCO-AAA-CLIENT-MIB", "cacLoginMode"),
)
if mibBuilder.loadTexts:
    cacPriorityEntry.setStatus("current")
_CacSession_Type = SessionType
_CacSession_Object = MibTableColumn
cacSession = _CacSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 1),
    _CacSession_Type()
)
cacSession.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cacSession.setStatus("current")
_CacAuthen_Type = AuthenMethod
_CacAuthen_Object = MibTableColumn
cacAuthen = _CacAuthen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 2),
    _CacAuthen_Type()
)
cacAuthen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cacAuthen.setStatus("current")
_CacLoginMode_Type = LoginMode
_CacLoginMode_Object = MibTableColumn
cacLoginMode = _CacLoginMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 3),
    _CacLoginMode_Type()
)
cacLoginMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cacLoginMode.setStatus("current")
_CacEnable_Type = TruthValue
_CacEnable_Object = MibTableColumn
cacEnable = _CacEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 4),
    _CacEnable_Type()
)
cacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacEnable.setStatus("current")


class _CacPriorityNumber_Type(Integer32):
    """Custom type cacPriorityNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CacPriorityNumber_Type.__name__ = "Integer32"
_CacPriorityNumber_Object = MibTableColumn
cacPriorityNumber = _CacPriorityNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 5),
    _CacPriorityNumber_Type()
)
cacPriorityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacPriorityNumber.setStatus("current")
_CacPrimaryMethod_Type = TruthValue
_CacPrimaryMethod_Object = MibTableColumn
cacPrimaryMethod = _CacPrimaryMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 6),
    _CacPrimaryMethod_Type()
)
cacPrimaryMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacPrimaryMethod.setStatus("current")
_CacLoginConfig_ObjectIdentity = ObjectIdentity
cacLoginConfig = _CacLoginConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2)
)
_CacLoginConfigTable_Object = MibTable
cacLoginConfigTable = _CacLoginConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cacLoginConfigTable.setStatus("current")
_CacLoginConfigEntry_Object = MibTableRow
cacLoginConfigEntry = _CacLoginConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1)
)
cacLoginConfigEntry.setIndexNames(
    (0, "CISCO-AAA-CLIENT-MIB", "cacLoginMode"),
    (0, "CISCO-AAA-CLIENT-MIB", "cacSession"),
)
if mibBuilder.loadTexts:
    cacLoginConfigEntry.setStatus("current")


class _CacMaxLoginAttempt_Type(Integer32):
    """Custom type cacMaxLoginAttempt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 10),
    )


_CacMaxLoginAttempt_Type.__name__ = "Integer32"
_CacMaxLoginAttempt_Object = MibTableColumn
cacMaxLoginAttempt = _CacMaxLoginAttempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 1),
    _CacMaxLoginAttempt_Type()
)
cacMaxLoginAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacMaxLoginAttempt.setStatus("current")


class _CacLockoutPeriod_Type(Integer32):
    """Custom type cacLockoutPeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 600),
    )


_CacLockoutPeriod_Type.__name__ = "Integer32"
_CacLockoutPeriod_Object = MibTableColumn
cacLockoutPeriod = _CacLockoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 2),
    _CacLockoutPeriod_Type()
)
cacLockoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacLockoutPeriod.setStatus("deprecated")
if mibBuilder.loadTexts:
    cacLockoutPeriod.setUnits("seconds")


class _CacLockoutPeriodExt_Type(Integer32):
    """Custom type cacLockoutPeriodExt based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 43200),
    )


_CacLockoutPeriodExt_Type.__name__ = "Integer32"
_CacLockoutPeriodExt_Object = MibTableColumn
cacLockoutPeriodExt = _CacLockoutPeriodExt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 3),
    _CacLockoutPeriodExt_Type()
)
cacLockoutPeriodExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacLockoutPeriodExt.setStatus("current")
if mibBuilder.loadTexts:
    cacLockoutPeriodExt.setUnits("seconds")
_CacMIBNotifications_ObjectIdentity = ObjectIdentity
cacMIBNotifications = _CacMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 2)
)
_CacMIBConformance_ObjectIdentity = ObjectIdentity
cacMIBConformance = _CacMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 3)
)
_CacMIBCompliances_ObjectIdentity = ObjectIdentity
cacMIBCompliances = _CacMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1)
)
_CacMIBGroups_ObjectIdentity = ObjectIdentity
cacMIBGroups = _CacMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2)
)

# Managed Objects groups

cacPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 1)
)
cacPriorityGroup.setObjects(
      *(("CISCO-AAA-CLIENT-MIB", "cacEnable"),
        ("CISCO-AAA-CLIENT-MIB", "cacPriorityNumber"),
        ("CISCO-AAA-CLIENT-MIB", "cacPrimaryMethod"))
)
if mibBuilder.loadTexts:
    cacPriorityGroup.setStatus("current")

cacLoginConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 2)
)
cacLoginConfigGroup.setObjects(
      *(("CISCO-AAA-CLIENT-MIB", "cacMaxLoginAttempt"),
        ("CISCO-AAA-CLIENT-MIB", "cacLockoutPeriod"))
)
if mibBuilder.loadTexts:
    cacLoginConfigGroup.setStatus("deprecated")

cacLoginConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 3)
)
cacLoginConfigGroupRev1.setObjects(
      *(("CISCO-AAA-CLIENT-MIB", "cacMaxLoginAttempt"),
        ("CISCO-AAA-CLIENT-MIB", "cacLockoutPeriodExt"))
)
if mibBuilder.loadTexts:
    cacLoginConfigGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cacMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cacMIBCompliance.setStatus(
        "deprecated"
    )

cacMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cacMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AAA-CLIENT-MIB",
    **{"SessionType": SessionType,
       "AuthenMethod": AuthenMethod,
       "LoginMode": LoginMode,
       "ciscoAAAClientMIB": ciscoAAAClientMIB,
       "cacMIBObjects": cacMIBObjects,
       "cacPriority": cacPriority,
       "cacPriorityTable": cacPriorityTable,
       "cacPriorityEntry": cacPriorityEntry,
       "cacSession": cacSession,
       "cacAuthen": cacAuthen,
       "cacLoginMode": cacLoginMode,
       "cacEnable": cacEnable,
       "cacPriorityNumber": cacPriorityNumber,
       "cacPrimaryMethod": cacPrimaryMethod,
       "cacLoginConfig": cacLoginConfig,
       "cacLoginConfigTable": cacLoginConfigTable,
       "cacLoginConfigEntry": cacLoginConfigEntry,
       "cacMaxLoginAttempt": cacMaxLoginAttempt,
       "cacLockoutPeriod": cacLockoutPeriod,
       "cacLockoutPeriodExt": cacLockoutPeriodExt,
       "cacMIBNotifications": cacMIBNotifications,
       "cacMIBConformance": cacMIBConformance,
       "cacMIBCompliances": cacMIBCompliances,
       "cacMIBCompliance": cacMIBCompliance,
       "cacMIBCompliance2": cacMIBCompliance2,
       "cacMIBGroups": cacMIBGroups,
       "cacPriorityGroup": cacPriorityGroup,
       "cacLoginConfigGroup": cacLoginConfigGroup,
       "cacLoginConfigGroupRev1": cacLoginConfigGroupRev1}
)
