# SNMP MIB module (CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:39 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SyslogSeverity,) = mibBuilder.importSymbols(
    "CISCO-SYSLOG-MIB",
    "SyslogSeverity")

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoTelepresenceExchangeSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758)
)
ciscoTelepresenceExchangeSystemMIB.setRevisions(
        ("2011-01-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CtxKeyId(OctetString, TextualConvention):
    status = "current"
    displayHint = "4x-"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class CtxIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class CtxPorts(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class CtxClusterNodeTypes(Integer32, TextualConvention):
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
        *(("admin", 1),
          ("db", 3),
          ("engine", 2))
    )



class CtxHealthStates(Integer32, TextualConvention):
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
        *(("error", 3),
          ("normal", 1),
          ("warning", 2))
    )



class CtxResourceOperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("failed", 3),
          ("maintenance", 4),
          ("operational", 1),
          ("pending", 5),
          ("standby", 6),
          ("unreachable", 7))
    )



class CtxSIPProtocolType(Integer32, TextualConvention):
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
        *(("tcp", 1),
          ("tls", 3),
          ("udp", 2))
    )



class CtxResourceType(Integer32, TextualConvention):
    status = "current"
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("ctms", 1),
          ("ctsmanager", 5),
          ("cucm", 10),
          ("cuvcm", 9),
          ("isdn", 8),
          ("ivr", 2),
          ("mseMedia2", 7),
          ("mseTps", 6),
          ("sbc", 3),
          ("sip", 4),
          ("tms", 12),
          ("vcs", 11))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoTelepresenceExchangeSystemMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTelepresenceExchangeSystemMIBNotifs = _CiscoTelepresenceExchangeSystemMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0)
)
_CiscoTelepresenceExchangeSystemMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTelepresenceExchangeSystemMIBObjects = _CiscoTelepresenceExchangeSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1)
)
_CtxConfigObjects_ObjectIdentity = ObjectIdentity
ctxConfigObjects = _CtxConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1)
)
_CtxServiceProviderTable_Object = MibTable
ctxServiceProviderTable = _CtxServiceProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctxServiceProviderTable.setStatus("current")
_CtxServiceProviderEntry_Object = MibTableRow
ctxServiceProviderEntry = _CtxServiceProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 1, 1)
)
ctxServiceProviderEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxServiceProviderIndex"),
)
if mibBuilder.loadTexts:
    ctxServiceProviderEntry.setStatus("current")
_CtxServiceProviderIndex_Type = CtxIndex
_CtxServiceProviderIndex_Object = MibTableColumn
ctxServiceProviderIndex = _CtxServiceProviderIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 1, 1, 1),
    _CtxServiceProviderIndex_Type()
)
ctxServiceProviderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctxServiceProviderIndex.setStatus("current")
_CtxServiceProviderKey_Type = CtxKeyId
_CtxServiceProviderKey_Object = MibTableColumn
ctxServiceProviderKey = _CtxServiceProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 1, 1, 2),
    _CtxServiceProviderKey_Type()
)
ctxServiceProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServiceProviderKey.setStatus("current")


class _CtxServiceProviderName_Type(DisplayString):
    """Custom type ctxServiceProviderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtxServiceProviderName_Type.__name__ = "DisplayString"
_CtxServiceProviderName_Object = MibTableColumn
ctxServiceProviderName = _CtxServiceProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 1, 1, 3),
    _CtxServiceProviderName_Type()
)
ctxServiceProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServiceProviderName.setStatus("current")


class _CtxServiceProviderDescr_Type(OctetString):
    """Custom type ctxServiceProviderDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtxServiceProviderDescr_Type.__name__ = "OctetString"
_CtxServiceProviderDescr_Object = MibTableColumn
ctxServiceProviderDescr = _CtxServiceProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 1, 1, 4),
    _CtxServiceProviderDescr_Type()
)
ctxServiceProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServiceProviderDescr.setStatus("current")
_CtxServiceProviderHDNumber_Type = DisplayString
_CtxServiceProviderHDNumber_Object = MibTableColumn
ctxServiceProviderHDNumber = _CtxServiceProviderHDNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 1, 1, 5),
    _CtxServiceProviderHDNumber_Type()
)
ctxServiceProviderHDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxServiceProviderHDNumber.setStatus("current")
_CtxRegionTable_Object = MibTable
ctxRegionTable = _CtxRegionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ctxRegionTable.setStatus("current")
_CtxRegionEntry_Object = MibTableRow
ctxRegionEntry = _CtxRegionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 2, 1)
)
ctxRegionEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionIndex"),
)
if mibBuilder.loadTexts:
    ctxRegionEntry.setStatus("current")
_CtxRegionIndex_Type = CtxIndex
_CtxRegionIndex_Object = MibTableColumn
ctxRegionIndex = _CtxRegionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 2, 1, 1),
    _CtxRegionIndex_Type()
)
ctxRegionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctxRegionIndex.setStatus("current")
_CtxRegionKey_Type = CtxKeyId
_CtxRegionKey_Object = MibTableColumn
ctxRegionKey = _CtxRegionKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 2, 1, 2),
    _CtxRegionKey_Type()
)
ctxRegionKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxRegionKey.setStatus("current")


class _CtxRegionName_Type(DisplayString):
    """Custom type ctxRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtxRegionName_Type.__name__ = "DisplayString"
_CtxRegionName_Object = MibTableColumn
ctxRegionName = _CtxRegionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 2, 1, 3),
    _CtxRegionName_Type()
)
ctxRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxRegionName.setStatus("current")


class _CtxRegionDescr_Type(OctetString):
    """Custom type ctxRegionDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtxRegionDescr_Type.__name__ = "OctetString"
_CtxRegionDescr_Object = MibTableColumn
ctxRegionDescr = _CtxRegionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 2, 1, 4),
    _CtxRegionDescr_Type()
)
ctxRegionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxRegionDescr.setStatus("current")
_CtxRegionServiceProviderKeyRef1_Type = CtxKeyId
_CtxRegionServiceProviderKeyRef1_Object = MibTableColumn
ctxRegionServiceProviderKeyRef1 = _CtxRegionServiceProviderKeyRef1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 2, 1, 5),
    _CtxRegionServiceProviderKeyRef1_Type()
)
ctxRegionServiceProviderKeyRef1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxRegionServiceProviderKeyRef1.setStatus("current")
_CtxOrganizationTable_Object = MibTable
ctxOrganizationTable = _CtxOrganizationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ctxOrganizationTable.setStatus("current")
_CtxOrganizationEntry_Object = MibTableRow
ctxOrganizationEntry = _CtxOrganizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 3, 1)
)
ctxOrganizationEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxOrganizationIndex"),
)
if mibBuilder.loadTexts:
    ctxOrganizationEntry.setStatus("current")
_CtxOrganizationIndex_Type = CtxIndex
_CtxOrganizationIndex_Object = MibTableColumn
ctxOrganizationIndex = _CtxOrganizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 3, 1, 1),
    _CtxOrganizationIndex_Type()
)
ctxOrganizationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctxOrganizationIndex.setStatus("current")
_CtxOrganizationKey_Type = CtxKeyId
_CtxOrganizationKey_Object = MibTableColumn
ctxOrganizationKey = _CtxOrganizationKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 3, 1, 2),
    _CtxOrganizationKey_Type()
)
ctxOrganizationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxOrganizationKey.setStatus("current")


class _CtxOrganizationName_Type(DisplayString):
    """Custom type ctxOrganizationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtxOrganizationName_Type.__name__ = "DisplayString"
_CtxOrganizationName_Object = MibTableColumn
ctxOrganizationName = _CtxOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 3, 1, 3),
    _CtxOrganizationName_Type()
)
ctxOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxOrganizationName.setStatus("current")


class _CtxOrganizationDescr_Type(OctetString):
    """Custom type ctxOrganizationDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtxOrganizationDescr_Type.__name__ = "OctetString"
