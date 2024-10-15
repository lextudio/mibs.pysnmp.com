# SNMP MIB module (CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:18 2024
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

ciscoLwappDot11ClientCCXTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 611)
)
ciscoLwappDot11ClientCCXTextualConventions.setRevisions(
        ("2007-03-22 00:00",
         "2007-02-22 00:00",
         "2007-02-19 00:00",
         "2007-01-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoLwappDot11ClientReqStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("failure", 4),
          ("inProgress", 2),
          ("initiate", 1),
          ("requestNotProcessedByClient", 5),
          ("success", 3))
    )



class CiscoLwappDot11ClientSSId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class CiscoLwappDot11ClientAuthMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("eap", 2),
          ("none", 0),
          ("preSharedKey", 1),
          ("unknown", 255))
    )



class CiscoLwappDot11ClientEAPMethod(Integer32, TextualConvention):
    status = "current"
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("eapFast", 1),
          ("eapMd5", 6),
          ("eapSim", 7),
          ("eapTls", 2),
          ("eapTtls", 3),
          ("leap", 0),
          ("peap0EapMschap2", 4),
          ("peap1EapGtc", 5),
          ("preSharedKey", 8),
          ("unknown", 255))
    )



class CiscoLwappDot11ClientKeyMgmtMethod(Integer32, TextualConvention):
    status = "current"
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("cckm", 7),
          ("dynamicWep", 2),
          ("none", 0),
          ("staticWep", 1),
          ("unknown", 255),
          ("wpa", 3),
          ("wpa2", 5),
          ("wpa2Cckm", 6),
          ("wpaCckm", 4))
    )



class CiscoLwappDot11ClientEncryptionMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aesCcmp", 5),
          ("ckip", 4),
          ("none", 0),
          ("tkip", 3),
          ("unknown", 255),
          ("wep104", 2),
          ("wep40", 1))
    )



class CiscoLwappDot11ClientCredentialType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hostOsLogin", 2),
          ("localSaved", 0),
          ("manuallyPrompted", 1),
          ("unknown", 255))
    )



class CiscoLwappDot11ClientPowerSaveMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("awake", 0),
          ("maxPower", 2),
          ("normal", 1),
          ("sApsd", 4),
          ("uApsd", 3),
          ("unknown", 255))
    )



class CiscoLwappDot11ClientTxPowerMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("fixed", 0))
    )



class CiscoLwappDot11ClientRadioType(Integer32, TextualConvention):
    status = "current"
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
        *(("draft11n2point4Ghz", 7),
          ("draft11n5Ghz", 8),
          ("dsss", 2),
          ("erp", 6),
          ("fhss", 1),
          ("highRateDsss", 5),
          ("irBaseband", 3),
          ("oFdm", 4),
          ("unused", 0))
    )



class CiscoLwappDot11ClientDataRates(Bits, TextualConvention):
    status = "current"


class CLDot11ClientDiagAssocReason(Integer32, TextualConvention):
    status = "current"
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
        *(("commonEapNegotiationFail", 9),
          ("dhcpFail", 5),
          ("dnsFail", 6),
          ("dot11AssocFail", 3),
          ("dot11AuthFail", 2),
          ("dot1xAuthFail", 8),
          ("executingTest", 11),
          ("ipConnectivityFail", 7),
          ("reconnect", 0),
          ("reserved", 12),
          ("rsnaFail", 4),
          ("unreliableLink", 1),
          ("userInitiatedReasonUnknown", 10))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB",
    **{"CiscoLwappDot11ClientReqStatus": CiscoLwappDot11ClientReqStatus,
       "CiscoLwappDot11ClientSSId": CiscoLwappDot11ClientSSId,
       "CiscoLwappDot11ClientAuthMethod": CiscoLwappDot11ClientAuthMethod,
       "CiscoLwappDot11ClientEAPMethod": CiscoLwappDot11ClientEAPMethod,
       "CiscoLwappDot11ClientKeyMgmtMethod": CiscoLwappDot11ClientKeyMgmtMethod,
       "CiscoLwappDot11ClientEncryptionMethod": CiscoLwappDot11ClientEncryptionMethod,
       "CiscoLwappDot11ClientCredentialType": CiscoLwappDot11ClientCredentialType,
       "CiscoLwappDot11ClientPowerSaveMode": CiscoLwappDot11ClientPowerSaveMode,
       "CiscoLwappDot11ClientTxPowerMode": CiscoLwappDot11ClientTxPowerMode,
       "CiscoLwappDot11ClientRadioType": CiscoLwappDot11ClientRadioType,
       "CiscoLwappDot11ClientDataRates": CiscoLwappDot11ClientDataRates,
       "CLDot11ClientDiagAssocReason": CLDot11ClientDiagAssocReason,
       "ciscoLwappDot11ClientCCXTextualConventions": ciscoLwappDot11ClientCCXTextualConventions}
)
