# SNMP MIB module (CADANT-CMTS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:51 2024
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

(cadSystem,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadSystem")

(AdminSrcAddrType,
 AdminState,
 CardId,
 OverloadThreshold,
 ServerType) = mibBuilder.importSymbols(
    "CADANT-TC",
    "AdminSrcAddrType",
    "AdminState",
    "CardId",
    "OverloadThreshold",
    "ServerType")

(TenthdB,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB")

(BitRate,) = mibBuilder.importSymbols(
    "DOCS-QOS3-MIB",
    "BitRate")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressType")

(SnmpAdminString,
 SnmpEngineID) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1)
)
cadSystemMib.setRevisions(
        ("2015-11-11 00:00",
         "2015-11-06 00:00",
         "2015-09-10 00:00",
         "2015-07-21 00:00",
         "2015-06-03 00:00",
         "2015-03-30 00:00",
         "2015-03-05 00:00",
         "2014-10-07 00:00",
         "2014-08-05 00:00",
         "2014-06-10 00:00",
         "2014-05-29 00:00",
         "2014-05-21 00:00",
         "2014-05-14 00:00",
         "2014-04-25 00:00",
         "2014-04-10 00:00",
         "2014-03-13 00:00",
         "2014-03-06 00:00",
         "2014-02-21 00:00",
         "2014-01-16 00:00",
         "2013-11-19 00:00",
         "2013-09-06 00:00",
         "2013-08-13 00:00",
         "2013-07-22 00:00",
         "2013-07-10 00:00",
         "2013-07-01 00:00",
         "2013-06-21 00:00",
         "2013-06-20 00:00",
         "2013-06-19 00:00",
         "2013-05-15 00:00",
         "2013-01-08 00:00",
         "2012-12-03 00:00",
         "2012-11-30 00:00",
         "2012-11-15 00:00",
         "2012-10-04 00:00",
         "2012-10-01 00:00",
         "2012-06-15 00:00",
         "2012-03-22 00:00",
         "2012-03-04 00:00",
         "2012-02-23 00:00",
         "2012-02-08 00:00",
         "2012-01-18 00:00",
         "2011-12-13 00:00",
         "2011-11-17 00:00",
         "2011-11-08 00:00",
         "2011-11-04 00:00",
         "2011-07-08 00:00",
         "2011-05-22 00:00",
         "2011-04-05 00:00",
         "2011-03-03 00:00",
         "2011-02-23 00:00",
         "2010-12-22 00:00",
         "2010-12-10 00:00",
         "2010-12-01 00:00",
         "2010-11-18 00:00",
         "2010-09-22 00:00",
         "2010-09-15 00:00",
         "2010-09-02 00:00",
         "2010-07-31 00:00",
         "2010-07-21 00:00",
         "2010-07-12 00:00",
         "2010-03-15 00:00",
         "2010-02-23 00:00",
         "2010-02-11 00:00",
         "2010-01-08 00:00",
         "2009-10-08 00:00",
         "2009-09-22 00:00",
         "2009-09-14 00:00",
         "2009-08-17 00:00",
         "2009-05-04 00:00",
         "2009-04-22 00:00",
         "2009-01-23 00:00",
         "2008-12-18 00:00",
         "2008-12-08 00:00",
         "2008-10-22 00:00",
         "2008-09-24 00:00",
         "2008-09-15 00:00",
         "2008-08-28 00:00",
         "2008-03-17 00:00",
         "2008-02-19 00:00",
         "2008-02-04 00:00",
         "2007-12-02 00:00",
         "2006-11-09 00:00",
         "2006-08-29 00:00",
         "2006-08-10 00:00",
         "2006-07-12 00:00",
         "2006-02-22 00:00",
         "2006-01-25 00:00",
         "2006-01-12 00:00",
         "2006-01-03 00:00",
         "2005-09-23 00:00",
         "2005-09-21 00:00",
         "2005-08-30 00:00",
         "2005-08-24 00:00",
         "2005-08-08 00:00",
         "2005-07-11 00:00",
         "2005-06-20 00:00",
         "2005-06-08 00:00",
         "2005-05-18 00:00",
         "2005-04-21 00:00",
         "2005-04-14 00:00",
         "2005-03-01 00:00",
         "2005-01-06 00:00",
         "2004-12-03 00:00",
         "2004-10-12 00:00",
         "2004-09-22 00:00",
         "2004-04-30 00:00",
         "2004-04-13 00:00",
         "2004-03-23 00:00",
         "2004-02-23 00:00",
         "2004-02-20 00:00",
         "2003-12-05 00:00",
         "2003-10-28 00:00",
         "2003-10-21 00:00",
         "2003-10-20 00:00",
         "2003-08-26 00:00",
         "2003-08-25 00:00",
         "2003-08-18 00:00",
         "2003-08-06 00:00",
         "2003-06-16 00:00",
         "2003-05-23 00:00",
         "2003-05-08 00:00",
         "2003-04-30 00:00",
         "2003-04-20 00:00",
         "2003-04-14 00:00",
         "2003-03-20 00:00",
         "2003-03-14 00:00",
         "2003-03-07 00:00",
         "2003-02-14 00:00",
         "2002-12-12 00:00",
         "2002-11-22 00:00",
         "2002-11-20 00:00",
         "2002-10-04 00:00",
         "2002-10-03 00:00",
         "2002-07-02 00:00",
         "2002-04-25 00:00",
         "2002-04-23 00:00",
         "2002-04-22 00:00",
         "2002-04-02 00:01",
         "2002-04-02 00:00",
         "2002-01-15 00:00",
         "2001-11-07 00:00",
         "2001-08-18 00:00",
         "2001-07-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadSysParams_ObjectIdentity = ObjectIdentity
cadSysParams = _CadSysParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1)
)


class _CadSysSyncInterval_Type(Integer32):
    """Custom type cadSysSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CadSysSyncInterval_Type.__name__ = "Integer32"
_CadSysSyncInterval_Object = MibScalar
cadSysSyncInterval = _CadSysSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 1),
    _CadSysSyncInterval_Type()
)
cadSysSyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadSysSyncInterval.setUnits("Milliseconds")


class _CadSysUCDInterval_Type(Integer32):
    """Custom type cadSysUCDInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_CadSysUCDInterval_Type.__name__ = "Integer32"
_CadSysUCDInterval_Object = MibScalar
cadSysUCDInterval = _CadSysUCDInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 2),
    _CadSysUCDInterval_Type()
)
cadSysUCDInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysUCDInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadSysUCDInterval.setUnits("Milliseconds")


class _CadSysMaxMAPPending_Type(Integer32):
    """Custom type cadSysMaxMAPPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CadSysMaxMAPPending_Type.__name__ = "Integer32"
_CadSysMaxMAPPending_Object = MibScalar
cadSysMaxMAPPending = _CadSysMaxMAPPending_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 3),
    _CadSysMaxMAPPending_Type()
)
cadSysMaxMAPPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysMaxMAPPending.setStatus("current")


class _CadSysRangingInterval_Type(Integer32):
    """Custom type cadSysRangingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_CadSysRangingInterval_Type.__name__ = "Integer32"
_CadSysRangingInterval_Object = MibScalar
cadSysRangingInterval = _CadSysRangingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 4),
    _CadSysRangingInterval_Type()
)
cadSysRangingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysRangingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadSysRangingInterval.setUnits("Milliseconds")


class _CadSysInvitedRangingRetries_Type(Integer32):
    """Custom type cadSysInvitedRangingRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
    )


_CadSysInvitedRangingRetries_Type.__name__ = "Integer32"
_CadSysInvitedRangingRetries_Object = MibScalar
cadSysInvitedRangingRetries = _CadSysInvitedRangingRetries_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 5),
    _CadSysInvitedRangingRetries_Type()
)
cadSysInvitedRangingRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysInvitedRangingRetries.setStatus("current")


class _CadSysRegistrationRequestRetries_Type(Integer32):
    """Custom type cadSysRegistrationRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
    )


_CadSysRegistrationRequestRetries_Type.__name__ = "Integer32"
_CadSysRegistrationRequestRetries_Object = MibScalar
cadSysRegistrationRequestRetries = _CadSysRegistrationRequestRetries_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 6),
    _CadSysRegistrationRequestRetries_Type()
)
cadSysRegistrationRequestRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysRegistrationRequestRetries.setStatus("current")


class _CadSysCMMAPProcessingTime_Type(Integer32):
    """Custom type cadSysCMMAPProcessingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 2000),
    )


_CadSysCMMAPProcessingTime_Type.__name__ = "Integer32"
_CadSysCMMAPProcessingTime_Object = MibScalar
cadSysCMMAPProcessingTime = _CadSysCMMAPProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 7),
    _CadSysCMMAPProcessingTime_Type()
)
cadSysCMMAPProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysCMMAPProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    cadSysCMMAPProcessingTime.setUnits("Microseconds")


class _CadSysCMRangingResponseProcessingTime_Type(Integer32):
    """Custom type cadSysCMRangingResponseProcessingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CadSysCMRangingResponseProcessingTime_Type.__name__ = "Integer32"
_CadSysCMRangingResponseProcessingTime_Object = MibScalar
cadSysCMRangingResponseProcessingTime = _CadSysCMRangingResponseProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 8),
    _CadSysCMRangingResponseProcessingTime_Type()
)
cadSysCMRangingResponseProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysCMRangingResponseProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    cadSysCMRangingResponseProcessingTime.setUnits("Milliseconds")


class _CadSysCMConfiguration_Type(Integer32):
    """Custom type cadSysCMConfiguration based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 2000),
    )


_CadSysCMConfiguration_Type.__name__ = "Integer32"
_CadSysCMConfiguration_Object = MibScalar
cadSysCMConfiguration = _CadSysCMConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 9),
    _CadSysCMConfiguration_Type()
)
cadSysCMConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysCMConfiguration.setStatus("current")
if mibBuilder.loadTexts:
    cadSysCMConfiguration.setUnits("Seconds")


class _CadSysT5Timeout_Type(Integer32):
    """Custom type cadSysT5Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_CadSysT5Timeout_Type.__name__ = "Integer32"
_CadSysT5Timeout_Object = MibScalar
cadSysT5Timeout = _CadSysT5Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 10),
    _CadSysT5Timeout_Type()
)
cadSysT5Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysT5Timeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysT5Timeout.setUnits("Milliseconds")


class _CadSysT6Timeout_Type(Integer32):
    """Custom type cadSysT6Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CadSysT6Timeout_Type.__name__ = "Integer32"
_CadSysT6Timeout_Object = MibScalar
cadSysT6Timeout = _CadSysT6Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 11),
    _CadSysT6Timeout_Type()
)
cadSysT6Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysT6Timeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysT6Timeout.setUnits("Milliseconds")


class _CadSysMiniSlotSize_Type(Integer32):
    """Custom type cadSysMiniSlotSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 300),
    )


_CadSysMiniSlotSize_Type.__name__ = "Integer32"
_CadSysMiniSlotSize_Object = MibScalar
cadSysMiniSlotSize = _CadSysMiniSlotSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 12),
    _CadSysMiniSlotSize_Type()
)
cadSysMiniSlotSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysMiniSlotSize.setStatus("current")


class _CadSysDSxRequestRetries_Type(Integer32):
    """Custom type cadSysDSxRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
    )


_CadSysDSxRequestRetries_Type.__name__ = "Integer32"
_CadSysDSxRequestRetries_Object = MibScalar
cadSysDSxRequestRetries = _CadSysDSxRequestRetries_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 13),
    _CadSysDSxRequestRetries_Type()
)
cadSysDSxRequestRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysDSxRequestRetries.setStatus("current")


class _CadSysDSxResponseRetries_Type(Integer32):
    """Custom type cadSysDSxResponseRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
    )


_CadSysDSxResponseRetries_Type.__name__ = "Integer32"
_CadSysDSxResponseRetries_Object = MibScalar
cadSysDSxResponseRetries = _CadSysDSxResponseRetries_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 14),
    _CadSysDSxResponseRetries_Type()
)
cadSysDSxResponseRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysDSxResponseRetries.setStatus("current")


class _CadSysT7Timeout_Type(Integer32):
    """Custom type cadSysT7Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CadSysT7Timeout_Type.__name__ = "Integer32"
_CadSysT7Timeout_Object = MibScalar
cadSysT7Timeout = _CadSysT7Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 15),
    _CadSysT7Timeout_Type()
)
cadSysT7Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysT7Timeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysT7Timeout.setUnits("Milliseconds")


class _CadSysT8Timeout_Type(Integer32):
    """Custom type cadSysT8Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CadSysT8Timeout_Type.__name__ = "Integer32"
_CadSysT8Timeout_Object = MibScalar
cadSysT8Timeout = _CadSysT8Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 16),
    _CadSysT8Timeout_Type()
)
cadSysT8Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysT8Timeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysT8Timeout.setUnits("Milliseconds")


class _CadSysT9Timeout_Type(Integer32):
    """Custom type cadSysT9Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1500),
    )


_CadSysT9Timeout_Type.__name__ = "Integer32"
_CadSysT9Timeout_Object = MibScalar
cadSysT9Timeout = _CadSysT9Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 17),
    _CadSysT9Timeout_Type()
)
cadSysT9Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysT9Timeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysT9Timeout.setUnits("Minutes")


class _CadSysT10Timeout_Type(Integer32):
    """Custom type cadSysT10Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CadSysT10Timeout_Type.__name__ = "Integer32"
_CadSysT10Timeout_Object = MibScalar
cadSysT10Timeout = _CadSysT10Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 18),
    _CadSysT10Timeout_Type()
)
cadSysT10Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysT10Timeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysT10Timeout.setUnits("Milliseconds")


class _CadSysT11Timeout_Type(Integer32):
    """Custom type cadSysT11Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CadSysT11Timeout_Type.__name__ = "Integer32"
_CadSysT11Timeout_Object = MibScalar
cadSysT11Timeout = _CadSysT11Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 19),
    _CadSysT11Timeout_Type()
)
cadSysT11Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysT11Timeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysT11Timeout.setUnits("Milliseconds")


class _CadSysT13Timeout_Type(Integer32):
    """Custom type cadSysT13Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CadSysT13Timeout_Type.__name__ = "Integer32"
_CadSysT13Timeout_Object = MibScalar
cadSysT13Timeout = _CadSysT13Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 20),
    _CadSysT13Timeout_Type()
)
cadSysT13Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysT13Timeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysT13Timeout.setUnits("Milliseconds")


class _CadSysDCCREQRetries_Type(Integer32):
    """Custom type cadSysDCCREQRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
    )


_CadSysDCCREQRetries_Type.__name__ = "Integer32"
_CadSysDCCREQRetries_Object = MibScalar
cadSysDCCREQRetries = _CadSysDCCREQRetries_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 21),
    _CadSysDCCREQRetries_Type()
)
cadSysDCCREQRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysDCCREQRetries.setStatus("current")
_CadSysMICEnable_Type = TruthValue
_CadSysMICEnable_Object = MibScalar
cadSysMICEnable = _CadSysMICEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 22),
    _CadSysMICEnable_Type()
)
cadSysMICEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMICEnable.setStatus("current")


class _CadSysMICAuthString_Type(OctetString):
    """Custom type cadSysMICAuthString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadSysMICAuthString_Type.__name__ = "OctetString"
_CadSysMICAuthString_Object = MibScalar
cadSysMICAuthString = _CadSysMICAuthString_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 23),
    _CadSysMICAuthString_Type()
)
cadSysMICAuthString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMICAuthString.setStatus("current")


class _CadSysAutoRecoveryEnable_Type(TruthValue):
    """Custom type cadSysAutoRecoveryEnable based on TruthValue"""


_CadSysAutoRecoveryEnable_Object = MibScalar
cadSysAutoRecoveryEnable = _CadSysAutoRecoveryEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 24),
    _CadSysAutoRecoveryEnable_Type()
)
cadSysAutoRecoveryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysAutoRecoveryEnable.setStatus("current")


class _CadSysActiveIpAddress_Type(IpAddress):
    """Custom type cadSysActiveIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_CadSysActiveIpAddress_Object = MibScalar
cadSysActiveIpAddress = _CadSysActiveIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 25),
    _CadSysActiveIpAddress_Type()
)
cadSysActiveIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysActiveIpAddress.setStatus("current")


class _CadSysSpOperMode_Type(Bits):
    """Custom type cadSysSpOperMode based on Bits"""
    defaultBinValue = "11101111111110111111111111111111"

    namedValues = NamedValues(
        *(("adjrxpwrctl", 1),
          ("bpiDynamicMulticastOff", 22),
          ("bpiHybridOff", 27),
          ("cmstatusoperational", 11),
          ("cpeNacksForceCmReset", 5),
          ("docsis10plusOff", 23),
          ("docsis20test", 13),
          ("docsis30ReqTxPolicyChkOff", 29),
          ("downstreamOverrideOn", 24),
          ("dqossf10cms", 0),
          ("enbudptcpfltr", 2),
          ("limitUsRngRspFreqOff", 9),
          ("loadBalUnbondedVoipOn", 6),
          ("ofdmSparingCleanupOff", 8),
          ("oneDCmDSMaxTrafBurstOn", 28),
          ("reserved10", 10),
          ("reserved12", 12),
          ("reserved14", 14),
          ("reserved15", 15),
          ("reserved16", 16),
          ("reserved17", 17),
          ("reserved18", 18),
          ("reserved19", 19),
          ("reserved20", 20),
          ("reserved30", 30),
          ("reserved31", 31),
          ("showCmFormatCVOff", 21),
          ("supressDCDOff", 25),
          ("upDownTrapIfDescrOff", 7),
          ("upce", 3),
          ("use16ForDSPeakTrafficRate", 4),
          ("virtualCmOff", 26))
    )

_CadSysSpOperMode_Type.__name__ = "Bits"
_CadSysSpOperMode_Object = MibScalar
cadSysSpOperMode = _CadSysSpOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 26),
    _CadSysSpOperMode_Type()
)
cadSysSpOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysSpOperMode.setStatus("current")


class _CadSysCountsCollectionRate_Type(Unsigned32):
    """Custom type cadSysCountsCollectionRate based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(15, 1440),
    )


_CadSysCountsCollectionRate_Type.__name__ = "Unsigned32"
_CadSysCountsCollectionRate_Object = MibScalar
cadSysCountsCollectionRate = _CadSysCountsCollectionRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 27),
    _CadSysCountsCollectionRate_Type()
)
cadSysCountsCollectionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysCountsCollectionRate.setStatus("current")


class _CadSysMaxQoSActiveTimeout_Type(Integer32):
    """Custom type cadSysMaxQoSActiveTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysMaxQoSActiveTimeout_Type.__name__ = "Integer32"
_CadSysMaxQoSActiveTimeout_Object = MibScalar
cadSysMaxQoSActiveTimeout = _CadSysMaxQoSActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 28),
    _CadSysMaxQoSActiveTimeout_Type()
)
cadSysMaxQoSActiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMaxQoSActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysMaxQoSActiveTimeout.setUnits("seconds")


class _CadSysMaxQoSAdmittedTimeout_Type(Integer32):
    """Custom type cadSysMaxQoSAdmittedTimeout based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysMaxQoSAdmittedTimeout_Type.__name__ = "Integer32"
_CadSysMaxQoSAdmittedTimeout_Object = MibScalar
cadSysMaxQoSAdmittedTimeout = _CadSysMaxQoSAdmittedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 29),
    _CadSysMaxQoSAdmittedTimeout_Type()
)
cadSysMaxQoSAdmittedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMaxQoSAdmittedTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysMaxQoSAdmittedTimeout.setUnits("seconds")


class _CadSysAllow10CmConcatenation_Type(TruthValue):
    """Custom type cadSysAllow10CmConcatenation based on TruthValue"""


_CadSysAllow10CmConcatenation_Object = MibScalar
cadSysAllow10CmConcatenation = _CadSysAllow10CmConcatenation_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 30),
    _CadSysAllow10CmConcatenation_Type()
)
cadSysAllow10CmConcatenation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysAllow10CmConcatenation.setStatus("current")


class _CadSysAllow10CmFragmentation_Type(TruthValue):
    """Custom type cadSysAllow10CmFragmentation based on TruthValue"""


_CadSysAllow10CmFragmentation_Object = MibScalar
cadSysAllow10CmFragmentation = _CadSysAllow10CmFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 31),
    _CadSysAllow10CmFragmentation_Type()
)
cadSysAllow10CmFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysAllow10CmFragmentation.setStatus("current")