_CtxOrganizationDescr_Object = MibTableColumn
ctxOrganizationDescr = _CtxOrganizationDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 3, 1, 4),
    _CtxOrganizationDescr_Type()
)
ctxOrganizationDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxOrganizationDescr.setStatus("current")
_CtxOrganizationMaxPorts_Type = CtxPorts
_CtxOrganizationMaxPorts_Object = MibTableColumn
ctxOrganizationMaxPorts = _CtxOrganizationMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 3, 1, 5),
    _CtxOrganizationMaxPorts_Type()
)
ctxOrganizationMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxOrganizationMaxPorts.setStatus("current")
_CtxOrganizationDirectDial_Type = TruthValue
_CtxOrganizationDirectDial_Object = MibTableColumn
ctxOrganizationDirectDial = _CtxOrganizationDirectDial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 3, 1, 6),
    _CtxOrganizationDirectDial_Type()
)
ctxOrganizationDirectDial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxOrganizationDirectDial.setStatus("current")
_CtxOrganizationServiceProviderKeyRef1_Type = CtxKeyId
_CtxOrganizationServiceProviderKeyRef1_Object = MibTableColumn
ctxOrganizationServiceProviderKeyRef1 = _CtxOrganizationServiceProviderKeyRef1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 3, 1, 7),
    _CtxOrganizationServiceProviderKeyRef1_Type()
)
ctxOrganizationServiceProviderKeyRef1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxOrganizationServiceProviderKeyRef1.setStatus("current")
_CtxResourceObjects_ObjectIdentity = ObjectIdentity
ctxResourceObjects = _CtxResourceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4)
)
_CtxResourceTable_Object = MibTable
ctxResourceTable = _CtxResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ctxResourceTable.setStatus("current")
_CtxResourceEntry_Object = MibTableRow
ctxResourceEntry = _CtxResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 1, 1)
)
ctxResourceEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceIndex"),
)
if mibBuilder.loadTexts:
    ctxResourceEntry.setStatus("current")
_CtxResourceIndex_Type = CtxIndex
_CtxResourceIndex_Object = MibTableColumn
ctxResourceIndex = _CtxResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 1, 1, 1),
    _CtxResourceIndex_Type()
)
ctxResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctxResourceIndex.setStatus("current")
_CtxResourceKey_Type = CtxKeyId
_CtxResourceKey_Object = MibTableColumn
ctxResourceKey = _CtxResourceKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 1, 1, 2),
    _CtxResourceKey_Type()
)
ctxResourceKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceKey.setStatus("current")


class _CtxResourceName_Type(DisplayString):
    """Custom type ctxResourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtxResourceName_Type.__name__ = "DisplayString"
_CtxResourceName_Object = MibTableColumn
ctxResourceName = _CtxResourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 1, 1, 3),
    _CtxResourceName_Type()
)
ctxResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceName.setStatus("current")


class _CtxResourceDescr_Type(OctetString):
    """Custom type ctxResourceDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtxResourceDescr_Type.__name__ = "OctetString"
_CtxResourceDescr_Object = MibTableColumn
ctxResourceDescr = _CtxResourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 1, 1, 4),
    _CtxResourceDescr_Type()
)
ctxResourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceDescr.setStatus("current")
_CtxResourceMgmtIPType_Type = InetAddressType
_CtxResourceMgmtIPType_Object = MibTableColumn
ctxResourceMgmtIPType = _CtxResourceMgmtIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 1, 1, 5),
    _CtxResourceMgmtIPType_Type()
)
ctxResourceMgmtIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceMgmtIPType.setStatus("current")
_CtxResourceMgmtIPAddr_Type = InetAddress
_CtxResourceMgmtIPAddr_Object = MibTableColumn
ctxResourceMgmtIPAddr = _CtxResourceMgmtIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 1, 1, 6),
    _CtxResourceMgmtIPAddr_Type()
)
ctxResourceMgmtIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceMgmtIPAddr.setStatus("current")
_CtxResourceDeviceType_Type = CtxResourceType
_CtxResourceDeviceType_Object = MibTableColumn
ctxResourceDeviceType = _CtxResourceDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 1, 1, 7),
    _CtxResourceDeviceType_Type()
)
ctxResourceDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceDeviceType.setStatus("current")
_CtxResourceRegionKeyRef1_Type = CtxKeyId
_CtxResourceRegionKeyRef1_Object = MibTableColumn
ctxResourceRegionKeyRef1 = _CtxResourceRegionKeyRef1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 1, 1, 8),
    _CtxResourceRegionKeyRef1_Type()
)
ctxResourceRegionKeyRef1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceRegionKeyRef1.setStatus("current")
_CtxSipConfigTable_Object = MibTable
ctxSipConfigTable = _CtxSipConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ctxSipConfigTable.setStatus("current")
_CtxSipConfigEntry_Object = MibTableRow
ctxSipConfigEntry = _CtxSipConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 2, 1)
)
ctxSipConfigEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceIndex"),
)
if mibBuilder.loadTexts:
    ctxSipConfigEntry.setStatus("current")
_CtxSipIpType_Type = InetAddressType
_CtxSipIpType_Object = MibTableColumn
ctxSipIpType = _CtxSipIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 2, 1, 1),
    _CtxSipIpType_Type()
)
ctxSipIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxSipIpType.setStatus("current")
_CtxSipIpAddr_Type = InetAddress
_CtxSipIpAddr_Object = MibTableColumn
ctxSipIpAddr = _CtxSipIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 2, 1, 2),
    _CtxSipIpAddr_Type()
)
ctxSipIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxSipIpAddr.setStatus("current")
_CtxSipPort_Type = CiscoPort
_CtxSipPort_Object = MibTableColumn
ctxSipPort = _CtxSipPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 2, 1, 3),
    _CtxSipPort_Type()
)
ctxSipPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxSipPort.setStatus("current")
_CtxSipTransportProto_Type = CtxSIPProtocolType
_CtxSipTransportProto_Object = MibTableColumn
ctxSipTransportProto = _CtxSipTransportProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 2, 1, 4),
    _CtxSipTransportProto_Type()
)
ctxSipTransportProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxSipTransportProto.setStatus("current")
_CtxMediaCapacityConfigTable_Object = MibTable
ctxMediaCapacityConfigTable = _CtxMediaCapacityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ctxMediaCapacityConfigTable.setStatus("current")
_CtxMediaCapacityConfigEntry_Object = MibTableRow
ctxMediaCapacityConfigEntry = _CtxMediaCapacityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 3, 1)
)
ctxMediaCapacityConfigEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceIndex"),
)
if mibBuilder.loadTexts:
    ctxMediaCapacityConfigEntry.setStatus("current")
_CtxMediaCapacityMaxPorts_Type = CtxPorts
_CtxMediaCapacityMaxPorts_Object = MibTableColumn
ctxMediaCapacityMaxPorts = _CtxMediaCapacityMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 3, 1, 1),
    _CtxMediaCapacityMaxPorts_Type()
)
ctxMediaCapacityMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxMediaCapacityMaxPorts.setStatus("current")
_CtxMediaCapacityLargeMeeting_Type = TruthValue
_CtxMediaCapacityLargeMeeting_Object = MibTableColumn
ctxMediaCapacityLargeMeeting = _CtxMediaCapacityLargeMeeting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 3, 1, 2),
    _CtxMediaCapacityLargeMeeting_Type()
)
ctxMediaCapacityLargeMeeting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxMediaCapacityLargeMeeting.setStatus("current")
_CtxMeetingConfigTable_Object = MibTable
ctxMeetingConfigTable = _CtxMeetingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ctxMeetingConfigTable.setStatus("current")
_CtxMeetingConfigEntry_Object = MibTableRow
ctxMeetingConfigEntry = _CtxMeetingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 4, 1)
)
ctxMeetingConfigEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceIndex"),
)
if mibBuilder.loadTexts:
    ctxMeetingConfigEntry.setStatus("current")


class _CtxMeetingConfigStaticMinId_Type(DisplayString):
    """Custom type ctxMeetingConfigStaticMinId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CtxMeetingConfigStaticMinId_Type.__name__ = "DisplayString"
_CtxMeetingConfigStaticMinId_Object = MibTableColumn
ctxMeetingConfigStaticMinId = _CtxMeetingConfigStaticMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 4, 1, 1),
    _CtxMeetingConfigStaticMinId_Type()
)
ctxMeetingConfigStaticMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxMeetingConfigStaticMinId.setStatus("current")


class _CtxMeetingConfigStaticMaxId_Type(DisplayString):
    """Custom type ctxMeetingConfigStaticMaxId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CtxMeetingConfigStaticMaxId_Type.__name__ = "DisplayString"
