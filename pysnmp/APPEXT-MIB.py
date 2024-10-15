# SNMP MIB module (APPEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:30 2024
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

(appExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "appExt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apAppMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApAppSessionTable_Object = MibTable
apAppSessionTable = _ApAppSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2)
)
if mibBuilder.loadTexts:
    apAppSessionTable.setStatus("current")
_ApAppSessionEntry_Object = MibTableRow
apAppSessionEntry = _ApAppSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1)
)
apAppSessionEntry.setIndexNames(
    (0, "APPEXT-MIB", "apAppIpAddr"),
)
if mibBuilder.loadTexts:
    apAppSessionEntry.setStatus("current")
_ApAppIpAddr_Type = IpAddress
_ApAppIpAddr_Object = MibTableColumn
apAppIpAddr = _ApAppIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 1),
    _ApAppIpAddr_Type()
)
apAppIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppIpAddr.setStatus("current")


class _ApAppAuthType_Type(Integer32):
    """Custom type apAppAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authChallenge", 1),
          ("authNone", 0))
    )


_ApAppAuthType_Type.__name__ = "Integer32"
_ApAppAuthType_Object = MibTableColumn
apAppAuthType = _ApAppAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 2),
    _ApAppAuthType_Type()
)
apAppAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAppAuthType.setStatus("current")


class _ApAppEncryptType_Type(Integer32):
    """Custom type apAppEncryptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encryptMd5hash", 1),
          ("encryptNone", 0))
    )


_ApAppEncryptType_Type.__name__ = "Integer32"
_ApAppEncryptType_Object = MibTableColumn
apAppEncryptType = _ApAppEncryptType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 3),
    _ApAppEncryptType_Type()
)
apAppEncryptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAppEncryptType.setStatus("current")


class _ApAppKalFreq_Type(Integer32):
    """Custom type apAppKalFreq based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14, 900),
    )


_ApAppKalFreq_Type.__name__ = "Integer32"
_ApAppKalFreq_Object = MibTableColumn
apAppKalFreq = _ApAppKalFreq_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 4),
    _ApAppKalFreq_Type()
)
apAppKalFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAppKalFreq.setStatus("current")


class _ApAppSecret_Type(DisplayString):
    """Custom type apAppSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApAppSecret_Type.__name__ = "DisplayString"
_ApAppSecret_Object = MibTableColumn
apAppSecret = _ApAppSecret_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 5),
    _ApAppSecret_Type()
)
apAppSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAppSecret.setStatus("current")
_ApAppPktsTx_Type = Integer32
_ApAppPktsTx_Object = MibTableColumn
apAppPktsTx = _ApAppPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 6),
    _ApAppPktsTx_Type()
)
apAppPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppPktsTx.setStatus("current")
_ApAppPktsRx_Type = Integer32
_ApAppPktsRx_Object = MibTableColumn
apAppPktsRx = _ApAppPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 7),
    _ApAppPktsRx_Type()
)
apAppPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppPktsRx.setStatus("current")


class _ApAppSessionState_Type(Integer32):
    """Custom type apAppSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auth", 3),
          ("down", 5),
          ("init", 1),
          ("opened", 2),
          ("stopped", 0),
          ("up", 4))
    )


_ApAppSessionState_Type.__name__ = "Integer32"
_ApAppSessionState_Object = MibTableColumn
apAppSessionState = _ApAppSessionState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 8),
    _ApAppSessionState_Type()
)
apAppSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppSessionState.setStatus("current")


class _ApAppRcmdEnable_Type(Integer32):
    """Custom type apAppRcmdEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rcmdDisable", 1),
          ("rcmdEnable", 0))
    )


_ApAppRcmdEnable_Type.__name__ = "Integer32"
_ApAppRcmdEnable_Object = MibTableColumn
apAppRcmdEnable = _ApAppRcmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 9),
    _ApAppRcmdEnable_Type()
)
apAppRcmdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAppRcmdEnable.setStatus("current")
_ApAppSessionStatus_Type = RowStatus
_ApAppSessionStatus_Object = MibTableColumn
apAppSessionStatus = _ApAppSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 10),
    _ApAppSessionStatus_Type()
)
apAppSessionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAppSessionStatus.setStatus("current")


class _ApAppEnable_Type(Integer32):
    """Custom type apAppEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApAppEnable_Type.__name__ = "Integer32"
_ApAppEnable_Object = MibScalar
apAppEnable = _ApAppEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 3),
    _ApAppEnable_Type()
)
apAppEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAppEnable.setStatus("current")


class _ApAppPortNumber_Type(Integer32):
    """Custom type apAppPortNumber based on Integer32"""
    defaultValue = 5001

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApAppPortNumber_Type.__name__ = "Integer32"
_ApAppPortNumber_Object = MibScalar
apAppPortNumber = _ApAppPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 4),
    _ApAppPortNumber_Type()
)
apAppPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAppPortNumber.setStatus("current")


class _ApAppMaxFrameSize_Type(Integer32):
    """Custom type apAppMaxFrameSize based on Integer32"""
    defaultValue = 10240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10240, 65535),
    )


_ApAppMaxFrameSize_Type.__name__ = "Integer32"
_ApAppMaxFrameSize_Object = MibScalar
apAppMaxFrameSize = _ApAppMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 32, 5),
    _ApAppMaxFrameSize_Type()
)
apAppMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAppMaxFrameSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPEXT-MIB",
    **{"apAppMib": apAppMib,
       "apAppSessionTable": apAppSessionTable,
       "apAppSessionEntry": apAppSessionEntry,
       "apAppIpAddr": apAppIpAddr,
       "apAppAuthType": apAppAuthType,
       "apAppEncryptType": apAppEncryptType,
       "apAppKalFreq": apAppKalFreq,
       "apAppSecret": apAppSecret,
       "apAppPktsTx": apAppPktsTx,
       "apAppPktsRx": apAppPktsRx,
       "apAppSessionState": apAppSessionState,
       "apAppRcmdEnable": apAppRcmdEnable,
       "apAppSessionStatus": apAppSessionStatus,
       "apAppEnable": apAppEnable,
       "apAppPortNumber": apAppPortNumber,
       "apAppMaxFrameSize": apAppMaxFrameSize}
)