class _CadSysPercentAddtlDsBwAllocated_Type(Integer32):
    """Custom type cadSysPercentAddtlDsBwAllocated based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CadSysPercentAddtlDsBwAllocated_Type.__name__ = "Integer32"
_CadSysPercentAddtlDsBwAllocated_Object = MibScalar
cadSysPercentAddtlDsBwAllocated = _CadSysPercentAddtlDsBwAllocated_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 32),
    _CadSysPercentAddtlDsBwAllocated_Type()
)
cadSysPercentAddtlDsBwAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysPercentAddtlDsBwAllocated.setStatus("current")


class _CadSysMaxTrafBurstFor11CMs_Type(Integer32):
    """Custom type cadSysMaxTrafBurstFor11CMs based on Integer32"""
    defaultValue = 128000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CadSysMaxTrafBurstFor11CMs_Type.__name__ = "Integer32"
_CadSysMaxTrafBurstFor11CMs_Object = MibScalar
cadSysMaxTrafBurstFor11CMs = _CadSysMaxTrafBurstFor11CMs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 33),
    _CadSysMaxTrafBurstFor11CMs_Type()
)
cadSysMaxTrafBurstFor11CMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMaxTrafBurstFor11CMs.setStatus("current")


class _CadSysFanSpeedControlEnable_Type(TruthValue):
    """Custom type cadSysFanSpeedControlEnable based on TruthValue"""


_CadSysFanSpeedControlEnable_Object = MibScalar
cadSysFanSpeedControlEnable = _CadSysFanSpeedControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 34),
    _CadSysFanSpeedControlEnable_Type()
)
cadSysFanSpeedControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysFanSpeedControlEnable.setStatus("obsolete")


class _CadSysFlaplistPowerAdjustThreshold_Type(TenthdB):
    """Custom type cadSysFlaplistPowerAdjustThreshold based on TenthdB"""
    defaultValue = 30

    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 100),
    )


_CadSysFlaplistPowerAdjustThreshold_Type.__name__ = "TenthdB"
_CadSysFlaplistPowerAdjustThreshold_Object = MibScalar
cadSysFlaplistPowerAdjustThreshold = _CadSysFlaplistPowerAdjustThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 35),
    _CadSysFlaplistPowerAdjustThreshold_Type()
)
cadSysFlaplistPowerAdjustThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysFlaplistPowerAdjustThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cadSysFlaplistPowerAdjustThreshold.setUnits("dB")


class _CadSysRemoteFSEnable_Type(TruthValue):
    """Custom type cadSysRemoteFSEnable based on TruthValue"""


_CadSysRemoteFSEnable_Object = MibScalar
cadSysRemoteFSEnable = _CadSysRemoteFSEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 36),
    _CadSysRemoteFSEnable_Type()
)
cadSysRemoteFSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysRemoteFSEnable.setStatus("current")


class _CadSysRemotePortEnable_Type(TruthValue):
    """Custom type cadSysRemotePortEnable based on TruthValue"""


_CadSysRemotePortEnable_Object = MibScalar
cadSysRemotePortEnable = _CadSysRemotePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 37),
    _CadSysRemotePortEnable_Type()
)
cadSysRemotePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysRemotePortEnable.setStatus("current")


class _CadSysTcpSmoothingValue1D8U_Type(Unsigned32):
    """Custom type cadSysTcpSmoothingValue1D8U based on Unsigned32"""
    defaultValue = 0


_CadSysTcpSmoothingValue1D8U_Object = MibScalar
cadSysTcpSmoothingValue1D8U = _CadSysTcpSmoothingValue1D8U_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 38),
    _CadSysTcpSmoothingValue1D8U_Type()
)
cadSysTcpSmoothingValue1D8U.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysTcpSmoothingValue1D8U.setStatus("current")


class _CadSysTcpSmoothingValue2D12U_Type(Unsigned32):
    """Custom type cadSysTcpSmoothingValue2D12U based on Unsigned32"""
    defaultValue = 0


_CadSysTcpSmoothingValue2D12U_Object = MibScalar
cadSysTcpSmoothingValue2D12U = _CadSysTcpSmoothingValue2D12U_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 39),
    _CadSysTcpSmoothingValue2D12U_Type()
)
cadSysTcpSmoothingValue2D12U.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysTcpSmoothingValue2D12U.setStatus("current")


class _CadSysModemLossThreshold_Type(Unsigned32):
    """Custom type cadSysModemLossThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_CadSysModemLossThreshold_Type.__name__ = "Unsigned32"
_CadSysModemLossThreshold_Object = MibScalar
cadSysModemLossThreshold = _CadSysModemLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 40),
    _CadSysModemLossThreshold_Type()
)
cadSysModemLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysModemLossThreshold.setStatus("deprecated")


class _CadSysPeakTrafRateFor11CMs_Type(BitRate):
    """Custom type cadSysPeakTrafRateFor11CMs based on BitRate"""
    defaultValue = 0


_CadSysPeakTrafRateFor11CMs_Object = MibScalar
cadSysPeakTrafRateFor11CMs = _CadSysPeakTrafRateFor11CMs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 41),
    _CadSysPeakTrafRateFor11CMs_Type()
)
cadSysPeakTrafRateFor11CMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysPeakTrafRateFor11CMs.setStatus("obsolete")


class _CadSysCpeHostAuthorization_Type(TruthValue):
    """Custom type cadSysCpeHostAuthorization based on TruthValue"""


_CadSysCpeHostAuthorization_Object = MibScalar
cadSysCpeHostAuthorization = _CadSysCpeHostAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 44),
    _CadSysCpeHostAuthorization_Type()
)
cadSysCpeHostAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysCpeHostAuthorization.setStatus("current")


class _CadSysMaxUcdBurstLength_Type(Integer32):
    """Custom type cadSysMaxUcdBurstLength based on Integer32"""
    defaultValue = 16128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 16128),
    )


_CadSysMaxUcdBurstLength_Type.__name__ = "Integer32"
_CadSysMaxUcdBurstLength_Object = MibScalar
cadSysMaxUcdBurstLength = _CadSysMaxUcdBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 46),
    _CadSysMaxUcdBurstLength_Type()
)
cadSysMaxUcdBurstLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMaxUcdBurstLength.setStatus("current")
if mibBuilder.loadTexts:
    cadSysMaxUcdBurstLength.setUnits("bytes")


class _CadSysLO1LeakDetect_Type(TruthValue):
    """Custom type cadSysLO1LeakDetect based on TruthValue"""


_CadSysLO1LeakDetect_Object = MibScalar
cadSysLO1LeakDetect = _CadSysLO1LeakDetect_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 47),
    _CadSysLO1LeakDetect_Type()
)
cadSysLO1LeakDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysLO1LeakDetect.setStatus("current")


class _CadMtcmConditionalOverride_Type(TruthValue):
    """Custom type cadMtcmConditionalOverride based on TruthValue"""


_CadMtcmConditionalOverride_Object = MibScalar
cadMtcmConditionalOverride = _CadMtcmConditionalOverride_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 48),
    _CadMtcmConditionalOverride_Type()
)
cadMtcmConditionalOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMtcmConditionalOverride.setStatus("current")


class _CadSysDelayedCpeLearning_Type(TruthValue):
    """Custom type cadSysDelayedCpeLearning based on TruthValue"""


_CadSysDelayedCpeLearning_Object = MibScalar
cadSysDelayedCpeLearning = _CadSysDelayedCpeLearning_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 49),
    _CadSysDelayedCpeLearning_Type()
)
cadSysDelayedCpeLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysDelayedCpeLearning.setStatus("current")


class _CadSysModPriDsInRccEnabled_Type(TruthValue):
    """Custom type cadSysModPriDsInRccEnabled based on TruthValue"""


_CadSysModPriDsInRccEnabled_Object = MibScalar
cadSysModPriDsInRccEnabled = _CadSysModPriDsInRccEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 52),
    _CadSysModPriDsInRccEnabled_Type()
)
cadSysModPriDsInRccEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysModPriDsInRccEnabled.setStatus("current")


class _CadSysSendTccRefIdPerFragment_Type(TruthValue):
    """Custom type cadSysSendTccRefIdPerFragment based on TruthValue"""


_CadSysSendTccRefIdPerFragment_Object = MibScalar
cadSysSendTccRefIdPerFragment = _CadSysSendTccRefIdPerFragment_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 53),
    _CadSysSendTccRefIdPerFragment_Type()
)
cadSysSendTccRefIdPerFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysSendTccRefIdPerFragment.setStatus("current")


class _CadSysPeakTrRateUpstream_Type(TruthValue):
    """Custom type cadSysPeakTrRateUpstream based on TruthValue"""


_CadSysPeakTrRateUpstream_Object = MibScalar
cadSysPeakTrRateUpstream = _CadSysPeakTrRateUpstream_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 54),
    _CadSysPeakTrRateUpstream_Type()
)
cadSysPeakTrRateUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysPeakTrRateUpstream.setStatus("current")


class _CadSysAllowAmbiguityOverride_Type(TruthValue):
    """Custom type cadSysAllowAmbiguityOverride based on TruthValue"""


_CadSysAllowAmbiguityOverride_Object = MibScalar
cadSysAllowAmbiguityOverride = _CadSysAllowAmbiguityOverride_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 55),
    _CadSysAllowAmbiguityOverride_Type()
)
cadSysAllowAmbiguityOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysAllowAmbiguityOverride.setStatus("current")


class _CadSysUnicastNpUsAcquisition_Type(TruthValue):
    """Custom type cadSysUnicastNpUsAcquisition based on TruthValue"""


_CadSysUnicastNpUsAcquisition_Object = MibScalar
cadSysUnicastNpUsAcquisition = _CadSysUnicastNpUsAcquisition_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 56),
    _CadSysUnicastNpUsAcquisition_Type()
)
cadSysUnicastNpUsAcquisition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysUnicastNpUsAcquisition.setStatus("current")


class _CadSysMacMoveBlockedOnRcptDhcpPkt_Type(TruthValue):
    """Custom type cadSysMacMoveBlockedOnRcptDhcpPkt based on TruthValue"""


_CadSysMacMoveBlockedOnRcptDhcpPkt_Object = MibScalar
cadSysMacMoveBlockedOnRcptDhcpPkt = _CadSysMacMoveBlockedOnRcptDhcpPkt_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 57),
    _CadSysMacMoveBlockedOnRcptDhcpPkt_Type()
)
cadSysMacMoveBlockedOnRcptDhcpPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMacMoveBlockedOnRcptDhcpPkt.setStatus("current")


class _CadSysTftpProxy_Type(Integer32):
    """Custom type cadSysTftpProxy based on Integer32"""
    defaultValue = 1

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
        *(("disable", 0),
          ("enable", 1),
          ("ipv4only", 2),
          ("ipv6only", 3))
    )


_CadSysTftpProxy_Type.__name__ = "Integer32"
_CadSysTftpProxy_Object = MibScalar
cadSysTftpProxy = _CadSysTftpProxy_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 58),
    _CadSysTftpProxy_Type()
)
cadSysTftpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysTftpProxy.setStatus("current")


class _CadSysFanSpeedLevel_Type(Integer32):
    """Custom type cadSysFanSpeedLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadSysFanSpeedLevel_Type.__name__ = "Integer32"
_CadSysFanSpeedLevel_Object = MibScalar
cadSysFanSpeedLevel = _CadSysFanSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 59),
    _CadSysFanSpeedLevel_Type()
)
cadSysFanSpeedLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysFanSpeedLevel.setStatus("current")


class _CadSys1x1onCmAcPwrLossEnabled_Type(TruthValue):
    """Custom type cadSys1x1onCmAcPwrLossEnabled based on TruthValue"""


_CadSys1x1onCmAcPwrLossEnabled_Object = MibScalar
cadSys1x1onCmAcPwrLossEnabled = _CadSys1x1onCmAcPwrLossEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 60),
    _CadSys1x1onCmAcPwrLossEnabled_Type()
)
cadSys1x1onCmAcPwrLossEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSys1x1onCmAcPwrLossEnabled.setStatus("current")


class _CadSysFlapListInsertionThreshold_Type(Integer32):
    """Custom type cadSysFlapListInsertionThreshold based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CadSysFlapListInsertionThreshold_Type.__name__ = "Integer32"
_CadSysFlapListInsertionThreshold_Object = MibScalar
cadSysFlapListInsertionThreshold = _CadSysFlapListInsertionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 61),
    _CadSysFlapListInsertionThreshold_Type()
)
cadSysFlapListInsertionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysFlapListInsertionThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cadSysFlapListInsertionThreshold.setUnits("seconds")


class _CadSysAES128Enable_Type(TruthValue):
    """Custom type cadSysAES128Enable based on TruthValue"""


_CadSysAES128Enable_Object = MibScalar
cadSysAES128Enable = _CadSysAES128Enable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 1, 62),
    _CadSysAES128Enable_Type()
)
cadSysAES128Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysAES128Enable.setStatus("current")
_CadSysSystem_ObjectIdentity = ObjectIdentity
cadSysSystem = _CadSysSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 2)
)


class _CadSysContact_Type(DisplayString):
    """Custom type cadSysContact based on DisplayString"""
    defaultValue = OctetString("support@arris.com")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CadSysContact_Type.__name__ = "DisplayString"
_CadSysContact_Object = MibScalar
cadSysContact = _CadSysContact_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 2, 1),
    _CadSysContact_Type()
)
cadSysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysContact.setStatus("current")


class _CadSysName_Type(DisplayString):
    """Custom type cadSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CadSysName_Type.__name__ = "DisplayString"
_CadSysName_Object = MibScalar
cadSysName = _CadSysName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 2, 2),
    _CadSysName_Type()
)
cadSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysName.setStatus("current")


class _CadSysLocation_Type(DisplayString):
    """Custom type cadSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CadSysLocation_Type.__name__ = "DisplayString"
_CadSysLocation_Object = MibScalar
cadSysLocation = _CadSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 2, 3),
    _CadSysLocation_Type()
)
cadSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysLocation.setStatus("current")
_CadSysControl_ObjectIdentity = ObjectIdentity
cadSysControl = _CadSysControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 3)
)


class _CadSysWriteMem_Type(TruthValue):
    """Custom type cadSysWriteMem based on TruthValue"""


_CadSysWriteMem_Object = MibScalar
cadSysWriteMem = _CadSysWriteMem_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 3, 1),
    _CadSysWriteMem_Type()
)
cadSysWriteMem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysWriteMem.setStatus("current")


class _CadSysEraseMem_Type(TruthValue):
    """Custom type cadSysEraseMem based on TruthValue"""


_CadSysEraseMem_Object = MibScalar
cadSysEraseMem = _CadSysEraseMem_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 3, 2),
    _CadSysEraseMem_Type()
)
cadSysEraseMem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysEraseMem.setStatus("current")
_CadSysSnmp_ObjectIdentity = ObjectIdentity
cadSysSnmp = _CadSysSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4)
)


class _CadSysEnableAuthenTraps_Type(Integer32):
    """Custom type cadSysEnableAuthenTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enable", 1))
    )


_CadSysEnableAuthenTraps_Type.__name__ = "Integer32"
_CadSysEnableAuthenTraps_Object = MibScalar
cadSysEnableAuthenTraps = _CadSysEnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 1),
    _CadSysEnableAuthenTraps_Type()
)
cadSysEnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysEnableAuthenTraps.setStatus("current")


class _CadSysSnmpReadAheadMax_Type(Unsigned32):
    """Custom type cadSysSnmpReadAheadMax based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CadSysSnmpReadAheadMax_Type.__name__ = "Unsigned32"
_CadSysSnmpReadAheadMax_Object = MibScalar
cadSysSnmpReadAheadMax = _CadSysSnmpReadAheadMax_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 2),
    _CadSysSnmpReadAheadMax_Type()
)
cadSysSnmpReadAheadMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysSnmpReadAheadMax.setStatus("current")


class _CadSysSnmpRefreshTime_Type(Unsigned32):
    """Custom type cadSysSnmpRefreshTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_CadSysSnmpRefreshTime_Type.__name__ = "Unsigned32"
_CadSysSnmpRefreshTime_Object = MibScalar
cadSysSnmpRefreshTime = _CadSysSnmpRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 3),
    _CadSysSnmpRefreshTime_Type()
)
cadSysSnmpRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysSnmpRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    cadSysSnmpRefreshTime.setUnits("seconds")
_CadSnmpRemoteEngineTable_Object = MibTable
cadSnmpRemoteEngineTable = _CadSnmpRemoteEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cadSnmpRemoteEngineTable.setStatus("deprecated")
_CadSnmpRemoteEngineEntry_Object = MibTableRow
cadSnmpRemoteEngineEntry = _CadSnmpRemoteEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 4, 1)
)
cadSnmpRemoteEngineEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSnmpRemoteEngineIpAddress"),
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSnmpRemoteEnginePortNumber"),
)
if mibBuilder.loadTexts:
    cadSnmpRemoteEngineEntry.setStatus("current")
_CadSnmpRemoteEngineIpAddress_Type = IpAddress
_CadSnmpRemoteEngineIpAddress_Object = MibTableColumn
cadSnmpRemoteEngineIpAddress = _CadSnmpRemoteEngineIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 4, 1, 1),
    _CadSnmpRemoteEngineIpAddress_Type()
)
cadSnmpRemoteEngineIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSnmpRemoteEngineIpAddress.setStatus("current")


class _CadSnmpRemoteEnginePortNumber_Type(Integer32):
    """Custom type cadSnmpRemoteEnginePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSnmpRemoteEnginePortNumber_Type.__name__ = "Integer32"
_CadSnmpRemoteEnginePortNumber_Object = MibTableColumn
cadSnmpRemoteEnginePortNumber = _CadSnmpRemoteEnginePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 4, 1, 2),
    _CadSnmpRemoteEnginePortNumber_Type()
)
cadSnmpRemoteEnginePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSnmpRemoteEnginePortNumber.setStatus("current")
_CadSnmpRemoteEngineID_Type = SnmpEngineID
_CadSnmpRemoteEngineID_Object = MibTableColumn
cadSnmpRemoteEngineID = _CadSnmpRemoteEngineID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 4, 1, 3),
    _CadSnmpRemoteEngineID_Type()
)
cadSnmpRemoteEngineID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSnmpRemoteEngineID.setStatus("deprecated")


class _CadSnmpRemoteUserName_Type(SnmpAdminString):
    """Custom type cadSnmpRemoteUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CadSnmpRemoteUserName_Type.__name__ = "SnmpAdminString"
_CadSnmpRemoteUserName_Object = MibTableColumn
cadSnmpRemoteUserName = _CadSnmpRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 4, 1, 4),
    _CadSnmpRemoteUserName_Type()
)
cadSnmpRemoteUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSnmpRemoteUserName.setStatus("current")


class _CadSnmpRemoteEngineType_Type(Integer32):
    """Custom type cadSnmpRemoteEngineType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 1))
    )


_CadSnmpRemoteEngineType_Type.__name__ = "Integer32"
_CadSnmpRemoteEngineType_Object = MibTableColumn
cadSnmpRemoteEngineType = _CadSnmpRemoteEngineType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 4, 1, 5),
    _CadSnmpRemoteEngineType_Type()
)
cadSnmpRemoteEngineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSnmpRemoteEngineType.setStatus("current")
_CadSnmpRemoteEngineStatus_Type = RowStatus
_CadSnmpRemoteEngineStatus_Object = MibTableColumn
cadSnmpRemoteEngineStatus = _CadSnmpRemoteEngineStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 4, 4, 1, 6),
    _CadSnmpRemoteEngineStatus_Type()
)
cadSnmpRemoteEngineStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSnmpRemoteEngineStatus.setStatus("current")
_CadSysBootParams_ObjectIdentity = ObjectIdentity
cadSysBootParams = _CadSysBootParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5)
)
_CadSysBootMacAddress_Type = MacAddress
_CadSysBootMacAddress_Object = MibScalar
cadSysBootMacAddress = _CadSysBootMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 1),
    _CadSysBootMacAddress_Type()
)
cadSysBootMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysBootMacAddress.setStatus("current")
_CadSysBootFpIpAddress_Type = IpAddress
_CadSysBootFpIpAddress_Object = MibScalar
cadSysBootFpIpAddress = _CadSysBootFpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 2),
    _CadSysBootFpIpAddress_Type()
)
cadSysBootFpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysBootFpIpAddress.setStatus("current")
_CadSysBootFpSubnetMask_Type = IpAddress
_CadSysBootFpSubnetMask_Object = MibScalar
cadSysBootFpSubnetMask = _CadSysBootFpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 3),
    _CadSysBootFpSubnetMask_Type()
)
cadSysBootFpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysBootFpSubnetMask.setStatus("current")
_CadSysBootDefaultGateway_Type = IpAddress
_CadSysBootDefaultGateway_Object = MibScalar
cadSysBootDefaultGateway = _CadSysBootDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 6),
    _CadSysBootDefaultGateway_Type()
)
cadSysBootDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysBootDefaultGateway.setStatus("current")
_CadSysBootTimeOffset_Type = Integer32
_CadSysBootTimeOffset_Object = MibScalar
cadSysBootTimeOffset = _CadSysBootTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 7),
    _CadSysBootTimeOffset_Type()
)
cadSysBootTimeOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysBootTimeOffset.setStatus("current")
_CadSysBootTimeServer_Type = IpAddress
_CadSysBootTimeServer_Object = MibScalar
cadSysBootTimeServer = _CadSysBootTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 8),
    _CadSysBootTimeServer_Type()
)
cadSysBootTimeServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysBootTimeServer.setStatus("current")


class _CadSysBootTimeServerConnType_Type(Integer32):
    """Custom type cadSysBootTimeServerConnType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_CadSysBootTimeServerConnType_Type.__name__ = "Integer32"
_CadSysBootTimeServerConnType_Object = MibScalar
cadSysBootTimeServerConnType = _CadSysBootTimeServerConnType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 9),
    _CadSysBootTimeServerConnType_Type()
)
cadSysBootTimeServerConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysBootTimeServerConnType.setStatus("current")


class _CadSysBootStartupApplication_Type(Integer32):
    """Custom type cadSysBootStartupApplication based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bootapplication", 4),
          ("bootprobe", 1))
    )


_CadSysBootStartupApplication_Type.__name__ = "Integer32"
_CadSysBootStartupApplication_Object = MibScalar
cadSysBootStartupApplication = _CadSysBootStartupApplication_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 10),
    _CadSysBootStartupApplication_Type()
)
cadSysBootStartupApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysBootStartupApplication.setStatus("current")


class _CadSysBootStartupDelay_Type(Integer32):
    """Custom type cadSysBootStartupDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CadSysBootStartupDelay_Type.__name__ = "Integer32"
_CadSysBootStartupDelay_Object = MibScalar
cadSysBootStartupDelay = _CadSysBootStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 11),
    _CadSysBootStartupDelay_Type()
)
cadSysBootStartupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysBootStartupDelay.setStatus("current")


class _CadSysBootSelection_Type(Integer32):
    """Custom type cadSysBootSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CadSysBootSelection_Type.__name__ = "Integer32"
_CadSysBootSelection_Object = MibScalar
cadSysBootSelection = _CadSysBootSelection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 12),
    _CadSysBootSelection_Type()
)
cadSysBootSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysBootSelection.setStatus("current")


class _CadSysBootBaud_Type(Integer32):
    """Custom type cadSysBootBaud based on Integer32"""
    defaultValue = 9600


_CadSysBootBaud_Object = MibScalar
cadSysBootBaud = _CadSysBootBaud_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 13),
    _CadSysBootBaud_Type()
)
cadSysBootBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysBootBaud.setStatus("deprecated")
_CadSysBootFpBIpAddress_Type = IpAddress
_CadSysBootFpBIpAddress_Object = MibScalar
cadSysBootFpBIpAddress = _CadSysBootFpBIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 15),
    _CadSysBootFpBIpAddress_Type()
)
cadSysBootFpBIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysBootFpBIpAddress.setStatus("current")


class _CadSysBootParity_Type(OctetString):
    """Custom type cadSysBootParity based on OctetString"""
    defaultValue = OctetString("N")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CadSysBootParity_Type.__name__ = "OctetString"
_CadSysBootParity_Object = MibScalar
cadSysBootParity = _CadSysBootParity_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 5, 16),
    _CadSysBootParity_Type()
)
cadSysBootParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysBootParity.setStatus("current")
_CadSysReload_ObjectIdentity = ObjectIdentity
cadSysReload = _CadSysReload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 6)
)