_CtxMeetingConfigStaticMaxId_Object = MibTableColumn
ctxMeetingConfigStaticMaxId = _CtxMeetingConfigStaticMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 4, 1, 2),
    _CtxMeetingConfigStaticMaxId_Type()
)
ctxMeetingConfigStaticMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxMeetingConfigStaticMaxId.setStatus("current")


class _CtxMeetingConfigInterOpMinId_Type(DisplayString):
    """Custom type ctxMeetingConfigInterOpMinId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CtxMeetingConfigInterOpMinId_Type.__name__ = "DisplayString"
_CtxMeetingConfigInterOpMinId_Object = MibTableColumn
ctxMeetingConfigInterOpMinId = _CtxMeetingConfigInterOpMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 4, 1, 3),
    _CtxMeetingConfigInterOpMinId_Type()
)
ctxMeetingConfigInterOpMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxMeetingConfigInterOpMinId.setStatus("current")


class _CtxMeetingConfigInterOpMaxId_Type(DisplayString):
    """Custom type ctxMeetingConfigInterOpMaxId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CtxMeetingConfigInterOpMaxId_Type.__name__ = "DisplayString"
_CtxMeetingConfigInterOpMaxId_Object = MibTableColumn
ctxMeetingConfigInterOpMaxId = _CtxMeetingConfigInterOpMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 4, 4, 1, 4),
    _CtxMeetingConfigInterOpMaxId_Type()
)
ctxMeetingConfigInterOpMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxMeetingConfigInterOpMaxId.setStatus("current")
_CtxClusterNodeTable_Object = MibTable
ctxClusterNodeTable = _CtxClusterNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ctxClusterNodeTable.setStatus("current")
_CtxClusterNodeEntry_Object = MibTableRow
ctxClusterNodeEntry = _CtxClusterNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5, 1)
)
ctxClusterNodeEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeIndex"),
)
if mibBuilder.loadTexts:
    ctxClusterNodeEntry.setStatus("current")
_CtxClusterNodeIndex_Type = CtxIndex
_CtxClusterNodeIndex_Object = MibTableColumn
ctxClusterNodeIndex = _CtxClusterNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5, 1, 1),
    _CtxClusterNodeIndex_Type()
)
ctxClusterNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctxClusterNodeIndex.setStatus("current")
_CtxClusterNodeKey_Type = CtxKeyId
_CtxClusterNodeKey_Object = MibTableColumn
ctxClusterNodeKey = _CtxClusterNodeKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5, 1, 2),
    _CtxClusterNodeKey_Type()
)
ctxClusterNodeKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxClusterNodeKey.setStatus("current")


class _CtxClusterNodeName_Type(DisplayString):
    """Custom type ctxClusterNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtxClusterNodeName_Type.__name__ = "DisplayString"
_CtxClusterNodeName_Object = MibTableColumn
ctxClusterNodeName = _CtxClusterNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5, 1, 3),
    _CtxClusterNodeName_Type()
)
ctxClusterNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxClusterNodeName.setStatus("current")
_CtxClusterNodeHostName_Type = DisplayString
_CtxClusterNodeHostName_Object = MibTableColumn
ctxClusterNodeHostName = _CtxClusterNodeHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5, 1, 4),
    _CtxClusterNodeHostName_Type()
)
ctxClusterNodeHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxClusterNodeHostName.setStatus("current")
_CtxClusterNodeIPType_Type = InetAddressType
_CtxClusterNodeIPType_Object = MibTableColumn
ctxClusterNodeIPType = _CtxClusterNodeIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5, 1, 5),
    _CtxClusterNodeIPType_Type()
)
ctxClusterNodeIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxClusterNodeIPType.setStatus("current")
_CtxClusterNodeIPAddr_Type = InetAddress
_CtxClusterNodeIPAddr_Object = MibTableColumn
ctxClusterNodeIPAddr = _CtxClusterNodeIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5, 1, 6),
    _CtxClusterNodeIPAddr_Type()
)
ctxClusterNodeIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxClusterNodeIPAddr.setStatus("current")


class _CtxClusterNodeClusterName_Type(DisplayString):
    """Custom type ctxClusterNodeClusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtxClusterNodeClusterName_Type.__name__ = "DisplayString"
_CtxClusterNodeClusterName_Object = MibTableColumn
ctxClusterNodeClusterName = _CtxClusterNodeClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5, 1, 7),
    _CtxClusterNodeClusterName_Type()
)
ctxClusterNodeClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxClusterNodeClusterName.setStatus("current")
_CtxClusterNodeType_Type = CtxClusterNodeTypes
_CtxClusterNodeType_Object = MibTableColumn
ctxClusterNodeType = _CtxClusterNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5, 1, 8),
    _CtxClusterNodeType_Type()
)
ctxClusterNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxClusterNodeType.setStatus("current")
_CtxClusterNodeOperState_Type = CtxResourceOperState
_CtxClusterNodeOperState_Object = MibTableColumn
ctxClusterNodeOperState = _CtxClusterNodeOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 1, 5, 1, 9),
    _CtxClusterNodeOperState_Type()
)
ctxClusterNodeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxClusterNodeOperState.setStatus("current")
_CtxSystemStatusObjects_ObjectIdentity = ObjectIdentity
ctxSystemStatusObjects = _CtxSystemStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 2)
)
_CtxAdminServersStatus_Type = CtxHealthStates
_CtxAdminServersStatus_Object = MibScalar
ctxAdminServersStatus = _CtxAdminServersStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 2, 1),
    _CtxAdminServersStatus_Type()
)
ctxAdminServersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAdminServersStatus.setStatus("current")
_CtxCallEnginesStatus_Type = CtxHealthStates
_CtxCallEnginesStatus_Object = MibScalar
ctxCallEnginesStatus = _CtxCallEnginesStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 2, 2),
    _CtxCallEnginesStatus_Type()
)
ctxCallEnginesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxCallEnginesStatus.setStatus("current")
_CtxDatabaseServersStatus_Type = CtxHealthStates
_CtxDatabaseServersStatus_Object = MibScalar
ctxDatabaseServersStatus = _CtxDatabaseServersStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 2, 3),
    _CtxDatabaseServersStatus_Type()
)
ctxDatabaseServersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxDatabaseServersStatus.setStatus("current")
_CtxResourceStatus_Type = CtxHealthStates
_CtxResourceStatus_Object = MibScalar
ctxResourceStatus = _CtxResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 2, 4),
    _CtxResourceStatus_Type()
)
ctxResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceStatus.setStatus("current")
_CtxSystemConfigStatus_Type = CtxHealthStates
_CtxSystemConfigStatus_Object = MibScalar
ctxSystemConfigStatus = _CtxSystemConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 2, 5),
    _CtxSystemConfigStatus_Type()
)
ctxSystemConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxSystemConfigStatus.setStatus("current")
_CtxSystemBackupStatus_Type = CtxHealthStates
_CtxSystemBackupStatus_Object = MibScalar
ctxSystemBackupStatus = _CtxSystemBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 2, 6),
    _CtxSystemBackupStatus_Type()
)
ctxSystemBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxSystemBackupStatus.setStatus("current")
_CtxStatisticsObjects_ObjectIdentity = ObjectIdentity
ctxStatisticsObjects = _CtxStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3)
)
_CtxResourceStatsTable_Object = MibTable
ctxResourceStatsTable = _CtxResourceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctxResourceStatsTable.setStatus("current")
_CtxResourceStatsEntry_Object = MibTableRow
ctxResourceStatsEntry = _CtxResourceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 1, 1)
)
ctxResourceStatsEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceIndex"),
)
if mibBuilder.loadTexts:
    ctxResourceStatsEntry.setStatus("current")
_CtxResourceOperState_Type = CtxResourceOperState
_CtxResourceOperState_Object = MibTableColumn
ctxResourceOperState = _CtxResourceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 1, 1, 1),
    _CtxResourceOperState_Type()
)
ctxResourceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceOperState.setStatus("current")
_CtxResourceUnavailTrans_Type = Counter32
_CtxResourceUnavailTrans_Object = MibTableColumn
ctxResourceUnavailTrans = _CtxResourceUnavailTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 1, 1, 2),
    _CtxResourceUnavailTrans_Type()
)
ctxResourceUnavailTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceUnavailTrans.setStatus("current")
if mibBuilder.loadTexts:
    ctxResourceUnavailTrans.setUnits("occurrences")
