# SNMP MIB module (JUNIPER-TLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-TLB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:20 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType")

(jnxSDKApplicationsRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxSDKApplicationsRoot")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxTLBMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1)
)
jnxTLBMIB.setRevisions(
        ("2014-02-12 20:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxTLBrealServer_ObjectIdentity = ObjectIdentity
jnxTLBrealServer = _JnxTLBrealServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1)
)
_JnxTLBRealServerTable_Object = MibTable
jnxTLBRealServerTable = _JnxTLBRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxTLBRealServerTable.setStatus("current")
_JnxTLBRealServerEntry_Object = MibTableRow
jnxTLBRealServerEntry = _JnxTLBRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1)
)
jnxTLBRealServerEntry.setIndexNames(
    (0, "JUNIPER-TLB-MIB", "jnxTLBRealServerNameKey"),
)
if mibBuilder.loadTexts:
    jnxTLBRealServerEntry.setStatus("current")


class _JnxTLBRealServerNameKey_Type(DisplayString):
    """Custom type jnxTLBRealServerNameKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxTLBRealServerNameKey_Type.__name__ = "DisplayString"
_JnxTLBRealServerNameKey_Object = MibTableColumn
jnxTLBRealServerNameKey = _JnxTLBRealServerNameKey_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 1),
    _JnxTLBRealServerNameKey_Type()
)
jnxTLBRealServerNameKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTLBRealServerNameKey.setStatus("current")


class _JnxTLBRealServerName_Type(DisplayString):
    """Custom type jnxTLBRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBRealServerName_Type.__name__ = "DisplayString"
_JnxTLBRealServerName_Object = MibTableColumn
jnxTLBRealServerName = _JnxTLBRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 2),
    _JnxTLBRealServerName_Type()
)
jnxTLBRealServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRealServerName.setStatus("current")


class _JnxTLBRealServerInstance_Type(DisplayString):
    """Custom type jnxTLBRealServerInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBRealServerInstance_Type.__name__ = "DisplayString"
_JnxTLBRealServerInstance_Object = MibTableColumn
jnxTLBRealServerInstance = _JnxTLBRealServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 3),
    _JnxTLBRealServerInstance_Type()
)
jnxTLBRealServerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRealServerInstance.setStatus("current")


class _JnxTLBRealServerIPVersion_Type(Integer32):
    """Custom type jnxTLBRealServerIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_JnxTLBRealServerIPVersion_Type.__name__ = "Integer32"
_JnxTLBRealServerIPVersion_Object = MibTableColumn
jnxTLBRealServerIPVersion = _JnxTLBRealServerIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 4),
    _JnxTLBRealServerIPVersion_Type()
)
jnxTLBRealServerIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRealServerIPVersion.setStatus("current")


class _JnxTLBRealServerIP_Type(DisplayString):
    """Custom type jnxTLBRealServerIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBRealServerIP_Type.__name__ = "DisplayString"
_JnxTLBRealServerIP_Object = MibTableColumn
jnxTLBRealServerIP = _JnxTLBRealServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 5),
    _JnxTLBRealServerIP_Type()
)
jnxTLBRealServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRealServerIP.setStatus("current")


class _JnxTLBRealServerOperStatus_Type(Integer32):
    """Custom type jnxTLBRealServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_JnxTLBRealServerOperStatus_Type.__name__ = "Integer32"
_JnxTLBRealServerOperStatus_Object = MibTableColumn
jnxTLBRealServerOperStatus = _JnxTLBRealServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 6),
    _JnxTLBRealServerOperStatus_Type()
)
jnxTLBRealServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRealServerOperStatus.setStatus("current")


class _JnxTLBRealServerAdminStatus_Type(Integer32):
    """Custom type jnxTLBRealServerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_JnxTLBRealServerAdminStatus_Type.__name__ = "Integer32"
_JnxTLBRealServerAdminStatus_Object = MibTableColumn
jnxTLBRealServerAdminStatus = _JnxTLBRealServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 7),
    _JnxTLBRealServerAdminStatus_Type()
)
jnxTLBRealServerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRealServerAdminStatus.setStatus("current")
_JnxTLBRealServerSubUnitNo_Type = Unsigned32
_JnxTLBRealServerSubUnitNo_Object = MibTableColumn
jnxTLBRealServerSubUnitNo = _JnxTLBRealServerSubUnitNo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 8),
    _JnxTLBRealServerSubUnitNo_Type()
)
jnxTLBRealServerSubUnitNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRealServerSubUnitNo.setStatus("current")
_JnxTLBRealServerFailures_Type = Unsigned32
_JnxTLBRealServerFailures_Object = MibTableColumn
jnxTLBRealServerFailures = _JnxTLBRealServerFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 9),
    _JnxTLBRealServerFailures_Type()
)
jnxTLBRealServerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRealServerFailures.setStatus("current")
_JnxTLBRSClientPacketForwardCount_Type = Counter64
_JnxTLBRSClientPacketForwardCount_Object = MibTableColumn
jnxTLBRSClientPacketForwardCount = _JnxTLBRSClientPacketForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 10),
    _JnxTLBRSClientPacketForwardCount_Type()
)
jnxTLBRSClientPacketForwardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSClientPacketForwardCount.setStatus("current")
_JnxTLBRSClientByteForwardCount_Type = Counter64
_JnxTLBRSClientByteForwardCount_Object = MibTableColumn
jnxTLBRSClientByteForwardCount = _JnxTLBRSClientByteForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 11),
    _JnxTLBRSClientByteForwardCount_Type()
)
jnxTLBRSClientByteForwardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSClientByteForwardCount.setStatus("current")
_JnxTLBRSClientPacketReverseCount_Type = Counter64
_JnxTLBRSClientPacketReverseCount_Object = MibTableColumn
jnxTLBRSClientPacketReverseCount = _JnxTLBRSClientPacketReverseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 12),
    _JnxTLBRSClientPacketReverseCount_Type()
)
jnxTLBRSClientPacketReverseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSClientPacketReverseCount.setStatus("current")
_JnxTLBRSClientByteReverseCount_Type = Counter64
_JnxTLBRSClientByteReverseCount_Object = MibTableColumn
jnxTLBRSClientByteReverseCount = _JnxTLBRSClientByteReverseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 13),
    _JnxTLBRSClientByteReverseCount_Type()
)
jnxTLBRSClientByteReverseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSClientByteReverseCount.setStatus("current")
_JnxTLBRSTotalUpCount_Type = Unsigned32
_JnxTLBRSTotalUpCount_Object = MibTableColumn
jnxTLBRSTotalUpCount = _JnxTLBRSTotalUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 14),
    _JnxTLBRSTotalUpCount_Type()
)
jnxTLBRSTotalUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSTotalUpCount.setStatus("current")
_JnxTLBRSTotalDownCount_Type = Unsigned32
_JnxTLBRSTotalDownCount_Object = MibTableColumn
jnxTLBRSTotalDownCount = _JnxTLBRSTotalDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 15),
    _JnxTLBRSTotalDownCount_Type()
)
jnxTLBRSTotalDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSTotalDownCount.setStatus("current")
_JnxTLBRSTotalRejoinCount_Type = Unsigned32
_JnxTLBRSTotalRejoinCount_Object = MibTableColumn
jnxTLBRSTotalRejoinCount = _JnxTLBRSTotalRejoinCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 16),
    _JnxTLBRSTotalRejoinCount_Type()
)
jnxTLBRSTotalRejoinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSTotalRejoinCount.setStatus("current")
_JnxTLBRSTotalProbeSent_Type = Unsigned32
_JnxTLBRSTotalProbeSent_Object = MibTableColumn
jnxTLBRSTotalProbeSent = _JnxTLBRSTotalProbeSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 17),
    _JnxTLBRSTotalProbeSent_Type()
)
jnxTLBRSTotalProbeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSTotalProbeSent.setStatus("current")
_JnxTLBRSTotalProbeSuccess_Type = Unsigned32
_JnxTLBRSTotalProbeSuccess_Object = MibTableColumn
jnxTLBRSTotalProbeSuccess = _JnxTLBRSTotalProbeSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 18),
    _JnxTLBRSTotalProbeSuccess_Type()
)
jnxTLBRSTotalProbeSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSTotalProbeSuccess.setStatus("current")
_JnxTLBRSTotalProbeFail_Type = Unsigned32
_JnxTLBRSTotalProbeFail_Object = MibTableColumn
jnxTLBRSTotalProbeFail = _JnxTLBRSTotalProbeFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 19),
    _JnxTLBRSTotalProbeFail_Type()
)
jnxTLBRSTotalProbeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSTotalProbeFail.setStatus("current")
_JnxTLBRSTotalProbeSentFail_Type = Unsigned32
_JnxTLBRSTotalProbeSentFail_Object = MibTableColumn
jnxTLBRSTotalProbeSentFail = _JnxTLBRSTotalProbeSentFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 1, 1, 1, 20),
    _JnxTLBRSTotalProbeSentFail_Type()
)
jnxTLBRSTotalProbeSentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBRSTotalProbeSentFail.setStatus("current")
_JnxTLBvirtualService_ObjectIdentity = ObjectIdentity
jnxTLBvirtualService = _JnxTLBvirtualService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2)
)
_JnxTLBVirtualServiceTable_Object = MibTable
jnxTLBVirtualServiceTable = _JnxTLBVirtualServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceTable.setStatus("current")
_JnxTLBVirtualServiceEntry_Object = MibTableRow
jnxTLBVirtualServiceEntry = _JnxTLBVirtualServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1)
)
jnxTLBVirtualServiceEntry.setIndexNames(
    (0, "JUNIPER-TLB-MIB", "jnxTLBVirtualServiceNameKey"),
)
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceEntry.setStatus("current")


class _JnxTLBVirtualServiceNameKey_Type(DisplayString):
    """Custom type jnxTLBVirtualServiceNameKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxTLBVirtualServiceNameKey_Type.__name__ = "DisplayString"
