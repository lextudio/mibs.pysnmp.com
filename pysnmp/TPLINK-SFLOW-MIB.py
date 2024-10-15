# SNMP MIB module (TPLINK-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-SFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:38 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkSflowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95)
)
tplinkSflowMIB.setRevisions(
        ("2015-09-23 10:07",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkSflowMIBObjects_ObjectIdentity = ObjectIdentity
tplinkSflowMIBObjects = _TplinkSflowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1)
)
_TpSflowGlobalConfig_ObjectIdentity = ObjectIdentity
tpSflowGlobalConfig = _TpSflowGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 1)
)


class _TpSflowGlobalConfigStatus_Type(Integer32):
    """Custom type tpSflowGlobalConfigStatus based on Integer32"""
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


_TpSflowGlobalConfigStatus_Type.__name__ = "Integer32"
_TpSflowGlobalConfigStatus_Object = MibScalar
tpSflowGlobalConfigStatus = _TpSflowGlobalConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 1, 1),
    _TpSflowGlobalConfigStatus_Type()
)
tpSflowGlobalConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowGlobalConfigStatus.setStatus("current")
_TpSflowGlobalConfigAddress_Type = IpAddress
_TpSflowGlobalConfigAddress_Object = MibScalar
tpSflowGlobalConfigAddress = _TpSflowGlobalConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 1, 2),
    _TpSflowGlobalConfigAddress_Type()
)
tpSflowGlobalConfigAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowGlobalConfigAddress.setStatus("current")
_TpSflowGlobalConfigVersion_Type = Integer32
_TpSflowGlobalConfigVersion_Object = MibScalar
tpSflowGlobalConfigVersion = _TpSflowGlobalConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 1, 3),
    _TpSflowGlobalConfigVersion_Type()
)
tpSflowGlobalConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSflowGlobalConfigVersion.setStatus("current")
_TpSflowCollector_ObjectIdentity = ObjectIdentity
tpSflowCollector = _TpSflowCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 2)
)
_TpSflowCollectorTable_Object = MibTable
tpSflowCollectorTable = _TpSflowCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpSflowCollectorTable.setStatus("current")
_TpSflowCollectorEntry_Object = MibTableRow
tpSflowCollectorEntry = _TpSflowCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 2, 1, 1)
)
tpSflowCollectorEntry.setIndexNames(
    (0, "TPLINK-SFLOW-MIB", "tpSflowCollectorCollectorId"),
)
if mibBuilder.loadTexts:
    tpSflowCollectorEntry.setStatus("current")
_TpSflowCollectorCollectorId_Type = Integer32
_TpSflowCollectorCollectorId_Object = MibTableColumn
tpSflowCollectorCollectorId = _TpSflowCollectorCollectorId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 2, 1, 1, 1),
    _TpSflowCollectorCollectorId_Type()
)
tpSflowCollectorCollectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSflowCollectorCollectorId.setStatus("current")
_TpSflowCollectorDescription_Type = DisplayString
_TpSflowCollectorDescription_Object = MibTableColumn
tpSflowCollectorDescription = _TpSflowCollectorDescription_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 2, 1, 1, 2),
    _TpSflowCollectorDescription_Type()
)
tpSflowCollectorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowCollectorDescription.setStatus("current")
_TpSflowCollectorCollectorIp_Type = IpAddress
_TpSflowCollectorCollectorIp_Object = MibTableColumn
tpSflowCollectorCollectorIp = _TpSflowCollectorCollectorIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 2, 1, 1, 3),
    _TpSflowCollectorCollectorIp_Type()
)
tpSflowCollectorCollectorIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowCollectorCollectorIp.setStatus("current")


class _TpSflowCollectorCollectorPort_Type(Integer32):
    """Custom type tpSflowCollectorCollectorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpSflowCollectorCollectorPort_Type.__name__ = "Integer32"
_TpSflowCollectorCollectorPort_Object = MibTableColumn
tpSflowCollectorCollectorPort = _TpSflowCollectorCollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 2, 1, 1, 4),
    _TpSflowCollectorCollectorPort_Type()
)
tpSflowCollectorCollectorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowCollectorCollectorPort.setStatus("current")


class _TpSflowCollectorMaxDatagram_Type(Integer32):
    """Custom type tpSflowCollectorMaxDatagram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1400),
    )


_TpSflowCollectorMaxDatagram_Type.__name__ = "Integer32"
_TpSflowCollectorMaxDatagram_Object = MibTableColumn
tpSflowCollectorMaxDatagram = _TpSflowCollectorMaxDatagram_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 2, 1, 1, 5),
    _TpSflowCollectorMaxDatagram_Type()
)
tpSflowCollectorMaxDatagram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowCollectorMaxDatagram.setStatus("current")


