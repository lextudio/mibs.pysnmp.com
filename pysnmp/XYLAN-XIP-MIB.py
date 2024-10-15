# SNMP MIB module (XYLAN-XIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-XIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:20 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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

(xylanXIPArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanXIPArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanXIPGMAPconfig_ObjectIdentity = ObjectIdentity
xylanXIPGMAPconfig = _XylanXIPGMAPconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1)
)


class _XylanXIPGMAPstate_Type(Integer32):
    """Custom type xylanXIPGMAPstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_XylanXIPGMAPstate_Type.__name__ = "Integer32"
_XylanXIPGMAPstate_Object = MibScalar
xylanXIPGMAPstate = _XylanXIPGMAPstate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 1),
    _XylanXIPGMAPstate_Type()
)
xylanXIPGMAPstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanXIPGMAPstate.setStatus("mandatory")


class _XylanXIPGMAPgaptime_Type(Integer32):
    """Custom type xylanXIPGMAPgaptime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylanXIPGMAPgaptime_Type.__name__ = "Integer32"
_XylanXIPGMAPgaptime_Object = MibScalar
xylanXIPGMAPgaptime = _XylanXIPGMAPgaptime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 2),
    _XylanXIPGMAPgaptime_Type()
)
xylanXIPGMAPgaptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanXIPGMAPgaptime.setStatus("mandatory")


class _XylanXIPGMAPupdatetime_Type(Integer32):
    """Custom type xylanXIPGMAPupdatetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XylanXIPGMAPupdatetime_Type.__name__ = "Integer32"
_XylanXIPGMAPupdatetime_Object = MibScalar
xylanXIPGMAPupdatetime = _XylanXIPGMAPupdatetime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 3),
    _XylanXIPGMAPupdatetime_Type()
)
xylanXIPGMAPupdatetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanXIPGMAPupdatetime.setStatus("mandatory")


class _XylanXIPGMAPholdtime_Type(Integer32):
    """Custom type xylanXIPGMAPholdtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XylanXIPGMAPholdtime_Type.__name__ = "Integer32"
_XylanXIPGMAPholdtime_Object = MibScalar
xylanXIPGMAPholdtime = _XylanXIPGMAPholdtime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 4),
    _XylanXIPGMAPholdtime_Type()
)
xylanXIPGMAPholdtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanXIPGMAPholdtime.setStatus("mandatory")


class _XylanXIPGMAPLastTrapReason_Type(Integer32):
    """Custom type xylanXIPGMAPLastTrapReason based on Integer32"""
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
        *(("authenticated-group", 1),
          ("conflicting-binding-rule", 2),
          ("no-trap-sent", 0),
          ("non-mobile-group", 5),
          ("same-group-different-protocols-conflict", 4),
          ("same-proto-different-groups-conflict", 3))
    )


_XylanXIPGMAPLastTrapReason_Type.__name__ = "Integer32"
_XylanXIPGMAPLastTrapReason_Object = MibScalar
xylanXIPGMAPLastTrapReason = _XylanXIPGMAPLastTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 5),
    _XylanXIPGMAPLastTrapReason_Type()
)
xylanXIPGMAPLastTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPLastTrapReason.setStatus("mandatory")
_XylanXIPGMAPLastTrapPort_Type = Integer32
_XylanXIPGMAPLastTrapPort_Object = MibScalar
xylanXIPGMAPLastTrapPort = _XylanXIPGMAPLastTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 6),
    _XylanXIPGMAPLastTrapPort_Type()
)
xylanXIPGMAPLastTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPLastTrapPort.setStatus("mandatory")
_XylanXIPGMAPLastTrapMac_Type = MacAddress
_XylanXIPGMAPLastTrapMac_Object = MibScalar
xylanXIPGMAPLastTrapMac = _XylanXIPGMAPLastTrapMac_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 7),
    _XylanXIPGMAPLastTrapMac_Type()
)
xylanXIPGMAPLastTrapMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPLastTrapMac.setStatus("mandatory")
_XylanXIPGMAPLastTrapProtocol_Type = Integer32
_XylanXIPGMAPLastTrapProtocol_Object = MibScalar
xylanXIPGMAPLastTrapProtocol = _XylanXIPGMAPLastTrapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 8),
    _XylanXIPGMAPLastTrapProtocol_Type()
)
xylanXIPGMAPLastTrapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPLastTrapProtocol.setStatus("mandatory")
_XylanXIPGMAPLastTrapGroup_Type = Integer32
_XylanXIPGMAPLastTrapGroup_Object = MibScalar
xylanXIPGMAPLastTrapGroup = _XylanXIPGMAPLastTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 9),
    _XylanXIPGMAPLastTrapGroup_Type()
)
xylanXIPGMAPLastTrapGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPLastTrapGroup.setStatus("mandatory")
_XylanXIPGMAPTable_Object = MibTable
xylanXIPGMAPTable = _XylanXIPGMAPTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 10)
)
if mibBuilder.loadTexts:
    xylanXIPGMAPTable.setStatus("mandatory")