_JnxTLBVirtualServiceNameKey_Object = MibTableColumn
jnxTLBVirtualServiceNameKey = _JnxTLBVirtualServiceNameKey_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 1),
    _JnxTLBVirtualServiceNameKey_Type()
)
jnxTLBVirtualServiceNameKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceNameKey.setStatus("current")


class _JnxTLBVirtualServiceName_Type(DisplayString):
    """Custom type jnxTLBVirtualServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBVirtualServiceName_Type.__name__ = "DisplayString"
_JnxTLBVirtualServiceName_Object = MibTableColumn
jnxTLBVirtualServiceName = _JnxTLBVirtualServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 2),
    _JnxTLBVirtualServiceName_Type()
)
jnxTLBVirtualServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceName.setStatus("current")


class _JnxTLBVirtualServiceTranslationMode_Type(DisplayString):
    """Custom type jnxTLBVirtualServiceTranslationMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBVirtualServiceTranslationMode_Type.__name__ = "DisplayString"
_JnxTLBVirtualServiceTranslationMode_Object = MibTableColumn
jnxTLBVirtualServiceTranslationMode = _JnxTLBVirtualServiceTranslationMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 3),
    _JnxTLBVirtualServiceTranslationMode_Type()
)
jnxTLBVirtualServiceTranslationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceTranslationMode.setStatus("current")


class _JnxTLBVirtualServiceInstance_Type(DisplayString):
    """Custom type jnxTLBVirtualServiceInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBVirtualServiceInstance_Type.__name__ = "DisplayString"
_JnxTLBVirtualServiceInstance_Object = MibTableColumn
jnxTLBVirtualServiceInstance = _JnxTLBVirtualServiceInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 4),
    _JnxTLBVirtualServiceInstance_Type()
)
jnxTLBVirtualServiceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceInstance.setStatus("current")


class _JnxTLBVirtualServiceIPVersion_Type(Integer32):
    """Custom type jnxTLBVirtualServiceIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_JnxTLBVirtualServiceIPVersion_Type.__name__ = "Integer32"
_JnxTLBVirtualServiceIPVersion_Object = MibTableColumn
jnxTLBVirtualServiceIPVersion = _JnxTLBVirtualServiceIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 5),
    _JnxTLBVirtualServiceIPVersion_Type()
)
jnxTLBVirtualServiceIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceIPVersion.setStatus("current")


class _JnxTLBVirtualServiceIP_Type(DisplayString):
    """Custom type jnxTLBVirtualServiceIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBVirtualServiceIP_Type.__name__ = "DisplayString"
_JnxTLBVirtualServiceIP_Object = MibTableColumn
jnxTLBVirtualServiceIP = _JnxTLBVirtualServiceIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 6),
    _JnxTLBVirtualServiceIP_Type()
)
jnxTLBVirtualServiceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceIP.setStatus("current")


class _JnxTLBVirtualServiceOperStatus_Type(Integer32):
    """Custom type jnxTLBVirtualServiceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_JnxTLBVirtualServiceOperStatus_Type.__name__ = "Integer32"
_JnxTLBVirtualServiceOperStatus_Object = MibTableColumn
jnxTLBVirtualServiceOperStatus = _JnxTLBVirtualServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 7),
    _JnxTLBVirtualServiceOperStatus_Type()
)
jnxTLBVirtualServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceOperStatus.setStatus("current")


