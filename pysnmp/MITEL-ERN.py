# SNMP MIB module (MITEL-ERN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-ERN
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:17 2024
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

(mitelAppCallServer,) = mibBuilder.importSymbols(
    "MITEL-MIB",
    "mitelAppCallServer")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Integer32(Integer32):
    """Custom type Integer32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )





class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MitelCsEmergencyResponse_ObjectIdentity = ObjectIdentity
mitelCsEmergencyResponse = _MitelCsEmergencyResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3)
)
_MitelCsErSeqNumber_Type = Integer32
_MitelCsErSeqNumber_Object = MibScalar
mitelCsErSeqNumber = _MitelCsErSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 1),
    _MitelCsErSeqNumber_Type()
)
mitelCsErSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mitelCsErSeqNumber.setStatus("mandatory")
_MitelCsErCallType_Type = Integer32
_MitelCsErCallType_Object = MibScalar
mitelCsErCallType = _MitelCsErCallType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 2),
    _MitelCsErCallType_Type()
)
mitelCsErCallType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mitelCsErCallType.setStatus("mandatory")
_MitelCsErDetectTime_Type = DateAndTime
_MitelCsErDetectTime_Object = MibScalar
mitelCsErDetectTime = _MitelCsErDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 3),
    _MitelCsErDetectTime_Type()
)
mitelCsErDetectTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mitelCsErDetectTime.setStatus("mandatory")
_MitelCsErCallingDN_Type = DisplayString
_MitelCsErCallingDN_Object = MibScalar
mitelCsErCallingDN = _MitelCsErCallingDN_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 4),
    _MitelCsErCallingDN_Type()
)
mitelCsErCallingDN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mitelCsErCallingDN.setStatus("mandatory")
_MitelCsErCallingPNI_Type = DisplayString
_MitelCsErCallingPNI_Object = MibScalar
mitelCsErCallingPNI = _MitelCsErCallingPNI_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 5),
    _MitelCsErCallingPNI_Type()
)
mitelCsErCallingPNI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mitelCsErCallingPNI.setStatus("mandatory")
_MitelCsErCesidDigits_Type = DisplayString
_MitelCsErCesidDigits_Object = MibScalar
mitelCsErCesidDigits = _MitelCsErCesidDigits_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 6),
    _MitelCsErCesidDigits_Type()
)
mitelCsErCesidDigits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mitelCsErCesidDigits.setStatus("mandatory")
_MitelCsErDialledDigits_Type = DisplayString
_MitelCsErDialledDigits_Object = MibScalar
mitelCsErDialledDigits = _MitelCsErDialledDigits_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 7),
    _MitelCsErDialledDigits_Type()
)
mitelCsErDialledDigits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mitelCsErDialledDigits.setStatus("mandatory")
_MitelCsErRegistrationDN_Type = DisplayString
_MitelCsErRegistrationDN_Object = MibScalar
mitelCsErRegistrationDN = _MitelCsErRegistrationDN_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 8),
    _MitelCsErRegistrationDN_Type()
)
mitelCsErRegistrationDN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mitelCsErRegistrationDN.setStatus("mandatory")
_MitelCsErUnackTable_Object = MibTable
mitelCsErUnackTable = _MitelCsErUnackTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    mitelCsErUnackTable.setStatus("mandatory")
_MitelCsErUnackTableEntry_Object = MibTableRow
mitelCsErUnackTableEntry = _MitelCsErUnackTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 9, 1)
)
mitelCsErUnackTableEntry.setIndexNames(
    (0, "MITEL-ERN", "mitelCsErUnackTableIndex"),
)
if mibBuilder.loadTexts:
    mitelCsErUnackTableEntry.setStatus("mandatory")
_MitelCsErUnackTableIndex_Type = Integer32
_MitelCsErUnackTableIndex_Object = MibTableColumn
mitelCsErUnackTableIndex = _MitelCsErUnackTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 9, 1, 1),
    _MitelCsErUnackTableIndex_Type()
)
mitelCsErUnackTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mitelCsErUnackTableIndex.setStatus("mandatory")
_MitelCsErUnackTableToken_Type = Integer32
_MitelCsErUnackTableToken_Object = MibTableColumn
mitelCsErUnackTableToken = _MitelCsErUnackTableToken_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 9, 1, 2),
    _MitelCsErUnackTableToken_Type()
)
mitelCsErUnackTableToken.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mitelCsErUnackTableToken.setStatus("mandatory")
_MitelCsErNotifications_ObjectIdentity = ObjectIdentity
mitelCsErNotifications = _MitelCsErNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 10)
)

# Managed Objects groups


# Notification objects

mitelCsErNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 0, 401)
)
mitelCsErNotification.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("MITEL-ERN", "mitelCsErSeqNumber"),
        ("MITEL-ERN", "mitelCsErCallType"),
        ("MITEL-ERN", "mitelCsErDetectTime"),
        ("MITEL-ERN", "mitelCsErCallingDN"),
        ("MITEL-ERN", "mitelCsErCallingPNI"),
        ("MITEL-ERN", "mitelCsErCesidDigits"),
        ("MITEL-ERN", "mitelCsErDialledDigits"),
        ("MITEL-ERN", "mitelCsErRegistrationDN"),
        ("MITEL-ERN", "mitelCsErUnackTableIndex"),
        ("MITEL-ERN", "mitelCsErUnackTableToken"))
)
if mibBuilder.loadTexts:
    mitelCsErNotification.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-ERN",
    **{"Integer32": Integer32,
       "DateAndTime": DateAndTime,
       "mitelCsEmergencyResponse": mitelCsEmergencyResponse,
       "mitelCsErNotification": mitelCsErNotification,
       "mitelCsErSeqNumber": mitelCsErSeqNumber,
       "mitelCsErCallType": mitelCsErCallType,
       "mitelCsErDetectTime": mitelCsErDetectTime,
       "mitelCsErCallingDN": mitelCsErCallingDN,
       "mitelCsErCallingPNI": mitelCsErCallingPNI,
       "mitelCsErCesidDigits": mitelCsErCesidDigits,
       "mitelCsErDialledDigits": mitelCsErDialledDigits,
       "mitelCsErRegistrationDN": mitelCsErRegistrationDN,
       "mitelCsErUnackTable": mitelCsErUnackTable,
       "mitelCsErUnackTableEntry": mitelCsErUnackTableEntry,
       "mitelCsErUnackTableIndex": mitelCsErUnackTableIndex,
       "mitelCsErUnackTableToken": mitelCsErUnackTableToken,
       "mitelCsErNotifications": mitelCsErNotifications}
)
