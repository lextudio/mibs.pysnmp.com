# SNMP MIB module (SMA-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SMA-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:31 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

notifications = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 2)
)
_Sma_ObjectIdentity = ObjectIdentity
sma = _Sma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 0)
)
_TrapInfo_ObjectIdentity = ObjectIdentity
trapInfo = _TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 1)
)


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 1, 1),
    _HostName_Type()
)
hostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hostName.setStatus("current")


class _ModuleName_Type(DisplayString):
    """Custom type moduleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModuleName_Type.__name__ = "DisplayString"
_ModuleName_Object = MibScalar
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 1, 2),
    _ModuleName_Type()
)
moduleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    moduleName.setStatus("current")
_StatusOID_Type = ObjectIdentifier
_StatusOID_Object = MibScalar
statusOID = _StatusOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 1, 3),
    _StatusOID_Type()
)
statusOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    statusOID.setStatus("current")


class _StatusOIDContext_Type(DisplayString):
    """Custom type statusOIDContext based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StatusOIDContext_Type.__name__ = "DisplayString"
_StatusOIDContext_Object = MibScalar
statusOIDContext = _StatusOIDContext_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 1, 4),
    _StatusOIDContext_Type()
)
statusOIDContext.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    statusOIDContext.setStatus("current")


class _Status_Type(DisplayString):
    """Custom type status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Status_Type.__name__ = "DisplayString"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 1, 5),
    _Status_Type()
)
status.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    status.setStatus("current")


class _Description_Type(DisplayString):
    """Custom type description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Description_Type.__name__ = "DisplayString"
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 1, 6),
    _Description_Type()
)
description.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    description.setStatus("current")


class _DataValue_Type(DisplayString):
    """Custom type dataValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DataValue_Type.__name__ = "DisplayString"
_DataValue_Object = MibScalar
dataValue = _DataValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 1, 7),
    _DataValue_Type()
)
dataValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dataValue.setStatus("current")


class _DataValueType_Type(Integer32):
    """Custom type dataValueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("autonomousType", 17),
          ("counter32", 6),
          ("counter64", 11),
          ("displayString", 12),
          ("gauge32", 7),
          ("integer", 1),
          ("integer32", 4),
          ("ipAddress", 5),
          ("macAddress", 14),
          ("none", 0),
          ("objectIdentifier", 3),
          ("octetString", 2),
          ("opaque", 10),
          ("other", 100),
          ("physAddress", 13),
          ("rowPointer", 19),
          ("rowStatus", 20),
          ("storageType", 21),
          ("tAddress", 23),
          ("tDomain", 22),
          ("testAndIncr", 16),
          ("timeTicks", 9),
          ("truthValue", 15),
          ("unsigned32", 8),
          ("variablePointer", 18))
    )


_DataValueType_Type.__name__ = "Integer32"
_DataValueType_Object = MibScalar
dataValueType = _DataValueType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 1, 8),
    _DataValueType_Type()
)
dataValueType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dataValueType.setStatus("current")

# Managed Objects groups


# Notification objects

statusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 2, 4, 3, 0, 1)
)
statusChange.setObjects(
      *(("SMA-NOTIFICATION-MIB", "hostName"),
        ("SMA-NOTIFICATION-MIB", "moduleName"),
        ("SMA-NOTIFICATION-MIB", "statusOID"),
        ("SMA-NOTIFICATION-MIB", "statusOIDContext"),
        ("SMA-NOTIFICATION-MIB", "status"),
        ("SMA-NOTIFICATION-MIB", "description"),
        ("SMA-NOTIFICATION-MIB", "dataValue"),
        ("SMA-NOTIFICATION-MIB", "dataValueType"))
)
if mibBuilder.loadTexts:
    statusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMA-NOTIFICATION-MIB",
    **{"sun": sun,
       "products": products,
       "management": management,
       "sma": sma,
       "notifications": notifications,
       "traps": traps,
       "statusChange": statusChange,
       "trapInfo": trapInfo,
       "hostName": hostName,
       "moduleName": moduleName,
       "statusOID": statusOID,
       "statusOIDContext": statusOIDContext,
       "status": status,
       "description": description,
       "dataValue": dataValue,
       "dataValueType": dataValueType}
)