class _JnxTLBVirtualServiceAdminStatus_Type(Integer32):
    """Custom type jnxTLBVirtualServiceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_JnxTLBVirtualServiceAdminStatus_Type.__name__ = "Integer32"
_JnxTLBVirtualServiceAdminStatus_Object = MibTableColumn
jnxTLBVirtualServiceAdminStatus = _JnxTLBVirtualServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 8),
    _JnxTLBVirtualServiceAdminStatus_Type()
)
jnxTLBVirtualServiceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceAdminStatus.setStatus("current")
_JnxTLBVirtualServiceSubUnitNo_Type = Unsigned32
_JnxTLBVirtualServiceSubUnitNo_Object = MibTableColumn
jnxTLBVirtualServiceSubUnitNo = _JnxTLBVirtualServiceSubUnitNo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 9),
    _JnxTLBVirtualServiceSubUnitNo_Type()
)
jnxTLBVirtualServiceSubUnitNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceSubUnitNo.setStatus("current")
_JnxTLBVirtualServiceFailures_Type = Unsigned32
_JnxTLBVirtualServiceFailures_Object = MibTableColumn
jnxTLBVirtualServiceFailures = _JnxTLBVirtualServiceFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 10),
    _JnxTLBVirtualServiceFailures_Type()
)
jnxTLBVirtualServiceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceFailures.setStatus("current")
_JnxTLBVSClientPacketForwardCount_Type = Counter64
_JnxTLBVSClientPacketForwardCount_Object = MibTableColumn
jnxTLBVSClientPacketForwardCount = _JnxTLBVSClientPacketForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 11),
    _JnxTLBVSClientPacketForwardCount_Type()
)
jnxTLBVSClientPacketForwardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVSClientPacketForwardCount.setStatus("current")
_JnxTLBVSClientByteForwardCount_Type = Counter64
_JnxTLBVSClientByteForwardCount_Object = MibTableColumn
jnxTLBVSClientByteForwardCount = _JnxTLBVSClientByteForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 12),
    _JnxTLBVSClientByteForwardCount_Type()
)
jnxTLBVSClientByteForwardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVSClientByteForwardCount.setStatus("current")
_JnxTLBVSClientPacketReverseCount_Type = Counter64
_JnxTLBVSClientPacketReverseCount_Object = MibTableColumn
jnxTLBVSClientPacketReverseCount = _JnxTLBVSClientPacketReverseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 13),
    _JnxTLBVSClientPacketReverseCount_Type()
)
jnxTLBVSClientPacketReverseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVSClientPacketReverseCount.setStatus("current")
_JnxTLBVSClientByteReverseCount_Type = Counter64
_JnxTLBVSClientByteReverseCount_Object = MibTableColumn
jnxTLBVSClientByteReverseCount = _JnxTLBVSClientByteReverseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 14),
    _JnxTLBVSClientByteReverseCount_Type()
)
jnxTLBVSClientByteReverseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVSClientByteReverseCount.setStatus("current")
_JnxTLBVSTotalUpCount_Type = Unsigned32
_JnxTLBVSTotalUpCount_Object = MibTableColumn
jnxTLBVSTotalUpCount = _JnxTLBVSTotalUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 15),
    _JnxTLBVSTotalUpCount_Type()
)
jnxTLBVSTotalUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVSTotalUpCount.setStatus("current")
_JnxTLBVSTotalDownCount_Type = Unsigned32
_JnxTLBVSTotalDownCount_Object = MibTableColumn
jnxTLBVSTotalDownCount = _JnxTLBVSTotalDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 16),
    _JnxTLBVSTotalDownCount_Type()
)
jnxTLBVSTotalDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVSTotalDownCount.setStatus("current")
_JnxTLBVSTotalRealServerCount_Type = Unsigned32
_JnxTLBVSTotalRealServerCount_Object = MibTableColumn
jnxTLBVSTotalRealServerCount = _JnxTLBVSTotalRealServerCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 17),
    _JnxTLBVSTotalRealServerCount_Type()
)
jnxTLBVSTotalRealServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVSTotalRealServerCount.setStatus("current")
_JnxTLBVSServiceUpTime_Type = DisplayString
_JnxTLBVSServiceUpTime_Object = MibTableColumn
jnxTLBVSServiceUpTime = _JnxTLBVSServiceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 18),
    _JnxTLBVSServiceUpTime_Type()
)
jnxTLBVSServiceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVSServiceUpTime.setStatus("current")
_JnxTLBVSActiveRealServerCount_Type = Unsigned32
_JnxTLBVSActiveRealServerCount_Object = MibTableColumn
jnxTLBVSActiveRealServerCount = _JnxTLBVSActiveRealServerCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 19),
    _JnxTLBVSActiveRealServerCount_Type()
)
jnxTLBVSActiveRealServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVSActiveRealServerCount.setStatus("current")
_JnxTLBVSNetworkMonitorProfileCount_Type = Unsigned32
_JnxTLBVSNetworkMonitorProfileCount_Object = MibTableColumn
jnxTLBVSNetworkMonitorProfileCount = _JnxTLBVSNetworkMonitorProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 20),
    _JnxTLBVSNetworkMonitorProfileCount_Type()
)
jnxTLBVSNetworkMonitorProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVSNetworkMonitorProfileCount.setStatus("current")
_JnxTLBVirtualServiceVirtualPort_Type = Unsigned32
_JnxTLBVirtualServiceVirtualPort_Object = MibTableColumn
jnxTLBVirtualServiceVirtualPort = _JnxTLBVirtualServiceVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 21),
    _JnxTLBVirtualServiceVirtualPort_Type()
)
jnxTLBVirtualServiceVirtualPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceVirtualPort.setStatus("current")
_JnxTLBVirtualServiceRealPort_Type = Unsigned32
_JnxTLBVirtualServiceRealPort_Object = MibTableColumn
jnxTLBVirtualServiceRealPort = _JnxTLBVirtualServiceRealPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 22),
    _JnxTLBVirtualServiceRealPort_Type()
)
jnxTLBVirtualServiceRealPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceRealPort.setStatus("current")
_JnxTLBVirtualServiceNextHopIndex_Type = Unsigned32
_JnxTLBVirtualServiceNextHopIndex_Object = MibTableColumn
jnxTLBVirtualServiceNextHopIndex = _JnxTLBVirtualServiceNextHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 23),
    _JnxTLBVirtualServiceNextHopIndex_Type()
)
jnxTLBVirtualServiceNextHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceNextHopIndex.setStatus("current")
_JnxTLBVirtualServiceProtocol_Type = DisplayString
_JnxTLBVirtualServiceProtocol_Object = MibTableColumn
jnxTLBVirtualServiceProtocol = _JnxTLBVirtualServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 24),
    _JnxTLBVirtualServiceProtocol_Type()
)
jnxTLBVirtualServiceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceProtocol.setStatus("current")
_JnxTLBVirtualServiceDemuxNextHopIndex_Type = Unsigned32
_JnxTLBVirtualServiceDemuxNextHopIndex_Object = MibTableColumn
jnxTLBVirtualServiceDemuxNextHopIndex = _JnxTLBVirtualServiceDemuxNextHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 25),
    _JnxTLBVirtualServiceDemuxNextHopIndex_Type()
)
jnxTLBVirtualServiceDemuxNextHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceDemuxNextHopIndex.setStatus("current")


class _JnxTLBVirtualServiceInterface_Type(DisplayString):
    """Custom type jnxTLBVirtualServiceInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBVirtualServiceInterface_Type.__name__ = "DisplayString"
_JnxTLBVirtualServiceInterface_Object = MibTableColumn
jnxTLBVirtualServiceInterface = _JnxTLBVirtualServiceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 26),
    _JnxTLBVirtualServiceInterface_Type()
)
jnxTLBVirtualServiceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceInterface.setStatus("current")


class _JnxTLBVirtualServiceRoutingInstance_Type(DisplayString):
    """Custom type jnxTLBVirtualServiceRoutingInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBVirtualServiceRoutingInstance_Type.__name__ = "DisplayString"
_JnxTLBVirtualServiceRoutingInstance_Object = MibTableColumn
jnxTLBVirtualServiceRoutingInstance = _JnxTLBVirtualServiceRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 27),
    _JnxTLBVirtualServiceRoutingInstance_Type()
)
jnxTLBVirtualServiceRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceRoutingInstance.setStatus("current")
_JnxTLBVirtualServiceHashMethod_Type = DisplayString
_JnxTLBVirtualServiceHashMethod_Object = MibTableColumn
jnxTLBVirtualServiceHashMethod = _JnxTLBVirtualServiceHashMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 28),
    _JnxTLBVirtualServiceHashMethod_Type()
)
jnxTLBVirtualServiceHashMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceHashMethod.setStatus("current")
_JnxTLBVirtualServiceRouteMetric_Type = Unsigned32
_JnxTLBVirtualServiceRouteMetric_Object = MibTableColumn
jnxTLBVirtualServiceRouteMetric = _JnxTLBVirtualServiceRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 29),
    _JnxTLBVirtualServiceRouteMetric_Type()
)
jnxTLBVirtualServiceRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceRouteMetric.setStatus("current")


class _JnxTLBVirtualServiceAutoRejoin_Type(Integer32):
    """Custom type jnxTLBVirtualServiceAutoRejoin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 0))
    )