class _CadSysReloadOperation_Type(Integer32):
    """Custom type cadSysReloadOperation based on Integer32"""
    defaultValue = 99

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
              8,
              9,
              99)
        )
    )
    namedValues = NamedValues(
        *(("none", 99),
          ("reloadActive", 3),
          ("reloadCommit", 2),
          ("reloadErasemem", 6),
          ("reloadHitless", 4),
          ("reloadImage", 1),
          ("reloadPatchApply", 9),
          ("reloadPatchInstall", 7),
          ("reloadPatchRemove", 8),
          ("reloadWritemem", 5))
    )


_CadSysReloadOperation_Type.__name__ = "Integer32"
_CadSysReloadOperation_Object = MibScalar
cadSysReloadOperation = _CadSysReloadOperation_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 6, 1),
    _CadSysReloadOperation_Type()
)
cadSysReloadOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysReloadOperation.setStatus("current")
_CadSysReloadImageName_Type = DisplayString
_CadSysReloadImageName_Object = MibScalar
cadSysReloadImageName = _CadSysReloadImageName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 6, 2),
    _CadSysReloadImageName_Type()
)
cadSysReloadImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysReloadImageName.setStatus("current")


class _CadSysReloadStatus_Type(Bits):
    """Custom type cadSysReloadStatus based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("abort", 18),
          ("bundling", 15),
          ("complete", 17),
          ("copyImage", 29),
          ("eraseMem", 21),
          ("firmwareUpdate", 11),
          ("idle", 0),
          ("inProgress", 1),
          ("localCheckImage", 2),
          ("localCommit", 3),
          ("localInstallImage", 24),
          ("localPreloadRsm", 26),
          ("localReboot", 8),
          ("patchApplyCheck", 31),
          ("patchInstall", 7),
          ("patchRemove", 9),
          ("preloadCams", 23),
          ("remoteCheckImage", 6),
          ("remoteCommit", 4),
          ("remoteCommitRsm", 28),
          ("remoteCopyImage", 5),
          ("remoteEraseMem", 22),
          ("remoteFirmwareUpdate", 10),
          ("remoteFirmwareUpdateRsm", 30),
          ("remoteInstallImage", 25),
          ("remotePatchInstall", 13),
          ("remotePatchRemove", 19),
          ("remotePreloadRsm", 27),
          ("remoteWriteMem", 20),
          ("unbundling", 16),
          ("waitCamsReset", 34),
          ("waitSoftswitch", 32),
          ("waitSpareCamsReset", 33),
          ("waitStandby", 12),
          ("writeMem", 14))
    )

_CadSysReloadStatus_Type.__name__ = "Bits"
_CadSysReloadStatus_Object = MibScalar
cadSysReloadStatus = _CadSysReloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 6, 3),
    _CadSysReloadStatus_Type()
)
cadSysReloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysReloadStatus.setStatus("current")
_CadSysReloadStatusDescription_Type = DisplayString
_CadSysReloadStatusDescription_Object = MibScalar
cadSysReloadStatusDescription = _CadSysReloadStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 6, 4),
    _CadSysReloadStatusDescription_Type()
)
cadSysReloadStatusDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysReloadStatusDescription.setStatus("current")
_CadSysReloadPatchName_Type = DisplayString
_CadSysReloadPatchName_Object = MibScalar
cadSysReloadPatchName = _CadSysReloadPatchName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 6, 5),
    _CadSysReloadPatchName_Type()
)
cadSysReloadPatchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysReloadPatchName.setStatus("current")
_CadSysImage_ObjectIdentity = ObjectIdentity
cadSysImage = _CadSysImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 7)
)
_CadSysImageFile_Type = DisplayString
_CadSysImageFile_Object = MibScalar
cadSysImageFile = _CadSysImageFile_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 7, 1),
    _CadSysImageFile_Type()
)
cadSysImageFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysImageFile.setStatus("current")
_CadSysImageId_Type = Integer32
_CadSysImageId_Object = MibScalar
cadSysImageId = _CadSysImageId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 7, 2),
    _CadSysImageId_Type()
)
cadSysImageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysImageId.setStatus("current")
_CadSysImageName_Type = DisplayString
_CadSysImageName_Object = MibScalar
cadSysImageName = _CadSysImageName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 7, 3),
    _CadSysImageName_Type()
)
cadSysImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysImageName.setStatus("current")
_CadSysImageComponentCount_Type = Integer32
_CadSysImageComponentCount_Object = MibScalar
cadSysImageComponentCount = _CadSysImageComponentCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 7, 4),
    _CadSysImageComponentCount_Type()
)
cadSysImageComponentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysImageComponentCount.setStatus("current")
_CadSysDictionary_ObjectIdentity = ObjectIdentity
cadSysDictionary = _CadSysDictionary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 8)
)
_CadSysDictionaryTable_Object = MibTable
cadSysDictionaryTable = _CadSysDictionaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cadSysDictionaryTable.setStatus("current")
_CadSysDictionaryEntry_Object = MibTableRow
cadSysDictionaryEntry = _CadSysDictionaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 8, 1, 1)
)
cadSysDictionaryEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysDictionaryTableId"),
)
if mibBuilder.loadTexts:
    cadSysDictionaryEntry.setStatus("current")
_CadSysDictionaryTableId_Type = Unsigned32
_CadSysDictionaryTableId_Object = MibTableColumn
cadSysDictionaryTableId = _CadSysDictionaryTableId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 8, 1, 1, 1),
    _CadSysDictionaryTableId_Type()
)
cadSysDictionaryTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysDictionaryTableId.setStatus("current")
_CadSysDictionaryName_Type = DisplayString
_CadSysDictionaryName_Object = MibTableColumn
cadSysDictionaryName = _CadSysDictionaryName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 8, 1, 1, 2),
    _CadSysDictionaryName_Type()
)
cadSysDictionaryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysDictionaryName.setStatus("current")
_CadSysDictionaryDynamic_Type = TruthValue
_CadSysDictionaryDynamic_Object = MibTableColumn
cadSysDictionaryDynamic = _CadSysDictionaryDynamic_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 8, 1, 1, 3),
    _CadSysDictionaryDynamic_Type()
)
cadSysDictionaryDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysDictionaryDynamic.setStatus("current")
_CadSysDictionaryNumberEntries_Type = Integer32
_CadSysDictionaryNumberEntries_Object = MibTableColumn
cadSysDictionaryNumberEntries = _CadSysDictionaryNumberEntries_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 8, 1, 1, 4),
    _CadSysDictionaryNumberEntries_Type()
)
cadSysDictionaryNumberEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysDictionaryNumberEntries.setStatus("current")
_CadSysDictionaryCurrentVer_Type = Unsigned32
_CadSysDictionaryCurrentVer_Object = MibTableColumn
cadSysDictionaryCurrentVer = _CadSysDictionaryCurrentVer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 8, 1, 1, 5),
    _CadSysDictionaryCurrentVer_Type()
)
cadSysDictionaryCurrentVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysDictionaryCurrentVer.setStatus("current")
_CadSysDictionaryPersistentVer_Type = Unsigned32
_CadSysDictionaryPersistentVer_Object = MibTableColumn
cadSysDictionaryPersistentVer = _CadSysDictionaryPersistentVer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 8, 1, 1, 6),
    _CadSysDictionaryPersistentVer_Type()
)
cadSysDictionaryPersistentVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysDictionaryPersistentVer.setStatus("current")
_CadSysDictionaryModuleVer_Type = Unsigned32
_CadSysDictionaryModuleVer_Object = MibTableColumn
cadSysDictionaryModuleVer = _CadSysDictionaryModuleVer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 8, 1, 1, 7),
    _CadSysDictionaryModuleVer_Type()
)
cadSysDictionaryModuleVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysDictionaryModuleVer.setStatus("current")
_CadSysConfiguration_ObjectIdentity = ObjectIdentity
cadSysConfiguration = _CadSysConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 9)
)
_CadSysConfigSaveTime_Type = DateAndTime
_CadSysConfigSaveTime_Object = MibScalar
cadSysConfigSaveTime = _CadSysConfigSaveTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 9, 1),
    _CadSysConfigSaveTime_Type()
)
cadSysConfigSaveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysConfigSaveTime.setStatus("current")
_CadCosToQosMapping_ObjectIdentity = ObjectIdentity
cadCosToQosMapping = _CadCosToQosMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10)
)
_CadCosToQosMappingTable_Object = MibTable
cadCosToQosMappingTable = _CadCosToQosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9)
)
if mibBuilder.loadTexts:
    cadCosToQosMappingTable.setStatus("current")
_CadCosToQosMappingEntry_Object = MibTableRow
cadCosToQosMappingEntry = _CadCosToQosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1)
)
cadCosToQosMappingEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadCosToQosMappingIndex"),
)
if mibBuilder.loadTexts:
    cadCosToQosMappingEntry.setStatus("current")


class _CadCosToQosMappingIndex_Type(Integer32):
    """Custom type cadCosToQosMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CadCosToQosMappingIndex_Type.__name__ = "Integer32"
_CadCosToQosMappingIndex_Object = MibTableColumn
cadCosToQosMappingIndex = _CadCosToQosMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 1),
    _CadCosToQosMappingIndex_Type()
)
cadCosToQosMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCosToQosMappingIndex.setStatus("current")


class _CadCosUpMaxTrafficBurst_Type(Unsigned32):
    """Custom type cadCosUpMaxTrafficBurst based on Unsigned32"""
    defaultValue = 3044


_CadCosUpMaxTrafficBurst_Object = MibTableColumn
cadCosUpMaxTrafficBurst = _CadCosUpMaxTrafficBurst_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 2),
    _CadCosUpMaxTrafficBurst_Type()
)
cadCosUpMaxTrafficBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosUpMaxTrafficBurst.setStatus("current")


class _CadCosDnMaxTrafficBurst_Type(Unsigned32):
    """Custom type cadCosDnMaxTrafficBurst based on Unsigned32"""
    defaultValue = 96000


_CadCosDnMaxTrafficBurst_Object = MibTableColumn
cadCosDnMaxTrafficBurst = _CadCosDnMaxTrafficBurst_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 3),
    _CadCosDnMaxTrafficBurst_Type()
)
cadCosDnMaxTrafficBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosDnMaxTrafficBurst.setStatus("current")


class _CadCosDnMinReservedRate_Type(BitRate):
    """Custom type cadCosDnMinReservedRate based on BitRate"""
    defaultValue = 0


_CadCosDnMinReservedRate_Object = MibTableColumn
cadCosDnMinReservedRate = _CadCosDnMinReservedRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 4),
    _CadCosDnMinReservedRate_Type()
)
cadCosDnMinReservedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosDnMinReservedRate.setStatus("current")


class _CadCosUpMinReservedPkt_Type(Integer32):
    """Custom type cadCosUpMinReservedPkt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadCosUpMinReservedPkt_Type.__name__ = "Integer32"
_CadCosUpMinReservedPkt_Object = MibTableColumn
cadCosUpMinReservedPkt = _CadCosUpMinReservedPkt_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 5),
    _CadCosUpMinReservedPkt_Type()
)
cadCosUpMinReservedPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosUpMinReservedPkt.setStatus("current")


class _CadCosDnMinReservedPkt_Type(Integer32):
    """Custom type cadCosDnMinReservedPkt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadCosDnMinReservedPkt_Type.__name__ = "Integer32"
_CadCosDnMinReservedPkt_Object = MibTableColumn
cadCosDnMinReservedPkt = _CadCosDnMinReservedPkt_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 6),
    _CadCosDnMinReservedPkt_Type()
)
cadCosDnMinReservedPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosDnMinReservedPkt.setStatus("current")


class _CadCosUpTosAndMask_Type(OctetString):
    """Custom type cadCosUpTosAndMask based on OctetString"""
    defaultHexValue = "ff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CadCosUpTosAndMask_Type.__name__ = "OctetString"
_CadCosUpTosAndMask_Object = MibTableColumn
cadCosUpTosAndMask = _CadCosUpTosAndMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 7),
    _CadCosUpTosAndMask_Type()
)
cadCosUpTosAndMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosUpTosAndMask.setStatus("current")


class _CadCosUpTosOrMask_Type(OctetString):
    """Custom type cadCosUpTosOrMask based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CadCosUpTosOrMask_Type.__name__ = "OctetString"
_CadCosUpTosOrMask_Object = MibTableColumn
cadCosUpTosOrMask = _CadCosUpTosOrMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 8),
    _CadCosUpTosOrMask_Type()
)
cadCosUpTosOrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosUpTosOrMask.setStatus("current")


class _CadCosDnMaxLatency_Type(Unsigned32):
    """Custom type cadCosDnMaxLatency based on Unsigned32"""
    defaultValue = 0


_CadCosDnMaxLatency_Object = MibTableColumn
cadCosDnMaxLatency = _CadCosDnMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 9),
    _CadCosDnMaxLatency_Type()
)
cadCosDnMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosDnMaxLatency.setStatus("current")


class _CadCosDnPriority_Type(Integer32):
    """Custom type cadCosDnPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_CadCosDnPriority_Type.__name__ = "Integer32"
_CadCosDnPriority_Object = MibTableColumn
cadCosDnPriority = _CadCosDnPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 10),
    _CadCosDnPriority_Type()
)
cadCosDnPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosDnPriority.setStatus("current")


class _CadCosDnPeakTrafficRate_Type(BitRate):
    """Custom type cadCosDnPeakTrafficRate based on BitRate"""
    defaultValue = 0


_CadCosDnPeakTrafficRate_Object = MibTableColumn
cadCosDnPeakTrafficRate = _CadCosDnPeakTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 11),
    _CadCosDnPeakTrafficRate_Type()
)
cadCosDnPeakTrafficRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosDnPeakTrafficRate.setStatus("current")


class _CadCosUpPeakTrafficRate_Type(BitRate):
    """Custom type cadCosUpPeakTrafficRate based on BitRate"""
    defaultValue = 0


_CadCosUpPeakTrafficRate_Object = MibTableColumn
cadCosUpPeakTrafficRate = _CadCosUpPeakTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 10, 9, 1, 12),
    _CadCosUpPeakTrafficRate_Type()
)
cadCosUpPeakTrafficRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCosUpPeakTrafficRate.setStatus("current")
_CadSysKeyChain_ObjectIdentity = ObjectIdentity
cadSysKeyChain = _CadSysKeyChain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11)
)
_CadSysKeyChainKeyTable_Object = MibTable
cadSysKeyChainKeyTable = _CadSysKeyChainKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cadSysKeyChainKeyTable.setStatus("current")
_CadSysKeyChainKeyEntry_Object = MibTableRow
cadSysKeyChainKeyEntry = _CadSysKeyChainKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1)
)
cadSysKeyChainKeyEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysKeyChainName"),
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysKeyChainKeySequenceId"),
)
if mibBuilder.loadTexts:
    cadSysKeyChainKeyEntry.setStatus("current")


class _CadSysKeyChainName_Type(OctetString):
    """Custom type cadSysKeyChainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CadSysKeyChainName_Type.__name__ = "OctetString"
_CadSysKeyChainName_Object = MibTableColumn
cadSysKeyChainName = _CadSysKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1, 1),
    _CadSysKeyChainName_Type()
)
cadSysKeyChainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysKeyChainName.setStatus("current")


class _CadSysKeyChainKeySequenceId_Type(Unsigned32):
    """Custom type cadSysKeyChainKeySequenceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadSysKeyChainKeySequenceId_Type.__name__ = "Unsigned32"
_CadSysKeyChainKeySequenceId_Object = MibTableColumn
cadSysKeyChainKeySequenceId = _CadSysKeyChainKeySequenceId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1, 2),
    _CadSysKeyChainKeySequenceId_Type()
)
cadSysKeyChainKeySequenceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysKeyChainKeySequenceId.setStatus("current")


class _CadSysKeyChainKey_Type(OctetString):
    """Custom type cadSysKeyChainKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadSysKeyChainKey_Type.__name__ = "OctetString"
_CadSysKeyChainKey_Object = MibTableColumn
cadSysKeyChainKey = _CadSysKeyChainKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1, 3),
    _CadSysKeyChainKey_Type()
)
cadSysKeyChainKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysKeyChainKey.setStatus("current")
_CadSysKeyChainKeyAcceptStartTime_Type = DateAndTime
_CadSysKeyChainKeyAcceptStartTime_Object = MibTableColumn
cadSysKeyChainKeyAcceptStartTime = _CadSysKeyChainKeyAcceptStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1, 4),
    _CadSysKeyChainKeyAcceptStartTime_Type()
)
cadSysKeyChainKeyAcceptStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysKeyChainKeyAcceptStartTime.setStatus("current")
_CadSysKeyChainKeyAcceptStopTime_Type = DateAndTime
_CadSysKeyChainKeyAcceptStopTime_Object = MibTableColumn
cadSysKeyChainKeyAcceptStopTime = _CadSysKeyChainKeyAcceptStopTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1, 5),
    _CadSysKeyChainKeyAcceptStopTime_Type()
)
cadSysKeyChainKeyAcceptStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysKeyChainKeyAcceptStopTime.setStatus("current")


class _CadSysKeyChainKeyAcceptInfiniteLifetime_Type(TruthValue):
    """Custom type cadSysKeyChainKeyAcceptInfiniteLifetime based on TruthValue"""


_CadSysKeyChainKeyAcceptInfiniteLifetime_Object = MibTableColumn
cadSysKeyChainKeyAcceptInfiniteLifetime = _CadSysKeyChainKeyAcceptInfiniteLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1, 6),
    _CadSysKeyChainKeyAcceptInfiniteLifetime_Type()
)
cadSysKeyChainKeyAcceptInfiniteLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysKeyChainKeyAcceptInfiniteLifetime.setStatus("current")
_CadSysKeyChainKeySendStartTime_Type = DateAndTime
_CadSysKeyChainKeySendStartTime_Object = MibTableColumn
cadSysKeyChainKeySendStartTime = _CadSysKeyChainKeySendStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1, 7),
    _CadSysKeyChainKeySendStartTime_Type()
)
cadSysKeyChainKeySendStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysKeyChainKeySendStartTime.setStatus("current")
_CadSysKeyChainKeySendStopTime_Type = DateAndTime
_CadSysKeyChainKeySendStopTime_Object = MibTableColumn
cadSysKeyChainKeySendStopTime = _CadSysKeyChainKeySendStopTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1, 8),
    _CadSysKeyChainKeySendStopTime_Type()
)
cadSysKeyChainKeySendStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysKeyChainKeySendStopTime.setStatus("current")


class _CadSysKeyChainKeySendInfiniteLifetime_Type(TruthValue):
    """Custom type cadSysKeyChainKeySendInfiniteLifetime based on TruthValue"""


_CadSysKeyChainKeySendInfiniteLifetime_Object = MibTableColumn
cadSysKeyChainKeySendInfiniteLifetime = _CadSysKeyChainKeySendInfiniteLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1, 9),
    _CadSysKeyChainKeySendInfiniteLifetime_Type()
)
cadSysKeyChainKeySendInfiniteLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysKeyChainKeySendInfiniteLifetime.setStatus("current")
_CadSysKeyChainKeyRowStatus_Type = RowStatus
_CadSysKeyChainKeyRowStatus_Object = MibTableColumn
cadSysKeyChainKeyRowStatus = _CadSysKeyChainKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 11, 1, 1, 10),
    _CadSysKeyChainKeyRowStatus_Type()
)
cadSysKeyChainKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysKeyChainKeyRowStatus.setStatus("current")
_CadSystemMibConformance_ObjectIdentity = ObjectIdentity
cadSystemMibConformance = _CadSystemMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12)
)
_CadSystemCompliances_ObjectIdentity = ObjectIdentity
cadSystemCompliances = _CadSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 1)
)
_CadSystemGroups_ObjectIdentity = ObjectIdentity
cadSystemGroups = _CadSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2)
)
_CadSysProcPolicingConfig_ObjectIdentity = ObjectIdentity
cadSysProcPolicingConfig = _CadSysProcPolicingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13)
)


class _CadSysProcRouterControlGlobalPacketRate_Type(Unsigned32):
    """Custom type cadSysProcRouterControlGlobalPacketRate based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcRouterControlGlobalPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcRouterControlGlobalPacketRate_Object = MibScalar
cadSysProcRouterControlGlobalPacketRate = _CadSysProcRouterControlGlobalPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 1),
    _CadSysProcRouterControlGlobalPacketRate_Type()
)
cadSysProcRouterControlGlobalPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcRouterControlGlobalPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcRouterControlGlobalPacketRate.setUnits("packets/second")


class _CadSysProcArpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcArpPacketRate based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcArpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcArpPacketRate_Object = MibScalar
cadSysProcArpPacketRate = _CadSysProcArpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 2),
    _CadSysProcArpPacketRate_Type()
)
cadSysProcArpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcArpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcArpPacketRate.setUnits("packets/second")


class _CadSysProcDhcpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcDhcpPacketRate based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcDhcpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcDhcpPacketRate_Object = MibScalar
cadSysProcDhcpPacketRate = _CadSysProcDhcpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 3),
    _CadSysProcDhcpPacketRate_Type()
)
cadSysProcDhcpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcDhcpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcDhcpPacketRate.setUnits("packets/second")


class _CadSysProcIcmpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcIcmpPacketRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcIcmpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcIcmpPacketRate_Object = MibScalar
cadSysProcIcmpPacketRate = _CadSysProcIcmpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 4),
    _CadSysProcIcmpPacketRate_Type()
)
cadSysProcIcmpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcIcmpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIcmpPacketRate.setUnits("packets/second")


class _CadSysProcOspfPacketRate_Type(Unsigned32):
    """Custom type cadSysProcOspfPacketRate based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcOspfPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcOspfPacketRate_Object = MibScalar
cadSysProcOspfPacketRate = _CadSysProcOspfPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 5),
    _CadSysProcOspfPacketRate_Type()
)
cadSysProcOspfPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcOspfPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcOspfPacketRate.setUnits("packets/second")


class _CadSysProcRipPacketRate_Type(Unsigned32):
    """Custom type cadSysProcRipPacketRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcRipPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcRipPacketRate_Object = MibScalar
cadSysProcRipPacketRate = _CadSysProcRipPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 6),
    _CadSysProcRipPacketRate_Type()
)
cadSysProcRipPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcRipPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcRipPacketRate.setUnits("packets/second")


class _CadSysProcIgmpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcIgmpPacketRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcIgmpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcIgmpPacketRate_Object = MibScalar
cadSysProcIgmpPacketRate = _CadSysProcIgmpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 7),
    _CadSysProcIgmpPacketRate_Type()
)
cadSysProcIgmpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcIgmpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIgmpPacketRate.setUnits("packets/second")


