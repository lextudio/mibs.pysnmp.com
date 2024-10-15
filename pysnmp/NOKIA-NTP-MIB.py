# SNMP MIB module (NOKIA-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:43 2024
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

(ntcCommonModules,
 ntcNtpMibs,
 ntcNtpReqs) = mibBuilder.importSymbols(
    "NOKIA-COMMON-MIB-OID-REGISTRATION-MIB",
    "ntcCommonModules",
    "ntcNtpMibs",
    "ntcNtpReqs")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

nokiaNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 2)
)
nokiaNtpMIB.setRevisions(
        ("1998-10-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledDisabled(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class TimeServerStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("clockNotInSynch", 3),
          ("diffTooBig", 4),
          ("notReachable", 2),
          ("ok", 1),
          ("otherError", 5))
    )



# MIB Managed Objects in the order of their OIDs

_NokiaNtpObjs_ObjectIdentity = ObjectIdentity
nokiaNtpObjs = _NokiaNtpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1)
)
_NtcNtpConf_ObjectIdentity = ObjectIdentity
ntcNtpConf = _NtcNtpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1)
)
_NtcNtpEnabled_Type = EnabledDisabled
_NtcNtpEnabled_Object = MibScalar
ntcNtpEnabled = _NtcNtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 1),
    _NtcNtpEnabled_Type()
)
ntcNtpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcNtpEnabled.setStatus("current")


class _NtcNtpServerTableNextIndex_Type(Integer32):
    """Custom type ntcNtpServerTableNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NtcNtpServerTableNextIndex_Type.__name__ = "Integer32"
_NtcNtpServerTableNextIndex_Object = MibScalar
ntcNtpServerTableNextIndex = _NtcNtpServerTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 2),
    _NtcNtpServerTableNextIndex_Type()
)
ntcNtpServerTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcNtpServerTableNextIndex.setStatus("current")
_NtcNtpServerTable_Object = MibTable
ntcNtpServerTable = _NtcNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ntcNtpServerTable.setStatus("current")
_NtcNtpServerEntry_Object = MibTableRow
ntcNtpServerEntry = _NtcNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1)
)
ntcNtpServerEntry.setIndexNames(
    (0, "NOKIA-NTP-MIB", "ntcNtpServerIndex"),
)
if mibBuilder.loadTexts:
    ntcNtpServerEntry.setStatus("current")


class _NtcNtpServerIndex_Type(Integer32):
    """Custom type ntcNtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtcNtpServerIndex_Type.__name__ = "Integer32"
_NtcNtpServerIndex_Object = MibTableColumn
ntcNtpServerIndex = _NtcNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 1),
    _NtcNtpServerIndex_Type()
)
ntcNtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcNtpServerIndex.setStatus("current")


class _NtcNtpServerAddress_Type(DisplayString):
    """Custom type ntcNtpServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcNtpServerAddress_Type.__name__ = "DisplayString"
_NtcNtpServerAddress_Object = MibTableColumn
ntcNtpServerAddress = _NtcNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 2),
    _NtcNtpServerAddress_Type()
)
ntcNtpServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcNtpServerAddress.setStatus("current")


class _NtcNtpServerPort_Type(Integer32):
    """Custom type ntcNtpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtcNtpServerPort_Type.__name__ = "Integer32"
_NtcNtpServerPort_Object = MibTableColumn
ntcNtpServerPort = _NtcNtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 3),
    _NtcNtpServerPort_Type()
)
ntcNtpServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcNtpServerPort.setStatus("current")
_NtcNtpServerStatus_Type = TimeServerStatus
_NtcNtpServerStatus_Object = MibTableColumn
ntcNtpServerStatus = _NtcNtpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 4),
    _NtcNtpServerStatus_Type()
)
ntcNtpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcNtpServerStatus.setStatus("current")
_NtcNtpServerPreferred_Type = TruthValue
_NtcNtpServerPreferred_Object = MibTableColumn
ntcNtpServerPreferred = _NtcNtpServerPreferred_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 5),
    _NtcNtpServerPreferred_Type()
)
ntcNtpServerPreferred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcNtpServerPreferred.setStatus("current")
_NtcNtpServerRowStatus_Type = RowStatus
_NtcNtpServerRowStatus_Object = MibTableColumn
ntcNtpServerRowStatus = _NtcNtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 6),
    _NtcNtpServerRowStatus_Type()
)
ntcNtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcNtpServerRowStatus.setStatus("current")
_NtcNtpRtcConf_ObjectIdentity = ObjectIdentity
ntcNtpRtcConf = _NtcNtpRtcConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 2)
)