_JnxTLBVirtualServiceAutoRejoin_Type.__name__ = "Integer32"
_JnxTLBVirtualServiceAutoRejoin_Object = MibTableColumn
jnxTLBVirtualServiceAutoRejoin = _JnxTLBVirtualServiceAutoRejoin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 30),
    _JnxTLBVirtualServiceAutoRejoin_Type()
)
jnxTLBVirtualServiceAutoRejoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceAutoRejoin.setStatus("current")


class _JnxTLBVirtualServiceRouteHoldTimer_Type(Integer32):
    """Custom type jnxTLBVirtualServiceRouteHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxTLBVirtualServiceRouteHoldTimer_Type.__name__ = "Integer32"
_JnxTLBVirtualServiceRouteHoldTimer_Object = MibTableColumn
jnxTLBVirtualServiceRouteHoldTimer = _JnxTLBVirtualServiceRouteHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 31),
    _JnxTLBVirtualServiceRouteHoldTimer_Type()
)
jnxTLBVirtualServiceRouteHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceRouteHoldTimer.setStatus("current")


class _JnxTLBVirtualServiceWarmUpTime_Type(Integer32):
    """Custom type jnxTLBVirtualServiceWarmUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxTLBVirtualServiceWarmUpTime_Type.__name__ = "Integer32"
_JnxTLBVirtualServiceWarmUpTime_Object = MibTableColumn
jnxTLBVirtualServiceWarmUpTime = _JnxTLBVirtualServiceWarmUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 2, 1, 1, 32),
    _JnxTLBVirtualServiceWarmUpTime_Type()
)
jnxTLBVirtualServiceWarmUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBVirtualServiceWarmUpTime.setStatus("current")
_JnxTLBserverGroup_ObjectIdentity = ObjectIdentity
jnxTLBserverGroup = _JnxTLBserverGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3)
)
_JnxTLBServerGroupTable_Object = MibTable
jnxTLBServerGroupTable = _JnxTLBServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxTLBServerGroupTable.setStatus("current")
_JnxTLBServerGroupEntry_Object = MibTableRow
jnxTLBServerGroupEntry = _JnxTLBServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1)
)
jnxTLBServerGroupEntry.setIndexNames(
    (0, "JUNIPER-TLB-MIB", "jnxTLBServerGroupNameKey"),
)
if mibBuilder.loadTexts:
    jnxTLBServerGroupEntry.setStatus("current")


class _JnxTLBServerGroupNameKey_Type(DisplayString):
    """Custom type jnxTLBServerGroupNameKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxTLBServerGroupNameKey_Type.__name__ = "DisplayString"
_JnxTLBServerGroupNameKey_Object = MibTableColumn
jnxTLBServerGroupNameKey = _JnxTLBServerGroupNameKey_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 1),
    _JnxTLBServerGroupNameKey_Type()
)
jnxTLBServerGroupNameKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTLBServerGroupNameKey.setStatus("current")


class _JnxTLBServerGroupName_Type(DisplayString):
    """Custom type jnxTLBServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBServerGroupName_Type.__name__ = "DisplayString"
_JnxTLBServerGroupName_Object = MibTableColumn
jnxTLBServerGroupName = _JnxTLBServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 2),
    _JnxTLBServerGroupName_Type()
)
jnxTLBServerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBServerGroupName.setStatus("current")
_JnxTLBServerGroupInstance_Type = DisplayString
_JnxTLBServerGroupInstance_Object = MibTableColumn
jnxTLBServerGroupInstance = _JnxTLBServerGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 3),
    _JnxTLBServerGroupInstance_Type()
)
jnxTLBServerGroupInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBServerGroupInstance.setStatus("current")


class _JnxTLBServerGroupIPVersion_Type(Integer32):
    """Custom type jnxTLBServerGroupIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_JnxTLBServerGroupIPVersion_Type.__name__ = "Integer32"
_JnxTLBServerGroupIPVersion_Object = MibTableColumn
jnxTLBServerGroupIPVersion = _JnxTLBServerGroupIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 4),
    _JnxTLBServerGroupIPVersion_Type()
)
jnxTLBServerGroupIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBServerGroupIPVersion.setStatus("current")


class _JnxTLBServerGroupOperStatus_Type(Integer32):
    """Custom type jnxTLBServerGroupOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_JnxTLBServerGroupOperStatus_Type.__name__ = "Integer32"
_JnxTLBServerGroupOperStatus_Object = MibTableColumn
jnxTLBServerGroupOperStatus = _JnxTLBServerGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 5),
    _JnxTLBServerGroupOperStatus_Type()
)
jnxTLBServerGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBServerGroupOperStatus.setStatus("current")


class _JnxTLBServerGroupAdminStatus_Type(Integer32):
    """Custom type jnxTLBServerGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_JnxTLBServerGroupAdminStatus_Type.__name__ = "Integer32"
_JnxTLBServerGroupAdminStatus_Object = MibTableColumn
jnxTLBServerGroupAdminStatus = _JnxTLBServerGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 6),
    _JnxTLBServerGroupAdminStatus_Type()
)
jnxTLBServerGroupAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBServerGroupAdminStatus.setStatus("current")
_JnxTLBServerGroupFailures_Type = Unsigned32
_JnxTLBServerGroupFailures_Object = MibTableColumn
jnxTLBServerGroupFailures = _JnxTLBServerGroupFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 7),
    _JnxTLBServerGroupFailures_Type()
)
jnxTLBServerGroupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBServerGroupFailures.setStatus("current")
_JnxTLBServerGroupLastTimeUp_Type = DisplayString
_JnxTLBServerGroupLastTimeUp_Object = MibTableColumn
jnxTLBServerGroupLastTimeUp = _JnxTLBServerGroupLastTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 8),
    _JnxTLBServerGroupLastTimeUp_Type()
)
jnxTLBServerGroupLastTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBServerGroupLastTimeUp.setStatus("current")
_JnxTLBServerGroupLastTimeDown_Type = DisplayString
_JnxTLBServerGroupLastTimeDown_Object = MibTableColumn
jnxTLBServerGroupLastTimeDown = _JnxTLBServerGroupLastTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 9),
    _JnxTLBServerGroupLastTimeDown_Type()
)
jnxTLBServerGroupLastTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBServerGroupLastTimeDown.setStatus("current")
_JnxTLBServerGroupTotalUpCount_Type = Unsigned32
_JnxTLBServerGroupTotalUpCount_Object = MibTableColumn
jnxTLBServerGroupTotalUpCount = _JnxTLBServerGroupTotalUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 10),
    _JnxTLBServerGroupTotalUpCount_Type()
)
jnxTLBServerGroupTotalUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBServerGroupTotalUpCount.setStatus("current")
_JnxTLBServerGroupTotalDownCount_Type = Unsigned32
_JnxTLBServerGroupTotalDownCount_Object = MibTableColumn
jnxTLBServerGroupTotalDownCount = _JnxTLBServerGroupTotalDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 3, 1, 1, 11),
    _JnxTLBServerGroupTotalDownCount_Type()
)
jnxTLBServerGroupTotalDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBServerGroupTotalDownCount.setStatus("current")
_TlbDataMib_ObjectIdentity = ObjectIdentity
tlbDataMib = _TlbDataMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    tlbDataMib.setStatus("current")
_TlbTrapMib_ObjectIdentity = ObjectIdentity
tlbTrapMib = _TlbTrapMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5)
)
if mibBuilder.loadTexts:
    tlbTrapMib.setStatus("current")
_TlbNotificationObjMib_ObjectIdentity = ObjectIdentity
tlbNotificationObjMib = _TlbNotificationObjMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3)
)
_TlbInstanceName_Type = OctetString
_TlbInstanceName_Object = MibScalar
tlbInstanceName = _TlbInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1001),
    _TlbInstanceName_Type()
)
tlbInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbInstanceName.setStatus("current")
_TlbRealServerName_Type = OctetString
_TlbRealServerName_Object = MibScalar
tlbRealServerName = _TlbRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1002),
    _TlbRealServerName_Type()
)
tlbRealServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbRealServerName.setStatus("current")
_TlbRealServerGroupName_Type = OctetString
_TlbRealServerGroupName_Object = MibScalar
tlbRealServerGroupName = _TlbRealServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1003),
    _TlbRealServerGroupName_Type()
)
tlbRealServerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbRealServerGroupName.setStatus("current")
_TlbRealServerIpAddress_Type = OctetString
_TlbRealServerIpAddress_Object = MibScalar
tlbRealServerIpAddress = _TlbRealServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1004),
    _TlbRealServerIpAddress_Type()
)
tlbRealServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbRealServerIpAddress.setStatus("current")
_TlbVirtualServiceName_Type = OctetString
_TlbVirtualServiceName_Object = MibScalar
tlbVirtualServiceName = _TlbVirtualServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1005),
    _TlbVirtualServiceName_Type()
)
tlbVirtualServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbVirtualServiceName.setStatus("current")
_TlbVirtualServiceIpAddr_Type = OctetString
_TlbVirtualServiceIpAddr_Object = MibScalar
tlbVirtualServiceIpAddr = _TlbVirtualServiceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1006),
    _TlbVirtualServiceIpAddr_Type()
)
tlbVirtualServiceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbVirtualServiceIpAddr.setStatus("current")


class _TlbVirtualServicePort_Type(Integer32):
    """Custom type tlbVirtualServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TlbVirtualServicePort_Type.__name__ = "Integer32"