_CtxResourceUnavailDuration_Type = Counter32
_CtxResourceUnavailDuration_Object = MibTableColumn
ctxResourceUnavailDuration = _CtxResourceUnavailDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 1, 1, 3),
    _CtxResourceUnavailDuration_Type()
)
ctxResourceUnavailDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceUnavailDuration.setStatus("current")
if mibBuilder.loadTexts:
    ctxResourceUnavailDuration.setUnits("seconds")
_CtxResourceCallSetupFailures_Type = Counter32
_CtxResourceCallSetupFailures_Object = MibTableColumn
ctxResourceCallSetupFailures = _CtxResourceCallSetupFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 1, 1, 4),
    _CtxResourceCallSetupFailures_Type()
)
ctxResourceCallSetupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxResourceCallSetupFailures.setStatus("current")
if mibBuilder.loadTexts:
    ctxResourceCallSetupFailures.setUnits("occurrences")
_CtxAllocStatsTable_Object = MibTable
ctxAllocStatsTable = _CtxAllocStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ctxAllocStatsTable.setStatus("current")
_CtxAllocStatsEntry_Object = MibTableRow
ctxAllocStatsEntry = _CtxAllocStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 2, 1)
)
ctxAllocStatsEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceIndex"),
)
if mibBuilder.loadTexts:
    ctxAllocStatsEntry.setStatus("current")
_CtxAllocActivePorts_Type = CtxPorts
_CtxAllocActivePorts_Object = MibTableColumn
ctxAllocActivePorts = _CtxAllocActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 2, 1, 1),
    _CtxAllocActivePorts_Type()
)
ctxAllocActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAllocActivePorts.setStatus("current")
_CtxAllocAvailPorts_Type = CtxPorts
_CtxAllocAvailPorts_Object = MibTableColumn
ctxAllocAvailPorts = _CtxAllocAvailPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 2, 1, 2),
    _CtxAllocAvailPorts_Type()
)
ctxAllocAvailPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAllocAvailPorts.setStatus("current")
_CtxAllocFailures_Type = Counter32
_CtxAllocFailures_Object = MibTableColumn
ctxAllocFailures = _CtxAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 2, 1, 3),
    _CtxAllocFailures_Type()
)
ctxAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAllocFailures.setStatus("current")
if mibBuilder.loadTexts:
    ctxAllocFailures.setUnits("failures")
_CtxAllocOutOfPorts_Type = Counter32
_CtxAllocOutOfPorts_Object = MibTableColumn
ctxAllocOutOfPorts = _CtxAllocOutOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 2, 1, 4),
    _CtxAllocOutOfPorts_Type()
)
ctxAllocOutOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAllocOutOfPorts.setStatus("current")
if mibBuilder.loadTexts:
    ctxAllocOutOfPorts.setUnits("occurrences")
_CtxRegionStatsTable_Object = MibTable
ctxRegionStatsTable = _CtxRegionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ctxRegionStatsTable.setStatus("current")
_CtxRegionStatsEntry_Object = MibTableRow
ctxRegionStatsEntry = _CtxRegionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 3, 1)
)
ctxRegionStatsEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionIndex"),
)
if mibBuilder.loadTexts:
    ctxRegionStatsEntry.setStatus("current")
_CtxRegionCallSetupFailures_Type = Counter32
_CtxRegionCallSetupFailures_Object = MibTableColumn
ctxRegionCallSetupFailures = _CtxRegionCallSetupFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 3, 1, 1),
    _CtxRegionCallSetupFailures_Type()
)
ctxRegionCallSetupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxRegionCallSetupFailures.setStatus("current")
if mibBuilder.loadTexts:
    ctxRegionCallSetupFailures.setUnits("failures")
_CtxAllocPoolActivePorts_Type = CtxPorts
_CtxAllocPoolActivePorts_Object = MibTableColumn
ctxAllocPoolActivePorts = _CtxAllocPoolActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 3, 1, 2),
    _CtxAllocPoolActivePorts_Type()
)
ctxAllocPoolActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAllocPoolActivePorts.setStatus("current")
_CtxAllocPoolAvailPorts_Type = CtxPorts
_CtxAllocPoolAvailPorts_Object = MibTableColumn
ctxAllocPoolAvailPorts = _CtxAllocPoolAvailPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 3, 1, 3),
    _CtxAllocPoolAvailPorts_Type()
)
ctxAllocPoolAvailPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAllocPoolAvailPorts.setStatus("current")
_CtxAllocPoolAllocFailures_Type = Counter32
_CtxAllocPoolAllocFailures_Object = MibTableColumn
ctxAllocPoolAllocFailures = _CtxAllocPoolAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 3, 1, 4),
    _CtxAllocPoolAllocFailures_Type()
)
ctxAllocPoolAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAllocPoolAllocFailures.setStatus("current")
if mibBuilder.loadTexts:
    ctxAllocPoolAllocFailures.setUnits("failures")
_CtxAllocPoolAllocOutOfPorts_Type = Counter32
_CtxAllocPoolAllocOutOfPorts_Object = MibTableColumn
ctxAllocPoolAllocOutOfPorts = _CtxAllocPoolAllocOutOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 3, 1, 5),
    _CtxAllocPoolAllocOutOfPorts_Type()
)
ctxAllocPoolAllocOutOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxAllocPoolAllocOutOfPorts.setStatus("current")
if mibBuilder.loadTexts:
    ctxAllocPoolAllocOutOfPorts.setUnits("occurrences")
_CtxAllocPeakHistory_ObjectIdentity = ObjectIdentity
ctxAllocPeakHistory = _CtxAllocPeakHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4)
)


class _CtxPeakHistMaxIntervals_Type(Unsigned32):
    """Custom type ctxPeakHistMaxIntervals based on Unsigned32"""
    defaultValue = 96

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 1440),
    )


_CtxPeakHistMaxIntervals_Type.__name__ = "Unsigned32"
_CtxPeakHistMaxIntervals_Object = MibScalar
ctxPeakHistMaxIntervals = _CtxPeakHistMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 1),
    _CtxPeakHistMaxIntervals_Type()
)
ctxPeakHistMaxIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxPeakHistMaxIntervals.setStatus("current")
if mibBuilder.loadTexts:
    ctxPeakHistMaxIntervals.setUnits("intervals")


class _CtxPeakHistIntTime_Type(Unsigned32):
    """Custom type ctxPeakHistIntTime based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_CtxPeakHistIntTime_Type.__name__ = "Unsigned32"
_CtxPeakHistIntTime_Object = MibScalar
ctxPeakHistIntTime = _CtxPeakHistIntTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 2),
    _CtxPeakHistIntTime_Type()
)
ctxPeakHistIntTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxPeakHistIntTime.setStatus("current")
if mibBuilder.loadTexts:
    ctxPeakHistIntTime.setUnits("minutes")
_CtxPeakHistAllocTable_Object = MibTable
ctxPeakHistAllocTable = _CtxPeakHistAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    ctxPeakHistAllocTable.setStatus("current")
_CtxPeakHistAllocEntry_Object = MibTableRow
ctxPeakHistAllocEntry = _CtxPeakHistAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 3, 1)
)
ctxPeakHistAllocEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceIndex"),
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxPeakHistAllocIntIndex"),
)
if mibBuilder.loadTexts:
    ctxPeakHistAllocEntry.setStatus("current")


class _CtxPeakHistAllocIntIndex_Type(Integer32):
    """Custom type ctxPeakHistAllocIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxPeakHistAllocIntIndex_Type.__name__ = "Integer32"