class _CadSysProcRouterControlOtherPacketRate_Type(Unsigned32):
    """Custom type cadSysProcRouterControlOtherPacketRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcRouterControlOtherPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcRouterControlOtherPacketRate_Object = MibScalar
cadSysProcRouterControlOtherPacketRate = _CadSysProcRouterControlOtherPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 8),
    _CadSysProcRouterControlOtherPacketRate_Type()
)
cadSysProcRouterControlOtherPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcRouterControlOtherPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcRouterControlOtherPacketRate.setUnits("packets/second")


class _CadSysProcSnmpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcSnmpPacketRate based on Unsigned32"""
    defaultValue = 650

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcSnmpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcSnmpPacketRate_Object = MibScalar
cadSysProcSnmpPacketRate = _CadSysProcSnmpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 10),
    _CadSysProcSnmpPacketRate_Type()
)
cadSysProcSnmpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcSnmpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcSnmpPacketRate.setUnits("packets/second")


class _CadSysProcTftpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcTftpPacketRate based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcTftpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcTftpPacketRate_Object = MibScalar
cadSysProcTftpPacketRate = _CadSysProcTftpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 11),
    _CadSysProcTftpPacketRate_Type()
)
cadSysProcTftpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcTftpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcTftpPacketRate.setUnits("packets/second")


class _CadSysProcIsisPacketRate_Type(Unsigned32):
    """Custom type cadSysProcIsisPacketRate based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcIsisPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcIsisPacketRate_Object = MibScalar
cadSysProcIsisPacketRate = _CadSysProcIsisPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 12),
    _CadSysProcIsisPacketRate_Type()
)
cadSysProcIsisPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcIsisPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIsisPacketRate.setUnits("packets/second")


class _CadSysProcNdPacketRate_Type(Unsigned32):
    """Custom type cadSysProcNdPacketRate based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcNdPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcNdPacketRate_Object = MibScalar
cadSysProcNdPacketRate = _CadSysProcNdPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 13),
    _CadSysProcNdPacketRate_Type()
)
cadSysProcNdPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcNdPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcNdPacketRate.setUnits("packets/second")


class _CadSysProcDhcpIpv6PacketRate_Type(Unsigned32):
    """Custom type cadSysProcDhcpIpv6PacketRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcDhcpIpv6PacketRate_Type.__name__ = "Unsigned32"
_CadSysProcDhcpIpv6PacketRate_Object = MibScalar
cadSysProcDhcpIpv6PacketRate = _CadSysProcDhcpIpv6PacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 14),
    _CadSysProcDhcpIpv6PacketRate_Type()
)
cadSysProcDhcpIpv6PacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcDhcpIpv6PacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcDhcpIpv6PacketRate.setUnits("packets/second")


class _CadSysProcIcmpIpv6PacketRate_Type(Unsigned32):
    """Custom type cadSysProcIcmpIpv6PacketRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcIcmpIpv6PacketRate_Type.__name__ = "Unsigned32"
_CadSysProcIcmpIpv6PacketRate_Object = MibScalar
cadSysProcIcmpIpv6PacketRate = _CadSysProcIcmpIpv6PacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 15),
    _CadSysProcIcmpIpv6PacketRate_Type()
)
cadSysProcIcmpIpv6PacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcIcmpIpv6PacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIcmpIpv6PacketRate.setUnits("packets/second")


class _CadSysProcMldPacketRate_Type(Unsigned32):
    """Custom type cadSysProcMldPacketRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcMldPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcMldPacketRate_Object = MibScalar
cadSysProcMldPacketRate = _CadSysProcMldPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 16),
    _CadSysProcMldPacketRate_Type()
)
cadSysProcMldPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcMldPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcMldPacketRate.setUnits("packets/second")


class _CadSysProcBgpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcBgpPacketRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcBgpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcBgpPacketRate_Object = MibScalar
cadSysProcBgpPacketRate = _CadSysProcBgpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 17),
    _CadSysProcBgpPacketRate_Type()
)
cadSysProcBgpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcBgpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcBgpPacketRate.setUnits("packets/second")


class _CadSysProcPimPacketRate_Type(Unsigned32):
    """Custom type cadSysProcPimPacketRate based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcPimPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcPimPacketRate_Object = MibScalar
cadSysProcPimPacketRate = _CadSysProcPimPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 18),
    _CadSysProcPimPacketRate_Type()
)
cadSysProcPimPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcPimPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcPimPacketRate.setUnits("packets/second")


class _CadSysProcSnmpCmPacketRate_Type(Unsigned32):
    """Custom type cadSysProcSnmpCmPacketRate based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcSnmpCmPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcSnmpCmPacketRate_Object = MibScalar
cadSysProcSnmpCmPacketRate = _CadSysProcSnmpCmPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 19),
    _CadSysProcSnmpCmPacketRate_Type()
)
cadSysProcSnmpCmPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcSnmpCmPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcSnmpCmPacketRate.setUnits("packets/second")


class _CadSysProcCopsPacketRate_Type(Unsigned32):
    """Custom type cadSysProcCopsPacketRate based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcCopsPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcCopsPacketRate_Object = MibScalar
cadSysProcCopsPacketRate = _CadSysProcCopsPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 20),
    _CadSysProcCopsPacketRate_Type()
)
cadSysProcCopsPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcCopsPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcCopsPacketRate.setUnits("packets/second")


class _CadSysProcTelnetPacketRate_Type(Unsigned32):
    """Custom type cadSysProcTelnetPacketRate based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcTelnetPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcTelnetPacketRate_Object = MibScalar
cadSysProcTelnetPacketRate = _CadSysProcTelnetPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 21),
    _CadSysProcTelnetPacketRate_Type()
)
cadSysProcTelnetPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcTelnetPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcTelnetPacketRate.setUnits("packets/second")


class _CadSysProcOspfv3PacketRate_Type(Unsigned32):
    """Custom type cadSysProcOspfv3PacketRate based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcOspfv3PacketRate_Type.__name__ = "Unsigned32"
_CadSysProcOspfv3PacketRate_Object = MibScalar
cadSysProcOspfv3PacketRate = _CadSysProcOspfv3PacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 22),
    _CadSysProcOspfv3PacketRate_Type()
)
cadSysProcOspfv3PacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcOspfv3PacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcOspfv3PacketRate.setUnits("packets/second")


class _CadSysProcTftpIpv6PacketRate_Type(Unsigned32):
    """Custom type cadSysProcTftpIpv6PacketRate based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcTftpIpv6PacketRate_Type.__name__ = "Unsigned32"
_CadSysProcTftpIpv6PacketRate_Object = MibScalar
cadSysProcTftpIpv6PacketRate = _CadSysProcTftpIpv6PacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 23),
    _CadSysProcTftpIpv6PacketRate_Type()
)
cadSysProcTftpIpv6PacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcTftpIpv6PacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcTftpIpv6PacketRate.setUnits("packets/second")


class _CadSysProcEventIcmpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcEventIcmpPacketRate based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcEventIcmpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcEventIcmpPacketRate_Object = MibScalar
cadSysProcEventIcmpPacketRate = _CadSysProcEventIcmpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 24),
    _CadSysProcEventIcmpPacketRate_Type()
)
cadSysProcEventIcmpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpPacketRate.setUnits("packets/second")


class _CadSysProcEventNoRoutePacketRate_Type(Unsigned32):
    """Custom type cadSysProcEventNoRoutePacketRate based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcEventNoRoutePacketRate_Type.__name__ = "Unsigned32"
_CadSysProcEventNoRoutePacketRate_Object = MibScalar
cadSysProcEventNoRoutePacketRate = _CadSysProcEventNoRoutePacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 25),
    _CadSysProcEventNoRoutePacketRate_Type()
)
cadSysProcEventNoRoutePacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcEventNoRoutePacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventNoRoutePacketRate.setUnits("packets/second")


class _CadSysProcEventIcmpIpv6PacketRate_Type(Unsigned32):
    """Custom type cadSysProcEventIcmpIpv6PacketRate based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcEventIcmpIpv6PacketRate_Type.__name__ = "Unsigned32"
_CadSysProcEventIcmpIpv6PacketRate_Object = MibScalar
cadSysProcEventIcmpIpv6PacketRate = _CadSysProcEventIcmpIpv6PacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 26),
    _CadSysProcEventIcmpIpv6PacketRate_Type()
)
cadSysProcEventIcmpIpv6PacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpIpv6PacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpIpv6PacketRate.setUnits("packets/second")


class _CadSysProcEventNoRouteIpv6PacketRate_Type(Unsigned32):
    """Custom type cadSysProcEventNoRouteIpv6PacketRate based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcEventNoRouteIpv6PacketRate_Type.__name__ = "Unsigned32"
_CadSysProcEventNoRouteIpv6PacketRate_Object = MibScalar
cadSysProcEventNoRouteIpv6PacketRate = _CadSysProcEventNoRouteIpv6PacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 27),
    _CadSysProcEventNoRouteIpv6PacketRate_Type()
)
cadSysProcEventNoRouteIpv6PacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcEventNoRouteIpv6PacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventNoRouteIpv6PacketRate.setUnits("packets/second")


class _CadSysProcEventArpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcEventArpPacketRate based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcEventArpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcEventArpPacketRate_Object = MibScalar
cadSysProcEventArpPacketRate = _CadSysProcEventArpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 28),
    _CadSysProcEventArpPacketRate_Type()
)
cadSysProcEventArpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcEventArpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventArpPacketRate.setUnits("packets/second")


class _CadSysProcEventNdPacketRate_Type(Unsigned32):
    """Custom type cadSysProcEventNdPacketRate based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcEventNdPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcEventNdPacketRate_Object = MibScalar
cadSysProcEventNdPacketRate = _CadSysProcEventNdPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 29),
    _CadSysProcEventNdPacketRate_Type()
)
cadSysProcEventNdPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcEventNdPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventNdPacketRate.setUnits("packets/second")


class _CadSysProcEventTtlPacketRate_Type(Unsigned32):
    """Custom type cadSysProcEventTtlPacketRate based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcEventTtlPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcEventTtlPacketRate_Object = MibScalar
cadSysProcEventTtlPacketRate = _CadSysProcEventTtlPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 30),
    _CadSysProcEventTtlPacketRate_Type()
)
cadSysProcEventTtlPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcEventTtlPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventTtlPacketRate.setUnits("packets/second")


class _CadSysProcEventTtlIpv6PacketRate_Type(Unsigned32):
    """Custom type cadSysProcEventTtlIpv6PacketRate based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcEventTtlIpv6PacketRate_Type.__name__ = "Unsigned32"
_CadSysProcEventTtlIpv6PacketRate_Object = MibScalar
cadSysProcEventTtlIpv6PacketRate = _CadSysProcEventTtlIpv6PacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 31),
    _CadSysProcEventTtlIpv6PacketRate_Type()
)
cadSysProcEventTtlIpv6PacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcEventTtlIpv6PacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventTtlIpv6PacketRate.setUnits("packets/second")


class _CadSysProcEventDadPacketRate_Type(Unsigned32):
    """Custom type cadSysProcEventDadPacketRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcEventDadPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcEventDadPacketRate_Object = MibScalar
cadSysProcEventDadPacketRate = _CadSysProcEventDadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 32),
    _CadSysProcEventDadPacketRate_Type()
)
cadSysProcEventDadPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcEventDadPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventDadPacketRate.setUnits("packets/second")


class _CadSysProcEventDefaultPacketRate_Type(Unsigned32):
    """Custom type cadSysProcEventDefaultPacketRate based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcEventDefaultPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcEventDefaultPacketRate_Object = MibScalar
cadSysProcEventDefaultPacketRate = _CadSysProcEventDefaultPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 33),
    _CadSysProcEventDefaultPacketRate_Type()
)
cadSysProcEventDefaultPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcEventDefaultPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventDefaultPacketRate.setUnits("packets/second")


class _CadSysProcLdpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcLdpPacketRate based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcLdpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcLdpPacketRate_Object = MibScalar
cadSysProcLdpPacketRate = _CadSysProcLdpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 34),
    _CadSysProcLdpPacketRate_Type()
)
cadSysProcLdpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcLdpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcLdpPacketRate.setUnits("packets/second")
_CadSysProcClearPolicingCounts_Type = TruthValue
_CadSysProcClearPolicingCounts_Object = MibScalar
cadSysProcClearPolicingCounts = _CadSysProcClearPolicingCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 35),
    _CadSysProcClearPolicingCounts_Type()
)
cadSysProcClearPolicingCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcClearPolicingCounts.setStatus("current")


class _CadSysProcLacpPacketRate_Type(Unsigned32):
    """Custom type cadSysProcLacpPacketRate based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcLacpPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcLacpPacketRate_Object = MibScalar
cadSysProcLacpPacketRate = _CadSysProcLacpPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 36),
    _CadSysProcLacpPacketRate_Type()
)
cadSysProcLacpPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcLacpPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcLacpPacketRate.setUnits("packets/second")


class _CadSysProcVrepPacketRate_Type(Unsigned32):
    """Custom type cadSysProcVrepPacketRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcVrepPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcVrepPacketRate_Object = MibScalar
cadSysProcVrepPacketRate = _CadSysProcVrepPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 37),
    _CadSysProcVrepPacketRate_Type()
)
cadSysProcVrepPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcVrepPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcVrepPacketRate.setUnits("packets/second")


class _CadSysProcVpmePacketRate_Type(Unsigned32):
    """Custom type cadSysProcVpmePacketRate based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcVpmePacketRate_Type.__name__ = "Unsigned32"
_CadSysProcVpmePacketRate_Object = MibScalar
cadSysProcVpmePacketRate = _CadSysProcVpmePacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 38),
    _CadSysProcVpmePacketRate_Type()
)
cadSysProcVpmePacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcVpmePacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcVpmePacketRate.setUnits("packets/second")


