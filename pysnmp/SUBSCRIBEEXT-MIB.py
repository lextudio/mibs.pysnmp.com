# SNMP MIB module (SUBSCRIBEEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUBSCRIBEEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:30 2024
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

(subscribeExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "subscribeExt")

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

apSubscribeExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApSubTable_Object = MibTable
apSubTable = _ApSubTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2)
)
if mibBuilder.loadTexts:
    apSubTable.setStatus("current")
_ApSubEntry_Object = MibTableRow
apSubEntry = _ApSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1)
)
apSubEntry.setIndexNames(
    (0, "SUBSCRIBEEXT-MIB", "apSubName"),
)
if mibBuilder.loadTexts:
    apSubEntry.setStatus("current")
_ApSubName_Type = DisplayString
_ApSubName_Object = MibTableColumn
apSubName = _ApSubName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 1),
    _ApSubName_Type()
)
apSubName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubName.setStatus("current")


class _ApSubState_Type(Integer32):
    """Custom type apSubState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("accessFail", 0),
          ("busy", 2),
          ("busyRetry", 3),
          ("down", 6),
          ("initializing", 7),
          ("invalid", 9),
          ("online", 4),
          ("ready", 1),
          ("suspended", 5),
          ("waitsConfig", 8))
    )


_ApSubState_Type.__name__ = "Integer32"
_ApSubState_Object = MibTableColumn
apSubState = _ApSubState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 2),
    _ApSubState_Type()
)
apSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubState.setStatus("current")
_ApSubAccessError_Type = DisplayString
_ApSubAccessError_Object = MibTableColumn
apSubAccessError = _ApSubAccessError_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 3),
    _ApSubAccessError_Type()
)
apSubAccessError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubAccessError.setStatus("current")
_ApSubAccessIP_Type = IpAddress
_ApSubAccessIP_Object = MibTableColumn
apSubAccessIP = _ApSubAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 4),
    _ApSubAccessIP_Type()
)
apSubAccessIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubAccessIP.setStatus("current")
_ApSubAccessUserName_Type = DisplayString
_ApSubAccessUserName_Object = MibTableColumn
apSubAccessUserName = _ApSubAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 5),
    _ApSubAccessUserName_Type()
)
apSubAccessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubAccessUserName.setStatus("current")
_ApSubSubscribedFiles_Type = Integer32
_ApSubSubscribedFiles_Object = MibTableColumn
apSubSubscribedFiles = _ApSubSubscribedFiles_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 6),
    _ApSubSubscribedFiles_Type()
)
apSubSubscribedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubSubscribedFiles.setStatus("current")
_ApSubLastMethod_Type = DisplayString
_ApSubLastMethod_Object = MibTableColumn
apSubLastMethod = _ApSubLastMethod_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 7),
    _ApSubLastMethod_Type()
)
apSubLastMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubLastMethod.setStatus("current")
_ApSubSynchronized_Type = Integer32
_ApSubSynchronized_Object = MibTableColumn
apSubSynchronized = _ApSubSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 8),
    _ApSubSynchronized_Type()
)
apSubSynchronized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubSynchronized.setStatus("current")


class _ApSubAccessType_Type(Integer32):
    """Custom type apSubAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 0),
          ("http", 1))
    )


_ApSubAccessType_Type.__name__ = "Integer32"
_ApSubAccessType_Object = MibTableColumn
apSubAccessType = _ApSubAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 9),
    _ApSubAccessType_Type()
)
apSubAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubAccessType.setStatus("current")
_ApSubAccessPort_Type = Integer32
_ApSubAccessPort_Object = MibTableColumn
apSubAccessPort = _ApSubAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 10),
    _ApSubAccessPort_Type()
)
apSubAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubAccessPort.setStatus("current")
_ApSubAccessBaseDir_Type = DisplayString
_ApSubAccessBaseDir_Object = MibTableColumn
apSubAccessBaseDir = _ApSubAccessBaseDir_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 11),
    _ApSubAccessBaseDir_Type()
)
apSubAccessBaseDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubAccessBaseDir.setStatus("current")
_ApSubSubscribedBytes_Type = Integer32
_ApSubSubscribedBytes_Object = MibTableColumn
apSubSubscribedBytes = _ApSubSubscribedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 12),
    _ApSubSubscribedBytes_Type()
)
apSubSubscribedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubSubscribedBytes.setStatus("current")
_ApSubLastTime_Type = DisplayString
_ApSubLastTime_Object = MibTableColumn
apSubLastTime = _ApSubLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 13),
    _ApSubLastTime_Type()
)
apSubLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSubLastTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUBSCRIBEEXT-MIB",
    **{"apSubscribeExtMib": apSubscribeExtMib,
       "apSubTable": apSubTable,
       "apSubEntry": apSubEntry,
       "apSubName": apSubName,
       "apSubState": apSubState,
       "apSubAccessError": apSubAccessError,
       "apSubAccessIP": apSubAccessIP,
       "apSubAccessUserName": apSubAccessUserName,
       "apSubSubscribedFiles": apSubSubscribedFiles,
       "apSubLastMethod": apSubLastMethod,
       "apSubSynchronized": apSubSynchronized,
       "apSubAccessType": apSubAccessType,
       "apSubAccessPort": apSubAccessPort,
       "apSubAccessBaseDir": apSubAccessBaseDir,
       "apSubSubscribedBytes": apSubSubscribedBytes,
       "apSubLastTime": apSubLastTime}
)