_CtxPeakHistAllocIntIndex_Object = MibTableColumn
ctxPeakHistAllocIntIndex = _CtxPeakHistAllocIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 3, 1, 1),
    _CtxPeakHistAllocIntIndex_Type()
)
ctxPeakHistAllocIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctxPeakHistAllocIntIndex.setStatus("current")
_CtxPeakHistAllocTS_Type = TimeStamp
_CtxPeakHistAllocTS_Object = MibTableColumn
ctxPeakHistAllocTS = _CtxPeakHistAllocTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 3, 1, 2),
    _CtxPeakHistAllocTS_Type()
)
ctxPeakHistAllocTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxPeakHistAllocTS.setStatus("current")
_CtxPeakHistAllocPorts_Type = CtxPorts
_CtxPeakHistAllocPorts_Object = MibTableColumn
ctxPeakHistAllocPorts = _CtxPeakHistAllocPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 3, 1, 3),
    _CtxPeakHistAllocPorts_Type()
)
ctxPeakHistAllocPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxPeakHistAllocPorts.setStatus("current")
if mibBuilder.loadTexts:
    ctxPeakHistAllocPorts.setUnits("ports")
_CtxPeakHistAllocPoolTable_Object = MibTable
ctxPeakHistAllocPoolTable = _CtxPeakHistAllocPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    ctxPeakHistAllocPoolTable.setStatus("current")
_CtxPeakHistAllocPoolEntry_Object = MibTableRow
ctxPeakHistAllocPoolEntry = _CtxPeakHistAllocPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 4, 1)
)
ctxPeakHistAllocPoolEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionIndex"),
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxPeakHistAllocPoolIntIndex"),
)
if mibBuilder.loadTexts:
    ctxPeakHistAllocPoolEntry.setStatus("current")


class _CtxPeakHistAllocPoolIntIndex_Type(Integer32):
    """Custom type ctxPeakHistAllocPoolIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtxPeakHistAllocPoolIntIndex_Type.__name__ = "Integer32"
_CtxPeakHistAllocPoolIntIndex_Object = MibTableColumn
ctxPeakHistAllocPoolIntIndex = _CtxPeakHistAllocPoolIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 4, 1, 1),
    _CtxPeakHistAllocPoolIntIndex_Type()
)
ctxPeakHistAllocPoolIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctxPeakHistAllocPoolIntIndex.setStatus("current")
_CtxPeakHistAllocPoolTS_Type = TimeStamp
_CtxPeakHistAllocPoolTS_Object = MibTableColumn
ctxPeakHistAllocPoolTS = _CtxPeakHistAllocPoolTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 4, 1, 2),
    _CtxPeakHistAllocPoolTS_Type()
)
ctxPeakHistAllocPoolTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxPeakHistAllocPoolTS.setStatus("current")
_CtxPeakHistAllocPoolPorts_Type = CtxPorts
_CtxPeakHistAllocPoolPorts_Object = MibTableColumn
ctxPeakHistAllocPoolPorts = _CtxPeakHistAllocPoolPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 3, 4, 4, 1, 3),
    _CtxPeakHistAllocPoolPorts_Type()
)
ctxPeakHistAllocPoolPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxPeakHistAllocPoolPorts.setStatus("current")
if mibBuilder.loadTexts:
    ctxPeakHistAllocPoolPorts.setUnits("ports")
_CtxEventHistory_ObjectIdentity = ObjectIdentity
ctxEventHistory = _CtxEventHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4)
)


class _CtxErrorHistoryTableSize_Type(Unsigned32):
    """Custom type ctxErrorHistoryTableSize based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(25, 2500),
    )


_CtxErrorHistoryTableSize_Type.__name__ = "Unsigned32"
_CtxErrorHistoryTableSize_Object = MibScalar
ctxErrorHistoryTableSize = _CtxErrorHistoryTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 1),
    _CtxErrorHistoryTableSize_Type()
)
ctxErrorHistoryTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxErrorHistoryTableSize.setStatus("current")


class _CtxErrorHistoryMaxSeverity_Type(SyslogSeverity):
    """Custom type ctxErrorHistoryMaxSeverity based on SyslogSeverity"""


_CtxErrorHistoryMaxSeverity_Object = MibScalar
ctxErrorHistoryMaxSeverity = _CtxErrorHistoryMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 2),
    _CtxErrorHistoryMaxSeverity_Type()
)
ctxErrorHistoryMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxErrorHistoryMaxSeverity.setStatus("current")
_CtxErrorHistoryLastIndex_Type = CtxIndex
_CtxErrorHistoryLastIndex_Object = MibScalar
ctxErrorHistoryLastIndex = _CtxErrorHistoryLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 3),
    _CtxErrorHistoryLastIndex_Type()
)
ctxErrorHistoryLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxErrorHistoryLastIndex.setStatus("current")
_CtxErrorHistoryTable_Object = MibTable
ctxErrorHistoryTable = _CtxErrorHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ctxErrorHistoryTable.setStatus("current")
_CtxErrorHistoryEntry_Object = MibTableRow
ctxErrorHistoryEntry = _CtxErrorHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 4, 1)
)
ctxErrorHistoryEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorIndex"),
)
if mibBuilder.loadTexts:
    ctxErrorHistoryEntry.setStatus("current")
_CtxErrorIndex_Type = CtxIndex
_CtxErrorIndex_Object = MibTableColumn
ctxErrorIndex = _CtxErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 4, 1, 1),
    _CtxErrorIndex_Type()
)
ctxErrorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctxErrorIndex.setStatus("current")
_CtxErrorKey_Type = CtxKeyId
_CtxErrorKey_Object = MibTableColumn
ctxErrorKey = _CtxErrorKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 4, 1, 2),
    _CtxErrorKey_Type()
)
ctxErrorKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxErrorKey.setStatus("current")
_CtxErrorTimeStamp_Type = TimeStamp
_CtxErrorTimeStamp_Object = MibTableColumn
ctxErrorTimeStamp = _CtxErrorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 4, 1, 3),
    _CtxErrorTimeStamp_Type()
)
ctxErrorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxErrorTimeStamp.setStatus("current")
_CtxErrorSeverity_Type = SyslogSeverity
_CtxErrorSeverity_Object = MibTableColumn
ctxErrorSeverity = _CtxErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 4, 1, 4),
    _CtxErrorSeverity_Type()
)
ctxErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxErrorSeverity.setStatus("current")


class _CtxErrorAppName_Type(DisplayString):
    """Custom type ctxErrorAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_CtxErrorAppName_Type.__name__ = "DisplayString"
_CtxErrorAppName_Object = MibTableColumn
ctxErrorAppName = _CtxErrorAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 4, 1, 5),
    _CtxErrorAppName_Type()
)
ctxErrorAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxErrorAppName.setStatus("current")


class _CtxErrorAlarmId_Type(DisplayString):
    """Custom type ctxErrorAlarmId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CtxErrorAlarmId_Type.__name__ = "DisplayString"
_CtxErrorAlarmId_Object = MibTableColumn
ctxErrorAlarmId = _CtxErrorAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 4, 1, 6),
    _CtxErrorAlarmId_Type()
)
ctxErrorAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxErrorAlarmId.setStatus("current")
_CtxErrorAttrValStr_Type = DisplayString
_CtxErrorAttrValStr_Object = MibTableColumn
ctxErrorAttrValStr = _CtxErrorAttrValStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 4, 1, 7),
    _CtxErrorAttrValStr_Type()
)
ctxErrorAttrValStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxErrorAttrValStr.setStatus("current")
_CtxErrorMessage_Type = DisplayString
_CtxErrorMessage_Object = MibTableColumn
ctxErrorMessage = _CtxErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 4, 4, 1, 8),
    _CtxErrorMessage_Type()
)
ctxErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxErrorMessage.setStatus("current")
_CtxNotifyObjects_ObjectIdentity = ObjectIdentity
ctxNotifyObjects = _CtxNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 5)
)
_CtxNotifyMessage_Type = DisplayString
_CtxNotifyMessage_Object = MibScalar
ctxNotifyMessage = _CtxNotifyMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 5, 1),
    _CtxNotifyMessage_Type()
)
ctxNotifyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctxNotifyMessage.setStatus("current")
_CtxNotifyConfigObjects_ObjectIdentity = ObjectIdentity
ctxNotifyConfigObjects = _CtxNotifyConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 5, 2)
)


class _CtxStatusChangeNotifyEnable_Type(TruthValue):
    """Custom type ctxStatusChangeNotifyEnable based on TruthValue"""


_CtxStatusChangeNotifyEnable_Object = MibScalar
ctxStatusChangeNotifyEnable = _CtxStatusChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 5, 2, 1),
    _CtxStatusChangeNotifyEnable_Type()
)
ctxStatusChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxStatusChangeNotifyEnable.setStatus("current")