class _CadSysProcErmRpcPacketRate_Type(Unsigned32):
    """Custom type cadSysProcErmRpcPacketRate based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadSysProcErmRpcPacketRate_Type.__name__ = "Unsigned32"
_CadSysProcErmRpcPacketRate_Object = MibScalar
cadSysProcErmRpcPacketRate = _CadSysProcErmRpcPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 13, 39),
    _CadSysProcErmRpcPacketRate_Type()
)
cadSysProcErmRpcPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysProcErmRpcPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcErmRpcPacketRate.setUnits("packets/second")
_CadSysProcPolicingCounts_ObjectIdentity = ObjectIdentity
cadSysProcPolicingCounts = _CadSysProcPolicingCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14)
)
_CadSysProcRouterControlGlobalPacketsReceivedPassed_Type = Counter32
_CadSysProcRouterControlGlobalPacketsReceivedPassed_Object = MibScalar
cadSysProcRouterControlGlobalPacketsReceivedPassed = _CadSysProcRouterControlGlobalPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 1),
    _CadSysProcRouterControlGlobalPacketsReceivedPassed_Type()
)
cadSysProcRouterControlGlobalPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcRouterControlGlobalPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcRouterControlGlobalPacketsReceivedPassed.setUnits("packets")
_CadSysProcRouterControlGlobalPacketsReceivedDropped_Type = Counter32
_CadSysProcRouterControlGlobalPacketsReceivedDropped_Object = MibScalar
cadSysProcRouterControlGlobalPacketsReceivedDropped = _CadSysProcRouterControlGlobalPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 2),
    _CadSysProcRouterControlGlobalPacketsReceivedDropped_Type()
)
cadSysProcRouterControlGlobalPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcRouterControlGlobalPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcRouterControlGlobalPacketsReceivedDropped.setUnits("packets")
_CadSysProcArpPacketsReceivedPassed_Type = Counter32
_CadSysProcArpPacketsReceivedPassed_Object = MibScalar
cadSysProcArpPacketsReceivedPassed = _CadSysProcArpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 4),
    _CadSysProcArpPacketsReceivedPassed_Type()
)
cadSysProcArpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcArpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcArpPacketsReceivedPassed.setUnits("packets")
_CadSysProcArpPacketsReceivedDropped_Type = Counter32
_CadSysProcArpPacketsReceivedDropped_Object = MibScalar
cadSysProcArpPacketsReceivedDropped = _CadSysProcArpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 5),
    _CadSysProcArpPacketsReceivedDropped_Type()
)
cadSysProcArpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcArpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcArpPacketsReceivedDropped.setUnits("packets")
_CadSysProcDhcpPacketsReceivedPassed_Type = Counter32
_CadSysProcDhcpPacketsReceivedPassed_Object = MibScalar
cadSysProcDhcpPacketsReceivedPassed = _CadSysProcDhcpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 7),
    _CadSysProcDhcpPacketsReceivedPassed_Type()
)
cadSysProcDhcpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcDhcpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcDhcpPacketsReceivedPassed.setUnits("packets")
_CadSysProcDhcpPacketsReceivedDropped_Type = Counter32
_CadSysProcDhcpPacketsReceivedDropped_Object = MibScalar
cadSysProcDhcpPacketsReceivedDropped = _CadSysProcDhcpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 8),
    _CadSysProcDhcpPacketsReceivedDropped_Type()
)
cadSysProcDhcpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcDhcpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcDhcpPacketsReceivedDropped.setUnits("packets")
_CadSysProcIcmpPacketsReceivedPassed_Type = Counter32
_CadSysProcIcmpPacketsReceivedPassed_Object = MibScalar
cadSysProcIcmpPacketsReceivedPassed = _CadSysProcIcmpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 10),
    _CadSysProcIcmpPacketsReceivedPassed_Type()
)
cadSysProcIcmpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcIcmpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIcmpPacketsReceivedPassed.setUnits("packets")
_CadSysProcIcmpPacketsReceivedDropped_Type = Counter32
_CadSysProcIcmpPacketsReceivedDropped_Object = MibScalar
cadSysProcIcmpPacketsReceivedDropped = _CadSysProcIcmpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 11),
    _CadSysProcIcmpPacketsReceivedDropped_Type()
)
cadSysProcIcmpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcIcmpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIcmpPacketsReceivedDropped.setUnits("packets")
_CadSysProcOspfPacketsReceivedPassed_Type = Counter32
_CadSysProcOspfPacketsReceivedPassed_Object = MibScalar
cadSysProcOspfPacketsReceivedPassed = _CadSysProcOspfPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 13),
    _CadSysProcOspfPacketsReceivedPassed_Type()
)
cadSysProcOspfPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcOspfPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcOspfPacketsReceivedPassed.setUnits("packets")
_CadSysProcOspfPacketsReceivedDropped_Type = Counter32
_CadSysProcOspfPacketsReceivedDropped_Object = MibScalar
cadSysProcOspfPacketsReceivedDropped = _CadSysProcOspfPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 14),
    _CadSysProcOspfPacketsReceivedDropped_Type()
)
cadSysProcOspfPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcOspfPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcOspfPacketsReceivedDropped.setUnits("packets")
_CadSysProcRipPacketsReceivedPassed_Type = Counter32
_CadSysProcRipPacketsReceivedPassed_Object = MibScalar
cadSysProcRipPacketsReceivedPassed = _CadSysProcRipPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 16),
    _CadSysProcRipPacketsReceivedPassed_Type()
)
cadSysProcRipPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcRipPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcRipPacketsReceivedPassed.setUnits("packets")
_CadSysProcRipPacketsReceivedDropped_Type = Counter32
_CadSysProcRipPacketsReceivedDropped_Object = MibScalar
cadSysProcRipPacketsReceivedDropped = _CadSysProcRipPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 17),
    _CadSysProcRipPacketsReceivedDropped_Type()
)
cadSysProcRipPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcRipPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcRipPacketsReceivedDropped.setUnits("packets")
_CadSysProcIgmpPacketsReceivedPassed_Type = Counter32
_CadSysProcIgmpPacketsReceivedPassed_Object = MibScalar
cadSysProcIgmpPacketsReceivedPassed = _CadSysProcIgmpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 19),
    _CadSysProcIgmpPacketsReceivedPassed_Type()
)
cadSysProcIgmpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcIgmpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIgmpPacketsReceivedPassed.setUnits("packets")
_CadSysProcIgmpPacketsReceivedDropped_Type = Counter32
_CadSysProcIgmpPacketsReceivedDropped_Object = MibScalar
cadSysProcIgmpPacketsReceivedDropped = _CadSysProcIgmpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 20),
    _CadSysProcIgmpPacketsReceivedDropped_Type()
)
cadSysProcIgmpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcIgmpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIgmpPacketsReceivedDropped.setUnits("packets")
_CadSysProcRouterControlOtherPacketsReceivedPassed_Type = Counter32
_CadSysProcRouterControlOtherPacketsReceivedPassed_Object = MibScalar
cadSysProcRouterControlOtherPacketsReceivedPassed = _CadSysProcRouterControlOtherPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 22),
    _CadSysProcRouterControlOtherPacketsReceivedPassed_Type()
)
cadSysProcRouterControlOtherPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcRouterControlOtherPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcRouterControlOtherPacketsReceivedPassed.setUnits("packets")
_CadSysProcRouterControlOtherPacketsReceivedDropped_Type = Counter32
_CadSysProcRouterControlOtherPacketsReceivedDropped_Object = MibScalar
cadSysProcRouterControlOtherPacketsReceivedDropped = _CadSysProcRouterControlOtherPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 23),
    _CadSysProcRouterControlOtherPacketsReceivedDropped_Type()
)
cadSysProcRouterControlOtherPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcRouterControlOtherPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcRouterControlOtherPacketsReceivedDropped.setUnits("packets")
_CadSysProcSnmpPacketsReceivedPassed_Type = Counter32
_CadSysProcSnmpPacketsReceivedPassed_Object = MibScalar
cadSysProcSnmpPacketsReceivedPassed = _CadSysProcSnmpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 25),
    _CadSysProcSnmpPacketsReceivedPassed_Type()
)
cadSysProcSnmpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcSnmpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcSnmpPacketsReceivedPassed.setUnits("packets")
_CadSysProcSnmpPacketsReceivedDropped_Type = Counter32
_CadSysProcSnmpPacketsReceivedDropped_Object = MibScalar
cadSysProcSnmpPacketsReceivedDropped = _CadSysProcSnmpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 26),
    _CadSysProcSnmpPacketsReceivedDropped_Type()
)
cadSysProcSnmpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcSnmpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcSnmpPacketsReceivedDropped.setUnits("packets")
_CadSysProcTftpPacketsReceivedPassed_Type = Counter32
_CadSysProcTftpPacketsReceivedPassed_Object = MibScalar
cadSysProcTftpPacketsReceivedPassed = _CadSysProcTftpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 28),
    _CadSysProcTftpPacketsReceivedPassed_Type()
)
cadSysProcTftpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcTftpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcTftpPacketsReceivedPassed.setUnits("packets")
_CadSysProcTftpPacketsReceivedDropped_Type = Counter32
_CadSysProcTftpPacketsReceivedDropped_Object = MibScalar
cadSysProcTftpPacketsReceivedDropped = _CadSysProcTftpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 29),
    _CadSysProcTftpPacketsReceivedDropped_Type()
)
cadSysProcTftpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcTftpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcTftpPacketsReceivedDropped.setUnits("packets")
_CadSysProcIsisPacketsReceivedPassed_Type = Counter32
_CadSysProcIsisPacketsReceivedPassed_Object = MibScalar
cadSysProcIsisPacketsReceivedPassed = _CadSysProcIsisPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 31),
    _CadSysProcIsisPacketsReceivedPassed_Type()
)
cadSysProcIsisPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcIsisPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIsisPacketsReceivedPassed.setUnits("packets")
_CadSysProcIsisPacketsReceivedDropped_Type = Counter32
_CadSysProcIsisPacketsReceivedDropped_Object = MibScalar
cadSysProcIsisPacketsReceivedDropped = _CadSysProcIsisPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 32),
    _CadSysProcIsisPacketsReceivedDropped_Type()
)
cadSysProcIsisPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcIsisPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIsisPacketsReceivedDropped.setUnits("packets")
_CadSysProcNdPacketsReceivedPassed_Type = Counter32
_CadSysProcNdPacketsReceivedPassed_Object = MibScalar
cadSysProcNdPacketsReceivedPassed = _CadSysProcNdPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 37),
    _CadSysProcNdPacketsReceivedPassed_Type()
)
cadSysProcNdPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcNdPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcNdPacketsReceivedPassed.setUnits("packets")
_CadSysProcNdPacketsReceivedDropped_Type = Counter32
_CadSysProcNdPacketsReceivedDropped_Object = MibScalar
cadSysProcNdPacketsReceivedDropped = _CadSysProcNdPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 38),
    _CadSysProcNdPacketsReceivedDropped_Type()
)
cadSysProcNdPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcNdPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcNdPacketsReceivedDropped.setUnits("packets")
_CadSysProcDhcpIpv6PacketsReceivedPassed_Type = Counter32
_CadSysProcDhcpIpv6PacketsReceivedPassed_Object = MibScalar
cadSysProcDhcpIpv6PacketsReceivedPassed = _CadSysProcDhcpIpv6PacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 40),
    _CadSysProcDhcpIpv6PacketsReceivedPassed_Type()
)
cadSysProcDhcpIpv6PacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcDhcpIpv6PacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcDhcpIpv6PacketsReceivedPassed.setUnits("packets")
_CadSysProcDhcpIpv6PacketsReceivedDropped_Type = Counter32
_CadSysProcDhcpIpv6PacketsReceivedDropped_Object = MibScalar
cadSysProcDhcpIpv6PacketsReceivedDropped = _CadSysProcDhcpIpv6PacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 41),
    _CadSysProcDhcpIpv6PacketsReceivedDropped_Type()
)
cadSysProcDhcpIpv6PacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcDhcpIpv6PacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcDhcpIpv6PacketsReceivedDropped.setUnits("packets")
_CadSysProcIcmpIpv6PacketsReceivedPassed_Type = Counter32
_CadSysProcIcmpIpv6PacketsReceivedPassed_Object = MibScalar
cadSysProcIcmpIpv6PacketsReceivedPassed = _CadSysProcIcmpIpv6PacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 43),
    _CadSysProcIcmpIpv6PacketsReceivedPassed_Type()
)
cadSysProcIcmpIpv6PacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcIcmpIpv6PacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIcmpIpv6PacketsReceivedPassed.setUnits("packets")
_CadSysProcIcmpIpv6PacketsReceivedDropped_Type = Counter32
_CadSysProcIcmpIpv6PacketsReceivedDropped_Object = MibScalar
cadSysProcIcmpIpv6PacketsReceivedDropped = _CadSysProcIcmpIpv6PacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 44),
    _CadSysProcIcmpIpv6PacketsReceivedDropped_Type()
)
cadSysProcIcmpIpv6PacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcIcmpIpv6PacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcIcmpIpv6PacketsReceivedDropped.setUnits("packets")
_CadSysProcMldPacketsReceivedPassed_Type = Counter32
_CadSysProcMldPacketsReceivedPassed_Object = MibScalar
cadSysProcMldPacketsReceivedPassed = _CadSysProcMldPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 46),
    _CadSysProcMldPacketsReceivedPassed_Type()
)
cadSysProcMldPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcMldPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcMldPacketsReceivedPassed.setUnits("packets")
_CadSysProcMldPacketsReceivedDropped_Type = Counter32
_CadSysProcMldPacketsReceivedDropped_Object = MibScalar
cadSysProcMldPacketsReceivedDropped = _CadSysProcMldPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 47),
    _CadSysProcMldPacketsReceivedDropped_Type()
)
cadSysProcMldPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcMldPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcMldPacketsReceivedDropped.setUnits("packets")
_CadSysProcBgpPacketsReceivedPassed_Type = Counter32
_CadSysProcBgpPacketsReceivedPassed_Object = MibScalar
cadSysProcBgpPacketsReceivedPassed = _CadSysProcBgpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 49),
    _CadSysProcBgpPacketsReceivedPassed_Type()
)
cadSysProcBgpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcBgpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcBgpPacketsReceivedPassed.setUnits("packets")
_CadSysProcBgpPacketsReceivedDropped_Type = Counter32
_CadSysProcBgpPacketsReceivedDropped_Object = MibScalar
cadSysProcBgpPacketsReceivedDropped = _CadSysProcBgpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 50),
    _CadSysProcBgpPacketsReceivedDropped_Type()
)
cadSysProcBgpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcBgpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcBgpPacketsReceivedDropped.setUnits("packets")
_CadSysProcPimPacketsReceivedPassed_Type = Counter32
_CadSysProcPimPacketsReceivedPassed_Object = MibScalar
cadSysProcPimPacketsReceivedPassed = _CadSysProcPimPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 52),
    _CadSysProcPimPacketsReceivedPassed_Type()
)
cadSysProcPimPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcPimPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcPimPacketsReceivedPassed.setUnits("packets")
_CadSysProcPimPacketsReceivedDropped_Type = Counter32
_CadSysProcPimPacketsReceivedDropped_Object = MibScalar
cadSysProcPimPacketsReceivedDropped = _CadSysProcPimPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 53),
    _CadSysProcPimPacketsReceivedDropped_Type()
)
cadSysProcPimPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcPimPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcPimPacketsReceivedDropped.setUnits("packets")
_CadSysProcSnmpCmPacketsReceivedPassed_Type = Counter32
_CadSysProcSnmpCmPacketsReceivedPassed_Object = MibScalar
cadSysProcSnmpCmPacketsReceivedPassed = _CadSysProcSnmpCmPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 55),
    _CadSysProcSnmpCmPacketsReceivedPassed_Type()
)
cadSysProcSnmpCmPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcSnmpCmPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcSnmpCmPacketsReceivedPassed.setUnits("packets")
_CadSysProcSnmpCmPacketsReceivedDropped_Type = Counter32
_CadSysProcSnmpCmPacketsReceivedDropped_Object = MibScalar
cadSysProcSnmpCmPacketsReceivedDropped = _CadSysProcSnmpCmPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 56),
    _CadSysProcSnmpCmPacketsReceivedDropped_Type()
)
cadSysProcSnmpCmPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcSnmpCmPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcSnmpCmPacketsReceivedDropped.setUnits("packets")
_CadSysProcCopsPacketsReceivedPassed_Type = Counter32
_CadSysProcCopsPacketsReceivedPassed_Object = MibScalar
cadSysProcCopsPacketsReceivedPassed = _CadSysProcCopsPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 58),
    _CadSysProcCopsPacketsReceivedPassed_Type()
)
cadSysProcCopsPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcCopsPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcCopsPacketsReceivedPassed.setUnits("packets")
_CadSysProcCopsPacketsReceivedDropped_Type = Counter32
_CadSysProcCopsPacketsReceivedDropped_Object = MibScalar
cadSysProcCopsPacketsReceivedDropped = _CadSysProcCopsPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 59),
    _CadSysProcCopsPacketsReceivedDropped_Type()
)
cadSysProcCopsPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcCopsPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcCopsPacketsReceivedDropped.setUnits("packets")
_CadSysProcTelnetPacketsReceivedPassed_Type = Counter32
_CadSysProcTelnetPacketsReceivedPassed_Object = MibScalar
cadSysProcTelnetPacketsReceivedPassed = _CadSysProcTelnetPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 61),
    _CadSysProcTelnetPacketsReceivedPassed_Type()
)
cadSysProcTelnetPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcTelnetPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcTelnetPacketsReceivedPassed.setUnits("packets")
_CadSysProcTelnetPacketsReceivedDropped_Type = Counter32
_CadSysProcTelnetPacketsReceivedDropped_Object = MibScalar
cadSysProcTelnetPacketsReceivedDropped = _CadSysProcTelnetPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 62),
    _CadSysProcTelnetPacketsReceivedDropped_Type()
)
cadSysProcTelnetPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcTelnetPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcTelnetPacketsReceivedDropped.setUnits("packets")
_CadSysProcOspfv3PacketsReceivedPassed_Type = Counter32
_CadSysProcOspfv3PacketsReceivedPassed_Object = MibScalar
cadSysProcOspfv3PacketsReceivedPassed = _CadSysProcOspfv3PacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 64),
    _CadSysProcOspfv3PacketsReceivedPassed_Type()
)
cadSysProcOspfv3PacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcOspfv3PacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcOspfv3PacketsReceivedPassed.setUnits("packets")
_CadSysProcOspfv3PacketsReceivedDropped_Type = Counter32
_CadSysProcOspfv3PacketsReceivedDropped_Object = MibScalar
cadSysProcOspfv3PacketsReceivedDropped = _CadSysProcOspfv3PacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 65),
    _CadSysProcOspfv3PacketsReceivedDropped_Type()
)
cadSysProcOspfv3PacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcOspfv3PacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcOspfv3PacketsReceivedDropped.setUnits("packets")
_CadSysProcTftpIpv6PacketsReceivedPassed_Type = Counter32
_CadSysProcTftpIpv6PacketsReceivedPassed_Object = MibScalar
cadSysProcTftpIpv6PacketsReceivedPassed = _CadSysProcTftpIpv6PacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 67),
    _CadSysProcTftpIpv6PacketsReceivedPassed_Type()
)
cadSysProcTftpIpv6PacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcTftpIpv6PacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcTftpIpv6PacketsReceivedPassed.setUnits("packets")
_CadSysProcTftpIpv6PacketsReceivedDropped_Type = Counter32
_CadSysProcTftpIpv6PacketsReceivedDropped_Object = MibScalar
cadSysProcTftpIpv6PacketsReceivedDropped = _CadSysProcTftpIpv6PacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 68),
    _CadSysProcTftpIpv6PacketsReceivedDropped_Type()
)
cadSysProcTftpIpv6PacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcTftpIpv6PacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcTftpIpv6PacketsReceivedDropped.setUnits("packets")
_CadSysProcLdpPacketsReceivedPassed_Type = Counter32
_CadSysProcLdpPacketsReceivedPassed_Object = MibScalar
cadSysProcLdpPacketsReceivedPassed = _CadSysProcLdpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 70),
    _CadSysProcLdpPacketsReceivedPassed_Type()
)
cadSysProcLdpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcLdpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcLdpPacketsReceivedPassed.setUnits("packets")
_CadSysProcLdpPacketsReceivedDropped_Type = Counter32
_CadSysProcLdpPacketsReceivedDropped_Object = MibScalar
cadSysProcLdpPacketsReceivedDropped = _CadSysProcLdpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 71),
    _CadSysProcLdpPacketsReceivedDropped_Type()
)
cadSysProcLdpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcLdpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcLdpPacketsReceivedDropped.setUnits("packets")
_CadSysProcEventIcmpPacketsReceivedPassed_Type = Counter32
_CadSysProcEventIcmpPacketsReceivedPassed_Object = MibScalar
cadSysProcEventIcmpPacketsReceivedPassed = _CadSysProcEventIcmpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 73),
    _CadSysProcEventIcmpPacketsReceivedPassed_Type()
)
cadSysProcEventIcmpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpPacketsReceivedPassed.setUnits("packets")
_CadSysProcEventIcmpPacketsReceivedDropped_Type = Counter32
_CadSysProcEventIcmpPacketsReceivedDropped_Object = MibScalar
cadSysProcEventIcmpPacketsReceivedDropped = _CadSysProcEventIcmpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 74),
    _CadSysProcEventIcmpPacketsReceivedDropped_Type()
)
cadSysProcEventIcmpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpPacketsReceivedDropped.setUnits("packets")
_CadSysProcEventNoRoutePacketsReceivedPassed_Type = Counter32
_CadSysProcEventNoRoutePacketsReceivedPassed_Object = MibScalar
cadSysProcEventNoRoutePacketsReceivedPassed = _CadSysProcEventNoRoutePacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 75),
    _CadSysProcEventNoRoutePacketsReceivedPassed_Type()
)
cadSysProcEventNoRoutePacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventNoRoutePacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventNoRoutePacketsReceivedPassed.setUnits("packets")
_CadSysProcEventNoRoutePacketsReceivedDropped_Type = Counter32
_CadSysProcEventNoRoutePacketsReceivedDropped_Object = MibScalar
cadSysProcEventNoRoutePacketsReceivedDropped = _CadSysProcEventNoRoutePacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 76),
    _CadSysProcEventNoRoutePacketsReceivedDropped_Type()
)
cadSysProcEventNoRoutePacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventNoRoutePacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventNoRoutePacketsReceivedDropped.setUnits("packets")
_CadSysProcEventIcmpIpv6PacketsReceivedPassed_Type = Counter32
_CadSysProcEventIcmpIpv6PacketsReceivedPassed_Object = MibScalar
cadSysProcEventIcmpIpv6PacketsReceivedPassed = _CadSysProcEventIcmpIpv6PacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 77),
    _CadSysProcEventIcmpIpv6PacketsReceivedPassed_Type()
)
cadSysProcEventIcmpIpv6PacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpIpv6PacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpIpv6PacketsReceivedPassed.setUnits("packets")
_CadSysProcEventIcmpIpv6PacketsReceivedDropped_Type = Counter32
_CadSysProcEventIcmpIpv6PacketsReceivedDropped_Object = MibScalar
cadSysProcEventIcmpIpv6PacketsReceivedDropped = _CadSysProcEventIcmpIpv6PacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 78),
    _CadSysProcEventIcmpIpv6PacketsReceivedDropped_Type()
)
cadSysProcEventIcmpIpv6PacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpIpv6PacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventIcmpIpv6PacketsReceivedDropped.setUnits("packets")
_CadSysProcEventNoRouteIpv6PacketsReceivedPassed_Type = Counter32
_CadSysProcEventNoRouteIpv6PacketsReceivedPassed_Object = MibScalar
cadSysProcEventNoRouteIpv6PacketsReceivedPassed = _CadSysProcEventNoRouteIpv6PacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 79),
    _CadSysProcEventNoRouteIpv6PacketsReceivedPassed_Type()
)
cadSysProcEventNoRouteIpv6PacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventNoRouteIpv6PacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventNoRouteIpv6PacketsReceivedPassed.setUnits("packets")
_CadSysProcEventNoRouteIpv6PacketsReceivedDropped_Type = Counter32
_CadSysProcEventNoRouteIpv6PacketsReceivedDropped_Object = MibScalar
cadSysProcEventNoRouteIpv6PacketsReceivedDropped = _CadSysProcEventNoRouteIpv6PacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 80),
    _CadSysProcEventNoRouteIpv6PacketsReceivedDropped_Type()
)
cadSysProcEventNoRouteIpv6PacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventNoRouteIpv6PacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventNoRouteIpv6PacketsReceivedDropped.setUnits("packets")
_CadSysProcEventArpPacketsReceivedPassed_Type = Counter32
_CadSysProcEventArpPacketsReceivedPassed_Object = MibScalar
cadSysProcEventArpPacketsReceivedPassed = _CadSysProcEventArpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 81),
    _CadSysProcEventArpPacketsReceivedPassed_Type()
)
cadSysProcEventArpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventArpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventArpPacketsReceivedPassed.setUnits("packets")
_CadSysProcEventArpPacketsReceivedDropped_Type = Counter32
_CadSysProcEventArpPacketsReceivedDropped_Object = MibScalar
cadSysProcEventArpPacketsReceivedDropped = _CadSysProcEventArpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 82),
    _CadSysProcEventArpPacketsReceivedDropped_Type()
)
cadSysProcEventArpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventArpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventArpPacketsReceivedDropped.setUnits("packets")
_CadSysProcEventNdPacketsReceivedPassed_Type = Counter32
_CadSysProcEventNdPacketsReceivedPassed_Object = MibScalar
cadSysProcEventNdPacketsReceivedPassed = _CadSysProcEventNdPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 83),
    _CadSysProcEventNdPacketsReceivedPassed_Type()
)
cadSysProcEventNdPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventNdPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventNdPacketsReceivedPassed.setUnits("packets")
_CadSysProcEventNdPacketsReceivedDropped_Type = Counter32
_CadSysProcEventNdPacketsReceivedDropped_Object = MibScalar
cadSysProcEventNdPacketsReceivedDropped = _CadSysProcEventNdPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 84),
    _CadSysProcEventNdPacketsReceivedDropped_Type()
)
cadSysProcEventNdPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventNdPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventNdPacketsReceivedDropped.setUnits("packets")
_CadSysProcEventTtlPacketsReceivedPassed_Type = Counter32
_CadSysProcEventTtlPacketsReceivedPassed_Object = MibScalar
cadSysProcEventTtlPacketsReceivedPassed = _CadSysProcEventTtlPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 85),
    _CadSysProcEventTtlPacketsReceivedPassed_Type()
)
cadSysProcEventTtlPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventTtlPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventTtlPacketsReceivedPassed.setUnits("packets")
_CadSysProcEventTtlPacketsReceivedDropped_Type = Counter32
_CadSysProcEventTtlPacketsReceivedDropped_Object = MibScalar
cadSysProcEventTtlPacketsReceivedDropped = _CadSysProcEventTtlPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 86),
    _CadSysProcEventTtlPacketsReceivedDropped_Type()
)
cadSysProcEventTtlPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventTtlPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventTtlPacketsReceivedDropped.setUnits("packets")
_CadSysProcEventTtlIpv6PacketsReceivedPassed_Type = Counter32
_CadSysProcEventTtlIpv6PacketsReceivedPassed_Object = MibScalar
cadSysProcEventTtlIpv6PacketsReceivedPassed = _CadSysProcEventTtlIpv6PacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 87),
    _CadSysProcEventTtlIpv6PacketsReceivedPassed_Type()
)
cadSysProcEventTtlIpv6PacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventTtlIpv6PacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventTtlIpv6PacketsReceivedPassed.setUnits("packets")
_CadSysProcEventTtlIpv6PacketsReceivedDropped_Type = Counter32
_CadSysProcEventTtlIpv6PacketsReceivedDropped_Object = MibScalar
cadSysProcEventTtlIpv6PacketsReceivedDropped = _CadSysProcEventTtlIpv6PacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 88),
    _CadSysProcEventTtlIpv6PacketsReceivedDropped_Type()
)
cadSysProcEventTtlIpv6PacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventTtlIpv6PacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventTtlIpv6PacketsReceivedDropped.setUnits("packets")
_CadSysProcEventDadPacketsReceivedPassed_Type = Counter32
_CadSysProcEventDadPacketsReceivedPassed_Object = MibScalar
cadSysProcEventDadPacketsReceivedPassed = _CadSysProcEventDadPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 89),
    _CadSysProcEventDadPacketsReceivedPassed_Type()
)
cadSysProcEventDadPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventDadPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventDadPacketsReceivedPassed.setUnits("packets")
_CadSysProcEventDadPacketsReceivedDropped_Type = Counter32
_CadSysProcEventDadPacketsReceivedDropped_Object = MibScalar
cadSysProcEventDadPacketsReceivedDropped = _CadSysProcEventDadPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 90),
    _CadSysProcEventDadPacketsReceivedDropped_Type()
)
cadSysProcEventDadPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventDadPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventDadPacketsReceivedDropped.setUnits("packets")
_CadSysProcEventDefaultPacketsReceivedPassed_Type = Counter32
_CadSysProcEventDefaultPacketsReceivedPassed_Object = MibScalar
cadSysProcEventDefaultPacketsReceivedPassed = _CadSysProcEventDefaultPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 91),
    _CadSysProcEventDefaultPacketsReceivedPassed_Type()
)
cadSysProcEventDefaultPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventDefaultPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventDefaultPacketsReceivedPassed.setUnits("packets")
_CadSysProcEventDefaultPacketsReceivedDropped_Type = Counter32
_CadSysProcEventDefaultPacketsReceivedDropped_Object = MibScalar
cadSysProcEventDefaultPacketsReceivedDropped = _CadSysProcEventDefaultPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 92),
    _CadSysProcEventDefaultPacketsReceivedDropped_Type()
)
cadSysProcEventDefaultPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcEventDefaultPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcEventDefaultPacketsReceivedDropped.setUnits("packets")
_CadSysProcLacpPacketsReceivedPassed_Type = Counter32
_CadSysProcLacpPacketsReceivedPassed_Object = MibScalar
cadSysProcLacpPacketsReceivedPassed = _CadSysProcLacpPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 93),
    _CadSysProcLacpPacketsReceivedPassed_Type()
)
cadSysProcLacpPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcLacpPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcLacpPacketsReceivedPassed.setUnits("packets")
_CadSysProcLacpPacketsReceivedDropped_Type = Counter32
_CadSysProcLacpPacketsReceivedDropped_Object = MibScalar
cadSysProcLacpPacketsReceivedDropped = _CadSysProcLacpPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 94),
    _CadSysProcLacpPacketsReceivedDropped_Type()
)
cadSysProcLacpPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcLacpPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcLacpPacketsReceivedDropped.setUnits("packets")
_CadSysProcVrepPacketsReceivedPassed_Type = Counter32
_CadSysProcVrepPacketsReceivedPassed_Object = MibScalar
cadSysProcVrepPacketsReceivedPassed = _CadSysProcVrepPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 95),
    _CadSysProcVrepPacketsReceivedPassed_Type()
)
cadSysProcVrepPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcVrepPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcVrepPacketsReceivedPassed.setUnits("packets")
_CadSysProcVrepPacketsReceivedDropped_Type = Counter32
_CadSysProcVrepPacketsReceivedDropped_Object = MibScalar
cadSysProcVrepPacketsReceivedDropped = _CadSysProcVrepPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 96),
    _CadSysProcVrepPacketsReceivedDropped_Type()
)
cadSysProcVrepPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcVrepPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcVrepPacketsReceivedDropped.setUnits("packets")
_CadSysProcVpmePacketsReceivedPassed_Type = Counter32
_CadSysProcVpmePacketsReceivedPassed_Object = MibScalar
cadSysProcVpmePacketsReceivedPassed = _CadSysProcVpmePacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 97),
    _CadSysProcVpmePacketsReceivedPassed_Type()
)
cadSysProcVpmePacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcVpmePacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcVpmePacketsReceivedPassed.setUnits("packets")
_CadSysProcVpmePacketsReceivedDropped_Type = Counter32
_CadSysProcVpmePacketsReceivedDropped_Object = MibScalar
cadSysProcVpmePacketsReceivedDropped = _CadSysProcVpmePacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 98),
    _CadSysProcVpmePacketsReceivedDropped_Type()
)
cadSysProcVpmePacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcVpmePacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcVpmePacketsReceivedDropped.setUnits("packets")
_CadSysProcErmRpcPacketsReceivedPassed_Type = Counter32
_CadSysProcErmRpcPacketsReceivedPassed_Object = MibScalar
cadSysProcErmRpcPacketsReceivedPassed = _CadSysProcErmRpcPacketsReceivedPassed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 99),
    _CadSysProcErmRpcPacketsReceivedPassed_Type()
)
cadSysProcErmRpcPacketsReceivedPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcErmRpcPacketsReceivedPassed.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcErmRpcPacketsReceivedPassed.setUnits("packets")
_CadSysProcErmRpcPacketsReceivedDropped_Type = Counter32
_CadSysProcErmRpcPacketsReceivedDropped_Object = MibScalar
cadSysProcErmRpcPacketsReceivedDropped = _CadSysProcErmRpcPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 14, 100),
    _CadSysProcErmRpcPacketsReceivedDropped_Type()
)
cadSysProcErmRpcPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysProcErmRpcPacketsReceivedDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadSysProcErmRpcPacketsReceivedDropped.setUnits("packets")
_CadSysBanner_ObjectIdentity = ObjectIdentity
cadSysBanner = _CadSysBanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15)
)
_CadSysBannerMotdTable_Object = MibTable
cadSysBannerMotdTable = _CadSysBannerMotdTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 1)
)
if mibBuilder.loadTexts:
    cadSysBannerMotdTable.setStatus("current")
_CadSysBannerMotdEntry_Object = MibTableRow
cadSysBannerMotdEntry = _CadSysBannerMotdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 1, 1)
)
cadSysBannerMotdEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysBannerMotdLine"),
)
if mibBuilder.loadTexts:
    cadSysBannerMotdEntry.setStatus("current")


class _CadSysBannerMotdLine_Type(Integer32):
    """Custom type cadSysBannerMotdLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CadSysBannerMotdLine_Type.__name__ = "Integer32"