class _TpSflowCollectorTimeout_Type(Integer32):
    """Custom type tpSflowCollectorTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_TpSflowCollectorTimeout_Type.__name__ = "Integer32"
_TpSflowCollectorTimeout_Object = MibTableColumn
tpSflowCollectorTimeout = _TpSflowCollectorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 2, 1, 1, 6),
    _TpSflowCollectorTimeout_Type()
)
tpSflowCollectorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowCollectorTimeout.setStatus("current")
_TpSflowCollectorLifetime_Type = Integer32
_TpSflowCollectorLifetime_Object = MibTableColumn
tpSflowCollectorLifetime = _TpSflowCollectorLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 2, 1, 1, 7),
    _TpSflowCollectorLifetime_Type()
)
tpSflowCollectorLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSflowCollectorLifetime.setStatus("current")
_TpSflowSampler_ObjectIdentity = ObjectIdentity
tpSflowSampler = _TpSflowSampler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 3)
)
_TpSflowSamplerTable_Object = MibTable
tpSflowSamplerTable = _TpSflowSamplerTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpSflowSamplerTable.setStatus("current")
_TpSflowSamplerEntry_Object = MibTableRow
tpSflowSamplerEntry = _TpSflowSamplerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 3, 1, 1)
)
tpSflowSamplerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpSflowSamplerEntry.setStatus("current")
_TpSflowSamplerPort_Type = DisplayString
_TpSflowSamplerPort_Object = MibTableColumn
tpSflowSamplerPort = _TpSflowSamplerPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 3, 1, 1, 1),
    _TpSflowSamplerPort_Type()
)
tpSflowSamplerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSflowSamplerPort.setStatus("current")


class _TpSflowSamplerCollectorId_Type(Integer32):
    """Custom type tpSflowSamplerCollectorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TpSflowSamplerCollectorId_Type.__name__ = "Integer32"
_TpSflowSamplerCollectorId_Object = MibTableColumn
tpSflowSamplerCollectorId = _TpSflowSamplerCollectorId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 3, 1, 1, 2),
    _TpSflowSamplerCollectorId_Type()
)
tpSflowSamplerCollectorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowSamplerCollectorId.setStatus("current")


class _TpSflowSamplerIngRate_Type(Integer32):
    """Custom type tpSflowSamplerIngRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TpSflowSamplerIngRate_Type.__name__ = "Integer32"
_TpSflowSamplerIngRate_Object = MibTableColumn
tpSflowSamplerIngRate = _TpSflowSamplerIngRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 3, 1, 1, 3),
    _TpSflowSamplerIngRate_Type()
)
tpSflowSamplerIngRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowSamplerIngRate.setStatus("current")


class _TpSflowSamplerEgRate_Type(Integer32):
    """Custom type tpSflowSamplerEgRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TpSflowSamplerEgRate_Type.__name__ = "Integer32"
_TpSflowSamplerEgRate_Object = MibTableColumn
tpSflowSamplerEgRate = _TpSflowSamplerEgRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 3, 1, 1, 4),
    _TpSflowSamplerEgRate_Type()
)
tpSflowSamplerEgRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowSamplerEgRate.setStatus("current")


class _TpSflowSamplerMaxHeader_Type(Integer32):
    """Custom type tpSflowSamplerMaxHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 256),
    )


_TpSflowSamplerMaxHeader_Type.__name__ = "Integer32"
_TpSflowSamplerMaxHeader_Object = MibTableColumn
tpSflowSamplerMaxHeader = _TpSflowSamplerMaxHeader_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 3, 1, 1, 5),
    _TpSflowSamplerMaxHeader_Type()
)
tpSflowSamplerMaxHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSflowSamplerMaxHeader.setStatus("current")


class _TpSflowSamplerPortLag_Type(OctetString):
    """Custom type tpSflowSamplerPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpSflowSamplerPortLag_Type.__name__ = "OctetString"
_TpSflowSamplerPortLag_Object = MibTableColumn
tpSflowSamplerPortLag = _TpSflowSamplerPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 95, 1, 3, 1, 1, 6),
    _TpSflowSamplerPortLag_Type()
)
tpSflowSamplerPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSflowSamplerPortLag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SFLOW-MIB",
    **{"tplinkSflowMIB": tplinkSflowMIB,
       "tplinkSflowMIBObjects": tplinkSflowMIBObjects,
       "tpSflowGlobalConfig": tpSflowGlobalConfig,
       "tpSflowGlobalConfigStatus": tpSflowGlobalConfigStatus,
       "tpSflowGlobalConfigAddress": tpSflowGlobalConfigAddress,
       "tpSflowGlobalConfigVersion": tpSflowGlobalConfigVersion,
       "tpSflowCollector": tpSflowCollector,
       "tpSflowCollectorTable": tpSflowCollectorTable,
       "tpSflowCollectorEntry": tpSflowCollectorEntry,
       "tpSflowCollectorCollectorId": tpSflowCollectorCollectorId,
       "tpSflowCollectorDescription": tpSflowCollectorDescription,
       "tpSflowCollectorCollectorIp": tpSflowCollectorCollectorIp,
       "tpSflowCollectorCollectorPort": tpSflowCollectorCollectorPort,
       "tpSflowCollectorMaxDatagram": tpSflowCollectorMaxDatagram,
       "tpSflowCollectorTimeout": tpSflowCollectorTimeout,
       "tpSflowCollectorLifetime": tpSflowCollectorLifetime,
       "tpSflowSampler": tpSflowSampler,
       "tpSflowSamplerTable": tpSflowSamplerTable,
       "tpSflowSamplerEntry": tpSflowSamplerEntry,
       "tpSflowSamplerPort": tpSflowSamplerPort,
       "tpSflowSamplerCollectorId": tpSflowSamplerCollectorId,
       "tpSflowSamplerIngRate": tpSflowSamplerIngRate,
       "tpSflowSamplerEgRate": tpSflowSamplerEgRate,
       "tpSflowSamplerMaxHeader": tpSflowSamplerMaxHeader,
       "tpSflowSamplerPortLag": tpSflowSamplerPortLag}
)