_TlbVirtualServicePort_Object = MibScalar
tlbVirtualServicePort = _TlbVirtualServicePort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1007),
    _TlbVirtualServicePort_Type()
)
tlbVirtualServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbVirtualServicePort.setStatus("current")
_TlbProfileName_Type = OctetString
_TlbProfileName_Object = MibScalar
tlbProfileName = _TlbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1008),
    _TlbProfileName_Type()
)
tlbProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbProfileName.setStatus("current")
_TlbMultiserviceInterface_Type = OctetString
_TlbMultiserviceInterface_Object = MibScalar
tlbMultiserviceInterface = _TlbMultiserviceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1009),
    _TlbMultiserviceInterface_Type()
)
tlbMultiserviceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbMultiserviceInterface.setStatus("current")


class _TlbMultiServicePIC_Type(Integer32):
    """Custom type tlbMultiServicePIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TlbMultiServicePIC_Type.__name__ = "Integer32"
_TlbMultiServicePIC_Object = MibScalar
tlbMultiServicePIC = _TlbMultiServicePIC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1010),
    _TlbMultiServicePIC_Type()
)
tlbMultiServicePIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbMultiServicePIC.setStatus("current")
_TlbNetmonCpuUsage_Type = Unsigned32
_TlbNetmonCpuUsage_Object = MibScalar
tlbNetmonCpuUsage = _TlbNetmonCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1011),
    _TlbNetmonCpuUsage_Type()
)
tlbNetmonCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbNetmonCpuUsage.setStatus("current")
_TlbMonitorMode_Type = OctetString
_TlbMonitorMode_Object = MibScalar
tlbMonitorMode = _TlbMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 3, 1099),
    _TlbMonitorMode_Type()
)
tlbMonitorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlbMonitorMode.setStatus("current")
_TlbNotificationMib_ObjectIdentity = ObjectIdentity
tlbNotificationMib = _TlbNotificationMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4)
)
_JnxTLBNetworkMonitorProfile_ObjectIdentity = ObjectIdentity
jnxTLBNetworkMonitorProfile = _JnxTLBNetworkMonitorProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6)
)
_JnxTLBNetworkMonitorProfileTable_Object = MibTable
jnxTLBNetworkMonitorProfileTable = _JnxTLBNetworkMonitorProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1)
)
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileTable.setStatus("current")
_JnxTLBNetworkMonitorProfileEntry_Object = MibTableRow
jnxTLBNetworkMonitorProfileEntry = _JnxTLBNetworkMonitorProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1)
)
jnxTLBNetworkMonitorProfileEntry.setIndexNames(
    (0, "JUNIPER-TLB-MIB", "jnxTLBNetworkMonitorProfileNameKey"),
)
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileEntry.setStatus("current")


class _JnxTLBNetworkMonitorProfileNameKey_Type(DisplayString):
    """Custom type jnxTLBNetworkMonitorProfileNameKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxTLBNetworkMonitorProfileNameKey_Type.__name__ = "DisplayString"
_JnxTLBNetworkMonitorProfileNameKey_Object = MibTableColumn
jnxTLBNetworkMonitorProfileNameKey = _JnxTLBNetworkMonitorProfileNameKey_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 1),
    _JnxTLBNetworkMonitorProfileNameKey_Type()
)
jnxTLBNetworkMonitorProfileNameKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileNameKey.setStatus("current")


class _JnxTLBNetworkMonitorProfileVirtualServiceName_Type(DisplayString):
    """Custom type jnxTLBNetworkMonitorProfileVirtualServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBNetworkMonitorProfileVirtualServiceName_Type.__name__ = "DisplayString"
_JnxTLBNetworkMonitorProfileVirtualServiceName_Object = MibTableColumn
jnxTLBNetworkMonitorProfileVirtualServiceName = _JnxTLBNetworkMonitorProfileVirtualServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 2),
    _JnxTLBNetworkMonitorProfileVirtualServiceName_Type()
)
jnxTLBNetworkMonitorProfileVirtualServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileVirtualServiceName.setStatus("current")


class _JnxTLBNetworkMonitorProfileRealServerName_Type(DisplayString):
    """Custom type jnxTLBNetworkMonitorProfileRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBNetworkMonitorProfileRealServerName_Type.__name__ = "DisplayString"
_JnxTLBNetworkMonitorProfileRealServerName_Object = MibTableColumn
jnxTLBNetworkMonitorProfileRealServerName = _JnxTLBNetworkMonitorProfileRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 3),
    _JnxTLBNetworkMonitorProfileRealServerName_Type()
)
jnxTLBNetworkMonitorProfileRealServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileRealServerName.setStatus("current")
_JnxTLBNetworkMonitorProfileIndex_Type = Unsigned32
_JnxTLBNetworkMonitorProfileIndex_Object = MibTableColumn
jnxTLBNetworkMonitorProfileIndex = _JnxTLBNetworkMonitorProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 4),
    _JnxTLBNetworkMonitorProfileIndex_Type()
)
jnxTLBNetworkMonitorProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileIndex.setStatus("current")


