# SNMP MIB module (JUNIPER-WX-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-WX-GLOBAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:29 2024
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

(jnxWxGrpStatus,) = mibBuilder.importSymbols(
    "JUNIPER-WX-GLOBAL-MIB",
    "jnxWxGrpStatus")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxWxGrpStatusSys_ObjectIdentity = ObjectIdentity
jnxWxGrpStatusSys = _JnxWxGrpStatusSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatusSys.setStatus("current")


class _JnxWxGrpStatusSysModel_Type(Integer32):
    """Custom type jnxWxGrpStatusSysModel based on Integer32"""
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
        *(("other", 8),
          ("wxc1800", 4),
          ("wxc250", 1),
          ("wxc2600", 5),
          ("wxc3400", 6),
          ("wxc500", 2),
          ("wxc590", 3),
          ("wxc7800", 7))
    )


_JnxWxGrpStatusSysModel_Type.__name__ = "Integer32"
_JnxWxGrpStatusSysModel_Object = MibScalar
jnxWxGrpStatusSysModel = _JnxWxGrpStatusSysModel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 1, 1),
    _JnxWxGrpStatusSysModel_Type()
)
jnxWxGrpStatusSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatusSysModel.setStatus("current")


class _JnxWxGrpStatusSysSwVersion_Type(DisplayString):
    """Custom type jnxWxGrpStatusSysSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxWxGrpStatusSysSwVersion_Type.__name__ = "DisplayString"
_JnxWxGrpStatusSysSwVersion_Object = MibScalar
jnxWxGrpStatusSysSwVersion = _JnxWxGrpStatusSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 1, 2),
    _JnxWxGrpStatusSysSwVersion_Type()
)
jnxWxGrpStatusSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatusSysSwVersion.setStatus("current")


class _JnxWxGrpStatusSysHwVersion_Type(DisplayString):
    """Custom type jnxWxGrpStatusSysHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxWxGrpStatusSysHwVersion_Type.__name__ = "DisplayString"
_JnxWxGrpStatusSysHwVersion_Object = MibScalar
jnxWxGrpStatusSysHwVersion = _JnxWxGrpStatusSysHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 1, 3),
    _JnxWxGrpStatusSysHwVersion_Type()
)
jnxWxGrpStatusSysHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatusSysHwVersion.setStatus("current")
_JnxWxGrpStatusApp_ObjectIdentity = ObjectIdentity
jnxWxGrpStatusApp = _JnxWxGrpStatusApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatusApp.setStatus("current")
_JnxWxGrpStatusAppMonCount_Type = Integer32
_JnxWxGrpStatusAppMonCount_Object = MibScalar
jnxWxGrpStatusAppMonCount = _JnxWxGrpStatusAppMonCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 1),
    _JnxWxGrpStatusAppMonCount_Type()
)
jnxWxGrpStatusAppMonCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatusAppMonCount.setStatus("current")
_JnxWxGrpStatusAppTable_Object = MibTable
jnxWxGrpStatusAppTable = _JnxWxGrpStatusAppTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatusAppTable.setStatus("current")
_JnxWxGrpStatusAppEntry_Object = MibTableRow
jnxWxGrpStatusAppEntry = _JnxWxGrpStatusAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 2, 1)
)
jnxWxGrpStatusAppEntry.setIndexNames(
    (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusAppId"),
)
if mibBuilder.loadTexts:
    jnxWxGrpStatusAppEntry.setStatus("current")
_JnxWxGrpStatusAppId_Type = Integer32
_JnxWxGrpStatusAppId_Object = MibTableColumn
jnxWxGrpStatusAppId = _JnxWxGrpStatusAppId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 2, 1, 1),
    _JnxWxGrpStatusAppId_Type()
)
jnxWxGrpStatusAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWxGrpStatusAppId.setStatus("current")


class _JnxWxGrpStatusAppName_Type(DisplayString):
    """Custom type jnxWxGrpStatusAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxWxGrpStatusAppName_Type.__name__ = "DisplayString"
_JnxWxGrpStatusAppName_Object = MibTableColumn
jnxWxGrpStatusAppName = _JnxWxGrpStatusAppName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 2, 1, 2),
    _JnxWxGrpStatusAppName_Type()
)
jnxWxGrpStatusAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatusAppName.setStatus("current")


class _JnxWxGrpStatusAppType_Type(Integer32):
    """Custom type jnxWxGrpStatusAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("ftp", 2))
    )