_CadSysBannerMotdLine_Object = MibTableColumn
cadSysBannerMotdLine = _CadSysBannerMotdLine_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 1, 1, 1),
    _CadSysBannerMotdLine_Type()
)
cadSysBannerMotdLine.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysBannerMotdLine.setStatus("current")


class _CadSysBannerMotdText_Type(DisplayString):
    """Custom type cadSysBannerMotdText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CadSysBannerMotdText_Type.__name__ = "DisplayString"
_CadSysBannerMotdText_Object = MibTableColumn
cadSysBannerMotdText = _CadSysBannerMotdText_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 1, 1, 2),
    _CadSysBannerMotdText_Type()
)
cadSysBannerMotdText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysBannerMotdText.setStatus("current")
_CadSysBannerMotdRowStatus_Type = RowStatus
_CadSysBannerMotdRowStatus_Object = MibTableColumn
cadSysBannerMotdRowStatus = _CadSysBannerMotdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 1, 1, 3),
    _CadSysBannerMotdRowStatus_Type()
)
cadSysBannerMotdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysBannerMotdRowStatus.setStatus("current")
_CadSysBannerLoginTable_Object = MibTable
cadSysBannerLoginTable = _CadSysBannerLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 2)
)
if mibBuilder.loadTexts:
    cadSysBannerLoginTable.setStatus("current")
_CadSysBannerLoginEntry_Object = MibTableRow
cadSysBannerLoginEntry = _CadSysBannerLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 2, 1)
)
cadSysBannerLoginEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysBannerLoginLine"),
)
if mibBuilder.loadTexts:
    cadSysBannerLoginEntry.setStatus("current")


class _CadSysBannerLoginLine_Type(Integer32):
    """Custom type cadSysBannerLoginLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CadSysBannerLoginLine_Type.__name__ = "Integer32"
_CadSysBannerLoginLine_Object = MibTableColumn
cadSysBannerLoginLine = _CadSysBannerLoginLine_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 2, 1, 1),
    _CadSysBannerLoginLine_Type()
)
cadSysBannerLoginLine.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysBannerLoginLine.setStatus("current")


class _CadSysBannerLoginText_Type(DisplayString):
    """Custom type cadSysBannerLoginText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CadSysBannerLoginText_Type.__name__ = "DisplayString"
_CadSysBannerLoginText_Object = MibTableColumn
cadSysBannerLoginText = _CadSysBannerLoginText_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 2, 1, 2),
    _CadSysBannerLoginText_Type()
)
cadSysBannerLoginText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysBannerLoginText.setStatus("current")
_CadSysBannerLoginRowStatus_Type = RowStatus
_CadSysBannerLoginRowStatus_Object = MibTableColumn
cadSysBannerLoginRowStatus = _CadSysBannerLoginRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 2, 1, 3),
    _CadSysBannerLoginRowStatus_Type()
)
cadSysBannerLoginRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysBannerLoginRowStatus.setStatus("current")
_CadSysBannerExecTable_Object = MibTable
cadSysBannerExecTable = _CadSysBannerExecTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 3)
)
if mibBuilder.loadTexts:
    cadSysBannerExecTable.setStatus("current")
_CadSysBannerExecEntry_Object = MibTableRow
cadSysBannerExecEntry = _CadSysBannerExecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 3, 1)
)
cadSysBannerExecEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysBannerExecLine"),
)
if mibBuilder.loadTexts:
    cadSysBannerExecEntry.setStatus("current")


class _CadSysBannerExecLine_Type(Integer32):
    """Custom type cadSysBannerExecLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_CadSysBannerExecLine_Type.__name__ = "Integer32"
_CadSysBannerExecLine_Object = MibTableColumn
cadSysBannerExecLine = _CadSysBannerExecLine_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 3, 1, 1),
    _CadSysBannerExecLine_Type()
)
cadSysBannerExecLine.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysBannerExecLine.setStatus("current")


class _CadSysBannerExecText_Type(DisplayString):
    """Custom type cadSysBannerExecText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CadSysBannerExecText_Type.__name__ = "DisplayString"
_CadSysBannerExecText_Object = MibTableColumn
cadSysBannerExecText = _CadSysBannerExecText_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 3, 1, 2),
    _CadSysBannerExecText_Type()
)
cadSysBannerExecText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysBannerExecText.setStatus("current")
_CadSysBannerExecRowStatus_Type = RowStatus
_CadSysBannerExecRowStatus_Object = MibTableColumn
cadSysBannerExecRowStatus = _CadSysBannerExecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 3, 1, 3),
    _CadSysBannerExecRowStatus_Type()
)
cadSysBannerExecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysBannerExecRowStatus.setStatus("current")
_CadSysBannerIncomingTable_Object = MibTable
cadSysBannerIncomingTable = _CadSysBannerIncomingTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 4)
)
if mibBuilder.loadTexts:
    cadSysBannerIncomingTable.setStatus("current")
_CadSysBannerIncomingEntry_Object = MibTableRow
cadSysBannerIncomingEntry = _CadSysBannerIncomingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 4, 1)
)
cadSysBannerIncomingEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysBannerIncomingLine"),
)
if mibBuilder.loadTexts:
    cadSysBannerIncomingEntry.setStatus("current")


class _CadSysBannerIncomingLine_Type(Integer32):
    """Custom type cadSysBannerIncomingLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_CadSysBannerIncomingLine_Type.__name__ = "Integer32"
_CadSysBannerIncomingLine_Object = MibTableColumn
cadSysBannerIncomingLine = _CadSysBannerIncomingLine_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 4, 1, 1),
    _CadSysBannerIncomingLine_Type()
)
cadSysBannerIncomingLine.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysBannerIncomingLine.setStatus("current")


class _CadSysBannerIncomingText_Type(DisplayString):
    """Custom type cadSysBannerIncomingText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CadSysBannerIncomingText_Type.__name__ = "DisplayString"
_CadSysBannerIncomingText_Object = MibTableColumn
cadSysBannerIncomingText = _CadSysBannerIncomingText_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 4, 1, 2),
    _CadSysBannerIncomingText_Type()
)
cadSysBannerIncomingText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysBannerIncomingText.setStatus("current")
_CadSysBannerIncomingRowStatus_Type = RowStatus
_CadSysBannerIncomingRowStatus_Object = MibTableColumn
cadSysBannerIncomingRowStatus = _CadSysBannerIncomingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 15, 4, 1, 3),
    _CadSysBannerIncomingRowStatus_Type()
)
cadSysBannerIncomingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysBannerIncomingRowStatus.setStatus("current")
_CadSysServer_ObjectIdentity = ObjectIdentity
cadSysServer = _CadSysServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 16)
)
_CadSysServerTable_Object = MibTable
cadSysServerTable = _CadSysServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cadSysServerTable.setStatus("current")
_CadSysServerEntry_Object = MibTableRow
cadSysServerEntry = _CadSysServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 16, 1, 1)
)
cadSysServerEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysServerType"),
)
if mibBuilder.loadTexts:
    cadSysServerEntry.setStatus("current")
_CadSysServerType_Type = ServerType
_CadSysServerType_Object = MibTableColumn
cadSysServerType = _CadSysServerType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 16, 1, 1, 1),
    _CadSysServerType_Type()
)
cadSysServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysServerType.setStatus("current")


class _CadSysServerAdminState_Type(AdminState):
    """Custom type cadSysServerAdminState based on AdminState"""


_CadSysServerAdminState_Object = MibTableColumn
cadSysServerAdminState = _CadSysServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 16, 1, 1, 2),
    _CadSysServerAdminState_Type()
)
cadSysServerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysServerAdminState.setStatus("current")
_CadSysPatchParams_ObjectIdentity = ObjectIdentity
cadSysPatchParams = _CadSysPatchParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 17)
)
_CadSysPatchParamTable_Object = MibTable
cadSysPatchParamTable = _CadSysPatchParamTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 17, 1)
)
if mibBuilder.loadTexts:
    cadSysPatchParamTable.setStatus("current")
_CadSysPatchParamEntry_Object = MibTableRow
cadSysPatchParamEntry = _CadSysPatchParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 17, 1, 1)
)
cadSysPatchParamEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysPatchParamIndex"),
)
if mibBuilder.loadTexts:
    cadSysPatchParamEntry.setStatus("current")


class _CadSysPatchParamIndex_Type(Integer32):
    """Custom type cadSysPatchParamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CadSysPatchParamIndex_Type.__name__ = "Integer32"
_CadSysPatchParamIndex_Object = MibTableColumn
cadSysPatchParamIndex = _CadSysPatchParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 17, 1, 1, 1),
    _CadSysPatchParamIndex_Type()
)
cadSysPatchParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysPatchParamIndex.setStatus("current")


class _CadSysPatchParamName_Type(DisplayString):
    """Custom type cadSysPatchParamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadSysPatchParamName_Type.__name__ = "DisplayString"
_CadSysPatchParamName_Object = MibTableColumn
cadSysPatchParamName = _CadSysPatchParamName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 17, 1, 1, 2),
    _CadSysPatchParamName_Type()
)
cadSysPatchParamName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysPatchParamName.setStatus("current")


class _CadSysPatchParamValue_Type(DisplayString):
    """Custom type cadSysPatchParamValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadSysPatchParamValue_Type.__name__ = "DisplayString"
_CadSysPatchParamValue_Object = MibTableColumn
cadSysPatchParamValue = _CadSysPatchParamValue_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 17, 1, 1, 3),
    _CadSysPatchParamValue_Type()
)
cadSysPatchParamValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysPatchParamValue.setStatus("current")


class _CadSysPatchParamDescription_Type(DisplayString):
    """Custom type cadSysPatchParamDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadSysPatchParamDescription_Type.__name__ = "DisplayString"
_CadSysPatchParamDescription_Object = MibTableColumn
cadSysPatchParamDescription = _CadSysPatchParamDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 17, 1, 1, 4),
    _CadSysPatchParamDescription_Type()
)
cadSysPatchParamDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysPatchParamDescription.setStatus("current")
_CadSysPatchParamRowStatus_Type = RowStatus
_CadSysPatchParamRowStatus_Object = MibTableColumn
cadSysPatchParamRowStatus = _CadSysPatchParamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 17, 1, 1, 5),
    _CadSysPatchParamRowStatus_Type()
)
cadSysPatchParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysPatchParamRowStatus.setStatus("current")
_CadSysMtceParams_ObjectIdentity = ObjectIdentity
cadSysMtceParams = _CadSysMtceParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 19)
)


class _CadSysMtceStatusCloneMonitorThreshold_Type(Unsigned32):
    """Custom type cadSysMtceStatusCloneMonitorThreshold based on Unsigned32"""
    defaultValue = 6000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2750, 6250),
    )


_CadSysMtceStatusCloneMonitorThreshold_Type.__name__ = "Unsigned32"
_CadSysMtceStatusCloneMonitorThreshold_Object = MibScalar
cadSysMtceStatusCloneMonitorThreshold = _CadSysMtceStatusCloneMonitorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 19, 8),
    _CadSysMtceStatusCloneMonitorThreshold_Type()
)
cadSysMtceStatusCloneMonitorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMtceStatusCloneMonitorThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cadSysMtceStatusCloneMonitorThreshold.setUnits("milliseconds")


class _CadSysMtceStatusCloneInitThreshold_Type(Unsigned32):
    """Custom type cadSysMtceStatusCloneInitThreshold based on Unsigned32"""
    defaultValue = 7500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 9000),
    )


_CadSysMtceStatusCloneInitThreshold_Type.__name__ = "Unsigned32"
_CadSysMtceStatusCloneInitThreshold_Object = MibScalar
cadSysMtceStatusCloneInitThreshold = _CadSysMtceStatusCloneInitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 19, 9),
    _CadSysMtceStatusCloneInitThreshold_Type()
)
cadSysMtceStatusCloneInitThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMtceStatusCloneInitThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cadSysMtceStatusCloneInitThreshold.setUnits("milliseconds")


class _CadSysMtceStatusCloneRcvyThreshold_Type(Unsigned32):
    """Custom type cadSysMtceStatusCloneRcvyThreshold based on Unsigned32"""
    defaultValue = 240000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120000, 360000),
    )


_CadSysMtceStatusCloneRcvyThreshold_Type.__name__ = "Unsigned32"
_CadSysMtceStatusCloneRcvyThreshold_Object = MibScalar
cadSysMtceStatusCloneRcvyThreshold = _CadSysMtceStatusCloneRcvyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 19, 10),
    _CadSysMtceStatusCloneRcvyThreshold_Type()
)
cadSysMtceStatusCloneRcvyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMtceStatusCloneRcvyThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cadSysMtceStatusCloneRcvyThreshold.setUnits("milliseconds")


class _CadSysMtceBasePingRate_Type(Unsigned32):
    """Custom type cadSysMtceBasePingRate based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(750, 2250),
    )


_CadSysMtceBasePingRate_Type.__name__ = "Unsigned32"
_CadSysMtceBasePingRate_Object = MibScalar
cadSysMtceBasePingRate = _CadSysMtceBasePingRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 19, 11),
    _CadSysMtceBasePingRate_Type()
)
cadSysMtceBasePingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMtceBasePingRate.setStatus("current")
if mibBuilder.loadTexts:
    cadSysMtceBasePingRate.setUnits("milliseconds")


class _CadSysMtceOvSensitivity_Type(OverloadThreshold):
    """Custom type cadSysMtceOvSensitivity based on OverloadThreshold"""


_CadSysMtceOvSensitivity_Object = MibScalar
cadSysMtceOvSensitivity = _CadSysMtceOvSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 19, 12),
    _CadSysMtceOvSensitivity_Type()
)
cadSysMtceOvSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMtceOvSensitivity.setStatus("current")


class _CadSysMtceOvThreshold_Type(OverloadThreshold):
    """Custom type cadSysMtceOvThreshold based on OverloadThreshold"""


_CadSysMtceOvThreshold_Object = MibScalar
cadSysMtceOvThreshold = _CadSysMtceOvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 19, 13),
    _CadSysMtceOvThreshold_Type()
)
cadSysMtceOvThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMtceOvThreshold.setStatus("current")


class _CadSysMtceDULPacketInterval_Type(Unsigned32):
    """Custom type cadSysMtceDULPacketInterval based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10000, 900000),
    )


_CadSysMtceDULPacketInterval_Type.__name__ = "Unsigned32"
_CadSysMtceDULPacketInterval_Object = MibScalar
cadSysMtceDULPacketInterval = _CadSysMtceDULPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 19, 14),
    _CadSysMtceDULPacketInterval_Type()
)
cadSysMtceDULPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysMtceDULPacketInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadSysMtceDULPacketInterval.setUnits("milliseconds")
_CadSysDataServer_ObjectIdentity = ObjectIdentity
cadSysDataServer = _CadSysDataServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 21)
)


class _CadSysDataServerDataTimeout_Type(Unsigned32):
    """Custom type cadSysDataServerDataTimeout based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50000, 500000),
    )


_CadSysDataServerDataTimeout_Type.__name__ = "Unsigned32"
_CadSysDataServerDataTimeout_Object = MibScalar
cadSysDataServerDataTimeout = _CadSysDataServerDataTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 21, 1),
    _CadSysDataServerDataTimeout_Type()
)
cadSysDataServerDataTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysDataServerDataTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysDataServerDataTimeout.setUnits("milliseconds")


class _CadSysDataServerDataEventsPerCycle_Type(Unsigned32):
    """Custom type cadSysDataServerDataEventsPerCycle based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_CadSysDataServerDataEventsPerCycle_Type.__name__ = "Unsigned32"
_CadSysDataServerDataEventsPerCycle_Object = MibScalar
cadSysDataServerDataEventsPerCycle = _CadSysDataServerDataEventsPerCycle_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 21, 2),
    _CadSysDataServerDataEventsPerCycle_Type()
)
cadSysDataServerDataEventsPerCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysDataServerDataEventsPerCycle.setStatus("current")
if mibBuilder.loadTexts:
    cadSysDataServerDataEventsPerCycle.setUnits("events/cycle")


class _CadSysDataServerDataSyncTimeout_Type(Unsigned32):
    """Custom type cadSysDataServerDataSyncTimeout based on Unsigned32"""
    defaultValue = 80000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 100000),
    )


_CadSysDataServerDataSyncTimeout_Type.__name__ = "Unsigned32"
_CadSysDataServerDataSyncTimeout_Object = MibScalar
cadSysDataServerDataSyncTimeout = _CadSysDataServerDataSyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 21, 3),
    _CadSysDataServerDataSyncTimeout_Type()
)
cadSysDataServerDataSyncTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysDataServerDataSyncTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cadSysDataServerDataSyncTimeout.setUnits("milliseconds")


class _CadSysDataServerSnmpReadAheadEnable_Type(TruthValue):
    """Custom type cadSysDataServerSnmpReadAheadEnable based on TruthValue"""


_CadSysDataServerSnmpReadAheadEnable_Object = MibScalar
cadSysDataServerSnmpReadAheadEnable = _CadSysDataServerSnmpReadAheadEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 21, 4),
    _CadSysDataServerSnmpReadAheadEnable_Type()
)
cadSysDataServerSnmpReadAheadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysDataServerSnmpReadAheadEnable.setStatus("current")


class _CadSysDataServerSnmpReadAheadMax_Type(Unsigned32):
    """Custom type cadSysDataServerSnmpReadAheadMax based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CadSysDataServerSnmpReadAheadMax_Type.__name__ = "Unsigned32"
_CadSysDataServerSnmpReadAheadMax_Object = MibScalar
cadSysDataServerSnmpReadAheadMax = _CadSysDataServerSnmpReadAheadMax_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 21, 5),
    _CadSysDataServerSnmpReadAheadMax_Type()
)
cadSysDataServerSnmpReadAheadMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysDataServerSnmpReadAheadMax.setStatus("current")


class _CadSysDataServerSnmpRefreshTime_Type(Unsigned32):
    """Custom type cadSysDataServerSnmpRefreshTime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_CadSysDataServerSnmpRefreshTime_Type.__name__ = "Unsigned32"
_CadSysDataServerSnmpRefreshTime_Object = MibScalar
cadSysDataServerSnmpRefreshTime = _CadSysDataServerSnmpRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 21, 6),
    _CadSysDataServerSnmpRefreshTime_Type()
)
cadSysDataServerSnmpRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysDataServerSnmpRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    cadSysDataServerSnmpRefreshTime.setUnits("seconds")


class _CadSysDataServerSyncDataEventsPerCycle_Type(Unsigned32):
    """Custom type cadSysDataServerSyncDataEventsPerCycle based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_CadSysDataServerSyncDataEventsPerCycle_Type.__name__ = "Unsigned32"
_CadSysDataServerSyncDataEventsPerCycle_Object = MibScalar
cadSysDataServerSyncDataEventsPerCycle = _CadSysDataServerSyncDataEventsPerCycle_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 21, 7),
    _CadSysDataServerSyncDataEventsPerCycle_Type()
)
cadSysDataServerSyncDataEventsPerCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysDataServerSyncDataEventsPerCycle.setStatus("current")
if mibBuilder.loadTexts:
    cadSysDataServerSyncDataEventsPerCycle.setUnits("events/cycle")