class _CtxLicenseAlarmNotifyEnable_Type(TruthValue):
    """Custom type ctxLicenseAlarmNotifyEnable based on TruthValue"""


_CtxLicenseAlarmNotifyEnable_Object = MibScalar
ctxLicenseAlarmNotifyEnable = _CtxLicenseAlarmNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 5, 2, 2),
    _CtxLicenseAlarmNotifyEnable_Type()
)
ctxLicenseAlarmNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxLicenseAlarmNotifyEnable.setStatus("current")


class _CtxAuthFailureNotifyEnable_Type(TruthValue):
    """Custom type ctxAuthFailureNotifyEnable based on TruthValue"""


_CtxAuthFailureNotifyEnable_Object = MibScalar
ctxAuthFailureNotifyEnable = _CtxAuthFailureNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 5, 2, 3),
    _CtxAuthFailureNotifyEnable_Type()
)
ctxAuthFailureNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxAuthFailureNotifyEnable.setStatus("current")


class _CtxClusterNodeAlarmNotifyEnable_Type(TruthValue):
    """Custom type ctxClusterNodeAlarmNotifyEnable based on TruthValue"""


_CtxClusterNodeAlarmNotifyEnable_Object = MibScalar
ctxClusterNodeAlarmNotifyEnable = _CtxClusterNodeAlarmNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 5, 2, 4),
    _CtxClusterNodeAlarmNotifyEnable_Type()
)
ctxClusterNodeAlarmNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxClusterNodeAlarmNotifyEnable.setStatus("current")


class _CtxResourceAlarmNotifyEnable_Type(TruthValue):
    """Custom type ctxResourceAlarmNotifyEnable based on TruthValue"""


_CtxResourceAlarmNotifyEnable_Object = MibScalar
ctxResourceAlarmNotifyEnable = _CtxResourceAlarmNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 5, 2, 5),
    _CtxResourceAlarmNotifyEnable_Type()
)
ctxResourceAlarmNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxResourceAlarmNotifyEnable.setStatus("current")


class _CtxCallFailureNotifyEnable_Type(TruthValue):
    """Custom type ctxCallFailureNotifyEnable based on TruthValue"""


_CtxCallFailureNotifyEnable_Object = MibScalar
ctxCallFailureNotifyEnable = _CtxCallFailureNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 5, 2, 6),
    _CtxCallFailureNotifyEnable_Type()
)
ctxCallFailureNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxCallFailureNotifyEnable.setStatus("current")


class _CtxErrorHistoryEventNotifyEnable_Type(TruthValue):
    """Custom type ctxErrorHistoryEventNotifyEnable based on TruthValue"""


_CtxErrorHistoryEventNotifyEnable_Object = MibScalar
ctxErrorHistoryEventNotifyEnable = _CtxErrorHistoryEventNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 1, 5, 2, 7),
    _CtxErrorHistoryEventNotifyEnable_Type()
)
ctxErrorHistoryEventNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctxErrorHistoryEventNotifyEnable.setStatus("current")
_CiscoTelepresenceExchangeSystemMIBConform_ObjectIdentity = ObjectIdentity
ciscoTelepresenceExchangeSystemMIBConform = _CiscoTelepresenceExchangeSystemMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 7)
)
_CiscoTelepresenceExchangeSystemMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTelepresenceExchangeSystemMIBCompliances = _CiscoTelepresenceExchangeSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 7, 1)
)
_CiscoTelepresenceExchangeSystemMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTelepresenceExchangeSystemMIBGroups = _CiscoTelepresenceExchangeSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 7, 2)
)

# Managed Objects groups

ciscoTelepresenceExchangeSystemMIBStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 7, 2, 1)
)
ciscoTelepresenceExchangeSystemMIBStatusGroup.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAdminServersStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxCallEnginesStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxDatabaseServersStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxSystemConfigStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxSystemBackupStatus"))
)
if mibBuilder.loadTexts:
    ciscoTelepresenceExchangeSystemMIBStatusGroup.setStatus("current")

ciscoTelepresenceExchangeSystemMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 7, 2, 2)
)
ciscoTelepresenceExchangeSystemMIBConfigGroup.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxServiceProviderName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxServiceProviderDescr"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxServiceProviderHDNumber"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionDescr"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxOrganizationName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxOrganizationDescr"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxOrganizationMaxPorts"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxOrganizationDirectDial"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceDescr"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceMgmtIPType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceMgmtIPAddr"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceDeviceType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxSipIpType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxSipIpAddr"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxSipPort"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxSipTransportProto"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxMediaCapacityMaxPorts"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxMediaCapacityLargeMeeting"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeHostName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeIPType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeIPAddr"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeClusterName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxServiceProviderKey"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionKey"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionServiceProviderKeyRef1"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxOrganizationKey"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxOrganizationServiceProviderKeyRef1"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceKey"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceRegionKeyRef1"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeOperState"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeKey"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxMeetingConfigStaticMinId"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxMeetingConfigStaticMaxId"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxMeetingConfigInterOpMinId"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxMeetingConfigInterOpMaxId"))
)
if mibBuilder.loadTexts:
    ciscoTelepresenceExchangeSystemMIBConfigGroup.setStatus("current")

ciscoTelePresenceExchangeSystemMIBStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 7, 2, 3)
)
ciscoTelePresenceExchangeSystemMIBStatsGroup.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceUnavailTrans"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAllocActivePorts"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAllocAvailPorts"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAllocPoolActivePorts"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAllocPoolAvailPorts"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAllocFailures"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAllocPoolAllocFailures"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceCallSetupFailures"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionCallSetupFailures"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAllocOutOfPorts"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAllocPoolAllocOutOfPorts"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceOperState"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceUnavailDuration"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxPeakHistMaxIntervals"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxPeakHistIntTime"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxPeakHistAllocTS"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxPeakHistAllocPorts"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxPeakHistAllocPoolTS"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxPeakHistAllocPoolPorts"))
)
if mibBuilder.loadTexts:
    ciscoTelePresenceExchangeSystemMIBStatsGroup.setStatus("current")

ciscoTelepresenceExchangeSystemMIBNotfyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 7, 2, 4)
)
ciscoTelepresenceExchangeSystemMIBNotfyObjectsGroup.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxStatusChangeNotifyEnable"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxLicenseAlarmNotifyEnable"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAuthFailureNotifyEnable"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeAlarmNotifyEnable"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceAlarmNotifyEnable"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxCallFailureNotifyEnable"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorHistoryEventNotifyEnable"))
)
if mibBuilder.loadTexts:
    ciscoTelepresenceExchangeSystemMIBNotfyObjectsGroup.setStatus("current")

ciscoTelepresenceExchangeSystemMIBErrorHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 7, 2, 5)
)
ciscoTelepresenceExchangeSystemMIBErrorHistoryGroup.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorHistoryTableSize"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorHistoryMaxSeverity"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorHistoryLastIndex"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorKey"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorTimeStamp"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorSeverity"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorMessage"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorAppName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorAlarmId"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorAttrValStr"))
)
if mibBuilder.loadTexts:
    ciscoTelepresenceExchangeSystemMIBErrorHistoryGroup.setStatus("current")


# Notification objects

ciscoCTXSysAdminServersStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 1)
)
ciscoCTXSysAdminServersStatusChg.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxAdminServersStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysAdminServersStatusChg.setStatus(
        "current"
    )

ciscoCTXSysDatabaseServersStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 2)
)
ciscoCTXSysDatabaseServersStatusChg.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxDatabaseServersStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysDatabaseServersStatusChg.setStatus(
        "current"
    )

ciscoCTXSysCallEnginesStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 3)
)
ciscoCTXSysCallEnginesStatusChg.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxCallEnginesStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysCallEnginesStatusChg.setStatus(
        "current"
    )

ciscoCTXSysResourceStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 4)
)
ciscoCTXSysResourceStatusChg.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysResourceStatusChg.setStatus(
        "current"
    )

ciscoCTXSysSystemConfigStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 5)
)
ciscoCTXSysSystemConfigStatusChg.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxSystemConfigStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysSystemConfigStatusChg.setStatus(
        "current"
    )

ciscoCTXSysSystemBackupStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 6)
)
ciscoCTXSysSystemBackupStatusChg.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxSystemBackupStatus"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysSystemBackupStatusChg.setStatus(
        "current"
    )

ciscoCTXSysLicenseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 7)
)
ciscoCTXSysLicenseFailure.setObjects(
    ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage")
)
if mibBuilder.loadTexts:
    ciscoCTXSysLicenseFailure.setStatus(
        "current"
    )

ciscoCTXSysUserAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 8)
)
ciscoCTXSysUserAuthFailure.setObjects(
    ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage")
)
if mibBuilder.loadTexts:
    ciscoCTXSysUserAuthFailure.setStatus(
        "current"
    )

ciscoCTXSysClusterNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 9)
)
ciscoCTXSysClusterNodeDown.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysClusterNodeDown.setStatus(
        "current"
    )

ciscoCTXSysClusterNodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 10)
)
ciscoCTXSysClusterNodeUp.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxClusterNodeName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysClusterNodeUp.setStatus(
        "current"
    )

ciscoCTXSysResourceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 11)
)
ciscoCTXSysResourceDown.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceDeviceType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysResourceDown.setStatus(
        "current"
    )

ciscoCTXSysResourceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 12)
)
ciscoCTXSysResourceUp.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceDeviceType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysResourceUp.setStatus(
        "current"
    )

ciscoCTXSysResourceAllocFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 13)
)
ciscoCTXSysResourceAllocFailure.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceDeviceType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxRegionKey"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysResourceAllocFailure.setStatus(
        "current"
    )

ciscoCTXSysCallSetupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 14)
)
ciscoCTXSysCallSetupFailure.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceDeviceType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysCallSetupFailure.setStatus(
        "current"
    )

ciscoCTXSysCallAbnormalDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 15)
)
ciscoCTXSysCallAbnormalDisconnect.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxResourceDeviceType"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxNotifyMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysCallAbnormalDisconnect.setStatus(
        "current"
    )

ciscoCTXSysErrorHistoryEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 0, 16)
)
ciscoCTXSysErrorHistoryEvent.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorKey"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorSeverity"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorAppName"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorAlarmId"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorAttrValStr"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ctxErrorMessage"))
)
if mibBuilder.loadTexts:
    ciscoCTXSysErrorHistoryEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoTelepresenceExchangeSystemMIBNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 7, 2, 6)
)
ciscoTelepresenceExchangeSystemMIBNotifyGroup.setObjects(
      *(("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysAdminServersStatusChg"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysDatabaseServersStatusChg"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysCallEnginesStatusChg"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysResourceStatusChg"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysSystemConfigStatusChg"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysSystemBackupStatusChg"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysLicenseFailure"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysUserAuthFailure"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysClusterNodeDown"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysResourceDown"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysCallSetupFailure"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysErrorHistoryEvent"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysCallAbnormalDisconnect"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysResourceAllocFailure"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysClusterNodeUp"),
        ("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB", "ciscoCTXSysResourceUp"))
)
if mibBuilder.loadTexts:
    ciscoTelepresenceExchangeSystemMIBNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTelepresenceExchangeSystemMIBModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 758, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTelepresenceExchangeSystemMIBModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB",
    **{"CtxKeyId": CtxKeyId,
       "CtxIndex": CtxIndex,
       "CtxPorts": CtxPorts,
       "CtxClusterNodeTypes": CtxClusterNodeTypes,
       "CtxHealthStates": CtxHealthStates,
       "CtxResourceOperState": CtxResourceOperState,
       "CtxSIPProtocolType": CtxSIPProtocolType,
       "CtxResourceType": CtxResourceType,
       "ciscoTelepresenceExchangeSystemMIB": ciscoTelepresenceExchangeSystemMIB,
       "ciscoTelepresenceExchangeSystemMIBNotifs": ciscoTelepresenceExchangeSystemMIBNotifs,
       "ciscoCTXSysAdminServersStatusChg": ciscoCTXSysAdminServersStatusChg,
       "ciscoCTXSysDatabaseServersStatusChg": ciscoCTXSysDatabaseServersStatusChg,
       "ciscoCTXSysCallEnginesStatusChg": ciscoCTXSysCallEnginesStatusChg,
       "ciscoCTXSysResourceStatusChg": ciscoCTXSysResourceStatusChg,
       "ciscoCTXSysSystemConfigStatusChg": ciscoCTXSysSystemConfigStatusChg,
       "ciscoCTXSysSystemBackupStatusChg": ciscoCTXSysSystemBackupStatusChg,
       "ciscoCTXSysLicenseFailure": ciscoCTXSysLicenseFailure,
       "ciscoCTXSysUserAuthFailure": ciscoCTXSysUserAuthFailure,
       "ciscoCTXSysClusterNodeDown": ciscoCTXSysClusterNodeDown,
       "ciscoCTXSysClusterNodeUp": ciscoCTXSysClusterNodeUp,
       "ciscoCTXSysResourceDown": ciscoCTXSysResourceDown,
       "ciscoCTXSysResourceUp": ciscoCTXSysResourceUp,
       "ciscoCTXSysResourceAllocFailure": ciscoCTXSysResourceAllocFailure,
       "ciscoCTXSysCallSetupFailure": ciscoCTXSysCallSetupFailure,
       "ciscoCTXSysCallAbnormalDisconnect": ciscoCTXSysCallAbnormalDisconnect,
       "ciscoCTXSysErrorHistoryEvent": ciscoCTXSysErrorHistoryEvent,
       "ciscoTelepresenceExchangeSystemMIBObjects": ciscoTelepresenceExchangeSystemMIBObjects,
       "ctxConfigObjects": ctxConfigObjects,
       "ctxServiceProviderTable": ctxServiceProviderTable,
       "ctxServiceProviderEntry": ctxServiceProviderEntry,
       "ctxServiceProviderIndex": ctxServiceProviderIndex,
       "ctxServiceProviderKey": ctxServiceProviderKey,
       "ctxServiceProviderName": ctxServiceProviderName,
       "ctxServiceProviderDescr": ctxServiceProviderDescr,
       "ctxServiceProviderHDNumber": ctxServiceProviderHDNumber,
       "ctxRegionTable": ctxRegionTable,
       "ctxRegionEntry": ctxRegionEntry,
       "ctxRegionIndex": ctxRegionIndex,
       "ctxRegionKey": ctxRegionKey,
       "ctxRegionName": ctxRegionName,
       "ctxRegionDescr": ctxRegionDescr,
       "ctxRegionServiceProviderKeyRef1": ctxRegionServiceProviderKeyRef1,
       "ctxOrganizationTable": ctxOrganizationTable,
       "ctxOrganizationEntry": ctxOrganizationEntry,
       "ctxOrganizationIndex": ctxOrganizationIndex,
       "ctxOrganizationKey": ctxOrganizationKey,
       "ctxOrganizationName": ctxOrganizationName,
       "ctxOrganizationDescr": ctxOrganizationDescr,
       "ctxOrganizationMaxPorts": ctxOrganizationMaxPorts,
       "ctxOrganizationDirectDial": ctxOrganizationDirectDial,
       "ctxOrganizationServiceProviderKeyRef1": ctxOrganizationServiceProviderKeyRef1,
       "ctxResourceObjects": ctxResourceObjects,
       "ctxResourceTable": ctxResourceTable,
       "ctxResourceEntry": ctxResourceEntry,
       "ctxResourceIndex": ctxResourceIndex,
       "ctxResourceKey": ctxResourceKey,
       "ctxResourceName": ctxResourceName,
       "ctxResourceDescr": ctxResourceDescr,
       "ctxResourceMgmtIPType": ctxResourceMgmtIPType,
       "ctxResourceMgmtIPAddr": ctxResourceMgmtIPAddr,
       "ctxResourceDeviceType": ctxResourceDeviceType,
       "ctxResourceRegionKeyRef1": ctxResourceRegionKeyRef1,
       "ctxSipConfigTable": ctxSipConfigTable,
       "ctxSipConfigEntry": ctxSipConfigEntry,
       "ctxSipIpType": ctxSipIpType,
       "ctxSipIpAddr": ctxSipIpAddr,
       "ctxSipPort": ctxSipPort,
       "ctxSipTransportProto": ctxSipTransportProto,
       "ctxMediaCapacityConfigTable": ctxMediaCapacityConfigTable,
       "ctxMediaCapacityConfigEntry": ctxMediaCapacityConfigEntry,
       "ctxMediaCapacityMaxPorts": ctxMediaCapacityMaxPorts,
       "ctxMediaCapacityLargeMeeting": ctxMediaCapacityLargeMeeting,
       "ctxMeetingConfigTable": ctxMeetingConfigTable,
       "ctxMeetingConfigEntry": ctxMeetingConfigEntry,
       "ctxMeetingConfigStaticMinId": ctxMeetingConfigStaticMinId,
       "ctxMeetingConfigStaticMaxId": ctxMeetingConfigStaticMaxId,
       "ctxMeetingConfigInterOpMinId": ctxMeetingConfigInterOpMinId,
       "ctxMeetingConfigInterOpMaxId": ctxMeetingConfigInterOpMaxId,
       "ctxClusterNodeTable": ctxClusterNodeTable,
       "ctxClusterNodeEntry": ctxClusterNodeEntry,
       "ctxClusterNodeIndex": ctxClusterNodeIndex,
       "ctxClusterNodeKey": ctxClusterNodeKey,
       "ctxClusterNodeName": ctxClusterNodeName,
       "ctxClusterNodeHostName": ctxClusterNodeHostName,
       "ctxClusterNodeIPType": ctxClusterNodeIPType,
       "ctxClusterNodeIPAddr": ctxClusterNodeIPAddr,
       "ctxClusterNodeClusterName": ctxClusterNodeClusterName,
       "ctxClusterNodeType": ctxClusterNodeType,
       "ctxClusterNodeOperState": ctxClusterNodeOperState,
       "ctxSystemStatusObjects": ctxSystemStatusObjects,
       "ctxAdminServersStatus": ctxAdminServersStatus,
       "ctxCallEnginesStatus": ctxCallEnginesStatus,
       "ctxDatabaseServersStatus": ctxDatabaseServersStatus,
       "ctxResourceStatus": ctxResourceStatus,
       "ctxSystemConfigStatus": ctxSystemConfigStatus,
       "ctxSystemBackupStatus": ctxSystemBackupStatus,
       "ctxStatisticsObjects": ctxStatisticsObjects,
       "ctxResourceStatsTable": ctxResourceStatsTable,
       "ctxResourceStatsEntry": ctxResourceStatsEntry,
       "ctxResourceOperState": ctxResourceOperState,
       "ctxResourceUnavailTrans": ctxResourceUnavailTrans,
       "ctxResourceUnavailDuration": ctxResourceUnavailDuration,
       "ctxResourceCallSetupFailures": ctxResourceCallSetupFailures,
       "ctxAllocStatsTable": ctxAllocStatsTable,
       "ctxAllocStatsEntry": ctxAllocStatsEntry,
       "ctxAllocActivePorts": ctxAllocActivePorts,
       "ctxAllocAvailPorts": ctxAllocAvailPorts,
       "ctxAllocFailures": ctxAllocFailures,
       "ctxAllocOutOfPorts": ctxAllocOutOfPorts,
       "ctxRegionStatsTable": ctxRegionStatsTable,
       "ctxRegionStatsEntry": ctxRegionStatsEntry,
       "ctxRegionCallSetupFailures": ctxRegionCallSetupFailures,
       "ctxAllocPoolActivePorts": ctxAllocPoolActivePorts,
       "ctxAllocPoolAvailPorts": ctxAllocPoolAvailPorts,
       "ctxAllocPoolAllocFailures": ctxAllocPoolAllocFailures,
       "ctxAllocPoolAllocOutOfPorts": ctxAllocPoolAllocOutOfPorts,
       "ctxAllocPeakHistory": ctxAllocPeakHistory,
       "ctxPeakHistMaxIntervals": ctxPeakHistMaxIntervals,
       "ctxPeakHistIntTime": ctxPeakHistIntTime,
       "ctxPeakHistAllocTable": ctxPeakHistAllocTable,
       "ctxPeakHistAllocEntry": ctxPeakHistAllocEntry,
       "ctxPeakHistAllocIntIndex": ctxPeakHistAllocIntIndex,
       "ctxPeakHistAllocTS": ctxPeakHistAllocTS,
       "ctxPeakHistAllocPorts": ctxPeakHistAllocPorts,
       "ctxPeakHistAllocPoolTable": ctxPeakHistAllocPoolTable,
       "ctxPeakHistAllocPoolEntry": ctxPeakHistAllocPoolEntry,
       "ctxPeakHistAllocPoolIntIndex": ctxPeakHistAllocPoolIntIndex,
       "ctxPeakHistAllocPoolTS": ctxPeakHistAllocPoolTS,
       "ctxPeakHistAllocPoolPorts": ctxPeakHistAllocPoolPorts,
       "ctxEventHistory": ctxEventHistory,
       "ctxErrorHistoryTableSize": ctxErrorHistoryTableSize,
       "ctxErrorHistoryMaxSeverity": ctxErrorHistoryMaxSeverity,
       "ctxErrorHistoryLastIndex": ctxErrorHistoryLastIndex,
       "ctxErrorHistoryTable": ctxErrorHistoryTable,
       "ctxErrorHistoryEntry": ctxErrorHistoryEntry,
       "ctxErrorIndex": ctxErrorIndex,
       "ctxErrorKey": ctxErrorKey,
       "ctxErrorTimeStamp": ctxErrorTimeStamp,
       "ctxErrorSeverity": ctxErrorSeverity,
       "ctxErrorAppName": ctxErrorAppName,
       "ctxErrorAlarmId": ctxErrorAlarmId,
       "ctxErrorAttrValStr": ctxErrorAttrValStr,
       "ctxErrorMessage": ctxErrorMessage,
       "ctxNotifyObjects": ctxNotifyObjects,
       "ctxNotifyMessage": ctxNotifyMessage,
       "ctxNotifyConfigObjects": ctxNotifyConfigObjects,
       "ctxStatusChangeNotifyEnable": ctxStatusChangeNotifyEnable,
       "ctxLicenseAlarmNotifyEnable": ctxLicenseAlarmNotifyEnable,
       "ctxAuthFailureNotifyEnable": ctxAuthFailureNotifyEnable,
       "ctxClusterNodeAlarmNotifyEnable": ctxClusterNodeAlarmNotifyEnable,
       "ctxResourceAlarmNotifyEnable": ctxResourceAlarmNotifyEnable,
       "ctxCallFailureNotifyEnable": ctxCallFailureNotifyEnable,
       "ctxErrorHistoryEventNotifyEnable": ctxErrorHistoryEventNotifyEnable,
       "ciscoTelepresenceExchangeSystemMIBConform": ciscoTelepresenceExchangeSystemMIBConform,
       "ciscoTelepresenceExchangeSystemMIBCompliances": ciscoTelepresenceExchangeSystemMIBCompliances,
       "ciscoTelepresenceExchangeSystemMIBModuleCompliance": ciscoTelepresenceExchangeSystemMIBModuleCompliance,
       "ciscoTelepresenceExchangeSystemMIBGroups": ciscoTelepresenceExchangeSystemMIBGroups,
       "ciscoTelepresenceExchangeSystemMIBStatusGroup": ciscoTelepresenceExchangeSystemMIBStatusGroup,
       "ciscoTelepresenceExchangeSystemMIBConfigGroup": ciscoTelepresenceExchangeSystemMIBConfigGroup,
       "ciscoTelePresenceExchangeSystemMIBStatsGroup": ciscoTelePresenceExchangeSystemMIBStatsGroup,
       "ciscoTelepresenceExchangeSystemMIBNotfyObjectsGroup": ciscoTelepresenceExchangeSystemMIBNotfyObjectsGroup,
       "ciscoTelepresenceExchangeSystemMIBErrorHistoryGroup": ciscoTelepresenceExchangeSystemMIBErrorHistoryGroup,
       "ciscoTelepresenceExchangeSystemMIBNotifyGroup": ciscoTelepresenceExchangeSystemMIBNotifyGroup}
)