class _NtcNtpRtcCurrentTime_Type(OctetString):
    """Custom type ntcNtpRtcCurrentTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_NtcNtpRtcCurrentTime_Type.__name__ = "OctetString"
_NtcNtpRtcCurrentTime_Object = MibScalar
ntcNtpRtcCurrentTime = _NtcNtpRtcCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 2, 1),
    _NtcNtpRtcCurrentTime_Type()
)
ntcNtpRtcCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcNtpRtcCurrentTime.setStatus("current")


class _NtcNtpRtcTimeZone_Type(DisplayString):
    """Custom type ntcNtpRtcTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NtcNtpRtcTimeZone_Type.__name__ = "DisplayString"
_NtcNtpRtcTimeZone_Object = MibScalar
ntcNtpRtcTimeZone = _NtcNtpRtcTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 2, 2),
    _NtcNtpRtcTimeZone_Type()
)
ntcNtpRtcTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcNtpRtcTimeZone.setStatus("current")
_NtcNtpGroups_ObjectIdentity = ObjectIdentity
ntcNtpGroups = _NtcNtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 1)
)
_NtcNtpCompliances_ObjectIdentity = ObjectIdentity
ntcNtpCompliances = _NtcNtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 2)
)

# Managed Objects groups

ntcNtpMinimumRTCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 1, 1)
)
ntcNtpMinimumRTCGroup.setObjects(
      *(("NOKIA-NTP-MIB", "ntcNtpRtcCurrentTime"),
        ("NOKIA-NTP-MIB", "ntcNtpRtcTimeZone"))
)
if mibBuilder.loadTexts:
    ntcNtpMinimumRTCGroup.setStatus("current")

ntcNtpMandatoryNTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 1, 2)
)
ntcNtpMandatoryNTPGroup.setObjects(
      *(("NOKIA-NTP-MIB", "ntcNtpEnabled"),
        ("NOKIA-NTP-MIB", "ntcNtpServerTableNextIndex"),
        ("NOKIA-NTP-MIB", "ntcNtpServerAddress"),
        ("NOKIA-NTP-MIB", "ntcNtpServerPort"),
        ("NOKIA-NTP-MIB", "ntcNtpServerStatus"),
        ("NOKIA-NTP-MIB", "ntcNtpServerPreferred"),
        ("NOKIA-NTP-MIB", "ntcNtpServerRowStatus"))
)
if mibBuilder.loadTexts:
    ntcNtpMandatoryNTPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nokiaNtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nokiaNtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-NTP-MIB",
    **{"EnabledDisabled": EnabledDisabled,
       "TimeServerStatus": TimeServerStatus,
       "nokiaNtpMIB": nokiaNtpMIB,
       "nokiaNtpObjs": nokiaNtpObjs,
       "ntcNtpConf": ntcNtpConf,
       "ntcNtpEnabled": ntcNtpEnabled,
       "ntcNtpServerTableNextIndex": ntcNtpServerTableNextIndex,
       "ntcNtpServerTable": ntcNtpServerTable,
       "ntcNtpServerEntry": ntcNtpServerEntry,
       "ntcNtpServerIndex": ntcNtpServerIndex,
       "ntcNtpServerAddress": ntcNtpServerAddress,
       "ntcNtpServerPort": ntcNtpServerPort,
       "ntcNtpServerStatus": ntcNtpServerStatus,
       "ntcNtpServerPreferred": ntcNtpServerPreferred,
       "ntcNtpServerRowStatus": ntcNtpServerRowStatus,
       "ntcNtpRtcConf": ntcNtpRtcConf,
       "ntcNtpRtcCurrentTime": ntcNtpRtcCurrentTime,
       "ntcNtpRtcTimeZone": ntcNtpRtcTimeZone,
       "ntcNtpGroups": ntcNtpGroups,
       "ntcNtpMinimumRTCGroup": ntcNtpMinimumRTCGroup,
       "ntcNtpMandatoryNTPGroup": ntcNtpMandatoryNTPGroup,
       "ntcNtpCompliances": ntcNtpCompliances,
       "nokiaNtpCompliance": nokiaNtpCompliance}
)