_XylanXIPGMAPTableEntry_Object = MibTableRow
xylanXIPGMAPTableEntry = _XylanXIPGMAPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 10, 1)
)
xylanXIPGMAPTableEntry.setIndexNames(
    (0, "XYLAN-XIP-MIB", "xylanXIPGMAPMacAddr"),
    (0, "XYLAN-XIP-MIB", "xylanXIPGMAPProtocol"),
)
if mibBuilder.loadTexts:
    xylanXIPGMAPTableEntry.setStatus("mandatory")
_XylanXIPGMAPMacAddr_Type = MacAddress
_XylanXIPGMAPMacAddr_Object = MibTableColumn
xylanXIPGMAPMacAddr = _XylanXIPGMAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 10, 1, 1),
    _XylanXIPGMAPMacAddr_Type()
)
xylanXIPGMAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPMacAddr.setStatus("mandatory")
_XylanXIPGMAPProtocol_Type = Integer32
_XylanXIPGMAPProtocol_Object = MibTableColumn
xylanXIPGMAPProtocol = _XylanXIPGMAPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 10, 1, 2),
    _XylanXIPGMAPProtocol_Type()
)
xylanXIPGMAPProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPProtocol.setStatus("mandatory")
_XylanXIPGMAPGroup_Type = Integer32
_XylanXIPGMAPGroup_Object = MibTableColumn
xylanXIPGMAPGroup = _XylanXIPGMAPGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 10, 1, 3),
    _XylanXIPGMAPGroup_Type()
)
xylanXIPGMAPGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPGroup.setStatus("mandatory")
_XylanXIPGMAPSrcSwitch_Type = MacAddress
_XylanXIPGMAPSrcSwitch_Object = MibTableColumn
xylanXIPGMAPSrcSwitch = _XylanXIPGMAPSrcSwitch_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 10, 1, 4),
    _XylanXIPGMAPSrcSwitch_Type()
)
xylanXIPGMAPSrcSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPSrcSwitch.setStatus("mandatory")


class _XylanXIPGMAPFlags_Type(OctetString):
    """Custom type xylanXIPGMAPFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanXIPGMAPFlags_Type.__name__ = "OctetString"
_XylanXIPGMAPFlags_Object = MibTableColumn
xylanXIPGMAPFlags = _XylanXIPGMAPFlags_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 10, 1, 5),
    _XylanXIPGMAPFlags_Type()
)
xylanXIPGMAPFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPFlags.setStatus("mandatory")
_XylanXIPGMAPTimeout_Type = Integer32
_XylanXIPGMAPTimeout_Object = MibTableColumn
xylanXIPGMAPTimeout = _XylanXIPGMAPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 1, 10, 1, 6),
    _XylanXIPGMAPTimeout_Type()
)
xylanXIPGMAPTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPGMAPTimeout.setStatus("mandatory")
_XylanXIPXMAPconfig_ObjectIdentity = ObjectIdentity
xylanXIPXMAPconfig = _XylanXIPXMAPconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2)
)


class _XylanXIPXMAPstate_Type(Integer32):
    """Custom type xylanXIPXMAPstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_XylanXIPXMAPstate_Type.__name__ = "Integer32"
_XylanXIPXMAPstate_Object = MibScalar
xylanXIPXMAPstate = _XylanXIPXMAPstate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 1),
    _XylanXIPXMAPstate_Type()
)
xylanXIPXMAPstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanXIPXMAPstate.setStatus("mandatory")


