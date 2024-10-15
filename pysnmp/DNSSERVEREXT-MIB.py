# SNMP MIB module (DNSSERVEREXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNSSERVEREXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:27 2024
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

(dnsServerExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "dnsServerExt")

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

apDnsServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApDnsServerEnable_Type(Integer32):
    """Custom type apDnsServerEnable based on Integer32"""
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


_ApDnsServerEnable_Type.__name__ = "Integer32"
_ApDnsServerEnable_Object = MibScalar
apDnsServerEnable = _ApDnsServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 2),
    _ApDnsServerEnable_Type()
)
apDnsServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnsServerEnable.setStatus("current")


class _ApDnsServerBufferCount_Type(Integer32):
    """Custom type apDnsServerBufferCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1000),
    )


_ApDnsServerBufferCount_Type.__name__ = "Integer32"
_ApDnsServerBufferCount_Object = MibScalar
apDnsServerBufferCount = _ApDnsServerBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 3),
    _ApDnsServerBufferCount_Type()
)
apDnsServerBufferCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnsServerBufferCount.setStatus("current")


class _ApDnsServerResponderTasks_Type(Integer32):
    """Custom type apDnsServerResponderTasks based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_ApDnsServerResponderTasks_Type.__name__ = "Integer32"
_ApDnsServerResponderTasks_Object = MibScalar
apDnsServerResponderTasks = _ApDnsServerResponderTasks_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 4),
    _ApDnsServerResponderTasks_Type()
)
apDnsServerResponderTasks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnsServerResponderTasks.setStatus("current")


class _ApDnsPeerRcvEntries_Type(Integer32):
    """Custom type apDnsPeerRcvEntries based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 1024),
    )


_ApDnsPeerRcvEntries_Type.__name__ = "Integer32"
_ApDnsPeerRcvEntries_Object = MibScalar
apDnsPeerRcvEntries = _ApDnsPeerRcvEntries_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 5),
    _ApDnsPeerRcvEntries_Type()
)
apDnsPeerRcvEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnsPeerRcvEntries.setStatus("current")


class _ApDnsPeerSndEntries_Type(Integer32):
    """Custom type apDnsPeerSndEntries based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 1024),
    )


_ApDnsPeerSndEntries_Type.__name__ = "Integer32"
_ApDnsPeerSndEntries_Object = MibScalar
apDnsPeerSndEntries = _ApDnsPeerSndEntries_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 6),
    _ApDnsPeerSndEntries_Type()
)
apDnsPeerSndEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnsPeerSndEntries.setStatus("current")


class _ApDnsPeerReportInterval_Type(Integer32):
    """Custom type apDnsPeerReportInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_ApDnsPeerReportInterval_Type.__name__ = "Integer32"
_ApDnsPeerReportInterval_Object = MibScalar
apDnsPeerReportInterval = _ApDnsPeerReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 7),
    _ApDnsPeerReportInterval_Type()
)
apDnsPeerReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnsPeerReportInterval.setStatus("current")


class _ApDnsAclIndex_Type(Integer32):
    """Custom type apDnsAclIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ApDnsAclIndex_Type.__name__ = "Integer32"
_ApDnsAclIndex_Object = MibScalar
apDnsAclIndex = _ApDnsAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 8),
    _ApDnsAclIndex_Type()
)
apDnsAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnsAclIndex.setStatus("current")


class _ApProximityType_Type(Integer32):
    """Custom type apProximityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pdb", 3),
          ("pdns", 2))
    )


_ApProximityType_Type.__name__ = "Integer32"
_ApProximityType_Object = MibScalar
apProximityType = _ApProximityType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 9),
    _ApProximityType_Type()
)
apProximityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProximityType.setStatus("current")


class _ApProximityEnable_Type(Integer32):
    """Custom type apProximityEnable based on Integer32"""
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


_ApProximityEnable_Type.__name__ = "Integer32"
_ApProximityEnable_Object = MibScalar
apProximityEnable = _ApProximityEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 10),
    _ApProximityEnable_Type()
)
apProximityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProximityEnable.setStatus("current")


class _ApProximityZone_Type(Integer32):
    """Custom type apProximityZone based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ApProximityZone_Type.__name__ = "Integer32"
_ApProximityZone_Object = MibScalar
apProximityZone = _ApProximityZone_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 11),
    _ApProximityZone_Type()
)
apProximityZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProximityZone.setStatus("current")


class _ApProximityDescription_Type(DisplayString):
    """Custom type apProximityDescription based on DisplayString"""
    defaultHexValue = "0"

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ApProximityDescription_Type.__name__ = "DisplayString"
_ApProximityDescription_Object = MibScalar
apProximityDescription = _ApProximityDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 12),
    _ApProximityDescription_Type()
)
apProximityDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityDescription.setStatus("current")


class _ApProximityZoneMax_Type(Integer32):
    """Custom type apProximityZoneMax based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              16)
        )
    )
    namedValues = NamedValues(
        *(("tier1", 6),
          ("tier2", 16))
    )


_ApProximityZoneMax_Type.__name__ = "Integer32"
_ApProximityZoneMax_Object = MibScalar
apProximityZoneMax = _ApProximityZoneMax_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 13),
    _ApProximityZoneMax_Type()
)
apProximityZoneMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProximityZoneMax.setStatus("current")


class _ApProximityPDBIpAddr_Type(IpAddress):
    """Custom type apProximityPDBIpAddr based on IpAddress"""
    defaultValue = 0


_ApProximityPDBIpAddr_Object = MibScalar
apProximityPDBIpAddr = _ApProximityPDBIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 14),
    _ApProximityPDBIpAddr_Type()
)
apProximityPDBIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityPDBIpAddr.setStatus("current")
_ApProximityRecordTable_Object = MibTable
apProximityRecordTable = _ApProximityRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15)
)
if mibBuilder.loadTexts:
    apProximityRecordTable.setStatus("current")
_ApProximityRecordEntry_Object = MibTableRow
apProximityRecordEntry = _ApProximityRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1)
)
apProximityRecordEntry.setIndexNames(
    (0, "DNSSERVEREXT-MIB", "apProximityRecordName"),
)
if mibBuilder.loadTexts:
    apProximityRecordEntry.setStatus("current")


class _ApProximityRecordName_Type(DisplayString):
    """Custom type apProximityRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApProximityRecordName_Type.__name__ = "DisplayString"