class _JnxTLBNetworkMonitorProfileName_Type(DisplayString):
    """Custom type jnxTLBNetworkMonitorProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBNetworkMonitorProfileName_Type.__name__ = "DisplayString"
_JnxTLBNetworkMonitorProfileName_Object = MibTableColumn
jnxTLBNetworkMonitorProfileName = _JnxTLBNetworkMonitorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 5),
    _JnxTLBNetworkMonitorProfileName_Type()
)
jnxTLBNetworkMonitorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileName.setStatus("current")


class _JnxTLBNetworkMonitorProfileType_Type(DisplayString):
    """Custom type jnxTLBNetworkMonitorProfileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxTLBNetworkMonitorProfileType_Type.__name__ = "DisplayString"
_JnxTLBNetworkMonitorProfileType_Object = MibTableColumn
jnxTLBNetworkMonitorProfileType = _JnxTLBNetworkMonitorProfileType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 6),
    _JnxTLBNetworkMonitorProfileType_Type()
)
jnxTLBNetworkMonitorProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileType.setStatus("current")
_JnxTLBNetworkMonitorProfileProbeInterval_Type = Unsigned32
_JnxTLBNetworkMonitorProfileProbeInterval_Object = MibTableColumn
jnxTLBNetworkMonitorProfileProbeInterval = _JnxTLBNetworkMonitorProfileProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 7),
    _JnxTLBNetworkMonitorProfileProbeInterval_Type()
)
jnxTLBNetworkMonitorProfileProbeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileProbeInterval.setStatus("current")
_JnxTLBNetworkMonitorProfileFailureRetry_Type = Unsigned32
_JnxTLBNetworkMonitorProfileFailureRetry_Object = MibTableColumn
jnxTLBNetworkMonitorProfileFailureRetry = _JnxTLBNetworkMonitorProfileFailureRetry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 8),
    _JnxTLBNetworkMonitorProfileFailureRetry_Type()
)
jnxTLBNetworkMonitorProfileFailureRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileFailureRetry.setStatus("current")
_JnxTLBNetworkMonitorProfileRecoverRetry_Type = Unsigned32
_JnxTLBNetworkMonitorProfileRecoverRetry_Object = MibTableColumn
jnxTLBNetworkMonitorProfileRecoverRetry = _JnxTLBNetworkMonitorProfileRecoverRetry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 9),
    _JnxTLBNetworkMonitorProfileRecoverRetry_Type()
)
jnxTLBNetworkMonitorProfileRecoverRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileRecoverRetry.setStatus("current")
_JnxTLBNetworkMonitorProfilePortNumber_Type = Unsigned32
_JnxTLBNetworkMonitorProfilePortNumber_Object = MibTableColumn
jnxTLBNetworkMonitorProfilePortNumber = _JnxTLBNetworkMonitorProfilePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 10),
    _JnxTLBNetworkMonitorProfilePortNumber_Type()
)
jnxTLBNetworkMonitorProfilePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfilePortNumber.setStatus("current")