class _XylanXIPXMAPdisctime_Type(Integer32):
    """Custom type xylanXIPXMAPdisctime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XylanXIPXMAPdisctime_Type.__name__ = "Integer32"
_XylanXIPXMAPdisctime_Object = MibScalar
xylanXIPXMAPdisctime = _XylanXIPXMAPdisctime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 2),
    _XylanXIPXMAPdisctime_Type()
)
xylanXIPXMAPdisctime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanXIPXMAPdisctime.setStatus("mandatory")


class _XylanXIPXMAPcommontime_Type(Integer32):
    """Custom type xylanXIPXMAPcommontime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XylanXIPXMAPcommontime_Type.__name__ = "Integer32"
_XylanXIPXMAPcommontime_Object = MibScalar
xylanXIPXMAPcommontime = _XylanXIPXMAPcommontime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 3),
    _XylanXIPXMAPcommontime_Type()
)
xylanXIPXMAPcommontime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanXIPXMAPcommontime.setStatus("mandatory")


class _XylanXIPXMAPLastTrapReason_Type(Integer32):
    """Custom type xylanXIPXMAPLastTrapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("change", 2),
          ("no-trap-sent", 0),
          ("remove", 3))
    )


_XylanXIPXMAPLastTrapReason_Type.__name__ = "Integer32"
_XylanXIPXMAPLastTrapReason_Object = MibScalar
xylanXIPXMAPLastTrapReason = _XylanXIPXMAPLastTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 4),
    _XylanXIPXMAPLastTrapReason_Type()
)
xylanXIPXMAPLastTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPXMAPLastTrapReason.setStatus("mandatory")
_XylanXIPXMAPLastTrapPort_Type = Integer32
_XylanXIPXMAPLastTrapPort_Object = MibScalar
xylanXIPXMAPLastTrapPort = _XylanXIPXMAPLastTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 5),
    _XylanXIPXMAPLastTrapPort_Type()
)
xylanXIPXMAPLastTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPXMAPLastTrapPort.setStatus("mandatory")
_XylanXIPXMAPports_Object = MibTable
xylanXIPXMAPports = _XylanXIPXMAPports_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 6)
)
if mibBuilder.loadTexts:
    xylanXIPXMAPports.setStatus("mandatory")
_XylanXIPXMAPPortentry_Object = MibTableRow
xylanXIPXMAPPortentry = _XylanXIPXMAPPortentry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 6, 1)
)
xylanXIPXMAPPortentry.setIndexNames(
    (0, "XYLAN-XIP-MIB", "xylanXIPXMAPAdjPort"),
    (0, "XYLAN-XIP-MIB", "xylanXIPXMAPRemMac"),
    (0, "XYLAN-XIP-MIB", "xylanXIPXMAPRemPort"),
)
if mibBuilder.loadTexts:
    xylanXIPXMAPPortentry.setStatus("mandatory")
_XylanXIPXMAPAdjPort_Type = Integer32
_XylanXIPXMAPAdjPort_Object = MibTableColumn
xylanXIPXMAPAdjPort = _XylanXIPXMAPAdjPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 6, 1, 1),
    _XylanXIPXMAPAdjPort_Type()
)
xylanXIPXMAPAdjPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPXMAPAdjPort.setStatus("mandatory")
_XylanXIPXMAPRemMac_Type = MacAddress
_XylanXIPXMAPRemMac_Object = MibTableColumn
xylanXIPXMAPRemMac = _XylanXIPXMAPRemMac_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 6, 1, 2),
    _XylanXIPXMAPRemMac_Type()
)
xylanXIPXMAPRemMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPXMAPRemMac.setStatus("mandatory")
_XylanXIPXMAPRemPort_Type = Integer32
_XylanXIPXMAPRemPort_Object = MibTableColumn
xylanXIPXMAPRemPort = _XylanXIPXMAPRemPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 6, 1, 3),
    _XylanXIPXMAPRemPort_Type()
)
xylanXIPXMAPRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPXMAPRemPort.setStatus("mandatory")
_XylanXIPXMAPRemGroup_Type = Integer32
_XylanXIPXMAPRemGroup_Object = MibTableColumn
xylanXIPXMAPRemGroup = _XylanXIPXMAPRemGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 6, 1, 4),
    _XylanXIPXMAPRemGroup_Type()
)
xylanXIPXMAPRemGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPXMAPRemGroup.setStatus("mandatory")
_XylanXIPXMAPhosts_Object = MibTable
xylanXIPXMAPhosts = _XylanXIPXMAPhosts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 7)
)
if mibBuilder.loadTexts:
    xylanXIPXMAPhosts.setStatus("mandatory")
_XylanXIPXMAPHostentry_Object = MibTableRow
xylanXIPXMAPHostentry = _XylanXIPXMAPHostentry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 7, 1)
)
xylanXIPXMAPHostentry.setIndexNames(
    (0, "XYLAN-XIP-MIB", "xylanXIPXMAPHostMac"),
    (0, "XYLAN-XIP-MIB", "xylanXIPXMAPIpAddr"),
)
if mibBuilder.loadTexts:
    xylanXIPXMAPHostentry.setStatus("mandatory")
_XylanXIPXMAPHostMac_Type = MacAddress
_XylanXIPXMAPHostMac_Object = MibTableColumn
xylanXIPXMAPHostMac = _XylanXIPXMAPHostMac_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 7, 1, 1),
    _XylanXIPXMAPHostMac_Type()
)
xylanXIPXMAPHostMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPXMAPHostMac.setStatus("mandatory")
_XylanXIPXMAPIpAddr_Type = IpAddress
_XylanXIPXMAPIpAddr_Object = MibTableColumn
xylanXIPXMAPIpAddr = _XylanXIPXMAPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 20, 2, 7, 1, 2),
    _XylanXIPXMAPIpAddr_Type()
)
xylanXIPXMAPIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanXIPXMAPIpAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-XIP-MIB",
    **{"xylanXIPGMAPconfig": xylanXIPGMAPconfig,
       "xylanXIPGMAPstate": xylanXIPGMAPstate,
       "xylanXIPGMAPgaptime": xylanXIPGMAPgaptime,
       "xylanXIPGMAPupdatetime": xylanXIPGMAPupdatetime,
       "xylanXIPGMAPholdtime": xylanXIPGMAPholdtime,
       "xylanXIPGMAPLastTrapReason": xylanXIPGMAPLastTrapReason,
       "xylanXIPGMAPLastTrapPort": xylanXIPGMAPLastTrapPort,
       "xylanXIPGMAPLastTrapMac": xylanXIPGMAPLastTrapMac,
       "xylanXIPGMAPLastTrapProtocol": xylanXIPGMAPLastTrapProtocol,
       "xylanXIPGMAPLastTrapGroup": xylanXIPGMAPLastTrapGroup,
       "xylanXIPGMAPTable": xylanXIPGMAPTable,
       "xylanXIPGMAPTableEntry": xylanXIPGMAPTableEntry,
       "xylanXIPGMAPMacAddr": xylanXIPGMAPMacAddr,
       "xylanXIPGMAPProtocol": xylanXIPGMAPProtocol,
       "xylanXIPGMAPGroup": xylanXIPGMAPGroup,
       "xylanXIPGMAPSrcSwitch": xylanXIPGMAPSrcSwitch,
       "xylanXIPGMAPFlags": xylanXIPGMAPFlags,
       "xylanXIPGMAPTimeout": xylanXIPGMAPTimeout,
       "xylanXIPXMAPconfig": xylanXIPXMAPconfig,
       "xylanXIPXMAPstate": xylanXIPXMAPstate,
       "xylanXIPXMAPdisctime": xylanXIPXMAPdisctime,
       "xylanXIPXMAPcommontime": xylanXIPXMAPcommontime,
       "xylanXIPXMAPLastTrapReason": xylanXIPXMAPLastTrapReason,
       "xylanXIPXMAPLastTrapPort": xylanXIPXMAPLastTrapPort,
       "xylanXIPXMAPports": xylanXIPXMAPports,
       "xylanXIPXMAPPortentry": xylanXIPXMAPPortentry,
       "xylanXIPXMAPAdjPort": xylanXIPXMAPAdjPort,
       "xylanXIPXMAPRemMac": xylanXIPXMAPRemMac,
       "xylanXIPXMAPRemPort": xylanXIPXMAPRemPort,
       "xylanXIPXMAPRemGroup": xylanXIPXMAPRemGroup,
       "xylanXIPXMAPhosts": xylanXIPXMAPhosts,
       "xylanXIPXMAPHostentry": xylanXIPXMAPHostentry,
       "xylanXIPXMAPHostMac": xylanXIPXMAPHostMac,
       "xylanXIPXMAPIpAddr": xylanXIPXMAPIpAddr}
)
