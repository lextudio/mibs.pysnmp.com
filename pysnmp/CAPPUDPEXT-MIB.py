# SNMP MIB module (CAPPUDPEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAPPUDPEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:30 2024
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

(cappUdpExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "cappUdpExt")

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

apCappUdpExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApCappUdpState_Type(Integer32):
    """Custom type apCappUdpState based on Integer32"""
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


_ApCappUdpState_Type.__name__ = "Integer32"
_ApCappUdpState_Object = MibScalar
apCappUdpState = _ApCappUdpState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 2),
    _ApCappUdpState_Type()
)
apCappUdpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCappUdpState.setStatus("current")


class _ApCappUdpSecureAll_Type(Integer32):
    """Custom type apCappUdpSecureAll based on Integer32"""
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


_ApCappUdpSecureAll_Type.__name__ = "Integer32"
_ApCappUdpSecureAll_Object = MibScalar
apCappUdpSecureAll = _ApCappUdpSecureAll_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 3),
    _ApCappUdpSecureAll_Type()
)
apCappUdpSecureAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCappUdpSecureAll.setStatus("current")


class _ApCappUdpPort_Type(Integer32):
    """Custom type apCappUdpPort based on Integer32"""
    defaultValue = 5002


_ApCappUdpPort_Object = MibScalar
apCappUdpPort = _ApCappUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 4),
    _ApCappUdpPort_Type()
)
apCappUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCappUdpPort.setStatus("current")
_ApCappUdpDropFrames_Type = Integer32
_ApCappUdpDropFrames_Object = MibScalar
apCappUdpDropFrames = _ApCappUdpDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 5),
    _ApCappUdpDropFrames_Type()
)
apCappUdpDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCappUdpDropFrames.setStatus("current")
_ApCappUdpReceiveFrames_Type = Integer32
_ApCappUdpReceiveFrames_Object = MibScalar
apCappUdpReceiveFrames = _ApCappUdpReceiveFrames_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 6),
    _ApCappUdpReceiveFrames_Type()
)
apCappUdpReceiveFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCappUdpReceiveFrames.setStatus("current")
_ApCappUdpTransmitFrames_Type = Integer32
_ApCappUdpTransmitFrames_Object = MibScalar
apCappUdpTransmitFrames = _ApCappUdpTransmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 7),
    _ApCappUdpTransmitFrames_Type()
)
apCappUdpTransmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCappUdpTransmitFrames.setStatus("current")
_ApCappUdpDropBytes_Type = Integer32
_ApCappUdpDropBytes_Object = MibScalar
apCappUdpDropBytes = _ApCappUdpDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 8),
    _ApCappUdpDropBytes_Type()
)
apCappUdpDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCappUdpDropBytes.setStatus("current")
_ApCappUdpReceiveBytes_Type = Integer32
_ApCappUdpReceiveBytes_Object = MibScalar
apCappUdpReceiveBytes = _ApCappUdpReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 9),
    _ApCappUdpReceiveBytes_Type()
)
apCappUdpReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCappUdpReceiveBytes.setStatus("current")
_ApCappUdpTransmitBytes_Type = Integer32
_ApCappUdpTransmitBytes_Object = MibScalar
apCappUdpTransmitBytes = _ApCappUdpTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 10),
    _ApCappUdpTransmitBytes_Type()
)
apCappUdpTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCappUdpTransmitBytes.setStatus("current")
_ApCappUdpOptionsTable_Object = MibTable
apCappUdpOptionsTable = _ApCappUdpOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 11)
)
if mibBuilder.loadTexts:
    apCappUdpOptionsTable.setStatus("current")
_ApCappUdpOptionsEntry_Object = MibTableRow
apCappUdpOptionsEntry = _ApCappUdpOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 11, 1)
)
apCappUdpOptionsEntry.setIndexNames(
    (0, "CAPPUDPEXT-MIB", "apCappUdpOptionsIpAddress"),
)
if mibBuilder.loadTexts:
    apCappUdpOptionsEntry.setStatus("current")
_ApCappUdpOptionsIpAddress_Type = IpAddress
_ApCappUdpOptionsIpAddress_Object = MibTableColumn
apCappUdpOptionsIpAddress = _ApCappUdpOptionsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 11, 1, 1),
    _ApCappUdpOptionsIpAddress_Type()
)
apCappUdpOptionsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCappUdpOptionsIpAddress.setStatus("current")


class _ApCappUdpOptionsType_Type(Integer32):
    """Custom type apCappUdpOptionsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encrypt-md5", 1),
          ("encrypt-none", 0))
    )


_ApCappUdpOptionsType_Type.__name__ = "Integer32"
_ApCappUdpOptionsType_Object = MibTableColumn
apCappUdpOptionsType = _ApCappUdpOptionsType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 11, 1, 2),
    _ApCappUdpOptionsType_Type()
)
apCappUdpOptionsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCappUdpOptionsType.setStatus("current")


class _ApCappUdpOptionsSecret_Type(DisplayString):
    """Custom type apCappUdpOptionsSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCappUdpOptionsSecret_Type.__name__ = "DisplayString"
_ApCappUdpOptionsSecret_Object = MibTableColumn
apCappUdpOptionsSecret = _ApCappUdpOptionsSecret_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 11, 1, 3),
    _ApCappUdpOptionsSecret_Type()
)
apCappUdpOptionsSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCappUdpOptionsSecret.setStatus("current")
_ApCappUdpOptionsStatus_Type = RowStatus
_ApCappUdpOptionsStatus_Object = MibTableColumn
apCappUdpOptionsStatus = _ApCappUdpOptionsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 52, 11, 1, 4),
    _ApCappUdpOptionsStatus_Type()
)
apCappUdpOptionsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCappUdpOptionsStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAPPUDPEXT-MIB",
    **{"apCappUdpExtMib": apCappUdpExtMib,
       "apCappUdpState": apCappUdpState,
       "apCappUdpSecureAll": apCappUdpSecureAll,
       "apCappUdpPort": apCappUdpPort,
       "apCappUdpDropFrames": apCappUdpDropFrames,
       "apCappUdpReceiveFrames": apCappUdpReceiveFrames,
       "apCappUdpTransmitFrames": apCappUdpTransmitFrames,
       "apCappUdpDropBytes": apCappUdpDropBytes,
       "apCappUdpReceiveBytes": apCappUdpReceiveBytes,
       "apCappUdpTransmitBytes": apCappUdpTransmitBytes,
       "apCappUdpOptionsTable": apCappUdpOptionsTable,
       "apCappUdpOptionsEntry": apCappUdpOptionsEntry,
       "apCappUdpOptionsIpAddress": apCappUdpOptionsIpAddress,
       "apCappUdpOptionsType": apCappUdpOptionsType,
       "apCappUdpOptionsSecret": apCappUdpOptionsSecret,
       "apCappUdpOptionsStatus": apCappUdpOptionsStatus}
)
