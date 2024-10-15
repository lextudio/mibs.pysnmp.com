# SNMP MIB module (CXCommonConsole-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXCommonConsole-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:15 2024
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

(Alias,
 cxCommonConsole) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxCommonConsole")

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



class _CxCcInactivityTimer_Type(Integer32):
    """Custom type cxCcInactivityTimer based on Integer32"""
    defaultValue = 300


_CxCcInactivityTimer_Object = MibScalar
cxCcInactivityTimer = _CxCcInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 1),
    _CxCcInactivityTimer_Type()
)
cxCcInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCcInactivityTimer.setStatus("mandatory")


class _CxCcPassword_Type(DisplayString):
    """Custom type cxCcPassword based on DisplayString"""
    defaultValue = OctetString("Supervisor")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 16),
    )


_CxCcPassword_Type.__name__ = "DisplayString"
_CxCcPassword_Object = MibScalar
cxCcPassword = _CxCcPassword_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 2),
    _CxCcPassword_Type()
)
cxCcPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cxCcPassword.setStatus("mandatory")


class _CxCcPrompt_Type(DisplayString):
    """Custom type cxCcPrompt based on DisplayString"""
    defaultValue = OctetString("Common Console")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CxCcPrompt_Type.__name__ = "DisplayString"
_CxCcPrompt_Object = MibScalar
cxCcPrompt = _CxCcPrompt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 3),
    _CxCcPrompt_Type()
)
cxCcPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCcPrompt.setStatus("mandatory")


class _CxCcLogDevice_Type(Integer32):
    """Custom type cxCcLogDevice based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CxCcLogDevice_Type.__name__ = "Integer32"
_CxCcLogDevice_Object = MibScalar
cxCcLogDevice = _CxCcLogDevice_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 4),
    _CxCcLogDevice_Type()
)
cxCcLogDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCcLogDevice.setStatus("mandatory")


class _CxCcLogDeviceSlot_Type(Integer32):
    """Custom type cxCcLogDeviceSlot based on Integer32"""
    defaultValue = 0


_CxCcLogDeviceSlot_Object = MibScalar
cxCcLogDeviceSlot = _CxCcLogDeviceSlot_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 5),
    _CxCcLogDeviceSlot_Type()
)
cxCcLogDeviceSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCcLogDeviceSlot.setStatus("mandatory")


class _CxCcQueueDepth_Type(Integer32):
    """Custom type cxCcQueueDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CxCcQueueDepth_Type.__name__ = "Integer32"
_CxCcQueueDepth_Object = MibScalar
cxCcQueueDepth = _CxCcQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 6),
    _CxCcQueueDepth_Type()
)
cxCcQueueDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCcQueueDepth.setStatus("mandatory")
_CxCcRemoteTable_Object = MibTable
cxCcRemoteTable = _CxCcRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 7)
)
if mibBuilder.loadTexts:
    cxCcRemoteTable.setStatus("mandatory")
_CxCcRemoteEntry_Object = MibTableRow
cxCcRemoteEntry = _CxCcRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 7, 1)
)
cxCcRemoteEntry.setIndexNames(
    (0, "CXCommonConsole-MIB", "cxCcRemoteIndex"),
)
if mibBuilder.loadTexts:
    cxCcRemoteEntry.setStatus("mandatory")
_CxCcRemoteIndex_Type = Integer32
_CxCcRemoteIndex_Object = MibTableColumn
cxCcRemoteIndex = _CxCcRemoteIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 7, 1, 1),
    _CxCcRemoteIndex_Type()
)
cxCcRemoteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCcRemoteIndex.setStatus("mandatory")
_CxCcRemoteDestAlias_Type = Alias
_CxCcRemoteDestAlias_Object = MibTableColumn
cxCcRemoteDestAlias = _CxCcRemoteDestAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 7, 1, 2),
    _CxCcRemoteDestAlias_Type()
)
cxCcRemoteDestAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCcRemoteDestAlias.setStatus("mandatory")


class _CxCcRemoteRowStatus_Type(Integer32):
    """Custom type cxCcRemoteRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxCcRemoteRowStatus_Type.__name__ = "Integer32"
_CxCcRemoteRowStatus_Object = MibTableColumn
cxCcRemoteRowStatus = _CxCcRemoteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14, 7, 1, 3),
    _CxCcRemoteRowStatus_Type()
)
cxCcRemoteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCcRemoteRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXCommonConsole-MIB",
    **{"cxCcInactivityTimer": cxCcInactivityTimer,
       "cxCcPassword": cxCcPassword,
       "cxCcPrompt": cxCcPrompt,
       "cxCcLogDevice": cxCcLogDevice,
       "cxCcLogDeviceSlot": cxCcLogDeviceSlot,
       "cxCcQueueDepth": cxCcQueueDepth,
       "cxCcRemoteTable": cxCcRemoteTable,
       "cxCcRemoteEntry": cxCcRemoteEntry,
       "cxCcRemoteIndex": cxCcRemoteIndex,
       "cxCcRemoteDestAlias": cxCcRemoteDestAlias,
       "cxCcRemoteRowStatus": cxCcRemoteRowStatus}
)