_ApProximityRecordName_Object = MibTableColumn
apProximityRecordName = _ApProximityRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 1),
    _ApProximityRecordName_Type()
)
apProximityRecordName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityRecordName.setStatus("current")


class _ApProximityRecordType_Type(Integer32):
    """Custom type apProximityRecordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("typeA", 1),
          ("typeNS", 2))
    )


_ApProximityRecordType_Type.__name__ = "Integer32"
_ApProximityRecordType_Object = MibTableColumn
apProximityRecordType = _ApProximityRecordType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 2),
    _ApProximityRecordType_Type()
)
apProximityRecordType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityRecordType.setStatus("current")
_ApProximityRecordAddr_Type = IpAddress
_ApProximityRecordAddr_Object = MibTableColumn
apProximityRecordAddr = _ApProximityRecordAddr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 3),
    _ApProximityRecordAddr_Type()
)
apProximityRecordAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityRecordAddr.setStatus("current")


class _ApProximityRecordTtl_Type(Integer32):
    """Custom type apProximityRecordTtl based on Integer32"""
    defaultValue = 0


_ApProximityRecordTtl_Object = MibTableColumn
apProximityRecordTtl = _ApProximityRecordTtl_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 4),
    _ApProximityRecordTtl_Type()
)
apProximityRecordTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityRecordTtl.setStatus("current")


class _ApProximityRecordKalType_Type(Integer32):
    """Custom type apProximityRecordKalType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kal-ap", 2),
          ("kal-icmp", 1),
          ("kal-none", 0))
    )


_ApProximityRecordKalType_Type.__name__ = "Integer32"
_ApProximityRecordKalType_Object = MibTableColumn
apProximityRecordKalType = _ApProximityRecordKalType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 5),
    _ApProximityRecordKalType_Type()
)
apProximityRecordKalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityRecordKalType.setStatus("current")
_ApProximityRecordKalAddr_Type = IpAddress
_ApProximityRecordKalAddr_Object = MibTableColumn
apProximityRecordKalAddr = _ApProximityRecordKalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 6),
    _ApProximityRecordKalAddr_Type()
)
apProximityRecordKalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityRecordKalAddr.setStatus("current")


class _ApProximityRecordKalThreshold_Type(Integer32):
    """Custom type apProximityRecordKalThreshold based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_ApProximityRecordKalThreshold_Type.__name__ = "Integer32"
_ApProximityRecordKalThreshold_Object = MibTableColumn
apProximityRecordKalThreshold = _ApProximityRecordKalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 7),
    _ApProximityRecordKalThreshold_Type()
)
apProximityRecordKalThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityRecordKalThreshold.setStatus("current")


class _ApProximityRecordRtnSingleArec_Type(Integer32):
    """Custom type apProximityRecordRtnSingleArec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("multiple", 0),
          ("single", 1))
    )


_ApProximityRecordRtnSingleArec_Type.__name__ = "Integer32"
_ApProximityRecordRtnSingleArec_Object = MibTableColumn
apProximityRecordRtnSingleArec = _ApProximityRecordRtnSingleArec_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 8),
    _ApProximityRecordRtnSingleArec_Type()
)
apProximityRecordRtnSingleArec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityRecordRtnSingleArec.setStatus("current")
_ApProximityRecordStatus_Type = RowStatus
_ApProximityRecordStatus_Object = MibTableColumn
apProximityRecordStatus = _ApProximityRecordStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 40, 15, 1, 9),
    _ApProximityRecordStatus_Type()
)
apProximityRecordStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apProximityRecordStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNSSERVEREXT-MIB",
    **{"apDnsServerMib": apDnsServerMib,
       "apDnsServerEnable": apDnsServerEnable,
       "apDnsServerBufferCount": apDnsServerBufferCount,
       "apDnsServerResponderTasks": apDnsServerResponderTasks,
       "apDnsPeerRcvEntries": apDnsPeerRcvEntries,
       "apDnsPeerSndEntries": apDnsPeerSndEntries,
       "apDnsPeerReportInterval": apDnsPeerReportInterval,
       "apDnsAclIndex": apDnsAclIndex,
       "apProximityType": apProximityType,
       "apProximityEnable": apProximityEnable,
       "apProximityZone": apProximityZone,
       "apProximityDescription": apProximityDescription,
       "apProximityZoneMax": apProximityZoneMax,
       "apProximityPDBIpAddr": apProximityPDBIpAddr,
       "apProximityRecordTable": apProximityRecordTable,
       "apProximityRecordEntry": apProximityRecordEntry,
       "apProximityRecordName": apProximityRecordName,
       "apProximityRecordType": apProximityRecordType,
       "apProximityRecordAddr": apProximityRecordAddr,
       "apProximityRecordTtl": apProximityRecordTtl,
       "apProximityRecordKalType": apProximityRecordKalType,
       "apProximityRecordKalAddr": apProximityRecordKalAddr,
       "apProximityRecordKalThreshold": apProximityRecordKalThreshold,
       "apProximityRecordRtnSingleArec": apProximityRecordRtnSingleArec,
       "apProximityRecordStatus": apProximityRecordStatus}
)