_JnxWxGrpStatusAppType_Type.__name__ = "Integer32"
_JnxWxGrpStatusAppType_Object = MibTableColumn
jnxWxGrpStatusAppType = _JnxWxGrpStatusAppType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 2, 1, 3),
    _JnxWxGrpStatusAppType_Type()
)
jnxWxGrpStatusAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatusAppType.setStatus("current")
_JnxWxGrpStatusRemoteWx_ObjectIdentity = ObjectIdentity
jnxWxGrpStatusRemoteWx = _JnxWxGrpStatusRemoteWx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatusRemoteWx.setStatus("current")
_JnxWxGrpStatusRemoteWxMonCount_Type = Integer32
_JnxWxGrpStatusRemoteWxMonCount_Object = MibScalar
jnxWxGrpStatusRemoteWxMonCount = _JnxWxGrpStatusRemoteWxMonCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 1),
    _JnxWxGrpStatusRemoteWxMonCount_Type()
)
jnxWxGrpStatusRemoteWxMonCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatusRemoteWxMonCount.setStatus("current")
_JnxWxGrpStatusRemoteWxTable_Object = MibTable
jnxWxGrpStatusRemoteWxTable = _JnxWxGrpStatusRemoteWxTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatusRemoteWxTable.setStatus("current")
_JnxWxGrpStatusRemoteWxEntry_Object = MibTableRow
jnxWxGrpStatusRemoteWxEntry = _JnxWxGrpStatusRemoteWxEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 2, 1)
)
jnxWxGrpStatusRemoteWxEntry.setIndexNames(
    (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusRemoteWxId"),
)
if mibBuilder.loadTexts:
    jnxWxGrpStatusRemoteWxEntry.setStatus("current")
_JnxWxGrpStatusRemoteWxId_Type = Integer32
_JnxWxGrpStatusRemoteWxId_Object = MibTableColumn
jnxWxGrpStatusRemoteWxId = _JnxWxGrpStatusRemoteWxId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 2, 1, 1),
    _JnxWxGrpStatusRemoteWxId_Type()
)
jnxWxGrpStatusRemoteWxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWxGrpStatusRemoteWxId.setStatus("current")


class _JnxWxGrpStatusRemoteWxName_Type(DisplayString):
    """Custom type jnxWxGrpStatusRemoteWxName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxWxGrpStatusRemoteWxName_Type.__name__ = "DisplayString"
_JnxWxGrpStatusRemoteWxName_Object = MibTableColumn
jnxWxGrpStatusRemoteWxName = _JnxWxGrpStatusRemoteWxName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 2, 1, 2),
    _JnxWxGrpStatusRemoteWxName_Type()
)
jnxWxGrpStatusRemoteWxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatusRemoteWxName.setStatus("current")


class _JnxWxGrpStatusRemoteWxType_Type(Integer32):
    """Custom type jnxWxGrpStatusRemoteWxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("non-wx-device", 3),
          ("wx-client", 2),
          ("wx-device", 1))
    )


_JnxWxGrpStatusRemoteWxType_Type.__name__ = "Integer32"
_JnxWxGrpStatusRemoteWxType_Object = MibTableColumn
jnxWxGrpStatusRemoteWxType = _JnxWxGrpStatusRemoteWxType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 2, 1, 3),
    _JnxWxGrpStatusRemoteWxType_Type()
)
jnxWxGrpStatusRemoteWxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatusRemoteWxType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-WX-STATUS-MIB",
    **{"jnxWxGrpStatusSys": jnxWxGrpStatusSys,
       "jnxWxGrpStatusSysModel": jnxWxGrpStatusSysModel,
       "jnxWxGrpStatusSysSwVersion": jnxWxGrpStatusSysSwVersion,
       "jnxWxGrpStatusSysHwVersion": jnxWxGrpStatusSysHwVersion,
       "jnxWxGrpStatusApp": jnxWxGrpStatusApp,
       "jnxWxGrpStatusAppMonCount": jnxWxGrpStatusAppMonCount,
       "jnxWxGrpStatusAppTable": jnxWxGrpStatusAppTable,
       "jnxWxGrpStatusAppEntry": jnxWxGrpStatusAppEntry,
       "jnxWxGrpStatusAppId": jnxWxGrpStatusAppId,
       "jnxWxGrpStatusAppName": jnxWxGrpStatusAppName,
       "jnxWxGrpStatusAppType": jnxWxGrpStatusAppType,
       "jnxWxGrpStatusRemoteWx": jnxWxGrpStatusRemoteWx,
       "jnxWxGrpStatusRemoteWxMonCount": jnxWxGrpStatusRemoteWxMonCount,
       "jnxWxGrpStatusRemoteWxTable": jnxWxGrpStatusRemoteWxTable,
       "jnxWxGrpStatusRemoteWxEntry": jnxWxGrpStatusRemoteWxEntry,
       "jnxWxGrpStatusRemoteWxId": jnxWxGrpStatusRemoteWxId,
       "jnxWxGrpStatusRemoteWxName": jnxWxGrpStatusRemoteWxName,
       "jnxWxGrpStatusRemoteWxType": jnxWxGrpStatusRemoteWxType}
)