class _CadSysDataServerLoPriDataEventsPerCycle_Type(Unsigned32):
    """Custom type cadSysDataServerLoPriDataEventsPerCycle based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_CadSysDataServerLoPriDataEventsPerCycle_Type.__name__ = "Unsigned32"
_CadSysDataServerLoPriDataEventsPerCycle_Object = MibScalar
cadSysDataServerLoPriDataEventsPerCycle = _CadSysDataServerLoPriDataEventsPerCycle_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 21, 8),
    _CadSysDataServerLoPriDataEventsPerCycle_Type()
)
cadSysDataServerLoPriDataEventsPerCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysDataServerLoPriDataEventsPerCycle.setStatus("current")
if mibBuilder.loadTexts:
    cadSysDataServerLoPriDataEventsPerCycle.setUnits("events/cycle")
_CadSysSourceAddress_ObjectIdentity = ObjectIdentity
cadSysSourceAddress = _CadSysSourceAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 22)
)
_CadSysSourceAddressTable_Object = MibTable
cadSysSourceAddressTable = _CadSysSourceAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 22, 1)
)
if mibBuilder.loadTexts:
    cadSysSourceAddressTable.setStatus("current")
_CadSysSourceAddressEntry_Object = MibTableRow
cadSysSourceAddressEntry = _CadSysSourceAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 22, 1, 1)
)
cadSysSourceAddressEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysSourceAddressIndex"),
)
if mibBuilder.loadTexts:
    cadSysSourceAddressEntry.setStatus("current")
_CadSysSourceAddressIndex_Type = AdminSrcAddrType
_CadSysSourceAddressIndex_Object = MibTableColumn
cadSysSourceAddressIndex = _CadSysSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 22, 1, 1, 1),
    _CadSysSourceAddressIndex_Type()
)
cadSysSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysSourceAddressIndex.setStatus("current")


class _CadSysSourceInterfaceIpv4IfIndex_Type(InterfaceIndexOrZero):
    """Custom type cadSysSourceInterfaceIpv4IfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadSysSourceInterfaceIpv4IfIndex_Object = MibTableColumn
cadSysSourceInterfaceIpv4IfIndex = _CadSysSourceInterfaceIpv4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 22, 1, 1, 2),
    _CadSysSourceInterfaceIpv4IfIndex_Type()
)
cadSysSourceInterfaceIpv4IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysSourceInterfaceIpv4IfIndex.setStatus("current")
_CadSysSourceAddressIpv4Address_Type = InetAddressIPv4
_CadSysSourceAddressIpv4Address_Object = MibTableColumn
cadSysSourceAddressIpv4Address = _CadSysSourceAddressIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 22, 1, 1, 3),
    _CadSysSourceAddressIpv4Address_Type()
)
cadSysSourceAddressIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysSourceAddressIpv4Address.setStatus("current")


class _CadSysSourceInterfaceIpv6IfIndex_Type(InterfaceIndexOrZero):
    """Custom type cadSysSourceInterfaceIpv6IfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadSysSourceInterfaceIpv6IfIndex_Object = MibTableColumn
cadSysSourceInterfaceIpv6IfIndex = _CadSysSourceInterfaceIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 22, 1, 1, 4),
    _CadSysSourceInterfaceIpv6IfIndex_Type()
)
cadSysSourceInterfaceIpv6IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysSourceInterfaceIpv6IfIndex.setStatus("current")
_CadSysSourceAddressIpv6Address_Type = InetAddressIPv6
_CadSysSourceAddressIpv6Address_Object = MibTableColumn
cadSysSourceAddressIpv6Address = _CadSysSourceAddressIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 22, 1, 1, 5),
    _CadSysSourceAddressIpv6Address_Type()
)
cadSysSourceAddressIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysSourceAddressIpv6Address.setStatus("current")
_CadSysLicenseControl_ObjectIdentity = ObjectIdentity
cadSysLicenseControl = _CadSysLicenseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 23)
)


class _CadSysLicenseCardId_Type(CardId):
    """Custom type cadSysLicenseCardId based on CardId"""
    defaultValue = 0


_CadSysLicenseCardId_Object = MibScalar
cadSysLicenseCardId = _CadSysLicenseCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 23, 1),
    _CadSysLicenseCardId_Type()
)
cadSysLicenseCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysLicenseCardId.setStatus("current")


class _CadSysLicenseKey_Type(OctetString):
    """Custom type cadSysLicenseKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CadSysLicenseKey_Type.__name__ = "OctetString"
_CadSysLicenseKey_Object = MibScalar
cadSysLicenseKey = _CadSysLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 23, 2),
    _CadSysLicenseKey_Type()
)
cadSysLicenseKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysLicenseKey.setStatus("current")


class _CadSysLicensePorts_Type(Integer32):
    """Custom type cadSysLicensePorts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CadSysLicensePorts_Type.__name__ = "Integer32"
_CadSysLicensePorts_Object = MibScalar
cadSysLicensePorts = _CadSysLicensePorts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 23, 3),
    _CadSysLicensePorts_Type()
)
cadSysLicensePorts.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysLicensePorts.setStatus("current")


class _CadSysLicenseAnnex_Type(Integer32):
    """Custom type cadSysLicenseAnnex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 3),
          ("annexB", 4),
          ("annexC", 5),
          ("other", 2),
          ("unknown", 1))
    )


_CadSysLicenseAnnex_Type.__name__ = "Integer32"
_CadSysLicenseAnnex_Object = MibScalar
cadSysLicenseAnnex = _CadSysLicenseAnnex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 23, 4),
    _CadSysLicenseAnnex_Type()
)
cadSysLicenseAnnex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysLicenseAnnex.setStatus("current")


class _CadSysLicenseStatus_Type(Integer32):
    """Custom type cadSysLicenseStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("none", 4),
          ("pending", 3),
          ("success", 1))
    )


_CadSysLicenseStatus_Type.__name__ = "Integer32"
_CadSysLicenseStatus_Object = MibScalar
cadSysLicenseStatus = _CadSysLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 23, 5),
    _CadSysLicenseStatus_Type()
)
cadSysLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSysLicenseStatus.setStatus("current")
_CadLaesMdTimestampMode_ObjectIdentity = ObjectIdentity
cadLaesMdTimestampMode = _CadLaesMdTimestampMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 24)
)
_CadLaesMdTimestampModeTable_Object = MibTable
cadLaesMdTimestampModeTable = _CadLaesMdTimestampModeTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 24, 1)
)
if mibBuilder.loadTexts:
    cadLaesMdTimestampModeTable.setStatus("current")
_CadLaesMdTimestampModeEntry_Object = MibTableRow
cadLaesMdTimestampModeEntry = _CadLaesMdTimestampModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 24, 1, 1)
)
cadLaesMdTimestampModeEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadLaesMdTimestampModeInetAddrType"),
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadLaesMdTimestampModeInetAddr"),
)
if mibBuilder.loadTexts:
    cadLaesMdTimestampModeEntry.setStatus("current")
_CadLaesMdTimestampModeInetAddrType_Type = InetAddressType
_CadLaesMdTimestampModeInetAddrType_Object = MibTableColumn
cadLaesMdTimestampModeInetAddrType = _CadLaesMdTimestampModeInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 24, 1, 1, 1),
    _CadLaesMdTimestampModeInetAddrType_Type()
)
cadLaesMdTimestampModeInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadLaesMdTimestampModeInetAddrType.setStatus("current")
_CadLaesMdTimestampModeInetAddr_Type = InetAddress
_CadLaesMdTimestampModeInetAddr_Object = MibTableColumn
cadLaesMdTimestampModeInetAddr = _CadLaesMdTimestampModeInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 24, 1, 1, 2),
    _CadLaesMdTimestampModeInetAddr_Type()
)
cadLaesMdTimestampModeInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadLaesMdTimestampModeInetAddr.setStatus("current")
_CadLaesMdTimestampModRowStatus_Type = RowStatus
_CadLaesMdTimestampModRowStatus_Object = MibTableColumn
cadLaesMdTimestampModRowStatus = _CadLaesMdTimestampModRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 24, 1, 1, 3),
    _CadLaesMdTimestampModRowStatus_Type()
)
cadLaesMdTimestampModRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadLaesMdTimestampModRowStatus.setStatus("current")
_CadSysSharedSecret_ObjectIdentity = ObjectIdentity
cadSysSharedSecret = _CadSysSharedSecret_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 25)
)
_CadSysMICSecondarySecretTable_Object = MibTable
cadSysMICSecondarySecretTable = _CadSysMICSecondarySecretTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 25, 1)
)
if mibBuilder.loadTexts:
    cadSysMICSecondarySecretTable.setStatus("current")
_CadSysMICSecondarySecretEntry_Object = MibTableRow
cadSysMICSecondarySecretEntry = _CadSysMICSecondarySecretEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 25, 1, 1)
)
cadSysMICSecondarySecretEntry.setIndexNames(
    (0, "CADANT-CMTS-SYSTEM-MIB", "cadSysMICSecondarySecretIndex"),
)
if mibBuilder.loadTexts:
    cadSysMICSecondarySecretEntry.setStatus("current")


class _CadSysMICSecondarySecretIndex_Type(Integer32):
    """Custom type cadSysMICSecondarySecretIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CadSysMICSecondarySecretIndex_Type.__name__ = "Integer32"
_CadSysMICSecondarySecretIndex_Object = MibTableColumn
cadSysMICSecondarySecretIndex = _CadSysMICSecondarySecretIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 25, 1, 1, 1),
    _CadSysMICSecondarySecretIndex_Type()
)
cadSysMICSecondarySecretIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSysMICSecondarySecretIndex.setStatus("current")


