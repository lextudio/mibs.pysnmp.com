# SNMP MIB module (NOMADIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOMADIX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:47 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

nomadix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3309)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1)
)
_Ag_ObjectIdentity = ObjectIdentity
ag = _Ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3)
)
_NdxTraps_ObjectIdentity = ObjectIdentity
ndxTraps = _NdxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 0)
)
_Aaa_ObjectIdentity = ObjectIdentity
aaa = _Aaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2)
)


class _AaaOn_Type(Integer32):
    """Custom type aaaOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaOn_Type.__name__ = "Integer32"
_AaaOn_Object = MibScalar
aaaOn = _AaaOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 1),
    _AaaOn_Type()
)
aaaOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaOn.setStatus("current")


class _AaaXmlOn_Type(Integer32):
    """Custom type aaaXmlOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaXmlOn_Type.__name__ = "Integer32"
_AaaXmlOn_Object = MibScalar
aaaXmlOn = _AaaXmlOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 2),
    _AaaXmlOn_Type()
)
aaaXmlOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaXmlOn.setStatus("current")
_AaaXmlSender1Ip_Type = IpAddress
_AaaXmlSender1Ip_Object = MibScalar
aaaXmlSender1Ip = _AaaXmlSender1Ip_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 3),
    _AaaXmlSender1Ip_Type()
)
aaaXmlSender1Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaXmlSender1Ip.setStatus("current")


class _AaaPrintBillingCommandOn_Type(Integer32):
    """Custom type aaaPrintBillingCommandOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaPrintBillingCommandOn_Type.__name__ = "Integer32"
_AaaPrintBillingCommandOn_Object = MibScalar
aaaPrintBillingCommandOn = _AaaPrintBillingCommandOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 4),
    _AaaPrintBillingCommandOn_Type()
)
aaaPrintBillingCommandOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPrintBillingCommandOn.setStatus("current")


class _AaaPassthroughPortOn_Type(Integer32):
    """Custom type aaaPassthroughPortOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaPassthroughPortOn_Type.__name__ = "Integer32"
_AaaPassthroughPortOn_Object = MibScalar
aaaPassthroughPortOn = _AaaPassthroughPortOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 5),
    _AaaPassthroughPortOn_Type()
)
aaaPassthroughPortOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPassthroughPortOn.setStatus("current")
_AaaPassthroughPortNumber_Type = Integer32
_AaaPassthroughPortNumber_Object = MibScalar
aaaPassthroughPortNumber = _AaaPassthroughPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 6),
    _AaaPassthroughPortNumber_Type()
)
aaaPassthroughPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPassthroughPortNumber.setStatus("current")


class _AaaDot1xOn_Type(Integer32):
    """Custom type aaaDot1xOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaDot1xOn_Type.__name__ = "Integer32"
_AaaDot1xOn_Object = MibScalar
aaaDot1xOn = _AaaDot1xOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 7),
    _AaaDot1xOn_Type()
)
aaaDot1xOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaDot1xOn.setStatus("current")


class _AaaOSencodingOn_Type(Integer32):
    """Custom type aaaOSencodingOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaOSencodingOn_Type.__name__ = "Integer32"
_AaaOSencodingOn_Object = MibScalar
aaaOSencodingOn = _AaaOSencodingOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 8),
    _AaaOSencodingOn_Type()
)
aaaOSencodingOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaOSencodingOn.setStatus("current")


class _AaaAuthMode_Type(Integer32):
    """Custom type aaaAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("externalAuthorization", 1),
          ("internalAuthorization", 0))
    )


_AaaAuthMode_Type.__name__ = "Integer32"
_AaaAuthMode_Object = MibScalar
aaaAuthMode = _AaaAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 9),
    _AaaAuthMode_Type()
)
aaaAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAuthMode.setStatus("current")
_AaaInternalAuth_ObjectIdentity = ObjectIdentity
aaaInternalAuth = _AaaInternalAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10)
)


class _AaaSslOn_Type(Integer32):
    """Custom type aaaSslOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSslOn_Type.__name__ = "Integer32"
_AaaSslOn_Object = MibScalar
aaaSslOn = _AaaSslOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 1),
    _AaaSslOn_Type()
)
aaaSslOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSslOn.setStatus("current")


class _AaaSslHostName_Type(DisplayString):
    """Custom type aaaSslHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaaSslHostName_Type.__name__ = "DisplayString"
_AaaSslHostName_Object = MibScalar
aaaSslHostName = _AaaSslHostName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 2),
    _AaaSslHostName_Type()
)
aaaSslHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSslHostName.setStatus("current")


class _AaaPortalPageOn_Type(Integer32):
    """Custom type aaaPortalPageOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaPortalPageOn_Type.__name__ = "Integer32"
_AaaPortalPageOn_Object = MibScalar
aaaPortalPageOn = _AaaPortalPageOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 3),
    _AaaPortalPageOn_Type()
)
aaaPortalPageOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPortalPageOn.setStatus("current")


class _AaaPortalPageUrl_Type(DisplayString):
    """Custom type aaaPortalPageUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_AaaPortalPageUrl_Type.__name__ = "DisplayString"
_AaaPortalPageUrl_Object = MibScalar
aaaPortalPageUrl = _AaaPortalPageUrl_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 4),
    _AaaPortalPageUrl_Type()
)
aaaPortalPageUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPortalPageUrl.setStatus("current")


class _AaaUsernameOn_Type(Integer32):
    """Custom type aaaUsernameOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaUsernameOn_Type.__name__ = "Integer32"
_AaaUsernameOn_Object = MibScalar
aaaUsernameOn = _AaaUsernameOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 5),
    _AaaUsernameOn_Type()
)
aaaUsernameOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaUsernameOn.setStatus("current")


class _AaaNewSubscriberOn_Type(Integer32):
    """Custom type aaaNewSubscriberOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaNewSubscriberOn_Type.__name__ = "Integer32"
_AaaNewSubscriberOn_Object = MibScalar
aaaNewSubscriberOn = _AaaNewSubscriberOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 6),
    _AaaNewSubscriberOn_Type()
)
aaaNewSubscriberOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaNewSubscriberOn.setStatus("current")


class _AaaReloginOn_Type(Integer32):
    """Custom type aaaReloginOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaReloginOn_Type.__name__ = "Integer32"
_AaaReloginOn_Object = MibScalar
aaaReloginOn = _AaaReloginOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 7),
    _AaaReloginOn_Type()
)
aaaReloginOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaReloginOn.setStatus("current")


class _AaaCreditCardOn_Type(Integer32):
    """Custom type aaaCreditCardOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaCreditCardOn_Type.__name__ = "Integer32"
_AaaCreditCardOn_Object = MibScalar
aaaCreditCardOn = _AaaCreditCardOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 8),
    _AaaCreditCardOn_Type()
)
aaaCreditCardOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaCreditCardOn.setStatus("current")


class _AaaCreditCardUrl_Type(DisplayString):
    """Custom type aaaCreditCardUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_AaaCreditCardUrl_Type.__name__ = "DisplayString"
_AaaCreditCardUrl_Object = MibScalar
aaaCreditCardUrl = _AaaCreditCardUrl_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 9),
    _AaaCreditCardUrl_Type()
)
aaaCreditCardUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaCreditCardUrl.setStatus("current")
_AaaCreditCardIp_Type = IpAddress
_AaaCreditCardIp_Object = MibScalar
aaaCreditCardIp = _AaaCreditCardIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 10),
    _AaaCreditCardIp_Type()
)
aaaCreditCardIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaCreditCardIp.setStatus("current")


class _AaaMerchantId_Type(DisplayString):
    """Custom type aaaMerchantId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaMerchantId_Type.__name__ = "DisplayString"
_AaaMerchantId_Object = MibScalar
aaaMerchantId = _AaaMerchantId_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 11),
    _AaaMerchantId_Type()
)
aaaMerchantId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMerchantId.setStatus("current")


class _AaaSmartClientOn_Type(Integer32):
    """Custom type aaaSmartClientOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSmartClientOn_Type.__name__ = "Integer32"
_AaaSmartClientOn_Object = MibScalar
aaaSmartClientOn = _AaaSmartClientOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 12),
    _AaaSmartClientOn_Type()
)
aaaSmartClientOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSmartClientOn.setStatus("current")


class _AaaPortalParameterPassing_Type(Integer32):
    """Custom type aaaPortalParameterPassing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaPortalParameterPassing_Type.__name__ = "Integer32"
_AaaPortalParameterPassing_Object = MibScalar
aaaPortalParameterPassing = _AaaPortalParameterPassing_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 13),
    _AaaPortalParameterPassing_Type()
)
aaaPortalParameterPassing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPortalParameterPassing.setStatus("current")


class _AaaPortalPostUrl_Type(DisplayString):
    """Custom type aaaPortalPostUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_AaaPortalPostUrl_Type.__name__ = "DisplayString"
_AaaPortalPostUrl_Object = MibScalar
aaaPortalPostUrl = _AaaPortalPostUrl_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 14),
    _AaaPortalPostUrl_Type()
)
aaaPortalPostUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPortalPostUrl.setStatus("current")
_AaaPortalXMLPort_Type = Integer32
_AaaPortalXMLPort_Object = MibScalar
aaaPortalXMLPort = _AaaPortalXMLPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 15),
    _AaaPortalXMLPort_Type()
)
aaaPortalXMLPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPortalXMLPort.setStatus("current")


class _AaaSupportGISClients_Type(Integer32):
    """Custom type aaaSupportGISClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSupportGISClients_Type.__name__ = "Integer32"
_AaaSupportGISClients_Object = MibScalar
aaaSupportGISClients = _AaaSupportGISClients_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 16),
    _AaaSupportGISClients_Type()
)
aaaSupportGISClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSupportGISClients.setStatus("current")


class _AaaIWSLoginPageBlocking_Type(Integer32):
    """Custom type aaaIWSLoginPageBlocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AaaIWSLoginPageBlocking_Type.__name__ = "Integer32"
_AaaIWSLoginPageBlocking_Object = MibScalar
aaaIWSLoginPageBlocking = _AaaIWSLoginPageBlocking_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 20),
    _AaaIWSLoginPageBlocking_Type()
)
aaaIWSLoginPageBlocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaIWSLoginPageBlocking.setStatus("current")


class _AaaCreditCardServerTypeSelection_Type(Integer32):
    """Custom type aaaCreditCardServerTypeSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorize-net", 2),
          ("chainfusion", 1))
    )


_AaaCreditCardServerTypeSelection_Type.__name__ = "Integer32"
_AaaCreditCardServerTypeSelection_Object = MibScalar
aaaCreditCardServerTypeSelection = _AaaCreditCardServerTypeSelection_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 21),
    _AaaCreditCardServerTypeSelection_Type()
)
aaaCreditCardServerTypeSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaCreditCardServerTypeSelection.setStatus("current")
_AaaChainfusionCCTransTime_Type = Integer32
_AaaChainfusionCCTransTime_Object = MibScalar
aaaChainfusionCCTransTime = _AaaChainfusionCCTransTime_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 10, 22),
    _AaaChainfusionCCTransTime_Type()
)
aaaChainfusionCCTransTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaChainfusionCCTransTime.setStatus("current")
_AaaExternalAuth_ObjectIdentity = ObjectIdentity
aaaExternalAuth = _AaaExternalAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 11)
)


class _AaaSecretKey_Type(DisplayString):
    """Custom type aaaSecretKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaSecretKey_Type.__name__ = "DisplayString"
_AaaSecretKey_Object = MibScalar
aaaSecretKey = _AaaSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 11, 1),
    _AaaSecretKey_Type()
)
aaaSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSecretKey.setStatus("current")
_AaaExternalIPAddress_Type = IpAddress
_AaaExternalIPAddress_Object = MibScalar
aaaExternalIPAddress = _AaaExternalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 11, 2),
    _AaaExternalIPAddress_Type()
)
aaaExternalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaExternalIPAddress.setStatus("current")


class _AaaAuthorizationUrl_Type(DisplayString):
    """Custom type aaaAuthorizationUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_AaaAuthorizationUrl_Type.__name__ = "DisplayString"
_AaaAuthorizationUrl_Object = MibScalar
aaaAuthorizationUrl = _AaaAuthorizationUrl_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 11, 3),
    _AaaAuthorizationUrl_Type()
)
aaaAuthorizationUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAuthorizationUrl.setStatus("current")


class _AaaLoggingOn_Type(Integer32):
    """Custom type aaaLoggingOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaLoggingOn_Type.__name__ = "Integer32"
_AaaLoggingOn_Object = MibScalar
aaaLoggingOn = _AaaLoggingOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 12),
    _AaaLoggingOn_Type()
)
aaaLoggingOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaLoggingOn.setStatus("current")


class _AaaLogNumber_Type(Integer32):
    """Custom type aaaLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaLogNumber_Type.__name__ = "Integer32"
_AaaLogNumber_Object = MibScalar
aaaLogNumber = _AaaLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 13),
    _AaaLogNumber_Type()
)
aaaLogNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaLogNumber.setStatus("current")
_AaaLogServerIp_Type = IpAddress
_AaaLogServerIp_Object = MibScalar
aaaLogServerIp = _AaaLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 14),
    _AaaLogServerIp_Type()
)
aaaLogServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaLogServerIp.setStatus("current")
_AaaBillingOption_ObjectIdentity = ObjectIdentity
aaaBillingOption = _AaaBillingOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15)
)


class _AaaBilloptIntroMsg_Type(DisplayString):
    """Custom type aaaBilloptIntroMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaBilloptIntroMsg_Type.__name__ = "DisplayString"
_AaaBilloptIntroMsg_Object = MibScalar
aaaBilloptIntroMsg = _AaaBilloptIntroMsg_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 1),
    _AaaBilloptIntroMsg_Type()
)
aaaBilloptIntroMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptIntroMsg.setStatus("current")


class _AaaBilloptOfferMsg_Type(DisplayString):
    """Custom type aaaBilloptOfferMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaBilloptOfferMsg_Type.__name__ = "DisplayString"
_AaaBilloptOfferMsg_Object = MibScalar
aaaBilloptOfferMsg = _AaaBilloptOfferMsg_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 2),
    _AaaBilloptOfferMsg_Type()
)
aaaBilloptOfferMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptOfferMsg.setStatus("current")


class _AaaBilloptPolicyMsg_Type(DisplayString):
    """Custom type aaaBilloptPolicyMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaBilloptPolicyMsg_Type.__name__ = "DisplayString"
_AaaBilloptPolicyMsg_Object = MibScalar
aaaBilloptPolicyMsg = _AaaBilloptPolicyMsg_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 3),
    _AaaBilloptPolicyMsg_Type()
)
aaaBilloptPolicyMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptPolicyMsg.setStatus("current")
_AaaBilloptMinTimeUnitMinute_Type = Integer32
_AaaBilloptMinTimeUnitMinute_Object = MibScalar
aaaBilloptMinTimeUnitMinute = _AaaBilloptMinTimeUnitMinute_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 5),
    _AaaBilloptMinTimeUnitMinute_Type()
)
aaaBilloptMinTimeUnitMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMinTimeUnitMinute.setStatus("current")
_AaaBilloptMinTimeUnitHour_Type = Integer32
_AaaBilloptMinTimeUnitHour_Object = MibScalar
aaaBilloptMinTimeUnitHour = _AaaBilloptMinTimeUnitHour_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 6),
    _AaaBilloptMinTimeUnitHour_Type()
)
aaaBilloptMinTimeUnitHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMinTimeUnitHour.setStatus("current")
_AaaBilloptMinTimeUnitDay_Type = Integer32
_AaaBilloptMinTimeUnitDay_Object = MibScalar
aaaBilloptMinTimeUnitDay = _AaaBilloptMinTimeUnitDay_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 7),
    _AaaBilloptMinTimeUnitDay_Type()
)
aaaBilloptMinTimeUnitDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMinTimeUnitDay.setStatus("current")
_AaaBilloptMinTimeUnitWeek_Type = Integer32
_AaaBilloptMinTimeUnitWeek_Object = MibScalar
aaaBilloptMinTimeUnitWeek = _AaaBilloptMinTimeUnitWeek_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 8),
    _AaaBilloptMinTimeUnitWeek_Type()
)
aaaBilloptMinTimeUnitWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMinTimeUnitWeek.setStatus("current")
_AaaBilloptMinTimeUnitMonth_Type = Integer32
_AaaBilloptMinTimeUnitMonth_Object = MibScalar
aaaBilloptMinTimeUnitMonth = _AaaBilloptMinTimeUnitMonth_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 9),
    _AaaBilloptMinTimeUnitMonth_Type()
)
aaaBilloptMinTimeUnitMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMinTimeUnitMonth.setStatus("current")
_AaaBilloptMaxTimeUnitMinute_Type = Integer32
_AaaBilloptMaxTimeUnitMinute_Object = MibScalar
aaaBilloptMaxTimeUnitMinute = _AaaBilloptMaxTimeUnitMinute_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 10),
    _AaaBilloptMaxTimeUnitMinute_Type()
)
aaaBilloptMaxTimeUnitMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMaxTimeUnitMinute.setStatus("current")
_AaaBilloptMaxTimeUnitHour_Type = Integer32
_AaaBilloptMaxTimeUnitHour_Object = MibScalar
aaaBilloptMaxTimeUnitHour = _AaaBilloptMaxTimeUnitHour_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 11),
    _AaaBilloptMaxTimeUnitHour_Type()
)
aaaBilloptMaxTimeUnitHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMaxTimeUnitHour.setStatus("current")
_AaaBilloptMaxTimeUnitDay_Type = Integer32
_AaaBilloptMaxTimeUnitDay_Object = MibScalar
aaaBilloptMaxTimeUnitDay = _AaaBilloptMaxTimeUnitDay_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 12),
    _AaaBilloptMaxTimeUnitDay_Type()
)
aaaBilloptMaxTimeUnitDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMaxTimeUnitDay.setStatus("current")
_AaaBilloptMaxTimeUnitWeek_Type = Integer32
_AaaBilloptMaxTimeUnitWeek_Object = MibScalar
aaaBilloptMaxTimeUnitWeek = _AaaBilloptMaxTimeUnitWeek_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 13),
    _AaaBilloptMaxTimeUnitWeek_Type()
)
aaaBilloptMaxTimeUnitWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMaxTimeUnitWeek.setStatus("current")
_AaaBilloptMaxTimeUnitMonth_Type = Integer32
_AaaBilloptMaxTimeUnitMonth_Object = MibScalar
aaaBilloptMaxTimeUnitMonth = _AaaBilloptMaxTimeUnitMonth_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 14),
    _AaaBilloptMaxTimeUnitMonth_Type()
)
aaaBilloptMaxTimeUnitMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMaxTimeUnitMonth.setStatus("current")
_AaaBilloptFreeAccessTime_Type = Integer32
_AaaBilloptFreeAccessTime_Object = MibScalar
aaaBilloptFreeAccessTime = _AaaBilloptFreeAccessTime_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 15),
    _AaaBilloptFreeAccessTime_Type()
)
aaaBilloptFreeAccessTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptFreeAccessTime.setStatus("current")
_AaaBilloptMaxSubLifetime_Type = Integer32
_AaaBilloptMaxSubLifetime_Object = MibScalar
aaaBilloptMaxSubLifetime = _AaaBilloptMaxSubLifetime_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 16),
    _AaaBilloptMaxSubLifetime_Type()
)
aaaBilloptMaxSubLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBilloptMaxSubLifetime.setStatus("current")


class _AaaTaxRate_Type(DisplayString):
    """Custom type aaaTaxRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_AaaTaxRate_Type.__name__ = "DisplayString"
_AaaTaxRate_Object = MibScalar
aaaTaxRate = _AaaTaxRate_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 18),
    _AaaTaxRate_Type()
)
aaaTaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaTaxRate.setStatus("current")
_AaaBillingPlans_ObjectIdentity = ObjectIdentity
aaaBillingPlans = _AaaBillingPlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19)
)
_AaaBillingPlan0_ObjectIdentity = ObjectIdentity
aaaBillingPlan0 = _AaaBillingPlan0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1)
)


class _AaaBillingPlanOn0_Type(Integer32):
    """Custom type aaaBillingPlanOn0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanOn0_Type.__name__ = "Integer32"
_AaaBillingPlanOn0_Object = MibScalar
aaaBillingPlanOn0 = _AaaBillingPlanOn0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 1),
    _AaaBillingPlanOn0_Type()
)
aaaBillingPlanOn0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanOn0.setStatus("current")


class _AaaBillingPlanAssigned0_Type(Integer32):
    """Custom type aaaBillingPlanAssigned0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanAssigned0_Type.__name__ = "Integer32"
_AaaBillingPlanAssigned0_Object = MibScalar
aaaBillingPlanAssigned0 = _AaaBillingPlanAssigned0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 2),
    _AaaBillingPlanAssigned0_Type()
)
aaaBillingPlanAssigned0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanAssigned0.setStatus("current")


class _AaaBillingPlanXoverY0_Type(Integer32):
    """Custom type aaaBillingPlanXoverY0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanXoverY0_Type.__name__ = "Integer32"
_AaaBillingPlanXoverY0_Object = MibScalar
aaaBillingPlanXoverY0 = _AaaBillingPlanXoverY0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 3),
    _AaaBillingPlanXoverY0_Type()
)
aaaBillingPlanXoverY0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanXoverY0.setStatus("current")


class _AaaBillingPlanLabel0_Type(DisplayString):
    """Custom type aaaBillingPlanLabel0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AaaBillingPlanLabel0_Type.__name__ = "DisplayString"
_AaaBillingPlanLabel0_Object = MibScalar
aaaBillingPlanLabel0 = _AaaBillingPlanLabel0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 4),
    _AaaBillingPlanLabel0_Type()
)
aaaBillingPlanLabel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanLabel0.setStatus("current")


class _AaaBillingPlanDesc0_Type(DisplayString):
    """Custom type aaaBillingPlanDesc0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 140),
    )


_AaaBillingPlanDesc0_Type.__name__ = "DisplayString"
_AaaBillingPlanDesc0_Object = MibScalar
aaaBillingPlanDesc0 = _AaaBillingPlanDesc0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 5),
    _AaaBillingPlanDesc0_Type()
)
aaaBillingPlanDesc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDesc0.setStatus("current")


class _AaaBillingPlanPricingMin0_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMin0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMin0_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMin0_Object = MibScalar
aaaBillingPlanPricingMin0 = _AaaBillingPlanPricingMin0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 6),
    _AaaBillingPlanPricingMin0_Type()
)
aaaBillingPlanPricingMin0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMin0.setStatus("current")


class _AaaBillingPlanPricingHour0_Type(DisplayString):
    """Custom type aaaBillingPlanPricingHour0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingHour0_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingHour0_Object = MibScalar
aaaBillingPlanPricingHour0 = _AaaBillingPlanPricingHour0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 7),
    _AaaBillingPlanPricingHour0_Type()
)
aaaBillingPlanPricingHour0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingHour0.setStatus("current")


class _AaaBillingPlanPricingDay0_Type(DisplayString):
    """Custom type aaaBillingPlanPricingDay0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingDay0_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingDay0_Object = MibScalar
aaaBillingPlanPricingDay0 = _AaaBillingPlanPricingDay0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 8),
    _AaaBillingPlanPricingDay0_Type()
)
aaaBillingPlanPricingDay0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingDay0.setStatus("current")


class _AaaBillingPlanPricingWeek0_Type(DisplayString):
    """Custom type aaaBillingPlanPricingWeek0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingWeek0_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingWeek0_Object = MibScalar
aaaBillingPlanPricingWeek0 = _AaaBillingPlanPricingWeek0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 9),
    _AaaBillingPlanPricingWeek0_Type()
)
aaaBillingPlanPricingWeek0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingWeek0.setStatus("current")


class _AaaBillingPlanPricingMonth0_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMonth0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMonth0_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMonth0_Object = MibScalar
aaaBillingPlanPricingMonth0 = _AaaBillingPlanPricingMonth0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 10),
    _AaaBillingPlanPricingMonth0_Type()
)
aaaBillingPlanPricingMonth0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMonth0.setStatus("current")


class _AaaBillingPlanBandwidthUp0_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthUp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthUp0_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthUp0_Object = MibScalar
aaaBillingPlanBandwidthUp0 = _AaaBillingPlanBandwidthUp0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 11),
    _AaaBillingPlanBandwidthUp0_Type()
)
aaaBillingPlanBandwidthUp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthUp0.setStatus("current")


class _AaaBillingPlanBandwidthDown0_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthDown0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthDown0_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthDown0_Object = MibScalar
aaaBillingPlanBandwidthDown0 = _AaaBillingPlanBandwidthDown0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 12),
    _AaaBillingPlanBandwidthDown0_Type()
)
aaaBillingPlanBandwidthDown0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthDown0.setStatus("current")


class _AaaBillingPlanDHCPPool0_Type(Integer32):
    """Custom type aaaBillingPlanDHCPPool0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("private", 0),
          ("public", 1))
    )


_AaaBillingPlanDHCPPool0_Type.__name__ = "Integer32"
_AaaBillingPlanDHCPPool0_Object = MibScalar
aaaBillingPlanDHCPPool0 = _AaaBillingPlanDHCPPool0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 13),
    _AaaBillingPlanDHCPPool0_Type()
)
aaaBillingPlanDHCPPool0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDHCPPool0.setStatus("current")


class _AaaBillingPlanRateShow0_Type(Integer32):
    """Custom type aaaBillingPlanRateShow0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("hour", 1),
          ("minute", 0),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanRateShow0_Type.__name__ = "Integer32"
_AaaBillingPlanRateShow0_Object = MibScalar
aaaBillingPlanRateShow0 = _AaaBillingPlanRateShow0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 14),
    _AaaBillingPlanRateShow0_Type()
)
aaaBillingPlanRateShow0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanRateShow0.setStatus("current")


class _AaaBillingPlanCost0_Type(DisplayString):
    """Custom type aaaBillingPlanCost0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanCost0_Type.__name__ = "DisplayString"
_AaaBillingPlanCost0_Object = MibScalar
aaaBillingPlanCost0 = _AaaBillingPlanCost0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 15),
    _AaaBillingPlanCost0_Type()
)
aaaBillingPlanCost0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanCost0.setStatus("current")
_AaaBillingPlanDuration0_Type = Integer32
_AaaBillingPlanDuration0_Object = MibScalar
aaaBillingPlanDuration0 = _AaaBillingPlanDuration0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 16),
    _AaaBillingPlanDuration0_Type()
)
aaaBillingPlanDuration0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDuration0.setStatus("current")
_AaaBillingPlanValidity0_Type = Integer32
_AaaBillingPlanValidity0_Object = MibScalar
aaaBillingPlanValidity0 = _AaaBillingPlanValidity0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 17),
    _AaaBillingPlanValidity0_Type()
)
aaaBillingPlanValidity0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidity0.setStatus("current")


class _AaaBillingPlanValidityRateShow0_Type(Integer32):
    """Custom type aaaBillingPlanValidityRateShow0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanValidityRateShow0_Type.__name__ = "Integer32"
_AaaBillingPlanValidityRateShow0_Object = MibScalar
aaaBillingPlanValidityRateShow0 = _AaaBillingPlanValidityRateShow0_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 1, 18),
    _AaaBillingPlanValidityRateShow0_Type()
)
aaaBillingPlanValidityRateShow0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidityRateShow0.setStatus("current")
_AaaBillingPlan1_ObjectIdentity = ObjectIdentity
aaaBillingPlan1 = _AaaBillingPlan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2)
)


class _AaaBillingPlanOn1_Type(Integer32):
    """Custom type aaaBillingPlanOn1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanOn1_Type.__name__ = "Integer32"
_AaaBillingPlanOn1_Object = MibScalar
aaaBillingPlanOn1 = _AaaBillingPlanOn1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 1),
    _AaaBillingPlanOn1_Type()
)
aaaBillingPlanOn1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanOn1.setStatus("current")


class _AaaBillingPlanAssigned1_Type(Integer32):
    """Custom type aaaBillingPlanAssigned1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanAssigned1_Type.__name__ = "Integer32"
_AaaBillingPlanAssigned1_Object = MibScalar
aaaBillingPlanAssigned1 = _AaaBillingPlanAssigned1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 2),
    _AaaBillingPlanAssigned1_Type()
)
aaaBillingPlanAssigned1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanAssigned1.setStatus("current")


class _AaaBillingPlanXoverY1_Type(Integer32):
    """Custom type aaaBillingPlanXoverY1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanXoverY1_Type.__name__ = "Integer32"
_AaaBillingPlanXoverY1_Object = MibScalar
aaaBillingPlanXoverY1 = _AaaBillingPlanXoverY1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 3),
    _AaaBillingPlanXoverY1_Type()
)
aaaBillingPlanXoverY1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanXoverY1.setStatus("current")


class _AaaBillingPlanLabel1_Type(DisplayString):
    """Custom type aaaBillingPlanLabel1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AaaBillingPlanLabel1_Type.__name__ = "DisplayString"
_AaaBillingPlanLabel1_Object = MibScalar
aaaBillingPlanLabel1 = _AaaBillingPlanLabel1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 4),
    _AaaBillingPlanLabel1_Type()
)
aaaBillingPlanLabel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanLabel1.setStatus("current")


class _AaaBillingPlanDesc1_Type(DisplayString):
    """Custom type aaaBillingPlanDesc1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 140),
    )


_AaaBillingPlanDesc1_Type.__name__ = "DisplayString"
_AaaBillingPlanDesc1_Object = MibScalar
aaaBillingPlanDesc1 = _AaaBillingPlanDesc1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 5),
    _AaaBillingPlanDesc1_Type()
)
aaaBillingPlanDesc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDesc1.setStatus("current")


class _AaaBillingPlanPricingMin1_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMin1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMin1_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMin1_Object = MibScalar
aaaBillingPlanPricingMin1 = _AaaBillingPlanPricingMin1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 6),
    _AaaBillingPlanPricingMin1_Type()
)
aaaBillingPlanPricingMin1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMin1.setStatus("current")


class _AaaBillingPlanPricingHour1_Type(DisplayString):
    """Custom type aaaBillingPlanPricingHour1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingHour1_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingHour1_Object = MibScalar
aaaBillingPlanPricingHour1 = _AaaBillingPlanPricingHour1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 7),
    _AaaBillingPlanPricingHour1_Type()
)
aaaBillingPlanPricingHour1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingHour1.setStatus("current")


class _AaaBillingPlanPricingDay1_Type(DisplayString):
    """Custom type aaaBillingPlanPricingDay1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingDay1_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingDay1_Object = MibScalar
aaaBillingPlanPricingDay1 = _AaaBillingPlanPricingDay1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 8),
    _AaaBillingPlanPricingDay1_Type()
)
aaaBillingPlanPricingDay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingDay1.setStatus("current")


class _AaaBillingPlanPricingWeek1_Type(DisplayString):
    """Custom type aaaBillingPlanPricingWeek1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingWeek1_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingWeek1_Object = MibScalar
aaaBillingPlanPricingWeek1 = _AaaBillingPlanPricingWeek1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 9),
    _AaaBillingPlanPricingWeek1_Type()
)
aaaBillingPlanPricingWeek1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingWeek1.setStatus("current")


class _AaaBillingPlanPricingMonth1_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMonth1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMonth1_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMonth1_Object = MibScalar
aaaBillingPlanPricingMonth1 = _AaaBillingPlanPricingMonth1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 10),
    _AaaBillingPlanPricingMonth1_Type()
)
aaaBillingPlanPricingMonth1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMonth1.setStatus("current")


class _AaaBillingPlanBandwidthUp1_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthUp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthUp1_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthUp1_Object = MibScalar
aaaBillingPlanBandwidthUp1 = _AaaBillingPlanBandwidthUp1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 11),
    _AaaBillingPlanBandwidthUp1_Type()
)
aaaBillingPlanBandwidthUp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthUp1.setStatus("current")


class _AaaBillingPlanBandwidthDown1_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthDown1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthDown1_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthDown1_Object = MibScalar
aaaBillingPlanBandwidthDown1 = _AaaBillingPlanBandwidthDown1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 12),
    _AaaBillingPlanBandwidthDown1_Type()
)
aaaBillingPlanBandwidthDown1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthDown1.setStatus("current")


class _AaaBillingPlanDHCPPool1_Type(Integer32):
    """Custom type aaaBillingPlanDHCPPool1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("private", 0),
          ("public", 1))
    )


_AaaBillingPlanDHCPPool1_Type.__name__ = "Integer32"
_AaaBillingPlanDHCPPool1_Object = MibScalar
aaaBillingPlanDHCPPool1 = _AaaBillingPlanDHCPPool1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 13),
    _AaaBillingPlanDHCPPool1_Type()
)
aaaBillingPlanDHCPPool1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDHCPPool1.setStatus("current")


class _AaaBillingPlanRateShow1_Type(Integer32):
    """Custom type aaaBillingPlanRateShow1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("hour", 1),
          ("minute", 0),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanRateShow1_Type.__name__ = "Integer32"
_AaaBillingPlanRateShow1_Object = MibScalar
aaaBillingPlanRateShow1 = _AaaBillingPlanRateShow1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 14),
    _AaaBillingPlanRateShow1_Type()
)
aaaBillingPlanRateShow1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanRateShow1.setStatus("current")


class _AaaBillingPlanCost1_Type(DisplayString):
    """Custom type aaaBillingPlanCost1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanCost1_Type.__name__ = "DisplayString"
_AaaBillingPlanCost1_Object = MibScalar
aaaBillingPlanCost1 = _AaaBillingPlanCost1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 15),
    _AaaBillingPlanCost1_Type()
)
aaaBillingPlanCost1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanCost1.setStatus("current")
_AaaBillingPlanDuration1_Type = Integer32
_AaaBillingPlanDuration1_Object = MibScalar
aaaBillingPlanDuration1 = _AaaBillingPlanDuration1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 16),
    _AaaBillingPlanDuration1_Type()
)
aaaBillingPlanDuration1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDuration1.setStatus("current")
_AaaBillingPlanValidity1_Type = Integer32
_AaaBillingPlanValidity1_Object = MibScalar
aaaBillingPlanValidity1 = _AaaBillingPlanValidity1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 17),
    _AaaBillingPlanValidity1_Type()
)
aaaBillingPlanValidity1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidity1.setStatus("current")


class _AaaBillingPlanValidityRateShow1_Type(Integer32):
    """Custom type aaaBillingPlanValidityRateShow1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanValidityRateShow1_Type.__name__ = "Integer32"
_AaaBillingPlanValidityRateShow1_Object = MibScalar
aaaBillingPlanValidityRateShow1 = _AaaBillingPlanValidityRateShow1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 2, 18),
    _AaaBillingPlanValidityRateShow1_Type()
)
aaaBillingPlanValidityRateShow1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidityRateShow1.setStatus("current")
_AaaBillingPlan2_ObjectIdentity = ObjectIdentity
aaaBillingPlan2 = _AaaBillingPlan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3)
)


class _AaaBillingPlanOn2_Type(Integer32):
    """Custom type aaaBillingPlanOn2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanOn2_Type.__name__ = "Integer32"
_AaaBillingPlanOn2_Object = MibScalar
aaaBillingPlanOn2 = _AaaBillingPlanOn2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 1),
    _AaaBillingPlanOn2_Type()
)
aaaBillingPlanOn2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanOn2.setStatus("current")


class _AaaBillingPlanAssigned2_Type(Integer32):
    """Custom type aaaBillingPlanAssigned2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanAssigned2_Type.__name__ = "Integer32"
_AaaBillingPlanAssigned2_Object = MibScalar
aaaBillingPlanAssigned2 = _AaaBillingPlanAssigned2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 2),
    _AaaBillingPlanAssigned2_Type()
)
aaaBillingPlanAssigned2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanAssigned2.setStatus("current")


class _AaaBillingPlanXoverY2_Type(Integer32):
    """Custom type aaaBillingPlanXoverY2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanXoverY2_Type.__name__ = "Integer32"
_AaaBillingPlanXoverY2_Object = MibScalar
aaaBillingPlanXoverY2 = _AaaBillingPlanXoverY2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 3),
    _AaaBillingPlanXoverY2_Type()
)
aaaBillingPlanXoverY2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanXoverY2.setStatus("current")


class _AaaBillingPlanLabel2_Type(DisplayString):
    """Custom type aaaBillingPlanLabel2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AaaBillingPlanLabel2_Type.__name__ = "DisplayString"
_AaaBillingPlanLabel2_Object = MibScalar
aaaBillingPlanLabel2 = _AaaBillingPlanLabel2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 4),
    _AaaBillingPlanLabel2_Type()
)
aaaBillingPlanLabel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanLabel2.setStatus("current")


class _AaaBillingPlanDesc2_Type(DisplayString):
    """Custom type aaaBillingPlanDesc2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 140),
    )


_AaaBillingPlanDesc2_Type.__name__ = "DisplayString"
_AaaBillingPlanDesc2_Object = MibScalar
aaaBillingPlanDesc2 = _AaaBillingPlanDesc2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 5),
    _AaaBillingPlanDesc2_Type()
)
aaaBillingPlanDesc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDesc2.setStatus("current")


class _AaaBillingPlanPricingMin2_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMin2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMin2_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMin2_Object = MibScalar
aaaBillingPlanPricingMin2 = _AaaBillingPlanPricingMin2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 6),
    _AaaBillingPlanPricingMin2_Type()
)
aaaBillingPlanPricingMin2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMin2.setStatus("current")


class _AaaBillingPlanPricingHour2_Type(DisplayString):
    """Custom type aaaBillingPlanPricingHour2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingHour2_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingHour2_Object = MibScalar
aaaBillingPlanPricingHour2 = _AaaBillingPlanPricingHour2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 7),
    _AaaBillingPlanPricingHour2_Type()
)
aaaBillingPlanPricingHour2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingHour2.setStatus("current")


class _AaaBillingPlanPricingDay2_Type(DisplayString):
    """Custom type aaaBillingPlanPricingDay2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingDay2_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingDay2_Object = MibScalar
aaaBillingPlanPricingDay2 = _AaaBillingPlanPricingDay2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 8),
    _AaaBillingPlanPricingDay2_Type()
)
aaaBillingPlanPricingDay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingDay2.setStatus("current")


class _AaaBillingPlanPricingWeek2_Type(DisplayString):
    """Custom type aaaBillingPlanPricingWeek2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingWeek2_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingWeek2_Object = MibScalar
aaaBillingPlanPricingWeek2 = _AaaBillingPlanPricingWeek2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 9),
    _AaaBillingPlanPricingWeek2_Type()
)
aaaBillingPlanPricingWeek2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingWeek2.setStatus("current")


class _AaaBillingPlanPricingMonth2_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMonth2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMonth2_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMonth2_Object = MibScalar
aaaBillingPlanPricingMonth2 = _AaaBillingPlanPricingMonth2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 10),
    _AaaBillingPlanPricingMonth2_Type()
)
aaaBillingPlanPricingMonth2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMonth2.setStatus("current")


class _AaaBillingPlanBandwidthUp2_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthUp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthUp2_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthUp2_Object = MibScalar
aaaBillingPlanBandwidthUp2 = _AaaBillingPlanBandwidthUp2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 11),
    _AaaBillingPlanBandwidthUp2_Type()
)
aaaBillingPlanBandwidthUp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthUp2.setStatus("current")


class _AaaBillingPlanBandwidthDown2_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthDown2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthDown2_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthDown2_Object = MibScalar
aaaBillingPlanBandwidthDown2 = _AaaBillingPlanBandwidthDown2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 12),
    _AaaBillingPlanBandwidthDown2_Type()
)
aaaBillingPlanBandwidthDown2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthDown2.setStatus("current")


class _AaaBillingPlanDHCPPool2_Type(Integer32):
    """Custom type aaaBillingPlanDHCPPool2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("private", 0),
          ("public", 1))
    )


_AaaBillingPlanDHCPPool2_Type.__name__ = "Integer32"
_AaaBillingPlanDHCPPool2_Object = MibScalar
aaaBillingPlanDHCPPool2 = _AaaBillingPlanDHCPPool2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 13),
    _AaaBillingPlanDHCPPool2_Type()
)
aaaBillingPlanDHCPPool2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDHCPPool2.setStatus("current")


class _AaaBillingPlanRateShow2_Type(Integer32):
    """Custom type aaaBillingPlanRateShow2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("hour", 1),
          ("minute", 0),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanRateShow2_Type.__name__ = "Integer32"
_AaaBillingPlanRateShow2_Object = MibScalar
aaaBillingPlanRateShow2 = _AaaBillingPlanRateShow2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 14),
    _AaaBillingPlanRateShow2_Type()
)
aaaBillingPlanRateShow2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanRateShow2.setStatus("current")


class _AaaBillingPlanCost2_Type(DisplayString):
    """Custom type aaaBillingPlanCost2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanCost2_Type.__name__ = "DisplayString"
_AaaBillingPlanCost2_Object = MibScalar
aaaBillingPlanCost2 = _AaaBillingPlanCost2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 15),
    _AaaBillingPlanCost2_Type()
)
aaaBillingPlanCost2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanCost2.setStatus("current")
_AaaBillingPlanDuration2_Type = Integer32
_AaaBillingPlanDuration2_Object = MibScalar
aaaBillingPlanDuration2 = _AaaBillingPlanDuration2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 16),
    _AaaBillingPlanDuration2_Type()
)
aaaBillingPlanDuration2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDuration2.setStatus("current")
_AaaBillingPlanValidity2_Type = Integer32
_AaaBillingPlanValidity2_Object = MibScalar
aaaBillingPlanValidity2 = _AaaBillingPlanValidity2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 17),
    _AaaBillingPlanValidity2_Type()
)
aaaBillingPlanValidity2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidity2.setStatus("current")


class _AaaBillingPlanValidityRateShow2_Type(Integer32):
    """Custom type aaaBillingPlanValidityRateShow2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanValidityRateShow2_Type.__name__ = "Integer32"
_AaaBillingPlanValidityRateShow2_Object = MibScalar
aaaBillingPlanValidityRateShow2 = _AaaBillingPlanValidityRateShow2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 3, 18),
    _AaaBillingPlanValidityRateShow2_Type()
)
aaaBillingPlanValidityRateShow2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidityRateShow2.setStatus("current")
_AaaBillingPlan3_ObjectIdentity = ObjectIdentity
aaaBillingPlan3 = _AaaBillingPlan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4)
)


class _AaaBillingPlanOn3_Type(Integer32):
    """Custom type aaaBillingPlanOn3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanOn3_Type.__name__ = "Integer32"
_AaaBillingPlanOn3_Object = MibScalar
aaaBillingPlanOn3 = _AaaBillingPlanOn3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 1),
    _AaaBillingPlanOn3_Type()
)
aaaBillingPlanOn3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanOn3.setStatus("current")


class _AaaBillingPlanAssigned3_Type(Integer32):
    """Custom type aaaBillingPlanAssigned3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanAssigned3_Type.__name__ = "Integer32"
_AaaBillingPlanAssigned3_Object = MibScalar
aaaBillingPlanAssigned3 = _AaaBillingPlanAssigned3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 2),
    _AaaBillingPlanAssigned3_Type()
)
aaaBillingPlanAssigned3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanAssigned3.setStatus("current")


class _AaaBillingPlanXoverY3_Type(Integer32):
    """Custom type aaaBillingPlanXoverY3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanXoverY3_Type.__name__ = "Integer32"
_AaaBillingPlanXoverY3_Object = MibScalar
aaaBillingPlanXoverY3 = _AaaBillingPlanXoverY3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 3),
    _AaaBillingPlanXoverY3_Type()
)
aaaBillingPlanXoverY3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanXoverY3.setStatus("current")


class _AaaBillingPlanLabel3_Type(DisplayString):
    """Custom type aaaBillingPlanLabel3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AaaBillingPlanLabel3_Type.__name__ = "DisplayString"
_AaaBillingPlanLabel3_Object = MibScalar
aaaBillingPlanLabel3 = _AaaBillingPlanLabel3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 4),
    _AaaBillingPlanLabel3_Type()
)
aaaBillingPlanLabel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanLabel3.setStatus("current")


class _AaaBillingPlanDesc3_Type(DisplayString):
    """Custom type aaaBillingPlanDesc3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 140),
    )


_AaaBillingPlanDesc3_Type.__name__ = "DisplayString"
_AaaBillingPlanDesc3_Object = MibScalar
aaaBillingPlanDesc3 = _AaaBillingPlanDesc3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 5),
    _AaaBillingPlanDesc3_Type()
)
aaaBillingPlanDesc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDesc3.setStatus("current")


class _AaaBillingPlanPricingMin3_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMin3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMin3_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMin3_Object = MibScalar
aaaBillingPlanPricingMin3 = _AaaBillingPlanPricingMin3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 6),
    _AaaBillingPlanPricingMin3_Type()
)
aaaBillingPlanPricingMin3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMin3.setStatus("current")


class _AaaBillingPlanPricingHour3_Type(DisplayString):
    """Custom type aaaBillingPlanPricingHour3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingHour3_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingHour3_Object = MibScalar
aaaBillingPlanPricingHour3 = _AaaBillingPlanPricingHour3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 7),
    _AaaBillingPlanPricingHour3_Type()
)
aaaBillingPlanPricingHour3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingHour3.setStatus("current")


class _AaaBillingPlanPricingDay3_Type(DisplayString):
    """Custom type aaaBillingPlanPricingDay3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingDay3_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingDay3_Object = MibScalar
aaaBillingPlanPricingDay3 = _AaaBillingPlanPricingDay3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 8),
    _AaaBillingPlanPricingDay3_Type()
)
aaaBillingPlanPricingDay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingDay3.setStatus("current")


class _AaaBillingPlanPricingWeek3_Type(DisplayString):
    """Custom type aaaBillingPlanPricingWeek3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingWeek3_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingWeek3_Object = MibScalar
aaaBillingPlanPricingWeek3 = _AaaBillingPlanPricingWeek3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 9),
    _AaaBillingPlanPricingWeek3_Type()
)
aaaBillingPlanPricingWeek3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingWeek3.setStatus("current")


class _AaaBillingPlanPricingMonth3_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMonth3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMonth3_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMonth3_Object = MibScalar
aaaBillingPlanPricingMonth3 = _AaaBillingPlanPricingMonth3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 10),
    _AaaBillingPlanPricingMonth3_Type()
)
aaaBillingPlanPricingMonth3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMonth3.setStatus("current")


class _AaaBillingPlanBandwidthUp3_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthUp3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthUp3_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthUp3_Object = MibScalar
aaaBillingPlanBandwidthUp3 = _AaaBillingPlanBandwidthUp3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 11),
    _AaaBillingPlanBandwidthUp3_Type()
)
aaaBillingPlanBandwidthUp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthUp3.setStatus("current")


class _AaaBillingPlanBandwidthDown3_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthDown3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthDown3_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthDown3_Object = MibScalar
aaaBillingPlanBandwidthDown3 = _AaaBillingPlanBandwidthDown3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 12),
    _AaaBillingPlanBandwidthDown3_Type()
)
aaaBillingPlanBandwidthDown3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthDown3.setStatus("current")


class _AaaBillingPlanDHCPPool3_Type(Integer32):
    """Custom type aaaBillingPlanDHCPPool3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("private", 0),
          ("public", 1))
    )


_AaaBillingPlanDHCPPool3_Type.__name__ = "Integer32"
_AaaBillingPlanDHCPPool3_Object = MibScalar
aaaBillingPlanDHCPPool3 = _AaaBillingPlanDHCPPool3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 13),
    _AaaBillingPlanDHCPPool3_Type()
)
aaaBillingPlanDHCPPool3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDHCPPool3.setStatus("current")


class _AaaBillingPlanRateShow3_Type(Integer32):
    """Custom type aaaBillingPlanRateShow3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("hour", 1),
          ("minute", 0),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanRateShow3_Type.__name__ = "Integer32"
_AaaBillingPlanRateShow3_Object = MibScalar
aaaBillingPlanRateShow3 = _AaaBillingPlanRateShow3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 14),
    _AaaBillingPlanRateShow3_Type()
)
aaaBillingPlanRateShow3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanRateShow3.setStatus("current")


class _AaaBillingPlanCost3_Type(DisplayString):
    """Custom type aaaBillingPlanCost3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanCost3_Type.__name__ = "DisplayString"
_AaaBillingPlanCost3_Object = MibScalar
aaaBillingPlanCost3 = _AaaBillingPlanCost3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 15),
    _AaaBillingPlanCost3_Type()
)
aaaBillingPlanCost3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanCost3.setStatus("current")
_AaaBillingPlanDuration3_Type = Integer32
_AaaBillingPlanDuration3_Object = MibScalar
aaaBillingPlanDuration3 = _AaaBillingPlanDuration3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 16),
    _AaaBillingPlanDuration3_Type()
)
aaaBillingPlanDuration3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDuration3.setStatus("current")
_AaaBillingPlanValidity3_Type = Integer32
_AaaBillingPlanValidity3_Object = MibScalar
aaaBillingPlanValidity3 = _AaaBillingPlanValidity3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 17),
    _AaaBillingPlanValidity3_Type()
)
aaaBillingPlanValidity3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidity3.setStatus("current")


class _AaaBillingPlanValidityRateShow3_Type(Integer32):
    """Custom type aaaBillingPlanValidityRateShow3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanValidityRateShow3_Type.__name__ = "Integer32"
_AaaBillingPlanValidityRateShow3_Object = MibScalar
aaaBillingPlanValidityRateShow3 = _AaaBillingPlanValidityRateShow3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 4, 18),
    _AaaBillingPlanValidityRateShow3_Type()
)
aaaBillingPlanValidityRateShow3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidityRateShow3.setStatus("current")
_AaaBillingPlan4_ObjectIdentity = ObjectIdentity
aaaBillingPlan4 = _AaaBillingPlan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5)
)


class _AaaBillingPlanOn4_Type(Integer32):
    """Custom type aaaBillingPlanOn4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanOn4_Type.__name__ = "Integer32"
_AaaBillingPlanOn4_Object = MibScalar
aaaBillingPlanOn4 = _AaaBillingPlanOn4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 1),
    _AaaBillingPlanOn4_Type()
)
aaaBillingPlanOn4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanOn4.setStatus("current")


class _AaaBillingPlanAssigned4_Type(Integer32):
    """Custom type aaaBillingPlanAssigned4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanAssigned4_Type.__name__ = "Integer32"
_AaaBillingPlanAssigned4_Object = MibScalar
aaaBillingPlanAssigned4 = _AaaBillingPlanAssigned4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 2),
    _AaaBillingPlanAssigned4_Type()
)
aaaBillingPlanAssigned4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanAssigned4.setStatus("current")


class _AaaBillingPlanXoverY4_Type(Integer32):
    """Custom type aaaBillingPlanXoverY4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanXoverY4_Type.__name__ = "Integer32"
_AaaBillingPlanXoverY4_Object = MibScalar
aaaBillingPlanXoverY4 = _AaaBillingPlanXoverY4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 3),
    _AaaBillingPlanXoverY4_Type()
)
aaaBillingPlanXoverY4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanXoverY4.setStatus("current")


class _AaaBillingPlanLabel4_Type(DisplayString):
    """Custom type aaaBillingPlanLabel4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AaaBillingPlanLabel4_Type.__name__ = "DisplayString"
_AaaBillingPlanLabel4_Object = MibScalar
aaaBillingPlanLabel4 = _AaaBillingPlanLabel4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 4),
    _AaaBillingPlanLabel4_Type()
)
aaaBillingPlanLabel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanLabel4.setStatus("current")


class _AaaBillingPlanDesc4_Type(DisplayString):
    """Custom type aaaBillingPlanDesc4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 140),
    )


_AaaBillingPlanDesc4_Type.__name__ = "DisplayString"
_AaaBillingPlanDesc4_Object = MibScalar
aaaBillingPlanDesc4 = _AaaBillingPlanDesc4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 5),
    _AaaBillingPlanDesc4_Type()
)
aaaBillingPlanDesc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDesc4.setStatus("current")


class _AaaBillingPlanPricingMin4_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMin4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMin4_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMin4_Object = MibScalar
aaaBillingPlanPricingMin4 = _AaaBillingPlanPricingMin4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 6),
    _AaaBillingPlanPricingMin4_Type()
)
aaaBillingPlanPricingMin4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMin4.setStatus("current")


class _AaaBillingPlanPricingHour4_Type(DisplayString):
    """Custom type aaaBillingPlanPricingHour4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingHour4_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingHour4_Object = MibScalar
aaaBillingPlanPricingHour4 = _AaaBillingPlanPricingHour4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 7),
    _AaaBillingPlanPricingHour4_Type()
)
aaaBillingPlanPricingHour4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingHour4.setStatus("current")


class _AaaBillingPlanPricingDay4_Type(DisplayString):
    """Custom type aaaBillingPlanPricingDay4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingDay4_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingDay4_Object = MibScalar
aaaBillingPlanPricingDay4 = _AaaBillingPlanPricingDay4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 8),
    _AaaBillingPlanPricingDay4_Type()
)
aaaBillingPlanPricingDay4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingDay4.setStatus("current")


class _AaaBillingPlanPricingWeek4_Type(DisplayString):
    """Custom type aaaBillingPlanPricingWeek4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingWeek4_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingWeek4_Object = MibScalar
aaaBillingPlanPricingWeek4 = _AaaBillingPlanPricingWeek4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 9),
    _AaaBillingPlanPricingWeek4_Type()
)
aaaBillingPlanPricingWeek4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingWeek4.setStatus("current")


class _AaaBillingPlanPricingMonth4_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMonth4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMonth4_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMonth4_Object = MibScalar
aaaBillingPlanPricingMonth4 = _AaaBillingPlanPricingMonth4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 10),
    _AaaBillingPlanPricingMonth4_Type()
)
aaaBillingPlanPricingMonth4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMonth4.setStatus("current")


class _AaaBillingPlanBandwidthUp4_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthUp4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthUp4_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthUp4_Object = MibScalar
aaaBillingPlanBandwidthUp4 = _AaaBillingPlanBandwidthUp4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 11),
    _AaaBillingPlanBandwidthUp4_Type()
)
aaaBillingPlanBandwidthUp4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthUp4.setStatus("current")


class _AaaBillingPlanBandwidthDown4_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthDown4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthDown4_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthDown4_Object = MibScalar
aaaBillingPlanBandwidthDown4 = _AaaBillingPlanBandwidthDown4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 12),
    _AaaBillingPlanBandwidthDown4_Type()
)
aaaBillingPlanBandwidthDown4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthDown4.setStatus("current")


class _AaaBillingPlanDHCPPool4_Type(Integer32):
    """Custom type aaaBillingPlanDHCPPool4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("private", 0),
          ("public", 1))
    )


_AaaBillingPlanDHCPPool4_Type.__name__ = "Integer32"
_AaaBillingPlanDHCPPool4_Object = MibScalar
aaaBillingPlanDHCPPool4 = _AaaBillingPlanDHCPPool4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 13),
    _AaaBillingPlanDHCPPool4_Type()
)
aaaBillingPlanDHCPPool4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDHCPPool4.setStatus("current")


class _AaaBillingPlanRateShow4_Type(Integer32):
    """Custom type aaaBillingPlanRateShow4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("hour", 1),
          ("minute", 0),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanRateShow4_Type.__name__ = "Integer32"
_AaaBillingPlanRateShow4_Object = MibScalar
aaaBillingPlanRateShow4 = _AaaBillingPlanRateShow4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 14),
    _AaaBillingPlanRateShow4_Type()
)
aaaBillingPlanRateShow4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanRateShow4.setStatus("current")


class _AaaBillingPlanCost4_Type(DisplayString):
    """Custom type aaaBillingPlanCost4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanCost4_Type.__name__ = "DisplayString"
_AaaBillingPlanCost4_Object = MibScalar
aaaBillingPlanCost4 = _AaaBillingPlanCost4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 15),
    _AaaBillingPlanCost4_Type()
)
aaaBillingPlanCost4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanCost4.setStatus("current")
_AaaBillingPlanDuration4_Type = Integer32
_AaaBillingPlanDuration4_Object = MibScalar
aaaBillingPlanDuration4 = _AaaBillingPlanDuration4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 16),
    _AaaBillingPlanDuration4_Type()
)
aaaBillingPlanDuration4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDuration4.setStatus("current")
_AaaBillingPlanValidity4_Type = Integer32
_AaaBillingPlanValidity4_Object = MibScalar
aaaBillingPlanValidity4 = _AaaBillingPlanValidity4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 17),
    _AaaBillingPlanValidity4_Type()
)
aaaBillingPlanValidity4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidity4.setStatus("current")


class _AaaBillingPlanValidityRateShow4_Type(Integer32):
    """Custom type aaaBillingPlanValidityRateShow4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanValidityRateShow4_Type.__name__ = "Integer32"
_AaaBillingPlanValidityRateShow4_Object = MibScalar
aaaBillingPlanValidityRateShow4 = _AaaBillingPlanValidityRateShow4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 5, 18),
    _AaaBillingPlanValidityRateShow4_Type()
)
aaaBillingPlanValidityRateShow4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidityRateShow4.setStatus("current")
_AaaBillingPlan5_ObjectIdentity = ObjectIdentity
aaaBillingPlan5 = _AaaBillingPlan5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6)
)


class _AaaBillingPlanOn5_Type(Integer32):
    """Custom type aaaBillingPlanOn5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanOn5_Type.__name__ = "Integer32"
_AaaBillingPlanOn5_Object = MibScalar
aaaBillingPlanOn5 = _AaaBillingPlanOn5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 1),
    _AaaBillingPlanOn5_Type()
)
aaaBillingPlanOn5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanOn5.setStatus("current")


class _AaaBillingPlanAssigned5_Type(Integer32):
    """Custom type aaaBillingPlanAssigned5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanAssigned5_Type.__name__ = "Integer32"
_AaaBillingPlanAssigned5_Object = MibScalar
aaaBillingPlanAssigned5 = _AaaBillingPlanAssigned5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 2),
    _AaaBillingPlanAssigned5_Type()
)
aaaBillingPlanAssigned5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanAssigned5.setStatus("current")


class _AaaBillingPlanXoverY5_Type(Integer32):
    """Custom type aaaBillingPlanXoverY5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaBillingPlanXoverY5_Type.__name__ = "Integer32"
_AaaBillingPlanXoverY5_Object = MibScalar
aaaBillingPlanXoverY5 = _AaaBillingPlanXoverY5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 3),
    _AaaBillingPlanXoverY5_Type()
)
aaaBillingPlanXoverY5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanXoverY5.setStatus("current")


class _AaaBillingPlanLabel5_Type(DisplayString):
    """Custom type aaaBillingPlanLabel5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AaaBillingPlanLabel5_Type.__name__ = "DisplayString"
_AaaBillingPlanLabel5_Object = MibScalar
aaaBillingPlanLabel5 = _AaaBillingPlanLabel5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 4),
    _AaaBillingPlanLabel5_Type()
)
aaaBillingPlanLabel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanLabel5.setStatus("current")


class _AaaBillingPlanDesc5_Type(DisplayString):
    """Custom type aaaBillingPlanDesc5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 140),
    )


_AaaBillingPlanDesc5_Type.__name__ = "DisplayString"
_AaaBillingPlanDesc5_Object = MibScalar
aaaBillingPlanDesc5 = _AaaBillingPlanDesc5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 5),
    _AaaBillingPlanDesc5_Type()
)
aaaBillingPlanDesc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDesc5.setStatus("current")


class _AaaBillingPlanPricingMin5_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMin5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMin5_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMin5_Object = MibScalar
aaaBillingPlanPricingMin5 = _AaaBillingPlanPricingMin5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 6),
    _AaaBillingPlanPricingMin5_Type()
)
aaaBillingPlanPricingMin5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMin5.setStatus("current")


class _AaaBillingPlanPricingHour5_Type(DisplayString):
    """Custom type aaaBillingPlanPricingHour5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingHour5_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingHour5_Object = MibScalar
aaaBillingPlanPricingHour5 = _AaaBillingPlanPricingHour5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 7),
    _AaaBillingPlanPricingHour5_Type()
)
aaaBillingPlanPricingHour5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingHour5.setStatus("current")


class _AaaBillingPlanPricingDay5_Type(DisplayString):
    """Custom type aaaBillingPlanPricingDay5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingDay5_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingDay5_Object = MibScalar
aaaBillingPlanPricingDay5 = _AaaBillingPlanPricingDay5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 8),
    _AaaBillingPlanPricingDay5_Type()
)
aaaBillingPlanPricingDay5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingDay5.setStatus("current")


class _AaaBillingPlanPricingWeek5_Type(DisplayString):
    """Custom type aaaBillingPlanPricingWeek5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingWeek5_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingWeek5_Object = MibScalar
aaaBillingPlanPricingWeek5 = _AaaBillingPlanPricingWeek5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 9),
    _AaaBillingPlanPricingWeek5_Type()
)
aaaBillingPlanPricingWeek5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingWeek5.setStatus("current")


class _AaaBillingPlanPricingMonth5_Type(DisplayString):
    """Custom type aaaBillingPlanPricingMonth5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanPricingMonth5_Type.__name__ = "DisplayString"
_AaaBillingPlanPricingMonth5_Object = MibScalar
aaaBillingPlanPricingMonth5 = _AaaBillingPlanPricingMonth5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 10),
    _AaaBillingPlanPricingMonth5_Type()
)
aaaBillingPlanPricingMonth5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanPricingMonth5.setStatus("current")


class _AaaBillingPlanBandwidthUp5_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthUp5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthUp5_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthUp5_Object = MibScalar
aaaBillingPlanBandwidthUp5 = _AaaBillingPlanBandwidthUp5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 11),
    _AaaBillingPlanBandwidthUp5_Type()
)
aaaBillingPlanBandwidthUp5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthUp5.setStatus("current")


class _AaaBillingPlanBandwidthDown5_Type(Integer32):
    """Custom type aaaBillingPlanBandwidthDown5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_AaaBillingPlanBandwidthDown5_Type.__name__ = "Integer32"
_AaaBillingPlanBandwidthDown5_Object = MibScalar
aaaBillingPlanBandwidthDown5 = _AaaBillingPlanBandwidthDown5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 12),
    _AaaBillingPlanBandwidthDown5_Type()
)
aaaBillingPlanBandwidthDown5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanBandwidthDown5.setStatus("current")


class _AaaBillingPlanDHCPPool5_Type(Integer32):
    """Custom type aaaBillingPlanDHCPPool5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("private", 0),
          ("public", 1))
    )


_AaaBillingPlanDHCPPool5_Type.__name__ = "Integer32"
_AaaBillingPlanDHCPPool5_Object = MibScalar
aaaBillingPlanDHCPPool5 = _AaaBillingPlanDHCPPool5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 13),
    _AaaBillingPlanDHCPPool5_Type()
)
aaaBillingPlanDHCPPool5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDHCPPool5.setStatus("current")


class _AaaBillingPlanRateShow5_Type(Integer32):
    """Custom type aaaBillingPlanRateShow5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("hour", 1),
          ("minute", 0),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanRateShow5_Type.__name__ = "Integer32"
_AaaBillingPlanRateShow5_Object = MibScalar
aaaBillingPlanRateShow5 = _AaaBillingPlanRateShow5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 14),
    _AaaBillingPlanRateShow5_Type()
)
aaaBillingPlanRateShow5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanRateShow5.setStatus("current")


class _AaaBillingPlanCost5_Type(DisplayString):
    """Custom type aaaBillingPlanCost5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaBillingPlanCost5_Type.__name__ = "DisplayString"
_AaaBillingPlanCost5_Object = MibScalar
aaaBillingPlanCost5 = _AaaBillingPlanCost5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 15),
    _AaaBillingPlanCost5_Type()
)
aaaBillingPlanCost5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanCost5.setStatus("current")
_AaaBillingPlanDuration5_Type = Integer32
_AaaBillingPlanDuration5_Object = MibScalar
aaaBillingPlanDuration5 = _AaaBillingPlanDuration5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 16),
    _AaaBillingPlanDuration5_Type()
)
aaaBillingPlanDuration5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanDuration5.setStatus("current")
_AaaBillingPlanValidity5_Type = Integer32
_AaaBillingPlanValidity5_Object = MibScalar
aaaBillingPlanValidity5 = _AaaBillingPlanValidity5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 17),
    _AaaBillingPlanValidity5_Type()
)
aaaBillingPlanValidity5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidity5.setStatus("current")


class _AaaBillingPlanValidityRateShow5_Type(Integer32):
    """Custom type aaaBillingPlanValidityRateShow5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("month", 4),
          ("week", 3))
    )


_AaaBillingPlanValidityRateShow5_Type.__name__ = "Integer32"
_AaaBillingPlanValidityRateShow5_Object = MibScalar
aaaBillingPlanValidityRateShow5 = _AaaBillingPlanValidityRateShow5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 15, 19, 6, 18),
    _AaaBillingPlanValidityRateShow5_Type()
)
aaaBillingPlanValidityRateShow5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBillingPlanValidityRateShow5.setStatus("current")
_AaaSubLoginUI_ObjectIdentity = ObjectIdentity
aaaSubLoginUI = _AaaSubLoginUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16)
)


class _AaaWebServiceMsg_Type(DisplayString):
    """Custom type aaaWebServiceMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaWebServiceMsg_Type.__name__ = "DisplayString"
_AaaWebServiceMsg_Object = MibScalar
aaaWebServiceMsg = _AaaWebServiceMsg_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 1),
    _AaaWebServiceMsg_Type()
)
aaaWebServiceMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebServiceMsg.setStatus("current")


class _AaaWebExistingUserMsg_Type(DisplayString):
    """Custom type aaaWebExistingUserMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaWebExistingUserMsg_Type.__name__ = "DisplayString"
_AaaWebExistingUserMsg_Object = MibScalar
aaaWebExistingUserMsg = _AaaWebExistingUserMsg_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 2),
    _AaaWebExistingUserMsg_Type()
)
aaaWebExistingUserMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebExistingUserMsg.setStatus("current")


class _AaaWebNewUsernameMsg_Type(DisplayString):
    """Custom type aaaWebNewUsernameMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaWebNewUsernameMsg_Type.__name__ = "DisplayString"
_AaaWebNewUsernameMsg_Object = MibScalar
aaaWebNewUsernameMsg = _AaaWebNewUsernameMsg_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 3),
    _AaaWebNewUsernameMsg_Type()
)
aaaWebNewUsernameMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebNewUsernameMsg.setStatus("current")


class _AaaWebContactMsg_Type(DisplayString):
    """Custom type aaaWebContactMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaWebContactMsg_Type.__name__ = "DisplayString"
_AaaWebContactMsg_Object = MibScalar
aaaWebContactMsg = _AaaWebContactMsg_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 4),
    _AaaWebContactMsg_Type()
)
aaaWebContactMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebContactMsg.setStatus("current")


class _AaaWebMicrosUsernameMsg_Type(DisplayString):
    """Custom type aaaWebMicrosUsernameMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaWebMicrosUsernameMsg_Type.__name__ = "DisplayString"
_AaaWebMicrosUsernameMsg_Object = MibScalar
aaaWebMicrosUsernameMsg = _AaaWebMicrosUsernameMsg_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 5),
    _AaaWebMicrosUsernameMsg_Type()
)
aaaWebMicrosUsernameMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebMicrosUsernameMsg.setStatus("current")


class _AaaWebJavascriptOn_Type(Integer32):
    """Custom type aaaWebJavascriptOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaWebJavascriptOn_Type.__name__ = "Integer32"
_AaaWebJavascriptOn_Object = MibScalar
aaaWebJavascriptOn = _AaaWebJavascriptOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 6),
    _AaaWebJavascriptOn_Type()
)
aaaWebJavascriptOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebJavascriptOn.setStatus("current")


class _AaaWebRememberMeOn_Type(Integer32):
    """Custom type aaaWebRememberMeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaWebRememberMeOn_Type.__name__ = "Integer32"
_AaaWebRememberMeOn_Object = MibScalar
aaaWebRememberMeOn = _AaaWebRememberMeOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 7),
    _AaaWebRememberMeOn_Type()
)
aaaWebRememberMeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebRememberMeOn.setStatus("current")


class _AaaRememberMeMsg_Type(DisplayString):
    """Custom type aaaRememberMeMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaRememberMeMsg_Type.__name__ = "DisplayString"
_AaaRememberMeMsg_Object = MibScalar
aaaRememberMeMsg = _AaaRememberMeMsg_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 8),
    _AaaRememberMeMsg_Type()
)
aaaRememberMeMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRememberMeMsg.setStatus("current")
_AaaRememberMeDays_Type = Integer32
_AaaRememberMeDays_Object = MibScalar
aaaRememberMeDays = _AaaRememberMeDays_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 9),
    _AaaRememberMeDays_Type()
)
aaaRememberMeDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRememberMeDays.setStatus("current")


class _AaaCurrency_Type(DisplayString):
    """Custom type aaaCurrency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AaaCurrency_Type.__name__ = "DisplayString"
_AaaCurrency_Object = MibScalar
aaaCurrency = _AaaCurrency_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 10),
    _AaaCurrency_Type()
)
aaaCurrency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaCurrency.setStatus("current")
_AaaAmountDecimals_Type = Integer32
_AaaAmountDecimals_Object = MibScalar
aaaAmountDecimals = _AaaAmountDecimals_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 11),
    _AaaAmountDecimals_Type()
)
aaaAmountDecimals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAmountDecimals.setStatus("current")


class _AaaWebImage_Type(DisplayString):
    """Custom type aaaWebImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 98),
    )


_AaaWebImage_Type.__name__ = "DisplayString"
_AaaWebImage_Object = MibScalar
aaaWebImage = _AaaWebImage_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 12),
    _AaaWebImage_Type()
)
aaaWebImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebImage.setStatus("current")


class _AaaWebPageBgcolor_Type(DisplayString):
    """Custom type aaaWebPageBgcolor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AaaWebPageBgcolor_Type.__name__ = "DisplayString"
_AaaWebPageBgcolor_Object = MibScalar
aaaWebPageBgcolor = _AaaWebPageBgcolor_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 13),
    _AaaWebPageBgcolor_Type()
)
aaaWebPageBgcolor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebPageBgcolor.setStatus("current")


class _AaaWebTabBgcolor_Type(DisplayString):
    """Custom type aaaWebTabBgcolor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 98),
    )


_AaaWebTabBgcolor_Type.__name__ = "DisplayString"
_AaaWebTabBgcolor_Object = MibScalar
aaaWebTabBgcolor = _AaaWebTabBgcolor_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 14),
    _AaaWebTabBgcolor_Type()
)
aaaWebTabBgcolor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebTabBgcolor.setStatus("current")


class _AaaWebTitleFont_Type(DisplayString):
    """Custom type aaaWebTitleFont based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 98),
    )


_AaaWebTitleFont_Type.__name__ = "DisplayString"
_AaaWebTitleFont_Object = MibScalar
aaaWebTitleFont = _AaaWebTitleFont_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 15),
    _AaaWebTitleFont_Type()
)
aaaWebTitleFont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebTitleFont.setStatus("current")


class _AaaWebItemFont_Type(DisplayString):
    """Custom type aaaWebItemFont based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 98),
    )


_AaaWebItemFont_Type.__name__ = "DisplayString"
_AaaWebItemFont_Object = MibScalar
aaaWebItemFont = _AaaWebItemFont_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 16),
    _AaaWebItemFont_Type()
)
aaaWebItemFont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaWebItemFont.setStatus("current")


class _AaaErrorAccessBlocked_Type(DisplayString):
    """Custom type aaaErrorAccessBlocked based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorAccessBlocked_Type.__name__ = "DisplayString"
_AaaErrorAccessBlocked_Object = MibScalar
aaaErrorAccessBlocked = _AaaErrorAccessBlocked_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 17),
    _AaaErrorAccessBlocked_Type()
)
aaaErrorAccessBlocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorAccessBlocked.setStatus("current")


class _AaaErrorAccessPassword_Type(DisplayString):
    """Custom type aaaErrorAccessPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorAccessPassword_Type.__name__ = "DisplayString"
_AaaErrorAccessPassword_Object = MibScalar
aaaErrorAccessPassword = _AaaErrorAccessPassword_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 18),
    _AaaErrorAccessPassword_Type()
)
aaaErrorAccessPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorAccessPassword.setStatus("current")


class _AaaErrorHasOccurred_Type(DisplayString):
    """Custom type aaaErrorHasOccurred based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorHasOccurred_Type.__name__ = "DisplayString"
_AaaErrorHasOccurred_Object = MibScalar
aaaErrorHasOccurred = _AaaErrorHasOccurred_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 19),
    _AaaErrorHasOccurred_Type()
)
aaaErrorHasOccurred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorHasOccurred.setStatus("current")


class _AaaErrorISPChallenge_Type(DisplayString):
    """Custom type aaaErrorISPChallenge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorISPChallenge_Type.__name__ = "DisplayString"
_AaaErrorISPChallenge_Object = MibScalar
aaaErrorISPChallenge = _AaaErrorISPChallenge_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 20),
    _AaaErrorISPChallenge_Type()
)
aaaErrorISPChallenge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorISPChallenge.setStatus("current")


class _AaaErrorMinMaxValues_Type(DisplayString):
    """Custom type aaaErrorMinMaxValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorMinMaxValues_Type.__name__ = "DisplayString"
_AaaErrorMinMaxValues_Object = MibScalar
aaaErrorMinMaxValues = _AaaErrorMinMaxValues_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 21),
    _AaaErrorMinMaxValues_Type()
)
aaaErrorMinMaxValues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorMinMaxValues.setStatus("current")


class _AaaErrorNoBillingOpts_Type(DisplayString):
    """Custom type aaaErrorNoBillingOpts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorNoBillingOpts_Type.__name__ = "DisplayString"
_AaaErrorNoBillingOpts_Object = MibScalar
aaaErrorNoBillingOpts = _AaaErrorNoBillingOpts_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 22),
    _AaaErrorNoBillingOpts_Type()
)
aaaErrorNoBillingOpts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorNoBillingOpts.setStatus("current")


class _AaaErrorNotAvailable_Type(DisplayString):
    """Custom type aaaErrorNotAvailable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorNotAvailable_Type.__name__ = "DisplayString"
_AaaErrorNotAvailable_Object = MibScalar
aaaErrorNotAvailable = _AaaErrorNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 23),
    _AaaErrorNotAvailable_Type()
)
aaaErrorNotAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorNotAvailable.setStatus("current")


class _AaaErrorPasswordMatch_Type(DisplayString):
    """Custom type aaaErrorPasswordMatch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorPasswordMatch_Type.__name__ = "DisplayString"
_AaaErrorPasswordMatch_Object = MibScalar
aaaErrorPasswordMatch = _AaaErrorPasswordMatch_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 24),
    _AaaErrorPasswordMatch_Type()
)
aaaErrorPasswordMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorPasswordMatch.setStatus("current")


class _AaaErrorPasswordWrong_Type(DisplayString):
    """Custom type aaaErrorPasswordWrong based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorPasswordWrong_Type.__name__ = "DisplayString"
_AaaErrorPasswordWrong_Object = MibScalar
aaaErrorPasswordWrong = _AaaErrorPasswordWrong_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 25),
    _AaaErrorPasswordWrong_Type()
)
aaaErrorPasswordWrong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorPasswordWrong.setStatus("current")


class _AaaErrorRoomBilling_Type(DisplayString):
    """Custom type aaaErrorRoomBilling based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorRoomBilling_Type.__name__ = "DisplayString"
_AaaErrorRoomBilling_Object = MibScalar
aaaErrorRoomBilling = _AaaErrorRoomBilling_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 26),
    _AaaErrorRoomBilling_Type()
)
aaaErrorRoomBilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorRoomBilling.setStatus("current")


class _AaaErrorTooManyUsers_Type(DisplayString):
    """Custom type aaaErrorTooManyUsers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorTooManyUsers_Type.__name__ = "DisplayString"
_AaaErrorTooManyUsers_Object = MibScalar
aaaErrorTooManyUsers = _AaaErrorTooManyUsers_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 27),
    _AaaErrorTooManyUsers_Type()
)
aaaErrorTooManyUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorTooManyUsers.setStatus("current")


class _AaaErrorTryAgain_Type(DisplayString):
    """Custom type aaaErrorTryAgain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorTryAgain_Type.__name__ = "DisplayString"
_AaaErrorTryAgain_Object = MibScalar
aaaErrorTryAgain = _AaaErrorTryAgain_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 28),
    _AaaErrorTryAgain_Type()
)
aaaErrorTryAgain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorTryAgain.setStatus("current")


class _AaaErrorUserIdMissing_Type(DisplayString):
    """Custom type aaaErrorUserIdMissing based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorUserIdMissing_Type.__name__ = "DisplayString"
_AaaErrorUserIdMissing_Object = MibScalar
aaaErrorUserIdMissing = _AaaErrorUserIdMissing_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 29),
    _AaaErrorUserIdMissing_Type()
)
aaaErrorUserIdMissing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorUserIdMissing.setStatus("current")


class _AaaErrorUserIdTaken_Type(DisplayString):
    """Custom type aaaErrorUserIdTaken based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorUserIdTaken_Type.__name__ = "DisplayString"
_AaaErrorUserIdTaken_Object = MibScalar
aaaErrorUserIdTaken = _AaaErrorUserIdTaken_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 30),
    _AaaErrorUserIdTaken_Type()
)
aaaErrorUserIdTaken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorUserIdTaken.setStatus("current")


class _AaaErrorWeAreSorry_Type(DisplayString):
    """Custom type aaaErrorWeAreSorry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorWeAreSorry_Type.__name__ = "DisplayString"
_AaaErrorWeAreSorry_Object = MibScalar
aaaErrorWeAreSorry = _AaaErrorWeAreSorry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 31),
    _AaaErrorWeAreSorry_Type()
)
aaaErrorWeAreSorry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorWeAreSorry.setStatus("current")


class _AaaErrorWholeNumber_Type(DisplayString):
    """Custom type aaaErrorWholeNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorWholeNumber_Type.__name__ = "DisplayString"
_AaaErrorWholeNumber_Object = MibScalar
aaaErrorWholeNumber = _AaaErrorWholeNumber_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 32),
    _AaaErrorWholeNumber_Type()
)
aaaErrorWholeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorWholeNumber.setStatus("current")


class _AaaErrorYourAccount_Type(DisplayString):
    """Custom type aaaErrorYourAccount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaErrorYourAccount_Type.__name__ = "DisplayString"
_AaaErrorYourAccount_Object = MibScalar
aaaErrorYourAccount = _AaaErrorYourAccount_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 33),
    _AaaErrorYourAccount_Type()
)
aaaErrorYourAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaErrorYourAccount.setStatus("current")


class _AaaMessageBillingMode_Type(DisplayString):
    """Custom type aaaMessageBillingMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageBillingMode_Type.__name__ = "DisplayString"
_AaaMessageBillingMode_Object = MibScalar
aaaMessageBillingMode = _AaaMessageBillingMode_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 34),
    _AaaMessageBillingMode_Type()
)
aaaMessageBillingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageBillingMode.setStatus("current")


class _AaaMessagebyCreditCard_Type(DisplayString):
    """Custom type aaaMessagebyCreditCard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessagebyCreditCard_Type.__name__ = "DisplayString"
_AaaMessagebyCreditCard_Object = MibScalar
aaaMessagebyCreditCard = _AaaMessagebyCreditCard_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 35),
    _AaaMessagebyCreditCard_Type()
)
aaaMessagebyCreditCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessagebyCreditCard.setStatus("current")


class _AaaMessagebyHotelRoom_Type(DisplayString):
    """Custom type aaaMessagebyHotelRoom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessagebyHotelRoom_Type.__name__ = "DisplayString"
_AaaMessagebyHotelRoom_Object = MibScalar
aaaMessagebyHotelRoom = _AaaMessagebyHotelRoom_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 36),
    _AaaMessagebyHotelRoom_Type()
)
aaaMessagebyHotelRoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessagebyHotelRoom.setStatus("current")


class _AaaMessageChooseUsername_Type(DisplayString):
    """Custom type aaaMessageChooseUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageChooseUsername_Type.__name__ = "DisplayString"
_AaaMessageChooseUsername_Object = MibScalar
aaaMessageChooseUsername = _AaaMessageChooseUsername_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 37),
    _AaaMessageChooseUsername_Type()
)
aaaMessageChooseUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageChooseUsername.setStatus("current")


class _AaaMessageChoosePasswd1_Type(DisplayString):
    """Custom type aaaMessageChoosePasswd1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageChoosePasswd1_Type.__name__ = "DisplayString"
_AaaMessageChoosePasswd1_Object = MibScalar
aaaMessageChoosePasswd1 = _AaaMessageChoosePasswd1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 38),
    _AaaMessageChoosePasswd1_Type()
)
aaaMessageChoosePasswd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageChoosePasswd1.setStatus("current")


class _AaaMessageChoosePasswd2_Type(DisplayString):
    """Custom type aaaMessageChoosePasswd2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageChoosePasswd2_Type.__name__ = "DisplayString"
_AaaMessageChoosePasswd2_Object = MibScalar
aaaMessageChoosePasswd2 = _AaaMessageChoosePasswd2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 39),
    _AaaMessageChoosePasswd2_Type()
)
aaaMessageChoosePasswd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageChoosePasswd2.setStatus("current")


class _AaaMessageFreeInternet_Type(DisplayString):
    """Custom type aaaMessageFreeInternet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageFreeInternet_Type.__name__ = "DisplayString"
_AaaMessageFreeInternet_Object = MibScalar
aaaMessageFreeInternet = _AaaMessageFreeInternet_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 40),
    _AaaMessageFreeInternet_Type()
)
aaaMessageFreeInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageFreeInternet.setStatus("current")


class _AaaMessageNewUserLogin_Type(DisplayString):
    """Custom type aaaMessageNewUserLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageNewUserLogin_Type.__name__ = "DisplayString"
_AaaMessageNewUserLogin_Object = MibScalar
aaaMessageNewUserLogin = _AaaMessageNewUserLogin_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 41),
    _AaaMessageNewUserLogin_Type()
)
aaaMessageNewUserLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageNewUserLogin.setStatus("current")


class _AaaMessageOldUserLogin_Type(DisplayString):
    """Custom type aaaMessageOldUserLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageOldUserLogin_Type.__name__ = "DisplayString"
_AaaMessageOldUserLogin_Object = MibScalar
aaaMessageOldUserLogin = _AaaMessageOldUserLogin_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 42),
    _AaaMessageOldUserLogin_Type()
)
aaaMessageOldUserLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageOldUserLogin.setStatus("current")


class _AaaMessagePurchaseOK1_Type(DisplayString):
    """Custom type aaaMessagePurchaseOK1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessagePurchaseOK1_Type.__name__ = "DisplayString"
_AaaMessagePurchaseOK1_Object = MibScalar
aaaMessagePurchaseOK1 = _AaaMessagePurchaseOK1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 43),
    _AaaMessagePurchaseOK1_Type()
)
aaaMessagePurchaseOK1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessagePurchaseOK1.setStatus("current")


class _AaaMessagePurchaseOK2_Type(DisplayString):
    """Custom type aaaMessagePurchaseOK2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessagePurchaseOK2_Type.__name__ = "DisplayString"
_AaaMessagePurchaseOK2_Object = MibScalar
aaaMessagePurchaseOK2 = _AaaMessagePurchaseOK2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 44),
    _AaaMessagePurchaseOK2_Type()
)
aaaMessagePurchaseOK2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessagePurchaseOK2.setStatus("current")


class _AaaMessagePurchaseSelect_Type(DisplayString):
    """Custom type aaaMessagePurchaseSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessagePurchaseSelect_Type.__name__ = "DisplayString"
_AaaMessagePurchaseSelect_Object = MibScalar
aaaMessagePurchaseSelect = _AaaMessagePurchaseSelect_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 45),
    _AaaMessagePurchaseSelect_Type()
)
aaaMessagePurchaseSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessagePurchaseSelect.setStatus("current")


class _AaaMessageRequestFailed_Type(DisplayString):
    """Custom type aaaMessageRequestFailed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageRequestFailed_Type.__name__ = "DisplayString"
_AaaMessageRequestFailed_Object = MibScalar
aaaMessageRequestFailed = _AaaMessageRequestFailed_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 49),
    _AaaMessageRequestFailed_Type()
)
aaaMessageRequestFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageRequestFailed.setStatus("current")


class _AaaMessageRequestGranted_Type(DisplayString):
    """Custom type aaaMessageRequestGranted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageRequestGranted_Type.__name__ = "DisplayString"
_AaaMessageRequestGranted_Object = MibScalar
aaaMessageRequestGranted = _AaaMessageRequestGranted_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 50),
    _AaaMessageRequestGranted_Type()
)
aaaMessageRequestGranted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageRequestGranted.setStatus("current")


class _AaaMessageThankYou_Type(DisplayString):
    """Custom type aaaMessageThankYou based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageThankYou_Type.__name__ = "DisplayString"
_AaaMessageThankYou_Object = MibScalar
aaaMessageThankYou = _AaaMessageThankYou_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 51),
    _AaaMessageThankYou_Type()
)
aaaMessageThankYou.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageThankYou.setStatus("current")


class _AaaMessageVerifying_Type(DisplayString):
    """Custom type aaaMessageVerifying based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageVerifying_Type.__name__ = "DisplayString"
_AaaMessageVerifying_Object = MibScalar
aaaMessageVerifying = _AaaMessageVerifying_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 52),
    _AaaMessageVerifying_Type()
)
aaaMessageVerifying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageVerifying.setStatus("current")


class _AaaMessageYourHotel_Type(DisplayString):
    """Custom type aaaMessageYourHotel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageYourHotel_Type.__name__ = "DisplayString"
_AaaMessageYourHotel_Object = MibScalar
aaaMessageYourHotel = _AaaMessageYourHotel_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 53),
    _AaaMessageYourHotel_Type()
)
aaaMessageYourHotel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageYourHotel.setStatus("current")


class _AaaMessageYourPurchase_Type(DisplayString):
    """Custom type aaaMessageYourPurchase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaMessageYourPurchase_Type.__name__ = "DisplayString"
_AaaMessageYourPurchase_Object = MibScalar
aaaMessageYourPurchase = _AaaMessageYourPurchase_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 54),
    _AaaMessageYourPurchase_Type()
)
aaaMessageYourPurchase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageYourPurchase.setStatus("current")


class _AaaPartnerImageOn_Type(Integer32):
    """Custom type aaaPartnerImageOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaPartnerImageOn_Type.__name__ = "Integer32"
_AaaPartnerImageOn_Object = MibScalar
aaaPartnerImageOn = _AaaPartnerImageOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 55),
    _AaaPartnerImageOn_Type()
)
aaaPartnerImageOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPartnerImageOn.setStatus("current")


class _AaaPartnerImageFileName_Type(DisplayString):
    """Custom type aaaPartnerImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaPartnerImageFileName_Type.__name__ = "DisplayString"
_AaaPartnerImageFileName_Object = MibScalar
aaaPartnerImageFileName = _AaaPartnerImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 16, 56),
    _AaaPartnerImageFileName_Type()
)
aaaPartnerImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPartnerImageFileName.setStatus("current")
_AaaSubPostSession_ObjectIdentity = ObjectIdentity
aaaSubPostSession = _AaaSubPostSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17)
)
_AaaSubGoodbyePage_ObjectIdentity = ObjectIdentity
aaaSubGoodbyePage = _AaaSubGoodbyePage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1)
)


class _AaaSubGPEnable_Type(Integer32):
    """Custom type aaaSubGPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSubGPEnable_Type.__name__ = "Integer32"
_AaaSubGPEnable_Object = MibScalar
aaaSubGPEnable = _AaaSubGPEnable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 1),
    _AaaSubGPEnable_Type()
)
aaaSubGPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPEnable.setStatus("current")


class _AaaSubGPIPAddressOn_Type(Integer32):
    """Custom type aaaSubGPIPAddressOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSubGPIPAddressOn_Type.__name__ = "Integer32"
_AaaSubGPIPAddressOn_Object = MibScalar
aaaSubGPIPAddressOn = _AaaSubGPIPAddressOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 2),
    _AaaSubGPIPAddressOn_Type()
)
aaaSubGPIPAddressOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPIPAddressOn.setStatus("current")


class _AaaSubGPAuthenTypeOn_Type(Integer32):
    """Custom type aaaSubGPAuthenTypeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSubGPAuthenTypeOn_Type.__name__ = "Integer32"
_AaaSubGPAuthenTypeOn_Object = MibScalar
aaaSubGPAuthenTypeOn = _AaaSubGPAuthenTypeOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 3),
    _AaaSubGPAuthenTypeOn_Type()
)
aaaSubGPAuthenTypeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPAuthenTypeOn.setStatus("current")


class _AaaSubGPStartTimeOn_Type(Integer32):
    """Custom type aaaSubGPStartTimeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSubGPStartTimeOn_Type.__name__ = "Integer32"
_AaaSubGPStartTimeOn_Object = MibScalar
aaaSubGPStartTimeOn = _AaaSubGPStartTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 4),
    _AaaSubGPStartTimeOn_Type()
)
aaaSubGPStartTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPStartTimeOn.setStatus("current")


class _AaaSubGPStopTimeOn_Type(Integer32):
    """Custom type aaaSubGPStopTimeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSubGPStopTimeOn_Type.__name__ = "Integer32"
_AaaSubGPStopTimeOn_Object = MibScalar
aaaSubGPStopTimeOn = _AaaSubGPStopTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 5),
    _AaaSubGPStopTimeOn_Type()
)
aaaSubGPStopTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPStopTimeOn.setStatus("current")


class _AaaSubGPByteSentOn_Type(Integer32):
    """Custom type aaaSubGPByteSentOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSubGPByteSentOn_Type.__name__ = "Integer32"
_AaaSubGPByteSentOn_Object = MibScalar
aaaSubGPByteSentOn = _AaaSubGPByteSentOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 6),
    _AaaSubGPByteSentOn_Type()
)
aaaSubGPByteSentOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPByteSentOn.setStatus("current")


class _AaaSubGPByteReceivedOn_Type(Integer32):
    """Custom type aaaSubGPByteReceivedOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSubGPByteReceivedOn_Type.__name__ = "Integer32"
_AaaSubGPByteReceivedOn_Object = MibScalar
aaaSubGPByteReceivedOn = _AaaSubGPByteReceivedOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 7),
    _AaaSubGPByteReceivedOn_Type()
)
aaaSubGPByteReceivedOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPByteReceivedOn.setStatus("current")


class _AaaSubGPHyperlinkOn_Type(Integer32):
    """Custom type aaaSubGPHyperlinkOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSubGPHyperlinkOn_Type.__name__ = "Integer32"
_AaaSubGPHyperlinkOn_Object = MibScalar
aaaSubGPHyperlinkOn = _AaaSubGPHyperlinkOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 8),
    _AaaSubGPHyperlinkOn_Type()
)
aaaSubGPHyperlinkOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPHyperlinkOn.setStatus("current")


class _AaaSubGPHyperlink_Type(DisplayString):
    """Custom type aaaSubGPHyperlink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_AaaSubGPHyperlink_Type.__name__ = "DisplayString"
_AaaSubGPHyperlink_Object = MibScalar
aaaSubGPHyperlink = _AaaSubGPHyperlink_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 9),
    _AaaSubGPHyperlink_Type()
)
aaaSubGPHyperlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPHyperlink.setStatus("current")


class _AaaSubGPSessionSummaryLabel_Type(DisplayString):
    """Custom type aaaSubGPSessionSummaryLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaSubGPSessionSummaryLabel_Type.__name__ = "DisplayString"
_AaaSubGPSessionSummaryLabel_Object = MibScalar
aaaSubGPSessionSummaryLabel = _AaaSubGPSessionSummaryLabel_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 10),
    _AaaSubGPSessionSummaryLabel_Type()
)
aaaSubGPSessionSummaryLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPSessionSummaryLabel.setStatus("current")


class _AaaSubGPSubIPAddressLabel_Type(DisplayString):
    """Custom type aaaSubGPSubIPAddressLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaSubGPSubIPAddressLabel_Type.__name__ = "DisplayString"
_AaaSubGPSubIPAddressLabel_Object = MibScalar
aaaSubGPSubIPAddressLabel = _AaaSubGPSubIPAddressLabel_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 11),
    _AaaSubGPSubIPAddressLabel_Type()
)
aaaSubGPSubIPAddressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPSubIPAddressLabel.setStatus("current")


class _AaaSubGPAuthenTypeLabel_Type(DisplayString):
    """Custom type aaaSubGPAuthenTypeLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaSubGPAuthenTypeLabel_Type.__name__ = "DisplayString"
_AaaSubGPAuthenTypeLabel_Object = MibScalar
aaaSubGPAuthenTypeLabel = _AaaSubGPAuthenTypeLabel_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 12),
    _AaaSubGPAuthenTypeLabel_Type()
)
aaaSubGPAuthenTypeLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPAuthenTypeLabel.setStatus("current")


class _AaaSubGPStartTimeLabel_Type(DisplayString):
    """Custom type aaaSubGPStartTimeLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaSubGPStartTimeLabel_Type.__name__ = "DisplayString"
_AaaSubGPStartTimeLabel_Object = MibScalar
aaaSubGPStartTimeLabel = _AaaSubGPStartTimeLabel_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 13),
    _AaaSubGPStartTimeLabel_Type()
)
aaaSubGPStartTimeLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPStartTimeLabel.setStatus("current")


class _AaaSubGPStopTimeLabel_Type(DisplayString):
    """Custom type aaaSubGPStopTimeLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaSubGPStopTimeLabel_Type.__name__ = "DisplayString"
_AaaSubGPStopTimeLabel_Object = MibScalar
aaaSubGPStopTimeLabel = _AaaSubGPStopTimeLabel_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 14),
    _AaaSubGPStopTimeLabel_Type()
)
aaaSubGPStopTimeLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPStopTimeLabel.setStatus("current")


class _AaaSubGPByteSentLabel_Type(DisplayString):
    """Custom type aaaSubGPByteSentLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaSubGPByteSentLabel_Type.__name__ = "DisplayString"
_AaaSubGPByteSentLabel_Object = MibScalar
aaaSubGPByteSentLabel = _AaaSubGPByteSentLabel_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 15),
    _AaaSubGPByteSentLabel_Type()
)
aaaSubGPByteSentLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPByteSentLabel.setStatus("current")


class _AaaSubGPByteReceivedLabel_Type(DisplayString):
    """Custom type aaaSubGPByteReceivedLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaSubGPByteReceivedLabel_Type.__name__ = "DisplayString"
_AaaSubGPByteReceivedLabel_Object = MibScalar
aaaSubGPByteReceivedLabel = _AaaSubGPByteReceivedLabel_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 16),
    _AaaSubGPByteReceivedLabel_Type()
)
aaaSubGPByteReceivedLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPByteReceivedLabel.setStatus("current")


class _AaaSubGPHypertextURLLabel_Type(DisplayString):
    """Custom type aaaSubGPHypertextURLLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 218),
    )


_AaaSubGPHypertextURLLabel_Type.__name__ = "DisplayString"
_AaaSubGPHypertextURLLabel_Object = MibScalar
aaaSubGPHypertextURLLabel = _AaaSubGPHypertextURLLabel_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 17, 1, 17),
    _AaaSubGPHypertextURLLabel_Type()
)
aaaSubGPHypertextURLLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSubGPHypertextURLLabel.setStatus("current")
_AaaSubscriber_ObjectIdentity = ObjectIdentity
aaaSubscriber = _AaaSubscriber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18)
)
_AaaSubCurrTable_Object = MibTable
aaaSubCurrTable = _AaaSubCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1)
)
if mibBuilder.loadTexts:
    aaaSubCurrTable.setStatus("current")
_AaaSubCurrTableEntry_Object = MibTableRow
aaaSubCurrTableEntry = _AaaSubCurrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1)
)
aaaSubCurrTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "subIndex"),
)
if mibBuilder.loadTexts:
    aaaSubCurrTableEntry.setStatus("current")
_SubIndex_Type = Integer32
_SubIndex_Object = MibTableColumn
subIndex = _SubIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 1),
    _SubIndex_Type()
)
subIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subIndex.setStatus("current")
_SubMac_Type = DisplayString
_SubMac_Object = MibTableColumn
subMac = _SubMac_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 2),
    _SubMac_Type()
)
subMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subMac.setStatus("current")
_SubIp_Type = IpAddress
_SubIp_Object = MibTableColumn
subIp = _SubIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 3),
    _SubIp_Type()
)
subIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subIp.setStatus("current")
_SubPort_Type = Integer32
_SubPort_Object = MibTableColumn
subPort = _SubPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 4),
    _SubPort_Type()
)
subPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subPort.setStatus("current")
_SubName_Type = DisplayString
_SubName_Object = MibTableColumn
subName = _SubName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 5),
    _SubName_Type()
)
subName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subName.setStatus("current")
_SubBwUp_Type = Integer32
_SubBwUp_Object = MibTableColumn
subBwUp = _SubBwUp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 6),
    _SubBwUp_Type()
)
subBwUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subBwUp.setStatus("current")
_SubBwDown_Type = Integer32
_SubBwDown_Object = MibTableColumn
subBwDown = _SubBwDown_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 7),
    _SubBwDown_Type()
)
subBwDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subBwDown.setStatus("current")
_SubAaaState_Type = DisplayString
_SubAaaState_Object = MibTableColumn
subAaaState = _SubAaaState_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 8),
    _SubAaaState_Type()
)
subAaaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subAaaState.setStatus("current")
_SubExpiration_Type = DisplayString
_SubExpiration_Object = MibTableColumn
subExpiration = _SubExpiration_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 9),
    _SubExpiration_Type()
)
subExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subExpiration.setStatus("current")
_SubIdleTimeout_Type = DisplayString
_SubIdleTimeout_Object = MibTableColumn
subIdleTimeout = _SubIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 10),
    _SubIdleTimeout_Type()
)
subIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subIdleTimeout.setStatus("current")
_SubBytesSent_Type = Counter32
_SubBytesSent_Object = MibTableColumn
subBytesSent = _SubBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 11),
    _SubBytesSent_Type()
)
subBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subBytesSent.setStatus("current")
_SubBytesRec_Type = Counter32
_SubBytesRec_Object = MibTableColumn
subBytesRec = _SubBytesRec_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 12),
    _SubBytesRec_Type()
)
subBytesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subBytesRec.setStatus("current")
_SubBytesTotal_Type = Counter32
_SubBytesTotal_Object = MibTableColumn
subBytesTotal = _SubBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 13),
    _SubBytesTotal_Type()
)
subBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subBytesTotal.setStatus("current")
_SubProxy_Type = DisplayString
_SubProxy_Object = MibTableColumn
subProxy = _SubProxy_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 14),
    _SubProxy_Type()
)
subProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subProxy.setStatus("current")
_SubSsid_Type = DisplayString
_SubSsid_Object = MibTableColumn
subSsid = _SubSsid_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 15),
    _SubSsid_Type()
)
subSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSsid.setStatus("current")
_SubStatus_Type = RowStatus
_SubStatus_Object = MibTableColumn
subStatus = _SubStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 1, 1, 16),
    _SubStatus_Type()
)
subStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subStatus.setStatus("current")
_AaaAuthSubTable_Object = MibTable
aaaAuthSubTable = _AaaAuthSubTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2)
)
if mibBuilder.loadTexts:
    aaaAuthSubTable.setStatus("current")
_AaaAuthSubTableEntry_Object = MibTableRow
aaaAuthSubTableEntry = _AaaAuthSubTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1)
)
aaaAuthSubTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "authSubIndex"),
)
if mibBuilder.loadTexts:
    aaaAuthSubTableEntry.setStatus("current")
_AuthSubIndex_Type = Integer32
_AuthSubIndex_Object = MibTableColumn
authSubIndex = _AuthSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 1),
    _AuthSubIndex_Type()
)
authSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSubIndex.setStatus("current")


class _AuthSubType_Type(Integer32):
    """Custom type authSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("device", 1),
          ("subscriber", 0))
    )


_AuthSubType_Type.__name__ = "Integer32"
_AuthSubType_Object = MibTableColumn
authSubType = _AuthSubType_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 2),
    _AuthSubType_Type()
)
authSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubType.setStatus("current")


class _AuthSubDhcpAddrType_Type(Integer32):
    """Custom type authSubDhcpAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("private", 0),
          ("public", 1))
    )


_AuthSubDhcpAddrType_Type.__name__ = "Integer32"
_AuthSubDhcpAddrType_Object = MibTableColumn
authSubDhcpAddrType = _AuthSubDhcpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 3),
    _AuthSubDhcpAddrType_Type()
)
authSubDhcpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubDhcpAddrType.setStatus("current")
_AuthSubDevicePort_Type = Integer32
_AuthSubDevicePort_Object = MibTableColumn
authSubDevicePort = _AuthSubDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 4),
    _AuthSubDevicePort_Type()
)
authSubDevicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubDevicePort.setStatus("current")


class _AuthSubMac_Type(DisplayString):
    """Custom type authSubMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AuthSubMac_Type.__name__ = "DisplayString"
_AuthSubMac_Object = MibTableColumn
authSubMac = _AuthSubMac_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 5),
    _AuthSubMac_Type()
)
authSubMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubMac.setStatus("current")
_AuthSubIp_Type = IpAddress
_AuthSubIp_Object = MibTableColumn
authSubIp = _AuthSubIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 6),
    _AuthSubIp_Type()
)
authSubIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubIp.setStatus("current")


class _AuthSubName_Type(DisplayString):
    """Custom type authSubName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_AuthSubName_Type.__name__ = "DisplayString"
_AuthSubName_Object = MibTableColumn
authSubName = _AuthSubName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 7),
    _AuthSubName_Type()
)
authSubName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubName.setStatus("current")


class _AuthSubPassword_Type(DisplayString):
    """Custom type authSubPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AuthSubPassword_Type.__name__ = "DisplayString"
_AuthSubPassword_Object = MibTableColumn
authSubPassword = _AuthSubPassword_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 8),
    _AuthSubPassword_Type()
)
authSubPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubPassword.setStatus("current")


class _AuthSubCountDown_Type(Integer32):
    """Custom type authSubCountDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AuthSubCountDown_Type.__name__ = "Integer32"
_AuthSubCountDown_Object = MibTableColumn
authSubCountDown = _AuthSubCountDown_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 9),
    _AuthSubCountDown_Type()
)
authSubCountDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubCountDown.setStatus("current")
_AuthSubExpTimeHrs_Type = Integer32
_AuthSubExpTimeHrs_Object = MibTableColumn
authSubExpTimeHrs = _AuthSubExpTimeHrs_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 10),
    _AuthSubExpTimeHrs_Type()
)
authSubExpTimeHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubExpTimeHrs.setStatus("current")


class _AuthSubExpTimeMins_Type(Integer32):
    """Custom type authSubExpTimeMins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AuthSubExpTimeMins_Type.__name__ = "Integer32"
_AuthSubExpTimeMins_Object = MibTableColumn
authSubExpTimeMins = _AuthSubExpTimeMins_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 11),
    _AuthSubExpTimeMins_Type()
)
authSubExpTimeMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubExpTimeMins.setStatus("current")


class _AuthSubAmtPaid_Type(DisplayString):
    """Custom type authSubAmtPaid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AuthSubAmtPaid_Type.__name__ = "DisplayString"
_AuthSubAmtPaid_Object = MibTableColumn
authSubAmtPaid = _AuthSubAmtPaid_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 12),
    _AuthSubAmtPaid_Type()
)
authSubAmtPaid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubAmtPaid.setStatus("current")
_AuthSubAmtLeft_Type = DisplayString
_AuthSubAmtLeft_Object = MibTableColumn
authSubAmtLeft = _AuthSubAmtLeft_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 13),
    _AuthSubAmtLeft_Type()
)
authSubAmtLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSubAmtLeft.setStatus("current")


class _AuthSubUser1_Type(DisplayString):
    """Custom type authSubUser1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthSubUser1_Type.__name__ = "DisplayString"
_AuthSubUser1_Object = MibTableColumn
authSubUser1 = _AuthSubUser1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 14),
    _AuthSubUser1_Type()
)
authSubUser1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubUser1.setStatus("current")


class _AuthSubUser2_Type(DisplayString):
    """Custom type authSubUser2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthSubUser2_Type.__name__ = "DisplayString"
_AuthSubUser2_Object = MibTableColumn
authSubUser2 = _AuthSubUser2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 15),
    _AuthSubUser2_Type()
)
authSubUser2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubUser2.setStatus("current")
_AuthSubBwUp_Type = Integer32
_AuthSubBwUp_Object = MibTableColumn
authSubBwUp = _AuthSubBwUp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 16),
    _AuthSubBwUp_Type()
)
authSubBwUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubBwUp.setStatus("current")
_AuthSubBwDown_Type = Integer32
_AuthSubBwDown_Object = MibTableColumn
authSubBwDown = _AuthSubBwDown_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 17),
    _AuthSubBwDown_Type()
)
authSubBwDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubBwDown.setStatus("current")
_AuthSubConfirmation_Type = DisplayString
_AuthSubConfirmation_Object = MibTableColumn
authSubConfirmation = _AuthSubConfirmation_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 18),
    _AuthSubConfirmation_Type()
)
authSubConfirmation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSubConfirmation.setStatus("current")
_AuthSubStatus_Type = RowStatus
_AuthSubStatus_Object = MibTableColumn
authSubStatus = _AuthSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 2, 1, 19),
    _AuthSubStatus_Type()
)
authSubStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSubStatus.setStatus("current")


class _RadHistSysloggingOn_Type(Integer32):
    """Custom type radHistSysloggingOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RadHistSysloggingOn_Type.__name__ = "Integer32"
_RadHistSysloggingOn_Object = MibScalar
radHistSysloggingOn = _RadHistSysloggingOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 3),
    _RadHistSysloggingOn_Type()
)
radHistSysloggingOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radHistSysloggingOn.setStatus("current")


class _RadHistSyslogNumber_Type(Integer32):
    """Custom type radHistSyslogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RadHistSyslogNumber_Type.__name__ = "Integer32"
_RadHistSyslogNumber_Object = MibScalar
radHistSyslogNumber = _RadHistSyslogNumber_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 4),
    _RadHistSyslogNumber_Type()
)
radHistSyslogNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radHistSyslogNumber.setStatus("current")
_RadHistSyslogServerIp_Type = IpAddress
_RadHistSyslogServerIp_Object = MibScalar
radHistSyslogServerIp = _RadHistSyslogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 5),
    _RadHistSyslogServerIp_Type()
)
radHistSyslogServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radHistSyslogServerIp.setStatus("current")


class _RadProxyAcctHistLog_Type(Integer32):
    """Custom type radProxyAcctHistLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RadProxyAcctHistLog_Type.__name__ = "Integer32"
_RadProxyAcctHistLog_Object = MibScalar
radProxyAcctHistLog = _RadProxyAcctHistLog_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 6),
    _RadProxyAcctHistLog_Type()
)
radProxyAcctHistLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radProxyAcctHistLog.setStatus("current")


class _RadProxyAcctHistSyslog_Type(Integer32):
    """Custom type radProxyAcctHistSyslog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RadProxyAcctHistSyslog_Type.__name__ = "Integer32"
_RadProxyAcctHistSyslog_Object = MibScalar
radProxyAcctHistSyslog = _RadProxyAcctHistSyslog_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 7),
    _RadProxyAcctHistSyslog_Type()
)
radProxyAcctHistSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radProxyAcctHistSyslog.setStatus("current")


class _RadHistSyslogFilter_Type(Integer32):
    """Custom type radHistSyslogFilter based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_RadHistSyslogFilter_Type.__name__ = "Integer32"
_RadHistSyslogFilter_Object = MibScalar
radHistSyslogFilter = _RadHistSyslogFilter_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 8),
    _RadHistSyslogFilter_Type()
)
radHistSyslogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radHistSyslogFilter.setStatus("current")


class _RadHistSyslogSaveToFile_Type(Integer32):
    """Custom type radHistSyslogSaveToFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RadHistSyslogSaveToFile_Type.__name__ = "Integer32"
_RadHistSyslogSaveToFile_Object = MibScalar
radHistSyslogSaveToFile = _RadHistSyslogSaveToFile_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 18, 9),
    _RadHistSyslogSaveToFile_Type()
)
radHistSyslogSaveToFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radHistSyslogSaveToFile.setStatus("current")
_AaaRadius_ObjectIdentity = ObjectIdentity
aaaRadius = _AaaRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19)
)


class _AaaRadiusRoutingMode_Type(Integer32):
    """Custom type aaaRadiusRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("fixed", 2),
          ("realm-based", 1))
    )


_AaaRadiusRoutingMode_Type.__name__ = "Integer32"
_AaaRadiusRoutingMode_Object = MibScalar
aaaRadiusRoutingMode = _AaaRadiusRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 1),
    _AaaRadiusRoutingMode_Type()
)
aaaRadiusRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusRoutingMode.setStatus("current")


class _AaaRadiusDefProf_Type(DisplayString):
    """Custom type aaaRadiusDefProf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AaaRadiusDefProf_Type.__name__ = "DisplayString"
_AaaRadiusDefProf_Object = MibScalar
aaaRadiusDefProf = _AaaRadiusDefProf_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 3),
    _AaaRadiusDefProf_Type()
)
aaaRadiusDefProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusDefProf.setStatus("current")


class _AaaRadiusCacheOn_Type(Integer32):
    """Custom type aaaRadiusCacheOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusCacheOn_Type.__name__ = "Integer32"
_AaaRadiusCacheOn_Object = MibScalar
aaaRadiusCacheOn = _AaaRadiusCacheOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 5),
    _AaaRadiusCacheOn_Type()
)
aaaRadiusCacheOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusCacheOn.setStatus("current")
_AaaRadiusDefaultIdle_Type = Integer32
_AaaRadiusDefaultIdle_Object = MibScalar
aaaRadiusDefaultIdle = _AaaRadiusDefaultIdle_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 11),
    _AaaRadiusDefaultIdle_Type()
)
aaaRadiusDefaultIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusDefaultIdle.setStatus("current")


class _AaaRadiusNasIdOn_Type(Integer32):
    """Custom type aaaRadiusNasIdOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusNasIdOn_Type.__name__ = "Integer32"
_AaaRadiusNasIdOn_Object = MibScalar
aaaRadiusNasIdOn = _AaaRadiusNasIdOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 12),
    _AaaRadiusNasIdOn_Type()
)
aaaRadiusNasIdOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusNasIdOn.setStatus("current")


class _AaaRadiusNasId_Type(DisplayString):
    """Custom type aaaRadiusNasId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaRadiusNasId_Type.__name__ = "DisplayString"
_AaaRadiusNasId_Object = MibScalar
aaaRadiusNasId = _AaaRadiusNasId_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 13),
    _AaaRadiusNasId_Type()
)
aaaRadiusNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusNasId.setStatus("current")


class _AaaRadiusNasIpOn_Type(Integer32):
    """Custom type aaaRadiusNasIpOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusNasIpOn_Type.__name__ = "Integer32"
_AaaRadiusNasIpOn_Object = MibScalar
aaaRadiusNasIpOn = _AaaRadiusNasIpOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 14),
    _AaaRadiusNasIpOn_Type()
)
aaaRadiusNasIpOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusNasIpOn.setStatus("current")


class _AaaRadiusNasPortOn_Type(Integer32):
    """Custom type aaaRadiusNasPortOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusNasPortOn_Type.__name__ = "Integer32"
_AaaRadiusNasPortOn_Object = MibScalar
aaaRadiusNasPortOn = _AaaRadiusNasPortOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 15),
    _AaaRadiusNasPortOn_Type()
)
aaaRadiusNasPortOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusNasPortOn.setStatus("current")
_AaaRadiusNasPortType_Type = Integer32
_AaaRadiusNasPortType_Object = MibScalar
aaaRadiusNasPortType = _AaaRadiusNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 16),
    _AaaRadiusNasPortType_Type()
)
aaaRadiusNasPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusNasPortType.setStatus("current")


class _AaaRadiusFipOn_Type(Integer32):
    """Custom type aaaRadiusFipOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusFipOn_Type.__name__ = "Integer32"
_AaaRadiusFipOn_Object = MibScalar
aaaRadiusFipOn = _AaaRadiusFipOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 17),
    _AaaRadiusFipOn_Type()
)
aaaRadiusFipOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusFipOn.setStatus("current")


class _AaaRadiusRedUrlOn_Type(Integer32):
    """Custom type aaaRadiusRedUrlOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusRedUrlOn_Type.__name__ = "Integer32"
_AaaRadiusRedUrlOn_Object = MibScalar
aaaRadiusRedUrlOn = _AaaRadiusRedUrlOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 18),
    _AaaRadiusRedUrlOn_Type()
)
aaaRadiusRedUrlOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusRedUrlOn.setStatus("current")


class _AaaRadiusGoodbyeUrlOn_Type(Integer32):
    """Custom type aaaRadiusGoodbyeUrlOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusGoodbyeUrlOn_Type.__name__ = "Integer32"
_AaaRadiusGoodbyeUrlOn_Object = MibScalar
aaaRadiusGoodbyeUrlOn = _AaaRadiusGoodbyeUrlOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 19),
    _AaaRadiusGoodbyeUrlOn_Type()
)
aaaRadiusGoodbyeUrlOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusGoodbyeUrlOn.setStatus("current")


class _AaaRadiusForgotPasswordUrlOn_Type(Integer32):
    """Custom type aaaRadiusForgotPasswordUrlOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusForgotPasswordUrlOn_Type.__name__ = "Integer32"
_AaaRadiusForgotPasswordUrlOn_Object = MibScalar
aaaRadiusForgotPasswordUrlOn = _AaaRadiusForgotPasswordUrlOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 20),
    _AaaRadiusForgotPasswordUrlOn_Type()
)
aaaRadiusForgotPasswordUrlOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusForgotPasswordUrlOn.setStatus("current")


class _AaaRadiusForgotPasswordUrl_Type(DisplayString):
    """Custom type aaaRadiusForgotPasswordUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_AaaRadiusForgotPasswordUrl_Type.__name__ = "DisplayString"
_AaaRadiusForgotPasswordUrl_Object = MibScalar
aaaRadiusForgotPasswordUrl = _AaaRadiusForgotPasswordUrl_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 21),
    _AaaRadiusForgotPasswordUrl_Type()
)
aaaRadiusForgotPasswordUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusForgotPasswordUrl.setStatus("current")


class _AaaRadiusSubnetAttrOn_Type(Integer32):
    """Custom type aaaRadiusSubnetAttrOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusSubnetAttrOn_Type.__name__ = "Integer32"
_AaaRadiusSubnetAttrOn_Object = MibScalar
aaaRadiusSubnetAttrOn = _AaaRadiusSubnetAttrOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 22),
    _AaaRadiusSubnetAttrOn_Type()
)
aaaRadiusSubnetAttrOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusSubnetAttrOn.setStatus("current")


class _AaaRadiusNetVlanOn_Type(Integer32):
    """Custom type aaaRadiusNetVlanOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusNetVlanOn_Type.__name__ = "Integer32"
_AaaRadiusNetVlanOn_Object = MibScalar
aaaRadiusNetVlanOn = _AaaRadiusNetVlanOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 23),
    _AaaRadiusNetVlanOn_Type()
)
aaaRadiusNetVlanOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusNetVlanOn.setStatus("current")


class _AaaRadiusNetVlanDefaultOn_Type(Integer32):
    """Custom type aaaRadiusNetVlanDefaultOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusNetVlanDefaultOn_Type.__name__ = "Integer32"
_AaaRadiusNetVlanDefaultOn_Object = MibScalar
aaaRadiusNetVlanDefaultOn = _AaaRadiusNetVlanDefaultOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 24),
    _AaaRadiusNetVlanDefaultOn_Type()
)
aaaRadiusNetVlanDefaultOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusNetVlanDefaultOn.setStatus("current")


class _AaaRadiusNetVlanDefaultTag_Type(Integer32):
    """Custom type aaaRadiusNetVlanDefaultTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AaaRadiusNetVlanDefaultTag_Type.__name__ = "Integer32"
_AaaRadiusNetVlanDefaultTag_Object = MibScalar
aaaRadiusNetVlanDefaultTag = _AaaRadiusNetVlanDefaultTag_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 25),
    _AaaRadiusNetVlanDefaultTag_Type()
)
aaaRadiusNetVlanDefaultTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusNetVlanDefaultTag.setStatus("current")
_AaaRadiusLocalAuthPort_Type = Integer32
_AaaRadiusLocalAuthPort_Object = MibScalar
aaaRadiusLocalAuthPort = _AaaRadiusLocalAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 26),
    _AaaRadiusLocalAuthPort_Type()
)
aaaRadiusLocalAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusLocalAuthPort.setStatus("current")
_AaaRadiusLocalAcctPort_Type = Integer32
_AaaRadiusLocalAcctPort_Object = MibScalar
aaaRadiusLocalAcctPort = _AaaRadiusLocalAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 27),
    _AaaRadiusLocalAcctPort_Type()
)
aaaRadiusLocalAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusLocalAcctPort.setStatus("current")
_AaaRadiusLoginRefresh_Type = Integer32
_AaaRadiusLoginRefresh_Object = MibScalar
aaaRadiusLoginRefresh = _AaaRadiusLoginRefresh_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 28),
    _AaaRadiusLoginRefresh_Type()
)
aaaRadiusLoginRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusLoginRefresh.setStatus("current")


class _AaaRadiusTerminationActionOn_Type(Integer32):
    """Custom type aaaRadiusTerminationActionOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaRadiusTerminationActionOn_Type.__name__ = "Integer32"
_AaaRadiusTerminationActionOn_Object = MibScalar
aaaRadiusTerminationActionOn = _AaaRadiusTerminationActionOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 19, 29),
    _AaaRadiusTerminationActionOn_Type()
)
aaaRadiusTerminationActionOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusTerminationActionOn.setStatus("current")


class _AaaLogFilter_Type(Integer32):
    """Custom type aaaLogFilter based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_AaaLogFilter_Type.__name__ = "Integer32"
_AaaLogFilter_Object = MibScalar
aaaLogFilter = _AaaLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 20),
    _AaaLogFilter_Type()
)
aaaLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaLogFilter.setStatus("current")


class _AaaSaveToFile_Type(Integer32):
    """Custom type aaaSaveToFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaSaveToFile_Type.__name__ = "Integer32"
_AaaSaveToFile_Object = MibScalar
aaaSaveToFile = _AaaSaveToFile_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 21),
    _AaaSaveToFile_Type()
)
aaaSaveToFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSaveToFile.setStatus("current")
_AaaXmlSender2Ip_Type = IpAddress
_AaaXmlSender2Ip_Object = MibScalar
aaaXmlSender2Ip = _AaaXmlSender2Ip_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 22),
    _AaaXmlSender2Ip_Type()
)
aaaXmlSender2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaXmlSender2Ip.setStatus("current")


class _AaaMessageNewUserTermsOn_Type(Integer32):
    """Custom type aaaMessageNewUserTermsOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaMessageNewUserTermsOn_Type.__name__ = "Integer32"
_AaaMessageNewUserTermsOn_Object = MibScalar
aaaMessageNewUserTermsOn = _AaaMessageNewUserTermsOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 23),
    _AaaMessageNewUserTermsOn_Type()
)
aaaMessageNewUserTermsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageNewUserTermsOn.setStatus("current")


class _AaaMessageNewUserTerms_Type(DisplayString):
    """Custom type aaaMessageNewUserTerms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(400, 400),
    )


_AaaMessageNewUserTerms_Type.__name__ = "DisplayString"
_AaaMessageNewUserTerms_Object = MibScalar
aaaMessageNewUserTerms = _AaaMessageNewUserTerms_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 24),
    _AaaMessageNewUserTerms_Type()
)
aaaMessageNewUserTerms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaMessageNewUserTerms.setStatus("current")
_AaaLoginPageFailover_ObjectIdentity = ObjectIdentity
aaaLoginPageFailover = _AaaLoginPageFailover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 25)
)


class _AaaLoginPageFailoverOn_Type(Integer32):
    """Custom type aaaLoginPageFailoverOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AaaLoginPageFailoverOn_Type.__name__ = "Integer32"
_AaaLoginPageFailoverOn_Object = MibScalar
aaaLoginPageFailoverOn = _AaaLoginPageFailoverOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 25, 1),
    _AaaLoginPageFailoverOn_Type()
)
aaaLoginPageFailoverOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaLoginPageFailoverOn.setStatus("current")
_AaaLpfStatusTable_Object = MibTable
aaaLpfStatusTable = _AaaLpfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 25, 2)
)
if mibBuilder.loadTexts:
    aaaLpfStatusTable.setStatus("current")
_AaaLpfStatusTableEntry_Object = MibTableRow
aaaLpfStatusTableEntry = _AaaLpfStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 25, 2, 1)
)
aaaLpfStatusTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "lpfEntryIndex"),
)
if mibBuilder.loadTexts:
    aaaLpfStatusTableEntry.setStatus("current")
_LpfEntryIndex_Type = Integer32
_LpfEntryIndex_Object = MibTableColumn
lpfEntryIndex = _LpfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 25, 2, 1, 1),
    _LpfEntryIndex_Type()
)
lpfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpfEntryIndex.setStatus("current")


class _LpfEntryNickname_Type(DisplayString):
    """Custom type lpfEntryNickname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_LpfEntryNickname_Type.__name__ = "DisplayString"
_LpfEntryNickname_Object = MibTableColumn
lpfEntryNickname = _LpfEntryNickname_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 25, 2, 1, 2),
    _LpfEntryNickname_Type()
)
lpfEntryNickname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpfEntryNickname.setStatus("current")


class _LpfEntryOnlineStatus_Type(Integer32):
    """Custom type lpfEntryOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("unknown", 0))
    )


_LpfEntryOnlineStatus_Type.__name__ = "Integer32"
_LpfEntryOnlineStatus_Object = MibTableColumn
lpfEntryOnlineStatus = _LpfEntryOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 2, 25, 2, 1, 3),
    _LpfEntryOnlineStatus_Type()
)
lpfEntryOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpfEntryOnlineStatus.setStatus("current")
_AccessControl_ObjectIdentity = ObjectIdentity
accessControl = _AccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4)
)


class _BlockTelnetAccessOn_Type(Integer32):
    """Custom type blockTelnetAccessOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BlockTelnetAccessOn_Type.__name__ = "Integer32"
_BlockTelnetAccessOn_Object = MibScalar
blockTelnetAccessOn = _BlockTelnetAccessOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 1),
    _BlockTelnetAccessOn_Type()
)
blockTelnetAccessOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockTelnetAccessOn.setStatus("current")


class _BlockWebAccessOn_Type(Integer32):
    """Custom type blockWebAccessOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BlockWebAccessOn_Type.__name__ = "Integer32"
_BlockWebAccessOn_Object = MibScalar
blockWebAccessOn = _BlockWebAccessOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 2),
    _BlockWebAccessOn_Type()
)
blockWebAccessOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockWebAccessOn.setStatus("current")


class _BlockFtpAccessOn_Type(Integer32):
    """Custom type blockFtpAccessOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BlockFtpAccessOn_Type.__name__ = "Integer32"
_BlockFtpAccessOn_Object = MibScalar
blockFtpAccessOn = _BlockFtpAccessOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 3),
    _BlockFtpAccessOn_Type()
)
blockFtpAccessOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockFtpAccessOn.setStatus("current")


class _AccessControlOn_Type(Integer32):
    """Custom type accessControlOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AccessControlOn_Type.__name__ = "Integer32"
_AccessControlOn_Object = MibScalar
accessControlOn = _AccessControlOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 4),
    _AccessControlOn_Type()
)
accessControlOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlOn.setStatus("current")
_AccessControlIpTable_Object = MibTable
accessControlIpTable = _AccessControlIpTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 5)
)
if mibBuilder.loadTexts:
    accessControlIpTable.setStatus("current")
_AccessControlIpEntry_Object = MibTableRow
accessControlIpEntry = _AccessControlIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 5, 1)
)
accessControlIpEntry.setIndexNames(
    (0, "NOMADIX-MIB", "acIndex"),
)
if mibBuilder.loadTexts:
    accessControlIpEntry.setStatus("current")
_AcIndex_Type = Integer32
_AcIndex_Object = MibTableColumn
acIndex = _AcIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 5, 1, 2),
    _AcIndex_Type()
)
acIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIndex.setStatus("current")
_AcStartAddress_Type = IpAddress
_AcStartAddress_Object = MibTableColumn
acStartAddress = _AcStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 5, 1, 4),
    _AcStartAddress_Type()
)
acStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStartAddress.setStatus("current")
_AcEndAddress_Type = IpAddress
_AcEndAddress_Object = MibTableColumn
acEndAddress = _AcEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 5, 1, 6),
    _AcEndAddress_Type()
)
acEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEndAddress.setStatus("current")
_AcStatus_Type = RowStatus
_AcStatus_Object = MibTableColumn
acStatus = _AcStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 5, 1, 7),
    _AcStatus_Type()
)
acStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStatus.setStatus("current")


class _BlockSFTPAccessOn_Type(Integer32):
    """Custom type blockSFTPAccessOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BlockSFTPAccessOn_Type.__name__ = "Integer32"
_BlockSFTPAccessOn_Object = MibScalar
blockSFTPAccessOn = _BlockSFTPAccessOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 6),
    _BlockSFTPAccessOn_Type()
)
blockSFTPAccessOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockSFTPAccessOn.setStatus("current")


class _BlockSSHShellAccessOn_Type(Integer32):
    """Custom type blockSSHShellAccessOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BlockSSHShellAccessOn_Type.__name__ = "Integer32"
_BlockSSHShellAccessOn_Object = MibScalar
blockSSHShellAccessOn = _BlockSSHShellAccessOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 4, 7),
    _BlockSSHShellAccessOn_Type()
)
blockSSHShellAccessOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockSSHShellAccessOn.setStatus("current")
_BandwidthManagement_ObjectIdentity = ObjectIdentity
bandwidthManagement = _BandwidthManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 5)
)


class _BandwidthManagementOn_Type(Integer32):
    """Custom type bandwidthManagementOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BandwidthManagementOn_Type.__name__ = "Integer32"
_BandwidthManagementOn_Object = MibScalar
bandwidthManagementOn = _BandwidthManagementOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 5, 1),
    _BandwidthManagementOn_Type()
)
bandwidthManagementOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthManagementOn.setStatus("current")
_BwmUpWanLinkSpeed_Type = Integer32
_BwmUpWanLinkSpeed_Object = MibScalar
bwmUpWanLinkSpeed = _BwmUpWanLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 5, 3),
    _BwmUpWanLinkSpeed_Type()
)
bwmUpWanLinkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmUpWanLinkSpeed.setStatus("current")
_BwmDownWanLinkSpeed_Type = Integer32
_BwmDownWanLinkSpeed_Object = MibScalar
bwmDownWanLinkSpeed = _BwmDownWanLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 5, 5),
    _BwmDownWanLinkSpeed_Type()
)
bwmDownWanLinkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmDownWanLinkSpeed.setStatus("current")
_BillRecMirror_ObjectIdentity = ObjectIdentity
billRecMirror = _BillRecMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6)
)


class _BrmMirrorOn_Type(Integer32):
    """Custom type brmMirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BrmMirrorOn_Type.__name__ = "Integer32"
_BrmMirrorOn_Object = MibScalar
brmMirrorOn = _BrmMirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 1),
    _BrmMirrorOn_Type()
)
brmMirrorOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmMirrorOn.setStatus("current")


class _BrmPropertyId_Type(DisplayString):
    """Custom type brmPropertyId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrmPropertyId_Type.__name__ = "DisplayString"
_BrmPropertyId_Object = MibScalar
brmPropertyId = _BrmPropertyId_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 2),
    _BrmPropertyId_Type()
)
brmPropertyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmPropertyId.setStatus("current")


class _BrmNseId_Type(DisplayString):
    """Custom type brmNseId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrmNseId_Type.__name__ = "DisplayString"
_BrmNseId_Object = MibScalar
brmNseId = _BrmNseId_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 3),
    _BrmNseId_Type()
)
brmNseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brmNseId.setStatus("current")
_BrmServerIpPrimary_Type = IpAddress
_BrmServerIpPrimary_Object = MibScalar
brmServerIpPrimary = _BrmServerIpPrimary_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 4),
    _BrmServerIpPrimary_Type()
)
brmServerIpPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerIpPrimary.setStatus("current")


class _BrmServerUrlPrimary_Type(DisplayString):
    """Custom type brmServerUrlPrimary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_BrmServerUrlPrimary_Type.__name__ = "DisplayString"
_BrmServerUrlPrimary_Object = MibScalar
brmServerUrlPrimary = _BrmServerUrlPrimary_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 5),
    _BrmServerUrlPrimary_Type()
)
brmServerUrlPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerUrlPrimary.setStatus("current")


class _BrmServerSecretPrimary_Type(DisplayString):
    """Custom type brmServerSecretPrimary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrmServerSecretPrimary_Type.__name__ = "DisplayString"
_BrmServerSecretPrimary_Object = MibScalar
brmServerSecretPrimary = _BrmServerSecretPrimary_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 6),
    _BrmServerSecretPrimary_Type()
)
brmServerSecretPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerSecretPrimary.setStatus("current")
_BrmServerPortPrimary_Type = Integer32
_BrmServerPortPrimary_Object = MibScalar
brmServerPortPrimary = _BrmServerPortPrimary_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 7),
    _BrmServerPortPrimary_Type()
)
brmServerPortPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerPortPrimary.setStatus("current")
_BrmServerIpSecondary_Type = IpAddress
_BrmServerIpSecondary_Object = MibScalar
brmServerIpSecondary = _BrmServerIpSecondary_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 8),
    _BrmServerIpSecondary_Type()
)
brmServerIpSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerIpSecondary.setStatus("current")


class _BrmServerUrlSecondary_Type(DisplayString):
    """Custom type brmServerUrlSecondary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_BrmServerUrlSecondary_Type.__name__ = "DisplayString"
_BrmServerUrlSecondary_Object = MibScalar
brmServerUrlSecondary = _BrmServerUrlSecondary_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 9),
    _BrmServerUrlSecondary_Type()
)
brmServerUrlSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerUrlSecondary.setStatus("current")


class _BrmServerSecretSecondary_Type(DisplayString):
    """Custom type brmServerSecretSecondary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrmServerSecretSecondary_Type.__name__ = "DisplayString"
_BrmServerSecretSecondary_Object = MibScalar
brmServerSecretSecondary = _BrmServerSecretSecondary_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 10),
    _BrmServerSecretSecondary_Type()
)
brmServerSecretSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerSecretSecondary.setStatus("current")
_BrmServerPortSecondary_Type = Integer32
_BrmServerPortSecondary_Object = MibScalar
brmServerPortSecondary = _BrmServerPortSecondary_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 11),
    _BrmServerPortSecondary_Type()
)
brmServerPortSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerPortSecondary.setStatus("current")
_BrmServerCCIpOne_Type = IpAddress
_BrmServerCCIpOne_Object = MibScalar
brmServerCCIpOne = _BrmServerCCIpOne_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 12),
    _BrmServerCCIpOne_Type()
)
brmServerCCIpOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCIpOne.setStatus("current")


class _BrmServerCCUrlOne_Type(DisplayString):
    """Custom type brmServerCCUrlOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_BrmServerCCUrlOne_Type.__name__ = "DisplayString"
_BrmServerCCUrlOne_Object = MibScalar
brmServerCCUrlOne = _BrmServerCCUrlOne_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 13),
    _BrmServerCCUrlOne_Type()
)
brmServerCCUrlOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCUrlOne.setStatus("current")


class _BrmServerCCSecretOne_Type(DisplayString):
    """Custom type brmServerCCSecretOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrmServerCCSecretOne_Type.__name__ = "DisplayString"
_BrmServerCCSecretOne_Object = MibScalar
brmServerCCSecretOne = _BrmServerCCSecretOne_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 14),
    _BrmServerCCSecretOne_Type()
)
brmServerCCSecretOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCSecretOne.setStatus("current")
_BrmServerCCPortOne_Type = Integer32
_BrmServerCCPortOne_Object = MibScalar
brmServerCCPortOne = _BrmServerCCPortOne_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 15),
    _BrmServerCCPortOne_Type()
)
brmServerCCPortOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCPortOne.setStatus("current")
_BrmServerCCIpTwo_Type = IpAddress
_BrmServerCCIpTwo_Object = MibScalar
brmServerCCIpTwo = _BrmServerCCIpTwo_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 16),
    _BrmServerCCIpTwo_Type()
)
brmServerCCIpTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCIpTwo.setStatus("current")


class _BrmServerCCUrlTwo_Type(DisplayString):
    """Custom type brmServerCCUrlTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_BrmServerCCUrlTwo_Type.__name__ = "DisplayString"
_BrmServerCCUrlTwo_Object = MibScalar
brmServerCCUrlTwo = _BrmServerCCUrlTwo_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 17),
    _BrmServerCCUrlTwo_Type()
)
brmServerCCUrlTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCUrlTwo.setStatus("current")


class _BrmServerCCSecretTwo_Type(DisplayString):
    """Custom type brmServerCCSecretTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrmServerCCSecretTwo_Type.__name__ = "DisplayString"
_BrmServerCCSecretTwo_Object = MibScalar
brmServerCCSecretTwo = _BrmServerCCSecretTwo_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 18),
    _BrmServerCCSecretTwo_Type()
)
brmServerCCSecretTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCSecretTwo.setStatus("current")
_BrmServerCCPortTwo_Type = Integer32
_BrmServerCCPortTwo_Object = MibScalar
brmServerCCPortTwo = _BrmServerCCPortTwo_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 19),
    _BrmServerCCPortTwo_Type()
)
brmServerCCPortTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCPortTwo.setStatus("current")
_BrmServerCCIpThree_Type = IpAddress
_BrmServerCCIpThree_Object = MibScalar
brmServerCCIpThree = _BrmServerCCIpThree_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 20),
    _BrmServerCCIpThree_Type()
)
brmServerCCIpThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCIpThree.setStatus("current")


class _BrmServerCCUrlThree_Type(DisplayString):
    """Custom type brmServerCCUrlThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_BrmServerCCUrlThree_Type.__name__ = "DisplayString"
_BrmServerCCUrlThree_Object = MibScalar
brmServerCCUrlThree = _BrmServerCCUrlThree_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 21),
    _BrmServerCCUrlThree_Type()
)
brmServerCCUrlThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCUrlThree.setStatus("current")


class _BrmServerCCSecretThree_Type(DisplayString):
    """Custom type brmServerCCSecretThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrmServerCCSecretThree_Type.__name__ = "DisplayString"
_BrmServerCCSecretThree_Object = MibScalar
brmServerCCSecretThree = _BrmServerCCSecretThree_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 22),
    _BrmServerCCSecretThree_Type()
)
brmServerCCSecretThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCSecretThree.setStatus("current")
_BrmServerCCPortThree_Type = Integer32
_BrmServerCCPortThree_Object = MibScalar
brmServerCCPortThree = _BrmServerCCPortThree_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 23),
    _BrmServerCCPortThree_Type()
)
brmServerCCPortThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmServerCCPortThree.setStatus("current")


class _BrmRetransMethod_Type(Integer32):
    """Custom type brmRetransMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("notAlternate", 2))
    )


_BrmRetransMethod_Type.__name__ = "Integer32"
_BrmRetransMethod_Object = MibScalar
brmRetransMethod = _BrmRetransMethod_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 24),
    _BrmRetransMethod_Type()
)
brmRetransMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmRetransMethod.setStatus("current")
_BrmRetransAttempts_Type = Integer32
_BrmRetransAttempts_Object = MibScalar
brmRetransAttempts = _BrmRetransAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 25),
    _BrmRetransAttempts_Type()
)
brmRetransAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmRetransAttempts.setStatus("current")
_BrmRetransDelay_Type = Integer32
_BrmRetransDelay_Object = MibScalar
brmRetransDelay = _BrmRetransDelay_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 6, 26),
    _BrmRetransDelay_Type()
)
brmRetransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmRetransDelay.setStatus("current")
_Dat_ObjectIdentity = ObjectIdentity
dat = _Dat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8)
)
_DatSessionTable_Object = MibTable
datSessionTable = _DatSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1)
)
if mibBuilder.loadTexts:
    datSessionTable.setStatus("current")
_DatSessionTableEntry_Object = MibTableRow
datSessionTableEntry = _DatSessionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1)
)
datSessionTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "datNetPort"),
)
if mibBuilder.loadTexts:
    datSessionTableEntry.setStatus("current")
_DatSubIp_Type = IpAddress
_DatSubIp_Object = MibTableColumn
datSubIp = _DatSubIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1, 1),
    _DatSubIp_Type()
)
datSubIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datSubIp.setStatus("current")
_DatSubPort_Type = Integer32
_DatSubPort_Object = MibTableColumn
datSubPort = _DatSubPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1, 2),
    _DatSubPort_Type()
)
datSubPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datSubPort.setStatus("current")
_DatSubMac_Type = DisplayString
_DatSubMac_Object = MibTableColumn
datSubMac = _DatSubMac_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1, 3),
    _DatSubMac_Type()
)
datSubMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datSubMac.setStatus("current")
_DatNetIp_Type = IpAddress
_DatNetIp_Object = MibTableColumn
datNetIp = _DatNetIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1, 4),
    _DatNetIp_Type()
)
datNetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datNetIp.setStatus("current")
_DatNetPort_Type = Integer32
_DatNetPort_Object = MibTableColumn
datNetPort = _DatNetPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1, 5),
    _DatNetPort_Type()
)
datNetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datNetPort.setStatus("current")
_DatDestIp_Type = IpAddress
_DatDestIp_Object = MibTableColumn
datDestIp = _DatDestIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1, 6),
    _DatDestIp_Type()
)
datDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datDestIp.setStatus("current")
_DatDestPort_Type = Integer32
_DatDestPort_Object = MibTableColumn
datDestPort = _DatDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1, 7),
    _DatDestPort_Type()
)
datDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datDestPort.setStatus("current")
_DatProto_Type = DisplayString
_DatProto_Object = MibTableColumn
datProto = _DatProto_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1, 8),
    _DatProto_Type()
)
datProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datProto.setStatus("current")
_DatSessState_Type = DisplayString
_DatSessState_Object = MibTableColumn
datSessState = _DatSessState_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1, 9),
    _DatSessState_Type()
)
datSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datSessState.setStatus("current")
_DatTimeout_Type = Integer32
_DatTimeout_Object = MibTableColumn
datTimeout = _DatTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 8, 1, 1, 10),
    _DatTimeout_Type()
)
datTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datTimeout.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10)
)


class _DhcpDisable_Type(Integer32):
    """Custom type dhcpDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DhcpDisable_Type.__name__ = "Integer32"
_DhcpDisable_Object = MibScalar
dhcpDisable = _DhcpDisable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 1),
    _DhcpDisable_Type()
)
dhcpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpDisable.setStatus("current")


class _DhcpIpUpsell_Type(Integer32):
    """Custom type dhcpIpUpsell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpIpUpsell_Type.__name__ = "Integer32"
_DhcpIpUpsell_Object = MibScalar
dhcpIpUpsell = _DhcpIpUpsell_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 2),
    _DhcpIpUpsell_Type()
)
dhcpIpUpsell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpIpUpsell.setStatus("current")
_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3)
)


class _DhcpServerEnable_Type(Integer32):
    """Custom type dhcpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpServerEnable_Type.__name__ = "Integer32"
_DhcpServerEnable_Object = MibScalar
dhcpServerEnable = _DhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 2),
    _DhcpServerEnable_Type()
)
dhcpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerEnable.setStatus("current")


class _DhcpServerSubnetBased_Type(Integer32):
    """Custom type dhcpServerSubnetBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpServerSubnetBased_Type.__name__ = "Integer32"
_DhcpServerSubnetBased_Object = MibScalar
dhcpServerSubnetBased = _DhcpServerSubnetBased_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 3),
    _DhcpServerSubnetBased_Type()
)
dhcpServerSubnetBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerSubnetBased.setStatus("current")
_DhcpServerTable_Object = MibTable
dhcpServerTable = _DhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4)
)
if mibBuilder.loadTexts:
    dhcpServerTable.setStatus("current")
_DhcpPoolTableEntry_Object = MibTableRow
dhcpPoolTableEntry = _DhcpPoolTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1)
)
dhcpPoolTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "poolIndex"),
)
if mibBuilder.loadTexts:
    dhcpPoolTableEntry.setStatus("current")
_PoolIndex_Type = Integer32
_PoolIndex_Object = MibTableColumn
poolIndex = _PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1, 2),
    _PoolIndex_Type()
)
poolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolIndex.setStatus("current")
_ServerIp_Type = IpAddress
_ServerIp_Object = MibTableColumn
serverIp = _ServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1, 4),
    _ServerIp_Type()
)
serverIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverIp.setStatus("current")
_NetMask_Type = IpAddress
_NetMask_Object = MibTableColumn
netMask = _NetMask_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1, 6),
    _NetMask_Type()
)
netMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMask.setStatus("current")
_PoolStartIp_Type = IpAddress
_PoolStartIp_Object = MibTableColumn
poolStartIp = _PoolStartIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1, 8),
    _PoolStartIp_Type()
)
poolStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poolStartIp.setStatus("current")
_PoolStopIp_Type = IpAddress
_PoolStopIp_Object = MibTableColumn
poolStopIp = _PoolStopIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1, 10),
    _PoolStopIp_Type()
)
poolStopIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poolStopIp.setStatus("current")
_LeaseMinutes_Type = Integer32
_LeaseMinutes_Object = MibTableColumn
leaseMinutes = _LeaseMinutes_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1, 12),
    _LeaseMinutes_Type()
)
leaseMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leaseMinutes.setStatus("current")


class _PublicPool_Type(Integer32):
    """Custom type publicPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PublicPool_Type.__name__ = "Integer32"
_PublicPool_Object = MibTableColumn
publicPool = _PublicPool_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1, 14),
    _PublicPool_Type()
)
publicPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicPool.setStatus("current")


class _IpUpSell_Type(Integer32):
    """Custom type ipUpSell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IpUpSell_Type.__name__ = "Integer32"
_IpUpSell_Object = MibTableColumn
ipUpSell = _IpUpSell_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1, 16),
    _IpUpSell_Type()
)
ipUpSell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipUpSell.setStatus("current")


class _DefaultPool_Type(Integer32):
    """Custom type defaultPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DefaultPool_Type.__name__ = "Integer32"
_DefaultPool_Object = MibTableColumn
defaultPool = _DefaultPool_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1, 18),
    _DefaultPool_Type()
)
defaultPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultPool.setStatus("current")
_PoolStatus_Type = RowStatus
_PoolStatus_Object = MibTableColumn
poolStatus = _PoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 4, 1, 20),
    _PoolStatus_Type()
)
poolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poolStatus.setStatus("current")
_DhcpLeaseTable_Object = MibTable
dhcpLeaseTable = _DhcpLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 6)
)
if mibBuilder.loadTexts:
    dhcpLeaseTable.setStatus("current")
_DhcpLeaseTableEntry_Object = MibTableRow
dhcpLeaseTableEntry = _DhcpLeaseTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 6, 1)
)
dhcpLeaseTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "leaseIndex"),
)
if mibBuilder.loadTexts:
    dhcpLeaseTableEntry.setStatus("current")
_LeaseIndex_Type = Integer32
_LeaseIndex_Object = MibTableColumn
leaseIndex = _LeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 6, 1, 2),
    _LeaseIndex_Type()
)
leaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leaseIndex.setStatus("current")
_LeaseAddress_Type = IpAddress
_LeaseAddress_Object = MibTableColumn
leaseAddress = _LeaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 6, 1, 4),
    _LeaseAddress_Type()
)
leaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leaseAddress.setStatus("current")
_LeaseCLID_Type = MacAddress
_LeaseCLID_Object = MibTableColumn
leaseCLID = _LeaseCLID_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 6, 1, 6),
    _LeaseCLID_Type()
)
leaseCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leaseCLID.setStatus("current")


class _LeaseStatus_Type(Integer32):
    """Custom type leaseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("available", 0),
          ("reserved", 1))
    )


_LeaseStatus_Type.__name__ = "Integer32"
_LeaseStatus_Object = MibTableColumn
leaseStatus = _LeaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 3, 6, 1, 7),
    _LeaseStatus_Type()
)
leaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leaseStatus.setStatus("current")
_DhcpRelay_ObjectIdentity = ObjectIdentity
dhcpRelay = _DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 10)
)


class _DhcpRelayEnable_Type(Integer32):
    """Custom type dhcpRelayEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpRelayEnable_Type.__name__ = "Integer32"
_DhcpRelayEnable_Object = MibScalar
dhcpRelayEnable = _DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 10, 2),
    _DhcpRelayEnable_Type()
)
dhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayEnable.setStatus("current")
_DhcpRelayAgentIP_Type = IpAddress
_DhcpRelayAgentIP_Object = MibScalar
dhcpRelayAgentIP = _DhcpRelayAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 10, 4),
    _DhcpRelayAgentIP_Type()
)
dhcpRelayAgentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayAgentIP.setStatus("current")
_DhcpRelayServerIP_Type = IpAddress
_DhcpRelayServerIP_Object = MibScalar
dhcpRelayServerIP = _DhcpRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 10, 10, 5),
    _DhcpRelayServerIP_Type()
)
dhcpRelayServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayServerIP.setStatus("current")
_Dns_ObjectIdentity = ObjectIdentity
dns = _Dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 12)
)


class _DnsHostName_Type(DisplayString):
    """Custom type dnsHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DnsHostName_Type.__name__ = "DisplayString"
_DnsHostName_Object = MibScalar
dnsHostName = _DnsHostName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 12, 1),
    _DnsHostName_Type()
)
dnsHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsHostName.setStatus("current")


class _DnsDomain_Type(DisplayString):
    """Custom type dnsDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DnsDomain_Type.__name__ = "DisplayString"
_DnsDomain_Object = MibScalar
dnsDomain = _DnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 12, 2),
    _DnsDomain_Type()
)
dnsDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomain.setStatus("current")
_DnsPrimaryServer_Type = IpAddress
_DnsPrimaryServer_Object = MibScalar
dnsPrimaryServer = _DnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 12, 3),
    _DnsPrimaryServer_Type()
)
dnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsPrimaryServer.setStatus("current")
_DnsSecondaryServer_Type = IpAddress
_DnsSecondaryServer_Object = MibScalar
dnsSecondaryServer = _DnsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 12, 4),
    _DnsSecondaryServer_Type()
)
dnsSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsSecondaryServer.setStatus("current")
_DnsTertiaryServer_Type = IpAddress
_DnsTertiaryServer_Object = MibScalar
dnsTertiaryServer = _DnsTertiaryServer_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 12, 5),
    _DnsTertiaryServer_Type()
)
dnsTertiaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsTertiaryServer.setStatus("current")
_GreTunneling_ObjectIdentity = ObjectIdentity
greTunneling = _GreTunneling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 13)
)


class _GreTunnelingEnable_Type(Integer32):
    """Custom type greTunnelingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GreTunnelingEnable_Type.__name__ = "Integer32"
_GreTunnelingEnable_Object = MibScalar
greTunnelingEnable = _GreTunnelingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 13, 1),
    _GreTunnelingEnable_Type()
)
greTunnelingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greTunnelingEnable.setStatus("current")
_GreVpnConcentratorIp_Type = IpAddress
_GreVpnConcentratorIp_Object = MibScalar
greVpnConcentratorIp = _GreVpnConcentratorIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 13, 2),
    _GreVpnConcentratorIp_Type()
)
greVpnConcentratorIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greVpnConcentratorIp.setStatus("current")
_GreInterfaceIp_Type = IpAddress
_GreInterfaceIp_Object = MibScalar
greInterfaceIp = _GreInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 13, 3),
    _GreInterfaceIp_Type()
)
greInterfaceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greInterfaceIp.setStatus("current")
_GreInterfaceNetmask_Type = IpAddress
_GreInterfaceNetmask_Object = MibScalar
greInterfaceNetmask = _GreInterfaceNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 13, 4),
    _GreInterfaceNetmask_Type()
)
greInterfaceNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greInterfaceNetmask.setStatus("current")
_GreInterfaceGateway_Type = IpAddress
_GreInterfaceGateway_Object = MibScalar
greInterfaceGateway = _GreInterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 13, 5),
    _GreInterfaceGateway_Type()
)
greInterfaceGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greInterfaceGateway.setStatus("current")
_Hpr_ObjectIdentity = ObjectIdentity
hpr = _Hpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 14)
)


class _HprOn_Type(Integer32):
    """Custom type hprOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HprOn_Type.__name__ = "Integer32"
_HprOn_Object = MibScalar
hprOn = _HprOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 14, 1),
    _HprOn_Type()
)
hprOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hprOn.setStatus("current")


class _HprUrl_Type(DisplayString):
    """Custom type hprUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_HprUrl_Type.__name__ = "DisplayString"
_HprUrl_Object = MibScalar
hprUrl = _HprUrl_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 14, 2),
    _HprUrl_Type()
)
hprUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hprUrl.setStatus("current")


class _HprParameterPassing_Type(Integer32):
    """Custom type hprParameterPassing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HprParameterPassing_Type.__name__ = "Integer32"
_HprParameterPassing_Object = MibScalar
hprParameterPassing = _HprParameterPassing_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 14, 3),
    _HprParameterPassing_Type()
)
hprParameterPassing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hprParameterPassing.setStatus("current")
_HprRedirectionFrequency_Type = Integer32
_HprRedirectionFrequency_Object = MibScalar
hprRedirectionFrequency = _HprRedirectionFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 14, 4),
    _HprRedirectionFrequency_Type()
)
hprRedirectionFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hprRedirectionFrequency.setStatus("current")
_Icc_ObjectIdentity = ObjectIdentity
icc = _Icc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16)
)


class _IccOn_Type(Integer32):
    """Custom type iccOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IccOn_Type.__name__ = "Integer32"
_IccOn_Object = MibScalar
iccOn = _IccOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 1),
    _IccOn_Type()
)
iccOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccOn.setStatus("current")


class _IccTitle_Type(DisplayString):
    """Custom type iccTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccTitle_Type.__name__ = "DisplayString"
_IccTitle_Object = MibScalar
iccTitle = _IccTitle_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 2),
    _IccTitle_Type()
)
iccTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccTitle.setStatus("current")


class _IccLogoutOption_Type(Integer32):
    """Custom type iccLogoutOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("logout", 2),
          ("redisplay", 0))
    )


_IccLogoutOption_Type.__name__ = "Integer32"
_IccLogoutOption_Object = MibScalar
iccLogoutOption = _IccLogoutOption_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 3),
    _IccLogoutOption_Type()
)
iccLogoutOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccLogoutOption.setStatus("current")


class _IccLanguageOption_Type(Integer32):
    """Custom type iccLanguageOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("chinese", 1),
          ("english", 0),
          ("french", 2),
          ("german", 3),
          ("japanese", 4),
          ("other", 6),
          ("spanish", 5))
    )


_IccLanguageOption_Type.__name__ = "Integer32"
_IccLanguageOption_Object = MibScalar
iccLanguageOption = _IccLanguageOption_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 5),
    _IccLanguageOption_Type()
)
iccLanguageOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccLanguageOption.setStatus("current")


class _IccTimerOption_Type(Integer32):
    """Custom type iccTimerOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("elapsed", 1),
          ("remaining", 0))
    )


_IccTimerOption_Type.__name__ = "Integer32"
_IccTimerOption_Object = MibScalar
iccTimerOption = _IccTimerOption_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 6),
    _IccTimerOption_Type()
)
iccTimerOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccTimerOption.setStatus("current")


class _IccCharSetOption_Type(Integer32):
    """Custom type iccCharSetOption based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("chinese-big5", 2),
          ("chinese-euc-cn", 3),
          ("chinese-euc-tw", 4),
          ("chinese-gb2312", 5),
          ("default", 0),
          ("japanese-euc-jp", 6),
          ("japanese-iso-2022-jp", 7),
          ("japanese-shift-jis", 8),
          ("korean-euc-kr", 9),
          ("korean-iso-2022-kr", 10),
          ("korean-ks-c-5601", 11),
          ("western-iso-8859-1", 1))
    )


_IccCharSetOption_Type.__name__ = "Integer32"
_IccCharSetOption_Object = MibScalar
iccCharSetOption = _IccCharSetOption_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 7),
    _IccCharSetOption_Type()
)
iccCharSetOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccCharSetOption.setStatus("current")
_IccButtons_ObjectIdentity = ObjectIdentity
iccButtons = _IccButtons_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10)
)
_IccISPLogoButton_ObjectIdentity = ObjectIdentity
iccISPLogoButton = _IccISPLogoButton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 5)
)


class _IccISPLogoButtonName_Type(DisplayString):
    """Custom type iccISPLogoButtonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_IccISPLogoButtonName_Type.__name__ = "DisplayString"
_IccISPLogoButtonName_Object = MibScalar
iccISPLogoButtonName = _IccISPLogoButtonName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 5, 1),
    _IccISPLogoButtonName_Type()
)
iccISPLogoButtonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccISPLogoButtonName.setStatus("current")


class _IccISPLogoButtonURL_Type(DisplayString):
    """Custom type iccISPLogoButtonURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccISPLogoButtonURL_Type.__name__ = "DisplayString"
_IccISPLogoButtonURL_Object = MibScalar
iccISPLogoButtonURL = _IccISPLogoButtonURL_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 5, 2),
    _IccISPLogoButtonURL_Type()
)
iccISPLogoButtonURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccISPLogoButtonURL.setStatus("current")


class _IccISPLogoButtonImgName_Type(DisplayString):
    """Custom type iccISPLogoButtonImgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccISPLogoButtonImgName_Type.__name__ = "DisplayString"
_IccISPLogoButtonImgName_Object = MibScalar
iccISPLogoButtonImgName = _IccISPLogoButtonImgName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 5, 3),
    _IccISPLogoButtonImgName_Type()
)
iccISPLogoButtonImgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccISPLogoButtonImgName.setStatus("current")
_IccButton2_ObjectIdentity = ObjectIdentity
iccButton2 = _IccButton2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 6)
)


class _IccButtonName2_Type(DisplayString):
    """Custom type iccButtonName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_IccButtonName2_Type.__name__ = "DisplayString"
_IccButtonName2_Object = MibScalar
iccButtonName2 = _IccButtonName2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 6, 1),
    _IccButtonName2_Type()
)
iccButtonName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonName2.setStatus("current")


class _IccButtonURL2_Type(DisplayString):
    """Custom type iccButtonURL2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccButtonURL2_Type.__name__ = "DisplayString"
_IccButtonURL2_Object = MibScalar
iccButtonURL2 = _IccButtonURL2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 6, 2),
    _IccButtonURL2_Type()
)
iccButtonURL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonURL2.setStatus("current")


class _IccButtonImgName2_Type(DisplayString):
    """Custom type iccButtonImgName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccButtonImgName2_Type.__name__ = "DisplayString"
_IccButtonImgName2_Object = MibScalar
iccButtonImgName2 = _IccButtonImgName2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 6, 3),
    _IccButtonImgName2_Type()
)
iccButtonImgName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonImgName2.setStatus("current")
_IccButton3_ObjectIdentity = ObjectIdentity
iccButton3 = _IccButton3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 7)
)


class _IccButtonName3_Type(DisplayString):
    """Custom type iccButtonName3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_IccButtonName3_Type.__name__ = "DisplayString"
_IccButtonName3_Object = MibScalar
iccButtonName3 = _IccButtonName3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 7, 1),
    _IccButtonName3_Type()
)
iccButtonName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonName3.setStatus("current")


class _IccButtonURL3_Type(DisplayString):
    """Custom type iccButtonURL3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccButtonURL3_Type.__name__ = "DisplayString"
_IccButtonURL3_Object = MibScalar
iccButtonURL3 = _IccButtonURL3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 7, 2),
    _IccButtonURL3_Type()
)
iccButtonURL3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonURL3.setStatus("current")


class _IccButtonImgName3_Type(DisplayString):
    """Custom type iccButtonImgName3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccButtonImgName3_Type.__name__ = "DisplayString"
_IccButtonImgName3_Object = MibScalar
iccButtonImgName3 = _IccButtonImgName3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 7, 3),
    _IccButtonImgName3_Type()
)
iccButtonImgName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonImgName3.setStatus("current")
_IccButton4_ObjectIdentity = ObjectIdentity
iccButton4 = _IccButton4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 8)
)


class _IccButtonName4_Type(DisplayString):
    """Custom type iccButtonName4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_IccButtonName4_Type.__name__ = "DisplayString"
_IccButtonName4_Object = MibScalar
iccButtonName4 = _IccButtonName4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 8, 1),
    _IccButtonName4_Type()
)
iccButtonName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonName4.setStatus("current")


class _IccButtonURL4_Type(DisplayString):
    """Custom type iccButtonURL4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccButtonURL4_Type.__name__ = "DisplayString"
_IccButtonURL4_Object = MibScalar
iccButtonURL4 = _IccButtonURL4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 8, 2),
    _IccButtonURL4_Type()
)
iccButtonURL4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonURL4.setStatus("current")


class _IccButtonImgName4_Type(DisplayString):
    """Custom type iccButtonImgName4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccButtonImgName4_Type.__name__ = "DisplayString"
_IccButtonImgName4_Object = MibScalar
iccButtonImgName4 = _IccButtonImgName4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 8, 3),
    _IccButtonImgName4_Type()
)
iccButtonImgName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonImgName4.setStatus("current")
_IccButton5_ObjectIdentity = ObjectIdentity
iccButton5 = _IccButton5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 9)
)


class _IccButtonName5_Type(DisplayString):
    """Custom type iccButtonName5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_IccButtonName5_Type.__name__ = "DisplayString"
_IccButtonName5_Object = MibScalar
iccButtonName5 = _IccButtonName5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 9, 1),
    _IccButtonName5_Type()
)
iccButtonName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonName5.setStatus("current")


class _IccButtonURL5_Type(DisplayString):
    """Custom type iccButtonURL5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccButtonURL5_Type.__name__ = "DisplayString"
_IccButtonURL5_Object = MibScalar
iccButtonURL5 = _IccButtonURL5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 9, 2),
    _IccButtonURL5_Type()
)
iccButtonURL5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonURL5.setStatus("current")


class _IccButtonImgName5_Type(DisplayString):
    """Custom type iccButtonImgName5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccButtonImgName5_Type.__name__ = "DisplayString"
_IccButtonImgName5_Object = MibScalar
iccButtonImgName5 = _IccButtonImgName5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 9, 3),
    _IccButtonImgName5_Type()
)
iccButtonImgName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonImgName5.setStatus("current")
_IccButton6_ObjectIdentity = ObjectIdentity
iccButton6 = _IccButton6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 10)
)


class _IccButtonName6_Type(DisplayString):
    """Custom type iccButtonName6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_IccButtonName6_Type.__name__ = "DisplayString"
_IccButtonName6_Object = MibScalar
iccButtonName6 = _IccButtonName6_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 10, 1),
    _IccButtonName6_Type()
)
iccButtonName6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonName6.setStatus("current")


class _IccButtonURL6_Type(DisplayString):
    """Custom type iccButtonURL6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccButtonURL6_Type.__name__ = "DisplayString"
_IccButtonURL6_Object = MibScalar
iccButtonURL6 = _IccButtonURL6_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 10, 2),
    _IccButtonURL6_Type()
)
iccButtonURL6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonURL6.setStatus("current")


class _IccButtonImgName6_Type(DisplayString):
    """Custom type iccButtonImgName6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccButtonImgName6_Type.__name__ = "DisplayString"
_IccButtonImgName6_Object = MibScalar
iccButtonImgName6 = _IccButtonImgName6_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 10, 3),
    _IccButtonImgName6_Type()
)
iccButtonImgName6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonImgName6.setStatus("current")
_IccButton7_ObjectIdentity = ObjectIdentity
iccButton7 = _IccButton7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 11)
)


class _IccButtonName7_Type(DisplayString):
    """Custom type iccButtonName7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_IccButtonName7_Type.__name__ = "DisplayString"
_IccButtonName7_Object = MibScalar
iccButtonName7 = _IccButtonName7_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 11, 1),
    _IccButtonName7_Type()
)
iccButtonName7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonName7.setStatus("current")


class _IccButtonURL7_Type(DisplayString):
    """Custom type iccButtonURL7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccButtonURL7_Type.__name__ = "DisplayString"
_IccButtonURL7_Object = MibScalar
iccButtonURL7 = _IccButtonURL7_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 11, 2),
    _IccButtonURL7_Type()
)
iccButtonURL7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonURL7.setStatus("current")


class _IccButtonImgName7_Type(DisplayString):
    """Custom type iccButtonImgName7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccButtonImgName7_Type.__name__ = "DisplayString"
_IccButtonImgName7_Object = MibScalar
iccButtonImgName7 = _IccButtonImgName7_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 11, 3),
    _IccButtonImgName7_Type()
)
iccButtonImgName7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonImgName7.setStatus("current")
_IccButton8_ObjectIdentity = ObjectIdentity
iccButton8 = _IccButton8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 12)
)


class _IccButtonName8_Type(DisplayString):
    """Custom type iccButtonName8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_IccButtonName8_Type.__name__ = "DisplayString"
_IccButtonName8_Object = MibScalar
iccButtonName8 = _IccButtonName8_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 12, 1),
    _IccButtonName8_Type()
)
iccButtonName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonName8.setStatus("current")


class _IccButtonURL8_Type(DisplayString):
    """Custom type iccButtonURL8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccButtonURL8_Type.__name__ = "DisplayString"
_IccButtonURL8_Object = MibScalar
iccButtonURL8 = _IccButtonURL8_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 12, 2),
    _IccButtonURL8_Type()
)
iccButtonURL8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonURL8.setStatus("current")


class _IccButtonImgName8_Type(DisplayString):
    """Custom type iccButtonImgName8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccButtonImgName8_Type.__name__ = "DisplayString"
_IccButtonImgName8_Object = MibScalar
iccButtonImgName8 = _IccButtonImgName8_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 12, 3),
    _IccButtonImgName8_Type()
)
iccButtonImgName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonImgName8.setStatus("current")
_IccButton9_ObjectIdentity = ObjectIdentity
iccButton9 = _IccButton9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 13)
)


class _IccButtonName9_Type(DisplayString):
    """Custom type iccButtonName9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_IccButtonName9_Type.__name__ = "DisplayString"
_IccButtonName9_Object = MibScalar
iccButtonName9 = _IccButtonName9_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 13, 1),
    _IccButtonName9_Type()
)
iccButtonName9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonName9.setStatus("current")


class _IccButtonURL9_Type(DisplayString):
    """Custom type iccButtonURL9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccButtonURL9_Type.__name__ = "DisplayString"
_IccButtonURL9_Object = MibScalar
iccButtonURL9 = _IccButtonURL9_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 13, 2),
    _IccButtonURL9_Type()
)
iccButtonURL9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonURL9.setStatus("current")


class _IccButtonImgName9_Type(DisplayString):
    """Custom type iccButtonImgName9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccButtonImgName9_Type.__name__ = "DisplayString"
_IccButtonImgName9_Object = MibScalar
iccButtonImgName9 = _IccButtonImgName9_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 10, 13, 3),
    _IccButtonImgName9_Type()
)
iccButtonImgName9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccButtonImgName9.setStatus("current")
_IccBanners_ObjectIdentity = ObjectIdentity
iccBanners = _IccBanners_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14)
)
_IccBanner1_ObjectIdentity = ObjectIdentity
iccBanner1 = _IccBanner1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 14)
)


class _IccBannerName1_Type(DisplayString):
    """Custom type iccBannerName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IccBannerName1_Type.__name__ = "DisplayString"
_IccBannerName1_Object = MibScalar
iccBannerName1 = _IccBannerName1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 14, 1),
    _IccBannerName1_Type()
)
iccBannerName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerName1.setStatus("current")


class _IccBannerURL1_Type(DisplayString):
    """Custom type iccBannerURL1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccBannerURL1_Type.__name__ = "DisplayString"
_IccBannerURL1_Object = MibScalar
iccBannerURL1 = _IccBannerURL1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 14, 2),
    _IccBannerURL1_Type()
)
iccBannerURL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerURL1.setStatus("current")


class _IccBannerImgName1_Type(DisplayString):
    """Custom type iccBannerImgName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccBannerImgName1_Type.__name__ = "DisplayString"
_IccBannerImgName1_Object = MibScalar
iccBannerImgName1 = _IccBannerImgName1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 14, 3),
    _IccBannerImgName1_Type()
)
iccBannerImgName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerImgName1.setStatus("current")
_IccBannerDuration1_Type = Integer32
_IccBannerDuration1_Object = MibScalar
iccBannerDuration1 = _IccBannerDuration1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 14, 4),
    _IccBannerDuration1_Type()
)
iccBannerDuration1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerDuration1.setStatus("current")


class _IccBannerStartTime1_Type(DisplayString):
    """Custom type iccBannerStartTime1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IccBannerStartTime1_Type.__name__ = "DisplayString"
_IccBannerStartTime1_Object = MibScalar
iccBannerStartTime1 = _IccBannerStartTime1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 14, 5),
    _IccBannerStartTime1_Type()
)
iccBannerStartTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerStartTime1.setStatus("current")


class _IccBannerStopTime1_Type(DisplayString):
    """Custom type iccBannerStopTime1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IccBannerStopTime1_Type.__name__ = "DisplayString"
_IccBannerStopTime1_Object = MibScalar
iccBannerStopTime1 = _IccBannerStopTime1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 14, 6),
    _IccBannerStopTime1_Type()
)
iccBannerStopTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerStopTime1.setStatus("current")
_IccBanner2_ObjectIdentity = ObjectIdentity
iccBanner2 = _IccBanner2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 15)
)


class _IccBannerName2_Type(DisplayString):
    """Custom type iccBannerName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IccBannerName2_Type.__name__ = "DisplayString"
_IccBannerName2_Object = MibScalar
iccBannerName2 = _IccBannerName2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 15, 1),
    _IccBannerName2_Type()
)
iccBannerName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerName2.setStatus("current")


class _IccBannerURL2_Type(DisplayString):
    """Custom type iccBannerURL2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccBannerURL2_Type.__name__ = "DisplayString"
_IccBannerURL2_Object = MibScalar
iccBannerURL2 = _IccBannerURL2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 15, 2),
    _IccBannerURL2_Type()
)
iccBannerURL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerURL2.setStatus("current")


class _IccBannerImgName2_Type(DisplayString):
    """Custom type iccBannerImgName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccBannerImgName2_Type.__name__ = "DisplayString"
_IccBannerImgName2_Object = MibScalar
iccBannerImgName2 = _IccBannerImgName2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 15, 3),
    _IccBannerImgName2_Type()
)
iccBannerImgName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerImgName2.setStatus("current")
_IccBannerDuration2_Type = Integer32
_IccBannerDuration2_Object = MibScalar
iccBannerDuration2 = _IccBannerDuration2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 15, 4),
    _IccBannerDuration2_Type()
)
iccBannerDuration2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerDuration2.setStatus("current")


class _IccBannerStartTime2_Type(DisplayString):
    """Custom type iccBannerStartTime2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IccBannerStartTime2_Type.__name__ = "DisplayString"
_IccBannerStartTime2_Object = MibScalar
iccBannerStartTime2 = _IccBannerStartTime2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 15, 5),
    _IccBannerStartTime2_Type()
)
iccBannerStartTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerStartTime2.setStatus("current")


class _IccBannerStopTime2_Type(DisplayString):
    """Custom type iccBannerStopTime2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IccBannerStopTime2_Type.__name__ = "DisplayString"
_IccBannerStopTime2_Object = MibScalar
iccBannerStopTime2 = _IccBannerStopTime2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 15, 6),
    _IccBannerStopTime2_Type()
)
iccBannerStopTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerStopTime2.setStatus("current")
_IccBanner3_ObjectIdentity = ObjectIdentity
iccBanner3 = _IccBanner3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 16)
)


class _IccBannerName3_Type(DisplayString):
    """Custom type iccBannerName3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IccBannerName3_Type.__name__ = "DisplayString"
_IccBannerName3_Object = MibScalar
iccBannerName3 = _IccBannerName3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 16, 1),
    _IccBannerName3_Type()
)
iccBannerName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerName3.setStatus("current")


class _IccBannerURL3_Type(DisplayString):
    """Custom type iccBannerURL3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccBannerURL3_Type.__name__ = "DisplayString"
_IccBannerURL3_Object = MibScalar
iccBannerURL3 = _IccBannerURL3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 16, 2),
    _IccBannerURL3_Type()
)
iccBannerURL3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerURL3.setStatus("current")


class _IccBannerImgName3_Type(DisplayString):
    """Custom type iccBannerImgName3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccBannerImgName3_Type.__name__ = "DisplayString"
_IccBannerImgName3_Object = MibScalar
iccBannerImgName3 = _IccBannerImgName3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 16, 3),
    _IccBannerImgName3_Type()
)
iccBannerImgName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerImgName3.setStatus("current")
_IccBannerDuration3_Type = Integer32
_IccBannerDuration3_Object = MibScalar
iccBannerDuration3 = _IccBannerDuration3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 16, 4),
    _IccBannerDuration3_Type()
)
iccBannerDuration3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerDuration3.setStatus("current")


class _IccBannerStartTime3_Type(DisplayString):
    """Custom type iccBannerStartTime3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IccBannerStartTime3_Type.__name__ = "DisplayString"
_IccBannerStartTime3_Object = MibScalar
iccBannerStartTime3 = _IccBannerStartTime3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 16, 5),
    _IccBannerStartTime3_Type()
)
iccBannerStartTime3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerStartTime3.setStatus("current")


class _IccBannerStopTime3_Type(DisplayString):
    """Custom type iccBannerStopTime3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IccBannerStopTime3_Type.__name__ = "DisplayString"
_IccBannerStopTime3_Object = MibScalar
iccBannerStopTime3 = _IccBannerStopTime3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 16, 6),
    _IccBannerStopTime3_Type()
)
iccBannerStopTime3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerStopTime3.setStatus("current")
_IccBanner4_ObjectIdentity = ObjectIdentity
iccBanner4 = _IccBanner4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 17)
)


class _IccBannerName4_Type(DisplayString):
    """Custom type iccBannerName4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IccBannerName4_Type.__name__ = "DisplayString"
_IccBannerName4_Object = MibScalar
iccBannerName4 = _IccBannerName4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 17, 1),
    _IccBannerName4_Type()
)
iccBannerName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerName4.setStatus("current")


class _IccBannerURL4_Type(DisplayString):
    """Custom type iccBannerURL4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccBannerURL4_Type.__name__ = "DisplayString"
_IccBannerURL4_Object = MibScalar
iccBannerURL4 = _IccBannerURL4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 17, 2),
    _IccBannerURL4_Type()
)
iccBannerURL4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerURL4.setStatus("current")


class _IccBannerImgName4_Type(DisplayString):
    """Custom type iccBannerImgName4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccBannerImgName4_Type.__name__ = "DisplayString"
_IccBannerImgName4_Object = MibScalar
iccBannerImgName4 = _IccBannerImgName4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 17, 3),
    _IccBannerImgName4_Type()
)
iccBannerImgName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerImgName4.setStatus("current")
_IccBannerDuration4_Type = Integer32
_IccBannerDuration4_Object = MibScalar
iccBannerDuration4 = _IccBannerDuration4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 17, 4),
    _IccBannerDuration4_Type()
)
iccBannerDuration4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerDuration4.setStatus("current")


class _IccBannerStartTime4_Type(DisplayString):
    """Custom type iccBannerStartTime4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IccBannerStartTime4_Type.__name__ = "DisplayString"
_IccBannerStartTime4_Object = MibScalar
iccBannerStartTime4 = _IccBannerStartTime4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 17, 5),
    _IccBannerStartTime4_Type()
)
iccBannerStartTime4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerStartTime4.setStatus("current")


class _IccBannerStopTime4_Type(DisplayString):
    """Custom type iccBannerStopTime4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IccBannerStopTime4_Type.__name__ = "DisplayString"
_IccBannerStopTime4_Object = MibScalar
iccBannerStopTime4 = _IccBannerStopTime4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 17, 6),
    _IccBannerStopTime4_Type()
)
iccBannerStopTime4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerStopTime4.setStatus("current")
_IccBanner5_ObjectIdentity = ObjectIdentity
iccBanner5 = _IccBanner5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 18)
)


class _IccBannerName5_Type(DisplayString):
    """Custom type iccBannerName5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IccBannerName5_Type.__name__ = "DisplayString"
_IccBannerName5_Object = MibScalar
iccBannerName5 = _IccBannerName5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 18, 1),
    _IccBannerName5_Type()
)
iccBannerName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerName5.setStatus("current")


class _IccBannerURL5_Type(DisplayString):
    """Custom type iccBannerURL5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_IccBannerURL5_Type.__name__ = "DisplayString"
_IccBannerURL5_Object = MibScalar
iccBannerURL5 = _IccBannerURL5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 18, 2),
    _IccBannerURL5_Type()
)
iccBannerURL5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerURL5.setStatus("current")


class _IccBannerImgName5_Type(DisplayString):
    """Custom type iccBannerImgName5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IccBannerImgName5_Type.__name__ = "DisplayString"
_IccBannerImgName5_Object = MibScalar
iccBannerImgName5 = _IccBannerImgName5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 18, 3),
    _IccBannerImgName5_Type()
)
iccBannerImgName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerImgName5.setStatus("current")
_IccBannerDuration5_Type = Integer32
_IccBannerDuration5_Object = MibScalar
iccBannerDuration5 = _IccBannerDuration5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 18, 4),
    _IccBannerDuration5_Type()
)
iccBannerDuration5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerDuration5.setStatus("current")


class _IccBannerStartTime5_Type(DisplayString):
    """Custom type iccBannerStartTime5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IccBannerStartTime5_Type.__name__ = "DisplayString"
_IccBannerStartTime5_Object = MibScalar
iccBannerStartTime5 = _IccBannerStartTime5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 18, 5),
    _IccBannerStartTime5_Type()
)
iccBannerStartTime5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerStartTime5.setStatus("current")


class _IccBannerStopTime5_Type(DisplayString):
    """Custom type iccBannerStopTime5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IccBannerStopTime5_Type.__name__ = "DisplayString"
_IccBannerStopTime5_Object = MibScalar
iccBannerStopTime5 = _IccBannerStopTime5_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 16, 14, 18, 6),
    _IccBannerStopTime5_Type()
)
iccBannerStopTime5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iccBannerStopTime5.setStatus("current")
_Inat_ObjectIdentity = ObjectIdentity
inat = _Inat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17)
)


class _InatOn_Type(Integer32):
    """Custom type inatOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_InatOn_Type.__name__ = "Integer32"
_InatOn_Object = MibScalar
inatOn = _InatOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17, 1),
    _InatOn_Type()
)
inatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inatOn.setStatus("current")


class _PptpOn_Type(Integer32):
    """Custom type pptpOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PptpOn_Type.__name__ = "Integer32"
_PptpOn_Object = MibScalar
pptpOn = _PptpOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17, 2),
    _PptpOn_Type()
)
pptpOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpOn.setStatus("current")


class _IpsecOn_Type(Integer32):
    """Custom type ipsecOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecOn_Type.__name__ = "Integer32"
_IpsecOn_Object = MibScalar
ipsecOn = _IpsecOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17, 3),
    _IpsecOn_Type()
)
ipsecOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecOn.setStatus("current")


class _PptpidOn_Type(Integer32):
    """Custom type pptpidOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PptpidOn_Type.__name__ = "Integer32"
_PptpidOn_Object = MibScalar
pptpidOn = _PptpidOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17, 4),
    _PptpidOn_Type()
)
pptpidOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpidOn.setStatus("current")
_InatIpTable_Object = MibTable
inatIpTable = _InatIpTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17, 5)
)
if mibBuilder.loadTexts:
    inatIpTable.setStatus("current")
_InatIpEntry_Object = MibTableRow
inatIpEntry = _InatIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17, 5, 1)
)
inatIpEntry.setIndexNames(
    (0, "NOMADIX-MIB", "inatIndex"),
)
if mibBuilder.loadTexts:
    inatIpEntry.setStatus("current")
_InatIndex_Type = Integer32
_InatIndex_Object = MibTableColumn
inatIndex = _InatIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17, 5, 1, 2),
    _InatIndex_Type()
)
inatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inatIndex.setStatus("current")
_InatStartAddress_Type = IpAddress
_InatStartAddress_Object = MibTableColumn
inatStartAddress = _InatStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17, 5, 1, 4),
    _InatStartAddress_Type()
)
inatStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inatStartAddress.setStatus("current")
_InatEndAddress_Type = IpAddress
_InatEndAddress_Object = MibTableColumn
inatEndAddress = _InatEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17, 5, 1, 6),
    _InatEndAddress_Type()
)
inatEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inatEndAddress.setStatus("current")
_InatEntryStatus_Type = RowStatus
_InatEntryStatus_Object = MibTableColumn
inatEntryStatus = _InatEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 17, 5, 1, 10),
    _InatEntryStatus_Type()
)
inatEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inatEntryStatus.setStatus("current")
_LicenseKeys_ObjectIdentity = ObjectIdentity
licenseKeys = _LicenseKeys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 18)
)


class _LkKey_Type(DisplayString):
    """Custom type lkKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LkKey_Type.__name__ = "DisplayString"
_LkKey_Object = MibScalar
lkKey = _LkKey_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 18, 1),
    _LkKey_Type()
)
lkKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lkKey.setStatus("current")


class _LkModelNo_Type(DisplayString):
    """Custom type lkModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_LkModelNo_Type.__name__ = "DisplayString"
_LkModelNo_Object = MibScalar
lkModelNo = _LkModelNo_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 18, 2),
    _LkModelNo_Type()
)
lkModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lkModelNo.setStatus("current")
_LkMaxNumSubs_Type = Integer32
_LkMaxNumSubs_Object = MibScalar
lkMaxNumSubs = _LkMaxNumSubs_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 18, 3),
    _LkMaxNumSubs_Type()
)
lkMaxNumSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lkMaxNumSubs.setStatus("current")
_LkFeatureList_Object = MibTable
lkFeatureList = _LkFeatureList_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 18, 4)
)
if mibBuilder.loadTexts:
    lkFeatureList.setStatus("current")
_LkFeatureListEntry_Object = MibTableRow
lkFeatureListEntry = _LkFeatureListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 18, 4, 1)
)
lkFeatureListEntry.setIndexNames(
    (0, "NOMADIX-MIB", "lkFeatureIndex"),
)
if mibBuilder.loadTexts:
    lkFeatureListEntry.setStatus("current")
_LkFeatureIndex_Type = Integer32
_LkFeatureIndex_Object = MibTableColumn
lkFeatureIndex = _LkFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 18, 4, 1, 1),
    _LkFeatureIndex_Type()
)
lkFeatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lkFeatureIndex.setStatus("current")


class _LkFeatureName_Type(DisplayString):
    """Custom type lkFeatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_LkFeatureName_Type.__name__ = "DisplayString"
_LkFeatureName_Object = MibTableColumn
lkFeatureName = _LkFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 18, 4, 1, 2),
    _LkFeatureName_Type()
)
lkFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lkFeatureName.setStatus("current")


class _LkFeatureStatus_Type(Integer32):
    """Custom type lkFeatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPurchased", 0),
          ("purchased", 1))
    )


_LkFeatureStatus_Type.__name__ = "Integer32"
_LkFeatureStatus_Object = MibTableColumn
lkFeatureStatus = _LkFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 18, 4, 1, 3),
    _LkFeatureStatus_Type()
)
lkFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lkFeatureStatus.setStatus("current")
_Location_ObjectIdentity = ObjectIdentity
location = _Location_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19)
)


class _LocationCompanyName_Type(DisplayString):
    """Custom type locationCompanyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 39),
    )


_LocationCompanyName_Type.__name__ = "DisplayString"
_LocationCompanyName_Object = MibScalar
locationCompanyName = _LocationCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 1),
    _LocationCompanyName_Type()
)
locationCompanyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationCompanyName.setStatus("current")


class _LocationSiteName_Type(DisplayString):
    """Custom type locationSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_LocationSiteName_Type.__name__ = "DisplayString"
_LocationSiteName_Object = MibScalar
locationSiteName = _LocationSiteName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 2),
    _LocationSiteName_Type()
)
locationSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationSiteName.setStatus("current")


class _LocationAddress1_Type(DisplayString):
    """Custom type locationAddress1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_LocationAddress1_Type.__name__ = "DisplayString"
_LocationAddress1_Object = MibScalar
locationAddress1 = _LocationAddress1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 3),
    _LocationAddress1_Type()
)
locationAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationAddress1.setStatus("current")


class _LocationAddress2_Type(DisplayString):
    """Custom type locationAddress2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_LocationAddress2_Type.__name__ = "DisplayString"
_LocationAddress2_Object = MibScalar
locationAddress2 = _LocationAddress2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 4),
    _LocationAddress2_Type()
)
locationAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationAddress2.setStatus("current")


class _LocationCity_Type(DisplayString):
    """Custom type locationCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 39),
    )


_LocationCity_Type.__name__ = "DisplayString"
_LocationCity_Object = MibScalar
locationCity = _LocationCity_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 5),
    _LocationCity_Type()
)
locationCity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationCity.setStatus("current")


class _LocationState_Type(DisplayString):
    """Custom type locationState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 39),
    )


_LocationState_Type.__name__ = "DisplayString"
_LocationState_Object = MibScalar
locationState = _LocationState_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 6),
    _LocationState_Type()
)
locationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationState.setStatus("current")


class _LocationZip_Type(DisplayString):
    """Custom type locationZip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_LocationZip_Type.__name__ = "DisplayString"
_LocationZip_Object = MibScalar
locationZip = _LocationZip_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 7),
    _LocationZip_Type()
)
locationZip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationZip.setStatus("current")


class _LocationCountry_Type(DisplayString):
    """Custom type locationCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 39),
    )


_LocationCountry_Type.__name__ = "DisplayString"
_LocationCountry_Object = MibScalar
locationCountry = _LocationCountry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 8),
    _LocationCountry_Type()
)
locationCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationCountry.setStatus("current")


class _LocationEmail_Type(DisplayString):
    """Custom type locationEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 39),
    )


_LocationEmail_Type.__name__ = "DisplayString"
_LocationEmail_Object = MibScalar
locationEmail = _LocationEmail_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 9),
    _LocationEmail_Type()
)
locationEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationEmail.setStatus("current")


class _LocationVenueType_Type(Integer32):
    """Custom type locationVenueType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("apartment", 1),
          ("bar-coffeeshop-restaurant", 2),
          ("convention-center", 3),
          ("corporate-guest-access", 4),
          ("education", 5),
          ("hospitality", 6),
          ("marina-camp-ground", 7),
          ("other", 10),
          ("public-space", 8),
          ("public-transport", 9))
    )


_LocationVenueType_Type.__name__ = "Integer32"
_LocationVenueType_Object = MibScalar
locationVenueType = _LocationVenueType_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 10),
    _LocationVenueType_Type()
)
locationVenueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationVenueType.setStatus("current")
_LocationNetworkIp_Type = IpAddress
_LocationNetworkIp_Object = MibScalar
locationNetworkIp = _LocationNetworkIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 12),
    _LocationNetworkIp_Type()
)
locationNetworkIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationNetworkIp.setStatus("current")
_LocationNetmask_Type = IpAddress
_LocationNetmask_Object = MibScalar
locationNetmask = _LocationNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 13),
    _LocationNetmask_Type()
)
locationNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationNetmask.setStatus("current")
_LocationGateway_Type = IpAddress
_LocationGateway_Object = MibScalar
locationGateway = _LocationGateway_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 14),
    _LocationGateway_Type()
)
locationGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationGateway.setStatus("current")


class _LocationNetIntfCfgMode_Type(Integer32):
    """Custom type locationNetIntfCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpClient", 1),
          ("pppoeClient", 2),
          ("static", 0))
    )


_LocationNetIntfCfgMode_Type.__name__ = "Integer32"
_LocationNetIntfCfgMode_Object = MibScalar
locationNetIntfCfgMode = _LocationNetIntfCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 15),
    _LocationNetIntfCfgMode_Type()
)
locationNetIntfCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationNetIntfCfgMode.setStatus("current")


class _LocationIsoCountryCode_Type(DisplayString):
    """Custom type locationIsoCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_LocationIsoCountryCode_Type.__name__ = "DisplayString"
_LocationIsoCountryCode_Object = MibScalar
locationIsoCountryCode = _LocationIsoCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 16),
    _LocationIsoCountryCode_Type()
)
locationIsoCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationIsoCountryCode.setStatus("current")


class _LocationPhoneCountryCode_Type(DisplayString):
    """Custom type locationPhoneCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LocationPhoneCountryCode_Type.__name__ = "DisplayString"
_LocationPhoneCountryCode_Object = MibScalar
locationPhoneCountryCode = _LocationPhoneCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 17),
    _LocationPhoneCountryCode_Type()
)
locationPhoneCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationPhoneCountryCode.setStatus("current")


class _LocationCallingAreaCode_Type(DisplayString):
    """Custom type locationCallingAreaCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LocationCallingAreaCode_Type.__name__ = "DisplayString"
_LocationCallingAreaCode_Object = MibScalar
locationCallingAreaCode = _LocationCallingAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 18),
    _LocationCallingAreaCode_Type()
)
locationCallingAreaCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationCallingAreaCode.setStatus("current")


class _LocationNetworkSsidZone_Type(DisplayString):
    """Custom type locationNetworkSsidZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LocationNetworkSsidZone_Type.__name__ = "DisplayString"
_LocationNetworkSsidZone_Object = MibScalar
locationNetworkSsidZone = _LocationNetworkSsidZone_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 19, 19),
    _LocationNetworkSsidZone_Type()
)
locationNetworkSsidZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationNetworkSsidZone.setStatus("current")
_Passthrough_ObjectIdentity = ObjectIdentity
passthrough = _Passthrough_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24)
)


class _PassthroughOn_Type(Integer32):
    """Custom type passthroughOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PassthroughOn_Type.__name__ = "Integer32"
_PassthroughOn_Object = MibScalar
passthroughOn = _PassthroughOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 1),
    _PassthroughOn_Type()
)
passthroughOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passthroughOn.setStatus("current")
_PassthroughIPTable_Object = MibTable
passthroughIPTable = _PassthroughIPTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 2)
)
if mibBuilder.loadTexts:
    passthroughIPTable.setStatus("current")
_PassthroughIPEntry_Object = MibTableRow
passthroughIPEntry = _PassthroughIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 2, 1)
)
passthroughIPEntry.setIndexNames(
    (0, "NOMADIX-MIB", "passthroughAddIndex"),
)
if mibBuilder.loadTexts:
    passthroughIPEntry.setStatus("current")
_PassthroughAddIndex_Type = Integer32
_PassthroughAddIndex_Object = MibTableColumn
passthroughAddIndex = _PassthroughAddIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 2, 1, 1),
    _PassthroughAddIndex_Type()
)
passthroughAddIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthroughAddIndex.setStatus("current")
_Passthroughaddress_Type = IpAddress
_Passthroughaddress_Object = MibTableColumn
passthroughaddress = _Passthroughaddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 2, 1, 2),
    _Passthroughaddress_Type()
)
passthroughaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passthroughaddress.setStatus("current")
_StatusIP_Type = RowStatus
_StatusIP_Object = MibTableColumn
statusIP = _StatusIP_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 2, 1, 3),
    _StatusIP_Type()
)
statusIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusIP.setStatus("current")
_PassthroughDNSTable_Object = MibTable
passthroughDNSTable = _PassthroughDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 3)
)
if mibBuilder.loadTexts:
    passthroughDNSTable.setStatus("current")
_PassthroughDNSEntry_Object = MibTableRow
passthroughDNSEntry = _PassthroughDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 3, 1)
)
passthroughDNSEntry.setIndexNames(
    (0, "NOMADIX-MIB", "passthroughNameIndex"),
)
if mibBuilder.loadTexts:
    passthroughDNSEntry.setStatus("current")
_PassthroughNameIndex_Type = Integer32
_PassthroughNameIndex_Object = MibTableColumn
passthroughNameIndex = _PassthroughNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 3, 1, 1),
    _PassthroughNameIndex_Type()
)
passthroughNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthroughNameIndex.setStatus("current")


class _Passthroughname_Type(DisplayString):
    """Custom type passthroughname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_Passthroughname_Type.__name__ = "DisplayString"
_Passthroughname_Object = MibTableColumn
passthroughname = _Passthroughname_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 3, 1, 2),
    _Passthroughname_Type()
)
passthroughname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passthroughname.setStatus("current")
_StatusDNS_Type = RowStatus
_StatusDNS_Object = MibTableColumn
statusDNS = _StatusDNS_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 24, 3, 1, 3),
    _StatusDNS_Type()
)
statusDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusDNS.setStatus("current")
_PortLoc_ObjectIdentity = ObjectIdentity
portLoc = _PortLoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28)
)


class _PortLocInRoomPortMappingOn_Type(Integer32):
    """Custom type portLocInRoomPortMappingOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PortLocInRoomPortMappingOn_Type.__name__ = "Integer32"
_PortLocInRoomPortMappingOn_Object = MibScalar
portLocInRoomPortMappingOn = _PortLocInRoomPortMappingOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 1),
    _PortLocInRoomPortMappingOn_Type()
)
portLocInRoomPortMappingOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLocInRoomPortMappingOn.setStatus("current")


class _PortLocInRoomPortMappingUsername_Type(DisplayString):
    """Custom type portLocInRoomPortMappingUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_PortLocInRoomPortMappingUsername_Type.__name__ = "DisplayString"
_PortLocInRoomPortMappingUsername_Object = MibScalar
portLocInRoomPortMappingUsername = _PortLocInRoomPortMappingUsername_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 2),
    _PortLocInRoomPortMappingUsername_Type()
)
portLocInRoomPortMappingUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLocInRoomPortMappingUsername.setStatus("current")


class _PortLocInRoomPortMappingPassword_Type(DisplayString):
    """Custom type portLocInRoomPortMappingPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_PortLocInRoomPortMappingPassword_Type.__name__ = "DisplayString"
_PortLocInRoomPortMappingPassword_Object = MibScalar
portLocInRoomPortMappingPassword = _PortLocInRoomPortMappingPassword_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 3),
    _PortLocInRoomPortMappingPassword_Type()
)
portLocInRoomPortMappingPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLocInRoomPortMappingPassword.setStatus("current")


class _PortLocConcentratorType_Type(Integer32):
    """Custom type portLocConcentratorType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("elastic", 8),
          ("expresso", 3),
          ("lucent", 4),
          ("mdulite", 5),
          ("no", 0),
          ("rfc1493", 6),
          ("riverdelta", 7),
          ("vlan1", 1),
          ("vlan2", 2))
    )


_PortLocConcentratorType_Type.__name__ = "Integer32"
_PortLocConcentratorType_Object = MibScalar
portLocConcentratorType = _PortLocConcentratorType_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 4),
    _PortLocConcentratorType_Type()
)
portLocConcentratorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLocConcentratorType.setStatus("current")
_PortLocConcentratorTable_Object = MibTable
portLocConcentratorTable = _PortLocConcentratorTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 10)
)
if mibBuilder.loadTexts:
    portLocConcentratorTable.setStatus("current")
_PortLocConcentratorTableEntry_Object = MibTableRow
portLocConcentratorTableEntry = _PortLocConcentratorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 10, 1)
)
portLocConcentratorTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "portLocConcIndex"),
)
if mibBuilder.loadTexts:
    portLocConcentratorTableEntry.setStatus("current")
_PortLocConcIndex_Type = Integer32
_PortLocConcIndex_Object = MibTableColumn
portLocConcIndex = _PortLocConcIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 10, 1, 2),
    _PortLocConcIndex_Type()
)
portLocConcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocConcIndex.setStatus("current")
_PortLocAddress_Type = IpAddress
_PortLocAddress_Object = MibTableColumn
portLocAddress = _PortLocAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 10, 1, 4),
    _PortLocAddress_Type()
)
portLocAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocAddress.setStatus("current")


class _PortLocCommunity_Type(DisplayString):
    """Custom type portLocCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 139),
    )


_PortLocCommunity_Type.__name__ = "DisplayString"
_PortLocCommunity_Object = MibTableColumn
portLocCommunity = _PortLocCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 10, 1, 6),
    _PortLocCommunity_Type()
)
portLocCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocCommunity.setStatus("current")
_PortLocUplinkPort_Type = Integer32
_PortLocUplinkPort_Object = MibTableColumn
portLocUplinkPort = _PortLocUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 10, 1, 8),
    _PortLocUplinkPort_Type()
)
portLocUplinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocUplinkPort.setStatus("current")
_PortLocTable_Object = MibTable
portLocTable = _PortLocTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 12)
)
if mibBuilder.loadTexts:
    portLocTable.setStatus("current")
_PortLocTableEntry_Object = MibTableRow
portLocTableEntry = _PortLocTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 12, 1)
)
portLocTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "portLocIndex"),
)
if mibBuilder.loadTexts:
    portLocTableEntry.setStatus("current")
_PortLocIndex_Type = Integer32
_PortLocIndex_Object = MibTableColumn
portLocIndex = _PortLocIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 12, 1, 1),
    _PortLocIndex_Type()
)
portLocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocIndex.setStatus("current")


class _PortLocLocation_Type(DisplayString):
    """Custom type portLocLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 139),
    )


_PortLocLocation_Type.__name__ = "DisplayString"
_PortLocLocation_Object = MibTableColumn
portLocLocation = _PortLocLocation_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 12, 1, 2),
    _PortLocLocation_Type()
)
portLocLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocLocation.setStatus("current")
_PortLocPort_Type = Integer32
_PortLocPort_Object = MibTableColumn
portLocPort = _PortLocPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 12, 1, 3),
    _PortLocPort_Type()
)
portLocPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocPort.setStatus("current")
_PortLocModemMAC_Type = DisplayString
_PortLocModemMAC_Object = MibTableColumn
portLocModemMAC = _PortLocModemMAC_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 12, 1, 4),
    _PortLocModemMAC_Type()
)
portLocModemMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocModemMAC.setStatus("current")


class _PortLocDescription_Type(DisplayString):
    """Custom type portLocDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 139),
    )


_PortLocDescription_Type.__name__ = "DisplayString"
_PortLocDescription_Object = MibTableColumn
portLocDescription = _PortLocDescription_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 12, 1, 5),
    _PortLocDescription_Type()
)
portLocDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocDescription.setStatus("current")


class _PortLocState_Type(Integer32):
    """Custom type portLocState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("charge", 1),
          ("noCharge", 0))
    )


_PortLocState_Type.__name__ = "Integer32"
_PortLocState_Object = MibTableColumn
portLocState = _PortLocState_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 28, 12, 1, 6),
    _PortLocState_Type()
)
portLocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocState.setStatus("current")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 30)
)


class _SmtpRedirect_Type(Integer32):
    """Custom type smtpRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SmtpRedirect_Type.__name__ = "Integer32"
_SmtpRedirect_Object = MibScalar
smtpRedirect = _SmtpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 30, 1),
    _SmtpRedirect_Type()
)
smtpRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpRedirect.setStatus("current")
_SmtpServerIP_Type = IpAddress
_SmtpServerIP_Object = MibScalar
smtpServerIP = _SmtpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 30, 2),
    _SmtpServerIP_Type()
)
smtpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerIP.setStatus("current")


class _SmtpPcRedirect_Type(Integer32):
    """Custom type smtpPcRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SmtpPcRedirect_Type.__name__ = "Integer32"
_SmtpPcRedirect_Object = MibScalar
smtpPcRedirect = _SmtpPcRedirect_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 30, 3),
    _SmtpPcRedirect_Type()
)
smtpPcRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPcRedirect.setStatus("current")


class _SmtpUsername_Type(DisplayString):
    """Custom type smtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_SmtpUsername_Type.__name__ = "DisplayString"
_SmtpUsername_Object = MibScalar
smtpUsername = _SmtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 30, 4),
    _SmtpUsername_Type()
)
smtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpUsername.setStatus("current")


class _SmtpPassword_Type(DisplayString):
    """Custom type smtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_SmtpPassword_Type.__name__ = "DisplayString"
_SmtpPassword_Object = MibScalar
smtpPassword = _SmtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 30, 5),
    _SmtpPassword_Type()
)
smtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPassword.setStatus("current")


class _SmtpServerDNS_Type(DisplayString):
    """Custom type smtpServerDNS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 238),
    )


_SmtpServerDNS_Type.__name__ = "DisplayString"
_SmtpServerDNS_Object = MibScalar
smtpServerDNS = _SmtpServerDNS_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 30, 6),
    _SmtpServerDNS_Type()
)
smtpServerDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerDNS.setStatus("current")
_Snmpagent_ObjectIdentity = ObjectIdentity
snmpagent = _Snmpagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 32)
)


class _SnmpdOn_Type(Integer32):
    """Custom type snmpdOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpdOn_Type.__name__ = "Integer32"
_SnmpdOn_Object = MibScalar
snmpdOn = _SnmpdOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 32, 1),
    _SnmpdOn_Type()
)
snmpdOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdOn.setStatus("current")


class _SystemContact_Type(DisplayString):
    """Custom type systemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_SystemContact_Type.__name__ = "DisplayString"
_SystemContact_Object = MibScalar
systemContact = _SystemContact_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 32, 2),
    _SystemContact_Type()
)
systemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemContact.setStatus("current")


class _SystemLocation_Type(DisplayString):
    """Custom type systemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_SystemLocation_Type.__name__ = "DisplayString"
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 32, 3),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocation.setStatus("current")


class _GetCommunity_Type(DisplayString):
    """Custom type getCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_GetCommunity_Type.__name__ = "DisplayString"
_GetCommunity_Object = MibScalar
getCommunity = _GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 32, 4),
    _GetCommunity_Type()
)
getCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getCommunity.setStatus("current")


class _SetCommunity_Type(DisplayString):
    """Custom type setCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_SetCommunity_Type.__name__ = "DisplayString"
_SetCommunity_Object = MibScalar
setCommunity = _SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 32, 5),
    _SetCommunity_Type()
)
setCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCommunity.setStatus("current")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 238),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibScalar
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 32, 6),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("current")
_TrapIP_Type = IpAddress
_TrapIP_Object = MibScalar
trapIP = _TrapIP_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 32, 7),
    _TrapIP_Type()
)
trapIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP.setStatus("current")
_Subsettings_ObjectIdentity = ObjectIdentity
subsettings = _Subsettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 33)
)


class _SubIdleLogoutTimeout_Type(Integer32):
    """Custom type subIdleLogoutTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_SubIdleLogoutTimeout_Type.__name__ = "Integer32"
_SubIdleLogoutTimeout_Object = MibScalar
subIdleLogoutTimeout = _SubIdleLogoutTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 33, 1),
    _SubIdleLogoutTimeout_Type()
)
subIdleLogoutTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subIdleLogoutTimeout.setStatus("current")


class _SubToSubCommBlock_Type(Integer32):
    """Custom type subToSubCommBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SubToSubCommBlock_Type.__name__ = "Integer32"
_SubToSubCommBlock_Object = MibScalar
subToSubCommBlock = _SubToSubCommBlock_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 33, 2),
    _SubToSubCommBlock_Type()
)
subToSubCommBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subToSubCommBlock.setStatus("current")
_Subnets_ObjectIdentity = ObjectIdentity
subnets = _Subnets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 34)
)
_SubnetTable_Object = MibTable
subnetTable = _SubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 34, 1)
)
if mibBuilder.loadTexts:
    subnetTable.setStatus("current")
_SubnetTableEntry_Object = MibTableRow
subnetTableEntry = _SubnetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 34, 1, 1)
)
subnetTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "subnetIndex"),
)
if mibBuilder.loadTexts:
    subnetTableEntry.setStatus("current")
_SubnetIndex_Type = Integer32
_SubnetIndex_Object = MibTableColumn
subnetIndex = _SubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 34, 1, 1, 1),
    _SubnetIndex_Type()
)
subnetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetIndex.setStatus("current")
_Subnet_Type = IpAddress
_Subnet_Object = MibTableColumn
subnet = _Subnet_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 34, 1, 1, 2),
    _Subnet_Type()
)
subnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnet.setStatus("current")
_Mask_Type = IpAddress
_Mask_Object = MibTableColumn
mask = _Mask_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 34, 1, 1, 3),
    _Mask_Type()
)
mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mask.setStatus("current")
_SubnetStatus_Type = RowStatus
_SubnetStatus_Object = MibTableColumn
subnetStatus = _SubnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 34, 1, 1, 4),
    _SubnetStatus_Type()
)
subnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetStatus.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35)
)


class _SystemLoggingOn_Type(Integer32):
    """Custom type systemLoggingOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemLoggingOn_Type.__name__ = "Integer32"
_SystemLoggingOn_Object = MibScalar
systemLoggingOn = _SystemLoggingOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 1),
    _SystemLoggingOn_Type()
)
systemLoggingOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingOn.setStatus("current")


class _SystemLogNumber_Type(Integer32):
    """Custom type systemLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SystemLogNumber_Type.__name__ = "Integer32"
_SystemLogNumber_Object = MibScalar
systemLogNumber = _SystemLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 2),
    _SystemLogNumber_Type()
)
systemLogNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogNumber.setStatus("current")


class _SystemLogFilter_Type(Integer32):
    """Custom type systemLogFilter based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_SystemLogFilter_Type.__name__ = "Integer32"
_SystemLogFilter_Object = MibScalar
systemLogFilter = _SystemLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 3),
    _SystemLogFilter_Type()
)
systemLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogFilter.setStatus("current")
_SystemLogServerIp_Type = IpAddress
_SystemLogServerIp_Object = MibScalar
systemLogServerIp = _SystemLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 4),
    _SystemLogServerIp_Type()
)
systemLogServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogServerIp.setStatus("current")


class _SystemSaveToFile_Type(Integer32):
    """Custom type systemSaveToFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemSaveToFile_Type.__name__ = "Integer32"
_SystemSaveToFile_Object = MibScalar
systemSaveToFile = _SystemSaveToFile_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 5),
    _SystemSaveToFile_Type()
)
systemSaveToFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSaveToFile.setStatus("current")


class _SystemReportLoggingOn_Type(Integer32):
    """Custom type systemReportLoggingOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemReportLoggingOn_Type.__name__ = "Integer32"
_SystemReportLoggingOn_Object = MibScalar
systemReportLoggingOn = _SystemReportLoggingOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 6),
    _SystemReportLoggingOn_Type()
)
systemReportLoggingOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReportLoggingOn.setStatus("current")


class _SystemReportLogNumber_Type(Integer32):
    """Custom type systemReportLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SystemReportLogNumber_Type.__name__ = "Integer32"
_SystemReportLogNumber_Object = MibScalar
systemReportLogNumber = _SystemReportLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 7),
    _SystemReportLogNumber_Type()
)
systemReportLogNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReportLogNumber.setStatus("current")
_SystemReportLogServerIp_Type = IpAddress
_SystemReportLogServerIp_Object = MibScalar
systemReportLogServerIp = _SystemReportLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 8),
    _SystemReportLogServerIp_Type()
)
systemReportLogServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReportLogServerIp.setStatus("current")


class _SystemReportLogInterval_Type(Integer32):
    """Custom type systemReportLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_SystemReportLogInterval_Type.__name__ = "Integer32"
_SystemReportLogInterval_Object = MibScalar
systemReportLogInterval = _SystemReportLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 9),
    _SystemReportLogInterval_Type()
)
systemReportLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReportLogInterval.setStatus("current")


class _SystemVersion_Type(DisplayString):
    """Custom type systemVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SystemVersion_Type.__name__ = "DisplayString"
_SystemVersion_Object = MibScalar
systemVersion = _SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 10),
    _SystemVersion_Type()
)
systemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVersion.setStatus("current")


class _SystemNseId_Type(DisplayString):
    """Custom type systemNseId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SystemNseId_Type.__name__ = "DisplayString"
_SystemNseId_Object = MibScalar
systemNseId = _SystemNseId_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 11),
    _SystemNseId_Type()
)
systemNseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNseId.setStatus("current")


class _SystemReboot_Type(Integer32):
    """Custom type systemReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_SystemReboot_Type.__name__ = "Integer32"
_SystemReboot_Object = MibScalar
systemReboot = _SystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 12),
    _SystemReboot_Type()
)
systemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReboot.setStatus("current")


class _SystemBridgeMode_Type(Integer32):
    """Custom type systemBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemBridgeMode_Type.__name__ = "Integer32"
_SystemBridgeMode_Object = MibScalar
systemBridgeMode = _SystemBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 13),
    _SystemBridgeMode_Type()
)
systemBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemBridgeMode.setStatus("current")


class _SystemConfigFile_Type(Integer32):
    """Custom type systemConfigFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("export", 2),
          ("factory", 1),
          ("import", 3))
    )


_SystemConfigFile_Type.__name__ = "Integer32"
_SystemConfigFile_Object = MibScalar
systemConfigFile = _SystemConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 14),
    _SystemConfigFile_Type()
)
systemConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigFile.setStatus("current")


class _SystemConfigFileStatus_Type(Integer32):
    """Custom type systemConfigFileStatus based on Integer32"""
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
        *(("errorCurrentMaybeCorrupted", 2),
          ("errorCurrentNotArchived", 3),
          ("errorCurrentNotChanged", 1),
          ("noError", 0))
    )


_SystemConfigFileStatus_Type.__name__ = "Integer32"
_SystemConfigFileStatus_Object = MibScalar
systemConfigFileStatus = _SystemConfigFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 15),
    _SystemConfigFileStatus_Type()
)
systemConfigFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigFileStatus.setStatus("current")


class _SystemAdminConcurrencyOn_Type(Integer32):
    """Custom type systemAdminConcurrencyOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemAdminConcurrencyOn_Type.__name__ = "Integer32"
_SystemAdminConcurrencyOn_Object = MibScalar
systemAdminConcurrencyOn = _SystemAdminConcurrencyOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 16),
    _SystemAdminConcurrencyOn_Type()
)
systemAdminConcurrencyOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAdminConcurrencyOn.setStatus("current")


class _SystemUptime_Type(DisplayString):
    """Custom type systemUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SystemUptime_Type.__name__ = "DisplayString"
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 17),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_SystemHistoryTable_Object = MibTable
systemHistoryTable = _SystemHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 18)
)
if mibBuilder.loadTexts:
    systemHistoryTable.setStatus("current")
_SystemHistoryTableEntry_Object = MibTableRow
systemHistoryTableEntry = _SystemHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 18, 1)
)
systemHistoryTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "systemHistoryIndex"),
)
if mibBuilder.loadTexts:
    systemHistoryTableEntry.setStatus("current")
_SystemHistoryIndex_Type = Integer32
_SystemHistoryIndex_Object = MibTableColumn
systemHistoryIndex = _SystemHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 18, 1, 1),
    _SystemHistoryIndex_Type()
)
systemHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHistoryIndex.setStatus("current")


class _SystemHistoryTimestamp_Type(DisplayString):
    """Custom type systemHistoryTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_SystemHistoryTimestamp_Type.__name__ = "DisplayString"
_SystemHistoryTimestamp_Object = MibTableColumn
systemHistoryTimestamp = _SystemHistoryTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 18, 1, 2),
    _SystemHistoryTimestamp_Type()
)
systemHistoryTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHistoryTimestamp.setStatus("current")


class _SystemHistoryLogin_Type(DisplayString):
    """Custom type systemHistoryLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_SystemHistoryLogin_Type.__name__ = "DisplayString"
_SystemHistoryLogin_Object = MibTableColumn
systemHistoryLogin = _SystemHistoryLogin_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 18, 1, 3),
    _SystemHistoryLogin_Type()
)
systemHistoryLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHistoryLogin.setStatus("current")
_SystemHistoryAddress_Type = IpAddress
_SystemHistoryAddress_Object = MibTableColumn
systemHistoryAddress = _SystemHistoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 18, 1, 4),
    _SystemHistoryAddress_Type()
)
systemHistoryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHistoryAddress.setStatus("current")


class _SystemHistoryMessage_Type(DisplayString):
    """Custom type systemHistoryMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 429),
    )


_SystemHistoryMessage_Type.__name__ = "DisplayString"
_SystemHistoryMessage_Object = MibTableColumn
systemHistoryMessage = _SystemHistoryMessage_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 18, 1, 5),
    _SystemHistoryMessage_Type()
)
systemHistoryMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHistoryMessage.setStatus("current")
_SystemSyslogTable_Object = MibTable
systemSyslogTable = _SystemSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 19)
)
if mibBuilder.loadTexts:
    systemSyslogTable.setStatus("current")
_SystemSyslogTableEntry_Object = MibTableRow
systemSyslogTableEntry = _SystemSyslogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 19, 1)
)
systemSyslogTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "systemSyslogIndex"),
)
if mibBuilder.loadTexts:
    systemSyslogTableEntry.setStatus("current")
_SystemSyslogIndex_Type = Integer32
_SystemSyslogIndex_Object = MibTableColumn
systemSyslogIndex = _SystemSyslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 19, 1, 1),
    _SystemSyslogIndex_Type()
)
systemSyslogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSyslogIndex.setStatus("current")


class _SystemSyslogTimestamp_Type(DisplayString):
    """Custom type systemSyslogTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_SystemSyslogTimestamp_Type.__name__ = "DisplayString"
_SystemSyslogTimestamp_Object = MibTableColumn
systemSyslogTimestamp = _SystemSyslogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 19, 1, 2),
    _SystemSyslogTimestamp_Type()
)
systemSyslogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSyslogTimestamp.setStatus("current")


class _SystemSyslogVersion_Type(DisplayString):
    """Custom type systemSyslogVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_SystemSyslogVersion_Type.__name__ = "DisplayString"
_SystemSyslogVersion_Object = MibTableColumn
systemSyslogVersion = _SystemSyslogVersion_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 19, 1, 3),
    _SystemSyslogVersion_Type()
)
systemSyslogVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSyslogVersion.setStatus("current")
_SystemSyslogAddress_Type = IpAddress
_SystemSyslogAddress_Object = MibTableColumn
systemSyslogAddress = _SystemSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 19, 1, 4),
    _SystemSyslogAddress_Type()
)
systemSyslogAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSyslogAddress.setStatus("current")


class _SystemSyslogMessage_Type(DisplayString):
    """Custom type systemSyslogMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 429),
    )


_SystemSyslogMessage_Type.__name__ = "DisplayString"
_SystemSyslogMessage_Object = MibTableColumn
systemSyslogMessage = _SystemSyslogMessage_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 19, 1, 5),
    _SystemSyslogMessage_Type()
)
systemSyslogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSyslogMessage.setStatus("current")
_SystemStaticPortMappingTable_Object = MibTable
systemStaticPortMappingTable = _SystemStaticPortMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20)
)
if mibBuilder.loadTexts:
    systemStaticPortMappingTable.setStatus("current")
_SystemStaticPortMappingTableEntry_Object = MibTableRow
systemStaticPortMappingTableEntry = _SystemStaticPortMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1)
)
systemStaticPortMappingTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "systemStaticPortMappingIndex"),
)
if mibBuilder.loadTexts:
    systemStaticPortMappingTableEntry.setStatus("current")
_SystemStaticPortMappingIndex_Type = Integer32
_SystemStaticPortMappingIndex_Object = MibTableColumn
systemStaticPortMappingIndex = _SystemStaticPortMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1, 1),
    _SystemStaticPortMappingIndex_Type()
)
systemStaticPortMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStaticPortMappingIndex.setStatus("current")


class _SystemStaticPortMappingMAC_Type(DisplayString):
    """Custom type systemStaticPortMappingMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SystemStaticPortMappingMAC_Type.__name__ = "DisplayString"
_SystemStaticPortMappingMAC_Object = MibTableColumn
systemStaticPortMappingMAC = _SystemStaticPortMappingMAC_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1, 2),
    _SystemStaticPortMappingMAC_Type()
)
systemStaticPortMappingMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStaticPortMappingMAC.setStatus("current")
_SystemStaticPortMappingInternalIP_Type = IpAddress
_SystemStaticPortMappingInternalIP_Object = MibTableColumn
systemStaticPortMappingInternalIP = _SystemStaticPortMappingInternalIP_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1, 3),
    _SystemStaticPortMappingInternalIP_Type()
)
systemStaticPortMappingInternalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStaticPortMappingInternalIP.setStatus("current")


class _SystemStaticPortMappingInternalPort_Type(Integer32):
    """Custom type systemStaticPortMappingInternalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SystemStaticPortMappingInternalPort_Type.__name__ = "Integer32"
_SystemStaticPortMappingInternalPort_Object = MibTableColumn
systemStaticPortMappingInternalPort = _SystemStaticPortMappingInternalPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1, 4),
    _SystemStaticPortMappingInternalPort_Type()
)
systemStaticPortMappingInternalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStaticPortMappingInternalPort.setStatus("current")
_SystemStaticPortMappingExternalIP_Type = IpAddress
_SystemStaticPortMappingExternalIP_Object = MibTableColumn
systemStaticPortMappingExternalIP = _SystemStaticPortMappingExternalIP_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1, 5),
    _SystemStaticPortMappingExternalIP_Type()
)
systemStaticPortMappingExternalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStaticPortMappingExternalIP.setStatus("current")


class _SystemStaticPortMappingExternalPort_Type(Integer32):
    """Custom type systemStaticPortMappingExternalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_SystemStaticPortMappingExternalPort_Type.__name__ = "Integer32"
_SystemStaticPortMappingExternalPort_Object = MibTableColumn
systemStaticPortMappingExternalPort = _SystemStaticPortMappingExternalPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1, 6),
    _SystemStaticPortMappingExternalPort_Type()
)
systemStaticPortMappingExternalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStaticPortMappingExternalPort.setStatus("current")
_SystemStaticPortMappingRemoteIP_Type = IpAddress
_SystemStaticPortMappingRemoteIP_Object = MibTableColumn
systemStaticPortMappingRemoteIP = _SystemStaticPortMappingRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1, 7),
    _SystemStaticPortMappingRemoteIP_Type()
)
systemStaticPortMappingRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStaticPortMappingRemoteIP.setStatus("current")


class _SystemStaticPortMappingRemotePort_Type(Integer32):
    """Custom type systemStaticPortMappingRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemStaticPortMappingRemotePort_Type.__name__ = "Integer32"
_SystemStaticPortMappingRemotePort_Object = MibTableColumn
systemStaticPortMappingRemotePort = _SystemStaticPortMappingRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1, 8),
    _SystemStaticPortMappingRemotePort_Type()
)
systemStaticPortMappingRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStaticPortMappingRemotePort.setStatus("current")


class _SystemStaticPortMappingProto_Type(Integer32):
    """Custom type systemStaticPortMappingProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 0))
    )


_SystemStaticPortMappingProto_Type.__name__ = "Integer32"
_SystemStaticPortMappingProto_Object = MibTableColumn
systemStaticPortMappingProto = _SystemStaticPortMappingProto_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1, 9),
    _SystemStaticPortMappingProto_Type()
)
systemStaticPortMappingProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStaticPortMappingProto.setStatus("current")
_SystemStaticPortMappingStatus_Type = RowStatus
_SystemStaticPortMappingStatus_Object = MibTableColumn
systemStaticPortMappingStatus = _SystemStaticPortMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 20, 1, 10),
    _SystemStaticPortMappingStatus_Type()
)
systemStaticPortMappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStaticPortMappingStatus.setStatus("current")


class _BlockIcmpFromPending_Type(Integer32):
    """Custom type blockIcmpFromPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BlockIcmpFromPending_Type.__name__ = "Integer32"
_BlockIcmpFromPending_Object = MibScalar
blockIcmpFromPending = _BlockIcmpFromPending_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 35, 21),
    _BlockIcmpFromPending_Type()
)
blockIcmpFromPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockIcmpFromPending.setStatus("current")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 36)
)


class _TimeCurrentDateAndTime_Type(DisplayString):
    """Custom type timeCurrentDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_TimeCurrentDateAndTime_Type.__name__ = "DisplayString"
_TimeCurrentDateAndTime_Object = MibScalar
timeCurrentDateAndTime = _TimeCurrentDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 36, 1),
    _TimeCurrentDateAndTime_Type()
)
timeCurrentDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeCurrentDateAndTime.setStatus("current")


class _TimeOffsetSign_Type(Integer32):
    """Custom type timeOffsetSign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("minus", 1),
          ("plus", 0))
    )


_TimeOffsetSign_Type.__name__ = "Integer32"
_TimeOffsetSign_Object = MibScalar
timeOffsetSign = _TimeOffsetSign_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 36, 2),
    _TimeOffsetSign_Type()
)
timeOffsetSign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeOffsetSign.setStatus("current")


class _TimeOffsetHours_Type(Integer32):
    """Custom type timeOffsetHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TimeOffsetHours_Type.__name__ = "Integer32"
_TimeOffsetHours_Object = MibScalar
timeOffsetHours = _TimeOffsetHours_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 36, 3),
    _TimeOffsetHours_Type()
)
timeOffsetHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeOffsetHours.setStatus("current")


class _TimeOffsetMinutes_Type(Integer32):
    """Custom type timeOffsetMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TimeOffsetMinutes_Type.__name__ = "Integer32"
_TimeOffsetMinutes_Object = MibScalar
timeOffsetMinutes = _TimeOffsetMinutes_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 36, 4),
    _TimeOffsetMinutes_Type()
)
timeOffsetMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeOffsetMinutes.setStatus("current")


class _TimeServerTimeout_Type(Integer32):
    """Custom type timeServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TimeServerTimeout_Type.__name__ = "Integer32"
_TimeServerTimeout_Object = MibScalar
timeServerTimeout = _TimeServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 36, 5),
    _TimeServerTimeout_Type()
)
timeServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServerTimeout.setStatus("current")


class _TimeServer1_Type(DisplayString):
    """Custom type timeServer1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 238),
    )


_TimeServer1_Type.__name__ = "DisplayString"
_TimeServer1_Object = MibScalar
timeServer1 = _TimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 36, 6),
    _TimeServer1_Type()
)
timeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer1.setStatus("current")


class _TimeServer2_Type(DisplayString):
    """Custom type timeServer2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 238),
    )


_TimeServer2_Type.__name__ = "DisplayString"
_TimeServer2_Object = MibScalar
timeServer2 = _TimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 36, 7),
    _TimeServer2_Type()
)
timeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer2.setStatus("current")


class _TimeServer3_Type(DisplayString):
    """Custom type timeServer3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 238),
    )


_TimeServer3_Type.__name__ = "DisplayString"
_TimeServer3_Object = MibScalar
timeServer3 = _TimeServer3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 36, 8),
    _TimeServer3_Type()
)
timeServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer3.setStatus("current")


class _TimeServer4_Type(DisplayString):
    """Custom type timeServer4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 238),
    )


_TimeServer4_Type.__name__ = "DisplayString"
_TimeServer4_Object = MibScalar
timeServer4 = _TimeServer4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 36, 9),
    _TimeServer4_Type()
)
timeServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer4.setStatus("current")
_UrlFiltering_ObjectIdentity = ObjectIdentity
urlFiltering = _UrlFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37)
)


class _UrlFilteringOn_Type(Integer32):
    """Custom type urlFilteringOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UrlFilteringOn_Type.__name__ = "Integer32"
_UrlFilteringOn_Object = MibScalar
urlFilteringOn = _UrlFilteringOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 1),
    _UrlFilteringOn_Type()
)
urlFilteringOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    urlFilteringOn.setStatus("current")
_UrlFilteringIPTable_Object = MibTable
urlFilteringIPTable = _UrlFilteringIPTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 2)
)
if mibBuilder.loadTexts:
    urlFilteringIPTable.setStatus("current")
_UrlFilteringIPTableEntry_Object = MibTableRow
urlFilteringIPTableEntry = _UrlFilteringIPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 2, 1)
)
urlFilteringIPTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "urlFilteringIPTableIndex"),
)
if mibBuilder.loadTexts:
    urlFilteringIPTableEntry.setStatus("current")
_UrlFilteringIPTableIndex_Type = Integer32
_UrlFilteringIPTableIndex_Object = MibTableColumn
urlFilteringIPTableIndex = _UrlFilteringIPTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 2, 1, 1),
    _UrlFilteringIPTableIndex_Type()
)
urlFilteringIPTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlFilteringIPTableIndex.setStatus("current")
_UrlFilteringIPTableAddress_Type = IpAddress
_UrlFilteringIPTableAddress_Object = MibTableColumn
urlFilteringIPTableAddress = _UrlFilteringIPTableAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 2, 1, 2),
    _UrlFilteringIPTableAddress_Type()
)
urlFilteringIPTableAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    urlFilteringIPTableAddress.setStatus("current")
_UrlFilteringIPTableStatus_Type = RowStatus
_UrlFilteringIPTableStatus_Object = MibTableColumn
urlFilteringIPTableStatus = _UrlFilteringIPTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 2, 1, 3),
    _UrlFilteringIPTableStatus_Type()
)
urlFilteringIPTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    urlFilteringIPTableStatus.setStatus("current")
_UrlFilteringDNSTable_Object = MibTable
urlFilteringDNSTable = _UrlFilteringDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 3)
)
if mibBuilder.loadTexts:
    urlFilteringDNSTable.setStatus("current")
_UrlFilteringDNSTableEntry_Object = MibTableRow
urlFilteringDNSTableEntry = _UrlFilteringDNSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 3, 1)
)
urlFilteringDNSTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "urlFilteringDNSTableIndex"),
)
if mibBuilder.loadTexts:
    urlFilteringDNSTableEntry.setStatus("current")
_UrlFilteringDNSTableIndex_Type = Integer32
_UrlFilteringDNSTableIndex_Object = MibTableColumn
urlFilteringDNSTableIndex = _UrlFilteringDNSTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 3, 1, 1),
    _UrlFilteringDNSTableIndex_Type()
)
urlFilteringDNSTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlFilteringDNSTableIndex.setStatus("current")


class _UrlFilteringDNSTableName_Type(DisplayString):
    """Custom type urlFilteringDNSTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_UrlFilteringDNSTableName_Type.__name__ = "DisplayString"
_UrlFilteringDNSTableName_Object = MibTableColumn
urlFilteringDNSTableName = _UrlFilteringDNSTableName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 3, 1, 2),
    _UrlFilteringDNSTableName_Type()
)
urlFilteringDNSTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    urlFilteringDNSTableName.setStatus("current")
_UrlFilteringDNSTableStatus_Type = RowStatus
_UrlFilteringDNSTableStatus_Object = MibTableColumn
urlFilteringDNSTableStatus = _UrlFilteringDNSTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 37, 3, 1, 3),
    _UrlFilteringDNSTableStatus_Type()
)
urlFilteringDNSTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    urlFilteringDNSTableStatus.setStatus("current")
_RadiusProxy_ObjectIdentity = ObjectIdentity
radiusProxy = _RadiusProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38)
)


class _RadProxyServices_Type(Integer32):
    """Custom type radProxyServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RadProxyServices_Type.__name__ = "Integer32"
_RadProxyServices_Object = MibScalar
radProxyServices = _RadProxyServices_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 1),
    _RadProxyServices_Type()
)
radProxyServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radProxyServices.setStatus("current")
_RadProxyAuthSvrPort_Type = Integer32
_RadProxyAuthSvrPort_Object = MibScalar
radProxyAuthSvrPort = _RadProxyAuthSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 2),
    _RadProxyAuthSvrPort_Type()
)
radProxyAuthSvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radProxyAuthSvrPort.setStatus("current")
_RadProxyAcctSvrPort_Type = Integer32
_RadProxyAcctSvrPort_Object = MibScalar
radProxyAcctSvrPort = _RadProxyAcctSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 3),
    _RadProxyAcctSvrPort_Type()
)
radProxyAcctSvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radProxyAcctSvrPort.setStatus("current")
_RadProxyUpstreamNas_ObjectIdentity = ObjectIdentity
radProxyUpstreamNas = _RadProxyUpstreamNas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 4)
)
_RadProxyUpstreamNasTable_Object = MibTable
radProxyUpstreamNasTable = _RadProxyUpstreamNasTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 4, 1)
)
if mibBuilder.loadTexts:
    radProxyUpstreamNasTable.setStatus("current")
_RadProxyUpstreamNasTableEntry_Object = MibTableRow
radProxyUpstreamNasTableEntry = _RadProxyUpstreamNasTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 4, 1, 1)
)
radProxyUpstreamNasTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "nasIndex"),
)
if mibBuilder.loadTexts:
    radProxyUpstreamNasTableEntry.setStatus("current")
_NasIndex_Type = Integer32
_NasIndex_Object = MibTableColumn
nasIndex = _NasIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 4, 1, 1, 1),
    _NasIndex_Type()
)
nasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasIndex.setStatus("current")


class _NasEntryActive_Type(Integer32):
    """Custom type nasEntryActive based on Integer32"""
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


_NasEntryActive_Type.__name__ = "Integer32"
_NasEntryActive_Object = MibTableColumn
nasEntryActive = _NasEntryActive_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 4, 1, 1, 2),
    _NasEntryActive_Type()
)
nasEntryActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nasEntryActive.setStatus("current")
_NasIpAddress_Type = IpAddress
_NasIpAddress_Object = MibTableColumn
nasIpAddress = _NasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 4, 1, 1, 3),
    _NasIpAddress_Type()
)
nasIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nasIpAddress.setStatus("current")


class _NasAuthSec_Type(DisplayString):
    """Custom type nasAuthSec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_NasAuthSec_Type.__name__ = "DisplayString"
_NasAuthSec_Object = MibTableColumn
nasAuthSec = _NasAuthSec_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 4, 1, 1, 4),
    _NasAuthSec_Type()
)
nasAuthSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nasAuthSec.setStatus("current")


class _NasAcctSec_Type(DisplayString):
    """Custom type nasAcctSec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_NasAcctSec_Type.__name__ = "DisplayString"
_NasAcctSec_Object = MibTableColumn
nasAcctSec = _NasAcctSec_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 4, 1, 1, 5),
    _NasAcctSec_Type()
)
nasAcctSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nasAcctSec.setStatus("current")


class _NasDefProf_Type(DisplayString):
    """Custom type nasDefProf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NasDefProf_Type.__name__ = "DisplayString"
_NasDefProf_Object = MibTableColumn
nasDefProf = _NasDefProf_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 4, 1, 1, 6),
    _NasDefProf_Type()
)
nasDefProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nasDefProf.setStatus("current")
_NasStatus_Type = RowStatus
_NasStatus_Object = MibTableColumn
nasStatus = _NasStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 4, 1, 1, 7),
    _NasStatus_Type()
)
nasStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nasStatus.setStatus("current")
_RadProxyLocalServcomPort_Type = Integer32
_RadProxyLocalServcomPort_Object = MibScalar
radProxyLocalServcomPort = _RadProxyLocalServcomPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 38, 5),
    _RadProxyLocalServcomPort_Type()
)
radProxyLocalServcomPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radProxyLocalServcomPort.setStatus("current")
_RealmBasedRouter_ObjectIdentity = ObjectIdentity
realmBasedRouter = _RealmBasedRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39)
)
_RBserviceProfiles_ObjectIdentity = ObjectIdentity
rBserviceProfiles = _RBserviceProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1)
)
_ServiceProfileTable_Object = MibTable
serviceProfileTable = _ServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1)
)
if mibBuilder.loadTexts:
    serviceProfileTable.setStatus("current")
_ServiceProfileTableEntry_Object = MibTableRow
serviceProfileTableEntry = _ServiceProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1)
)
serviceProfileTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "profIndex"),
)
if mibBuilder.loadTexts:
    serviceProfileTableEntry.setStatus("current")
_ProfIndex_Type = Integer32
_ProfIndex_Object = MibTableColumn
profIndex = _ProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 1),
    _ProfIndex_Type()
)
profIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profIndex.setStatus("current")


class _ProfName_Type(DisplayString):
    """Custom type profName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ProfName_Type.__name__ = "DisplayString"
_ProfName_Object = MibTableColumn
profName = _ProfName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 2),
    _ProfName_Type()
)
profName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profName.setStatus("current")


class _RadAuthOn_Type(Integer32):
    """Custom type radAuthOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RadAuthOn_Type.__name__ = "Integer32"
_RadAuthOn_Object = MibTableColumn
radAuthOn = _RadAuthOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 3),
    _RadAuthOn_Type()
)
radAuthOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAuthOn.setStatus("current")


class _RadAuthProto_Type(Integer32):
    """Custom type radAuthProto based on Integer32"""
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
        *(("rad-auth-proto-chap", 1),
          ("rad-auth-proto-mschap-v1", 2),
          ("rad-auth-proto-mschap-v2", 3),
          ("rad-auth-proto-pap", 0))
    )


_RadAuthProto_Type.__name__ = "Integer32"
_RadAuthProto_Object = MibTableColumn
radAuthProto = _RadAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 4),
    _RadAuthProto_Type()
)
radAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAuthProto.setStatus("current")
_RadAuthSrv1Ip_Type = IpAddress
_RadAuthSrv1Ip_Object = MibTableColumn
radAuthSrv1Ip = _RadAuthSrv1Ip_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 5),
    _RadAuthSrv1Ip_Type()
)
radAuthSrv1Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAuthSrv1Ip.setStatus("current")
_RadAuthSrv1Port_Type = Integer32
_RadAuthSrv1Port_Object = MibTableColumn
radAuthSrv1Port = _RadAuthSrv1Port_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 6),
    _RadAuthSrv1Port_Type()
)
radAuthSrv1Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAuthSrv1Port.setStatus("current")


class _RadAuthSrv1Sec_Type(DisplayString):
    """Custom type radAuthSrv1Sec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_RadAuthSrv1Sec_Type.__name__ = "DisplayString"
_RadAuthSrv1Sec_Object = MibTableColumn
radAuthSrv1Sec = _RadAuthSrv1Sec_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 7),
    _RadAuthSrv1Sec_Type()
)
radAuthSrv1Sec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAuthSrv1Sec.setStatus("current")
_RadAuthSrv2Ip_Type = IpAddress
_RadAuthSrv2Ip_Object = MibTableColumn
radAuthSrv2Ip = _RadAuthSrv2Ip_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 8),
    _RadAuthSrv2Ip_Type()
)
radAuthSrv2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAuthSrv2Ip.setStatus("current")
_RadAuthSrv2Port_Type = Integer32
_RadAuthSrv2Port_Object = MibTableColumn
radAuthSrv2Port = _RadAuthSrv2Port_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 9),
    _RadAuthSrv2Port_Type()
)
radAuthSrv2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAuthSrv2Port.setStatus("current")


class _RadAuthSrv2Sec_Type(DisplayString):
    """Custom type radAuthSrv2Sec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_RadAuthSrv2Sec_Type.__name__ = "DisplayString"
_RadAuthSrv2Sec_Object = MibTableColumn
radAuthSrv2Sec = _RadAuthSrv2Sec_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 10),
    _RadAuthSrv2Sec_Type()
)
radAuthSrv2Sec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAuthSrv2Sec.setStatus("current")


class _RadAcctOn_Type(Integer32):
    """Custom type radAcctOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RadAcctOn_Type.__name__ = "Integer32"
_RadAcctOn_Object = MibTableColumn
radAcctOn = _RadAcctOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 11),
    _RadAcctOn_Type()
)
radAcctOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctOn.setStatus("current")
_RadAcctSrv1Ip_Type = IpAddress
_RadAcctSrv1Ip_Object = MibTableColumn
radAcctSrv1Ip = _RadAcctSrv1Ip_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 12),
    _RadAcctSrv1Ip_Type()
)
radAcctSrv1Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctSrv1Ip.setStatus("current")
_RadAcctSrv1Port_Type = Integer32
_RadAcctSrv1Port_Object = MibTableColumn
radAcctSrv1Port = _RadAcctSrv1Port_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 13),
    _RadAcctSrv1Port_Type()
)
radAcctSrv1Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctSrv1Port.setStatus("current")


class _RadAcctSrv1Sec_Type(DisplayString):
    """Custom type radAcctSrv1Sec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_RadAcctSrv1Sec_Type.__name__ = "DisplayString"
_RadAcctSrv1Sec_Object = MibTableColumn
radAcctSrv1Sec = _RadAcctSrv1Sec_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 14),
    _RadAcctSrv1Sec_Type()
)
radAcctSrv1Sec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctSrv1Sec.setStatus("current")
_RadAcctSrv2Ip_Type = IpAddress
_RadAcctSrv2Ip_Object = MibTableColumn
radAcctSrv2Ip = _RadAcctSrv2Ip_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 15),
    _RadAcctSrv2Ip_Type()
)
radAcctSrv2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctSrv2Ip.setStatus("current")
_RadAcctSrv2Port_Type = Integer32
_RadAcctSrv2Port_Object = MibTableColumn
radAcctSrv2Port = _RadAcctSrv2Port_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 16),
    _RadAcctSrv2Port_Type()
)
radAcctSrv2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctSrv2Port.setStatus("current")


class _RadAcctSrv2Sec_Type(DisplayString):
    """Custom type radAcctSrv2Sec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_RadAcctSrv2Sec_Type.__name__ = "DisplayString"
_RadAcctSrv2Sec_Object = MibTableColumn
radAcctSrv2Sec = _RadAcctSrv2Sec_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 17),
    _RadAcctSrv2Sec_Type()
)
radAcctSrv2Sec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctSrv2Sec.setStatus("current")


class _RadRetrMethod_Type(Integer32):
    """Custom type radRetrMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failover", 0),
          ("round-robin", 1))
    )


_RadRetrMethod_Type.__name__ = "Integer32"
_RadRetrMethod_Object = MibTableColumn
radRetrMethod = _RadRetrMethod_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 18),
    _RadRetrMethod_Type()
)
radRetrMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radRetrMethod.setStatus("current")
_RadRetrFreq_Type = Integer32
_RadRetrFreq_Object = MibTableColumn
radRetrFreq = _RadRetrFreq_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 19),
    _RadRetrFreq_Type()
)
radRetrFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radRetrFreq.setStatus("current")
_RadRetrAttempts_Type = Integer32
_RadRetrAttempts_Object = MibTableColumn
radRetrAttempts = _RadRetrAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 20),
    _RadRetrAttempts_Type()
)
radRetrAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radRetrAttempts.setStatus("current")
_ProfStatus_Type = RowStatus
_ProfStatus_Object = MibTableColumn
profStatus = _ProfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 1, 1, 1, 21),
    _ProfStatus_Type()
)
profStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profStatus.setStatus("current")
_RBroutes_ObjectIdentity = ObjectIdentity
rBroutes = _RBroutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2)
)
_RealmBasedRoutingTable_Object = MibTable
realmBasedRoutingTable = _RealmBasedRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1)
)
if mibBuilder.loadTexts:
    realmBasedRoutingTable.setStatus("current")
_RealmBasedRoutingTableEntry_Object = MibTableRow
realmBasedRoutingTableEntry = _RealmBasedRoutingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1)
)
realmBasedRoutingTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "realmIndex"),
)
if mibBuilder.loadTexts:
    realmBasedRoutingTableEntry.setStatus("current")
_RealmIndex_Type = Integer32
_RealmIndex_Object = MibTableColumn
realmIndex = _RealmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 1),
    _RealmIndex_Type()
)
realmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realmIndex.setStatus("current")


class _RealmEntryActive_Type(Integer32):
    """Custom type realmEntryActive based on Integer32"""
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


_RealmEntryActive_Type.__name__ = "Integer32"
_RealmEntryActive_Object = MibTableColumn
realmEntryActive = _RealmEntryActive_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 2),
    _RealmEntryActive_Type()
)
realmEntryActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realmEntryActive.setStatus("current")


class _RealmWildcard_Type(Integer32):
    """Custom type realmWildcard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RealmWildcard_Type.__name__ = "Integer32"
_RealmWildcard_Object = MibTableColumn
realmWildcard = _RealmWildcard_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 3),
    _RealmWildcard_Type()
)
realmWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realmWildcard.setStatus("current")


class _RealmName_Type(DisplayString):
    """Custom type realmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RealmName_Type.__name__ = "DisplayString"
_RealmName_Object = MibTableColumn
realmName = _RealmName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 4),
    _RealmName_Type()
)
realmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realmName.setStatus("current")


class _RealmMatchType_Type(Integer32):
    """Custom type realmMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prefixOnly", 0),
          ("prefixOrSuffix", 2),
          ("suffixOnly", 1))
    )


_RealmMatchType_Type.__name__ = "Integer32"
_RealmMatchType_Object = MibTableColumn
realmMatchType = _RealmMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 5),
    _RealmMatchType_Type()
)
realmMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realmMatchType.setStatus("current")


class _RealmProfile_Type(DisplayString):
    """Custom type realmProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_RealmProfile_Type.__name__ = "DisplayString"
_RealmProfile_Object = MibTableColumn
realmProfile = _RealmProfile_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 6),
    _RealmProfile_Type()
)
realmProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realmProfile.setStatus("current")


class _RealmStrip_Type(Integer32):
    """Custom type realmStrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dontStrip", 0),
          ("strip", 1))
    )


_RealmStrip_Type.__name__ = "Integer32"
_RealmStrip_Object = MibTableColumn
realmStrip = _RealmStrip_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 7),
    _RealmStrip_Type()
)
realmStrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realmStrip.setStatus("current")
_RealmStatus_Type = RowStatus
_RealmStatus_Object = MibTableColumn
realmStatus = _RealmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 8),
    _RealmStatus_Type()
)
realmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realmStatus.setStatus("current")


class _RealmTunProfile_Type(DisplayString):
    """Custom type realmTunProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_RealmTunProfile_Type.__name__ = "DisplayString"
_RealmTunProfile_Object = MibTableColumn
realmTunProfile = _RealmTunProfile_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 9),
    _RealmTunProfile_Type()
)
realmTunProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realmTunProfile.setStatus("current")


class _RealmTunStrip_Type(Integer32):
    """Custom type realmTunStrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dontStrip", 0),
          ("strip", 1))
    )


_RealmTunStrip_Type.__name__ = "Integer32"
_RealmTunStrip_Object = MibTableColumn
realmTunStrip = _RealmTunStrip_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 10),
    _RealmTunStrip_Type()
)
realmTunStrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realmTunStrip.setStatus("current")


class _RealmTunLocHostName_Type(DisplayString):
    """Custom type realmTunLocHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_RealmTunLocHostName_Type.__name__ = "DisplayString"
_RealmTunLocHostName_Object = MibTableColumn
realmTunLocHostName = _RealmTunLocHostName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 2, 1, 1, 11),
    _RealmTunLocHostName_Type()
)
realmTunLocHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realmTunLocHostName.setStatus("current")
_RBtunnelProfiles_ObjectIdentity = ObjectIdentity
rBtunnelProfiles = _RBtunnelProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 3)
)
_TunnelProfileTable_Object = MibTable
tunnelProfileTable = _TunnelProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 3, 1)
)
if mibBuilder.loadTexts:
    tunnelProfileTable.setStatus("current")
_TunnelProfileTableEntry_Object = MibTableRow
tunnelProfileTableEntry = _TunnelProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 3, 1, 1)
)
tunnelProfileTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "tunProfIndex"),
)
if mibBuilder.loadTexts:
    tunnelProfileTableEntry.setStatus("current")
_TunProfIndex_Type = Integer32
_TunProfIndex_Object = MibTableColumn
tunProfIndex = _TunProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 3, 1, 1, 2),
    _TunProfIndex_Type()
)
tunProfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunProfIndex.setStatus("current")


class _TunProfName_Type(DisplayString):
    """Custom type tunProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TunProfName_Type.__name__ = "DisplayString"
_TunProfName_Object = MibTableColumn
tunProfName = _TunProfName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 3, 1, 1, 4),
    _TunProfName_Type()
)
tunProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunProfName.setStatus("current")


class _TunPassword_Type(DisplayString):
    """Custom type tunPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TunPassword_Type.__name__ = "DisplayString"
_TunPassword_Object = MibTableColumn
tunPassword = _TunPassword_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 3, 1, 1, 6),
    _TunPassword_Type()
)
tunPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunPassword.setStatus("current")
_TunPeerIp_Type = IpAddress
_TunPeerIp_Object = MibTableColumn
tunPeerIp = _TunPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 3, 1, 1, 8),
    _TunPeerIp_Type()
)
tunPeerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunPeerIp.setStatus("current")
_TunProfStatus_Type = RowStatus
_TunProfStatus_Object = MibTableColumn
tunProfStatus = _TunProfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 39, 3, 1, 1, 20),
    _TunProfStatus_Type()
)
tunProfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunProfStatus.setStatus("current")
_Sessionlimit_ObjectIdentity = ObjectIdentity
sessionlimit = _Sessionlimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 40)
)


class _SessionLimitEnable_Type(Integer32):
    """Custom type sessionLimitEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SessionLimitEnable_Type.__name__ = "Integer32"
_SessionLimitEnable_Object = MibScalar
sessionLimitEnable = _SessionLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 40, 1),
    _SessionLimitEnable_Type()
)
sessionLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLimitEnable.setStatus("current")
_SessionLimitMeanRate_Type = Integer32
_SessionLimitMeanRate_Object = MibScalar
sessionLimitMeanRate = _SessionLimitMeanRate_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 40, 2),
    _SessionLimitMeanRate_Type()
)
sessionLimitMeanRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLimitMeanRate.setStatus("current")
_SessionLimitBurstSize_Type = Integer32
_SessionLimitBurstSize_Object = MibScalar
sessionLimitBurstSize = _SessionLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 40, 3),
    _SessionLimitBurstSize_Type()
)
sessionLimitBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLimitBurstSize.setStatus("current")
_SessionLimitTimeInterval_Type = Integer32
_SessionLimitTimeInterval_Object = MibScalar
sessionLimitTimeInterval = _SessionLimitTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 40, 4),
    _SessionLimitTimeInterval_Type()
)
sessionLimitTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLimitTimeInterval.setStatus("current")


class _SessionLimitFilterOffendersEnable_Type(Integer32):
    """Custom type sessionLimitFilterOffendersEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SessionLimitFilterOffendersEnable_Type.__name__ = "Integer32"
_SessionLimitFilterOffendersEnable_Object = MibScalar
sessionLimitFilterOffendersEnable = _SessionLimitFilterOffendersEnable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 40, 5),
    _SessionLimitFilterOffendersEnable_Type()
)
sessionLimitFilterOffendersEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLimitFilterOffendersEnable.setStatus("current")
_MacFiltering_ObjectIdentity = ObjectIdentity
macFiltering = _MacFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 41)
)


class _MacFilteringOn_Type(Integer32):
    """Custom type macFilteringOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MacFilteringOn_Type.__name__ = "Integer32"
_MacFilteringOn_Object = MibScalar
macFilteringOn = _MacFilteringOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 41, 1),
    _MacFilteringOn_Type()
)
macFilteringOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilteringOn.setStatus("current")
_MacFilteringTable_Object = MibTable
macFilteringTable = _MacFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 41, 4)
)
if mibBuilder.loadTexts:
    macFilteringTable.setStatus("current")
_MacFilteringTableEntry_Object = MibTableRow
macFilteringTableEntry = _MacFilteringTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 41, 4, 1)
)
macFilteringTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "macFilteringTableIndex"),
)
if mibBuilder.loadTexts:
    macFilteringTableEntry.setStatus("current")
_MacFilteringTableIndex_Type = Integer32
_MacFilteringTableIndex_Object = MibTableColumn
macFilteringTableIndex = _MacFilteringTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 41, 4, 1, 1),
    _MacFilteringTableIndex_Type()
)
macFilteringTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilteringTableIndex.setStatus("current")
_MacFilteringTableAddress_Type = MacAddress
_MacFilteringTableAddress_Object = MibTableColumn
macFilteringTableAddress = _MacFilteringTableAddress_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 41, 4, 1, 2),
    _MacFilteringTableAddress_Type()
)
macFilteringTableAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilteringTableAddress.setStatus("current")
_MacFilteringStatus_Type = RowStatus
_MacFilteringStatus_Object = MibTableColumn
macFilteringStatus = _MacFilteringStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 41, 4, 1, 3),
    _MacFilteringStatus_Type()
)
macFilteringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilteringStatus.setStatus("current")
_Tunneling_ObjectIdentity = ObjectIdentity
tunneling = _Tunneling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 42)
)


class _TunnelingOn_Type(Integer32):
    """Custom type tunnelingOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TunnelingOn_Type.__name__ = "Integer32"
_TunnelingOn_Object = MibScalar
tunnelingOn = _TunnelingOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 42, 1),
    _TunnelingOn_Type()
)
tunnelingOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelingOn.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43)
)


class _WirelessSsid_Type(DisplayString):
    """Custom type wirelessSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WirelessSsid_Type.__name__ = "DisplayString"
_WirelessSsid_Object = MibScalar
wirelessSsid = _WirelessSsid_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 1),
    _WirelessSsid_Type()
)
wirelessSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSsid.setStatus("current")


class _WirelessSsidBroadcastOn_Type(Integer32):
    """Custom type wirelessSsidBroadcastOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WirelessSsidBroadcastOn_Type.__name__ = "Integer32"
_WirelessSsidBroadcastOn_Object = MibScalar
wirelessSsidBroadcastOn = _WirelessSsidBroadcastOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 2),
    _WirelessSsidBroadcastOn_Type()
)
wirelessSsidBroadcastOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSsidBroadcastOn.setStatus("current")


class _WirelessChannel_Type(Integer32):
    """Custom type wirelessChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
    )


_WirelessChannel_Type.__name__ = "Integer32"
_WirelessChannel_Object = MibScalar
wirelessChannel = _WirelessChannel_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 3),
    _WirelessChannel_Type()
)
wirelessChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessChannel.setStatus("current")


class _WirelessRate_Type(Integer32):
    """Custom type wirelessRate based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("rate-11Mbits", 6),
          ("rate-12Mbits", 7),
          ("rate-18Mbits", 8),
          ("rate-1Mbits", 1),
          ("rate-24Mbits", 9),
          ("rate-2Mbits", 2),
          ("rate-36Mbits", 10),
          ("rate-48Mbits", 11),
          ("rate-54Mbits", 12),
          ("rate-5andhalfMbits", 3),
          ("rate-6Mbits", 4),
          ("rate-9Mbits", 5))
    )


_WirelessRate_Type.__name__ = "Integer32"
_WirelessRate_Object = MibScalar
wirelessRate = _WirelessRate_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 4),
    _WirelessRate_Type()
)
wirelessRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRate.setStatus("current")


class _WirelessPower_Type(Integer32):
    """Custom type wirelessPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eighth", 3),
          ("full", 0),
          ("half", 1),
          ("min", 4),
          ("quarter", 2))
    )


_WirelessPower_Type.__name__ = "Integer32"
_WirelessPower_Object = MibScalar
wirelessPower = _WirelessPower_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 5),
    _WirelessPower_Type()
)
wirelessPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessPower.setStatus("current")


class _WirelessFragLength_Type(Integer32):
    """Custom type wirelessFragLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_WirelessFragLength_Type.__name__ = "Integer32"
_WirelessFragLength_Object = MibScalar
wirelessFragLength = _WirelessFragLength_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 6),
    _WirelessFragLength_Type()
)
wirelessFragLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessFragLength.setStatus("current")


class _WirelessRtsLength_Type(Integer32):
    """Custom type wirelessRtsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_WirelessRtsLength_Type.__name__ = "Integer32"
_WirelessRtsLength_Object = MibScalar
wirelessRtsLength = _WirelessRtsLength_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 7),
    _WirelessRtsLength_Type()
)
wirelessRtsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRtsLength.setStatus("current")


class _WirelessBeaconInterval_Type(Integer32):
    """Custom type wirelessBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_WirelessBeaconInterval_Type.__name__ = "Integer32"
_WirelessBeaconInterval_Object = MibScalar
wirelessBeaconInterval = _WirelessBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 8),
    _WirelessBeaconInterval_Type()
)
wirelessBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessBeaconInterval.setStatus("current")


class _WirelessDtim_Type(Integer32):
    """Custom type wirelessDtim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WirelessDtim_Type.__name__ = "Integer32"
_WirelessDtim_Object = MibScalar
wirelessDtim = _WirelessDtim_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 9),
    _WirelessDtim_Type()
)
wirelessDtim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessDtim.setStatus("current")


class _WirelessShortPreambleOn_Type(Integer32):
    """Custom type wirelessShortPreambleOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WirelessShortPreambleOn_Type.__name__ = "Integer32"
_WirelessShortPreambleOn_Object = MibScalar
wirelessShortPreambleOn = _WirelessShortPreambleOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 10),
    _WirelessShortPreambleOn_Type()
)
wirelessShortPreambleOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessShortPreambleOn.setStatus("current")
_WirelessMssid_ObjectIdentity = ObjectIdentity
wirelessMssid = _WirelessMssid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 11)
)


class _WirelessMssidVlanOn_Type(Integer32):
    """Custom type wirelessMssidVlanOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WirelessMssidVlanOn_Type.__name__ = "Integer32"
_WirelessMssidVlanOn_Object = MibScalar
wirelessMssidVlanOn = _WirelessMssidVlanOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 11, 1),
    _WirelessMssidVlanOn_Type()
)
wirelessMssidVlanOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMssidVlanOn.setStatus("current")


class _WirelessMssidVlanDefaultOn_Type(Integer32):
    """Custom type wirelessMssidVlanDefaultOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WirelessMssidVlanDefaultOn_Type.__name__ = "Integer32"
_WirelessMssidVlanDefaultOn_Object = MibScalar
wirelessMssidVlanDefaultOn = _WirelessMssidVlanDefaultOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 11, 2),
    _WirelessMssidVlanDefaultOn_Type()
)
wirelessMssidVlanDefaultOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMssidVlanDefaultOn.setStatus("current")


class _WirelessMssidVlanDefaultTag_Type(Integer32):
    """Custom type wirelessMssidVlanDefaultTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WirelessMssidVlanDefaultTag_Type.__name__ = "Integer32"
_WirelessMssidVlanDefaultTag_Object = MibScalar
wirelessMssidVlanDefaultTag = _WirelessMssidVlanDefaultTag_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 11, 3),
    _WirelessMssidVlanDefaultTag_Type()
)
wirelessMssidVlanDefaultTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMssidVlanDefaultTag.setStatus("current")
_WirelessMssidTable_Object = MibTable
wirelessMssidTable = _WirelessMssidTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 11, 4)
)
if mibBuilder.loadTexts:
    wirelessMssidTable.setStatus("current")
_WirelessMssidTableEntry_Object = MibTableRow
wirelessMssidTableEntry = _WirelessMssidTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 11, 4, 1)
)
wirelessMssidTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "mssidIndex"),
)
if mibBuilder.loadTexts:
    wirelessMssidTableEntry.setStatus("current")
_MssidIndex_Type = Integer32
_MssidIndex_Object = MibTableColumn
mssidIndex = _MssidIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 11, 4, 1, 1),
    _MssidIndex_Type()
)
mssidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssidIndex.setStatus("current")


class _MssidName_Type(DisplayString):
    """Custom type mssidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MssidName_Type.__name__ = "DisplayString"
_MssidName_Object = MibTableColumn
mssidName = _MssidName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 11, 4, 1, 2),
    _MssidName_Type()
)
mssidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mssidName.setStatus("current")


class _MssidVlan_Type(Integer32):
    """Custom type mssidVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MssidVlan_Type.__name__ = "Integer32"
_MssidVlan_Object = MibTableColumn
mssidVlan = _MssidVlan_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 11, 4, 1, 3),
    _MssidVlan_Type()
)
mssidVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mssidVlan.setStatus("current")
_MssidStatus_Type = RowStatus
_MssidStatus_Object = MibTableColumn
mssidStatus = _MssidStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 11, 4, 1, 4),
    _MssidStatus_Type()
)
mssidStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mssidStatus.setStatus("current")
_WirelessWep_ObjectIdentity = ObjectIdentity
wirelessWep = _WirelessWep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12)
)


class _WirelessWepOn_Type(Integer32):
    """Custom type wirelessWepOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WirelessWepOn_Type.__name__ = "Integer32"
_WirelessWepOn_Object = MibScalar
wirelessWepOn = _WirelessWepOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12, 1),
    _WirelessWepOn_Type()
)
wirelessWepOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessWepOn.setStatus("current")


class _WirelessWepClients_Type(DisplayString):
    """Custom type wirelessWepClients based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 21),
    )


_WirelessWepClients_Type.__name__ = "DisplayString"
_WirelessWepClients_Object = MibScalar
wirelessWepClients = _WirelessWepClients_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12, 3),
    _WirelessWepClients_Type()
)
wirelessWepClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessWepClients.setStatus("current")


class _WirelessWepAuthType_Type(Integer32):
    """Custom type wirelessWepAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("shared", 1))
    )


_WirelessWepAuthType_Type.__name__ = "Integer32"
_WirelessWepAuthType_Object = MibScalar
wirelessWepAuthType = _WirelessWepAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12, 4),
    _WirelessWepAuthType_Type()
)
wirelessWepAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessWepAuthType.setStatus("current")


class _WirelessWepNon1xAllowedOn_Type(Integer32):
    """Custom type wirelessWepNon1xAllowedOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WirelessWepNon1xAllowedOn_Type.__name__ = "Integer32"
_WirelessWepNon1xAllowedOn_Object = MibScalar
wirelessWepNon1xAllowedOn = _WirelessWepNon1xAllowedOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12, 5),
    _WirelessWepNon1xAllowedOn_Type()
)
wirelessWepNon1xAllowedOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessWepNon1xAllowedOn.setStatus("current")


class _WirelessWepKeyType_Type(Integer32):
    """Custom type wirelessWepKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 0))
    )


_WirelessWepKeyType_Type.__name__ = "Integer32"
_WirelessWepKeyType_Object = MibScalar
wirelessWepKeyType = _WirelessWepKeyType_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12, 6),
    _WirelessWepKeyType_Type()
)
wirelessWepKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessWepKeyType.setStatus("current")


class _WirelessWepDefaultKey_Type(Integer32):
    """Custom type wirelessWepDefaultKey based on Integer32"""
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
        *(("key-1", 1),
          ("key-2", 2),
          ("key-3", 3),
          ("key-4", 4))
    )


_WirelessWepDefaultKey_Type.__name__ = "Integer32"
_WirelessWepDefaultKey_Object = MibScalar
wirelessWepDefaultKey = _WirelessWepDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12, 7),
    _WirelessWepDefaultKey_Type()
)
wirelessWepDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessWepDefaultKey.setStatus("current")


class _WirelessWepKey1_Type(DisplayString):
    """Custom type wirelessWepKey1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WirelessWepKey1_Type.__name__ = "DisplayString"
_WirelessWepKey1_Object = MibScalar
wirelessWepKey1 = _WirelessWepKey1_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12, 8),
    _WirelessWepKey1_Type()
)
wirelessWepKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessWepKey1.setStatus("current")


class _WirelessWepKey2_Type(DisplayString):
    """Custom type wirelessWepKey2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WirelessWepKey2_Type.__name__ = "DisplayString"
_WirelessWepKey2_Object = MibScalar
wirelessWepKey2 = _WirelessWepKey2_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12, 9),
    _WirelessWepKey2_Type()
)
wirelessWepKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessWepKey2.setStatus("current")


class _WirelessWepKey3_Type(DisplayString):
    """Custom type wirelessWepKey3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WirelessWepKey3_Type.__name__ = "DisplayString"
_WirelessWepKey3_Object = MibScalar
wirelessWepKey3 = _WirelessWepKey3_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12, 10),
    _WirelessWepKey3_Type()
)
wirelessWepKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessWepKey3.setStatus("current")


class _WirelessWepKey4_Type(DisplayString):
    """Custom type wirelessWepKey4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WirelessWepKey4_Type.__name__ = "DisplayString"
_WirelessWepKey4_Object = MibScalar
wirelessWepKey4 = _WirelessWepKey4_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 43, 12, 11),
    _WirelessWepKey4_Type()
)
wirelessWepKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessWepKey4.setStatus("current")
_PppoeClient_ObjectIdentity = ObjectIdentity
pppoeClient = _PppoeClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 44)
)


class _PppoeSvcName_Type(DisplayString):
    """Custom type pppoeSvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PppoeSvcName_Type.__name__ = "DisplayString"
_PppoeSvcName_Object = MibScalar
pppoeSvcName = _PppoeSvcName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 44, 1),
    _PppoeSvcName_Type()
)
pppoeSvcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeSvcName.setStatus("current")
_PppEchoReqIntvl_Type = Integer32
_PppEchoReqIntvl_Object = MibScalar
pppEchoReqIntvl = _PppEchoReqIntvl_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 44, 2),
    _PppEchoReqIntvl_Type()
)
pppEchoReqIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppEchoReqIntvl.setStatus("current")
_PppEchoMaxNonresp_Type = Integer32
_PppEchoMaxNonresp_Object = MibScalar
pppEchoMaxNonresp = _PppEchoMaxNonresp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 44, 3),
    _PppEchoMaxNonresp_Type()
)
pppEchoMaxNonresp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppEchoMaxNonresp.setStatus("current")


class _PppAuthUsername_Type(DisplayString):
    """Custom type pppAuthUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PppAuthUsername_Type.__name__ = "DisplayString"
_PppAuthUsername_Object = MibScalar
pppAuthUsername = _PppAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 44, 4),
    _PppAuthUsername_Type()
)
pppAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthUsername.setStatus("current")


class _PppAuthPassword_Type(DisplayString):
    """Custom type pppAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PppAuthPassword_Type.__name__ = "DisplayString"
_PppAuthPassword_Object = MibScalar
pppAuthPassword = _PppAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 44, 5),
    _PppAuthPassword_Type()
)
pppAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthPassword.setStatus("current")


class _PppIpCfgMode_Type(Integer32):
    """Custom type pppIpCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_PppIpCfgMode_Type.__name__ = "Integer32"
_PppIpCfgMode_Object = MibScalar
pppIpCfgMode = _PppIpCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 44, 6),
    _PppIpCfgMode_Type()
)
pppIpCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppIpCfgMode.setStatus("current")
_PppStaticIpAddr_Type = IpAddress
_PppStaticIpAddr_Object = MibScalar
pppStaticIpAddr = _PppStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 44, 7),
    _PppStaticIpAddr_Type()
)
pppStaticIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppStaticIpAddr.setStatus("current")
_PppMaxTcpMss_Type = Integer32
_PppMaxTcpMss_Object = MibScalar
pppMaxTcpMss = _PppMaxTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 44, 8),
    _PppMaxTcpMss_Type()
)
pppMaxTcpMss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppMaxTcpMss.setStatus("current")
_Dyndns_ObjectIdentity = ObjectIdentity
dyndns = _Dyndns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 50)
)


class _DynDnsEnable_Type(Integer32):
    """Custom type dynDnsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DynDnsEnable_Type.__name__ = "Integer32"
_DynDnsEnable_Object = MibScalar
dynDnsEnable = _DynDnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 50, 0),
    _DynDnsEnable_Type()
)
dynDnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynDnsEnable.setStatus("current")


class _DynDnsProtocol_Type(Integer32):
    """Custom type dynDnsProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynDnsOrgProto", 0),
          ("dynDnsOrgProtoSecure", 1))
    )


_DynDnsProtocol_Type.__name__ = "Integer32"
_DynDnsProtocol_Object = MibScalar
dynDnsProtocol = _DynDnsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 50, 1),
    _DynDnsProtocol_Type()
)
dynDnsProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynDnsProtocol.setStatus("current")


class _DynDnsServer_Type(DisplayString):
    """Custom type dynDnsServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DynDnsServer_Type.__name__ = "DisplayString"
_DynDnsServer_Object = MibScalar
dynDnsServer = _DynDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 50, 2),
    _DynDnsServer_Type()
)
dynDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynDnsServer.setStatus("current")


class _DynDnsPort_Type(Integer32):
    """Custom type dynDnsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynDnsPort443", 2),
          ("dynDnsPort80", 0),
          ("dynDnsPort8245", 1))
    )


_DynDnsPort_Type.__name__ = "Integer32"
_DynDnsPort_Object = MibScalar
dynDnsPort = _DynDnsPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 50, 3),
    _DynDnsPort_Type()
)
dynDnsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynDnsPort.setStatus("current")


class _DynDnsHostname_Type(DisplayString):
    """Custom type dynDnsHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DynDnsHostname_Type.__name__ = "DisplayString"
_DynDnsHostname_Object = MibScalar
dynDnsHostname = _DynDnsHostname_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 50, 4),
    _DynDnsHostname_Type()
)
dynDnsHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynDnsHostname.setStatus("current")


class _DynDnsUsername_Type(DisplayString):
    """Custom type dynDnsUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DynDnsUsername_Type.__name__ = "DisplayString"
_DynDnsUsername_Object = MibScalar
dynDnsUsername = _DynDnsUsername_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 50, 5),
    _DynDnsUsername_Type()
)
dynDnsUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynDnsUsername.setStatus("current")


class _DynDnsPassword_Type(DisplayString):
    """Custom type dynDnsPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DynDnsPassword_Type.__name__ = "DisplayString"
_DynDnsPassword_Object = MibScalar
dynDnsPassword = _DynDnsPassword_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 50, 6),
    _DynDnsPassword_Type()
)
dynDnsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynDnsPassword.setStatus("current")


class _DynDnsForceUpdate_Type(Integer32):
    """Custom type dynDnsForceUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DynDnsForceUpdate_Type.__name__ = "Integer32"
_DynDnsForceUpdate_Object = MibScalar
dynDnsForceUpdate = _DynDnsForceUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 50, 7),
    _DynDnsForceUpdate_Type()
)
dynDnsForceUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynDnsForceUpdate.setStatus("current")
_LocalWeb_ObjectIdentity = ObjectIdentity
localWeb = _LocalWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52)
)
_LocalWebPages_ObjectIdentity = ObjectIdentity
localWebPages = _LocalWebPages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 4)
)
_LocalWebPagesTable_Object = MibTable
localWebPagesTable = _LocalWebPagesTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 4, 1)
)
if mibBuilder.loadTexts:
    localWebPagesTable.setStatus("current")
_LocalWebPagesTableEntry_Object = MibTableRow
localWebPagesTableEntry = _LocalWebPagesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 4, 1, 1)
)
localWebPagesTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "localWebPagesTableIndex"),
)
if mibBuilder.loadTexts:
    localWebPagesTableEntry.setStatus("current")
_LocalWebPagesTableIndex_Type = Integer32
_LocalWebPagesTableIndex_Object = MibTableColumn
localWebPagesTableIndex = _LocalWebPagesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 4, 1, 1, 1),
    _LocalWebPagesTableIndex_Type()
)
localWebPagesTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localWebPagesTableIndex.setStatus("current")


class _LocalWebPagesTableName_Type(DisplayString):
    """Custom type localWebPagesTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_LocalWebPagesTableName_Type.__name__ = "DisplayString"
_LocalWebPagesTableName_Object = MibTableColumn
localWebPagesTableName = _LocalWebPagesTableName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 4, 1, 1, 2),
    _LocalWebPagesTableName_Type()
)
localWebPagesTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localWebPagesTableName.setStatus("current")
_LocalWebPagesTableStatus_Type = RowStatus
_LocalWebPagesTableStatus_Object = MibTableColumn
localWebPagesTableStatus = _LocalWebPagesTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 4, 1, 1, 3),
    _LocalWebPagesTableStatus_Type()
)
localWebPagesTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localWebPagesTableStatus.setStatus("current")
_LocalWebImages_ObjectIdentity = ObjectIdentity
localWebImages = _LocalWebImages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 8)
)
_LocalWebImagesTable_Object = MibTable
localWebImagesTable = _LocalWebImagesTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 8, 1)
)
if mibBuilder.loadTexts:
    localWebImagesTable.setStatus("current")
_LocalWebImagesTableEntry_Object = MibTableRow
localWebImagesTableEntry = _LocalWebImagesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 8, 1, 1)
)
localWebImagesTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "localWebImagesTableIndex"),
)
if mibBuilder.loadTexts:
    localWebImagesTableEntry.setStatus("current")
_LocalWebImagesTableIndex_Type = Integer32
_LocalWebImagesTableIndex_Object = MibTableColumn
localWebImagesTableIndex = _LocalWebImagesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 8, 1, 1, 1),
    _LocalWebImagesTableIndex_Type()
)
localWebImagesTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localWebImagesTableIndex.setStatus("current")


class _LocalWebImagesTableName_Type(DisplayString):
    """Custom type localWebImagesTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 237),
    )


_LocalWebImagesTableName_Type.__name__ = "DisplayString"
_LocalWebImagesTableName_Object = MibTableColumn
localWebImagesTableName = _LocalWebImagesTableName_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 8, 1, 1, 2),
    _LocalWebImagesTableName_Type()
)
localWebImagesTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localWebImagesTableName.setStatus("current")
_LocalWebImagesTableStatus_Type = RowStatus
_LocalWebImagesTableStatus_Object = MibTableColumn
localWebImagesTableStatus = _LocalWebImagesTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 52, 8, 1, 1, 3),
    _LocalWebImagesTableStatus_Type()
)
localWebImagesTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localWebImagesTableStatus.setStatus("current")
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54)
)


class _IpsecVpnOn_Type(Integer32):
    """Custom type ipsecVpnOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecVpnOn_Type.__name__ = "Integer32"
_IpsecVpnOn_Object = MibScalar
ipsecVpnOn = _IpsecVpnOn_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 1),
    _IpsecVpnOn_Type()
)
ipsecVpnOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecVpnOn.setStatus("current")
_IpsecPeers_ObjectIdentity = ObjectIdentity
ipsecPeers = _IpsecPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4)
)
_IpsecPeerTable_Object = MibTable
ipsecPeerTable = _IpsecPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1)
)
if mibBuilder.loadTexts:
    ipsecPeerTable.setStatus("current")
_IpsecPeerTableEntry_Object = MibTableRow
ipsecPeerTableEntry = _IpsecPeerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1)
)
ipsecPeerTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "ipsecPeerIndex"),
)
if mibBuilder.loadTexts:
    ipsecPeerTableEntry.setStatus("current")
_IpsecPeerIndex_Type = Integer32
_IpsecPeerIndex_Object = MibTableColumn
ipsecPeerIndex = _IpsecPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 1),
    _IpsecPeerIndex_Type()
)
ipsecPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecPeerIndex.setStatus("current")
_IpsecPeerIpAddr_Type = IpAddress
_IpsecPeerIpAddr_Object = MibTableColumn
ipsecPeerIpAddr = _IpsecPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 2),
    _IpsecPeerIpAddr_Type()
)
ipsecPeerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerIpAddr.setStatus("current")


class _IpsecPeerAuthMethod_Type(Integer32):
    """Custom type ipsecPeerAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("preSharedKey", 0),
          ("x509Certificate", 1))
    )


_IpsecPeerAuthMethod_Type.__name__ = "Integer32"
_IpsecPeerAuthMethod_Object = MibTableColumn
ipsecPeerAuthMethod = _IpsecPeerAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 3),
    _IpsecPeerAuthMethod_Type()
)
ipsecPeerAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerAuthMethod.setStatus("current")


class _IpsecPeerSharedKey_Type(DisplayString):
    """Custom type ipsecPeerSharedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IpsecPeerSharedKey_Type.__name__ = "DisplayString"
_IpsecPeerSharedKey_Object = MibTableColumn
ipsecPeerSharedKey = _IpsecPeerSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 4),
    _IpsecPeerSharedKey_Type()
)
ipsecPeerSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerSharedKey.setStatus("current")


class _IpsecPeerPrivkeyFile_Type(DisplayString):
    """Custom type ipsecPeerPrivkeyFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_IpsecPeerPrivkeyFile_Type.__name__ = "DisplayString"
_IpsecPeerPrivkeyFile_Object = MibTableColumn
ipsecPeerPrivkeyFile = _IpsecPeerPrivkeyFile_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 5),
    _IpsecPeerPrivkeyFile_Type()
)
ipsecPeerPrivkeyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerPrivkeyFile.setStatus("current")


class _IpsecPeerCertFile_Type(DisplayString):
    """Custom type ipsecPeerCertFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_IpsecPeerCertFile_Type.__name__ = "DisplayString"
_IpsecPeerCertFile_Object = MibTableColumn
ipsecPeerCertFile = _IpsecPeerCertFile_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 6),
    _IpsecPeerCertFile_Type()
)
ipsecPeerCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerCertFile.setStatus("current")


class _IpsecPeerEncDesOk_Type(Integer32):
    """Custom type ipsecPeerEncDesOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_IpsecPeerEncDesOk_Type.__name__ = "Integer32"
_IpsecPeerEncDesOk_Object = MibTableColumn
ipsecPeerEncDesOk = _IpsecPeerEncDesOk_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 7),
    _IpsecPeerEncDesOk_Type()
)
ipsecPeerEncDesOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerEncDesOk.setStatus("current")


class _IpsecPeerEnc3DesOk_Type(Integer32):
    """Custom type ipsecPeerEnc3DesOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_IpsecPeerEnc3DesOk_Type.__name__ = "Integer32"
_IpsecPeerEnc3DesOk_Object = MibTableColumn
ipsecPeerEnc3DesOk = _IpsecPeerEnc3DesOk_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 8),
    _IpsecPeerEnc3DesOk_Type()
)
ipsecPeerEnc3DesOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerEnc3DesOk.setStatus("current")


class _IpsecPeerHashMd5Ok_Type(Integer32):
    """Custom type ipsecPeerHashMd5Ok based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_IpsecPeerHashMd5Ok_Type.__name__ = "Integer32"
_IpsecPeerHashMd5Ok_Object = MibTableColumn
ipsecPeerHashMd5Ok = _IpsecPeerHashMd5Ok_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 9),
    _IpsecPeerHashMd5Ok_Type()
)
ipsecPeerHashMd5Ok.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerHashMd5Ok.setStatus("current")


class _IpsecPeerHashShaOk_Type(Integer32):
    """Custom type ipsecPeerHashShaOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_IpsecPeerHashShaOk_Type.__name__ = "Integer32"
_IpsecPeerHashShaOk_Object = MibTableColumn
ipsecPeerHashShaOk = _IpsecPeerHashShaOk_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 10),
    _IpsecPeerHashShaOk_Type()
)
ipsecPeerHashShaOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerHashShaOk.setStatus("current")


class _IpsecPeerKeyStrength_Type(Integer32):
    """Custom type ipsecPeerKeyStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("key1024-bit", 1),
          ("key768-bit", 0))
    )


_IpsecPeerKeyStrength_Type.__name__ = "Integer32"
_IpsecPeerKeyStrength_Object = MibTableColumn
ipsecPeerKeyStrength = _IpsecPeerKeyStrength_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 11),
    _IpsecPeerKeyStrength_Type()
)
ipsecPeerKeyStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerKeyStrength.setStatus("current")
_IpsecPeerLifetime_Type = Integer32
_IpsecPeerLifetime_Object = MibTableColumn
ipsecPeerLifetime = _IpsecPeerLifetime_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 12),
    _IpsecPeerLifetime_Type()
)
ipsecPeerLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerLifetime.setStatus("current")
_IpsecPeerStatus_Type = RowStatus
_IpsecPeerStatus_Object = MibTableColumn
ipsecPeerStatus = _IpsecPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 4, 1, 1, 20),
    _IpsecPeerStatus_Type()
)
ipsecPeerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerStatus.setStatus("current")
_IpsecPolicies_ObjectIdentity = ObjectIdentity
ipsecPolicies = _IpsecPolicies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5)
)
_IpsecPolicyTable_Object = MibTable
ipsecPolicyTable = _IpsecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1)
)
if mibBuilder.loadTexts:
    ipsecPolicyTable.setStatus("current")
_IpsecPolicyTableEntry_Object = MibTableRow
ipsecPolicyTableEntry = _IpsecPolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1)
)
ipsecPolicyTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "ipsecPolicyIndex"),
)
if mibBuilder.loadTexts:
    ipsecPolicyTableEntry.setStatus("current")
_IpsecPolicyIndex_Type = Integer32
_IpsecPolicyIndex_Object = MibTableColumn
ipsecPolicyIndex = _IpsecPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 1),
    _IpsecPolicyIndex_Type()
)
ipsecPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecPolicyIndex.setStatus("current")
_IpsecPolicyPeerIp_Type = IpAddress
_IpsecPolicyPeerIp_Object = MibTableColumn
ipsecPolicyPeerIp = _IpsecPolicyPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 2),
    _IpsecPolicyPeerIp_Type()
)
ipsecPolicyPeerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyPeerIp.setStatus("current")
_IpsecPolicyProtocol_Type = Integer32
_IpsecPolicyProtocol_Object = MibTableColumn
ipsecPolicyProtocol = _IpsecPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 3),
    _IpsecPolicyProtocol_Type()
)
ipsecPolicyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyProtocol.setStatus("current")
_IpsecPolicyRemIp_Type = IpAddress
_IpsecPolicyRemIp_Object = MibTableColumn
ipsecPolicyRemIp = _IpsecPolicyRemIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 4),
    _IpsecPolicyRemIp_Type()
)
ipsecPolicyRemIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyRemIp.setStatus("current")
_IpsecPolicyRemSubnet_Type = IpAddress
_IpsecPolicyRemSubnet_Object = MibTableColumn
ipsecPolicyRemSubnet = _IpsecPolicyRemSubnet_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 5),
    _IpsecPolicyRemSubnet_Type()
)
ipsecPolicyRemSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyRemSubnet.setStatus("current")
_IpsecPolicyRemPort_Type = Integer32
_IpsecPolicyRemPort_Object = MibTableColumn
ipsecPolicyRemPort = _IpsecPolicyRemPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 6),
    _IpsecPolicyRemPort_Type()
)
ipsecPolicyRemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyRemPort.setStatus("current")


class _IpsecPolicyUseNetIp_Type(Integer32):
    """Custom type ipsecPolicyUseNetIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_IpsecPolicyUseNetIp_Type.__name__ = "Integer32"
_IpsecPolicyUseNetIp_Object = MibTableColumn
ipsecPolicyUseNetIp = _IpsecPolicyUseNetIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 7),
    _IpsecPolicyUseNetIp_Type()
)
ipsecPolicyUseNetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyUseNetIp.setStatus("current")
_IpsecPolicyLocIp_Type = IpAddress
_IpsecPolicyLocIp_Object = MibTableColumn
ipsecPolicyLocIp = _IpsecPolicyLocIp_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 8),
    _IpsecPolicyLocIp_Type()
)
ipsecPolicyLocIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyLocIp.setStatus("current")
_IpsecPolicyLocSubnet_Type = IpAddress
_IpsecPolicyLocSubnet_Object = MibTableColumn
ipsecPolicyLocSubnet = _IpsecPolicyLocSubnet_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 9),
    _IpsecPolicyLocSubnet_Type()
)
ipsecPolicyLocSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyLocSubnet.setStatus("current")
_IpsecPolicyLocPort_Type = Integer32
_IpsecPolicyLocPort_Object = MibTableColumn
ipsecPolicyLocPort = _IpsecPolicyLocPort_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 10),
    _IpsecPolicyLocPort_Type()
)
ipsecPolicyLocPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyLocPort.setStatus("current")


class _IpsecPolicyType_Type(Integer32):
    """Custom type ipsecPolicyType based on Integer32"""
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
        *(("ah", 3),
          ("bypass", 1),
          ("discard", 0),
          ("esp", 2))
    )


_IpsecPolicyType_Type.__name__ = "Integer32"
_IpsecPolicyType_Object = MibTableColumn
ipsecPolicyType = _IpsecPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 11),
    _IpsecPolicyType_Type()
)
ipsecPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyType.setStatus("current")


class _IpsecPolicyDirType_Type(Integer32):
    """Custom type ipsecPolicyDirType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inAndOut", 2),
          ("inOnly", 0),
          ("outOnly", 1))
    )


_IpsecPolicyDirType_Type.__name__ = "Integer32"
_IpsecPolicyDirType_Object = MibTableColumn
ipsecPolicyDirType = _IpsecPolicyDirType_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 12),
    _IpsecPolicyDirType_Type()
)
ipsecPolicyDirType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyDirType.setStatus("current")


class _IpsecPolicyEncDesOk_Type(Integer32):
    """Custom type ipsecPolicyEncDesOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_IpsecPolicyEncDesOk_Type.__name__ = "Integer32"
_IpsecPolicyEncDesOk_Object = MibTableColumn
ipsecPolicyEncDesOk = _IpsecPolicyEncDesOk_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 13),
    _IpsecPolicyEncDesOk_Type()
)
ipsecPolicyEncDesOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyEncDesOk.setStatus("current")


class _IpsecPolicyEnc3desOk_Type(Integer32):
    """Custom type ipsecPolicyEnc3desOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_IpsecPolicyEnc3desOk_Type.__name__ = "Integer32"
_IpsecPolicyEnc3desOk_Object = MibTableColumn
ipsecPolicyEnc3desOk = _IpsecPolicyEnc3desOk_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 14),
    _IpsecPolicyEnc3desOk_Type()
)
ipsecPolicyEnc3desOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyEnc3desOk.setStatus("current")


class _IpsecPolicyEncNullOk_Type(Integer32):
    """Custom type ipsecPolicyEncNullOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_IpsecPolicyEncNullOk_Type.__name__ = "Integer32"
_IpsecPolicyEncNullOk_Object = MibTableColumn
ipsecPolicyEncNullOk = _IpsecPolicyEncNullOk_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 15),
    _IpsecPolicyEncNullOk_Type()
)
ipsecPolicyEncNullOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyEncNullOk.setStatus("current")


class _IpsecPolicyAuthMd5Ok_Type(Integer32):
    """Custom type ipsecPolicyAuthMd5Ok based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_IpsecPolicyAuthMd5Ok_Type.__name__ = "Integer32"
_IpsecPolicyAuthMd5Ok_Object = MibTableColumn
ipsecPolicyAuthMd5Ok = _IpsecPolicyAuthMd5Ok_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 16),
    _IpsecPolicyAuthMd5Ok_Type()
)
ipsecPolicyAuthMd5Ok.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyAuthMd5Ok.setStatus("current")


class _IpsecPolicyAuthShaOk_Type(Integer32):
    """Custom type ipsecPolicyAuthShaOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_IpsecPolicyAuthShaOk_Type.__name__ = "Integer32"
_IpsecPolicyAuthShaOk_Object = MibTableColumn
ipsecPolicyAuthShaOk = _IpsecPolicyAuthShaOk_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 17),
    _IpsecPolicyAuthShaOk_Type()
)
ipsecPolicyAuthShaOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyAuthShaOk.setStatus("current")


class _IpsecPolicyAuthNullOk_Type(Integer32):
    """Custom type ipsecPolicyAuthNullOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_IpsecPolicyAuthNullOk_Type.__name__ = "Integer32"
_IpsecPolicyAuthNullOk_Object = MibTableColumn
ipsecPolicyAuthNullOk = _IpsecPolicyAuthNullOk_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 18),
    _IpsecPolicyAuthNullOk_Type()
)
ipsecPolicyAuthNullOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyAuthNullOk.setStatus("current")


class _IpsecPolicyPfsStrength_Type(Integer32):
    """Custom type ipsecPolicyPfsStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pfs1024", 2),
          ("pfs768", 1),
          ("pfsNone", 0))
    )


_IpsecPolicyPfsStrength_Type.__name__ = "Integer32"
_IpsecPolicyPfsStrength_Object = MibTableColumn
ipsecPolicyPfsStrength = _IpsecPolicyPfsStrength_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 19),
    _IpsecPolicyPfsStrength_Type()
)
ipsecPolicyPfsStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyPfsStrength.setStatus("current")
_IpsecPolicyMaxLifetime_Type = Integer32
_IpsecPolicyMaxLifetime_Object = MibTableColumn
ipsecPolicyMaxLifetime = _IpsecPolicyMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 20),
    _IpsecPolicyMaxLifetime_Type()
)
ipsecPolicyMaxLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyMaxLifetime.setStatus("current")
_IpsecPolicyMaxLifesize_Type = Integer32
_IpsecPolicyMaxLifesize_Object = MibTableColumn
ipsecPolicyMaxLifesize = _IpsecPolicyMaxLifesize_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 21),
    _IpsecPolicyMaxLifesize_Type()
)
ipsecPolicyMaxLifesize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyMaxLifesize.setStatus("current")


class _IpsecPolicyAutoRenew_Type(Integer32):
    """Custom type ipsecPolicyAutoRenew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_IpsecPolicyAutoRenew_Type.__name__ = "Integer32"
_IpsecPolicyAutoRenew_Object = MibTableColumn
ipsecPolicyAutoRenew = _IpsecPolicyAutoRenew_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 22),
    _IpsecPolicyAutoRenew_Type()
)
ipsecPolicyAutoRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyAutoRenew.setStatus("current")
_IpsecPolicyStatus_Type = RowStatus
_IpsecPolicyStatus_Object = MibTableColumn
ipsecPolicyStatus = _IpsecPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 5, 1, 1, 40),
    _IpsecPolicyStatus_Type()
)
ipsecPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPolicyStatus.setStatus("current")
_IpsecSaStatus_ObjectIdentity = ObjectIdentity
ipsecSaStatus = _IpsecSaStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 6)
)
_IpsecSaStatusTable_Object = MibTable
ipsecSaStatusTable = _IpsecSaStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 6, 1)
)
if mibBuilder.loadTexts:
    ipsecSaStatusTable.setStatus("current")
_IpsecSaStatusTableEntry_Object = MibTableRow
ipsecSaStatusTableEntry = _IpsecSaStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 6, 1, 1)
)
ipsecSaStatusTableEntry.setIndexNames(
    (0, "NOMADIX-MIB", "ipsecSaStatusIndex"),
)
if mibBuilder.loadTexts:
    ipsecSaStatusTableEntry.setStatus("current")
_IpsecSaStatusIndex_Type = Integer32
_IpsecSaStatusIndex_Object = MibTableColumn
ipsecSaStatusIndex = _IpsecSaStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 6, 1, 1, 1),
    _IpsecSaStatusIndex_Type()
)
ipsecSaStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaStatusIndex.setStatus("current")


class _IpsecSaStatusState_Type(Integer32):
    """Custom type ipsecSaStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipsecDisabled", 1),
          ("ipsecUp", 0),
          ("noIkeChannelToPeer", 3),
          ("notConfiguredInStack", 2),
          ("notNegotiatedWithPeer", 4))
    )


_IpsecSaStatusState_Type.__name__ = "Integer32"
_IpsecSaStatusState_Object = MibTableColumn
ipsecSaStatusState = _IpsecSaStatusState_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 6, 1, 1, 2),
    _IpsecSaStatusState_Type()
)
ipsecSaStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaStatusState.setStatus("current")
_IpsecSaStatusStatus_Type = RowStatus
_IpsecSaStatusStatus_Object = MibTableColumn
ipsecSaStatusStatus = _IpsecSaStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 54, 6, 1, 1, 20),
    _IpsecSaStatusStatus_Type()
)
ipsecSaStatusStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecSaStatusStatus.setStatus("current")

# Managed Objects groups


# Notification objects

failedLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 0, 8)
)
if mibBuilder.loadTexts:
    failedLogin.setStatus(
        "current"
    )

subCapacityReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 0, 9)
)
if mibBuilder.loadTexts:
    subCapacityReached.setStatus(
        "current"
    )

nseReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 0, 10)
)
if mibBuilder.loadTexts:
    nseReboot.setStatus(
        "current"
    )

nseRadCapacityReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 3309, 1, 3, 0, 15)
)
if mibBuilder.loadTexts:
    nseRadCapacityReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOMADIX-MIB",
    **{"DisplayString": DisplayString,
       "nomadix": nomadix,
       "products": products,
       "ag": ag,
       "ndxTraps": ndxTraps,
       "failedLogin": failedLogin,
       "subCapacityReached": subCapacityReached,
       "nseReboot": nseReboot,
       "nseRadCapacityReached": nseRadCapacityReached,
       "aaa": aaa,
       "aaaOn": aaaOn,
       "aaaXmlOn": aaaXmlOn,
       "aaaXmlSender1Ip": aaaXmlSender1Ip,
       "aaaPrintBillingCommandOn": aaaPrintBillingCommandOn,
       "aaaPassthroughPortOn": aaaPassthroughPortOn,
       "aaaPassthroughPortNumber": aaaPassthroughPortNumber,
       "aaaDot1xOn": aaaDot1xOn,
       "aaaOSencodingOn": aaaOSencodingOn,
       "aaaAuthMode": aaaAuthMode,
       "aaaInternalAuth": aaaInternalAuth,
       "aaaSslOn": aaaSslOn,
       "aaaSslHostName": aaaSslHostName,
       "aaaPortalPageOn": aaaPortalPageOn,
       "aaaPortalPageUrl": aaaPortalPageUrl,
       "aaaUsernameOn": aaaUsernameOn,
       "aaaNewSubscriberOn": aaaNewSubscriberOn,
       "aaaReloginOn": aaaReloginOn,
       "aaaCreditCardOn": aaaCreditCardOn,
       "aaaCreditCardUrl": aaaCreditCardUrl,
       "aaaCreditCardIp": aaaCreditCardIp,
       "aaaMerchantId": aaaMerchantId,
       "aaaSmartClientOn": aaaSmartClientOn,
       "aaaPortalParameterPassing": aaaPortalParameterPassing,
       "aaaPortalPostUrl": aaaPortalPostUrl,
       "aaaPortalXMLPort": aaaPortalXMLPort,
       "aaaSupportGISClients": aaaSupportGISClients,
       "aaaIWSLoginPageBlocking": aaaIWSLoginPageBlocking,
       "aaaCreditCardServerTypeSelection": aaaCreditCardServerTypeSelection,
       "aaaChainfusionCCTransTime": aaaChainfusionCCTransTime,
       "aaaExternalAuth": aaaExternalAuth,
       "aaaSecretKey": aaaSecretKey,
       "aaaExternalIPAddress": aaaExternalIPAddress,
       "aaaAuthorizationUrl": aaaAuthorizationUrl,
       "aaaLoggingOn": aaaLoggingOn,
       "aaaLogNumber": aaaLogNumber,
       "aaaLogServerIp": aaaLogServerIp,
       "aaaBillingOption": aaaBillingOption,
       "aaaBilloptIntroMsg": aaaBilloptIntroMsg,
       "aaaBilloptOfferMsg": aaaBilloptOfferMsg,
       "aaaBilloptPolicyMsg": aaaBilloptPolicyMsg,
       "aaaBilloptMinTimeUnitMinute": aaaBilloptMinTimeUnitMinute,
       "aaaBilloptMinTimeUnitHour": aaaBilloptMinTimeUnitHour,
       "aaaBilloptMinTimeUnitDay": aaaBilloptMinTimeUnitDay,
       "aaaBilloptMinTimeUnitWeek": aaaBilloptMinTimeUnitWeek,
       "aaaBilloptMinTimeUnitMonth": aaaBilloptMinTimeUnitMonth,
       "aaaBilloptMaxTimeUnitMinute": aaaBilloptMaxTimeUnitMinute,
       "aaaBilloptMaxTimeUnitHour": aaaBilloptMaxTimeUnitHour,
       "aaaBilloptMaxTimeUnitDay": aaaBilloptMaxTimeUnitDay,
       "aaaBilloptMaxTimeUnitWeek": aaaBilloptMaxTimeUnitWeek,
       "aaaBilloptMaxTimeUnitMonth": aaaBilloptMaxTimeUnitMonth,
       "aaaBilloptFreeAccessTime": aaaBilloptFreeAccessTime,
       "aaaBilloptMaxSubLifetime": aaaBilloptMaxSubLifetime,
       "aaaTaxRate": aaaTaxRate,
       "aaaBillingPlans": aaaBillingPlans,
       "aaaBillingPlan0": aaaBillingPlan0,
       "aaaBillingPlanOn0": aaaBillingPlanOn0,
       "aaaBillingPlanAssigned0": aaaBillingPlanAssigned0,
       "aaaBillingPlanXoverY0": aaaBillingPlanXoverY0,
       "aaaBillingPlanLabel0": aaaBillingPlanLabel0,
       "aaaBillingPlanDesc0": aaaBillingPlanDesc0,
       "aaaBillingPlanPricingMin0": aaaBillingPlanPricingMin0,
       "aaaBillingPlanPricingHour0": aaaBillingPlanPricingHour0,
       "aaaBillingPlanPricingDay0": aaaBillingPlanPricingDay0,
       "aaaBillingPlanPricingWeek0": aaaBillingPlanPricingWeek0,
       "aaaBillingPlanPricingMonth0": aaaBillingPlanPricingMonth0,
       "aaaBillingPlanBandwidthUp0": aaaBillingPlanBandwidthUp0,
       "aaaBillingPlanBandwidthDown0": aaaBillingPlanBandwidthDown0,
       "aaaBillingPlanDHCPPool0": aaaBillingPlanDHCPPool0,
       "aaaBillingPlanRateShow0": aaaBillingPlanRateShow0,
       "aaaBillingPlanCost0": aaaBillingPlanCost0,
       "aaaBillingPlanDuration0": aaaBillingPlanDuration0,
       "aaaBillingPlanValidity0": aaaBillingPlanValidity0,
       "aaaBillingPlanValidityRateShow0": aaaBillingPlanValidityRateShow0,
       "aaaBillingPlan1": aaaBillingPlan1,
       "aaaBillingPlanOn1": aaaBillingPlanOn1,
       "aaaBillingPlanAssigned1": aaaBillingPlanAssigned1,
       "aaaBillingPlanXoverY1": aaaBillingPlanXoverY1,
       "aaaBillingPlanLabel1": aaaBillingPlanLabel1,
       "aaaBillingPlanDesc1": aaaBillingPlanDesc1,
       "aaaBillingPlanPricingMin1": aaaBillingPlanPricingMin1,
       "aaaBillingPlanPricingHour1": aaaBillingPlanPricingHour1,
       "aaaBillingPlanPricingDay1": aaaBillingPlanPricingDay1,
       "aaaBillingPlanPricingWeek1": aaaBillingPlanPricingWeek1,
       "aaaBillingPlanPricingMonth1": aaaBillingPlanPricingMonth1,
       "aaaBillingPlanBandwidthUp1": aaaBillingPlanBandwidthUp1,
       "aaaBillingPlanBandwidthDown1": aaaBillingPlanBandwidthDown1,
       "aaaBillingPlanDHCPPool1": aaaBillingPlanDHCPPool1,
       "aaaBillingPlanRateShow1": aaaBillingPlanRateShow1,
       "aaaBillingPlanCost1": aaaBillingPlanCost1,
       "aaaBillingPlanDuration1": aaaBillingPlanDuration1,
       "aaaBillingPlanValidity1": aaaBillingPlanValidity1,
       "aaaBillingPlanValidityRateShow1": aaaBillingPlanValidityRateShow1,
       "aaaBillingPlan2": aaaBillingPlan2,
       "aaaBillingPlanOn2": aaaBillingPlanOn2,
       "aaaBillingPlanAssigned2": aaaBillingPlanAssigned2,
       "aaaBillingPlanXoverY2": aaaBillingPlanXoverY2,
       "aaaBillingPlanLabel2": aaaBillingPlanLabel2,
       "aaaBillingPlanDesc2": aaaBillingPlanDesc2,
       "aaaBillingPlanPricingMin2": aaaBillingPlanPricingMin2,
       "aaaBillingPlanPricingHour2": aaaBillingPlanPricingHour2,
       "aaaBillingPlanPricingDay2": aaaBillingPlanPricingDay2,
       "aaaBillingPlanPricingWeek2": aaaBillingPlanPricingWeek2,
       "aaaBillingPlanPricingMonth2": aaaBillingPlanPricingMonth2,
       "aaaBillingPlanBandwidthUp2": aaaBillingPlanBandwidthUp2,
       "aaaBillingPlanBandwidthDown2": aaaBillingPlanBandwidthDown2,
       "aaaBillingPlanDHCPPool2": aaaBillingPlanDHCPPool2,
       "aaaBillingPlanRateShow2": aaaBillingPlanRateShow2,
       "aaaBillingPlanCost2": aaaBillingPlanCost2,
       "aaaBillingPlanDuration2": aaaBillingPlanDuration2,
       "aaaBillingPlanValidity2": aaaBillingPlanValidity2,
       "aaaBillingPlanValidityRateShow2": aaaBillingPlanValidityRateShow2,
       "aaaBillingPlan3": aaaBillingPlan3,
       "aaaBillingPlanOn3": aaaBillingPlanOn3,
       "aaaBillingPlanAssigned3": aaaBillingPlanAssigned3,
       "aaaBillingPlanXoverY3": aaaBillingPlanXoverY3,
       "aaaBillingPlanLabel3": aaaBillingPlanLabel3,
       "aaaBillingPlanDesc3": aaaBillingPlanDesc3,
       "aaaBillingPlanPricingMin3": aaaBillingPlanPricingMin3,
       "aaaBillingPlanPricingHour3": aaaBillingPlanPricingHour3,
       "aaaBillingPlanPricingDay3": aaaBillingPlanPricingDay3,
       "aaaBillingPlanPricingWeek3": aaaBillingPlanPricingWeek3,
       "aaaBillingPlanPricingMonth3": aaaBillingPlanPricingMonth3,
       "aaaBillingPlanBandwidthUp3": aaaBillingPlanBandwidthUp3,
       "aaaBillingPlanBandwidthDown3": aaaBillingPlanBandwidthDown3,
       "aaaBillingPlanDHCPPool3": aaaBillingPlanDHCPPool3,
       "aaaBillingPlanRateShow3": aaaBillingPlanRateShow3,
       "aaaBillingPlanCost3": aaaBillingPlanCost3,
       "aaaBillingPlanDuration3": aaaBillingPlanDuration3,
       "aaaBillingPlanValidity3": aaaBillingPlanValidity3,
       "aaaBillingPlanValidityRateShow3": aaaBillingPlanValidityRateShow3,
       "aaaBillingPlan4": aaaBillingPlan4,
       "aaaBillingPlanOn4": aaaBillingPlanOn4,
       "aaaBillingPlanAssigned4": aaaBillingPlanAssigned4,
       "aaaBillingPlanXoverY4": aaaBillingPlanXoverY4,
       "aaaBillingPlanLabel4": aaaBillingPlanLabel4,
       "aaaBillingPlanDesc4": aaaBillingPlanDesc4,
       "aaaBillingPlanPricingMin4": aaaBillingPlanPricingMin4,
       "aaaBillingPlanPricingHour4": aaaBillingPlanPricingHour4,
       "aaaBillingPlanPricingDay4": aaaBillingPlanPricingDay4,
       "aaaBillingPlanPricingWeek4": aaaBillingPlanPricingWeek4,
       "aaaBillingPlanPricingMonth4": aaaBillingPlanPricingMonth4,
       "aaaBillingPlanBandwidthUp4": aaaBillingPlanBandwidthUp4,
       "aaaBillingPlanBandwidthDown4": aaaBillingPlanBandwidthDown4,
       "aaaBillingPlanDHCPPool4": aaaBillingPlanDHCPPool4,
       "aaaBillingPlanRateShow4": aaaBillingPlanRateShow4,
       "aaaBillingPlanCost4": aaaBillingPlanCost4,
       "aaaBillingPlanDuration4": aaaBillingPlanDuration4,
       "aaaBillingPlanValidity4": aaaBillingPlanValidity4,
       "aaaBillingPlanValidityRateShow4": aaaBillingPlanValidityRateShow4,
       "aaaBillingPlan5": aaaBillingPlan5,
       "aaaBillingPlanOn5": aaaBillingPlanOn5,
       "aaaBillingPlanAssigned5": aaaBillingPlanAssigned5,
       "aaaBillingPlanXoverY5": aaaBillingPlanXoverY5,
       "aaaBillingPlanLabel5": aaaBillingPlanLabel5,
       "aaaBillingPlanDesc5": aaaBillingPlanDesc5,
       "aaaBillingPlanPricingMin5": aaaBillingPlanPricingMin5,
       "aaaBillingPlanPricingHour5": aaaBillingPlanPricingHour5,
       "aaaBillingPlanPricingDay5": aaaBillingPlanPricingDay5,
       "aaaBillingPlanPricingWeek5": aaaBillingPlanPricingWeek5,
       "aaaBillingPlanPricingMonth5": aaaBillingPlanPricingMonth5,
       "aaaBillingPlanBandwidthUp5": aaaBillingPlanBandwidthUp5,
       "aaaBillingPlanBandwidthDown5": aaaBillingPlanBandwidthDown5,
       "aaaBillingPlanDHCPPool5": aaaBillingPlanDHCPPool5,
       "aaaBillingPlanRateShow5": aaaBillingPlanRateShow5,
       "aaaBillingPlanCost5": aaaBillingPlanCost5,
       "aaaBillingPlanDuration5": aaaBillingPlanDuration5,
       "aaaBillingPlanValidity5": aaaBillingPlanValidity5,
       "aaaBillingPlanValidityRateShow5": aaaBillingPlanValidityRateShow5,
       "aaaSubLoginUI": aaaSubLoginUI,
       "aaaWebServiceMsg": aaaWebServiceMsg,
       "aaaWebExistingUserMsg": aaaWebExistingUserMsg,
       "aaaWebNewUsernameMsg": aaaWebNewUsernameMsg,
       "aaaWebContactMsg": aaaWebContactMsg,
       "aaaWebMicrosUsernameMsg": aaaWebMicrosUsernameMsg,
       "aaaWebJavascriptOn": aaaWebJavascriptOn,
       "aaaWebRememberMeOn": aaaWebRememberMeOn,
       "aaaRememberMeMsg": aaaRememberMeMsg,
       "aaaRememberMeDays": aaaRememberMeDays,
       "aaaCurrency": aaaCurrency,
       "aaaAmountDecimals": aaaAmountDecimals,
       "aaaWebImage": aaaWebImage,
       "aaaWebPageBgcolor": aaaWebPageBgcolor,
       "aaaWebTabBgcolor": aaaWebTabBgcolor,
       "aaaWebTitleFont": aaaWebTitleFont,
       "aaaWebItemFont": aaaWebItemFont,
       "aaaErrorAccessBlocked": aaaErrorAccessBlocked,
       "aaaErrorAccessPassword": aaaErrorAccessPassword,
       "aaaErrorHasOccurred": aaaErrorHasOccurred,
       "aaaErrorISPChallenge": aaaErrorISPChallenge,
       "aaaErrorMinMaxValues": aaaErrorMinMaxValues,
       "aaaErrorNoBillingOpts": aaaErrorNoBillingOpts,
       "aaaErrorNotAvailable": aaaErrorNotAvailable,
       "aaaErrorPasswordMatch": aaaErrorPasswordMatch,
       "aaaErrorPasswordWrong": aaaErrorPasswordWrong,
       "aaaErrorRoomBilling": aaaErrorRoomBilling,
       "aaaErrorTooManyUsers": aaaErrorTooManyUsers,
       "aaaErrorTryAgain": aaaErrorTryAgain,
       "aaaErrorUserIdMissing": aaaErrorUserIdMissing,
       "aaaErrorUserIdTaken": aaaErrorUserIdTaken,
       "aaaErrorWeAreSorry": aaaErrorWeAreSorry,
       "aaaErrorWholeNumber": aaaErrorWholeNumber,
       "aaaErrorYourAccount": aaaErrorYourAccount,
       "aaaMessageBillingMode": aaaMessageBillingMode,
       "aaaMessagebyCreditCard": aaaMessagebyCreditCard,
       "aaaMessagebyHotelRoom": aaaMessagebyHotelRoom,
       "aaaMessageChooseUsername": aaaMessageChooseUsername,
       "aaaMessageChoosePasswd1": aaaMessageChoosePasswd1,
       "aaaMessageChoosePasswd2": aaaMessageChoosePasswd2,
       "aaaMessageFreeInternet": aaaMessageFreeInternet,
       "aaaMessageNewUserLogin": aaaMessageNewUserLogin,
       "aaaMessageOldUserLogin": aaaMessageOldUserLogin,
       "aaaMessagePurchaseOK1": aaaMessagePurchaseOK1,
       "aaaMessagePurchaseOK2": aaaMessagePurchaseOK2,
       "aaaMessagePurchaseSelect": aaaMessagePurchaseSelect,
       "aaaMessageRequestFailed": aaaMessageRequestFailed,
       "aaaMessageRequestGranted": aaaMessageRequestGranted,
       "aaaMessageThankYou": aaaMessageThankYou,
       "aaaMessageVerifying": aaaMessageVerifying,
       "aaaMessageYourHotel": aaaMessageYourHotel,
       "aaaMessageYourPurchase": aaaMessageYourPurchase,
       "aaaPartnerImageOn": aaaPartnerImageOn,
       "aaaPartnerImageFileName": aaaPartnerImageFileName,
       "aaaSubPostSession": aaaSubPostSession,
       "aaaSubGoodbyePage": aaaSubGoodbyePage,
       "aaaSubGPEnable": aaaSubGPEnable,
       "aaaSubGPIPAddressOn": aaaSubGPIPAddressOn,
       "aaaSubGPAuthenTypeOn": aaaSubGPAuthenTypeOn,
       "aaaSubGPStartTimeOn": aaaSubGPStartTimeOn,
       "aaaSubGPStopTimeOn": aaaSubGPStopTimeOn,
       "aaaSubGPByteSentOn": aaaSubGPByteSentOn,
       "aaaSubGPByteReceivedOn": aaaSubGPByteReceivedOn,
       "aaaSubGPHyperlinkOn": aaaSubGPHyperlinkOn,
       "aaaSubGPHyperlink": aaaSubGPHyperlink,
       "aaaSubGPSessionSummaryLabel": aaaSubGPSessionSummaryLabel,
       "aaaSubGPSubIPAddressLabel": aaaSubGPSubIPAddressLabel,
       "aaaSubGPAuthenTypeLabel": aaaSubGPAuthenTypeLabel,
       "aaaSubGPStartTimeLabel": aaaSubGPStartTimeLabel,
       "aaaSubGPStopTimeLabel": aaaSubGPStopTimeLabel,
       "aaaSubGPByteSentLabel": aaaSubGPByteSentLabel,
       "aaaSubGPByteReceivedLabel": aaaSubGPByteReceivedLabel,
       "aaaSubGPHypertextURLLabel": aaaSubGPHypertextURLLabel,
       "aaaSubscriber": aaaSubscriber,
       "aaaSubCurrTable": aaaSubCurrTable,
       "aaaSubCurrTableEntry": aaaSubCurrTableEntry,
       "subIndex": subIndex,
       "subMac": subMac,
       "subIp": subIp,
       "subPort": subPort,
       "subName": subName,
       "subBwUp": subBwUp,
       "subBwDown": subBwDown,
       "subAaaState": subAaaState,
       "subExpiration": subExpiration,
       "subIdleTimeout": subIdleTimeout,
       "subBytesSent": subBytesSent,
       "subBytesRec": subBytesRec,
       "subBytesTotal": subBytesTotal,
       "subProxy": subProxy,
       "subSsid": subSsid,
       "subStatus": subStatus,
       "aaaAuthSubTable": aaaAuthSubTable,
       "aaaAuthSubTableEntry": aaaAuthSubTableEntry,
       "authSubIndex": authSubIndex,
       "authSubType": authSubType,
       "authSubDhcpAddrType": authSubDhcpAddrType,
       "authSubDevicePort": authSubDevicePort,
       "authSubMac": authSubMac,
       "authSubIp": authSubIp,
       "authSubName": authSubName,
       "authSubPassword": authSubPassword,
       "authSubCountDown": authSubCountDown,
       "authSubExpTimeHrs": authSubExpTimeHrs,
       "authSubExpTimeMins": authSubExpTimeMins,
       "authSubAmtPaid": authSubAmtPaid,
       "authSubAmtLeft": authSubAmtLeft,
       "authSubUser1": authSubUser1,
       "authSubUser2": authSubUser2,
       "authSubBwUp": authSubBwUp,
       "authSubBwDown": authSubBwDown,
       "authSubConfirmation": authSubConfirmation,
       "authSubStatus": authSubStatus,
       "radHistSysloggingOn": radHistSysloggingOn,
       "radHistSyslogNumber": radHistSyslogNumber,
       "radHistSyslogServerIp": radHistSyslogServerIp,
       "radProxyAcctHistLog": radProxyAcctHistLog,
       "radProxyAcctHistSyslog": radProxyAcctHistSyslog,
       "radHistSyslogFilter": radHistSyslogFilter,
       "radHistSyslogSaveToFile": radHistSyslogSaveToFile,
       "aaaRadius": aaaRadius,
       "aaaRadiusRoutingMode": aaaRadiusRoutingMode,
       "aaaRadiusDefProf": aaaRadiusDefProf,
       "aaaRadiusCacheOn": aaaRadiusCacheOn,
       "aaaRadiusDefaultIdle": aaaRadiusDefaultIdle,
       "aaaRadiusNasIdOn": aaaRadiusNasIdOn,
       "aaaRadiusNasId": aaaRadiusNasId,
       "aaaRadiusNasIpOn": aaaRadiusNasIpOn,
       "aaaRadiusNasPortOn": aaaRadiusNasPortOn,
       "aaaRadiusNasPortType": aaaRadiusNasPortType,
       "aaaRadiusFipOn": aaaRadiusFipOn,
       "aaaRadiusRedUrlOn": aaaRadiusRedUrlOn,
       "aaaRadiusGoodbyeUrlOn": aaaRadiusGoodbyeUrlOn,
       "aaaRadiusForgotPasswordUrlOn": aaaRadiusForgotPasswordUrlOn,
       "aaaRadiusForgotPasswordUrl": aaaRadiusForgotPasswordUrl,
       "aaaRadiusSubnetAttrOn": aaaRadiusSubnetAttrOn,
       "aaaRadiusNetVlanOn": aaaRadiusNetVlanOn,
       "aaaRadiusNetVlanDefaultOn": aaaRadiusNetVlanDefaultOn,
       "aaaRadiusNetVlanDefaultTag": aaaRadiusNetVlanDefaultTag,
       "aaaRadiusLocalAuthPort": aaaRadiusLocalAuthPort,
       "aaaRadiusLocalAcctPort": aaaRadiusLocalAcctPort,
       "aaaRadiusLoginRefresh": aaaRadiusLoginRefresh,
       "aaaRadiusTerminationActionOn": aaaRadiusTerminationActionOn,
       "aaaLogFilter": aaaLogFilter,
       "aaaSaveToFile": aaaSaveToFile,
       "aaaXmlSender2Ip": aaaXmlSender2Ip,
       "aaaMessageNewUserTermsOn": aaaMessageNewUserTermsOn,
       "aaaMessageNewUserTerms": aaaMessageNewUserTerms,
       "aaaLoginPageFailover": aaaLoginPageFailover,
       "aaaLoginPageFailoverOn": aaaLoginPageFailoverOn,
       "aaaLpfStatusTable": aaaLpfStatusTable,
       "aaaLpfStatusTableEntry": aaaLpfStatusTableEntry,
       "lpfEntryIndex": lpfEntryIndex,
       "lpfEntryNickname": lpfEntryNickname,
       "lpfEntryOnlineStatus": lpfEntryOnlineStatus,
       "accessControl": accessControl,
       "blockTelnetAccessOn": blockTelnetAccessOn,
       "blockWebAccessOn": blockWebAccessOn,
       "blockFtpAccessOn": blockFtpAccessOn,
       "accessControlOn": accessControlOn,
       "accessControlIpTable": accessControlIpTable,
       "accessControlIpEntry": accessControlIpEntry,
       "acIndex": acIndex,
       "acStartAddress": acStartAddress,
       "acEndAddress": acEndAddress,
       "acStatus": acStatus,
       "blockSFTPAccessOn": blockSFTPAccessOn,
       "blockSSHShellAccessOn": blockSSHShellAccessOn,
       "bandwidthManagement": bandwidthManagement,
       "bandwidthManagementOn": bandwidthManagementOn,
       "bwmUpWanLinkSpeed": bwmUpWanLinkSpeed,
       "bwmDownWanLinkSpeed": bwmDownWanLinkSpeed,
       "billRecMirror": billRecMirror,
       "brmMirrorOn": brmMirrorOn,
       "brmPropertyId": brmPropertyId,
       "brmNseId": brmNseId,
       "brmServerIpPrimary": brmServerIpPrimary,
       "brmServerUrlPrimary": brmServerUrlPrimary,
       "brmServerSecretPrimary": brmServerSecretPrimary,
       "brmServerPortPrimary": brmServerPortPrimary,
       "brmServerIpSecondary": brmServerIpSecondary,
       "brmServerUrlSecondary": brmServerUrlSecondary,
       "brmServerSecretSecondary": brmServerSecretSecondary,
       "brmServerPortSecondary": brmServerPortSecondary,
       "brmServerCCIpOne": brmServerCCIpOne,
       "brmServerCCUrlOne": brmServerCCUrlOne,
       "brmServerCCSecretOne": brmServerCCSecretOne,
       "brmServerCCPortOne": brmServerCCPortOne,
       "brmServerCCIpTwo": brmServerCCIpTwo,
       "brmServerCCUrlTwo": brmServerCCUrlTwo,
       "brmServerCCSecretTwo": brmServerCCSecretTwo,
       "brmServerCCPortTwo": brmServerCCPortTwo,
       "brmServerCCIpThree": brmServerCCIpThree,
       "brmServerCCUrlThree": brmServerCCUrlThree,
       "brmServerCCSecretThree": brmServerCCSecretThree,
       "brmServerCCPortThree": brmServerCCPortThree,
       "brmRetransMethod": brmRetransMethod,
       "brmRetransAttempts": brmRetransAttempts,
       "brmRetransDelay": brmRetransDelay,
       "dat": dat,
       "datSessionTable": datSessionTable,
       "datSessionTableEntry": datSessionTableEntry,
       "datSubIp": datSubIp,
       "datSubPort": datSubPort,
       "datSubMac": datSubMac,
       "datNetIp": datNetIp,
       "datNetPort": datNetPort,
       "datDestIp": datDestIp,
       "datDestPort": datDestPort,
       "datProto": datProto,
       "datSessState": datSessState,
       "datTimeout": datTimeout,
       "dhcp": dhcp,
       "dhcpDisable": dhcpDisable,
       "dhcpIpUpsell": dhcpIpUpsell,
       "dhcpServer": dhcpServer,
       "dhcpServerEnable": dhcpServerEnable,
       "dhcpServerSubnetBased": dhcpServerSubnetBased,
       "dhcpServerTable": dhcpServerTable,
       "dhcpPoolTableEntry": dhcpPoolTableEntry,
       "poolIndex": poolIndex,
       "serverIp": serverIp,
       "netMask": netMask,
       "poolStartIp": poolStartIp,
       "poolStopIp": poolStopIp,
       "leaseMinutes": leaseMinutes,
       "publicPool": publicPool,
       "ipUpSell": ipUpSell,
       "defaultPool": defaultPool,
       "poolStatus": poolStatus,
       "dhcpLeaseTable": dhcpLeaseTable,
       "dhcpLeaseTableEntry": dhcpLeaseTableEntry,
       "leaseIndex": leaseIndex,
       "leaseAddress": leaseAddress,
       "leaseCLID": leaseCLID,
       "leaseStatus": leaseStatus,
       "dhcpRelay": dhcpRelay,
       "dhcpRelayEnable": dhcpRelayEnable,
       "dhcpRelayAgentIP": dhcpRelayAgentIP,
       "dhcpRelayServerIP": dhcpRelayServerIP,
       "dns": dns,
       "dnsHostName": dnsHostName,
       "dnsDomain": dnsDomain,
       "dnsPrimaryServer": dnsPrimaryServer,
       "dnsSecondaryServer": dnsSecondaryServer,
       "dnsTertiaryServer": dnsTertiaryServer,
       "greTunneling": greTunneling,
       "greTunnelingEnable": greTunnelingEnable,
       "greVpnConcentratorIp": greVpnConcentratorIp,
       "greInterfaceIp": greInterfaceIp,
       "greInterfaceNetmask": greInterfaceNetmask,
       "greInterfaceGateway": greInterfaceGateway,
       "hpr": hpr,
       "hprOn": hprOn,
       "hprUrl": hprUrl,
       "hprParameterPassing": hprParameterPassing,
       "hprRedirectionFrequency": hprRedirectionFrequency,
       "icc": icc,
       "iccOn": iccOn,
       "iccTitle": iccTitle,
       "iccLogoutOption": iccLogoutOption,
       "iccLanguageOption": iccLanguageOption,
       "iccTimerOption": iccTimerOption,
       "iccCharSetOption": iccCharSetOption,
       "iccButtons": iccButtons,
       "iccISPLogoButton": iccISPLogoButton,
       "iccISPLogoButtonName": iccISPLogoButtonName,
       "iccISPLogoButtonURL": iccISPLogoButtonURL,
       "iccISPLogoButtonImgName": iccISPLogoButtonImgName,
       "iccButton2": iccButton2,
       "iccButtonName2": iccButtonName2,
       "iccButtonURL2": iccButtonURL2,
       "iccButtonImgName2": iccButtonImgName2,
       "iccButton3": iccButton3,
       "iccButtonName3": iccButtonName3,
       "iccButtonURL3": iccButtonURL3,
       "iccButtonImgName3": iccButtonImgName3,
       "iccButton4": iccButton4,
       "iccButtonName4": iccButtonName4,
       "iccButtonURL4": iccButtonURL4,
       "iccButtonImgName4": iccButtonImgName4,
       "iccButton5": iccButton5,
       "iccButtonName5": iccButtonName5,
       "iccButtonURL5": iccButtonURL5,
       "iccButtonImgName5": iccButtonImgName5,
       "iccButton6": iccButton6,
       "iccButtonName6": iccButtonName6,
       "iccButtonURL6": iccButtonURL6,
       "iccButtonImgName6": iccButtonImgName6,
       "iccButton7": iccButton7,
       "iccButtonName7": iccButtonName7,
       "iccButtonURL7": iccButtonURL7,
       "iccButtonImgName7": iccButtonImgName7,
       "iccButton8": iccButton8,
       "iccButtonName8": iccButtonName8,
       "iccButtonURL8": iccButtonURL8,
       "iccButtonImgName8": iccButtonImgName8,
       "iccButton9": iccButton9,
       "iccButtonName9": iccButtonName9,
       "iccButtonURL9": iccButtonURL9,
       "iccButtonImgName9": iccButtonImgName9,
       "iccBanners": iccBanners,
       "iccBanner1": iccBanner1,
       "iccBannerName1": iccBannerName1,
       "iccBannerURL1": iccBannerURL1,
       "iccBannerImgName1": iccBannerImgName1,
       "iccBannerDuration1": iccBannerDuration1,
       "iccBannerStartTime1": iccBannerStartTime1,
       "iccBannerStopTime1": iccBannerStopTime1,
       "iccBanner2": iccBanner2,
       "iccBannerName2": iccBannerName2,
       "iccBannerURL2": iccBannerURL2,
       "iccBannerImgName2": iccBannerImgName2,
       "iccBannerDuration2": iccBannerDuration2,
       "iccBannerStartTime2": iccBannerStartTime2,
       "iccBannerStopTime2": iccBannerStopTime2,
       "iccBanner3": iccBanner3,
       "iccBannerName3": iccBannerName3,
       "iccBannerURL3": iccBannerURL3,
       "iccBannerImgName3": iccBannerImgName3,
       "iccBannerDuration3": iccBannerDuration3,
       "iccBannerStartTime3": iccBannerStartTime3,
       "iccBannerStopTime3": iccBannerStopTime3,
       "iccBanner4": iccBanner4,
       "iccBannerName4": iccBannerName4,
       "iccBannerURL4": iccBannerURL4,
       "iccBannerImgName4": iccBannerImgName4,
       "iccBannerDuration4": iccBannerDuration4,
       "iccBannerStartTime4": iccBannerStartTime4,
       "iccBannerStopTime4": iccBannerStopTime4,
       "iccBanner5": iccBanner5,
       "iccBannerName5": iccBannerName5,
       "iccBannerURL5": iccBannerURL5,
       "iccBannerImgName5": iccBannerImgName5,
       "iccBannerDuration5": iccBannerDuration5,
       "iccBannerStartTime5": iccBannerStartTime5,
       "iccBannerStopTime5": iccBannerStopTime5,
       "inat": inat,
       "inatOn": inatOn,
       "pptpOn": pptpOn,
       "ipsecOn": ipsecOn,
       "pptpidOn": pptpidOn,
       "inatIpTable": inatIpTable,
       "inatIpEntry": inatIpEntry,
       "inatIndex": inatIndex,
       "inatStartAddress": inatStartAddress,
       "inatEndAddress": inatEndAddress,
       "inatEntryStatus": inatEntryStatus,
       "licenseKeys": licenseKeys,
       "lkKey": lkKey,
       "lkModelNo": lkModelNo,
       "lkMaxNumSubs": lkMaxNumSubs,
       "lkFeatureList": lkFeatureList,
       "lkFeatureListEntry": lkFeatureListEntry,
       "lkFeatureIndex": lkFeatureIndex,
       "lkFeatureName": lkFeatureName,
       "lkFeatureStatus": lkFeatureStatus,
       "location": location,
       "locationCompanyName": locationCompanyName,
       "locationSiteName": locationSiteName,
       "locationAddress1": locationAddress1,
       "locationAddress2": locationAddress2,
       "locationCity": locationCity,
       "locationState": locationState,
       "locationZip": locationZip,
       "locationCountry": locationCountry,
       "locationEmail": locationEmail,
       "locationVenueType": locationVenueType,
       "locationNetworkIp": locationNetworkIp,
       "locationNetmask": locationNetmask,
       "locationGateway": locationGateway,
       "locationNetIntfCfgMode": locationNetIntfCfgMode,
       "locationIsoCountryCode": locationIsoCountryCode,
       "locationPhoneCountryCode": locationPhoneCountryCode,
       "locationCallingAreaCode": locationCallingAreaCode,
       "locationNetworkSsidZone": locationNetworkSsidZone,
       "passthrough": passthrough,
       "passthroughOn": passthroughOn,
       "passthroughIPTable": passthroughIPTable,
       "passthroughIPEntry": passthroughIPEntry,
       "passthroughAddIndex": passthroughAddIndex,
       "passthroughaddress": passthroughaddress,
       "statusIP": statusIP,
       "passthroughDNSTable": passthroughDNSTable,
       "passthroughDNSEntry": passthroughDNSEntry,
       "passthroughNameIndex": passthroughNameIndex,
       "passthroughname": passthroughname,
       "statusDNS": statusDNS,
       "portLoc": portLoc,
       "portLocInRoomPortMappingOn": portLocInRoomPortMappingOn,
       "portLocInRoomPortMappingUsername": portLocInRoomPortMappingUsername,
       "portLocInRoomPortMappingPassword": portLocInRoomPortMappingPassword,
       "portLocConcentratorType": portLocConcentratorType,
       "portLocConcentratorTable": portLocConcentratorTable,
       "portLocConcentratorTableEntry": portLocConcentratorTableEntry,
       "portLocConcIndex": portLocConcIndex,
       "portLocAddress": portLocAddress,
       "portLocCommunity": portLocCommunity,
       "portLocUplinkPort": portLocUplinkPort,
       "portLocTable": portLocTable,
       "portLocTableEntry": portLocTableEntry,
       "portLocIndex": portLocIndex,
       "portLocLocation": portLocLocation,
       "portLocPort": portLocPort,
       "portLocModemMAC": portLocModemMAC,
       "portLocDescription": portLocDescription,
       "portLocState": portLocState,
       "smtp": smtp,
       "smtpRedirect": smtpRedirect,
       "smtpServerIP": smtpServerIP,
       "smtpPcRedirect": smtpPcRedirect,
       "smtpUsername": smtpUsername,
       "smtpPassword": smtpPassword,
       "smtpServerDNS": smtpServerDNS,
       "snmpagent": snmpagent,
       "snmpdOn": snmpdOn,
       "systemContact": systemContact,
       "systemLocation": systemLocation,
       "getCommunity": getCommunity,
       "setCommunity": setCommunity,
       "trapCommunity": trapCommunity,
       "trapIP": trapIP,
       "subsettings": subsettings,
       "subIdleLogoutTimeout": subIdleLogoutTimeout,
       "subToSubCommBlock": subToSubCommBlock,
       "subnets": subnets,
       "subnetTable": subnetTable,
       "subnetTableEntry": subnetTableEntry,
       "subnetIndex": subnetIndex,
       "subnet": subnet,
       "mask": mask,
       "subnetStatus": subnetStatus,
       "system": system,
       "systemLoggingOn": systemLoggingOn,
       "systemLogNumber": systemLogNumber,
       "systemLogFilter": systemLogFilter,
       "systemLogServerIp": systemLogServerIp,
       "systemSaveToFile": systemSaveToFile,
       "systemReportLoggingOn": systemReportLoggingOn,
       "systemReportLogNumber": systemReportLogNumber,
       "systemReportLogServerIp": systemReportLogServerIp,
       "systemReportLogInterval": systemReportLogInterval,
       "systemVersion": systemVersion,
       "systemNseId": systemNseId,
       "systemReboot": systemReboot,
       "systemBridgeMode": systemBridgeMode,
       "systemConfigFile": systemConfigFile,
       "systemConfigFileStatus": systemConfigFileStatus,
       "systemAdminConcurrencyOn": systemAdminConcurrencyOn,
       "systemUptime": systemUptime,
       "systemHistoryTable": systemHistoryTable,
       "systemHistoryTableEntry": systemHistoryTableEntry,
       "systemHistoryIndex": systemHistoryIndex,
       "systemHistoryTimestamp": systemHistoryTimestamp,
       "systemHistoryLogin": systemHistoryLogin,
       "systemHistoryAddress": systemHistoryAddress,
       "systemHistoryMessage": systemHistoryMessage,
       "systemSyslogTable": systemSyslogTable,
       "systemSyslogTableEntry": systemSyslogTableEntry,
       "systemSyslogIndex": systemSyslogIndex,
       "systemSyslogTimestamp": systemSyslogTimestamp,
       "systemSyslogVersion": systemSyslogVersion,
       "systemSyslogAddress": systemSyslogAddress,
       "systemSyslogMessage": systemSyslogMessage,
       "systemStaticPortMappingTable": systemStaticPortMappingTable,
       "systemStaticPortMappingTableEntry": systemStaticPortMappingTableEntry,
       "systemStaticPortMappingIndex": systemStaticPortMappingIndex,
       "systemStaticPortMappingMAC": systemStaticPortMappingMAC,
       "systemStaticPortMappingInternalIP": systemStaticPortMappingInternalIP,
       "systemStaticPortMappingInternalPort": systemStaticPortMappingInternalPort,
       "systemStaticPortMappingExternalIP": systemStaticPortMappingExternalIP,
       "systemStaticPortMappingExternalPort": systemStaticPortMappingExternalPort,
       "systemStaticPortMappingRemoteIP": systemStaticPortMappingRemoteIP,
       "systemStaticPortMappingRemotePort": systemStaticPortMappingRemotePort,
       "systemStaticPortMappingProto": systemStaticPortMappingProto,
       "systemStaticPortMappingStatus": systemStaticPortMappingStatus,
       "blockIcmpFromPending": blockIcmpFromPending,
       "time": time,
       "timeCurrentDateAndTime": timeCurrentDateAndTime,
       "timeOffsetSign": timeOffsetSign,
       "timeOffsetHours": timeOffsetHours,
       "timeOffsetMinutes": timeOffsetMinutes,
       "timeServerTimeout": timeServerTimeout,
       "timeServer1": timeServer1,
       "timeServer2": timeServer2,
       "timeServer3": timeServer3,
       "timeServer4": timeServer4,
       "urlFiltering": urlFiltering,
       "urlFilteringOn": urlFilteringOn,
       "urlFilteringIPTable": urlFilteringIPTable,
       "urlFilteringIPTableEntry": urlFilteringIPTableEntry,
       "urlFilteringIPTableIndex": urlFilteringIPTableIndex,
       "urlFilteringIPTableAddress": urlFilteringIPTableAddress,
       "urlFilteringIPTableStatus": urlFilteringIPTableStatus,
       "urlFilteringDNSTable": urlFilteringDNSTable,
       "urlFilteringDNSTableEntry": urlFilteringDNSTableEntry,
       "urlFilteringDNSTableIndex": urlFilteringDNSTableIndex,
       "urlFilteringDNSTableName": urlFilteringDNSTableName,
       "urlFilteringDNSTableStatus": urlFilteringDNSTableStatus,
       "radiusProxy": radiusProxy,
       "radProxyServices": radProxyServices,
       "radProxyAuthSvrPort": radProxyAuthSvrPort,
       "radProxyAcctSvrPort": radProxyAcctSvrPort,
       "radProxyUpstreamNas": radProxyUpstreamNas,
       "radProxyUpstreamNasTable": radProxyUpstreamNasTable,
       "radProxyUpstreamNasTableEntry": radProxyUpstreamNasTableEntry,
       "nasIndex": nasIndex,
       "nasEntryActive": nasEntryActive,
       "nasIpAddress": nasIpAddress,
       "nasAuthSec": nasAuthSec,
       "nasAcctSec": nasAcctSec,
       "nasDefProf": nasDefProf,
       "nasStatus": nasStatus,
       "radProxyLocalServcomPort": radProxyLocalServcomPort,
       "realmBasedRouter": realmBasedRouter,
       "rBserviceProfiles": rBserviceProfiles,
       "serviceProfileTable": serviceProfileTable,
       "serviceProfileTableEntry": serviceProfileTableEntry,
       "profIndex": profIndex,
       "profName": profName,
       "radAuthOn": radAuthOn,
       "radAuthProto": radAuthProto,
       "radAuthSrv1Ip": radAuthSrv1Ip,
       "radAuthSrv1Port": radAuthSrv1Port,
       "radAuthSrv1Sec": radAuthSrv1Sec,
       "radAuthSrv2Ip": radAuthSrv2Ip,
       "radAuthSrv2Port": radAuthSrv2Port,
       "radAuthSrv2Sec": radAuthSrv2Sec,
       "radAcctOn": radAcctOn,
       "radAcctSrv1Ip": radAcctSrv1Ip,
       "radAcctSrv1Port": radAcctSrv1Port,
       "radAcctSrv1Sec": radAcctSrv1Sec,
       "radAcctSrv2Ip": radAcctSrv2Ip,
       "radAcctSrv2Port": radAcctSrv2Port,
       "radAcctSrv2Sec": radAcctSrv2Sec,
       "radRetrMethod": radRetrMethod,
       "radRetrFreq": radRetrFreq,
       "radRetrAttempts": radRetrAttempts,
       "profStatus": profStatus,
       "rBroutes": rBroutes,
       "realmBasedRoutingTable": realmBasedRoutingTable,
       "realmBasedRoutingTableEntry": realmBasedRoutingTableEntry,
       "realmIndex": realmIndex,
       "realmEntryActive": realmEntryActive,
       "realmWildcard": realmWildcard,
       "realmName": realmName,
       "realmMatchType": realmMatchType,
       "realmProfile": realmProfile,
       "realmStrip": realmStrip,
       "realmStatus": realmStatus,
       "realmTunProfile": realmTunProfile,
       "realmTunStrip": realmTunStrip,
       "realmTunLocHostName": realmTunLocHostName,
       "rBtunnelProfiles": rBtunnelProfiles,
       "tunnelProfileTable": tunnelProfileTable,
       "tunnelProfileTableEntry": tunnelProfileTableEntry,
       "tunProfIndex": tunProfIndex,
       "tunProfName": tunProfName,
       "tunPassword": tunPassword,
       "tunPeerIp": tunPeerIp,
       "tunProfStatus": tunProfStatus,
       "sessionlimit": sessionlimit,
       "sessionLimitEnable": sessionLimitEnable,
       "sessionLimitMeanRate": sessionLimitMeanRate,
       "sessionLimitBurstSize": sessionLimitBurstSize,
       "sessionLimitTimeInterval": sessionLimitTimeInterval,
       "sessionLimitFilterOffendersEnable": sessionLimitFilterOffendersEnable,
       "macFiltering": macFiltering,
       "macFilteringOn": macFilteringOn,
       "macFilteringTable": macFilteringTable,
       "macFilteringTableEntry": macFilteringTableEntry,
       "macFilteringTableIndex": macFilteringTableIndex,
       "macFilteringTableAddress": macFilteringTableAddress,
       "macFilteringStatus": macFilteringStatus,
       "tunneling": tunneling,
       "tunnelingOn": tunnelingOn,
       "wireless": wireless,
       "wirelessSsid": wirelessSsid,
       "wirelessSsidBroadcastOn": wirelessSsidBroadcastOn,
       "wirelessChannel": wirelessChannel,
       "wirelessRate": wirelessRate,
       "wirelessPower": wirelessPower,
       "wirelessFragLength": wirelessFragLength,
       "wirelessRtsLength": wirelessRtsLength,
       "wirelessBeaconInterval": wirelessBeaconInterval,
       "wirelessDtim": wirelessDtim,
       "wirelessShortPreambleOn": wirelessShortPreambleOn,
       "wirelessMssid": wirelessMssid,
       "wirelessMssidVlanOn": wirelessMssidVlanOn,
       "wirelessMssidVlanDefaultOn": wirelessMssidVlanDefaultOn,
       "wirelessMssidVlanDefaultTag": wirelessMssidVlanDefaultTag,
       "wirelessMssidTable": wirelessMssidTable,
       "wirelessMssidTableEntry": wirelessMssidTableEntry,
       "mssidIndex": mssidIndex,
       "mssidName": mssidName,
       "mssidVlan": mssidVlan,
       "mssidStatus": mssidStatus,
       "wirelessWep": wirelessWep,
       "wirelessWepOn": wirelessWepOn,
       "wirelessWepClients": wirelessWepClients,
       "wirelessWepAuthType": wirelessWepAuthType,
       "wirelessWepNon1xAllowedOn": wirelessWepNon1xAllowedOn,
       "wirelessWepKeyType": wirelessWepKeyType,
       "wirelessWepDefaultKey": wirelessWepDefaultKey,
       "wirelessWepKey1": wirelessWepKey1,
       "wirelessWepKey2": wirelessWepKey2,
       "wirelessWepKey3": wirelessWepKey3,
       "wirelessWepKey4": wirelessWepKey4,
       "pppoeClient": pppoeClient,
       "pppoeSvcName": pppoeSvcName,
       "pppEchoReqIntvl": pppEchoReqIntvl,
       "pppEchoMaxNonresp": pppEchoMaxNonresp,
       "pppAuthUsername": pppAuthUsername,
       "pppAuthPassword": pppAuthPassword,
       "pppIpCfgMode": pppIpCfgMode,
       "pppStaticIpAddr": pppStaticIpAddr,
       "pppMaxTcpMss": pppMaxTcpMss,
       "dyndns": dyndns,
       "dynDnsEnable": dynDnsEnable,
       "dynDnsProtocol": dynDnsProtocol,
       "dynDnsServer": dynDnsServer,
       "dynDnsPort": dynDnsPort,
       "dynDnsHostname": dynDnsHostname,
       "dynDnsUsername": dynDnsUsername,
       "dynDnsPassword": dynDnsPassword,
       "dynDnsForceUpdate": dynDnsForceUpdate,
       "localWeb": localWeb,
       "localWebPages": localWebPages,
       "localWebPagesTable": localWebPagesTable,
       "localWebPagesTableEntry": localWebPagesTableEntry,
       "localWebPagesTableIndex": localWebPagesTableIndex,
       "localWebPagesTableName": localWebPagesTableName,
       "localWebPagesTableStatus": localWebPagesTableStatus,
       "localWebImages": localWebImages,
       "localWebImagesTable": localWebImagesTable,
       "localWebImagesTableEntry": localWebImagesTableEntry,
       "localWebImagesTableIndex": localWebImagesTableIndex,
       "localWebImagesTableName": localWebImagesTableName,
       "localWebImagesTableStatus": localWebImagesTableStatus,
       "ipsec": ipsec,
       "ipsecVpnOn": ipsecVpnOn,
       "ipsecPeers": ipsecPeers,
       "ipsecPeerTable": ipsecPeerTable,
       "ipsecPeerTableEntry": ipsecPeerTableEntry,
       "ipsecPeerIndex": ipsecPeerIndex,
       "ipsecPeerIpAddr": ipsecPeerIpAddr,
       "ipsecPeerAuthMethod": ipsecPeerAuthMethod,
       "ipsecPeerSharedKey": ipsecPeerSharedKey,
       "ipsecPeerPrivkeyFile": ipsecPeerPrivkeyFile,
       "ipsecPeerCertFile": ipsecPeerCertFile,
       "ipsecPeerEncDesOk": ipsecPeerEncDesOk,
       "ipsecPeerEnc3DesOk": ipsecPeerEnc3DesOk,
       "ipsecPeerHashMd5Ok": ipsecPeerHashMd5Ok,
       "ipsecPeerHashShaOk": ipsecPeerHashShaOk,
       "ipsecPeerKeyStrength": ipsecPeerKeyStrength,
       "ipsecPeerLifetime": ipsecPeerLifetime,
       "ipsecPeerStatus": ipsecPeerStatus,
       "ipsecPolicies": ipsecPolicies,
       "ipsecPolicyTable": ipsecPolicyTable,
       "ipsecPolicyTableEntry": ipsecPolicyTableEntry,
       "ipsecPolicyIndex": ipsecPolicyIndex,
       "ipsecPolicyPeerIp": ipsecPolicyPeerIp,
       "ipsecPolicyProtocol": ipsecPolicyProtocol,
       "ipsecPolicyRemIp": ipsecPolicyRemIp,
       "ipsecPolicyRemSubnet": ipsecPolicyRemSubnet,
       "ipsecPolicyRemPort": ipsecPolicyRemPort,
       "ipsecPolicyUseNetIp": ipsecPolicyUseNetIp,
       "ipsecPolicyLocIp": ipsecPolicyLocIp,
       "ipsecPolicyLocSubnet": ipsecPolicyLocSubnet,
       "ipsecPolicyLocPort": ipsecPolicyLocPort,
       "ipsecPolicyType": ipsecPolicyType,
       "ipsecPolicyDirType": ipsecPolicyDirType,
       "ipsecPolicyEncDesOk": ipsecPolicyEncDesOk,
       "ipsecPolicyEnc3desOk": ipsecPolicyEnc3desOk,
       "ipsecPolicyEncNullOk": ipsecPolicyEncNullOk,
       "ipsecPolicyAuthMd5Ok": ipsecPolicyAuthMd5Ok,
       "ipsecPolicyAuthShaOk": ipsecPolicyAuthShaOk,
       "ipsecPolicyAuthNullOk": ipsecPolicyAuthNullOk,
       "ipsecPolicyPfsStrength": ipsecPolicyPfsStrength,
       "ipsecPolicyMaxLifetime": ipsecPolicyMaxLifetime,
       "ipsecPolicyMaxLifesize": ipsecPolicyMaxLifesize,
       "ipsecPolicyAutoRenew": ipsecPolicyAutoRenew,
       "ipsecPolicyStatus": ipsecPolicyStatus,
       "ipsecSaStatus": ipsecSaStatus,
       "ipsecSaStatusTable": ipsecSaStatusTable,
       "ipsecSaStatusTableEntry": ipsecSaStatusTableEntry,
       "ipsecSaStatusIndex": ipsecSaStatusIndex,
       "ipsecSaStatusState": ipsecSaStatusState,
       "ipsecSaStatusStatus": ipsecSaStatusStatus}
)