class _JnxTLBNetworkMonitorProfileProbeState_Type(Integer32):
    """Custom type jnxTLBNetworkMonitorProfileProbeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("probeStateDown", 2),
          ("probeStateUp", 1))
    )


_JnxTLBNetworkMonitorProfileProbeState_Type.__name__ = "Integer32"
_JnxTLBNetworkMonitorProfileProbeState_Object = MibTableColumn
jnxTLBNetworkMonitorProfileProbeState = _JnxTLBNetworkMonitorProfileProbeState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 11),
    _JnxTLBNetworkMonitorProfileProbeState_Type()
)
jnxTLBNetworkMonitorProfileProbeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileProbeState.setStatus("current")
_JnxTLBNetworkMonitorProfileProbeSent_Type = Unsigned32
_JnxTLBNetworkMonitorProfileProbeSent_Object = MibTableColumn
jnxTLBNetworkMonitorProfileProbeSent = _JnxTLBNetworkMonitorProfileProbeSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 12),
    _JnxTLBNetworkMonitorProfileProbeSent_Type()
)
jnxTLBNetworkMonitorProfileProbeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileProbeSent.setStatus("current")
_JnxTLBNetworkMonitorProfileProbeSuccess_Type = Unsigned32
_JnxTLBNetworkMonitorProfileProbeSuccess_Object = MibTableColumn
jnxTLBNetworkMonitorProfileProbeSuccess = _JnxTLBNetworkMonitorProfileProbeSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 13),
    _JnxTLBNetworkMonitorProfileProbeSuccess_Type()
)
jnxTLBNetworkMonitorProfileProbeSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileProbeSuccess.setStatus("current")
_JnxTLBNetworkMonitorProfileProbeFail_Type = Unsigned32
_JnxTLBNetworkMonitorProfileProbeFail_Object = MibTableColumn
jnxTLBNetworkMonitorProfileProbeFail = _JnxTLBNetworkMonitorProfileProbeFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 14),
    _JnxTLBNetworkMonitorProfileProbeFail_Type()
)
jnxTLBNetworkMonitorProfileProbeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileProbeFail.setStatus("current")
_JnxTLBNetworkMonitorProfileProbeConsecutiveSuccess_Type = Unsigned32
_JnxTLBNetworkMonitorProfileProbeConsecutiveSuccess_Object = MibTableColumn
jnxTLBNetworkMonitorProfileProbeConsecutiveSuccess = _JnxTLBNetworkMonitorProfileProbeConsecutiveSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 15),
    _JnxTLBNetworkMonitorProfileProbeConsecutiveSuccess_Type()
)
jnxTLBNetworkMonitorProfileProbeConsecutiveSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileProbeConsecutiveSuccess.setStatus("current")
_JnxTLBNetworkMonitorProfileProbeConsecutiveFail_Type = Unsigned32
_JnxTLBNetworkMonitorProfileProbeConsecutiveFail_Object = MibTableColumn
jnxTLBNetworkMonitorProfileProbeConsecutiveFail = _JnxTLBNetworkMonitorProfileProbeConsecutiveFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 6, 1, 1, 16),
    _JnxTLBNetworkMonitorProfileProbeConsecutiveFail_Type()
)
jnxTLBNetworkMonitorProfileProbeConsecutiveFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTLBNetworkMonitorProfileProbeConsecutiveFail.setStatus("current")

# Managed Objects groups


# Notification objects

tlbRealServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 1)
)
tlbRealServerUp.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbInstanceName"),
        ("JUNIPER-TLB-MIB", "tlbRealServerName"),
        ("JUNIPER-TLB-MIB", "tlbRealServerIpAddress"),
        ("JUNIPER-TLB-MIB", "tlbRealServerGroupName"),
        ("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbRealServerUp.setStatus(
        "current"
    )

tlbRealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 2)
)
tlbRealServerDown.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbInstanceName"),
        ("JUNIPER-TLB-MIB", "tlbRealServerName"),
        ("JUNIPER-TLB-MIB", "tlbRealServerIpAddress"),
        ("JUNIPER-TLB-MIB", "tlbRealServerGroupName"),
        ("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbRealServerDown.setStatus(
        "current"
    )

tlbRealServerRejoined = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 3)
)
tlbRealServerRejoined.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbInstanceName"),
        ("JUNIPER-TLB-MIB", "tlbRealServerName"),
        ("JUNIPER-TLB-MIB", "tlbRealServerIpAddress"),
        ("JUNIPER-TLB-MIB", "tlbRealServerGroupName"),
        ("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbRealServerRejoined.setStatus(
        "current"
    )

tlbVirtualServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 5)
)
tlbVirtualServiceUp.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbInstanceName"),
        ("JUNIPER-TLB-MIB", "tlbVirtualServiceName"),
        ("JUNIPER-TLB-MIB", "tlbVirtualServiceIpAddr"),
        ("JUNIPER-TLB-MIB", "tlbRealServerGroupName"),
        ("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbVirtualServiceUp.setStatus(
        "current"
    )

tlbVirtualServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 6)
)
tlbVirtualServiceDown.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbInstanceName"),
        ("JUNIPER-TLB-MIB", "tlbVirtualServiceName"),
        ("JUNIPER-TLB-MIB", "tlbVirtualServiceIpAddr"),
        ("JUNIPER-TLB-MIB", "tlbRealServerGroupName"),
        ("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbVirtualServiceDown.setStatus(
        "current"
    )

tlbRealServerServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 7)
)
tlbRealServerServiceUp.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbInstanceName"),
        ("JUNIPER-TLB-MIB", "tlbRealServerName"),
        ("JUNIPER-TLB-MIB", "tlbRealServerIpAddress"),
        ("JUNIPER-TLB-MIB", "tlbRealServerGroupName"),
        ("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbRealServerServiceUp.setStatus(
        "current"
    )

tlbRealServerServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 8)
)
tlbRealServerServiceDown.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbInstanceName"),
        ("JUNIPER-TLB-MIB", "tlbRealServerName"),
        ("JUNIPER-TLB-MIB", "tlbRealServerIpAddress"),
        ("JUNIPER-TLB-MIB", "tlbRealServerGroupName"),
        ("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbRealServerServiceDown.setStatus(
        "current"
    )

tlbVirtualServerServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 9)
)
tlbVirtualServerServiceUp.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbInstanceName"),
        ("JUNIPER-TLB-MIB", "tlbVirtualServiceName"),
        ("JUNIPER-TLB-MIB", "tlbVirtualServiceIpAddr"),
        ("JUNIPER-TLB-MIB", "tlbRealServerGroupName"),
        ("JUNIPER-TLB-MIB", "tlbVirtualServicePort"),
        ("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbVirtualServerServiceUp.setStatus(
        "current"
    )

tlbVirtualServerServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 10)
)
tlbVirtualServerServiceDown.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbInstanceName"),
        ("JUNIPER-TLB-MIB", "tlbVirtualServiceName"),
        ("JUNIPER-TLB-MIB", "tlbVirtualServiceIpAddr"),
        ("JUNIPER-TLB-MIB", "tlbRealServerGroupName"),
        ("JUNIPER-TLB-MIB", "tlbVirtualServicePort"),
        ("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbVirtualServerServiceDown.setStatus(
        "current"
    )

tlbUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 11)
)
tlbUp.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbUp.setStatus(
        "current"
    )

tlbShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 12)
)
tlbShutdown.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbShutdown.setStatus(
        "current"
    )

tlbPicConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 13)
)
tlbPicConnected.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("JUNIPER-TLB-MIB", "tlbMultiserviceInterface"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbPicConnected.setStatus(
        "current"
    )

tlbPicDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 14)
)
tlbPicDisconnected.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("JUNIPER-TLB-MIB", "tlbMultiserviceInterface"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbPicDisconnected.setStatus(
        "current"
    )

tlbCpuHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 15)
)
tlbCpuHigh.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("JUNIPER-TLB-MIB", "tlbNetmonCpuUsage"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbCpuHigh.setStatus(
        "current"
    )

tlbCpuNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 16)
)
tlbCpuNormal.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("JUNIPER-TLB-MIB", "tlbNetmonCpuUsage"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbCpuNormal.setStatus(
        "current"
    )

tlbUnlicensedPic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7, 1, 5, 4, 17)
)
tlbUnlicensedPic.setObjects(
      *(("JUNIPER-TLB-MIB", "tlbMonitorMode"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    tlbUnlicensedPic.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-TLB-MIB",
    **{"jnxTLBMIB": jnxTLBMIB,
       "jnxTLBrealServer": jnxTLBrealServer,
       "jnxTLBRealServerTable": jnxTLBRealServerTable,
       "jnxTLBRealServerEntry": jnxTLBRealServerEntry,
       "jnxTLBRealServerNameKey": jnxTLBRealServerNameKey,
       "jnxTLBRealServerName": jnxTLBRealServerName,
       "jnxTLBRealServerInstance": jnxTLBRealServerInstance,
       "jnxTLBRealServerIPVersion": jnxTLBRealServerIPVersion,
       "jnxTLBRealServerIP": jnxTLBRealServerIP,
       "jnxTLBRealServerOperStatus": jnxTLBRealServerOperStatus,
       "jnxTLBRealServerAdminStatus": jnxTLBRealServerAdminStatus,
       "jnxTLBRealServerSubUnitNo": jnxTLBRealServerSubUnitNo,
       "jnxTLBRealServerFailures": jnxTLBRealServerFailures,
       "jnxTLBRSClientPacketForwardCount": jnxTLBRSClientPacketForwardCount,
       "jnxTLBRSClientByteForwardCount": jnxTLBRSClientByteForwardCount,
       "jnxTLBRSClientPacketReverseCount": jnxTLBRSClientPacketReverseCount,
       "jnxTLBRSClientByteReverseCount": jnxTLBRSClientByteReverseCount,
       "jnxTLBRSTotalUpCount": jnxTLBRSTotalUpCount,
       "jnxTLBRSTotalDownCount": jnxTLBRSTotalDownCount,
       "jnxTLBRSTotalRejoinCount": jnxTLBRSTotalRejoinCount,
       "jnxTLBRSTotalProbeSent": jnxTLBRSTotalProbeSent,
       "jnxTLBRSTotalProbeSuccess": jnxTLBRSTotalProbeSuccess,
       "jnxTLBRSTotalProbeFail": jnxTLBRSTotalProbeFail,
       "jnxTLBRSTotalProbeSentFail": jnxTLBRSTotalProbeSentFail,
       "jnxTLBvirtualService": jnxTLBvirtualService,
       "jnxTLBVirtualServiceTable": jnxTLBVirtualServiceTable,
       "jnxTLBVirtualServiceEntry": jnxTLBVirtualServiceEntry,
       "jnxTLBVirtualServiceNameKey": jnxTLBVirtualServiceNameKey,
       "jnxTLBVirtualServiceName": jnxTLBVirtualServiceName,
       "jnxTLBVirtualServiceTranslationMode": jnxTLBVirtualServiceTranslationMode,
       "jnxTLBVirtualServiceInstance": jnxTLBVirtualServiceInstance,
       "jnxTLBVirtualServiceIPVersion": jnxTLBVirtualServiceIPVersion,
       "jnxTLBVirtualServiceIP": jnxTLBVirtualServiceIP,
       "jnxTLBVirtualServiceOperStatus": jnxTLBVirtualServiceOperStatus,
       "jnxTLBVirtualServiceAdminStatus": jnxTLBVirtualServiceAdminStatus,
       "jnxTLBVirtualServiceSubUnitNo": jnxTLBVirtualServiceSubUnitNo,
       "jnxTLBVirtualServiceFailures": jnxTLBVirtualServiceFailures,
       "jnxTLBVSClientPacketForwardCount": jnxTLBVSClientPacketForwardCount,
       "jnxTLBVSClientByteForwardCount": jnxTLBVSClientByteForwardCount,
       "jnxTLBVSClientPacketReverseCount": jnxTLBVSClientPacketReverseCount,
       "jnxTLBVSClientByteReverseCount": jnxTLBVSClientByteReverseCount,
       "jnxTLBVSTotalUpCount": jnxTLBVSTotalUpCount,
       "jnxTLBVSTotalDownCount": jnxTLBVSTotalDownCount,
       "jnxTLBVSTotalRealServerCount": jnxTLBVSTotalRealServerCount,
       "jnxTLBVSServiceUpTime": jnxTLBVSServiceUpTime,
       "jnxTLBVSActiveRealServerCount": jnxTLBVSActiveRealServerCount,
       "jnxTLBVSNetworkMonitorProfileCount": jnxTLBVSNetworkMonitorProfileCount,
       "jnxTLBVirtualServiceVirtualPort": jnxTLBVirtualServiceVirtualPort,
       "jnxTLBVirtualServiceRealPort": jnxTLBVirtualServiceRealPort,
       "jnxTLBVirtualServiceNextHopIndex": jnxTLBVirtualServiceNextHopIndex,
       "jnxTLBVirtualServiceProtocol": jnxTLBVirtualServiceProtocol,
       "jnxTLBVirtualServiceDemuxNextHopIndex": jnxTLBVirtualServiceDemuxNextHopIndex,
       "jnxTLBVirtualServiceInterface": jnxTLBVirtualServiceInterface,
       "jnxTLBVirtualServiceRoutingInstance": jnxTLBVirtualServiceRoutingInstance,
       "jnxTLBVirtualServiceHashMethod": jnxTLBVirtualServiceHashMethod,
       "jnxTLBVirtualServiceRouteMetric": jnxTLBVirtualServiceRouteMetric,
       "jnxTLBVirtualServiceAutoRejoin": jnxTLBVirtualServiceAutoRejoin,
       "jnxTLBVirtualServiceRouteHoldTimer": jnxTLBVirtualServiceRouteHoldTimer,
       "jnxTLBVirtualServiceWarmUpTime": jnxTLBVirtualServiceWarmUpTime,
       "jnxTLBserverGroup": jnxTLBserverGroup,
       "jnxTLBServerGroupTable": jnxTLBServerGroupTable,
       "jnxTLBServerGroupEntry": jnxTLBServerGroupEntry,
       "jnxTLBServerGroupNameKey": jnxTLBServerGroupNameKey,
       "jnxTLBServerGroupName": jnxTLBServerGroupName,
       "jnxTLBServerGroupInstance": jnxTLBServerGroupInstance,
       "jnxTLBServerGroupIPVersion": jnxTLBServerGroupIPVersion,
       "jnxTLBServerGroupOperStatus": jnxTLBServerGroupOperStatus,
       "jnxTLBServerGroupAdminStatus": jnxTLBServerGroupAdminStatus,
       "jnxTLBServerGroupFailures": jnxTLBServerGroupFailures,
       "jnxTLBServerGroupLastTimeUp": jnxTLBServerGroupLastTimeUp,
       "jnxTLBServerGroupLastTimeDown": jnxTLBServerGroupLastTimeDown,
       "jnxTLBServerGroupTotalUpCount": jnxTLBServerGroupTotalUpCount,
       "jnxTLBServerGroupTotalDownCount": jnxTLBServerGroupTotalDownCount,
       "tlbDataMib": tlbDataMib,
       "tlbTrapMib": tlbTrapMib,
       "tlbNotificationObjMib": tlbNotificationObjMib,
       "tlbInstanceName": tlbInstanceName,
       "tlbRealServerName": tlbRealServerName,
       "tlbRealServerGroupName": tlbRealServerGroupName,
       "tlbRealServerIpAddress": tlbRealServerIpAddress,
       "tlbVirtualServiceName": tlbVirtualServiceName,
       "tlbVirtualServiceIpAddr": tlbVirtualServiceIpAddr,
       "tlbVirtualServicePort": tlbVirtualServicePort,
       "tlbProfileName": tlbProfileName,
       "tlbMultiserviceInterface": tlbMultiserviceInterface,
       "tlbMultiServicePIC": tlbMultiServicePIC,
       "tlbNetmonCpuUsage": tlbNetmonCpuUsage,
       "tlbMonitorMode": tlbMonitorMode,
       "tlbNotificationMib": tlbNotificationMib,
       "tlbRealServerUp": tlbRealServerUp,
       "tlbRealServerDown": tlbRealServerDown,
       "tlbRealServerRejoined": tlbRealServerRejoined,
       "tlbVirtualServiceUp": tlbVirtualServiceUp,
       "tlbVirtualServiceDown": tlbVirtualServiceDown,
       "tlbRealServerServiceUp": tlbRealServerServiceUp,
       "tlbRealServerServiceDown": tlbRealServerServiceDown,
       "tlbVirtualServerServiceUp": tlbVirtualServerServiceUp,
       "tlbVirtualServerServiceDown": tlbVirtualServerServiceDown,
       "tlbUp": tlbUp,
       "tlbShutdown": tlbShutdown,
       "tlbPicConnected": tlbPicConnected,
       "tlbPicDisconnected": tlbPicDisconnected,
       "tlbCpuHigh": tlbCpuHigh,
       "tlbCpuNormal": tlbCpuNormal,
       "tlbUnlicensedPic": tlbUnlicensedPic,
       "jnxTLBNetworkMonitorProfile": jnxTLBNetworkMonitorProfile,
       "jnxTLBNetworkMonitorProfileTable": jnxTLBNetworkMonitorProfileTable,
       "jnxTLBNetworkMonitorProfileEntry": jnxTLBNetworkMonitorProfileEntry,
       "jnxTLBNetworkMonitorProfileNameKey": jnxTLBNetworkMonitorProfileNameKey,
       "jnxTLBNetworkMonitorProfileVirtualServiceName": jnxTLBNetworkMonitorProfileVirtualServiceName,
       "jnxTLBNetworkMonitorProfileRealServerName": jnxTLBNetworkMonitorProfileRealServerName,
       "jnxTLBNetworkMonitorProfileIndex": jnxTLBNetworkMonitorProfileIndex,
       "jnxTLBNetworkMonitorProfileName": jnxTLBNetworkMonitorProfileName,
       "jnxTLBNetworkMonitorProfileType": jnxTLBNetworkMonitorProfileType,
       "jnxTLBNetworkMonitorProfileProbeInterval": jnxTLBNetworkMonitorProfileProbeInterval,
       "jnxTLBNetworkMonitorProfileFailureRetry": jnxTLBNetworkMonitorProfileFailureRetry,
       "jnxTLBNetworkMonitorProfileRecoverRetry": jnxTLBNetworkMonitorProfileRecoverRetry,
       "jnxTLBNetworkMonitorProfilePortNumber": jnxTLBNetworkMonitorProfilePortNumber,
       "jnxTLBNetworkMonitorProfileProbeState": jnxTLBNetworkMonitorProfileProbeState,
       "jnxTLBNetworkMonitorProfileProbeSent": jnxTLBNetworkMonitorProfileProbeSent,
       "jnxTLBNetworkMonitorProfileProbeSuccess": jnxTLBNetworkMonitorProfileProbeSuccess,
       "jnxTLBNetworkMonitorProfileProbeFail": jnxTLBNetworkMonitorProfileProbeFail,
       "jnxTLBNetworkMonitorProfileProbeConsecutiveSuccess": jnxTLBNetworkMonitorProfileProbeConsecutiveSuccess,
       "jnxTLBNetworkMonitorProfileProbeConsecutiveFail": jnxTLBNetworkMonitorProfileProbeConsecutiveFail}
)