class _CadSysMICSecondarySecretString_Type(OctetString):
    """Custom type cadSysMICSecondarySecretString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadSysMICSecondarySecretString_Type.__name__ = "OctetString"
_CadSysMICSecondarySecretString_Object = MibTableColumn
cadSysMICSecondarySecretString = _CadSysMICSecondarySecretString_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 25, 1, 1, 2),
    _CadSysMICSecondarySecretString_Type()
)
cadSysMICSecondarySecretString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysMICSecondarySecretString.setStatus("current")
_CadSysMICSecondarySecretStatus_Type = RowStatus
_CadSysMICSecondarySecretStatus_Object = MibTableColumn
cadSysMICSecondarySecretStatus = _CadSysMICSecondarySecretStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 25, 1, 1, 3),
    _CadSysMICSecondarySecretStatus_Type()
)
cadSysMICSecondarySecretStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSysMICSecondarySecretStatus.setStatus("current")

# Managed Objects groups

cadSysParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2, 1)
)
cadSysParamsGroup.setObjects(
      *(("CADANT-CMTS-SYSTEM-MIB", "cadSysSyncInterval"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysUCDInterval"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysMaxMAPPending"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysRangingInterval"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysInvitedRangingRetries"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysRegistrationRequestRetries"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysCMMAPProcessingTime"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysCMConfiguration"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysT5Timeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysT6Timeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysMiniSlotSize"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysDSxRequestRetries"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysT7Timeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysT8Timeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysT9Timeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysT10Timeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysT11Timeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysT13Timeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysDCCREQRetries"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysMICEnable"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysMICAuthString"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysAutoRecoveryEnable"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysActiveIpAddress"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysSpOperMode"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysMaxQoSActiveTimeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysMaxQoSAdmittedTimeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysAllow10CmConcatenation"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysAllow10CmFragmentation"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysPercentAddtlDsBwAllocated"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysMaxTrafBurstFor11CMs"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysRemoteFSEnable"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysRemotePortEnable"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysTcpSmoothingValue1D8U"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysTcpSmoothingValue2D12U"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysModemLossThreshold"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysPeakTrafRateFor11CMs"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysCpeHostAuthorization"))
)
if mibBuilder.loadTexts:
    cadSysParamsGroup.setStatus("current")

cadSysSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2, 2)
)
cadSysSystemGroup.setObjects(
      *(("CADANT-CMTS-SYSTEM-MIB", "cadSysContact"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysName"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysLocation"))
)
if mibBuilder.loadTexts:
    cadSysSystemGroup.setStatus("current")

cadSysControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2, 3)
)
cadSysControlGroup.setObjects(
      *(("CADANT-CMTS-SYSTEM-MIB", "cadSysWriteMem"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysEraseMem"))
)
if mibBuilder.loadTexts:
    cadSysControlGroup.setStatus("deprecated")

cadSysSnmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2, 4)
)
cadSysSnmpGroup.setObjects(
      *(("CADANT-CMTS-SYSTEM-MIB", "cadSysEnableAuthenTraps"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysSnmpReadAheadMax"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysSnmpRefreshTime"))
)
if mibBuilder.loadTexts:
    cadSysSnmpGroup.setStatus("current")

cadSysBootParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2, 5)
)
cadSysBootParamsGroup.setObjects(
      *(("CADANT-CMTS-SYSTEM-MIB", "cadSysBootMacAddress"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysBootFpIpAddress"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysBootFpSubnetMask"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysBootDefaultGateway"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysBootTimeOffset"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysBootTimeServer"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysBootTimeServerConnType"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysBootStartupApplication"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysBootStartupDelay"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysBootSelection"))
)
if mibBuilder.loadTexts:
    cadSysBootParamsGroup.setStatus("current")

cadSysReloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2, 6)
)
cadSysReloadGroup.setObjects(
      *(("CADANT-CMTS-SYSTEM-MIB", "cadSysReloadImageName"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysReloadOperation"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysReloadStatus"))
)
if mibBuilder.loadTexts:
    cadSysReloadGroup.setStatus("current")

cadSysImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2, 7)
)
cadSysImageGroup.setObjects(
      *(("CADANT-CMTS-SYSTEM-MIB", "cadSysImageFile"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysImageId"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysImageName"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysImageComponentCount"))
)
if mibBuilder.loadTexts:
    cadSysImageGroup.setStatus("current")

cadSysConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2, 8)
)
cadSysConfigurationGroup.setObjects(
    ("CADANT-CMTS-SYSTEM-MIB", "cadSysConfigSaveTime")
)
if mibBuilder.loadTexts:
    cadSysConfigurationGroup.setStatus("current")

cadSysDataServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2, 9)
)
cadSysDataServerGroup.setObjects(
      *(("CADANT-CMTS-SYSTEM-MIB", "cadSysDataServerDataTimeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysDataServerDataEventsPerCycle"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysDataServerDataSyncTimeout"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysDataServerSnmpReadAheadEnable"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysDataServerSnmpReadAheadMax"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysDataServerSnmpRefreshTime"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysDataServerSyncDataEventsPerCycle"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysDataServerLoPriDataEventsPerCycle"))
)
if mibBuilder.loadTexts:
    cadSysDataServerGroup.setStatus("current")

cadSysSourceAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 2, 10)
)
cadSysSourceAddressGroup.setObjects(
      *(("CADANT-CMTS-SYSTEM-MIB", "cadSysSourceInterfaceIpv4IfIndex"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysSourceAddressIpv4Address"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysSourceInterfaceIpv6IfIndex"),
        ("CADANT-CMTS-SYSTEM-MIB", "cadSysSourceAddressIpv6Address"))
)
if mibBuilder.loadTexts:
    cadSysSourceAddressGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cadSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    cadSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-SYSTEM-MIB",
    **{"cadSystemMib": cadSystemMib,
       "cadSysParams": cadSysParams,
       "cadSysSyncInterval": cadSysSyncInterval,
       "cadSysUCDInterval": cadSysUCDInterval,
       "cadSysMaxMAPPending": cadSysMaxMAPPending,
       "cadSysRangingInterval": cadSysRangingInterval,
       "cadSysInvitedRangingRetries": cadSysInvitedRangingRetries,
       "cadSysRegistrationRequestRetries": cadSysRegistrationRequestRetries,
       "cadSysCMMAPProcessingTime": cadSysCMMAPProcessingTime,
       "cadSysCMRangingResponseProcessingTime": cadSysCMRangingResponseProcessingTime,
       "cadSysCMConfiguration": cadSysCMConfiguration,
       "cadSysT5Timeout": cadSysT5Timeout,
       "cadSysT6Timeout": cadSysT6Timeout,
       "cadSysMiniSlotSize": cadSysMiniSlotSize,
       "cadSysDSxRequestRetries": cadSysDSxRequestRetries,
       "cadSysDSxResponseRetries": cadSysDSxResponseRetries,
       "cadSysT7Timeout": cadSysT7Timeout,
       "cadSysT8Timeout": cadSysT8Timeout,
       "cadSysT9Timeout": cadSysT9Timeout,
       "cadSysT10Timeout": cadSysT10Timeout,
       "cadSysT11Timeout": cadSysT11Timeout,
       "cadSysT13Timeout": cadSysT13Timeout,
       "cadSysDCCREQRetries": cadSysDCCREQRetries,
       "cadSysMICEnable": cadSysMICEnable,
       "cadSysMICAuthString": cadSysMICAuthString,
       "cadSysAutoRecoveryEnable": cadSysAutoRecoveryEnable,
       "cadSysActiveIpAddress": cadSysActiveIpAddress,
       "cadSysSpOperMode": cadSysSpOperMode,
       "cadSysCountsCollectionRate": cadSysCountsCollectionRate,
       "cadSysMaxQoSActiveTimeout": cadSysMaxQoSActiveTimeout,
       "cadSysMaxQoSAdmittedTimeout": cadSysMaxQoSAdmittedTimeout,
       "cadSysAllow10CmConcatenation": cadSysAllow10CmConcatenation,
       "cadSysAllow10CmFragmentation": cadSysAllow10CmFragmentation,
       "cadSysPercentAddtlDsBwAllocated": cadSysPercentAddtlDsBwAllocated,
       "cadSysMaxTrafBurstFor11CMs": cadSysMaxTrafBurstFor11CMs,
       "cadSysFanSpeedControlEnable": cadSysFanSpeedControlEnable,
       "cadSysFlaplistPowerAdjustThreshold": cadSysFlaplistPowerAdjustThreshold,
       "cadSysRemoteFSEnable": cadSysRemoteFSEnable,
       "cadSysRemotePortEnable": cadSysRemotePortEnable,
       "cadSysTcpSmoothingValue1D8U": cadSysTcpSmoothingValue1D8U,
       "cadSysTcpSmoothingValue2D12U": cadSysTcpSmoothingValue2D12U,
       "cadSysModemLossThreshold": cadSysModemLossThreshold,
       "cadSysPeakTrafRateFor11CMs": cadSysPeakTrafRateFor11CMs,
       "cadSysCpeHostAuthorization": cadSysCpeHostAuthorization,
       "cadSysMaxUcdBurstLength": cadSysMaxUcdBurstLength,
       "cadSysLO1LeakDetect": cadSysLO1LeakDetect,
       "cadMtcmConditionalOverride": cadMtcmConditionalOverride,
       "cadSysDelayedCpeLearning": cadSysDelayedCpeLearning,
       "cadSysModPriDsInRccEnabled": cadSysModPriDsInRccEnabled,
       "cadSysSendTccRefIdPerFragment": cadSysSendTccRefIdPerFragment,
       "cadSysPeakTrRateUpstream": cadSysPeakTrRateUpstream,
       "cadSysAllowAmbiguityOverride": cadSysAllowAmbiguityOverride,
       "cadSysUnicastNpUsAcquisition": cadSysUnicastNpUsAcquisition,
       "cadSysMacMoveBlockedOnRcptDhcpPkt": cadSysMacMoveBlockedOnRcptDhcpPkt,
       "cadSysTftpProxy": cadSysTftpProxy,
       "cadSysFanSpeedLevel": cadSysFanSpeedLevel,
       "cadSys1x1onCmAcPwrLossEnabled": cadSys1x1onCmAcPwrLossEnabled,
       "cadSysFlapListInsertionThreshold": cadSysFlapListInsertionThreshold,
       "cadSysAES128Enable": cadSysAES128Enable,
       "cadSysSystem": cadSysSystem,
       "cadSysContact": cadSysContact,
       "cadSysName": cadSysName,
       "cadSysLocation": cadSysLocation,
       "cadSysControl": cadSysControl,
       "cadSysWriteMem": cadSysWriteMem,
       "cadSysEraseMem": cadSysEraseMem,
       "cadSysSnmp": cadSysSnmp,
       "cadSysEnableAuthenTraps": cadSysEnableAuthenTraps,
       "cadSysSnmpReadAheadMax": cadSysSnmpReadAheadMax,
       "cadSysSnmpRefreshTime": cadSysSnmpRefreshTime,
       "cadSnmpRemoteEngineTable": cadSnmpRemoteEngineTable,
       "cadSnmpRemoteEngineEntry": cadSnmpRemoteEngineEntry,
       "cadSnmpRemoteEngineIpAddress": cadSnmpRemoteEngineIpAddress,
       "cadSnmpRemoteEnginePortNumber": cadSnmpRemoteEnginePortNumber,
       "cadSnmpRemoteEngineID": cadSnmpRemoteEngineID,
       "cadSnmpRemoteUserName": cadSnmpRemoteUserName,
       "cadSnmpRemoteEngineType": cadSnmpRemoteEngineType,
       "cadSnmpRemoteEngineStatus": cadSnmpRemoteEngineStatus,
       "cadSysBootParams": cadSysBootParams,
       "cadSysBootMacAddress": cadSysBootMacAddress,
       "cadSysBootFpIpAddress": cadSysBootFpIpAddress,
       "cadSysBootFpSubnetMask": cadSysBootFpSubnetMask,
       "cadSysBootDefaultGateway": cadSysBootDefaultGateway,
       "cadSysBootTimeOffset": cadSysBootTimeOffset,
       "cadSysBootTimeServer": cadSysBootTimeServer,
       "cadSysBootTimeServerConnType": cadSysBootTimeServerConnType,
       "cadSysBootStartupApplication": cadSysBootStartupApplication,
       "cadSysBootStartupDelay": cadSysBootStartupDelay,
       "cadSysBootSelection": cadSysBootSelection,
       "cadSysBootBaud": cadSysBootBaud,
       "cadSysBootFpBIpAddress": cadSysBootFpBIpAddress,
       "cadSysBootParity": cadSysBootParity,
       "cadSysReload": cadSysReload,
       "cadSysReloadOperation": cadSysReloadOperation,
       "cadSysReloadImageName": cadSysReloadImageName,
       "cadSysReloadStatus": cadSysReloadStatus,
       "cadSysReloadStatusDescription": cadSysReloadStatusDescription,
       "cadSysReloadPatchName": cadSysReloadPatchName,
       "cadSysImage": cadSysImage,
       "cadSysImageFile": cadSysImageFile,
       "cadSysImageId": cadSysImageId,
       "cadSysImageName": cadSysImageName,
       "cadSysImageComponentCount": cadSysImageComponentCount,
       "cadSysDictionary": cadSysDictionary,
       "cadSysDictionaryTable": cadSysDictionaryTable,
       "cadSysDictionaryEntry": cadSysDictionaryEntry,
       "cadSysDictionaryTableId": cadSysDictionaryTableId,
       "cadSysDictionaryName": cadSysDictionaryName,
       "cadSysDictionaryDynamic": cadSysDictionaryDynamic,
       "cadSysDictionaryNumberEntries": cadSysDictionaryNumberEntries,
       "cadSysDictionaryCurrentVer": cadSysDictionaryCurrentVer,
       "cadSysDictionaryPersistentVer": cadSysDictionaryPersistentVer,
       "cadSysDictionaryModuleVer": cadSysDictionaryModuleVer,
       "cadSysConfiguration": cadSysConfiguration,
       "cadSysConfigSaveTime": cadSysConfigSaveTime,
       "cadCosToQosMapping": cadCosToQosMapping,
       "cadCosToQosMappingTable": cadCosToQosMappingTable,
       "cadCosToQosMappingEntry": cadCosToQosMappingEntry,
       "cadCosToQosMappingIndex": cadCosToQosMappingIndex,
       "cadCosUpMaxTrafficBurst": cadCosUpMaxTrafficBurst,
       "cadCosDnMaxTrafficBurst": cadCosDnMaxTrafficBurst,
       "cadCosDnMinReservedRate": cadCosDnMinReservedRate,
       "cadCosUpMinReservedPkt": cadCosUpMinReservedPkt,
       "cadCosDnMinReservedPkt": cadCosDnMinReservedPkt,
       "cadCosUpTosAndMask": cadCosUpTosAndMask,
       "cadCosUpTosOrMask": cadCosUpTosOrMask,
       "cadCosDnMaxLatency": cadCosDnMaxLatency,
       "cadCosDnPriority": cadCosDnPriority,
       "cadCosDnPeakTrafficRate": cadCosDnPeakTrafficRate,
       "cadCosUpPeakTrafficRate": cadCosUpPeakTrafficRate,
       "cadSysKeyChain": cadSysKeyChain,
       "cadSysKeyChainKeyTable": cadSysKeyChainKeyTable,
       "cadSysKeyChainKeyEntry": cadSysKeyChainKeyEntry,
       "cadSysKeyChainName": cadSysKeyChainName,
       "cadSysKeyChainKeySequenceId": cadSysKeyChainKeySequenceId,
       "cadSysKeyChainKey": cadSysKeyChainKey,
       "cadSysKeyChainKeyAcceptStartTime": cadSysKeyChainKeyAcceptStartTime,
       "cadSysKeyChainKeyAcceptStopTime": cadSysKeyChainKeyAcceptStopTime,
       "cadSysKeyChainKeyAcceptInfiniteLifetime": cadSysKeyChainKeyAcceptInfiniteLifetime,
       "cadSysKeyChainKeySendStartTime": cadSysKeyChainKeySendStartTime,
       "cadSysKeyChainKeySendStopTime": cadSysKeyChainKeySendStopTime,
       "cadSysKeyChainKeySendInfiniteLifetime": cadSysKeyChainKeySendInfiniteLifetime,
       "cadSysKeyChainKeyRowStatus": cadSysKeyChainKeyRowStatus,
       "cadSystemMibConformance": cadSystemMibConformance,
       "cadSystemCompliances": cadSystemCompliances,
       "cadSystemCompliance": cadSystemCompliance,
       "cadSystemGroups": cadSystemGroups,
       "cadSysParamsGroup": cadSysParamsGroup,
       "cadSysSystemGroup": cadSysSystemGroup,
       "cadSysControlGroup": cadSysControlGroup,
       "cadSysSnmpGroup": cadSysSnmpGroup,
       "cadSysBootParamsGroup": cadSysBootParamsGroup,
       "cadSysReloadGroup": cadSysReloadGroup,
       "cadSysImageGroup": cadSysImageGroup,
       "cadSysConfigurationGroup": cadSysConfigurationGroup,
       "cadSysDataServerGroup": cadSysDataServerGroup,
       "cadSysSourceAddressGroup": cadSysSourceAddressGroup,
       "cadSysProcPolicingConfig": cadSysProcPolicingConfig,
       "cadSysProcRouterControlGlobalPacketRate": cadSysProcRouterControlGlobalPacketRate,
       "cadSysProcArpPacketRate": cadSysProcArpPacketRate,
       "cadSysProcDhcpPacketRate": cadSysProcDhcpPacketRate,
       "cadSysProcIcmpPacketRate": cadSysProcIcmpPacketRate,
       "cadSysProcOspfPacketRate": cadSysProcOspfPacketRate,
       "cadSysProcRipPacketRate": cadSysProcRipPacketRate,
       "cadSysProcIgmpPacketRate": cadSysProcIgmpPacketRate,
       "cadSysProcRouterControlOtherPacketRate": cadSysProcRouterControlOtherPacketRate,
       "cadSysProcSnmpPacketRate": cadSysProcSnmpPacketRate,
       "cadSysProcTftpPacketRate": cadSysProcTftpPacketRate,
       "cadSysProcIsisPacketRate": cadSysProcIsisPacketRate,
       "cadSysProcNdPacketRate": cadSysProcNdPacketRate,
       "cadSysProcDhcpIpv6PacketRate": cadSysProcDhcpIpv6PacketRate,
       "cadSysProcIcmpIpv6PacketRate": cadSysProcIcmpIpv6PacketRate,
       "cadSysProcMldPacketRate": cadSysProcMldPacketRate,
       "cadSysProcBgpPacketRate": cadSysProcBgpPacketRate,
       "cadSysProcPimPacketRate": cadSysProcPimPacketRate,
       "cadSysProcSnmpCmPacketRate": cadSysProcSnmpCmPacketRate,
       "cadSysProcCopsPacketRate": cadSysProcCopsPacketRate,
       "cadSysProcTelnetPacketRate": cadSysProcTelnetPacketRate,
       "cadSysProcOspfv3PacketRate": cadSysProcOspfv3PacketRate,
       "cadSysProcTftpIpv6PacketRate": cadSysProcTftpIpv6PacketRate,
       "cadSysProcEventIcmpPacketRate": cadSysProcEventIcmpPacketRate,
       "cadSysProcEventNoRoutePacketRate": cadSysProcEventNoRoutePacketRate,
       "cadSysProcEventIcmpIpv6PacketRate": cadSysProcEventIcmpIpv6PacketRate,
       "cadSysProcEventNoRouteIpv6PacketRate": cadSysProcEventNoRouteIpv6PacketRate,
       "cadSysProcEventArpPacketRate": cadSysProcEventArpPacketRate,
       "cadSysProcEventNdPacketRate": cadSysProcEventNdPacketRate,
       "cadSysProcEventTtlPacketRate": cadSysProcEventTtlPacketRate,
       "cadSysProcEventTtlIpv6PacketRate": cadSysProcEventTtlIpv6PacketRate,
       "cadSysProcEventDadPacketRate": cadSysProcEventDadPacketRate,
       "cadSysProcEventDefaultPacketRate": cadSysProcEventDefaultPacketRate,
       "cadSysProcLdpPacketRate": cadSysProcLdpPacketRate,
       "cadSysProcClearPolicingCounts": cadSysProcClearPolicingCounts,
       "cadSysProcLacpPacketRate": cadSysProcLacpPacketRate,
       "cadSysProcVrepPacketRate": cadSysProcVrepPacketRate,
       "cadSysProcVpmePacketRate": cadSysProcVpmePacketRate,
       "cadSysProcErmRpcPacketRate": cadSysProcErmRpcPacketRate,
       "cadSysProcPolicingCounts": cadSysProcPolicingCounts,
       "cadSysProcRouterControlGlobalPacketsReceivedPassed": cadSysProcRouterControlGlobalPacketsReceivedPassed,
       "cadSysProcRouterControlGlobalPacketsReceivedDropped": cadSysProcRouterControlGlobalPacketsReceivedDropped,
       "cadSysProcArpPacketsReceivedPassed": cadSysProcArpPacketsReceivedPassed,
       "cadSysProcArpPacketsReceivedDropped": cadSysProcArpPacketsReceivedDropped,
       "cadSysProcDhcpPacketsReceivedPassed": cadSysProcDhcpPacketsReceivedPassed,
       "cadSysProcDhcpPacketsReceivedDropped": cadSysProcDhcpPacketsReceivedDropped,
       "cadSysProcIcmpPacketsReceivedPassed": cadSysProcIcmpPacketsReceivedPassed,
       "cadSysProcIcmpPacketsReceivedDropped": cadSysProcIcmpPacketsReceivedDropped,
       "cadSysProcOspfPacketsReceivedPassed": cadSysProcOspfPacketsReceivedPassed,
       "cadSysProcOspfPacketsReceivedDropped": cadSysProcOspfPacketsReceivedDropped,
       "cadSysProcRipPacketsReceivedPassed": cadSysProcRipPacketsReceivedPassed,
       "cadSysProcRipPacketsReceivedDropped": cadSysProcRipPacketsReceivedDropped,
       "cadSysProcIgmpPacketsReceivedPassed": cadSysProcIgmpPacketsReceivedPassed,
       "cadSysProcIgmpPacketsReceivedDropped": cadSysProcIgmpPacketsReceivedDropped,
       "cadSysProcRouterControlOtherPacketsReceivedPassed": cadSysProcRouterControlOtherPacketsReceivedPassed,
       "cadSysProcRouterControlOtherPacketsReceivedDropped": cadSysProcRouterControlOtherPacketsReceivedDropped,
       "cadSysProcSnmpPacketsReceivedPassed": cadSysProcSnmpPacketsReceivedPassed,
       "cadSysProcSnmpPacketsReceivedDropped": cadSysProcSnmpPacketsReceivedDropped,
       "cadSysProcTftpPacketsReceivedPassed": cadSysProcTftpPacketsReceivedPassed,
       "cadSysProcTftpPacketsReceivedDropped": cadSysProcTftpPacketsReceivedDropped,
       "cadSysProcIsisPacketsReceivedPassed": cadSysProcIsisPacketsReceivedPassed,
       "cadSysProcIsisPacketsReceivedDropped": cadSysProcIsisPacketsReceivedDropped,
       "cadSysProcNdPacketsReceivedPassed": cadSysProcNdPacketsReceivedPassed,
       "cadSysProcNdPacketsReceivedDropped": cadSysProcNdPacketsReceivedDropped,
       "cadSysProcDhcpIpv6PacketsReceivedPassed": cadSysProcDhcpIpv6PacketsReceivedPassed,
       "cadSysProcDhcpIpv6PacketsReceivedDropped": cadSysProcDhcpIpv6PacketsReceivedDropped,
       "cadSysProcIcmpIpv6PacketsReceivedPassed": cadSysProcIcmpIpv6PacketsReceivedPassed,
       "cadSysProcIcmpIpv6PacketsReceivedDropped": cadSysProcIcmpIpv6PacketsReceivedDropped,
       "cadSysProcMldPacketsReceivedPassed": cadSysProcMldPacketsReceivedPassed,
       "cadSysProcMldPacketsReceivedDropped": cadSysProcMldPacketsReceivedDropped,
       "cadSysProcBgpPacketsReceivedPassed": cadSysProcBgpPacketsReceivedPassed,
       "cadSysProcBgpPacketsReceivedDropped": cadSysProcBgpPacketsReceivedDropped,
       "cadSysProcPimPacketsReceivedPassed": cadSysProcPimPacketsReceivedPassed,
       "cadSysProcPimPacketsReceivedDropped": cadSysProcPimPacketsReceivedDropped,
       "cadSysProcSnmpCmPacketsReceivedPassed": cadSysProcSnmpCmPacketsReceivedPassed,
       "cadSysProcSnmpCmPacketsReceivedDropped": cadSysProcSnmpCmPacketsReceivedDropped,
       "cadSysProcCopsPacketsReceivedPassed": cadSysProcCopsPacketsReceivedPassed,
       "cadSysProcCopsPacketsReceivedDropped": cadSysProcCopsPacketsReceivedDropped,
       "cadSysProcTelnetPacketsReceivedPassed": cadSysProcTelnetPacketsReceivedPassed,
       "cadSysProcTelnetPacketsReceivedDropped": cadSysProcTelnetPacketsReceivedDropped,
       "cadSysProcOspfv3PacketsReceivedPassed": cadSysProcOspfv3PacketsReceivedPassed,
       "cadSysProcOspfv3PacketsReceivedDropped": cadSysProcOspfv3PacketsReceivedDropped,
       "cadSysProcTftpIpv6PacketsReceivedPassed": cadSysProcTftpIpv6PacketsReceivedPassed,
       "cadSysProcTftpIpv6PacketsReceivedDropped": cadSysProcTftpIpv6PacketsReceivedDropped,
       "cadSysProcLdpPacketsReceivedPassed": cadSysProcLdpPacketsReceivedPassed,
       "cadSysProcLdpPacketsReceivedDropped": cadSysProcLdpPacketsReceivedDropped,
       "cadSysProcEventIcmpPacketsReceivedPassed": cadSysProcEventIcmpPacketsReceivedPassed,
       "cadSysProcEventIcmpPacketsReceivedDropped": cadSysProcEventIcmpPacketsReceivedDropped,
       "cadSysProcEventNoRoutePacketsReceivedPassed": cadSysProcEventNoRoutePacketsReceivedPassed,
       "cadSysProcEventNoRoutePacketsReceivedDropped": cadSysProcEventNoRoutePacketsReceivedDropped,
       "cadSysProcEventIcmpIpv6PacketsReceivedPassed": cadSysProcEventIcmpIpv6PacketsReceivedPassed,
       "cadSysProcEventIcmpIpv6PacketsReceivedDropped": cadSysProcEventIcmpIpv6PacketsReceivedDropped,
       "cadSysProcEventNoRouteIpv6PacketsReceivedPassed": cadSysProcEventNoRouteIpv6PacketsReceivedPassed,
       "cadSysProcEventNoRouteIpv6PacketsReceivedDropped": cadSysProcEventNoRouteIpv6PacketsReceivedDropped,
       "cadSysProcEventArpPacketsReceivedPassed": cadSysProcEventArpPacketsReceivedPassed,
       "cadSysProcEventArpPacketsReceivedDropped": cadSysProcEventArpPacketsReceivedDropped,
       "cadSysProcEventNdPacketsReceivedPassed": cadSysProcEventNdPacketsReceivedPassed,
       "cadSysProcEventNdPacketsReceivedDropped": cadSysProcEventNdPacketsReceivedDropped,
       "cadSysProcEventTtlPacketsReceivedPassed": cadSysProcEventTtlPacketsReceivedPassed,
       "cadSysProcEventTtlPacketsReceivedDropped": cadSysProcEventTtlPacketsReceivedDropped,
       "cadSysProcEventTtlIpv6PacketsReceivedPassed": cadSysProcEventTtlIpv6PacketsReceivedPassed,
       "cadSysProcEventTtlIpv6PacketsReceivedDropped": cadSysProcEventTtlIpv6PacketsReceivedDropped,
       "cadSysProcEventDadPacketsReceivedPassed": cadSysProcEventDadPacketsReceivedPassed,
       "cadSysProcEventDadPacketsReceivedDropped": cadSysProcEventDadPacketsReceivedDropped,
       "cadSysProcEventDefaultPacketsReceivedPassed": cadSysProcEventDefaultPacketsReceivedPassed,
       "cadSysProcEventDefaultPacketsReceivedDropped": cadSysProcEventDefaultPacketsReceivedDropped,
       "cadSysProcLacpPacketsReceivedPassed": cadSysProcLacpPacketsReceivedPassed,
       "cadSysProcLacpPacketsReceivedDropped": cadSysProcLacpPacketsReceivedDropped,
       "cadSysProcVrepPacketsReceivedPassed": cadSysProcVrepPacketsReceivedPassed,
       "cadSysProcVrepPacketsReceivedDropped": cadSysProcVrepPacketsReceivedDropped,
       "cadSysProcVpmePacketsReceivedPassed": cadSysProcVpmePacketsReceivedPassed,
       "cadSysProcVpmePacketsReceivedDropped": cadSysProcVpmePacketsReceivedDropped,
       "cadSysProcErmRpcPacketsReceivedPassed": cadSysProcErmRpcPacketsReceivedPassed,
       "cadSysProcErmRpcPacketsReceivedDropped": cadSysProcErmRpcPacketsReceivedDropped,
       "cadSysBanner": cadSysBanner,
       "cadSysBannerMotdTable": cadSysBannerMotdTable,
       "cadSysBannerMotdEntry": cadSysBannerMotdEntry,
       "cadSysBannerMotdLine": cadSysBannerMotdLine,
       "cadSysBannerMotdText": cadSysBannerMotdText,
       "cadSysBannerMotdRowStatus": cadSysBannerMotdRowStatus,
       "cadSysBannerLoginTable": cadSysBannerLoginTable,
       "cadSysBannerLoginEntry": cadSysBannerLoginEntry,
       "cadSysBannerLoginLine": cadSysBannerLoginLine,
       "cadSysBannerLoginText": cadSysBannerLoginText,
       "cadSysBannerLoginRowStatus": cadSysBannerLoginRowStatus,
       "cadSysBannerExecTable": cadSysBannerExecTable,
       "cadSysBannerExecEntry": cadSysBannerExecEntry,
       "cadSysBannerExecLine": cadSysBannerExecLine,
       "cadSysBannerExecText": cadSysBannerExecText,
       "cadSysBannerExecRowStatus": cadSysBannerExecRowStatus,
       "cadSysBannerIncomingTable": cadSysBannerIncomingTable,
       "cadSysBannerIncomingEntry": cadSysBannerIncomingEntry,
       "cadSysBannerIncomingLine": cadSysBannerIncomingLine,
       "cadSysBannerIncomingText": cadSysBannerIncomingText,
       "cadSysBannerIncomingRowStatus": cadSysBannerIncomingRowStatus,
       "cadSysServer": cadSysServer,
       "cadSysServerTable": cadSysServerTable,
       "cadSysServerEntry": cadSysServerEntry,
       "cadSysServerType": cadSysServerType,
       "cadSysServerAdminState": cadSysServerAdminState,
       "cadSysPatchParams": cadSysPatchParams,
       "cadSysPatchParamTable": cadSysPatchParamTable,
       "cadSysPatchParamEntry": cadSysPatchParamEntry,
       "cadSysPatchParamIndex": cadSysPatchParamIndex,
       "cadSysPatchParamName": cadSysPatchParamName,
       "cadSysPatchParamValue": cadSysPatchParamValue,
       "cadSysPatchParamDescription": cadSysPatchParamDescription,
       "cadSysPatchParamRowStatus": cadSysPatchParamRowStatus,
       "cadSysMtceParams": cadSysMtceParams,
       "cadSysMtceStatusCloneMonitorThreshold": cadSysMtceStatusCloneMonitorThreshold,
       "cadSysMtceStatusCloneInitThreshold": cadSysMtceStatusCloneInitThreshold,
       "cadSysMtceStatusCloneRcvyThreshold": cadSysMtceStatusCloneRcvyThreshold,
       "cadSysMtceBasePingRate": cadSysMtceBasePingRate,
       "cadSysMtceOvSensitivity": cadSysMtceOvSensitivity,
       "cadSysMtceOvThreshold": cadSysMtceOvThreshold,
       "cadSysMtceDULPacketInterval": cadSysMtceDULPacketInterval,
       "cadSysDataServer": cadSysDataServer,
       "cadSysDataServerDataTimeout": cadSysDataServerDataTimeout,
       "cadSysDataServerDataEventsPerCycle": cadSysDataServerDataEventsPerCycle,
       "cadSysDataServerDataSyncTimeout": cadSysDataServerDataSyncTimeout,
       "cadSysDataServerSnmpReadAheadEnable": cadSysDataServerSnmpReadAheadEnable,
       "cadSysDataServerSnmpReadAheadMax": cadSysDataServerSnmpReadAheadMax,
       "cadSysDataServerSnmpRefreshTime": cadSysDataServerSnmpRefreshTime,
       "cadSysDataServerSyncDataEventsPerCycle": cadSysDataServerSyncDataEventsPerCycle,
       "cadSysDataServerLoPriDataEventsPerCycle": cadSysDataServerLoPriDataEventsPerCycle,
       "cadSysSourceAddress": cadSysSourceAddress,
       "cadSysSourceAddressTable": cadSysSourceAddressTable,
       "cadSysSourceAddressEntry": cadSysSourceAddressEntry,
       "cadSysSourceAddressIndex": cadSysSourceAddressIndex,
       "cadSysSourceInterfaceIpv4IfIndex": cadSysSourceInterfaceIpv4IfIndex,
       "cadSysSourceAddressIpv4Address": cadSysSourceAddressIpv4Address,
       "cadSysSourceInterfaceIpv6IfIndex": cadSysSourceInterfaceIpv6IfIndex,
       "cadSysSourceAddressIpv6Address": cadSysSourceAddressIpv6Address,
       "cadSysLicenseControl": cadSysLicenseControl,
       "cadSysLicenseCardId": cadSysLicenseCardId,
       "cadSysLicenseKey": cadSysLicenseKey,
       "cadSysLicensePorts": cadSysLicensePorts,
       "cadSysLicenseAnnex": cadSysLicenseAnnex,
       "cadSysLicenseStatus": cadSysLicenseStatus,
       "cadLaesMdTimestampMode": cadLaesMdTimestampMode,
       "cadLaesMdTimestampModeTable": cadLaesMdTimestampModeTable,
       "cadLaesMdTimestampModeEntry": cadLaesMdTimestampModeEntry,
       "cadLaesMdTimestampModeInetAddrType": cadLaesMdTimestampModeInetAddrType,
       "cadLaesMdTimestampModeInetAddr": cadLaesMdTimestampModeInetAddr,
       "cadLaesMdTimestampModRowStatus": cadLaesMdTimestampModRowStatus,
       "cadSysSharedSecret": cadSysSharedSecret,
       "cadSysMICSecondarySecretTable": cadSysMICSecondarySecretTable,
       "cadSysMICSecondarySecretEntry": cadSysMICSecondarySecretEntry,
       "cadSysMICSecondarySecretIndex": cadSysMICSecondarySecretIndex,
       "cadSysMICSecondarySecretString": cadSysMICSecondarySecretString,
       "cadSysMICSecondarySecretStatus": cadSysMICSecondarySecretStatus}
)
