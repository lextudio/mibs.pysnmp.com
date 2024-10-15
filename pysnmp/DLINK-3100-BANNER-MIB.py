# SNMP MIB module (DLINK-3100-BANNER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-BANNER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:43 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

rlBanner = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133)
)
rlBanner.setRevisions(
        ("2007-12-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BannerMessageType(Integer32, TextualConvention):
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
        *(("rlBannerExec", 3),
          ("rlBannerLogin", 2),
          ("rlBannerMOTD", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlBannerMessageTable_Object = MibTable
rlBannerMessageTable = _RlBannerMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 1)
)
if mibBuilder.loadTexts:
    rlBannerMessageTable.setStatus("current")
_RlBannerMessageEntry_Object = MibTableRow
rlBannerMessageEntry = _RlBannerMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 1, 1)
)
rlBannerMessageEntry.setIndexNames(
    (0, "DLINK-3100-BANNER-MIB", "rlBannerMessageType"),
    (0, "DLINK-3100-BANNER-MIB", "rlBannerMessageIndex"),
)
if mibBuilder.loadTexts:
    rlBannerMessageEntry.setStatus("current")
_RlBannerMessageType_Type = BannerMessageType
_RlBannerMessageType_Object = MibTableColumn
rlBannerMessageType = _RlBannerMessageType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 1, 1, 1),
    _RlBannerMessageType_Type()
)
rlBannerMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBannerMessageType.setStatus("current")


class _RlBannerMessageIndex_Type(Integer32):
    """Custom type rlBannerMessageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_RlBannerMessageIndex_Type.__name__ = "Integer32"
_RlBannerMessageIndex_Object = MibTableColumn
rlBannerMessageIndex = _RlBannerMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 1, 1, 2),
    _RlBannerMessageIndex_Type()
)
rlBannerMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBannerMessageIndex.setStatus("current")
_RlBannerMessageText_Type = SnmpAdminString
_RlBannerMessageText_Object = MibTableColumn
rlBannerMessageText = _RlBannerMessageText_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 1, 1, 3),
    _RlBannerMessageText_Type()
)
rlBannerMessageText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBannerMessageText.setStatus("current")
_RlBannerManageTable_Object = MibTable
rlBannerManageTable = _RlBannerManageTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 2)
)
if mibBuilder.loadTexts:
    rlBannerManageTable.setStatus("current")
_RlBannerManageEntry_Object = MibTableRow
rlBannerManageEntry = _RlBannerManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 2, 1)
)
rlBannerManageEntry.setIndexNames(
    (0, "DLINK-3100-BANNER-MIB", "rlBannerMessageType"),
)
if mibBuilder.loadTexts:
    rlBannerManageEntry.setStatus("current")
_RlBannerManageSSH_Type = EnabledStatus
_RlBannerManageSSH_Object = MibTableColumn
rlBannerManageSSH = _RlBannerManageSSH_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 2, 1, 1),
    _RlBannerManageSSH_Type()
)
rlBannerManageSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBannerManageSSH.setStatus("current")
_RlBannerManageTelnet_Type = EnabledStatus
_RlBannerManageTelnet_Object = MibTableColumn
rlBannerManageTelnet = _RlBannerManageTelnet_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 2, 1, 2),
    _RlBannerManageTelnet_Type()
)
rlBannerManageTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBannerManageTelnet.setStatus("current")
_RlBannerManageConsole_Type = EnabledStatus
_RlBannerManageConsole_Object = MibTableColumn
rlBannerManageConsole = _RlBannerManageConsole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 2, 1, 3),
    _RlBannerManageConsole_Type()
)
rlBannerManageConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBannerManageConsole.setStatus("current")
_RlBannerMessageClear_Type = BannerMessageType
_RlBannerMessageClear_Object = MibScalar
rlBannerMessageClear = _RlBannerMessageClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 133, 3),
    _RlBannerMessageClear_Type()
)
rlBannerMessageClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBannerMessageClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-BANNER-MIB",
    **{"BannerMessageType": BannerMessageType,
       "rlBanner": rlBanner,
       "rlBannerMessageTable": rlBannerMessageTable,
       "rlBannerMessageEntry": rlBannerMessageEntry,
       "rlBannerMessageType": rlBannerMessageType,
       "rlBannerMessageIndex": rlBannerMessageIndex,
       "rlBannerMessageText": rlBannerMessageText,
       "rlBannerManageTable": rlBannerManageTable,
       "rlBannerManageEntry": rlBannerManageEntry,
       "rlBannerManageSSH": rlBannerManageSSH,
       "rlBannerManageTelnet": rlBannerManageTelnet,
       "rlBannerManageConsole": rlBannerManageConsole,
       "rlBannerMessageClear": rlBannerMessageClear}
)
